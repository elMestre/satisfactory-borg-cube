"""Fase 2 del cubo "Estrella de la Muerte II" (decisiones en ARQUITECTURA.md) → 338.sav
Uso: .venv/bin/python cubo.py [ENTRADA] [SALIDA]   (por defecto 334c.sav → 338.sav)

- Cara sur bajo la plataforma (X 2988–3252): vitrina de cristal de 50 a 138 m, delante de la fábrica, y encima tres fachadas
  de prueba una al lado de otra, sin azar: monolito (oeste), bandas de ventanas (centro) y costillas (este). Cornisas en
  grafito. Lo que choque (la escalera de mano de X 3200) se descarta y queda abierto.
- Esqueleto en construcción hasta el techo 3:2:1 (568 m): columnas de celosía (Big Frame Pillar, cubos de 4 m) y vigas.
- Ascensor espacial colgado en el centro del cubo (opción B de Carlos): isla de 80 × 80 m con chaflanes por debajo,
  cuatro tirantes de celosía desde sus esquinas al techo, y un hueco cuadrado en la cruz del techo para que la carga suba limpia.
- Corredor modular sobre el puente N–S del anillo (X 2448): paredes, techo y costillas cada 32 m.
- El mirador de la fase 0, para ver la cara sur desde fuera."""
import math, random, sys
import numpy as np
import satisfactory_save as s
import muestra as M

TECHO = 56800                                         # 3:2:1 → 568 m (centro de la última fila de celosía)
X_O, X_E, Y_S, Y_N = 155200, 324800, -144000, -256800  # centros de cimiento del borde del anillo
CENTRO = (240000, -200000, 38200)                     # pivote del ascensor (su cable sale de aquí) sobre el anillo (382 m)
GRAFITO = 15                                          # libre en el 334c
MUESTRAS = {**M.BORG, GRAFITO: ((0.030, 0.032, 0.035, 1.0), M.NEGRO, "")}
VIDRIO, CELOSIA, PILAR = "Build_Wall_Window_Thin_8x4_01_C", "Build_PillarMiddle_Frame_C", "Build_PillarMiddle_Concrete_C"
LOSA, CIMIENTO = "Build_Foundation_8x1_01_C", "Build_Foundation_8x4_01_C"
BAHIAS = list(range(299200, 324801, 800))             # 33 vanos de 8 m bajo la plataforma (centros 2992…3248 m)
PLANTAS = (13800, 17800, 21800, 25800, 29800, 33800)  # líneas de planta cada 40 m contando desde la plataforma (378)
borg, gris, grafito = M.SWATCH, M.GRIS, M.swatch(GRAFITO)


def cara_sur():
    out = []
    pared = lambda cls, x, zb: out.append((cls, x, M.CARA_Y, zb, M.SUR, borg))
    cornisa = lambda x, z: out.append((LOSA, x, M.CARA_Y + 400, z - 50, 0, grafito))
    for i, x in enumerate(BAHIAS):
        variante = i // 11                                # 0 monolito, 1 bandas, 2 costillas
        for zb in range(5000, 37800, 400):
            if zb < PLANTAS[0]:
                pared(VIDRIO, x, zb)                       # vitrina delante de la fábrica (40–130 m)
            elif variante == 1 and zb + 400 in PLANTAS[1:] and zb < 33800:
                pared(M.HEX, x, zb)                        # banda de ventanas bajo cada cornisa
            else:
                pared(M.ACERO, x, zb)
        for z in (PLANTAS if variante < 2 else (PLANTAS[0], PLANTAS[-1])):
            cornisa(x, z)
    # Costillas de la variante este: pilares de hormigón cada 16 m, salientes 4 m, de la vitrina a la plataforma
    for xb in range(317200, 325201, 1600):
        out += [(PILAR, xb, M.CARA_Y + 200, z, 0, grafito) for z in range(14000, 37601, 400)]
    return out


def celosia(x, y, z):
    return (CELOSIA, x, y, z, 0, grafito)


def columna(x, y, z0=38400):
    return [celosia(x, y, z) for z in range(z0, TECHO, 400)]


def isla():
    """Isla de 80 × 80 m bajo el ascensor (cara a 382 m), chaflanes a 45° por debajo de sus bordes, tirantes en las
    esquinas hasta el techo, enlace con el puente N–S y anillo del hueco del techo. Devuelve (piezas, caja del hueco)."""
    xs, ys = range(236000, 243201, 800), range(-204000, -196799, 800)   # centros: X 2360–2432, Y −2040…−1968
    out = [(CIMIENTO, x, y, 38000, 0, borg) for x in xs for y in ys]
    out.append((CIMIENTO, 244000, -200000, 38000, 0, borg))              # enlace con el puente (X 2436–2444)
    zc = 37000                                                           # chaflán: caja de 8 m bajo la cara inferior (378)
    out += [(M.CHAFLAN, x, ys[0], zc, 270, borg) for x in xs] + [(M.CHAFLAN, x, ys[-1], zc, 90, borg) for x in xs]
    out += [(M.CHAFLAN, xs[0], y, zc, 180, borg) for y in ys] + [(M.CHAFLAN, xs[-1], y, zc, 0, borg) for y in ys]
    x0, x1, y0, y1 = xs[0] - 400, xs[-1] + 400, ys[0] - 400, ys[-1] + 400   # bordes: 2356, 2436, −2044, −1964
    out += [c for x in (x0, x1) for y in (y0, y1) for c in columna(x, y, 38000)]     # tirantes, agarrando cada esquina
    out += [celosia(x, y, TECHO) for x in range(x0, x1 + 1, 400) for y in (y0, y1)]
    out += [celosia(x, y, TECHO) for y in range(y0 + 400, y1, 400) for x in (x0, x1)]
    return out, (x0, x1, y0, y1)


def esqueleto(hueco):
    """Columnas de celosía sobre la plataforma (384…564 m) y vigas a 568 m: cara sur del bloque y cruz del techo,
    sin nada dentro del hueco del ascensor."""
    x0, x1, y0, y1 = hueco
    fuera = lambda x, y: not (x0 <= x <= x1 and y0 <= y <= y1)
    out = [c for x in (324800, 317600, 310400, 303200) for c in columna(x, Y_S)]   # cara sur, cada 72 m
    out += [celosia(x, Y_S, TECHO) for x in range(299200, 324801, 400)]             # viga sur del bloque
    out += [celosia(X_E, y, TECHO) for y in range(Y_S - 400, Y_S - 6401, -400)]     # arranque de la viga este
    cx, cy, _ = CENTRO
    out += [celosia(x, cy, TECHO) for x in range(X_O, X_E + 1, 400) if fuera(x, cy)]
    out += [celosia(cx, y, TECHO) for y in range(Y_S, Y_N - 1, -400) if fuera(cx, y)]
    out += [c for x, y in ((X_O, cy), (X_E, cy), (cx, Y_S), (cx, Y_N)) for c in columna(x, y)]
    return out


def corredor(sg, nuevos):
    """Tubo modular sobre el puente N–S (X 2448, cara a 382 m): paredes de 8 m de alto a los dos lados, salvo donde llega
    otro suelo (cruces y el enlace de la isla), techo de losas y costillas de hormigón cada 32 m. Ventana cada 4.º vano."""
    suelo = {(round(x / 100), round(y / 100)) for (c, x, y, z, _s) in M.censo(sg) if "Foundation" in c and abs(z - 38000) < 100}
    suelo |= {(round(x / 100), round(y / 100)) for c, x, y, z, *_ in nuevos if c == CIMIENTO and z == 38000}
    out = []
    for k, y in enumerate(range(Y_N, Y_S + 1, 800)):
        for xw, lado, xp in ((244400, 244000, 244200), (245200, 245600, 245400)):
            if (round(lado / 100), round(y / 100)) in suelo:
                continue
            out.append((M.ACERO, xw, y, 38200, 0, borg))
            out.append((M.HEX if k % 4 == 0 else M.ACERO, xw, y, 38600, 0, borg))
            if k % 4 == 2:
                out += [(PILAR, xp, y, z, 0, grafito) for z in (38400, 38800)]
        out.append((LOSA, 244800, y, 39050, 0, borg))
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
    piezas_isla, hueco = isla()
    hx0, hx1, hy0, hy1 = hueco
    assert hx0 < ex0 and ex1 < hx1 and hy0 < ey0 and ey1 < hy1, "el ascensor no cabe en la isla"
    piezas = cara_sur() + piezas_isla + esqueleto(hueco) + M.mirador()
    piezas += corredor(sg, piezas)
    piezas = list(dict.fromkeys(piezas))
    M.escribir(entrada, salida, piezas, MUESTRAS, retoque=ascensor)
    el = M.objeto(s.SaveGame(salida), "Build_SpaceElevator_C").Header.Transform.Translation
    assert (round(el.X), round(el.Y), round(el.Z)) == CENTRO, "el ascensor no se movió"
    print(f"  ascensor en {tuple(v / 100 for v in CENTRO)} m, giro {giro}°, huella X {ex0 / 100:.0f}–{ex1 / 100:.0f}, "
          f"Y {ey0 / 100:.0f}–{ey1 / 100:.0f}; hueco del techo X {hx0 / 100:.0f}–{hx1 / 100:.0f}, Y {hy0 / 100:.0f}–{hy1 / 100:.0f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "334c.sav", sys.argv[2] if len(sys.argv) > 2 else "338.sav")
