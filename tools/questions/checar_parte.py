#!/usr/bin/env python3
"""Confere um arquivo novo de perguntas contra o banco inteiro, sem gerar o questions.json.

Uso: python3 tools/questions/checar_parte.py parte6a
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_questions import near_dup, validate  # noqa: E402
from qdsl import QUESTIONS  # noqa: E402

for m in ["parte1", "parte2", "parte3", "parte4", "parte4b", "parte5", "parte6a", "parte6b", "parte6c", "parte6d"]:
    importlib.import_module(m)
antes = len(QUESTIONS)
for m in sys.argv[1:]:
    importlib.import_module(m)
novas = QUESTIONS[antes:]
# Campos de cada pergunta nova (e ids repetidos); quase-duplicatas só entre nova e qualquer outra.
problemas = [p for p in validate(novas) if not p.startswith("quase-duplicatas")]
ids = {}
for q in QUESTIONS:
    ids[q["id"]] = ids.get(q["id"], 0) + 1
problemas += [f"id duplicado {i}" for i, n in ids.items() if n > 1]
for i, q in enumerate(novas):
    for o in QUESTIONS[: antes + i]:
        if near_dup(q, o):
            problemas.append(f"quase-duplicatas: {q['id']} ~ {o['id']}: {q['text']} | {o['text']}")
print(f"{len(novas)} perguntas novas")
if problemas:
    print("PROBLEMAS:")
    for p in problemas:
        print(" -", p)
    sys.exit(1)
print("OK")
