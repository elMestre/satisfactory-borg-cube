"""Fase 0: muestra Borg colgada de la cara sur de la plataforma del ascensor espacial, y mirador provisional para verla desde fuera.
Uso: .venv/bin/python muestra.py [ENTRADA] [SALIDA]   (por defecto 334c.sav → 336.sav)

Panel de 80 × 40 m: 8 filas × 10 columnas de paredes de 8 × 4 m con relieve (0, −1 o −2 m hacia dentro, semilla fija)
y, debajo, un chaflán a 45° de paredes inclinadas de 8 m. Todo con la muestra Slot14 redefinida como "Borg".
La pared inclinada sube hacia su +X local: con giro SUR la arista alta queda fuera, pegada al borde del panel.
Se averiguó con un A/B en el 335.sav que cargó Carlos (columnas 0–4 a 90°, la buena; 5–9 a 270°). Este script ya pone todo a 90°.
Mirador: pasarela de cimientos 8x1 que sale de la plataforma por el oeste del panel (sin taparlo) y balcón a 96 m al sur,
a la altura de la plataforma, en el gris de siempre (Slot16). Es provisional: se quita cuando haya sitio de verdad desde donde mirar.
Rutas y recetas salen de catalogo.json (catalogo.py)."""
import collections, hashlib, json, math, pathlib, random, sys
import numpy as np
import satisfactory_save as s

ENTRADA = sys.argv[1] if len(sys.argv) > 1 else "334c.sav"
SALIDA = sys.argv[2] if len(sys.argv) > 2 else "336.sav"
CAT = {p["clase"]: p for p in json.load(open(pathlib.Path(__file__).with_name("catalogo.json")))["piezas"]}

SLOT = 14  # libre: ninguna pieza ni edificio la usa en el 334c
SWATCH = f"/Game/FactoryGame/Buildable/-Shared/Customization/Swatches/SwatchDesc_Slot{SLOT}.SwatchDesc_Slot{SLOT}_C"
GRIS = "/Game/FactoryGame/Buildable/-Shared/Customization/Swatches/SwatchDesc_Slot16.SwatchDesc_Slot16_C"  # la de sus cimientos
CARBON = "/Game/FactoryGame/Buildable/-Shared/Customization/PaintFinishes/Metals/PaintFinishDesc_CarbonSteel.PaintFinishDesc_CarbonSteel_C"
NEGRO = (0.008, 0.0097, 0.0091, 1.0)  # color lineal, ≈ sRGB 22,25,24
VERDE = (0.021, 0.716, 0.102, 1.0)    # ≈ sRGB 40,220,90

# Geometría en cm. Cimientos 8x4 de la plataforma: centro Y=−144000, Z=38000 (pivote en el centro) → cara sur Y=−143600, base Z=37800.
# Pared: pivote en el centro de la base, 8 m a lo largo del eje local Y, normal en el local X → giro 90° = mira al sur (+Y).
CARA_Y, BASE_Z = -143600, 37800
X0, COLS, FILAS = 309600, 10, 8  # columnas centradas en 3096…3168 m, como los cimientos de encima
SUR = 90

ACERO, HORMIGON = "Build_Wall_8x4_02_C", "Build_Wall_Concrete_8x4_C"
HEX, CHAFLAN = "Build_Wall_Window_Thin_8x4_02_C", "Build_WallSet_Steel_Angular_8x8_C"
# Las paredes de cinta no valen: no son ligeras (son actores con conexiones)
MEZCLA = {ACERO: 6, HORMIGON: 2, "Build_SteelWall_8x4_Gate_01_C": 2, HEX: 1, "Build_Wall_Window_8x4_06_C": 1}


def panel():
    """[(clase, x, y, z, giro, muestra)]: fila 0 enrasada, fila 2 franja de ventanas hundida 1 m, el resto al azar."""
    rnd = random.Random(334)
    out = []
    for f in range(FILAS):
        z = BASE_Z - 400 * (f + 1)
        for c in range(COLS):
            x = X0 + 800 * c
            if f == 0:
                cls, fondo = ACERO, 0
            elif f == 2:
                cls, fondo = HEX, -100
            else:
                cls, fondo = rnd.choices(list(MEZCLA), list(MEZCLA.values()))[0], rnd.choice((0, -100, -200))
            out.append((cls, x, CARA_Y + fondo, z, SUR, SWATCH))
    zc = BASE_Z - 400 * FILAS - 800  # caja de 8 × 8 × 8 m con el pivote en el centro de la base
    out += [(CHAFLAN, X0 + 800 * c, CARA_Y - 400, zc, SUR, SWATCH) for c in range(COLS)]
    return out


def mirador(lejos=12, ancho=13):
    """Pasarela de `lejos`+1 cimientos 8x1 hacia el sur desde la cara de la plataforma, dos columnas al oeste del panel,
    y balcón de `ancho` cimientos hacia el este. Cara superior enrasada con la plataforma (382 m); borde del balcón a 96 m del panel."""
    z, x0, y0 = BASE_Z + 400 - 50, X0 - 1600, CARA_Y + 400  # 8x1: pivote en el centro, 1 m de grueso
    sitios = [(x0, y0 + 800 * k) for k in range(lejos + 1)] + [(x0 + 800 * c, y0 + 800 * lejos) for c in range(1, ancho + 1)]
    return [("Build_Foundation_8x1_01_C", x, y, z, 0, GRIS) for x, y in sitios]


def objeto(sg, sufijo):
    return next(o for o in sg.allSaveObjects() if o.BaseHeader.ClassName.endswith(sufijo))


def instancia(cls, x, y, z, giro, muestra):
    i = s.FRuntimeBuildableInstanceData()
    t = i.Transform
    h = math.radians(giro) / 2
    t.Rotation.X, t.Rotation.Y, t.Rotation.Z, t.Rotation.W = 0.0, 0.0, math.sin(h), math.cos(h)
    t.Translation.X, t.Translation.Y, t.Translation.Z = float(x), float(y), float(z)
    t.Scale3D.X = t.Scale3D.Y = t.Scale3D.Z = 1.0
    i.BuiltWithRecipe.PathName = CAT[cls]["receta"]
    i.CustomizationData.SwatchDesc.PathName = muestra
    i.CustomizationData.OverrideColorData.PrimaryColor.A = 1.0  # como las piezas que pone el juego
    i.CustomizationData.OverrideColorData.SecondaryColor.A = 1.0
    assert (i.Transform.Translation.Z, i.BuiltWithRecipe.PathName) == (float(z), CAT[cls]["receta"]), "la lib no guardó el campo"
    return i


def guardar(sg, ruta):
    """sg.save() deja el nombre interno y la huella del save de entrada; el juego avisa entonces de "save editado".
    Pone el nombre del fichero y recalcula la huella: MD5 de todo lo que sigue a la cabecera."""
    sg.mSaveHeader.SaveName = pathlib.Path(ruta).stem
    sg.save(ruta)
    b = bytearray(pathlib.Path(ruta).read_bytes())
    i = b.find(bytes.fromhex("c1832a9e"))  # primer trozo comprimido = fin de la cabecera
    assert b[i - 24:i - 20] == b"\x01\x00\x00\x00", "cabecera inesperada"  # bIsValid de SaveDataHash
    b[i - 20:i - 4] = hashlib.md5(b[i:]).digest()  # detrás va IsCreativeModeEnabled
    pathlib.Path(ruta).write_bytes(b)


def censo(sg):
    """Todas las piezas ligeras como (ruta de clase, x, y, z, muestra), con repeticiones."""
    m = objeto(sg, "FGLightweightBuildableSubsystem").Object.mBuildableClassToInstanceArray
    return collections.Counter((k.PathName, *(round(getattr(i.Transform.Translation, a)) for a in "XYZ"), i.CustomizationData.SwatchDesc.PathName)
                               for k, v in zip(m.Keys, m.Values) for i in v)


def muestra_borg(sg):
    """Valores de la muestra SLOT tal y como quedan en el save."""
    d = objeto(sg, "BP_BuildableSubsystem_C").Object.Properties[0].Value.Values[SLOT].Data
    p = {q.Name.Name: q.Value for q in d}
    rgba = lambda v: tuple(round(getattr(v.Data, a), 4) for a in "RGBA")
    return rgba(p["PrimaryColor"]), rgba(p["SecondaryColor"]), p["PaintFinish"].PathName


def main():
    piezas = panel() + mirador()
    sg = s.SaveGame(ENTRADA)
    antes, n_objetos = censo(sg), len(sg.allSaveObjects())

    # Solo piezas ligeras y desbloqueadas (como el modo creativo sin piezas bloqueadas)
    desbloqueadas = {r.PathName for r in objeto(sg, "FGRecipeManager").Object.Properties[0].Value.Values}
    for cls in {p[0] for p in piezas}:
        assert CAT[cls]["ligera"] and CAT[cls]["receta"] in desbloqueadas, f"{cls}: no ligera o bloqueada"
    assert any(r.endswith(".Recipe_PaintFinish_CarbonSteel_C") for r in desbloqueadas), "Carbon Steel sin comprar"

    # Nadie usa la muestra y ninguna pieza existente tiene el pivote a menos de 4 m (en los tres ejes) del de una nueva
    assert all(k[4] != SWATCH for k in antes), "la muestra ya está en uso"
    hay = np.array([k[1:4] for k in antes])
    for cls, x, y, z, *_ in piezas:
        assert not (abs(hay - (x, y, z)) < 400).all(axis=1).any(), f"{cls} en ({x}, {y}, {z}) choca con algo que ya existe"
    m = objeto(sg, "FGLightweightBuildableSubsystem").Object.mBuildableClassToInstanceArray

    # Muestra Borg: casi negro + verde, acabado Carbon Steel
    d = objeto(sg, "BP_BuildableSubsystem_C").Object.Properties[0].Value.Values[SLOT].Data
    p = {q.Name.Name: q.Value for q in d}
    for nombre, col in (("PrimaryColor", NEGRO), ("SecondaryColor", VERDE)):
        for a, v in zip("RGBA", col):
            setattr(p[nombre].Data, a, v)
    p["PaintFinish"].PathName = CARBON

    # Clases que el save aún no tiene: clave nueva + vector vacío (Values devuelve copia: hay que reasignarla)
    rutas = {CAT[c]["ruta"] for c, *_ in piezas}
    nuevas = sorted(rutas - {k.PathName for k in m.Keys})
    if nuevas:
        vals = m.Values
        for r in nuevas:
            k = s.FObjectReferenceDisc()
            k.PathName, k.LevelName = r, ""
            m.Keys.append(k)
            vals.append(s.StdVectorFRuntimeBuildableInstanceData())
        m.Values = vals
    idx = {k.PathName: n for n, k in enumerate(m.Keys)}
    for cls, *pos in piezas:
        m.Values[idx[CAT[cls]["ruta"]]].append(instancia(cls, *pos))

    guardar(sg, SALIDA)

    # Comprobación sobre el fichero escrito
    sg2 = s.SaveGame(SALIDA)
    esperado = antes + collections.Counter((CAT[c]["ruta"], x, y, z, sw) for c, x, y, z, _, sw in piezas)
    assert censo(sg2) == esperado, "cambian piezas que no tocaban o las nuevas no están donde tocaba"
    assert len(sg2.allSaveObjects()) == n_objetos and sg2.mSaveHeader.SaveName == pathlib.Path(SALIDA).stem
    assert muestra_borg(sg2) == (tuple(round(v, 4) for v in NEGRO), tuple(round(v, 4) for v in VERDE), CARBON)
    print(f"{SALIDA}: {len(piezas)} piezas nuevas en {len(rutas)} clases ({len(nuevas)} nuevas en el save); muestra {SLOT} = Borg")
    for r, n in sorted(collections.Counter(CAT[c]["nombre"] + " · " + c for c, *_ in piezas).items()):
        print(f"  {n:3d}  {r}")


if __name__ == "__main__":
    main()
