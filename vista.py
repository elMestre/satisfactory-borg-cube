"""Planta y alzados de una partida: estructura (lightweight) vs máquinas.
Uso: vista.py 334.sav salida.png"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import satisfactory_save as s

sg = s.SaveGame(sys.argv[1])
groups = {"suelo": [], "pared": [], "pilar": [], "máquina": [], "transporte": []}
for o in sg.allSaveObjects():
    c = o.BaseHeader.ClassName
    if "Lightweight" in c:
        m = o.Object.mBuildableClassToInstanceArray
        for k, v in zip(m.Keys, m.Values):
            n = k.PathName
            g = "pared" if "Wall" in n or "Fence" in n else "pilar" if "Pillar" in n else "suelo"
            groups[g] += [(i.Transform.Translation.X, i.Transform.Translation.Y, i.Transform.Translation.Z) for i in v]
    elif o.isActor and "/Buildable/" in c:
        t = o.Header.Transform.Translation
        if (t.X == 0 and t.Y == 0) or t.Z > 200000:  # restos en el origen y el proyecto del ascensor en el cielo
            continue
        g = "transporte" if any(k in c for k in ("Conveyor", "Pipe", "PowerLine", "PowerPole", "Wire", "Railroad")) else "máquina"
        groups[g].append((t.X, t.Y, t.Z))

col = {"suelo": "#9aa0a6", "pared": "#5f6368", "pilar": "#c58af9", "máquina": "#e8710a", "transporte": "#1a73e8"}
fig, ax = plt.subplots(1, 3, figsize=(24, 8))
for g, pts in groups.items():
    if not pts:
        continue
    a = np.array(pts) / 100  # cm -> m
    kw = dict(s=1, c=col[g], label=f"{g} ({len(a)})", alpha=0.5, linewidths=0)
    ax[0].scatter(a[:, 0], -a[:, 1], **kw)  # planta: norte arriba
    ax[1].scatter(a[:, 0], a[:, 2], **kw)   # alzado mirando al norte
    ax[2].scatter(-a[:, 1], a[:, 2], **kw)  # alzado mirando al oeste
for a_, t in zip(ax, ("Planta (m, norte arriba)", "Alzado: X–altura (m)", "Alzado: Y–altura (m)")):
    a_.set_title(t); a_.set_aspect("equal"); a_.grid(alpha=0.3)
ax[0].legend(markerscale=10)
fig.tight_layout()
fig.savefig(sys.argv[2], dpi=110)

allp = np.array([p for v in groups.values() for p in v]) / 100
print("extensión m: X", allp[:, 0].min().round(), allp[:, 0].max().round(),
      "Y", allp[:, 1].min().round(), allp[:, 1].max().round(),
      "Z", allp[:, 2].min().round(), allp[:, 2].max().round())
