# Carta arquitectónica del cubo Borg (fase 1)

Borrador del 2026-10-23, hecho con datos de `334c.sav` y con lo aprendido en la fase 0 (`img/336_*`, `img/335_*`). Cada punto lleva una propuesta recomendada, sus alternativas y una casilla para la **decisión de Carlos**. Las maquetas son `img/f1_planta.png`, `img/f1_alzados.png` e `img/f1_iso.png` (las genera `maqueta.py`).

## 1. Retícula y alturas
**Datos:** el 99 % de los cimientos 8x4 cae en la rejilla de 8 m en planta y de 4 m en altura. Las plantas con más cimientos son 48 m (2.981), 156 m (2.037), 116 m (1.936), 90 m (1.224), 70–78 m (2.640 entre las dos) y el anillo de 380 m (3.251). Las máquinas se concentran a 50–60 m (133 de 371), y luego a 90–100, 70–80, 30–40 y 110–120 m.
- **Propuesta:** se mantienen la rejilla de 8 m y la altura en múltiplos de 4 m. La fachada se organiza en **módulos de 40 m de alto (10 filas)**, contados hacia abajo desde el techo a 382 m. Las plantas fijas son **48, 92, 116, 156 y 380 m**; lo que se construya a partir de ahora va en ellas, y lo que ya existe no se mueve.
- **Alternativa:** módulos de 32 m (8 filas), como la muestra.
- Decisión de Carlos: ☐

## 2. Envolvente
Las tres opciones de la maqueta (ver `img/f1_*`):

| Opción | Paredes 8×4 | Cimientos de techo (descontado el anillo) | Cimientos de suelo | Total nuevo, aprox. | Máquinas dentro (de 595) |
|---|---|---|---|---|---|
| A, caja completa | 68.160 | 26.995 | (el terreno) | **95.000** | 346 |
| B, caja flotante | 35.500 | 26.995 | 30.246 | 93.000 | 87 |
| C, caja con la zona este | 106.944 | 67.831 | (el terreno) | 175.000 | 565 |

**Lo que enseña la planta (`img/f1_planta.png`):** el interior del anillo está **casi vacío**. La fábrica va pegada a los bordes: el bloque del ascensor al este (X 3.050–3.250), la franja norte y la franja oeste, más la zona este (X 3.700–4.330). Con A, el interior se convierte en un hangar colosal; con B, la caja encierra sobre todo aire (87 máquinas).

- **A, caja completa (recomendada):** la planta del anillo (1.704 × 1.136 m), cerrada desde el suelo hasta el techo a 382 m. El anillo pasa a ser el borde del techo. Es lo que pide "cubo Borg, todo cerrado". El lago y la parte del cañón que quedan al sur (Y > −1436) siguen fuera.
- **B, caja flotante:** la misma planta, de 182 a 382 m, sobre pilares gigantes. La fábrica de 30–160 m quedaría a la vista por debajo, en sombra. Es espectacular, pero encierra aire y deja fuera lo feo.
- **C, caja con la zona este:** envuelve también X 3.250–4.330. Es la más grande; alternativa: cerrar la zona este como un anexo más bajo, en una sección posterior.
- Que sea un cubo de verdad (1.136 m de lado) queda descartado: no cubre la planta del anillo y tendría 1,1 km de alto.
- Decisión de Carlos: ☐ A ☐ B ☐ C ☐ A + anexo este

## 3. Estructura
El juego no tiene física: los pilares son pura estética y ritmo.
- **Propuesta:** costillas en fachada cada 64 m (8 paredes), hechas con Big Concrete Pillar 4 × 4 m apilado, sobresaliendo 4 m de la fachada, y en las esquinas pilares dobles. Dentro, nada nuevo. El andamiaje de pilares finos se retira por secciones (ver punto 8).
- **Alternativa:** sin costillas, solo el relieve de la fachada.
- Decisión de Carlos: ☐

## 4. Fachada (módulo)
**Lecciones de la fase 0:** un relieve de 1–2 m no se lee a 100 m; los huecos enseñan el desorden de detrás; el chaflán a 45° funciona (la pared inclinada sube hacia su +X local); y la coronación también es fachada.
- **Propuesta:** módulo de 64 × 40 m (8 × 10 paredes):
  - **Casi ciego:** pared de acero `Build_Wall_8x4_02`.
  - **Relieve:** a 0 y a −8 m, por franjas. Cada escalón se cierra con cimientos 8x1 como alféizar, porque a −8 m un hueco sin cerrar se ve.
  - **Una franja de ventanas por planta fija**, solo donde haya interior que ver.
  - **Chaflanes:** de 45° en la coronación (`WallSet_Steel_Angular_8x8`) y en las aristas verticales. Las esquinas inclinadas de acero **no son ligeras**; las de FICSIT (`Build_Wall_Orange_8x8_Corner_01`) sí, y se pintan igual con la muestra Borg.
- **Alternativa:** sin franjas de ventana, todo ciego, con la luz verde como única señal de vida.
- Decisión de Carlos: ☐

## 5. Paleta
**Datos:** el verde de la pintura secundaria no se ve en paredes ni ventanas (cero píxeles verdes en las capturas).
- **Propuesta:**
  - **Envolvente:** Slot14 "Borg" (casi negro con Carbon Steel), ya probado.
  - **Costillas y coronación:** Slot15, libre, como grafito algo más claro.
  - **Verde:** solo de las luces.
  - **Maquinaria:** se queda naranja FICSIT, como contraste cálido a través de las ventanas.
- **Alternativa:** repintar Slot0 en bloque. Es reversible: un solo cambio afecta a unas 11.000 piezas y actores.
- Decisión de Carlos: ☐

## 6. Luz
**Datos:**
- **Consumos:** panel de techo (`Build_CeilingLight`) 2 MW; foco de pared o de torre 6 MW; farola 1 MW. Todas son actores, no piezas ligeras, y gastan solo de noche.
- **Light Control Panel:** 7 colores, intensidad y encendido/apagado. Controla como grupo todo lo que cuelga de su conector de luces. Un panel de techo que nunca se ha conectado a un panel sale blanco, y el foco de pared no se colorea por separado.
- **Cómo se guarda una conexión:** el cable (`Build_PowerLine`) guarda sus dos extremos en `mConnections`, y cada conexión lista sus cables en `mWires`. Los circuitos parecen recalcularse al cargar.
- En el 334c **no hay ninguna luz** que sirva de ejemplo.
- **Orden de magnitud:** una franja de paneles de techo cada 16 m por todo el perímetro de A son unas 355 luces, unos 710 MW de noche por franja.

**Propuesta, mixta:**
1. Carlos pone a mano, en una esquina de la sección sur, un Light Control Panel en verde y una luz de cada tipo, cableadas, y guarda.
2. El script copia ese patrón (actor, componentes y cable) a lo largo de la fachada.
3. Si al final son pocas decenas de luces, en vez de eso Carlos las estampa con un blueprint del juego, sin riesgo.

- **Alternativa:** el verde solo con focos de pared, de 6 MW cada uno, desde fuera hacia la fachada.
- Decisión de Carlos: ☐

## 7. Logística
Pendiente del informe de cruces por cara (cintas, tuberías, cables, vías).
- **Propuesta:** todo lo que cruce la envolvente entra por paredes con hueco (Conveyor Wall Hole, comprado), agrupado en "puertas logísticas" de 8 m, y nada queda colgando por fuera.
- Decisión de Carlos: ☐

## 8. Qué se queda y qué se va
Pendiente del recuento de andamiaje dentro y fuera de cada opción.
- **Propuesta:** dentro de la caja se queda todo, porque deja de verse. El andamiaje que quede fuera (pilares finos, pasarelas sueltas, rampas), en cuanto su tramo esté cerrado, se retira. El mirador de la fase 0 se retira cuando haya otro sitio desde el que mirar.
- Decisión de Carlos: ☐

## 9. Presupuesto de piezas y rendimiento
**Datos:** hoy hay 27.851 piezas ligeras. A supone unas 95.000 más (68.160 paredes y 26.995 cimientos de techo): 4,4 veces lo que hay. C, unas 175.000 (7,3 veces). El desglose está en la tabla del punto 2. Con el 336 cargado, la carga de piezas ligeras tarda 0,73 s.
No hay cifras públicas de rendimiento con más de 100.000 piezas ligeras (ni de Coffee Stain ni de la comunidad): habrá que medirlo nosotros.
- **Propuesta:** se construye por secciones, empezando por la cara del ascensor (sur), y tras cada sección se mide el rendimiento (FPS en el mismo sitio y tiempo de carga del log).
- Decisión de Carlos: ☐
