# Cubo Borg en Satisfactory: plan para retomar

> Al aprobarse, este plan se copia a `~/cowork/satis/PLAN.md`, que pasa a ser la copia viva. Cada sesión o agente lee primero ese fichero y, al terminar, anota su avance en **Registro** (al final).

**Estado (2026-10-23, 16:50):** fase 0 cerrada. **Fase 1 en borrador: `ARQUITECTURA.md`**, con los 9 puntos, una propuesta recomendada y alternativas en cada uno. Ya lleva los tres informes y las maquetas `img/f1_*`. Falta que Carlos marque sus decisiones.

**Repo público:** https://github.com/elMestre/satisfactory-borg-cube. Incluye scripts, plan, catálogo, la partida base `334c.sav`, la última muestra y `img/` (capturas y dibujos). Los demás `.sav` se ignoran; los que se quieran subir van con `git add -f`.

## Qué es
La partida principal de Carlos (sesión elMestre, `334.sav`, juego v1.2.4.1 CL 513885, 101 h) funciona, pero es fea: losas desnudas a alturas sueltas, pilares finos, máquinas y cintas al aire, sin luz. Su idea original era un **cubo kilométrico estilo Borg**. A 380 m quedaron las aristas sin caras: un anillo de cimientos de 1.696 × 1.128 m. La meta es una fábrica cinematográfica. Por script generamos la arquitectura (envolvente, estructura, fachada) dentro de saves nuevos; Carlos juega, revisa con capturas y decide.

## Decisiones ya tomadas (Carlos, 2026-10-23)
- **Se aprovecha lo que hay; no se rehace.** La producción no se toca. El andamiaje feo (pilares finos, pasarelas sueltas) se retira cuando se cierra su sección.
- **Se trabaja por secciones**, cada una en un save nuevo, y antes de la obra se fijan unas bases arquitectónicas.
- **Las piezas generadas aparecen gratis, pero solo las ya desbloqueadas** (como el modo creativo, sin piezas bloqueadas). Cada script comprueba con `assert` que todos sus `BuiltWithRecipe` están en `FGRecipeManager.mAvailableRecipes`.
- **Antes de empezar, compra en la tienda AWESOME** (ver la lista). Lo que se desbloquee entra solo en la siguiente lectura del save.
- Paleta inicial "Borg" (casi negro con acento verde). No es una decisión irreversible: ver "Paleta en masa".

## Compra en la tienda AWESOME (antes de la fase 0)
Cupones disponibles: **27** (10 por imprimir en el sumidero y 17 en inventarios). Todos los artículos tienen los requisitos cumplidos. **No hay piezas críticas imposibles de desbloquear**: el único límite son los cupones, y se consiguen más alimentando el sumidero.

| Prioridad | Artículo | Cupones | Para qué |
|---|---|---|---|
| Imprescindible | Indoor Lighting (luz de techo) | 3 | Filas de paneles de luz, como en las referencias |
| Imprescindible | Light Control Panel | 2 | Poner las luces en verde y regular su intensidad |
| Imprescindible | Steel Wall Material | 5 | Paredes de acero oscuras (y sus ventanas) para el revestimiento Borg |
| Imprescindible | Carbon Steel Finish | 8 | Acabado metálico oscuro para la muestra Borg |
| Imprescindible | Conveyor Wall Hole | 1 | Que las cintas atraviesen la envolvente por cualquier pared |
| Muy útil | Beam Expansion Pack | 4 | Vigas de hormigón, en H y en cruz: estructura y relieve |
| Muy útil | Flood Lights | 5 | Iluminar las fachadas desde fuera |
| Si sobra | Grip Metal / Coated Concrete Foundation | 5 / 6 | Techo de metal oscuro / suelo pulido de las naves |
| Si sobra | Structural Frame Set | 10 | Suelo de cristal, muro y suelo de estructura |
| Si sobra | Tar / Metal Roof Material | 2 / 3 | Tejados oscuros |

Imprescindibles: 19 cupones. Con los muy útiles, 28 (falta uno). **Ya tenidos y útiles:** ventanas hexagonales y de panal (`Wall_Window_Thin_8x4_02`, `Wall_Window_8x4_06`), paredes en chaflán (Tilted Walls), muros de cinta, pilares de hormigón, metal y estructura, tejados con ventana, material de muro de hormigón y patrones de línea.

## Datos ya sacados del `334.sav` (no repetir)
- **Retícula casi perfecta, hecha a mano por Carlos** copiando y multiplicando módulos a propósito; no es cosa del juego: los 10.824 cimientos 8x4 tienen X e Y en múltiplos de 8 m y Z en múltiplos de 4 m, con giros de 0, 90, 180 o 270°; solo 4 se salen. Las paredes caen en la rejilla de 4 m (99,76 % de las piezas ligeras). Las excepciones son 667 pilares de hormigón con giros sueltos (cosmético) y 1.999 pilares colgados boca abajo, que es lo normal al construirlos bajo un cimiento. Los 8x1 están centrados a medio metro porque miden 1 m de grosor. Las máquinas tienen giro recto en el 99,2 % y van en la rejilla fina de los cimientos.
- **Extensión:** X de 1.463 a 4.328 m e Y de −3.013 a −1.436 m. La masa de la fábrica está entre 30 y 160 m de altura. Hay 18 alturas de cimiento en uso (−18, 26, 38, 48, 52, 56, 69, 70, 78, 89, 90, 99, 116, 156, 298, 338, 380, 422 m).
- **Anillo de 380 m:** X de 1.552 a 3.248 m e Y de −2.568 a −1.440 m, con 3.251 piezas (la mitad en el borde y la otra mitad en puentes interiores). El ascensor espacial está en (3204, −1482, 382) y el HUB en (3210, −1542, 50). La zona este (X de 3.250 a 4.330 m) queda fuera del anillo.
- **Suelo, aproximado:** la mediana de los extractores está a 14 m (de −16 a 234 m) y las bases de pilar entre 8 y 72 m. El terreno real no se conoce: un cubo flotante no lo necesita.
- **Piezas:** 27.851 ligeras (10.824 cimientos 8x4, 7.851 de 8x1, 3.826 paredes, 1.918 pilares…) y 6.691 edificios en total (942 máquinas).
- **Paleta en masa: sí se puede.** El 99 % usa tres muestras de color en las piezas ligeras: `Slot16` gris (19.758), `Slot0` naranja FICSIT (5.622) y `Concrete` (2.471). En los actores: `Slot0` (5.536) y `Slot17` (1.139). Cada color se define una sola vez en `BP_BuildableSubsystem.mColorSlots_Data` (28 muestras): si se cambia esa definición, se repinta todo de golpe. También se pueden reasignar muestras por zonas.
- **Biomas:** desierto de dunas con cañón, cascadas y lago al sur. Es lo más bonito del sitio y no hay que enterrarlo.

## Herramientas y API (lib `satisfactory-save` 0.11.0, venv `~/cowork/satis/.venv`)
- Lectura: `sg = satisfactory_save.SaveGame(path)` y `sg.allSaveObjects()`. Hay que filtrar el ruido de stderr: `grep -vi 'unknown binary'`.
- Piezas ligeras: el objeto de clase `FGLightweightBuildableSubsystem` tiene `.Object.mBuildableClassToInstanceArray`, con `.Keys` (referencias a clases) y `.Values` (vectores de `FRuntimeBuildableInstanceData`: `Transform`, `BuiltWithRecipe`, `CustomizationData.SwatchDesc`/`MaterialDesc`/`PatternDesc`/`OverrideColorData`, `BuiltBy`, `BlueprintProxy`, `TypeSpecificData`).
- Escritura **en memoria, comprobada**: `m.Values[i].append(inst)` persiste, `m.Keys.append(ref)` persiste y `FRuntimeBuildableInstanceData()` y `FObjectReferenceDisc()` tienen constructor. **Escribir a fichero en SaveVersion 60 está probado (2026-10-23):** guardar sin cambios da un fichero idéntico byte a byte y el `334b.sav` (+1 cupón) se escribió y recargó bien.
- Muestras de color: el objeto `BP_BuildableSubsystem` tiene `.Object.Properties[0]` (`mColorSlots_Data`, un StructArray). Cada entrada `.Data` contiene `PrimaryColor`, `SecondaryColor` y `PaintFinish`.
- Desbloqueos: `FGRecipeManager.mAvailableRecipes`, `BP_SchematicManager.mPurchasedSchematics` y los cupones en `FGResourceSinkSubsystem.mNumResourceSinkCoupons`.
- **Catálogo propio: `~/cowork/satis/catalogo.json`** (lo genera `catalogo.py [SAVE]`; hay que regenerarlo si el juego se actualiza o tras comprar algo). Tiene una pieza construible por línea con clase, **ruta exacta para el save**, nombre del juego, tipo, `ligera`, medidas en m, menú, receta y si está desbloqueada. Las rutas salen del índice del `.utoc` del juego (sin cifrar) y no se adivinan; las parejas clase-receta, de los datos del juego y del save. Los scripts sacan rutas y recetas de ahí.
- Catálogo del juego: `~/.local/share/Steam/steamapps/common/Satisfactory/CommunityResources/Docs/en-US.json` (UTF-16), con la tienda en `FGSchematic` (`mType=EST_ResourceSink`). **Ligera no es la sección del JSON sino el flag `mManagedByLightweightBuildableSubsystem`:** las paredes de cinta salen entre las ligeras y son actores, mientras que **las vigas (`Build_Beam_*`), las escaleras y algunas pasarelas sí son ligeras** (lo dice el flag; en el save aún no hay ningún ejemplo, y la longitud de la viga irá seguramente en `TypeSpecificData`). Las luces sí son actores y necesitan cable.
- **Geometría (medida en el save y en `mClearanceData`):** el cimiento 8x4 tiene el pivote en su centro (8 × 8 × 4 m). La pared tiene el pivote en el centro de la base, 8 m a lo largo del eje local Y y 0,5 m de grosor en el local X; con giro 90° mira a +Y (sur) y apoya en Z = Zcimiento + 200 cm. La pared inclinada (`*_Angular_8x4/8x8`) ocupa una caja de 8 × 8 m con el pivote en su centro: la de 4 m baja a unos 27° y la de 8 m a 45°. **Sube hacia su +X local** (comprobado en la fase 0). Para un chaflán con la arista alta fuera, el +X local apunta hacia fuera: en la cara sur, giro 90°.
- **Cuidado con la lib:** `m.Values` devuelve una copia de la lista. Para meter una clase nueva hay que hacer `vals = m.Values`, `vals.append(StdVectorFRuntimeBuildableInstanceData())` y `m.Values = vals`, además de `m.Keys.append(ref)`. Los vectores de dentro sí son referencias (`m.Values[i].append(inst)` persiste). Una instancia hay que rellenarla antes de añadirla, porque se copia. Las del juego llevan alfa 1 en `OverrideColorData`.
- **Guardar siempre con `muestra.guardar(sg, ruta)`, no con `sg.save()` a secas.** La cabecera lleva `SaveDataHash`, que es el MD5 de todo lo que sigue a la cabecera (el cuerpo comprimido, desde el primer `c1832a9e`), y `SaveName`. La lib copia los del save de entrada, así que el juego avisa de "save editado por terceros", aunque carga igual. `guardar()` pone el nombre del fichero y recalcula la huella.
- Vista: `~/cowork/satis/vista.py SAVE salida.png` dibuja la planta y dos alzados (estructura frente a máquinas).
- Diagnóstico de carga: `…/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/Logs/FactoryGame.log`, en el bloque "Load error summary" que sigue a la línea `loadgame=NNN`. Con el 334 sale `NO LOAD ERRORS FOUND`, sin clases desconocidas y con un único objeto desconocido (`Build_Locker_MK1_C_2147470864`). Una ruta de clase mal escrita aparecería en "Unknown Classes". **Ruido del motor que sale en todas las cargas,** también en las partidas sin tocar (333 y 334), así que no es nuestro: "Navmesh bounds are too large" (15 veces), "Nav Data for agent Elite/Giraffe was not found", `conveyor.UseExperimental` y el emisor Niagara `ImpactPointsAtSphere`. (Los 54 avisos eran de cargar el 333 en la build nueva.)
- Capturas de Carlos (F12): `~/.local/share/Steam/userdata/1878935/760/remote/526870/screenshots/`. Sus referencias: `~/Pictures/screenshot-2026-10-23_14-2*.png` (vídeo "Gorgeous Satisfactory World Tour") y dos jpg del 23 de octubre en `~/Downloads`.
- Saves: `~/.local/share/Steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/76561197962144663/`.

## Normas para cualquier sesión o agente
- **Antes de diseñar una sección, leer `DISENO.md`** (guía de diseño que aportó Carlos el 2026-10-23). Cómo aplica aquí:
  - **Producción:** aquí no se toca, así que ese criterio no aplica.
  - **Logística, sí:** antes de vestir algo, ver qué conexiones llegan y dónde hay que dejar paso. La sala del ascensor necesita la entrada de muchas cintas.
  - **Ya aprendido a golpes:** ritmo antes que azar (el relieve aleatorio se leía como ruido), ventanas donde se lee actividad (vitrina), nada de cajas planas (costillas), prototipo a escala, validar y luego repetir (el ciclo save → capturas).
  - **Pendiente según la guía:** capa logística de cada sección, iluminación y registro del terreno (no se conoce bajo la sala).
  - Al cerrar cada versión, puntuarla con los criterios de aceptación de la guía (0–2, sin "producción").
- **No tocar nunca el `334.sav`** ni ningún save existente. Se escribe a un nombre nuevo (`335`, `336`…) en `cowork/satis` y se copia a SaveGames.
- Cada script deja su comprobación: recargar la salida y verificar con `assert` que solo cambian las piezas previstas (recuento por clase) y que todas las recetas están desbloqueadas.
- No veo el juego: Carlos carga el save y hace capturas con F12. Hay que preguntarle cosas concretas (ver la memoria `carlos-forma-de-trabajar`).
- Al terminar, anotar en **Registro** y actualizar la memoria `satisfactory-cubo-borg`.

## Fase 0: muestra técnica → `335.sav` (un agente)
Va primero porque comprueba que se pueden escribir piezas. Si falla, la carta cambia (por ejemplo, a blueprints).
1. ~~Ida y vuelta~~: hecho el 2026-10-23, md5 idéntico. **Base de la fase 0: `334c.sav`**, con la compra AWESOME hecha.
2. **`~/cowork/satis/muestra.py`:** definir una muestra libre como "Borg" (por ejemplo `Slot14`: principal casi negro, secundario verde; con Carbon Steel si se ha comprado). Panel de 10 × 10 paredes (80 × 40 m) colgado por fuera del borde sur del anillo, junto al ascensor espacial. Relieve con profundidades pseudoaleatorias (0, −1 o −2 m, semilla fija) mezclando paredes de acero o hormigón, muro con hueco, ventana hexagonal y borde en chaflán (`*_Angular_8x4`). Todo con la muestra Borg.
3. Escribir el `335.sav` con su comprobación y copiarlo a SaveGames. Carlos lo carga y manda capturas; se revisa el log.
- **Hecho (2026-10-23):** `muestra.py` → `335.sav`, copiado a SaveGames (md5 `0ebf39fa…`). El panel cuelga bajo la cara sur de la plataforma del ascensor (cimientos a 380 m, cara en Y = −1436 m), en X 3092–3172 m, al oeste del pilar de X 3176 y de las escaleras de mano de X 3200, y delante de la escalera de rampas, que queda 8 m dentro. Tiene 8 filas de paredes (de 378 a 346 m), con la fila de arriba enrasada y la tercera como franja de ventanas hexagonales hundida 1 m. El resto mezcla acero, hormigón, muro con hueco y ventanas hexagonales y de panal, con fondo 0, −1 o −2 m (semilla 334). Debajo va un chaflán de paredes inclinadas de 8 m (45°, de 346 a 338 m) en **A/B**: las columnas 0–4, al oeste, con giro 90°, y las 5–9, al este, con 270°. La buena es la que baja desde el borde del panel hacia dentro, como un casco. La muestra `Slot14` ("Borg") queda casi negra con verde y acabado Carbon Steel. Son 90 piezas de 6 clases, 5 de ellas nuevas en el save. Se comprobó recargando que solo cambian esas piezas y esa muestra, y que todo está desbloqueado. Las paredes de cinta se quitaron de la mezcla porque no son ligeras.
- **Carga comprobada (2026-10-23, 16:02):** "Unknown Classes" vacío, el mismo objeto desconocido de siempre (la taquilla), `NO LOAD ERRORS FOUND`, y las piezas ligeras aplicadas en 0,68 s (0,75 s con el 334). El único aviso nuevo, "Hash for save game data mismatched", ya está corregido en `muestra.guardar()`.
- **Vista desde fuera** (`img/336_desde_el_balcon.jpg`: desde el balcón, a 96 m, mirando al norte y unos 25 m por encima del centro del panel):
  - El panel se lee como un bloque oscuro colgado bajo el canto de la plataforma, y el chaflán cierra bien el borde inferior.
  - **El relieve de 1–2 m apenas se distingue** a 100 m: para que se lea hará falta relieve de 4–8 m, o luz rasante.
  - **Las ventanas y los huecos dejan ver el desorden de detrás** (la escalera de rampas en diagonal). Una fachada con huecos necesita algo detrás, por ejemplo un interior iluminado; si no, mejor casi ciega, como un cubo Borg.
  - **La coronación también es fachada:** encima quedan a la vista el canto de la plataforma con su barandilla, cintas, tuberías y el ascensor.
  - El conjunto sale marrón muy oscuro con la neblina rosada del desierto, y sigue sin verse verde.
- **`336.sav` (muestra v2 + mirador):** la misma muestra (semilla 334) con todo el chaflán a 90°, más el mirador de `muestra.mirador()`. Es una pasarela de 13 cimientos 8x1 que sale de la cara sur en X 3080, al oeste del panel, y recorre 96 m. Al final, un balcón de 13 cimientos hacia el este (X 3088–3184), con la cara superior a 382 m, enrasada con la plataforma, y en Slot16. Ahí no hay barandilla (empieza en X 3168). Para el mirador se usan cimientos 8x1 en vez de una escalera, porque nadie ha comprobado aún cómo se orientan las rampas. La comprobación es más fuerte: el conjunto de todas las piezas ligeras (ruta, posición, muestra) = entrada + previstas, y ninguna pieza existente a menos de 4 m de una nueva.
- **A/B del chaflán, resuelto:** el bueno es el de **90°** (la mitad oeste). Carlos lo vio mirando hacia el sur desde dentro, por eso le quedaba a la derecha. Con 270° queda un hueco entre el panel y la pieza, que enseña su cara de abajo. Regla: **la pared inclinada sube hacia su +X local**. `muestra.py` ya usa 90° en todo el chaflán; el `335.sav` de SaveGames conserva el A/B.
- **Visto en las capturas** (3, de las 16:04, todas desde dentro mirando al sur, con luz de tarde): la muestra se aplica y el conjunto sale casi negro tirando a marrón. Se nota el relieve, y el chaflán bueno queda bien. **No hay ni un píxel verde:** en las paredes de acero, hormigón y ventanas el color secundario no se ve, así que el acento verde tendrá que venir de la luz (punto 6 de la fase 1). Falta una vista desde fuera (al sur, mirando al norte, a unos 100 m) para juzgar la fachada, que es lo que se verá desde el cañón. Si Carlos no llega volando, se le pone un mirador (unos cimientos sueltos) en el siguiente save.
- **Hecho cuando:** el juego carga el 335 sin errores nuevos y Carlos ha visto la muestra.

## Fase 1: carta arquitectónica (una o dos sesiones)
`~/cowork/satis/ARQUITECTURA.md` más maquetas hechas con datos reales (ampliando `vista.py`: la envolvente propuesta sobre la fábrica, en planta, alzado e isométrica). Cada punto lleva propuesta y la decisión de Carlos:
1. **Retícula y alturas:** 8 m en horizontal y múltiplos de 4 m en vertical; pocas cubiertas fijas en lugar de 18 alturas.
2. **Envolvente:** forma y tamaño. Una opción es la caja flotante sobre el anillo (1.696 × 1.128 m, techo a 380 m, base por encima de la fábrica, pocos pilares gigantes, sin enterrar el cañón); otra, un cubo de verdad de 1.128 m de lado. Falta decidir qué pasa con la zona este.
3. **Estructura:** pocos pilares gruesos (Big Concrete Pillar apilado, base en chaflán) y vanos fijos.
4. **Fachada:** módulo con relieve y jerarquía (paños ciegos, franjas de ventana, aristas en chaflán), a partir de la muestra.
5. **Paleta:** qué muestra lleva cada cosa (envolvente, estructura, acento, maquinaria).
6. **Luz:** paneles de techo y focos en verde con el Light Control Panel. Es lo único que dará el verde, porque la pintura secundaria no se ve en las paredes (fase 0). Las luces son actores y necesitan cable, así que hay que elegir entre generar el cableado por script o colocarlas Carlos con blueprint.
7. **Logística:** las cintas y tuberías cruzan la envolvente por huecos de pared; en fachada no queda nada a la vista.
8. **Qué se queda y qué se va**, por zonas.
9. **Presupuesto de piezas y rendimiento:** cerrar el anillo son unas 100.000 piezas (hoy hay 27.851). Se mide después de cada sección.
- **Hecho cuando:** Carlos ha decidido los 9 puntos.

## Fase 2: obra por secciones (un agente por sección)
Orden propuesto: 1) la cara del ascensor espacial, que es la más visible; 2) el resto de caras; 3) el techo; 4) los pilares; 5) luz e interiores. `~/cowork/satis/cubo.py` lleva las decisiones de la carta como constantes y reutiliza los módulos de `muestra.py`. Cada sección va en un save `33x`; Carlos lo carga, manda capturas y dice qué tal va el rendimiento; se ajusta y se pasa a la siguiente.

## Riesgos conocidos
- El rendimiento con más de 100.000 piezas ligeras está por medir.
- Las luces necesitan cableado y no son ligeras.
- La lib avisa de "unknown binary data" en `FGItemPickup_Spawnable`. Es inofensivo para leer; vigilarlo al escribir.

## Registro
- 2026-10-23: plan escrito y copiado a `~/cowork/satis/PLAN.md`.
- 2026-10-23: ida y vuelta en SaveVersion 60 correcta. `334b.sav` = 334 más 1 cupón (11 por imprimir, 28 en total) para comprar los imprescindibles y los muy útiles. No llegó a usarse: Carlos cargó el 334 y esperó al último cupón; el 334b se ha quitado de SaveGames.
- 2026-10-23: **`334c.sav`** = compra hecha: Indoor Lighting, Light Control Panel, Flood Lights, Steel Wall Material (con toda la familia de paredes de acero: ventanas, chaflán, diagonales, muros de cinta, puertas, portones), Carbon Steel Finish, Conveyor Wall Hole y Beam Expansion Pack, en total 38 recetas nuevas; quedan 0 cupones por imprimir. Siguiente: fase 0 sobre el 334c.
- 2026-10-23: fase 0 escrita. `catalogo.py` → `catalogo.json` (546 piezas, 344 desbloqueadas en el 334c), a petición de Carlos, para tener el catálogo a mano. `muestra.py` → **`335.sav`**, ya en SaveGames y pendiente de que Carlos lo cargue. Se corrigieron dos cosas del plan: las vigas sí son ligeras, y "Basic Wall (4 m)" de acero es `Build_Wall_8x4_02` (llegó con Steel Wall Material), no `Build_SteelWall_8x4`, que es una pieza vieja sin receta. Carlos propuso usar ultraplan; se dejó para la fase 1, que es donde se decide la estética.
- 2026-10-23 16:02: Carlos carga el 335 y no hay errores nuevos (detalle en la fase 0). Se corrige la huella del save en `muestra.guardar()`; el 335 de SaveGames se queda como está, con el aviso de huella, porque lo tiene abierto. Esperando capturas y la mitad buena del chaflán.
- 2026-10-23 16:10: **fase 0 cerrada.** El chaflán bueno es el de 90° (la pared inclinada sube hacia su +X local) y no se ve verde en la pintura; detalles en la fase 0. Sobre ultraplan: necesita un repo de GitHub (sesión en la nube con una copia del repo) y `cowork/satis` no lo es, así que sin subir el save y las capturas a un repo privado no vería los datos. Se le propone a Carlos hacer la fase 1 aquí.
- 2026-10-23 16:25: Carlos pidió el mirador y el repo ("todo esto puede ser público"). `336.sav` copiado a SaveGames, con vigilante en el log. Repo público `elMestre/satisfactory-borg-cube` creado, con README.
- 2026-10-23 16:44: Carlos carga el 336 sin errores nuevos y **sin el aviso de huella**, así que `muestra.guardar()` funciona. Piezas ligeras aplicadas en 0,73 s. Esperando la captura desde el balcón.
- 2026-10-23 16:45: captura desde el balcón subida a `img/`, con sus observaciones en la fase 0. Listo para la fase 1 (Carlos la lanzará con ultraplan sobre el repo).
- 2026-10-23 16:50: fase 1 hecha aquí, a petición de Carlos ("esfuérzate al máximo y lanza subagentes"), antes de que se acabara su ventana de uso a las 17:00. Borrador de `ARQUITECTURA.md` subido; tres subagentes trabajando en maquetas, logística/andamiaje y luz/rendimiento.
- 2026-10-23 16:54: `ARQUITECTURA.md` completa con los tres informes (maquetas A/B/C, luz, logística y andamiaje). Pendiente: que Carlos marque las casillas. Lo siguiente, la fase 2: la cara sur según lo que decida.
- 2026-10-23 16:57: **Carlos decide** el concepto "Estrella de la Muerte II" (cerrar y embellecer lo que hay, con el cubo en construcción), una altura en proporción perfecta (elegí 3:2:1, techo a 568 m; alternativa áurea, unos 616 m), fachada variada por plantas con un gran espacio acristalado, y deja la luz a mi criterio (aplazada). Todo apuntado arriba en `ARQUITECTURA.md`. Siguiente: la fase 2 empieza por el bloque del ascensor (muro cortina sur) y el esqueleto de las aristas.
- 2026-10-23 17:25: **fase 2, sección 1 → `337.sav`** (`cubo.py`), copiado a SaveGames, con vigilante en el log. Contenido:
  - Cara sur bajo la plataforma (X 2988–3252): zócalo de 50–98 m, gran acristalado de 98–338 m (Full Frame Window), coraza Borg de 338–378 m y cornisas en grafito (Slot15, nueva).
  - Esqueleto en celosía (Big Frame Pillar, cubos de 4 m centrados en el pivote): 4 columnas en la cara sur, cruz del techo a 568 m por el centro y sus 4 columnas en el borde del anillo.
  - **El ascensor espacial, movido al centro** (2400, −2000, 382), a petición de Carlos ("en plan GLaDOS, que cuelgue"): su cable al espacio (en el catálogo es una caja de 1.000 m de alto) atraviesa la cruz del techo. Pasarela de 3 losas hasta el puente N–S del anillo (X 2448).
  - 3.905 piezas. Se descartaron 52 por choque: 39 en la columna de la escalera de mano (X 3200) y 13 de la coraza hundida delante de los pilares de X 3176 y 3248. Arreglo pendiente: no hundir esas dos columnas.
  - `muestra.py` reorganizado: `escribir()` es común a la muestra y a las secciones, comprueba choques con actores (splines, escaleras de mano, cables) y descarta lo que choca. El 336 regenerado sale idéntico byte a byte.
- 2026-10-23 17:15 (hora del log, UTC+2): el **337 carga sin errores nuevos** y sin aviso de huella. Piezas ligeras aplicadas en 0,79 s (0,73 s con el 336). Esperando las capturas de Carlos.
- 2026-10-23 17:35: lo que dijo Carlos del 337: la pared "no pinta mal, tampoco bonita"; el ascensor flotando "así está feo", y la cruz del techo se cruza con la carga (las abrazaderas quedan por debajo de las vigas). Elige la **opción B** (colgado de verdad) y propone **corredores modulares** o embellecer los nodos de fábrica concentrada.
- 2026-10-23 17:50: **`338.sav`** (`cubo.py` reescrito), copiado a SaveGames, con vigilante. Contenido:
  - **Vitrina:** cristal de 50 a 138 m, delante de la fábrica.
  - **Tres fachadas de prueba encima, sin azar:** monolito (oeste), bandas de ventanas hexagonales (centro) y costillas de hormigón cada 16 m (este).
  - **Isla del ascensor:** 80 × 80 m, chaflanes por debajo, 4 tirantes de celosía y un hueco de 80 m en la cruz del techo.
  - **Corredor modular** sobre el puente N–S (X 2448): tubo de 8 m con ventana cada 4.º vano y costillas cada 32 m.
  - 5.530 piezas. Se descartaron 46: 44 en la escalera de mano de X 3200 y 2 losas del techo del corredor en su extremo norte.
  - **Corrección:** el cable del ascensor sale de su pivote (la caja de 8 × 8 × 1.000 m no está desplazada). La caja desplazada 20 m es un detalle pequeño de 5 × 4 × 3 m.
  - El catálogo trae ahora `caja_m` (holgura en ejes de la pieza) para 501 piezas, y los choques usan esas cajas de los actores.

- 2026-10-23 17:44 (hora del log): el **338 carga sin errores nuevos** y sin aviso de huella. Piezas ligeras aplicadas en 0,87 s (unas 33.400 en total). Esperando el veredicto de Carlos: fachada, corredor y ascensor.
- 2026-10-23 18:05: lo que dijo Carlos del 338:
  - **Fachada:** la de costillas ("aunque quizá sea una muestra muy pequeña").
  - **Corredor:** "mejor que plataforma desnuda, pero feo un rato", y además una caja cuadrada que no deja ver nada: hay que rediseñarlo.
  - **Ascensor:** "ha mejorado mucho", pero lo imagina en una sala "en plan pirámide invertida", con más espacio alrededor (sin la caja de tirantes).
- 2026-10-23 18:10: **`339.sav`**, copiado a SaveGames, con vigilante. Contenido:
  - **Costillas en toda la cara sur:** 17 pilares de hormigón cada 16 m, de 50 a 378 m, sobre la vitrina y la pared ciega.
  - **Embudo en pirámide invertida:** 3.127 paredes inclinadas a 45° en 23 anillos, de la isla (382 m) al techo (566 m), con una boca de 448 m. Las esquinas se resuelven cruzando los dos lados. La cruz del techo se para en la boca. Sin tirantes.
  - **Corredor rediseñado y abierto:** galería de cristal con pórticos de celosía cada 16 m en el tramo norte, y puente de celosía (pretil de 1 m y viga de 8 m de canto bajo el tablero) en el tramo sur. Bajo el embudo, el puente pasa a cubierto con 8 m libres y entra a la isla por el enlace.
  - 8.888 piezas. Se descartaron 59: 44 en la escalera de mano, 3 del dintel del extremo norte y 12 de la viga de celosía en los cruces.

- 2026-10-23 18:50 (hora del log): el **339 carga sin errores nuevos** y sin aviso de huella. Piezas ligeras aplicadas en 0,88 s (unas 36.700 en total, 1,3 veces las de partida). Esperando el veredicto de Carlos: embudo, corredor y costillas.
- 2026-10-23 19:05: lo que dijo Carlos del 339:
  - **Pared:** "aceptable, no bien ni bonito", y "genial por el hueco con escalera". **La ranura abierta con la escalera de mano le encanta:** es un motivo a repetir (ranuras verticales de circulación a la vista).
  - **Pirámide:** "bien, pero esperaba una sala inmensa alrededor del ascensor", porque hay que conectar muchas cintas. Hay que mejorar las esquinas, y que no quede colgando. "Buen principio".
  - **Pasillos:** se queda con el acristalado, pero "me agobia tanta viga alrededor".
- 2026-10-23 19:15: **`340.sav`**, copiado a SaveGames, con vigilante. Contenido:
  - **Sala del ascensor de 320 × 320 m** a 382 m, que integra el puente N–S. Se apoya en 20 pilares de hormigón cada 64 m por el perímetro, de −2 a 378 m.
  - **Embudo desde los bordes de la sala** hasta 566 m, con una boca de 688 m. Las esquinas son bloques escalonados de cimientos 8x4 en grafito, sin paredes cruzadas.
  - **Corredor:** solo cristal, sin pórticos.
  - 14.495 piezas. Descartes, los previstos: 44 en la escalera, 40 cimientos sobre el puente y 2 paredes inclinadas que lo tapaban.
  - Se desconoce la altura del terreno bajo la sala: los pilares bajan a −2 m. Si quedan cortos o enterrados, se verá en el juego.
- 2026-10-23 19:25: Carlos aporta una guía de diseño arquitectónico para Satisfactory; se guarda en `DISENO.md` y se enlaza en las Normas.
- 2026-10-23 19:05 (hora del log): el **340 carga sin errores nuevos** y sin aviso de huella. Piezas ligeras aplicadas en **1,08 s** (unas 42.300, 1,5 veces las de partida). Serie: 0,75 s (27.900) → 0,88 s (36.700) → 1,08 s (42.300).
