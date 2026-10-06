#!/usr/bin/env python3
"""Valida un archivo de lección: python3 tools/check_lesson.py content/U2/2.1.json"""
import json
import re
import sys
from collections import Counter

COMPETENCIAS = {
    "Responsabilidad con la organización B", "Organización del trabajo B",
    "Gestión de la información B", "Cumplimiento de parámetros de trabajo C", "Objetividad B",
}
SECCIONES = {"objetivos": 4, "explicacion": 4, "conceptos": 8, "confusiones": 5,
             "procuraduria": 3, "altaProbabilidad": 5, "ejemplos": 3, "repaso": 4}
TAG = re.compile(r"<(/?)([a-zA-Z0-9]+)[^>]*>")
PERMITIDAS = {"b", "i", "em", "strong", "u", "br"}


def textos(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from textos(x)
    elif isinstance(o, dict):
        for x in o.values():
            yield from textos(x)


def main(path):
    err = []
    try:
        l = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: JSON inválido: {e}")
        return 1
    lid = l.get("id", "")
    if not re.fullmatch(r"\d+\.\d+", lid):
        err.append("id de lección inválido (ej. 2.1)")
    if not l.get("titulo"):
        err.append("falta titulo")
    if not l.get("normas"):
        err.append("falta normas")
    for k, n in SECCIONES.items():
        if not isinstance(l.get(k), list) or len(l[k]) < n:
            err.append(f"sección '{k}' con menos de {n} elementos")
    for b in l.get("explicacion", []):
        if not b.get("parrafos"):
            err.append("bloque de explicación sin parrafos")
    for c in l.get("conceptos", []):
        if not (c.get("termino") and c.get("definicion")):
            err.append("concepto incompleto")
    for c in l.get("confusiones", []):
        if not (c.get("concepto") and c.get("seConfundeCon") and c.get("diferencia")):
            err.append("fila de confusiones incompleta")
    for e in l.get("ejemplos", []):
        if not (e.get("titulo") and e.get("caso") and e.get("analisis")):
            err.append("ejemplo incompleto")
    qs = l.get("preguntas", [])
    if len(qs) < 16:
        err.append(f"solo {len(qs)} preguntas (se requieren 16)")
    unidad = lid.split(".")[0]
    ids = set()
    niveles = Counter()
    pos = Counter()
    for i, q in enumerate(qs, 1):
        p = f"pregunta {q.get('id', i)}: "
        if q.get("id") != f"{lid}-{i:02d}":
            err.append(p + f"id debe ser {lid}-{i:02d}")
        if q.get("id") in ids:
            err.append(p + "id repetido")
        ids.add(q.get("id"))
        if q.get("nivel") not in (1, 2, 3, 4, 5):
            err.append(p + "nivel debe ser 1–5")
        niveles[q.get("nivel")] += 1
        op = q.get("opciones", [])
        if len(op) != 4 or not all(isinstance(x, str) and x.strip() for x in op):
            err.append(p + "debe tener 4 opciones de texto")
        if len(set(op)) != len(op):
            err.append(p + "opciones repetidas")
        c = q.get("correcta")
        if not isinstance(c, int) or not 0 <= c < 4:
            err.append(p + "correcta fuera de rango")
        else:
            pos[c] += 1
            largos = [len(x) for x in op]
            if len(op) == 4 and largos[c] == max(largos) and largos[c] > 1.5 * sorted(largos)[-2]:
                err.append(p + "la opción correcta es mucho más larga que las demás")
        ex = q.get("explicaciones", [])
        if len(ex) != 4 or not all(isinstance(x, str) and x.strip() for x in ex):
            err.append(p + "debe tener 4 explicaciones")
        if not q.get("enunciado"):
            err.append(p + "falta enunciado")
        if not q.get("concepto"):
            err.append(p + "falta concepto")
        tipo = q.get("tipo")
        if unidad == "9":
            if tipo != "competencia":
                err.append(p + "en U9 tipo debe ser 'competencia'")
            if q.get("competencia") not in COMPETENCIAS:
                err.append(p + "competencia inválida: " + str(q.get("competencia")))
        elif tipo != "multiple":
            err.append(p + "tipo debe ser 'multiple'")
        for t in textos([q.get("enunciado"), op]):
            low = t.lower()
            if "todas las anteriores" in low or "ninguna de las anteriores" in low:
                err.append(p + "no uses 'todas/ninguna de las anteriores'")
    esperado = {1: 3, 2: 4, 3: 4, 4: 3, 5: 2}
    if len(qs) == 16 and dict(niveles) != esperado:
        err.append(f"distribución de niveles {dict(niveles)}; se espera {esperado}")
    if qs and max(pos.values()) > 7:
        err.append(f"la respuesta correcta está demasiadas veces en la misma posición: {dict(pos)}")
    for t in textos(l):
        for m in TAG.finditer(t):
            if m.group(2).lower() not in PERMITIDAS:
                err.append(f"etiqueta no permitida <{m.group(2)}> en: {t[:60]}…")
                break
        if '"' in t:
            err.append(f"comilla recta doble dentro del texto (usa “ ”): {t[:60]}…")
        if "Ley 734" in t and "deroga" not in t.lower():
            err.append(f"menciona la Ley 734 de 2002 sin indicar que está derogada: {t[:60]}…")
    if err:
        print("ERRORES:")
        for e in dict.fromkeys(err):
            print(" -", e)
        return 1
    print(f"OK: {path} · {len(qs)} preguntas · niveles {dict(sorted(niveles.items()))} · posiciones {dict(sorted(pos.items()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
