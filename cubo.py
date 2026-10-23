"""Fase 2, sección 1 del cubo "Estrella de la Muerte II" (decisiones en ARQUITECTURA.md) → 337.sav
Uso: .venv/bin/python cubo.py [ENTRADA] [SALIDA]   (por defecto 334c.sav → 337.sav)

- Cara sur bajo la plataforma del antiguo ascensor (X 2988–3252): zócalo ciego (50–98 m), gran acristalado de 240 m
  (98–338 m), coraza Borg (338–378 m) y cornisas en grafito a 98 y 338 m. Lo que choque (la escalera de mano de X 3200)
  se descarta y queda abierto.
- Esqueleto en construcción hasta el techo 3:2:1 (568 m): pilares de celosía (Big Frame Pillar, cubos de 4 m) en la cara
  sur cada 72 m, alineados con los pilares de Carlos en X 3176 y 3248, y vigas de celosía a 568 m.
- GLaDOS: el ascensor espacial pasa al centro del cubo, a 382 m (la línea del anillo), sin cimientos debajo. Su cable al
  espacio atraviesa la cruz de vigas del techo, así que parece colgar de ella. Una pasarela 8x1 lo une al puente N–S del
  anillo (X 2448) para seguir entregando fases.
- El mirador de la fase 0, para verlo desde fuera."""
import math, random, sys
import numpy as np
import satisfactory_save as s
import muestra as M

TECHO = 56800                                       # 3:2:1 → 568 m (centro de la última fila de celosía)
X_O, X_E, Y_S, Y_N = 155200, 324800, -144000, -256800  # centros de cimiento del borde del anillo
CENTRO = (240000, -200000, 38200)                   # centro del cubo en la rejilla de 8 m, sobre el anillo (382 m)
GRAFITO = 15                                        # libre en el 334c
MUESTRAS = {**M.BORG, GRAFITO: ((0.030, 0.032, 0.035, 1.0), M.NEGRO, "")}
VIDRIO, CELOSIA, LOSA = "Build_Wall_Window_Thin_8x4_01_C", "Build_PillarMiddle_Frame_C", "Build_Foundation_8x1_01_C"
BAHIAS = range(299200, 324801, 800)                 # 33 vanos de 8 m bajo la plataforma (centros 2992…3248 m)


def cara_sur():
    rnd, out = random.Random(337), []
    coraza = {M.ACERO: 6, M.HORMIGON: 3, M.HEX: 1}
    for x in BAHIAS:
        for zb in range(5000, 37800, 400):          # filas de 4 m entre la planta de 48 m (cara a 50) y la plataforma (378)
            if zb < 9800:
                cls, y = M.ACERO, M.CARA_Y          # zócalo
            elif zb < 33800:
                cls, y = VIDRIO, M.CARA_Y           # gran acristalado
            else:
                cls, y = rnd.choices(list(coraza), list(coraza.values()))[0], M.CARA_Y + rnd.choice((0, -100, -200))
            out.append((cls, x, y, zb, M.SUR, M.SWATCH))
    out += [(LOSA, x, M.CARA_Y + 400, z - 50, 0, M.swatch(GRAFITO)) for z in (9800, 33800) for x in BAHIAS]  # cornisas
    return out


def celosia(x, y, z):
    return (CELOSIA, x, y, z, 0, M.swatch(GRAFITO))


def esqueleto():
    """Columnas de celosía sobre la plataforma (384…564 m) y vigas a 568 m: cara sur del bloque y cruz del techo."""
    col = lambda x, y: [celosia(x, y, z) for z in range(38400, TECHO, 400)]
    out = [c for x in (324800, 317600, 310400, 303200) for c in col(x, Y_S)]       # cara sur, cada 72 m
    out += [celosia(x, Y_S, TECHO) for x in range(299200, 324801, 400)]             # viga sur del bloque
    out += [celosia(X_E, y, TECHO) for y in range(Y_S - 400, Y_S - 6401, -400)]     # arranque de la viga este
    # Cruz del techo por el centro, con sus cuatro columnas en el borde del anillo
    cx, cy, _ = CENTRO
    out += [celosia(x, cy, TECHO) for x in range(X_O, X_E + 1, 400)]
    out += [celosia(cx, y, TECHO) for y in range(Y_S, Y_N - 1, -400) if y != cy]
    out += [c for x, y in ((X_O, cy), (X_E, cy), (cx, Y_S), (cx, Y_N)) for c in col(x, y)]
    return list(dict.fromkeys(out))                                                 # sin repetir cruces


def huella_ascensor(x, y, giro):
    """Caja XY (cm) del ascensor espacial en (x, y) con ese giro, según sus cajas de holgura del catálogo
    (base, tres patas de 26,5 m y el cable al espacio)."""
    cajas = [((-750, -2150), (750, 2150), (1500, 0), 0), ((-850, 0), (850, 2650), (0, 0), 30), ((-850, 0), (850, 2650), (0, 0), 150),
             ((-850, 0), (850, 2650), (0, 0), -90), ((-800, -800), (800, 800), (-2000, 0), 0)]
    pts = []
    for (x0, y0), (x1, y1), (tx, ty), rot in cajas:
        for px, py in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
            a = math.radians(rot)
            qx, qy = px * math.cos(a) - py * math.sin(a) + tx, px * math.sin(a) + py * math.cos(a) + ty
            g = math.radians(giro)
            pts.append((x + qx * math.cos(g) - qy * math.sin(g), y + qx * math.sin(g) + qy * math.cos(g)))
    p = np.array(pts)
    return p.min(axis=0), p.max(axis=0)


def ascensor(sg):
    """Mueve el ascensor espacial al centro del cubo. Devuelve su giro."""
    el = M.objeto(sg, "Build_SpaceElevator_C")
    t, q = el.Header.Transform.Translation, el.Header.Transform.Rotation
    t.X, t.Y, t.Z = map(float, CENTRO)
    return round(math.degrees(2 * math.atan2(q.Z, q.W))) % 360


def pasarela(giro):
    """Losas 8x1 desde el puente N–S del anillo (X 2448, borde oeste en 2444) hasta el borde este del ascensor."""
    (_, _), (xmax, _) = huella_ascensor(CENTRO[0], CENTRO[1], giro)
    xs = range(244000, int(xmax) - 400, -800)
    return [(LOSA, x, CENTRO[1], CENTRO[2] - 50, 0, M.GRIS) for x in xs]


def main(entrada, salida):
    giro = round(math.degrees(2 * math.atan2(*(lambda q: (q.Z, q.W))(M.objeto(s.SaveGame(entrada), "Build_SpaceElevator_C").Header.Transform.Rotation)))) % 360
    (x0, y0), (x1, y1) = huella_ascensor(CENTRO[0], CENTRO[1], giro)
    assert x1 < 244000, f"el ascensor llegaría al puente N–S (borde este en {x1 / 100:.0f} m)"
    piezas = cara_sur() + esqueleto() + pasarela(giro) + M.mirador()
    M.escribir(entrada, salida, piezas, MUESTRAS, retoque=ascensor)
    el = M.objeto(s.SaveGame(salida), "Build_SpaceElevator_C").Header.Transform.Translation
    assert (round(el.X), round(el.Y), round(el.Z)) == CENTRO, "el ascensor no se movió"
    print(f"  ascensor en {tuple(v / 100 for v in CENTRO)} m, giro {giro}°, huella X {x0 / 100:.0f}–{x1 / 100:.0f}, Y {y0 / 100:.0f}–{y1 / 100:.0f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "334c.sav", sys.argv[2] if len(sys.argv) > 2 else "337.sav")
