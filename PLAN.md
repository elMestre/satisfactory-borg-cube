# Cubo Borg en Satisfactory: plan

**Estado (2026-10-23):** el método para escribir piezas en el save funciona y está probado (saves 335–342 cargan sin errores). El diseño a ciegas no: cada versión era una apuesta que Carlos tenía que cargar y fotografiar. **Siguiente paso: Carlos diseña un módulo en el juego y el script lo multiplica** (ver al final).

## Qué es
La partida *elMestre* de Carlos funciona pero es fea: losas a alturas sueltas, pilares finos y máquinas y cintas al aire. La idea es convertirla en un cubo estilo Borg, generando la arquitectura por script dentro de saves nuevos sin tocar la producción.

## Decisiones de Carlos (vigentes)
- **Concepto "Estrella de la Muerte II":** cerrar y embellecer lo que ya existe y dejar el cubo *en construcción*, con el esqueleto a la vista. No hace falta un cubo perfecto.
- **Proporción 3:2:1:** la planta del anillo mide 1.704 × 1.136 m (3:2 exacto) y el techo final va a 568 m. El anillo actual de 380 m queda a 2/3 de la altura. (La alternativa áurea sería un techo a 616 m.)
- **Fachada:** costillas verticales (pilares cada 16 m). Cada planta puede ser distinta, y se reserva un gran espacio acristalado.
- **Ascensor espacial en el centro**, dentro de una sala inmensa en pirámide invertida, con sitio para que lleguen muchas cintas, y sin que cuelgue en el aire.
- **Corredores:** acristalados y con poca estructura.
- **Luz:** aplazada (la decido yo). El verde vendrá de las luces.
- **Reglas:** aprovechar lo que hay, trabajar por secciones y usar solo piezas desbloqueadas (ver la memoria `carlos-forma-de-trabajar`).

## Gusto de Carlos (visto en el juego)
- **Sí:**
  - las costillas verticales;
  - la ranura abierta con la escalera de mano a la vista ("genial"): un motivo a repetir;
  - la vitrina de cristal donde se ve la fábrica;
  - la sala grande alrededor del ascensor;
  - el chaflán a 45° en los bordes inferiores.
- **No:**
  - el relieve aleatorio (se lee como ruido);
  - las cajas cerradas que no dejan ver;
  - el exceso de vigas ("agobia");
  - cosas flotando;
  - las esquinas del embudo (escalonadas o con pared de esquina);
  - la fachada lisa sin más ("aceptable, no bien ni bonito").

## Lo que sabemos (comprobado)
**Partida.** Juego v1.2.4.1, build 513885, SaveVersion 60. Lib `satisfactory-save` 0.11.0 en `.venv` (Python 3.14). La base es `334c.sav` (el 334 más la compra AWESOME de paredes de acero, luces, Carbon Steel y vigas). Los saves del juego están en `~/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/76561197962144663/`, y las capturas (F12) en `~/.local/share/Steam/userdata/1878935/760/remote/526870/screenshots/`.
- **Coordenadas:** cm en el save, +X al este, +Y al sur y Z hacia arriba.
- **Anillo:** cimientos a 380 m con bordes en X 1.548–3.252 e Y −2.572…−1.436. Su interior está casi vacío.
- **Fábrica:** va pegada a los bordes (franja este X 3.050–3.250, franjas norte y oeste) y a la zona este (X 3.700–4.330).
- **Alturas:** masa entre 30 y 160 m. Las plantas principales están a 48, 90, 116 y 156 m, y la mayoría de máquinas, a 50–60 m.
- **Puntos conocidos:** el ascensor original estaba en (3204, −1482, 382) con giro 270° y el HUB está en (3210, −1542, 50).
- **Corredores de 380 m:** el puente N–S en X 2448 y los puentes E–O en Y −1752/−1760.
- **Terreno bajo la sala:** a 1–2 m (lo comprobó Carlos en un pilar).
- **Muestras de color en uso:** Slot0, 16, 17, Concrete y ProjectAssembly. Nuestros saves definen Slot14 "Borg" (casi negro con Carbon Steel) y Slot15 "grafito". Slot1–13 están libres.
- **Acabados:** solo está desbloqueado Carbon Steel. **El color secundario no se ve en paredes ni ventanas.**

**Escribir en el save.** Todo pasa por `muestra.escribir(entrada, salida, piezas, muestras, retoque)`:
- **Piezas:** solo ligeras y desbloqueadas.
- **Choques:** descarta cualquier pieza a menos de 4 m del pivote de una existente, o que toque la caja de holgura de un actor, los splines de cintas y tuberías, las escaleras de mano o los cables.
- **Guardado:** reescribe la huella `SaveDataHash` (MD5 del cuerpo tras la cabecera) y `SaveName`; sin eso, el juego avisa de "save editado".
- **Verificación al recargar:** el conjunto de piezas (clase, posición, muestra) es exactamente el de entrada más las nuevas.
- **Trampa de la lib:** `m.Values` devuelve una copia; para añadir una clase hay que reasignarla.
- **Actores:** moverlos es solo cambiar `Header.Transform`. Probado con el ascensor y con el jugador (`Char_Player_C`, el pivote va 1,1 m sobre el suelo).

**Comprobar una carga.** En `FactoryGame.log`, el bloque "Load error summary" tras `loadgame=NNN`.
- **Lo normal:** "Unknown Classes" vacío y un único objeto desconocido, `Build_Locker_MK1_C_2147470866`.
- **Ruido del motor que sale siempre:** navmesh demasiado grande, Nav Data Elite/Giraffe, `conveyor.UseExperimental` y Niagara `ImpactPointsAtSphere`.
- **Tiempo de carga de las piezas ligeras:** 0,75 s con 27.900 piezas, 0,88 s con 36.700 y 1,09 s con 42.300.

**Geometría de las piezas** (medida, y en `catalogo.json` → `caja_m`):
- **Cimiento:** 8x4 de 8×8×4 m y 8x1 de 8×8×1 m, con el pivote en el centro.
- **Pilar grande:** 4×4×4 m, con el pivote en el centro.
- **Pared:** pivote en el centro de la base, 8 m a lo largo de su Y local y 0,5 m de grueso en su X. Con giro 90° mira al sur. Apoya en la cara superior del cimiento.
- **Pared inclinada de 8 m** (`WallSet_Steel_Angular_8x8`): caja de 8×8×8 m con el pivote en el centro de la base, a 45°. **Sube hacia su +X local.** La de 4 m sube 4 m en 8 m (27°).
- **Esquina del embudo:** la pared de esquina inclinada de FICSIT (ligera) no la cierra en ninguno de los 4 giros. La cóncava, que sería la buena, no es ligera.
- **Ascensor espacial:** caja de unos 49×54 m; su cable al espacio (16×16×1.000 m) sale del pivote.

**Qué se puede escribir.** Manda el flag `mManagedByLightweightBuildableSubsystem` (columna `ligera` del catálogo), no la sección del JSON del juego.
- **Ligeras:** paredes, ventanas, cimientos, rampas, pilares, tejados, barandillas, escaleras y **vigas** (la longitud irá en `TypeSpecificData`, sin comprobar).
- **No ligeras (edificios normales):** paredes de cinta, esquinas inclinadas de acero y de hormigón, todas las cóncavas y las luces.

## El último save (342) y qué tal ha quedado
Parte del 334c y tiene 14.403 piezas nuevas. El jugador aparece en la sala.

| Elemento | Qué es | Veredicto |
|---|---|---|
| Cara sur (X 2.988–3.252) | Vitrina de cristal (50–138 m), pared ciega encima, 17 costillas de hormigón cada 16 m, cornisas a 138 y 338 m | "Aceptable"; la ranura de la escalera, "genial" |
| Esqueleto | Columnas y vigas de celosía hasta 568 m; cruz sobre el anillo, cortada en la boca del embudo | Sin veredicto claro; cuidado con el exceso de vigas |
| Sala del ascensor | Suelo de 320 × 320 m a 382 m sobre 20 pilares hasta −2 m; ascensor en (2400, −2000, 382) | "Mejor" |
| Embudo | Paredes a 45° de 382 a 566 m, boca de 688 m | La forma, bien; **las esquinas, mal** |
| Corredor | Paredes de cristal sobre el puente N–S, fuera del embudo | El cristal gusta |
| Mirador | Pasarela y balcón a 96 m al sur de la cara | Provisional |

## Lo que no funcionó (no repetir)
- **Diseñar a ciegas y en grande:** 5.700 paredes de embudo sin validar antes una esquina.
- **El A/B por esquinas con la pared de esquina de FICSIT.**
- **El relieve aleatorio de 1–2 m:** no se lee a 100 m.
- **Cajas cerradas:** el corredor de 8 × 8 m.
- **Tirantes alrededor del ascensor.**
- **Ascensor flotando sin base.**
- **Vigas cruzando el camino de la carga del ascensor.**
- **Grafito sin acabado en bloques grandes:** al sol sale casi blanco.

## Lo que aún hay que aprender
- Escribir **edificios normales** (luces con cable, paredes cóncavas, paredes de cinta): componentes, cables y circuitos.
- Las **vigas**: cómo se guarda su longitud.
- El **terreno** en cada punto: solo se conoce un pilar.
- El **rendimiento** con 100.000 piezas más.
- La orientación de tejados y rampas.
- La **logística de la sala**: por dónde entran las cintas.

## Siguiente paso: tú diseñas, el script multiplica
1. Carlos construye **un módulo** en el juego con piezas ligeras, por ejemplo una esquina del embudo de un escalón, un tramo de corredor o un vano de fachada. Lo pinta con una muestra libre como marca (por ejemplo Slot13) y guarda.
2. Script nuevo (`modulo.py`):
   - lee las piezas con esa marca (clase, posición relativa a un ancla de la rejilla de 8 m, giro y muestra final);
   - las guarda como JSON;
   - las estampa a lo largo de una línea o rejilla con giros de 90°, usando `escribir()`.
3. Una sola carga para validar, con 2–3 repeticiones antes de escalar (`DISENO.md`, fase E).
4. Primeros módulos: **la esquina del embudo**, **el tramo de corredor** y **el vano de fachada**.

## Ficheros
| Fichero | Qué es |
|---|---|
| `PLAN.md` | Este plan |
| `DISENO.md` | Guía de diseño arquitectónico, aportada por Carlos; leerla antes de diseñar |
| `catalogo.py` → `catalogo.json` | Cada pieza construible: ruta exacta para el save, receta, desbloqueo, ligera y caja |
| `muestra.py` | Motor común `escribir()` más la muestra y el mirador de la fase 0 |
| `cubo.py` | Genera el save en curso desde `334c.sav` (`.venv/bin/python cubo.py 334c.sav 343.sav`) |
| `vista.py`, `maqueta.py` | Planta y alzados de una partida; maquetas de envolvente de la fase 1 |
| `img/` | Capturas del juego y dibujos |

La carta de la fase 1 (opciones A/B/C, cruces de logística y recuento de andamiaje) está en el historial de git, en `ARQUITECTURA.md`.

## Normas
- **Nunca tocar** los saves existentes: siempre se escribe un número nuevo y se copia a SaveGames con `cp -n`.
- Tras cada cambio en `muestra.py`, comprobar que el 336 regenerado sale idéntico byte a byte.
- Vigilar el log en cada carga y anotar aquí lo aprendido, en corto. Subir al repo: https://github.com/elMestre/satisfactory-borg-cube
- Una cosa por iteración, pequeña y validada en el juego antes de repetirla.

## Historia
- **Fase 0:** muestra de fachada. En el 335, A/B del chaflán (gana 90°); en el 336, el mirador.
- **Fase 1:** carta con subagentes y decisiones de Carlos.
- **Fase 2:**
  - 337: cara sur con cristal, esqueleto y ascensor al centro.
  - 338: vitrina, tres fachadas e isla.
  - 339: costillas, embudo y corredores abiertos.
  - 340: sala de 320 m sobre pilares.
  - 341/342: prueba de esquinas (ninguna vale) y aparición en la sala.
  - Veredicto de Carlos: el proceso a ciegas es caro y poco eficaz.
