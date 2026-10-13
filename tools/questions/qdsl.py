"""Mini-linguagem para escrever perguntas: mc() múltipla escolha, tf() verdadeiro/falso, op() aberta."""
from collections import Counter

DIFF = {1: "facil", 2: "media", 3: "dificil", 4: "muito_dificil"}
THEMES = {
    "geo": "geografia", "his": "historia", "cie": "ciencia", "tec": "tecnologia", "cin": "cinema",
    "inf": "filmes_infantis", "nov": "novelas", "tv": "televisao", "esp": "esportes", "mar": "marcas",
    "mus": "musica", "lit": "literatura", "nat": "natureza", "cul": "cultura_brasileira", "cur": "curiosidades",
}
TF = ["Verdadeiro", "Falso"]

_counters = Counter()
QUESTIONS = []


def _add(t, sub, d, age, text, fmt, options, answer, syn, exp, src, br, ref):
    _counters[t] += 1
    q = {
        "id": f"{t}-{_counters[t]:03d}",
        "text": text,
        "theme": THEMES[t],
        "subtheme": sub,
        "difficulty": DIFF[d],
        "minAge": age,
        "format": fmt,
        "options": options,
        "answer": answer,
        "synonyms": list(syn),
        "explanation": exp,
        "source": src,
        "brazil": br,
    }
    if ref:
        q["referenceDate"] = ref
    QUESTIONS.append(q)


def mc(t, sub, d, age, text, options, answer, exp, src, syn=(), br=False, ref=None):
    _add(t, sub, d, age, text, "multipla_escolha", list(options), answer, syn, exp, src, br, ref)


def tf(t, sub, d, age, text, value, exp, src, br=False, ref=None):
    _add(t, sub, d, age, text, "verdadeiro_falso", TF, TF[0] if value else TF[1], (), exp, src, br, ref)


def op(t, sub, d, age, text, answer, syn, exp, src, br=False, ref=None):
    _add(t, sub, d, age, text, "aberta", [], answer, syn, exp, src, br, ref)


