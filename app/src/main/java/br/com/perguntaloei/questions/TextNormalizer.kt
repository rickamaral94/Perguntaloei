package br.com.perguntaloei.questions

import java.text.Normalizer

/** Utilidades de texto: normalização (sem acentos/pontuação), similaridade e impressões digitais. */
object TextNormalizer {

    private val diacritics = Regex("\\p{Mn}+")
    private val nonAlnum = Regex("[^a-z0-9 ]")
    private val spaces = Regex("\\s+")

    /** Palavras sem peso de conteúdo, ignoradas na comparação de enunciados. */
    val STOPWORDS = setOf(
        "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das", "e", "em", "no", "na",
        "nos", "nas", "por", "para", "pra", "pelo", "pela", "com", "que", "qual", "quais", "quem", "como", "se",
        "ao", "aos", "the", "foi", "e", "eh", "sao", "seu", "sua", "seus", "suas", "este", "esta", "esse", "essa",
        "isso", "isto", "ou", "mais", "muito", "onde", "quando", "quanto", "quantos", "quantas", "chamado",
        "chamada", "conhecido", "conhecida",
    )

    fun normalize(text: String): String {
        val decomposed = Normalizer.normalize(text.lowercase(), Normalizer.Form.NFD)
        return decomposed.replace(diacritics, "")
            .replace(nonAlnum, " ")
            .replace(spaces, " ")
            .trim()
    }

    fun tokens(text: String): List<String> = normalize(text).split(' ').filter { it.isNotEmpty() }

    fun contentTokens(text: String): Set<String> =
        tokens(text).filter { it !in STOPWORDS && it.length > 1 }.map(::stem).toSet()

    /** Radical simplificado (plural e gênero) para tolerar pequenas variações de escrita. */
    fun stem(token: String): String {
        var t = token
        if (t.length > 4 && t.endsWith("s")) t = t.dropLast(1)
        if (t.length > 4 && (t.endsWith("a") || t.endsWith("o"))) t = t.dropLast(1)
        return t
    }

    /** Similaridade de Jaccard entre os conjuntos de palavras de conteúdo. */
    fun jaccard(a: String, b: String): Double {
        val ta = contentTokens(a)
        val tb = contentTokens(b)
        if (ta.isEmpty() && tb.isEmpty()) return 1.0
        val inter = ta.intersect(tb).size.toDouble()
        val union = ta.union(tb).size.toDouble()
        return if (union == 0.0) 0.0 else inter / union
    }

    fun levenshtein(a: String, b: String): Int {
        if (a == b) return 0
        if (a.isEmpty()) return b.length
        if (b.isEmpty()) return a.length
        var prev = IntArray(b.length + 1) { it }
        var cur = IntArray(b.length + 1)
        for (i in 1..a.length) {
            cur[0] = i
            for (j in 1..b.length) {
                val cost = if (a[i - 1] == b[j - 1]) 0 else 1
                cur[j] = minOf(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
            }
            val tmp = prev; prev = cur; cur = tmp
        }
        return prev[b.length]
    }

    /** 1.0 = idênticos; 0.0 = totalmente diferentes (após normalização). */
    fun similarity(a: String, b: String): Double {
        val na = normalize(a)
        val nb = normalize(b)
        val max = maxOf(na.length, nb.length)
        if (max == 0) return 1.0
        return 1.0 - levenshtein(na, nb).toDouble() / max
    }

    /** Impressão digital estável do enunciado: palavras de conteúdo ordenadas. */
    fun fingerprint(text: String): String = contentTokens(text).sorted().joinToString(" ")

    /**
     * Duas perguntas são "essencialmente iguais" quando os enunciados quase coincidem,
     * ou quando pedem a mesma resposta com enunciados muito parecidos.
     */
    fun isNearDuplicate(textA: String, answerA: String, textB: String, answerB: String): Boolean =
        isNearDuplicatePrepared(normalize(textA), contentTokens(textA), normalize(answerA), normalize(textB), contentTokens(textB), normalize(answerB))

    /** Mesma regra de [isNearDuplicate], com textos já normalizados (para comparar muitos pares). */
    fun isNearDuplicatePrepared(
        normA: String, tokensA: Set<String>, answerA: String,
        normB: String, tokensB: Set<String>, answerB: String,
    ): Boolean {
        val j = jaccardOf(tokensA, tokensB)
        if (j >= 0.8) return true
        // Similaridade ≥ 0,85 exige tamanhos parecidos: a distância nunca é menor que a diferença de tamanho.
        val max = maxOf(normA.length, normB.length)
        if (max == 0) return true
        // Texto quase igual só conta se as palavras importantes também baterem: "capital da Rússia" e
        // "capital da Turquia" têm quase as mesmas letras, mas são perguntas diferentes.
        if (j >= SIMILAR_MIN_JACCARD && kotlin.math.abs(normA.length - normB.length) <= 0.15 * max) {
            if (1.0 - levenshtein(normA, normB).toDouble() / max >= 0.85) return true
        }
        return answerA == answerB && j >= 0.55
    }

    /** Mesmo valor de SIMILAR_MIN_JACCARD no gerador do banco (tools/questions/build_questions.py). */
    const val SIMILAR_MIN_JACCARD = 0.65

    fun jaccardOf(ta: Set<String>, tb: Set<String>): Double {
        if (ta.isEmpty() && tb.isEmpty()) return 1.0
        val inter = ta.count { it in tb }.toDouble()
        val union = (ta.size + tb.size - inter)
        return if (union == 0.0) 0.0 else inter / union
    }
}
