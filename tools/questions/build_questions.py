#!/usr/bin/env python3
"""Monta e valida o banco de perguntas do PERGUNTÁ-LO-EI.

As perguntas são escritas em parte*.py (dados Python compactos, ver qdsl.py).
Para conferir um arquivo novo rapidamente, sem gerar o JSON: checar_parte.py.
Este script valida tudo e gera app/src/main/assets/questions.json.

Uso: python3 tools/questions/build_questions.py
"""
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "app", "src", "main", "assets", "questions.json")
sys.path.insert(0, HERE)

from qdsl import QUESTIONS  # noqa: E402


# ---------------------------------------------------------------- normalização (igual ao app)
STOP = set("""a o as os um uma uns umas de do da dos das e em no na nos nas por para pra pelo pela com que qual quais
quem como se ao aos the foi eh sao seu sua seus suas este esta esse essa isso isto ou mais muito onde quando quanto
quantos quantas chamado chamada conhecido conhecida""".split())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def stem(t):
    if len(t) > 4 and t.endswith("s"):
        t = t[:-1]
    if len(t) > 4 and (t.endswith("a") or t.endswith("o")):
        t = t[:-1]
    return t


def content(s):
    return {stem(t) for t in norm(s).split() if t not in STOP and len(t) > 1}


def jaccard(a, b):
    ta, tb = content(a), content(b)
    if not ta and not tb:
        return 1.0
    u = len(ta | tb)
    return len(ta & tb) / u if u else 0.0


def lev(a, b):
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[-1]


def similarity(a, b):
    na, nb = norm(a), norm(b)
    m = max(len(na), len(nb))
    return 1.0 if m == 0 else 1 - lev(na, nb) / m


_cache = {}


def _prep(q):
    """Texto normalizado, palavras de conteúdo e resposta normalizada (calculados uma vez)."""
    key = q["id"]
    if key not in _cache:
        _cache[key] = (norm(q["text"]), content(q["text"]), norm(q["answer"]))
    return _cache[key]


# Para o texto quase igual contar como repetição, as palavras importantes também precisam bater:
# "capital da Rússia" e "capital da Turquia" têm quase as mesmas letras, mas são perguntas diferentes.
SIMILAR_MIN_JACCARD = 0.65


def near_dup(a, b):
    na, ta, ra = _prep(a)
    nb, tb, rb = _prep(b)
    u = len(ta | tb)
    j = 1.0 if u == 0 else len(ta & tb) / u
    if j >= 0.8:
        return True
    # Similaridade >= 0.85 exige tamanhos parecidos: evita calcular a distância à toa.
    m = max(len(na), len(nb))
    if j >= SIMILAR_MIN_JACCARD and m and abs(len(na) - len(nb)) / m <= 0.15 and 1 - lev(na, nb) / m >= 0.85:
        return True
    return ra == rb and j >= 0.55


def near_dup_pairs(qs, first_new=0):
    """Pares (i, j) de quase-duplicatas, com j >= first_new.

    Toda regra exige palavras em comum (Jaccard >= 0,55), então só compara perguntas que
    compartilham alguma palavra — usando um índice — em vez de todos os pares.
    """
    index = defaultdict(list)
    empty = []
    for i, q in enumerate(qs):
        tokens = _prep(q)[1]
        if not tokens:
            empty.append(i)
        for t in tokens:
            index[t].append(i)
    pairs = set()
    for j in range(first_new, len(qs)):
        seen = set()
        for t in _prep(qs[j])[1]:
            seen.update(index[t])
        if not _prep(qs[j])[1]:
            seen.update(empty)
        for i in seen:
            if i == j or (i >= first_new and i > j):
                continue  # cada par novo-novo uma vez só
            if near_dup(qs[i], qs[j]):
                pairs.add((min(i, j), max(i, j)))
    return sorted(pairs)


# ---------------------------------------------------------------- validação

def validate(qs):
    problems = []
    ids = Counter(q["id"] for q in qs)
    problems += [f"id duplicado {i}" for i, n in ids.items() if n > 1]
    for q in qs:
        tag = q["id"]
        for f in ("text", "answer", "explanation", "source", "subtheme"):
            if not q[f].strip():
                problems.append(f"{tag}: campo vazio {f}")
        if q["format"] == "multipla_escolha":
            if not 3 <= len(q["options"]) <= 4:
                problems.append(f"{tag}: precisa de 3 ou 4 alternativas")
            if q["answer"] not in q["options"]:
                problems.append(f"{tag}: resposta fora das alternativas")
            n = [norm(o) for o in q["options"]]
            if len(set(n)) != len(n):
                problems.append(f"{tag}: alternativas duplicadas")
        if q["format"] in ("multipla_escolha", "aberta"):
            a = norm(q["answer"])
            if len(a) >= 3 and f" {a} " in f" {norm(q['text'])} ":
                problems.append(f"{tag}: enunciado entrega a resposta")
        if q["format"] == "aberta" and not q["synonyms"]:
            problems.append(f"{tag}: pergunta aberta sem sinônimos")
        if not q["text"].rstrip().endswith(("?", ".")):
            problems.append(f"{tag}: enunciado sem pontuação final")
    for i, j in near_dup_pairs(qs):
        problems.append(f"quase-duplicatas: {qs[j]['id']} ~ {qs[i]['id']}: {qs[j]['text']} | {qs[i]['text']}")
    return problems


def report(qs):
    by_theme = defaultdict(list)
    for q in qs:
        by_theme[q["theme"]].append(q)
    print(f"Total: {len(qs)} perguntas")
    print(f"{'tema':20} total fac med dif mdf kids<=7 kids<=9 brasil aberta v/f")
    for t, lst in by_theme.items():
        c = Counter(q["difficulty"] for q in lst)
        kids7 = sum(1 for q in lst if q["difficulty"] == "facil" and q["minAge"] <= 7)
        kids9 = sum(1 for q in lst if q["difficulty"] == "facil" and q["minAge"] <= 9)
        br = sum(1 for q in lst if q["brazil"])
        ab = sum(1 for q in lst if q["format"] == "aberta")
        vf = sum(1 for q in lst if q["format"] == "verdadeiro_falso")
        print(f"{t:20} {len(lst):5} {c['facil']:3} {c['media']:3} {c['dificil']:3} {c['muito_dificil']:3} {kids7:7} {kids9:7} {br:6} {ab:6} {vf:3}")


if __name__ == "__main__":
    import importlib

    from partes import PARTES

    for m in PARTES:
        importlib.import_module(m)

    problems = validate(QUESTIONS)
    report(QUESTIONS)
    if problems:
        print("\nPROBLEMAS:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"version": 1, "questions": QUESTIONS}, f, ensure_ascii=False, indent=1)
    print(f"\nOK: {OUT}")
