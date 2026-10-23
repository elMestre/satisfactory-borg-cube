# Base de conocimiento: diseño arquitectónico y espacial en Satisfactory

> Aportada por Carlos el 2026-10-23. Se guarda tal cual, solo con el formato pasado a Markdown. Cómo se aplica a este proyecto (donde la producción no se toca) está en `PLAN.md`, en "Normas".

**Versión:** 1.0
**Propósito:** servir como conocimiento de referencia para una LLM que diseña fábricas funcionales, visualmente coherentes, ordenadas y ampliables.
**Alcance:** principios de diseño, planificación espacial, circulación, logística, modularidad, estética y validación. No sustituye una base de datos de recetas ni las instrucciones de comportamiento de la LLM.

## 1. Principios rectores

1. **Diseñar la función y después la envolvente arquitectónica.** Primero se define la producción, el espacio ocupado por máquinas y el flujo de materiales. Después se diseña la fachada, la cubierta, los soportes y la iluminación alrededor de esa distribución.
2. **Reservar más espacio del mínimo calculado.** Las dimensiones de máquinas no representan el espacio total necesario: también hacen falta pasillos, conexiones, curvas de cintas y tuberías, accesos, soportes y margen para modificaciones.
3. **Usar una retícula consistente.** Las foundations proporcionan una cuadrícula de construcción y facilitan alinear máquinas, paredes, pasillos y módulos.
4. **Separar capas de circulación.** Siempre que sea práctico, separar peatones, cintas, tuberías, energía y transporte de vehículos. Evitar que todos los sistemas crucen el mismo espacio.
5. **Hacer visible la lógica de la fábrica.** Una persona debería poder deducir qué entra, qué se transforma y qué sale de cada zona sin seguir cintas al azar.
6. **Diseñar para ampliaciones concretas.** Dejar espacio en los extremos de líneas, laterales de módulos, plantas técnicas y puntos de conexión. No confiar en una futura ampliación que obligue a demoler la fachada o rehacer toda la logística.
7. **La estética debe reforzar la estructura.** Repetición, ritmo, profundidad, proporciones, contraste de materiales y una iluminación deliberada suelen funcionar mejor que añadir decoración aleatoria.
8. **No confundir una imagen bonita con un diseño válido.** Todo plano propuesto debe comprobarse contra dimensiones, entradas/salidas, altura libre, capacidad logística, tecnología desbloqueada y terreno.

## 2. Modelo mental para diseñar una fábrica

Representar cada fábrica en cuatro capas, que se diseñan por separado y luego se integran:

### 2.1 Capa de proceso
- Producto final y producción objetivo, por ejemplo, unidades/minuto.
- Recetas elegidas y alternativas disponibles.
- Número de máquinas, tasas de entrada/salida y velocidad de reloj.
- Subproductos, fluidos, almacenamiento intermedio y residuos.
- Dependencias entre etapas y puntos de control de producción.

### 2.2 Capa logística
- Entrada de materias primas y salida de productos.
- Rutas de cintas, lifts, tuberías, trenes, vehículos o drones.
- Distribución a máquinas: manifold, balanceador u otra topología.
- Capacidad de cada segmento comparada con el caudal requerido.
- Corredores verticales/horizontales y puntos de cruce.
- Accesibilidad para inspeccionar y modificar conexiones.

### 2.3 Capa arquitectónica
- Huella exterior y retícula de foundations.
- Plantas de producción, logística, servicios y circulación.
- Altura entre plantas y huecos técnicos.
- Pilares, vigas, paredes, cubiertas, ventanas, puertas y accesos.
- Fachada, proporciones, materiales, colores, iluminación y señalización.

### 2.4 Capa de expansión
- Espacio reservado para máquinas o módulos adicionales.
- Entradas/salidas de reserva en los bordes.
- Corredores de logística dimensionados para una capacidad objetivo.
- Posibilidad de duplicar una línea sin rehacer las demás.
- Zonas futuras marcadas y accesibles, no ocupadas por decoración irreversible.

## 3. Retícula y dimensiones

- Una foundation estándar mide 8 × 8 m; existen variantes de altura y piezas fraccionarias. Las foundations sirven como suelo y retícula de alineación.
- Las construcciones pueden colocarse sobre foundations con ajustes de posición en pasos de 1 m. Para alinear una base con la cuadrícula mundial, usar la mecánica de alineación indicada en la wiki y comprobar la orientación.
- No asumir que los nodos de recursos están alineados con la retícula mundial: los extractores se alinean con el propio nodo.
- Definir una unidad de diseño propia: por ejemplo, módulos de 4×4, 6×6 u 8×8 foundations. La elección es una convención de proyecto, no una regla del juego.
- Dibujar las huellas de máquinas y sus conexiones antes de fijar la fachada. Añadir un margen de mantenimiento y un corredor de distribución.
- No fijar una altura universal de planta. Calcularla a partir de la máquina más alta, lifts, tuberías, vigas, iluminación y el espacio de acceso. Comprobar colisiones en el juego.
- Si se construye cerca del terreno, comprobar que este no atraviese el suelo. Una plataforma elevada puede facilitar una base limpia y permite alojar servicios por debajo.

**Regla de documentación:** cada plano debe declarar unidades y orientación; preferiblemente, metros y número de foundations. No usar expresiones vagas como "un poco más a la izquierda".

## 4. Zonificación espacial recomendada

Una fábrica modular puede dividirse en estas zonas. No es obligatorio que todas sean plantas distintas.

1. **Entrada de recursos:** punto de llegada claro, con buffers solo donde tengan función.
2. **Procesamiento primario:** fundición, refinado o primera transformación.
3. **Producción intermedia:** subensamblajes agrupados por dependencia.
4. **Ensamblaje final:** cerca de las salidas y con accesos para expansión.
5. **Logística técnica:** corredores de cintas, tuberías, lifts y conexiones entre plantas.
6. **Servicios:** energía, agua, combustible, control y almacenamiento técnico cuando proceda.
7. **Circulación humana:** pasillos, escaleras, plataformas de observación y accesos.
8. **Salida y expedición:** contenedores, estación ferroviaria, puerto de drones u otra conexión.
9. **Reserva de crecimiento:** espacio vacío deliberado con entradas y salidas previstas.

Para productos complejos, valorar fábricas especializadas por familias de producto y una red de transporte entre ellas, en lugar de concentrar toda la cadena en un único edificio. La decisión depende del terreno, distancias, transporte desbloqueado y preferencia del jugador.

## 5. Patrones de distribución

### 5.1 Producción en línea
Las máquinas se colocan siguiendo el orden de las etapas.
- **Ventajas:** lectura intuitiva, fácil seguimiento de flujo y buena visibilidad.
- **Riesgos:** puede generar líneas muy largas y cruces cuando hay muchos ingredientes.
- **Adecuado para:** cadenas cortas, productos con pocas entradas y módulos repetibles.

### 5.2 Filas paralelas
Máquinas idénticas se organizan en filas con corredores de alimentación y recogida.
- **Ventajas:** simetría, ampliación por repetición y fachada regular.
- **Riesgos:** los ingredientes múltiples pueden exigir distribución compleja.
- **Adecuado para:** fundiciones, constructores y grandes grupos de máquinas similares.

### 5.3 Manifold
Una línea de alimentación pasa por distribuidores que alimentan sucesivamente las máquinas.
- **Ventajas:** compacto, fácil de ampliar y normalmente sencillo de construir.
- **Riesgos:** al arrancar, las máquinas más alejadas pueden tardar en llenarse; la cinta principal debe soportar el caudal total requerido.
- **Diseño:** reservar una ruta limpia para la cinta principal y acceso a distribuidores. No afirmar que un manifold está equilibrado solo porque todas las máquinas reciben una conexión.

### 5.4 Balanceador
Divide el flujo entre ramales mediante distribuidores y combinadores.
- **Ventajas:** puede repartir el caudal de forma controlada.
- **Riesgos:** más complejo, ocupa espacio y puede resultar innecesario.
- **Diseño:** usarlo cuando exista una razón cuantitativa o de operación, no como decoración ni como solución automática para cualquier línea.

### 5.5 Producción por plantas
Cada piso representa una etapa, familia de máquinas o capa logística.
- **Ventajas:** reduce la huella del edificio y permite una silueta arquitectónica clara.
- **Riesgos:** múltiples lifts, conexiones verticales difíciles de mantener y accesibilidad limitada.
- **Diseño:** reservar huecos verticales alineados entre plantas y evitar que cada máquina cree una ruta vertical independiente si se puede agrupar.

### 5.6 Falso suelo o planta técnica
Un espacio entre el suelo visible y una segunda plataforma oculta cintas y conexiones.
- **Ventajas:** limpia las áreas de producción y permite fachadas ordenadas.
- **Riesgos:** dificulta diagnosticar bloqueos si no hay acceso; consume altura y materiales.
- **Diseño:** prever registros, accesos y rutas distinguibles. Separar circuitos por dirección o tipo cuando sea útil. Es una técnica comunitaria, no una exigencia del juego.

### 5.7 Módulos repetibles
Un bloque contiene una función completa o una sección estable de producción.
- **Ventajas:** replicación, mantenimiento y blueprinting.
- **Riesgos:** un módulo excesivamente rígido puede no encajar con recetas alternativas o nuevos ratios.
- **Diseño:** especificar dimensiones, entradas, salidas, capacidad, orientación y espacio de conexión. Crear módulos con límites de interfaz explícitos.

## 6. Logística legible y mantenible

- Dibujar las rutas principales antes de conectar cada máquina.
- Agrupar cintas y tuberías en corredores; evitar rutas que atraviesen pasillos o espacios de mantenimiento.
- Usar lifts para cambios verticales cuando reduzcan recorridos desordenados. Los lifts tienen límites de caudal según su nivel: verificar la capacidad en la wiki de la versión actual.
- Los agujeros de suelo para cintas/lifts y tuberías pueden mejorar la limpieza visual, pero hay que validar la conexión y el espacio disponible.
- No ocultar todas las conexiones. Una fábrica debe permitir localizar un bloqueo o cambiar una ruta sin demoler paredes.
- Evitar cruces innecesarios. Si los cruces son inevitables, asignar alturas o corredores diferentes.
- No asumir que una cinta de salida puede transportar toda la producción: comparar caudal calculado y capacidad de la cinta.
- Para fluidos, considerar trazado, desnivel, bombas, buffers y acceso a tuberías. No copiar sin validar una solución de transporte de objetos a fluidos.
- Los corredores deben dejar margen para actualizar cintas a niveles superiores sin rediseñar todo el edificio.
- Señalizar líneas por función, producto o destino con un esquema coherente. La señalización debe ayudar a operar, no convertirse en ruido visual.

## 7. Arquitectura y estética

### 7.1 Composición
- Definir una idea arquitectónica simple antes de decorar: planta industrial, refinería, complejo modular, torre de producción, fábrica integrada en una montaña, etc.
- Usar una jerarquía visual: volumen principal, volúmenes secundarios, zócalo/base, cubierta y detalles.
- Repetir ventanas, pilares, vigas y paneles con un ritmo consistente.
- Evitar una caja plana: introducir retranqueos, marcos, contrafuertes, cambios de altura y profundidad.
- Diseñar una silueta reconocible desde lejos y detalles útiles al acercarse.
- Integrar el edificio con el terreno cuando sea razonable, sin sacrificar el acceso a las máquinas.

### 7.2 Fachadas
- Diseñar la fachada después de confirmar la huella interior.
- Dividir superficies grandes en paños, marcos y franjas horizontales/verticales.
- Usar ventanas donde permitan leer la actividad interior; no es necesario mostrar toda la fábrica.
- Mantener alineados huecos, pilares y cambios de material.
- Incorporar cintas, tuberías, depósitos y conductos exteriores cuando comuniquen la función industrial del edificio.
- No cubrir conexiones importantes con decoración permanente.

### 7.3 Materiales y color
- Limitar cada edificio a una paleta pequeña: un material dominante, uno secundario y un color de acento suelen bastar.
- Reservar colores intensos para identificación, seguridad o elementos focales.
- Mantener el mismo código de color entre edificio, señalización y líneas logísticas cuando ayude a orientarse.
- La disponibilidad de materiales, patrones y elementos decorativos depende de los desbloqueos y compras del juego. Verificar qué está disponible en la partida.

### 7.4 Iluminación
- Usar iluminación funcional en accesos, pasillos, plantas técnicas y puntos de operación.
- Aplicar iluminación de acento para destacar entradas, estructuras o equipos importantes.
- Evitar que todas las superficies emitan luz o que la iluminación compita con las señales.
- Comprobar el resultado de noche y desde las distancias habituales de juego.

### 7.5 Cubierta y estructura
- La cubierta debe corresponderse con la escala del edificio y cubrir los volúmenes previstos.
- Considerar vigas, soportes, pilares, pasarelas y accesos a mantenimiento como parte del diseño.
- No añadir soportes que bloqueen máquinas, cintas o rutas de vehículos.
- Las estructuras decorativas pueden atravesar o intersectar piezas en ciertos casos; verificar cada caso en el juego en lugar de asumir que la geometría es físicamente realista.

## 8. Terreno y emplazamiento

Antes de construir, registrar:
- topografía y desniveles;
- nodos y recursos cercanos;
- rutas de transporte actuales o previstas;
- espacio para expansión horizontal y vertical;
- líneas de visión y silueta desde puntos de acceso;
- obstáculos naturales y riesgo de que el terreno atraviese foundations;
- coste logístico de transportar entradas y salidas.

No elegir una ubicación solo por ser plana. Una meseta, acantilado o costa puede aportar una composición arquitectónica mejor, pero hay que cuantificar el coste de accesos, soportes y transporte.

Una base elevada puede proporcionar un zócalo limpio y un espacio técnico inferior. Su altura debe responder al terreno y a las rutas, no a una cifra universal.

## 9. Blueprints y modularidad

Los Blueprints permiten guardar y repetir configuraciones. Los diseñadores tienen límites de tamaño y desbloqueos concretos; comprobar la versión y el nivel disponible.

Buenas prácticas:
- Crear blueprints de elementos pequeños y estables: filas de máquinas, soportes, pasarelas, esquinas de corredores, iluminación o secciones de fachada.
- Mantener el módulo dentro de los límites del diseñador.
- Definir orientación frontal y punto de referencia; probar el encaje con otro módulo.
- Diseñar conexiones compatibles con el sistema de retícula elegido.
- Separar blueprint funcional y blueprint decorativo cuando la decoración impida adaptar el módulo.
- No crear un blueprint gigante antes de validar los módulos básicos.
- Probar una repetición de dos o tres módulos y comprobar conexiones, colisiones y accesibilidad antes de escalar.

Los Blueprints no eliminan la necesidad de planificar conexiones externas, alineación con el mundo y acceso para mantenimiento.

## 10. Método de diseño recomendado

### Fase A: especificación
1. Definir el producto objetivo y su tasa de producción.
2. Registrar fase del juego, recetas alternativas, máquinas y materiales desbloqueados.
3. Registrar terreno, recursos, logística disponible y restricciones.
4. Decidir si la fábrica será autónoma o recibirá componentes de otras instalaciones.
5. Definir prioridades: estética, compactación, ampliabilidad, facilidad de construcción o rendimiento.

### Fase B: cálculo de proceso
1. Calcular máquinas y flujos de entrada/salida.
2. Identificar subproductos y dependencias.
3. Verificar que las cintas, lifts y tuberías soportan el caudal.
4. Establecer buffers solo donde tengan propósito.
5. Mantener los cálculos en una tabla separada del plano arquitectónico.

### Fase C: plano funcional
1. Dibujar zonas y huellas de máquinas sobre la retícula.
2. Marcar entradas, salidas, corredores y conexiones verticales.
3. Añadir pasillos y espacios de mantenimiento.
4. Reservar expansión.
5. Verificar que las rutas no se cruzan de forma innecesaria.

### Fase D: volumen arquitectónico
1. Definir dimensiones y número de plantas.
2. Comprobar alturas libres, lifts, tuberías y cubierta.
3. Crear zócalo, estructura, fachada y techo.
4. Seleccionar una paleta y un lenguaje visual.
5. Añadir iluminación y señalización.

### Fase E: prototipo y validación
1. Construir una sección representativa a escala real.
2. Probar una máquina, un corredor, una conexión vertical y un fragmento de fachada.
3. Confirmar que las conexiones se pueden construir en el juego.
4. Corregir el módulo antes de duplicarlo.
5. Repetir el módulo y validar el conjunto.
6. Probar el flujo con la fábrica encendida y comprobar bloqueos, caudal y acceso.

### Fase F: documentación
Guardar:
- plano por planta;
- dimensiones totales en metros y foundations;
- orientación y punto de referencia;
- inventario de máquinas;
- mapa de entradas/salidas;
- corredores y conexiones verticales;
- espacios reservados;
- materiales y desbloqueos requeridos;
- lista de pruebas superadas y pendientes.

## 11. Esquema mínimo que debe tener un plano generado por una LLM

Todo diseño detallado debería incluir:

1. **Resumen:** propósito, tasa de producción y estilo arquitectónico.
2. **Suposiciones:** fase del juego, desbloqueos, recetas y limitaciones desconocidas.
3. **Dimensiones globales:** ancho × largo × altura en metros y número de foundations.
4. **Plano de cada planta:** norte/orientación, coordenadas o referencias de retícula, máquinas, pasillos y rutas.
5. **Tabla de máquinas:** tipo, cantidad, orientación, planta y función.
6. **Tabla logística:** material/fluido, origen, destino, caudal, medio de transporte y nivel de cinta/lift.
7. **Sección vertical:** alturas de plantas, falso suelo, lifts, tuberías, vigas y cubierta.
8. **Fachada:** proporciones, materiales, colores, ventanas, accesos e iluminación.
9. **Expansión:** espacio reservado y qué elementos pueden duplicarse.
10. **Validación:** colisiones por comprobar, conexiones inciertas, cuellos de botella y elementos no desbloqueados.

Si no se dispone de coordenadas exactas o de una herramienta de dibujo a escala, el plano debe identificarse como esquemático. No inventar una precisión geométrica que no se ha calculado.

## 12. Criterios de aceptación

Puntuar cada dimensión de 0 a 2: 0 = no cumple; 1 = parcial; 2 = cumple.

| Criterio | Pregunta |
|---|---|
| Producción | ¿Los números y recetas están calculados y son consistentes? |
| Logística | ¿Cada flujo tiene origen, destino y capacidad suficiente? |
| Construibilidad | ¿Las piezas caben, se alinean y se pueden conectar? |
| Legibilidad | ¿Se entiende el flujo sin seguir conexiones al azar? |
| Mantenimiento | ¿Se accede a máquinas, distribuidores y conexiones? |
| Modularidad | ¿Se puede duplicar una sección sin rehacer el edificio? |
| Expansión | ¿Hay espacio y capacidad reservados de forma explícita? |
| Arquitectura | ¿Hay proporciones, profundidad, ritmo y una silueta deliberada? |
| Coherencia visual | ¿Materiales, colores e iluminación siguen un sistema? |
| Terreno | ¿El diseño considera desnivel, clipping y accesos? |

Un diseño no debe declararse terminado si falla en producción, logística o construibilidad, aunque su estética sea buena.

## 13. Errores frecuentes que hay que evitar

- Diseñar la fachada antes de saber cuántas máquinas y conexiones caben.
- Calcular solo la huella de las máquinas y olvidar accesos, cintas y tuberías.
- Hacer edificios demasiado compactos para que sean mantenibles.
- Ocultar toda la logística tras paredes sin accesos.
- Mezclar rutas de productos sin señalización o patrón consistente.
- Usar balanceadores complejos sin una necesidad real.
- Construir una megafábrica monolítica cuando varias fábricas especializadas simplificarían el transporte y la expansión.
- Replicar blueprints antes de probar sus conexiones.
- Suponer que todas las recetas, materiales y piezas decorativas están desbloqueados.
- Proponer medidas aproximadas como si fueran coordenadas exactas.
- Tratar consejos estéticos comunitarios como reglas obligatorias del juego.
- No dejar margen para futuras actualizaciones de cintas, recetas o producción.

## 14. Fuentes de referencia

### Fuentes técnicas primarias
- [Satisfactory Wiki (wiki.gg)](https://satisfactory.wiki.gg/): referencia comunitaria principal del juego.
- [Foundations](https://satisfactory.wiki.gg/wiki/Foundations): retícula, dimensiones y uso de foundations.
- [Blueprint Designer](https://satisfactory.wiki.gg/wiki/Blueprint_Designer): tamaños y límites de los diseñadores.
- [Blueprint](https://satisfactory.wiki.gg/wiki/Blueprint): colocación, orientación y conexiones automáticas.
- [Conveyor Lifts](https://satisfactory.wiki.gg/wiki/Conveyor_Lifts): capacidad y conexiones verticales.
- [Walls](https://satisfactory.wiki.gg/wiki/Walls): paredes y construcción de varias plantas.
- [Display Sign](https://satisfactory.wiki.gg/wiki/Display_Sign): señalización e iluminación con letreros.
- [Customizer](https://satisfactory.wiki.gg/wiki/Customizer): materiales, patrones y colores.
- [Online tools](https://satisfactory.wiki.gg/wiki/Online_tools): herramientas y mapas externos.

### Herramientas de planificación
- [Satisfactory Calculator](https://satisfactory-calculator.com/): planificador de producción, mapa interactivo y blueprints.
- [Satisfactory Modeler](https://satisfactorymodeler.github.io/docs/): calculadora visual para recetas y cantidades de máquinas; no pretende dar un plano espacial exacto.

### Experiencia comunitaria (fuente secundaria, no normativa)
- [Consejos para mejorar el aspecto de las fábricas](https://www.reddit.com/r/SatisfactoryGame/comments/1iyyanh/)
- [Guías personales de organización y falsos suelos](https://www.reddit.com/r/SatisfactoryGame/comments/1fsjxi2/)
- [Consejos de diseño estético](https://www.reddit.com/r/SatisfactoryGame/comments/1fw9tk7/)

**Jerarquía de confianza:** usar la wiki para mecánicas, dimensiones, límites y desbloqueos; las herramientas de planificación para contrastar cálculos; las comunidades para inspiración estética y técnicas prácticas. Verificar en el juego cualquier detalle que dependa de la versión, de los desbloqueos o de una conexión física específica.
