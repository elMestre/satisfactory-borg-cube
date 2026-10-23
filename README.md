# Cubo Borg en Satisfactory

Mi fábrica de Satisfactory (partida *elMestre*, 101 h) funciona, pero es fea. Este repo la va convirtiendo en un cubo kilométrico estilo Borg. Las piezas no se construyen a mano: un script las escribe directamente en el fichero de la partida, y luego compruebo el resultado jugando.

Empieza por **[PLAN.md](PLAN.md)**. Ahí están las decisiones, los datos medidos en la partida, cómo se escriben las piezas y las fases.

- `DISENO.md` es la guía de diseño arquitectónico: principios, patrones, método y criterios de aceptación.
- `catalogo.py` genera `catalogo.json`: cada pieza construible del juego con la ruta exacta que lleva en el save, su receta y si está desbloqueada.
- `muestra.py` hace la fase 0 (muestra de fachada y mirador) y lleva `escribir()`, el motor común que comprueba choques, añade piezas, guarda y verifica.
- `cubo.py` hace la fase 2: genera la versión en curso desde la partida base (fachada sur, sala del ascensor en pirámide invertida, esqueleto y corredores).
- `vista.py` dibuja la planta y los alzados de una partida.
- `334c.sav` es la partida base. En `img/` están las capturas del juego y los dibujos.

Requisitos: Python 3.14 con `pip install satisfactory-save numpy matplotlib`. Los scripts leen el catálogo del juego desde la instalación de Steam en Linux (Proton); las rutas están en `catalogo.py`.
