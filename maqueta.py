"""Fase 1: fábrica real + envolventes A/B/C en planta, alzados e isométrica, y presupuesto de piezas.
Uso: maqueta.py [SAVE]   (por defecto 334c.sav; solo lee). Salida: img/f1_{planta,alzados,iso}.png"""
import sys, math, itertools
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import satisfactory_save as s

AQUI = Path(__file__).parent
SAVE = sys.argv[1] if len(sys.argv) > 1 else str(AQUI / "334c.sav")
OUT = AQUI / "img"
ANILLO = 3251                      # piezas del anillo de 380 m que ya forman el borde del techo
ASCENSOR = (3204, -1482, 382)
MUESTRA = (3092, 3172, -1436, -1436, 338, 378)   # fachada sur de la fase 0 (plana: y0 == y1)
X0, X1, Y0, Y1 = 1548, 3252, -2572, -1436         # planta del anillo de 380 m
COL = {"estructura": "#9aa0a6", "máquina": "#e8710a", "transporte": "#1a73e8"}

# ---- lectura, como vista.py (cm -> m) ----
sg = s.SaveGame(SAVE)
pts = {g: [] for g in COL}
for o in sg.allSaveObjects():
    c = o.BaseHeader.ClassName
    if "Lightweight" in c:
        for v in o.Object.mBuildableClassToInstanceArray.Values:
            pts["estructura"] += [(i.Transform.Translation.X, i.Transform.Translation.Y, i.Transform.Translation.Z) for i in v]
    elif o.isActor and "/Buildable/" in c:
        t = o.Header.Transform.Translation
        if (t.X == 0 and t.Y == 0) or t.Z > 200000:  # restos en el origen y el proyecto del ascensor en el cielo
            continue
        g = ("transporte" if any(k in c for k in ("Conveyor", "Pipe", "PowerLine", "PowerPole", "Wire", "Railroad"))
             else "estructura" if "/Building/" in c else "máquina")  # pasarelas, escaleras... son estructura
        pts[g].append((t.X, t.Y, t.Z))
pts = {g: np.array(v) / 100 for g, v in pts.items()}

# ---- opciones de envolvente: (x0, x1, y0, y1, z0, z1) en m ----
todo = np.vstack(list(pts.values()))
(cx0, cy0), (cx1, cy1) = np.floor(todo[:, :2].min(0) / 8) * 8, np.ceil(todo[:, :2].max(0) / 8) * 8  # a rejilla de 8 m
OPC = {
    "A caja completa": dict(b=(X0, X1, Y0, Y1, 0, 382), col="#d93025", ls="-"),
    "B caja flotante": dict(b=(X0, X1, Y0, Y1, 182, 382), col="#9334e6", ls="--"),
    "C caja + zona este": dict(b=(cx0, cx1, cy0, cy1, 0, 382), col="#188038", ls="-."),
}
CB = OPC["B caja flotante"]["col"]
xs, ys = [*np.arange(X0, X1, 256), X1], [*np.arange(Y0, Y1, 256), Y1]
PILARES = np.array(sorted({(x, y) for x in xs for y in (Y0, Y1)} | {(x, y) for y in ys for x in (X0, X1)}))


def rango(b, vista):  # caja -> ((h0, h1), (v0, v1)) en la vista
    x0, x1, y0, y1, z0, z1 = b
    return {"planta": ((x0, x1), (-y1, -y0)), "sur": ((x0, x1), (z0, z1)), "este": ((-y1, -y0), (z0, z1))}[vista]


def proy(a, vista):  # puntos (N, 3) -> (h, v); planta con el norte (−Y) arriba, alzado este con el norte a la derecha
    a = np.atleast_2d(a)
    return {"planta": (a[:, 0], -a[:, 1]), "sur": (a[:, 0], a[:, 2]), "este": (-a[:, 1], a[:, 2])}[vista]


def dentro(a, b):
    x0, x1, y0, y1, z0, z1 = b
    return int(((a[:, 0] >= x0) & (a[:, 0] <= x1) & (a[:, 1] >= y0) & (a[:, 1] <= y1) & (a[:, 2] >= z0) & (a[:, 2] <= z1)).sum())


# ~20.000 puntos: todas las máquinas y el resto submuestreado
rng = np.random.default_rng(0)
f = min(1, (20000 - len(pts["máquina"])) / (len(pts["estructura"]) + len(pts["transporte"])))
sub = {g: a if g == "máquina" else a[rng.random(len(a)) < f] for g, a in pts.items()}

LEY = [Line2D([], [], ls="", marker="o", ms=6, c=COL[g], label=f"{g} ({len(pts[g]):,})".replace(",", ".")) for g in COL]
LEY += [Line2D([], [], c=o["col"], ls=o["ls"], lw=2, label=n) for n, o in OPC.items()]
LEY += [Line2D([], [], c=CB, marker="s", ls="", label=f"pilares B: {len(PILARES)}, cada 256 m, 0–182 m"),
        Line2D([], [], c="k", marker="*", ms=14, ls="", label="ascensor espacial"),
        Line2D([], [], c="#f9ab00", lw=5, label="muestra de fachada (fase 0)")]


def dibuja(ax, vista, titulo, xl, yl):
    for g, a in sub.items():
        ax.scatter(*proy(a, vista), s=1.5, c=COL[g], alpha=0.5, linewidths=0)
    for o in OPC.values():
        (h0, h1), (v0, v1) = rango(o["b"], vista)
        ax.add_patch(Rectangle((h0, v0), h1 - h0, v1 - v0, fill=False, ec=o["col"], ls=o["ls"], lw=2))
    h, v = proy(np.c_[PILARES, np.zeros(len(PILARES))], vista)
    if vista == "planta":
        ax.scatter(h, v, marker="s", s=30, c=CB, zorder=4)
    else:
        ax.vlines(np.unique(h), 0, 182, colors=CB, lw=1.5)
    ax.scatter(*proy(np.array(ASCENSOR, float), vista), marker="*", s=300, c="k", zorder=5)
    (h0, h1), (v0, v1) = rango(MUESTRA, vista)
    ax.plot([h0, h1, h1, h0, h0], [v0, v0, v1, v1, v0], c="#f9ab00", lw=5, zorder=5)
    ax.set_title(titulo); ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_aspect("equal"); ax.grid(alpha=0.3)


OUT.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(18, 11))
dibuja(ax, "planta", "Planta: fábrica real (334c) y envolventes A/B/C", "X (m) → este", "−Y (m) → norte")
ax.legend(handles=LEY, loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=11)
fig.tight_layout(); fig.savefig(OUT / "f1_planta.png", dpi=110); plt.close(fig)

fig, ax = plt.subplots(1, 2, figsize=(26, 7), gridspec_kw=dict(width_ratios=[cx1 - cx0, cy1 - cy0]))
dibuja(ax[0], "sur", "Alzado sur (mirando al norte)", "X (m) → este", "Z (m)")
dibuja(ax[1], "este", "Alzado este (mirando al oeste)", "−Y (m) → norte", "Z (m)")
fig.legend(handles=LEY, loc="lower center", ncol=5, fontsize=11)
fig.tight_layout(rect=(0, 0.12, 1, 1)); fig.savefig(OUT / "f1_alzados.png", dpi=110); plt.close(fig)

fig = plt.figure(figsize=(16, 11)); ax = fig.add_subplot(projection="3d")
for g, a in sub.items():
    ax.scatter(a[:, 0], -a[:, 1], a[:, 2], s=0.6, c=COL[g], alpha=0.4, linewidths=0, depthshade=False)
for o in OPC.values():
    x0, x1, y0, y1, z0, z1 = o["b"]
    esq = list(itertools.product((x0, x1), (y0, y1), (z0, z1)))
    ar = [(p, q) for p, q in itertools.combinations(esq, 2) if sum(i != j for i, j in zip(p, q)) == 1]
    assert len(ar) == 12  # una caja tiene 12 aristas
    for p, q in ar:
        ax.plot([p[0], q[0]], [-p[1], -q[1]], [p[2], q[2]], c=o["col"], ls=o["ls"], lw=1.6)
for x, y in PILARES:
    ax.plot([x, x], [-y, -y], [0, 182], c=CB, lw=1.2)
ax.scatter([ASCENSOR[0]], [-ASCENSOR[1]], [ASCENSOR[2]], marker="*", s=300, c="k")
mx0, mx1, my, _, mz0, mz1 = MUESTRA
ax.plot([mx0, mx1, mx1, mx0, mx0], [-my] * 5, [mz0, mz0, mz1, mz1, mz0], c="#f9ab00", lw=4)
ax.set_box_aspect((cx1 - cx0, cy1 - cy0, 430)); ax.view_init(elev=28, azim=-60)
ax.set_xlabel("X (m) → este"); ax.set_ylabel("−Y (m) → norte"); ax.set_zlabel("Z (m)")
ax.set_title("Isométrica desde el sureste (escala real, ~20.000 puntos)")
ax.legend(handles=LEY, loc="upper left", fontsize=10)
fig.tight_layout(); fig.savefig(OUT / "f1_iso.png", dpi=110); plt.close(fig)

# ---- presupuesto ----
print(f"C = X {cx0:.0f}–{cx1:.0f}, Y {cy0:.0f}…{cy1:.0f}; pilares B: {len(PILARES)}; máquinas totales: {len(pts['máquina'])}")
print(f"{'opción':20}{'laterales m²':>14}{'techo m²':>12}{'suelo m²':>12}{'paredes 8x4':>13}{'cim. techo*':>13}{'cim. suelo':>12}{'máquinas':>10}")
for n, o in OPC.items():
    x0, x1, y0, y1, z0, z1 = o["b"]
    L, W, H = x1 - x0, y1 - y0, z1 - z0
    nx, ny = math.ceil(L / 8), math.ceil(W / 8)
    print(f"{n:20}{2 * (L + W) * H:>14,.0f}{L * W:>12,.0f}{L * W:>12,.0f}{2 * (nx + ny) * math.ceil(H / 4):>13,}"
          f"{nx * ny - ANILLO:>13,}{nx * ny:>12,}{dentro(pts['máquina'], o['b']):>10}".replace(",", "."))
print(f"* techo menos las {ANILLO} piezas del anillo existente")
