#!/usr/bin/env python3
"""Arma el archivo único de la app.

Lee content/unidades.json (meta + esqueleto de unidades) y, para cada unidad,
las lecciones de content/<ID>/*.json (si la carpeta existe). Valida el
contenido e inserta el JSON resultante en src/app.html -> index.html.

Uso:  python3 tools/build.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TEMPLATE = ROOT / "src" / "app.html"
OUT = ROOT / "index.html"
ART = ROOT / "dist" / "estudio-pgn-252.html"
MINI_N = 8


def clave(path):
    return [int(x) for x in re.findall(r"\d+", path.stem)]


def validar(datos):
    errores, ids = [], set()
    for u in datos["unidades"]:
        for l in u["lecciones"]:
            qs = l.get("preguntas", [])
            if len(qs) < 15:
                errores.append(f"{l['id']}: solo {len(qs)} preguntas (mínimo 15)")
            for q in qs:
                p = f"{q.get('id')}:"
                if q["id"] in ids:
                    errores.append(f"{p} id repetido")
                ids.add(q["id"])
                if not q["id"].startswith(l["id"] + "-"):
                    errores.append(f"{p} no corresponde a la lección {l['id']}")
                n = len(q["opciones"])
                if n != 4:
                    errores.append(f"{p} debe tener 4 opciones (A–D)")
                if not 0 <= q["correcta"] < n:
                    errores.append(f"{p} 'correcta' fuera de rango")
                if len(q["explicaciones"]) != n:
                    errores.append(f"{p} debe tener una explicación por opción")
                if q.get("nivel") not in (1, 2, 3, 4, 5):
                    errores.append(f"{p} nivel debe ser 1–5")
                if q.get("tipo") == "competencia" and not q.get("competencia"):
                    errores.append(f"{p} falta 'competencia'")
                if not q.get("concepto"):
                    errores.append(f"{p} falta 'concepto'")
            for campo in ("objetivos", "explicacion", "conceptos", "confusiones",
                          "procuraduria", "altaProbabilidad", "ejemplos", "repaso"):
                if not l.get(campo):
                    errores.append(f"{l['id']}: falta la sección '{campo}'")
    return errores


def main():
    datos = json.loads((CONTENT / "unidades.json").read_text(encoding="utf-8"))
    for u in datos["unidades"]:
        carpeta = CONTENT / u["id"]
        if carpeta.is_dir():
            u["lecciones"] = [json.loads(p.read_text(encoding="utf-8"))
                              for p in sorted(carpeta.glob("*.json"), key=clave)]
    errores = validar(datos)
    if errores:
        print("Errores de contenido:\n  " + "\n  ".join(errores))
        sys.exit(1)
    js = json.dumps(datos, ensure_ascii=False, separators=(",", ":"))
    js = js.replace("</", "<\\/")  # no cerrar el <script> por accidente
    html = TEMPLATE.read_text(encoding="utf-8").replace("__CONTENIDO_JSON__", js)
    OUT.write_text(html, encoding="utf-8")
    # Versión para publicar como Artifact: el visor agrega su propio esqueleto
    # (doctype, html, head, body, charset y viewport), así que se quitan aquí.
    art = re.sub(r"(?is)<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", html, count=1)
    art = re.sub(r'(?i)<meta (charset|name="viewport"|name="theme-color")[^>]*>\s*', "", art)
    art = re.sub(r"(?i)</head>\s*<body>\s*", "", art, count=1)
    art = re.sub(r"(?i)\s*</body>\s*</html>\s*$", "\n", art, count=1)
    assert art.lstrip().startswith("<title>"), "el <title> debe ir al inicio"
    ART.parent.mkdir(exist_ok=True)
    ART.write_text(art, encoding="utf-8")
    total = sum(len(l["preguntas"]) for u in datos["unidades"] for l in u["lecciones"])
    lecs = sum(len(u["lecciones"]) for u in datos["unidades"])
    print(f"OK: {OUT.name} · {lecs} lecciones · {total} preguntas · {len(html)//1024} KB")
    # Exporta cada unidad con contenido como JSON independiente (formato para pegar en la app)
    (ROOT / "unidades").mkdir(exist_ok=True)
    for u in datos["unidades"]:
        if u["lecciones"]:
            (ROOT / "unidades" / f"{u['id']}.json").write_text(
                json.dumps(u, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
