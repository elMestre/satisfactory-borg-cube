"""Fase 2 del cubo "Estrella de la Muerte II" (decisiones en ARQUITECTURA.md) → 339.sav
Uso: .venv/bin/python cubo.py [ENTRADA] [SALIDA]   (por defecto 334c.sav → 339.sav)

- Cara sur bajo la plataforma (X 2988–3252): vitrina de cristal de 50 a 138 m, delante de la fábrica, y encima pared ciega
  con costillas de hormigón cada 16 m (la variante que eligió Carlos en el 338), cornisas en grafito a 138 y 338 m.
  Lo que choque (la escalera de mano de X 3200) se descarta y queda abierto.
- Esqueleto en construcción hasta el techo 3:2:1 (568 m): columnas de celosía (Big Frame Pillar, cubos de 4 m) y vigas.
- Sala del ascensor en pirámide invertida (Carlos, tras el 338): el ascensor sobre una isla de 80 × 80 m en el centro del
  cubo, y desde sus bordes un embudo de paredes inclinadas a 45° hasta el techo, con la boca (448 m) abierta al cielo.
- Corredor sobre el puente N–S (X 2448), dos diseños abiertos para comparar: galería de cristal con pórticos (tramo norte)
  y puente de celosía con pretil (tramo sur). Bajo el embudo el puente pasa a cubierto.
- El mirador de la fase 0, para ver la cara sur desde fuera."""
import math, sys
import numpy as np
import satisfactory_save as s
import muestra as M

TECHO = 56800                                         # 3:2:1 → 568 m (centro de la última fila de celosía)
X_O, X_E, Y_S, Y_N = 155200, 324800, -144000, -256800  # centros de cimiento del borde del anillo
CENTRO = (240000, -200000, 38200)                     # pivote del ascensor (su cable sale de aquí) sobre el anillo (382 m)
GRAFITO = 15                                          # libre en el 334c
MUESTRAS = {**M.BORG, GRAFITO: ((0.030, 0.032, 0.035, 1.0), M.NEGRO, "")}
VIDRIO, CELOSIA, PILAR = "Build_Wall_Window_Thin_8x4_01_C", "Build_PillarMiddle_Frame_C", "Build_PillarMiddle_Concrete_C"
LOSA, CIMIENTO, PRETIL = "Build_Foundation_8x1_01_C", "Build_Foundation_8x4_01_C", "Build_SteelWall_8x1_C"
BAHIAS = list(range(299200, 324801, 800))             # 33 vanos de 8 m bajo la plataforma (centros 2992…3248 m)
ISLA = (235600, 243600, -204400, -196400)             # bordes de la isla: X 2356–2436, Y −2044…−1964
NIVELES = 23                                          # escalones de 8 m del embudo: de 382 a 566 m
PUENTE_X = 244800                                     # puente N–S del anillo
borg, gris, grafito = M.SWATCH, M.GRIS, M.swatch(GRAFITO)


def cara_sur():
    out = []
    for x in BAHIAS:
        for zb in range(5000, 37800, 400):
            out.append((VIDRIO if zb < 13800 else M.ACERO, x, M.CARA_Y, zb, M.SUR, borg))   # vitrina hasta 138 m
        out += [(LOSA, x, M.CARA_Y + 400, z - 50, 0, grafito) for z in (13800, 33800)]       # cornisas
    # Costillas: pilares de hormigón cada 16 m desde la esquina este, salientes 4 m, de 50 a 378 m
    for xb in range(325200, 298799, -1600):
        out += [(PILAR, xb, M.CARA_Y + 200, z, 0, grafito) for z in range(5200, 37601, 400)]
    return out


def celosia(x, y, z):
    return (CELOSIA, x, y, z, 0, grafito)


def columna(x, y, z0=38400):
    return [celosia(x, y, z) for z in range(z0, TECHO, 400)]


def isla():
    """Isla de 80 × 80 m bajo el ascensor (cara a 382 m), chaflanes a 45° por debajo de sus bordes y enlace con el puente."""
    x0, x1, y0, y1 = ISLA
    xs, ys = range(x0 + 400, x1, 800), range(y0 + 400, y1, 800)
    out = [(CIMIENTO, x, y, 38000, 0, borg) for x in xs for y in ys]
    out.append((CIMIENTO, x1 + 400, CENTRO[1], 38000, 0, borg))         # enlace con el puente (X 2436–2444)
    zc = 37000                                                          # chaflán: caja de 8 m bajo la cara inferior (378)
    out += [(M.CHAFLAN, x, ys[0], zc, 270, borg) for x in xs] + [(M.CHAFLAN, x, ys[-1], zc, 90, borg) for x in xs]
    out += [(M.CHAFLAN, xs[0], y, zc, 180, borg) for y in ys] + [(M.CHAFLAN, xs[-1], y, zc, 0, borg) for y in ys]
    return out


def embudo():
    """Pirámide invertida: anillos de paredes inclinadas a 45° (suben hacia su +X local, ver PLAN.md) desde los bordes de
    la isla. El nivel k sube de 382 + 8k a 390 + 8k m y se aleja 8k m del borde; cada lado se alarga por las esquinas, donde
    se cruza con el de al lado. Devuelve (piezas, boca)."""
    x0, x1, y0, y1 = ISLA
    out = []
    for k in range(NIVELES):
        d, z, e = 800 * k + 400, 38200 + 800 * k, 800 * (k + 1)
        xs, ys = range(x0 - e + 400, x1 + e, 800), range(y0 - e + 400, y1 + e, 800)
        out += [(M.CHAFLAN, x, y0 - d, z, 270, borg) for x in xs] + [(M.CHAFLAN, x, y1 + d, z, 90, borg) for x in xs]
        out += [(M.CHAFLAN, x0 - d, y, z, 180, borg) for y in ys]
        out += [(M.CHAFLAN, x1 + d, y, z, 0, borg) for y in ys if k or y != CENTRO[1]]   # sin tapar el enlace con el puente
    e = 800 * NIVELES
    return out, (x0 - e, x1 + e, y0 - e, y1 + e)


def esqueleto(boca):
    """Columnas de celosía sobre la plataforma (384…564 m) y vigas a 568 m: cara sur del bloque y cruz del techo,
    que se para en el borde de la boca del embudo."""
    x0, x1, y0, y1 = boca
    fuera = lambda x, y: not (x0 <= x <= x1 and y0 <= y <= y1)
    out = [c for x in (324800, 317600, 310400, 303200) for c in columna(x, Y_S)]   # cara sur, cada 72 m
    out += [celosia(x, Y_S, TECHO) for x in range(299200, 324801, 400)]             # viga sur del bloque
    out += [celosia(X_E, y, TECHO) for y in range(Y_S - 400, Y_S - 6401, -400)]     # arranque de la viga este
    cx, cy, _ = CENTRO
    out += [celosia(x, cy, TECHO) for x in range(X_O, X_E + 1, 400) if fuera(x, cy)]
    out += [celosia(cx, y, TECHO) for y in range(Y_S, Y_N - 1, -400) if fuera(cx, y)]
    out += [c for x, y in ((X_O, cy), (X_E, cy), (cx, Y_S), (cx, Y_N)) for c in columna(x, y)]
    return out


def corredor(sg, nuevos, boca):
    """Dos diseños abiertos sobre el puente N–S (cara a 382 m), fuera de la planta del embudo. Sin pared donde llega otro suelo.
    - Norte: galería de cristal (Full Frame Window, 8 m de alto) con pórticos de celosía en U cada 16 m.
    - Sur: puente de celosía: pretil de 1 m y viga de celosía de 8 m de canto bajo el tablero."""
    suelo = {(round(x / 100), round(y / 100)) for (c, x, y, z, _s) in M.censo(sg) if "Foundation" in c and abs(z - 38000) < 100}
    suelo |= {(round(x / 100), round(y / 100)) for c, x, y, z, *_ in nuevos if c == CIMIENTO and z == 38000}
    _, _, by0, by1 = boca
    out = []
    for k, y in enumerate(range(Y_N, Y_S + 1, 800)):
        if by0 - 400 <= y <= by1 + 400:
            continue                                                    # bajo el embudo
        lados = [(PUENTE_X + s_ * 400, PUENTE_X + s_ * 800, PUENTE_X + s_ * 600) for s_ in (-1, 1)]   # pared, vecino, pórtico
        abiertos = [l for l in lados if (round(l[1] / 100), round(y / 100)) not in suelo]
        if y < by0:                                                     # tramo norte: galería
            for xw, _, _ in abiertos:
                out += [(VIDRIO, xw, y, z, 0, borg) for z in (38200, 38600)]
            if k % 2 == 0:
                out += [celosia(xp, y, z) for _, _, xp in abiertos for z in (38400, 38800)]
                out += [celosia(x, y, 39200) for x in range(PUENTE_X - 600, PUENTE_X + 601, 400)]
        else:                                                           # tramo sur: celosía
            out += [(PRETIL, xw, y, 38200, 0, borg) for xw, _, _ in abiertos]
            out += [celosia(x, y, z) for x in (PUENTE_X - 200, PUENTE_X + 200) for z in (37600, 37200)]
    return out


def ascensor(sg):
    """Mueve el ascensor espacial al centro del cubo."""
    t = M.objeto(sg, "Build_SpaceElevator_C").Header.Transform.Translation
    t.X, t.Y, t.Z = map(float, CENTRO)


def huella_ascensor(giro):
    """Caja XY (cm) del ascensor en el centro, con la caja de holgura del catálogo."""
    (lx0, ly0, _), (lx1, ly1, _) = M.CAT["Build_SpaceElevator_C"]["caja_m"]
    g = math.radians(giro)
    p = np.array([(CENTRO[0] + 100 * (x * math.cos(g) - y * math.sin(g)), CENTRO[1] + 100 * (x * math.sin(g) + y * math.cos(g)))
                  for x in (lx0, lx1) for y in (ly0, ly1)])
    return p.min(axis=0), p.max(axis=0)


def main(entrada, salida):
    sg = s.SaveGame(entrada)
    q = M.objeto(sg, "Build_SpaceElevator_C").Header.Transform.Rotation
    giro = round(math.degrees(2 * math.atan2(q.Z, q.W))) % 360
    (ex0, ey0), (ex1, ey1) = huella_ascensor(giro)
    x0, x1, y0, y1 = ISLA
    assert x0 < ex0 and ex1 < x1 and y0 < ey0 and ey1 < y1, "el ascensor no cabe en la isla"
    piezas_embudo, boca = embudo()
    piezas = cara_sur() + isla() + piezas_embudo + esqueleto(boca) + M.mirador()
    piezas += corredor(sg, piezas, boca)
    piezas = list(dict.fromkeys(piezas))
    M.escribir(entrada, salida, piezas, MUESTRAS, retoque=ascensor)
    el = M.objeto(s.SaveGame(salida), "Build_SpaceElevator_C").Header.Transform.Translation
    assert (round(el.X), round(el.Y), round(el.Z)) == CENTRO, "el ascensor no se movió"
    print(f"  ascensor en {tuple(v / 100 for v in CENTRO)} m, giro {giro}°, huella X {ex0 / 100:.0f}–{ex1 / 100:.0f}, "
          f"Y {ey0 / 100:.0f}–{ey1 / 100:.0f}; boca del embudo X {boca[0] / 100:.0f}–{boca[1] / 100:.0f}, Y {boca[2] / 100:.0f}–{boca[3] / 100:.0f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "334c.sav", sys.argv[2] if len(sys.argv) > 2 else "339.sav")
