# Guía de contenido · App de estudio PGN 252-2026

Contexto: app de estudio para el concurso de méritos de la Procuraduría General de la Nación (PGN), Convocatoria 252-2026, empleo **Técnico Administrativo 4TM-13, nivel Técnico**. La prueba de conocimientos es eliminatoria (65/100) y pesa 60 %. Todo el contenido va en **español de Colombia**, claro, de nivel técnico, explicado "de cero a técnico".

## Fuentes y vigencia (fecha de referencia: octubre de 2026)

- Usa **normativa vigente**. Ejemplos obligatorios: el Código General Disciplinario es la **Ley 1952 de 2019, reformada por la Ley 2094 de 2021** (la **Ley 734 de 2002 está derogada**); la estructura de la PGN está en el **Decreto Ley 262 de 2000, modificado por el Decreto Ley 1851 de 2021**.
- Verifica cada dato normativo (número de ley, artículo, término, porcentaje, órgano competente) contra fuentes oficiales cuando no estés 100 % seguro: secretariasenado.gov.co, funcionpublica.gov.co (Gestor Normativo), procuraduria.gov.co, corteconstitucional.gov.co, archivogeneral.gov.co, icontec / guías oficiales, suin-juriscol.gov.co. Las herramientas WebSearch y WebFetch se cargan con ToolSearch.
- **No inventes** datos de la convocatoria ni cifras. Si un dato no se puede verificar, no lo conviertas en pregunta; puedes mencionarlo en la explicación marcado como **[COMPLEMENTARIO]** o dejarlo fuera.
- Marca **[COMPLEMENTARIO]** todo lo que no provenga de fuentes oficiales (trucos de memoria, recomendaciones prácticas, buenas prácticas no normativas).
- Datos oficiales del empleo (de la convocatoria): propósito "Apoyar la gestión administrativa y aplicar conocimientos técnicos para el cumplimiento de objetivos y la prestación del servicio de la dependencia"; funciones: registros técnicos y administrativos, informes, recolectar información, apoyo técnico y tecnológico a dependencias y al Ministerio Público, diligencias y trámites, registrar información en el sistema de información, orientar a usuarios internos y externos, generar reportes, elaborar e interpretar cuadros, informes y estadísticas. Ubicaciones: División de Gestión Humana (Bogotá), Procuraduría Provincial de Instrucción (Ibagué), Procuraduría Regional de Instrucción (Atlántico), Procuraduría Delegada con Funciones Mixtas 9 para el seguimiento a los recursos del Sistema General de Regalías (Bogotá). Procesos: Talento Humano – Preventivo – Disciplinario. Competencias: Responsabilidad con la organización (B), Organización del trabajo (B), Gestión de la información (B), Cumplimiento de parámetros de trabajo (C), Objetividad (B).

## Formato de una lección (archivo `content/<UNIDAD>/<id>.json`)

Un objeto JSON con exactamente estos campos:

```json
{
  "id": "2.1",
  "titulo": "…",
  "normas": ["Decreto Ley 262 de 2000, arts. …", "…"],
  "objetivos": ["…"],                                  // sección «¿Qué debo aprender?» (4–6 ítems)
  "explicacion": [ {"subtitulo": "1. …", "parrafos": ["…", "…"]} ],   // 4–7 bloques, de cero a técnico
  "conceptos": [ {"termino": "…", "definicion": "…"} ],              // 8–12
  "confusiones": [ {"concepto": "…", "seConfundeCon": "…", "diferencia": "…"} ],  // 5–7 filas
  "procuraduria": ["…"],                               // relación con la PGN y con el cargo (3–5)
  "altaProbabilidad": ["…"],                           // puntos de alta probabilidad de examen (5–8)
  "ejemplos": [ {"titulo": "…", "caso": "…", "analisis": "…"} ],    // 3 casos de oficina
  "repaso": ["…"],                                     // lista corta (4–6)
  "preguntas": [ /* 16 preguntas */ ]
}
```

Etiquetas permitidas dentro de los textos: `<b>`, `<i>`, `<em>`, `<strong>`, `<u>`, `<br>`. Nada más (ni `<span>`, ni enlaces). Usa comillas tipográficas “ ” o « » dentro del texto, nunca comillas rectas dobles.

### Preguntas

```json
{
  "id": "2.1-01",                 // <id de lección>-NN, de 01 a 16
  "nivel": 1,                     // 1..5
  "tipo": "multiple",             // "competencia" solo en U9
  "enunciado": "…",
  "opciones": ["…", "…", "…", "…"],   // exactamente 4 (A–D)
  "correcta": 0,                  // índice 0–3; varía la posición entre preguntas
  "explicaciones": ["…", "…", "…", "…"], // una por opción: por qué es correcta / por qué es incorrecta
  "concepto": "concepto que debo reforzar (una línea)"
}
```

Reglas de calidad:
- **16 preguntas por lección**, distribución de niveles: N1 básico ×3, N2 aplicación ×4, N3 avanzado ×4, N4 competitivo ×3, N5 simulacro ×2.
- Selección múltiple con **única respuesta**: exactamente una opción correcta e inequívoca; ningún distractor puede ser defendible.
- Al menos la mitad de las preguntas deben ser **casos prácticos de un Técnico Administrativo** (en la PGN o en una entidad pública): radicar, orientar a un usuario, registrar en un sistema, elaborar un informe, archivar, manejar un inventario, etc.
- **Distractores plausibles** (errores típicos, cifras cercanas, normas parecidas) y **opciones de longitud similar** (que la correcta no sea la más larga).
- Evita “todas las anteriores”, “ninguna de las anteriores” y dobles negaciones.
- La explicación de la correcta dice por qué es correcta citando la norma; la de cada distractor dice por qué es incorrecta (no solo “es falsa”).
- Variedad: no repitas la misma idea en dos preguntas de la misma lección.

## Unidad U9 · Competencias comportamentales

- Una lección por competencia: 9.1 Responsabilidad con la organización (B), 9.2 Organización del trabajo (B), 9.3 Gestión de la información (B), 9.4 Cumplimiento de parámetros de trabajo (C), 9.5 Objetividad (B); y 9.6 casos integrados (mezcla de las cinco).
- Todas las preguntas tienen `"tipo": "competencia"` y `"competencia"` con uno de estos valores exactos: `"Responsabilidad con la organización B"`, `"Organización del trabajo B"`, `"Gestión de la información B"`, `"Cumplimiento de parámetros de trabajo C"`, `"Objetividad B"`.
- El `enunciado` es un **caso laboral** de un Técnico Administrativo de la PGN y las 4 opciones son **actuaciones** posibles (todas razonables a primera vista). La correcta es la que mejor representa la competencia en el nivel indicado; las `explicaciones` dicen por qué esa actuación la representa mejor y qué le falta a cada una de las otras.
- Las definiciones y conductas asociadas deben salir del **Diccionario de Competencias Comportamentales de la PGN** (publicado en procuraduria.gov.co). Si no logras consultarlo, explica las competencias con conductas generales y marca esas definiciones como **[COMPLEMENTARIO]**; no presentes como oficial un texto que no verificaste.

## Validación

Después de escribir el archivo ejecuta:

```bash
python3 tools/check_lesson.py content/<UNIDAD>/<id>.json
```

y corrige hasta que diga `OK`. Escribe el archivo con Python (`json.dump(obj, f, ensure_ascii=False, indent=2)`) para evitar errores de escape.
