# Estudio PGN · Convocatoria 252-2026 · Técnico Administrativo 4TM-13

Aplicación web de estudio en **un solo archivo** (`index.html`): sin servidor y sin instalación. Funciona en celular y computador, también sin conexión.

## Cómo usarla

1. Descarga `index.html` y ábrelo en el navegador (Chrome, Edge, Safari o Firefox).
2. En el celular puedes guardarlo en el teléfono y abrirlo desde el navegador o publicarlo con GitHub Pages.
3. El progreso se guarda en el navegador (localStorage). Usa **Ajustes → Exportar progreso** con frecuencia para tener una copia en JSON; con **Importar progreso** lo recuperas o lo pasas a otro dispositivo.

## Qué incluye (Fase 1)

- **Motor completo**: lecciones con las 9 secciones (¿Qué debo aprender? → Explicación → Conceptos → Confusiones → Relación con la Procuraduría → Alta probabilidad → Ejemplos → Mini examen → Repaso).
- **Desbloqueo progresivo**: solo 1.1 al inicio; ≥ 80 % desbloquea la siguiente; 70–79 % muestra un refuerzo y repite con preguntas distintas; < 70 % vuelve a la explicación. Cada unidad se desbloquea con el quiz de cierre (20 preguntas, 80 %). U9 va en paralelo desde el inicio. Los simulacros se abren al aprobar U1–U8.
- **Preguntas**: única respuesta A–D, orden de preguntas y opciones aleatorio, niveles N1–N5, explicación de la correcta y de cada distractor, y concepto a reforzar. Para competencias (U9): se indica la competencia evaluada.
- **Seguimiento**: panel por tema (preguntas, correctas, incorrectas, %, clasificación), «Mis errores» (sale de la lista tras 2 aciertos seguidos) y repaso espaciado a 1 día, 4 días y 17 días (2–3 semanas), que aparece primero al entrar.
- **Simulacros**: 80 preguntas mezcladas, sin tema, con temporizador; puntaje, temas débiles, conceptos confundidos y plan de refuerzo.
- **Fechas límite** por unidad (en el JSON o en Ajustes) con aviso de atraso.
- **Datos oficiales de la convocatoria** (empleo, funciones, ejes temáticos, competencias y pruebas) tomados del formato de la Convocatoria 252-2026 (Resolución 212 de 2026, versión 3).
- **Contenido**: U1 Constitución completa con 8 lecciones y 129 preguntas.

## Estructura del repositorio

```
index.html            ← la app (archivo final, generado)
src/app.html          ← motor (HTML + CSS + JS) con el marcador __CONTENIDO_JSON__
content/unidades.json ← meta, datos de la convocatoria y esqueleto de U1–U9
content/U1/*.json     ← una lección por archivo
unidades/U1.json      ← la unidad completa en el formato para pegar en la app (generado)
tools/build.py        ← valida el contenido y genera index.html y unidades/*.json
```

## Agregar una unidad nueva

**Opción A (sin tocar código):** en la app, ve a **Ajustes → Agregar o actualizar unidad**, pega el JSON de la unidad (por ejemplo `U2.json`) y presiona *Validar y guardar*. Queda guardada en ese navegador y viaja en la exportación del progreso.

**Opción B (en el repositorio):** crea `content/U2/2.1.json`, `content/U2/2.2.json`… y ejecuta:

```bash
python3 tools/build.py
```

El formato de la unidad está documentado en el comentario de `src/app.html` y en `unidades/U1.json`. Reglas de validación: mínimo 15 preguntas por lección, 4 opciones, una explicación por opción, nivel 1–5 y un `concepto` por pregunta.
