"""Catálogo de piezas construibles → catalogo.json, una pieza por línea:
clase, ruta (tal cual va en el save), nombre del juego, tipo, ligera (mManagedByLightweightBuildableSubsystem: va en
FGLightweightBuildableSubsystem y no como actor), medidas (m), menú, receta y si está desbloqueada.
Uso: .venv/bin/python catalogo.py [SAVE]   (SAVE da las recetas desbloqueadas y las parejas clase-receta reales; por defecto 334c.sav)
Fuentes: Docs/en-US.json del juego (nombres, medidas, recetas) y el índice del .utoc (ruta de cada asset)."""
import json, re, struct, sys
import satisfactory_save as s

GAME = "/home/carlos/.local/share/Steam/steamapps/common/Satisfactory"
UTOC = GAME + "/FactoryGame/Content/Paks/FactoryGame-Windows.utoc"
DOCS = GAME + "/CommunityResources/Docs/en-US.json"
NONE = 0xFFFFFFFF


def assets(path=UTOC):
    """{nombre_asset en minúsculas: [ruta /Game/...]} leyendo el índice de directorios del .utoc (IoStore v8, sin cifrar)."""
    b = open(path, "rb").read()
    assert b[:16] == b"-==--==--==--==-" and b[16] == 8, "formato de .utoc no previsto"
    n, nblk, _, ncm, cmlen, _, dirsize = struct.unpack_from("<7I", b, 24)
    flags, nseeds, nwithout = b[80], struct.unpack_from("<I", b, 84)[0], struct.unpack_from("<I", b, 96)[0]
    assert flags & 0b1000 and not flags & 0b10, "índice ausente o cifrado"
    o = 144 + n * 22 + (nseeds + nwithout) * 4 + nblk * 12 + ncm * cmlen
    if flags & 0b100:  # firmado: dos firmas y un SHA1 por bloque
        h = struct.unpack_from("<i", b, o)[0]
        o += 4 + 2 * h + nblk * 20
    d, p = memoryview(b)[o:o + dirsize], 0

    def i32():
        nonlocal p
        p += 4
        return struct.unpack_from("<i", d, p - 4)[0]

    def fstr():
        nonlocal p
        k = i32()
        raw = bytes(d[p:p + (k if k >= 0 else -2 * k)])
        p += len(raw)
        return (raw.decode("latin-1") if k >= 0 else raw.decode("utf-16-le")).rstrip("\0")

    def arr(fmt):
        nonlocal p
        k, sz = i32(), struct.calcsize(fmt)
        p += k * sz
        return [struct.unpack_from(fmt, d, p - (k - i) * sz) for i in range(k)]

    mount = fstr()
    dirs, files = arr("<4I"), arr("<3I")
    names = [fstr() for _ in range(i32())]
    out, stack = {}, [(0, mount.rstrip("/"))]
    while stack:
        i, pre = stack.pop()
        name, child, sib, f = dirs[i]
        here = pre if name == NONE else f"{pre}/{names[name]}"
        while f != NONE:
            fn, f, _ = files[f]
            if names[fn].endswith(".uasset"):
                out.setdefault(names[fn][:-7].lower(), []).append(game_path(f"{here}/{names[fn][:-7]}"))
        if child != NONE:
            stack.append((child, here))
        if sib != NONE:
            stack.append((sib, pre))
    return out


def game_path(p):
    """../../../FactoryGame/Content/X → /Game/X ; …/Plugins/…/<Plugin>/Content/X → /<Plugin>/X"""
    head, _, tail = p.partition("/Content/")
    root = head.rsplit("/", 1)[-1]
    return f"/{'Game' if root == 'FactoryGame' else root}/{tail}"


def tokens(name, prefix):
    return sorted(name.lower().removeprefix(prefix.lower()).removesuffix("_c").split("_"))


def main(save):
    docs = json.loads(open(DOCS, encoding="utf-16").read())
    sec = {x["NativeClass"].split(".")[-1].rstrip("'"): x["Classes"] for x in docs}
    paths = assets()

    # Parejas clase-receta reales del save y recetas desbloqueadas
    sg = s.SaveGame(save)
    truth, unlocked = {}, set()
    for o in sg.allSaveObjects():
        c = o.BaseHeader.ClassName
        if c.endswith("FGLightweightBuildableSubsystem"):
            m = o.Object.mBuildableClassToInstanceArray
            for k, v in zip(m.Keys, m.Values):
                for i in v:
                    truth.setdefault(i.BuiltWithRecipe.PathName, set()).add(k.PathName)
        elif c.endswith("FGRecipeManager"):
            unlocked = {r.PathName for r in o.Object.Properties[0].Value.Values}
        elif o.isActor and "/Buildable/" in c:
            for prop in o.Object.Properties:
                if prop.Name.Name == "mBuiltWithRecipe":
                    truth.setdefault(prop.Value.PathName, set()).add(c)

    # Receta de la pistola de construcción → descriptor → clase Build_
    shown = {}
    for classes in sec.values():
        for c in classes:
            if c["ClassName"].startswith("Build_"):
                shown.setdefault(c.get("mDisplayName"), []).append(c["ClassName"].removesuffix("_C").lower())
    menu = {c["ClassName"]: re.search(r"SC_(\w+?)_C", c.get("mSubCategories", "")) for c in sec["FGBuildingDescriptor"]}
    build_of, unresolved = {}, []
    for r in sec["FGRecipe"]:
        if "BuildGun" not in r["mProducedIn"]:
            continue
        rpath = r["FullName"].split(" ", 1)[1]
        desc = re.search(r"'(/[^']+?)'", r["mProduct"]).group(1)
        folder, dname = desc.rsplit(".", 1)[0].rsplit("/", 1)
        if rpath in truth and len(truth[rpath]) == 1:
            bcls = next(iter(truth[rpath])).rsplit(".", 1)[1]
        else:
            # Mismo nombre salvo el orden de las partes (Desc_X_8x4_FlipTris → Build_X_FlipTris_8x4); si no, misma carpeta y mismo nombre visible
            want = tokens(dname, "Desc_")
            cands = [q for name, qs in paths.items() if name.startswith("build_") and tokens(name, "build_") == want for q in qs]
            same = [q for q in cands if q.rsplit("/", 1)[0] == folder]
            pick = same if len(same) == 1 else cands if len(cands) == 1 else None
            if not pick:
                pick = [p for c in shown.get(r["mDisplayName"], []) for p in paths[c] if p.rsplit("/", 1)[0] == folder]
                pick = pick if len(pick) == 1 else None
            if not pick:
                unresolved.append((r["ClassName"], dname, cands))
                continue
            bcls = pick[0].rsplit("/", 1)[1] + "_C"
        m_ = menu.get(dname + "_C")
        build_of.setdefault(bcls.lower(), []).append((rpath, m_.group(1) if m_ else None))

    pieces = []
    for kind, classes in sec.items():
        for c in classes:
            cls = c["ClassName"]
            if not cls.startswith("Build_"):
                continue
            ps = paths.get(cls.removesuffix("_C").lower(), [])
            assert len(ps) == 1, f"{cls}: {len(ps)} rutas en el .utoc"
            dims = {}
            for f in ("mWidth", "mDepth", "mHeight", "mElevation", "mAngularDepth", "mSize"):
                if f in c:
                    nums = [round(float(x) / 100, 3) for x in re.findall(r"-?\d+\.\d+", c[f])]
                    dims[f[1:]] = nums[0] if len(nums) == 1 else nums
            recs = build_of.get(cls.lower(), [])
            pieces.append({
                "clase": cls, "ruta": f"{ps[0]}.{cls}", "nombre": c.get("mDisplayName", ""),
                "tipo": kind, "ligera": c.get("mManagedByLightweightBuildableSubsystem") == "True", "medidas_m": dims,
                "menu": recs[0][1] if recs else None,
                "receta": recs[0][0] if recs else None,
                "desbloqueada": bool(recs) and recs[0][0] in unlocked,
                **({"otras_recetas": [x[0] for x in recs[1:]]} if len(recs) > 1 else {}),
            })
    pieces.sort(key=lambda x: (x["tipo"], x["clase"]))
    with open("catalogo.json", "w") as f:
        f.write('{"fuente": ' + json.dumps({"docs": DOCS, "utoc": UTOC, "desbloqueos": save}, ensure_ascii=False))
        f.write(',\n "piezas": [\n' + ",\n".join(json.dumps(p, ensure_ascii=False) for p in pieces) + "\n]}\n")
    print(len(pieces), "piezas;", sum(p["receta"] is not None for p in pieces), "con receta;",
          sum(p["desbloqueada"] for p in pieces), "desbloqueadas")
    for u in unresolved:
        print("sin clase:", u)
    return pieces


if __name__ == "__main__":
    pieces = main(sys.argv[1] if len(sys.argv) > 1 else "334c.sav")
    by = {p["clase"]: p for p in pieces}
    # Comprobaciones con clases ya vistas en el save
    assert by["Build_Wall_8x4_01_C"]["ruta"] == "/Game/FactoryGame/Buildable/Building/Wall/Build_Wall_8x4_01.Build_Wall_8x4_01_C"
    assert by["Build_Wall_Orange_FlipTris_8x4_C"]["receta"].endswith("Recipe_Wall_Orange_FlipTris_8x4_C")
    assert by["Build_Ramp_8x4_01_C"]["desbloqueada"]
    assert not by["Build_Wall_Conveyor_8x4_01_Steel_C"]["ligera"] and by["Build_Beam_C"]["ligera"]  # el flag manda, no la sección
    assert by["Build_PipelinePumpMk2_C"]["ruta"] == "/Game/FactoryGame/Buildable/Factory/PipePumpMk2/Build_PipelinePumpMK2.Build_PipelinePumpMk2_C"
