#!/usr/bin/env python3
"""Procura pares de perguntas em que o enunciado de uma entrega a resposta da outra.

Ex.: "Qual combustível, feito da cana-de-açúcar..." entrega "De qual planta é feito o etanol?".
Como o app sorteia as perguntas de um tema na mesma partida, só olha pares do MESMO tema
que também falam do mesmo assunto (alguma outra palavra importante em comum).

Uso: python3 tools/questions/vazamentos.py [módulos...]   (sem módulos: o banco inteiro;
com módulos: só pares em que pelo menos uma pergunta é desses módulos)
"""
import importlib
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_questions import content, norm  # noqa: E402
from partes import PARTES  # noqa: E402
from qdsl import QUESTIONS  # noqa: E402

GENERICAS = {"verdadeiro", "falso", "brasil", "brasileiro", "brasileira", "agua", "terra", "sol", "lua"}


def main(alvo):
    for m in PARTES:
        if m not in alvo:
            importlib.import_module(m)
    inicio = len(QUESTIONS)
    for m in alvo:
        importlib.import_module(m)
    novas = set(range(inicio, len(QUESTIONS))) if alvo else set(range(len(QUESTIONS)))
    por_tema = defaultdict(list)
    for i, q in enumerate(QUESTIONS):
        por_tema[q["theme"]].append(i)
    achados = []
    for idx in por_tema.values():
        for j in idx:  # j: pergunta cuja resposta pode vazar
            a = norm(QUESTIONS[j]["answer"])
            if len(a) < 5 or a in GENERICAS or a.isdigit():
                continue
            ta = content(QUESTIONS[j]["text"])
            for i in idx:  # i: pergunta cujo enunciado pode entregar
                if i == j or (i not in novas and j not in novas):
                    continue
                texto = norm(QUESTIONS[i]["text"])
                if f" {a} " in f" {texto} " and (content(QUESTIONS[i]["text"]) & ta) - set(a.split()):
                    achados.append((QUESTIONS[i], QUESTIONS[j]))
    for qi, qj in achados:
        print(f"- {qi['id']} \"{qi['text']}\" entrega {qj['id']} \"{qj['text']}\" => {qj['answer']}")
    print(f"{len(achados)} possíveis vazamentos")


if __name__ == "__main__":
    main(sys.argv[1:])
