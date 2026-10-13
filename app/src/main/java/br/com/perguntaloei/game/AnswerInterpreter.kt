package br.com.perguntaloei.game

import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.questions.TextNormalizer

/** Uma hipótese do reconhecedor de fala. [confidence] é nulo quando o serviço não informa. */
data class Transcript(val text: String, val confidence: Float? = null)

/** Escolha que o motor do jogo avalia. */
sealed interface AnswerChoice {
    /** Alternativa escolhida (múltipla escolha e verdadeiro/falso). */
    data class Option(val index: Int) : AnswerChoice

    /** Texto livre (pergunta aberta), avaliado contra resposta e sinônimos. */
    data class Text(val text: String) : AnswerChoice

    /** Decisão do grupo depois de uma resposta aberta ambígua confirmada pelo jogador. */
    data class Judged(val text: String, val correct: Boolean) : AnswerChoice
}

enum class CommandKind { REPEAT, SKIP, DONT_KNOW }

sealed interface Interpretation {
    val heard: String

    /** Comando falado (ex.: "repete"). Não é resposta e não muda o placar. */
    data class Command(val kind: CommandKind, override val heard: String) : Interpretation

    /** Resposta clara: pode ser avaliada imediatamente. */
    data class Clear(val choice: AnswerChoice, val description: String, override val heard: String) : Interpretation

    /** Provável resposta, mas é preciso confirmar a transcrição antes de avaliar. */
    data class NeedsConfirmation(
        val choice: AnswerChoice,
        val description: String,
        val reason: String,
        override val heard: String,
    ) : Interpretation

    /** Não ficou claro qual é a resposta: pedir esclarecimento (sem marcar certo ou errado). */
    data class Ambiguous(val reason: String, override val heard: String, val allowGroupDecision: Boolean = false) : Interpretation

    /** Nada reconhecível como resposta. */
    data class Unclear(override val heard: String) : Interpretation
}

/** Comparação de respostas abertas com a resposta cadastrada e seus sinônimos. */
object AnswerMatcher {

    private val fillerPrefixes = listOf(
        "minha resposta final e", "minha resposta e", "a resposta e", "resposta final", "resposta", "eu acho que e",
        "acho que e", "eu acho que", "acho que", "eu diria", "eu vou de", "vou de", "fico com", "e o", "e a", "e os",
        "e as", "e", "eh", "o", "a", "os", "as", "um", "uma",
    )

    /** Remove muletas do início ("a resposta é", "acho que é", artigos) e converte números falados. */
    fun clean(text: String): String {
        var t = NumberWords.replace(TextNormalizer.normalize(text))
        var changed = true
        while (changed) {
            changed = false
            for (p in fillerPrefixes) {
                if (t == p) continue
                if (t.startsWith("$p ")) { t = t.removePrefix("$p ").trim(); changed = true; break }
            }
        }
        return t
    }

    fun accepted(q: Question): List<String> =
        (listOf(q.answer) + q.synonyms).map { NumberWords.replace(TextNormalizer.normalize(it)) }
            .flatMap { listOf(it, stripArticle(it)) }.filter { it.isNotEmpty() }.distinct()

    private fun stripArticle(s: String): String {
        for (a in listOf("o ", "a ", "os ", "as ")) if (s.startsWith(a)) return s.removePrefix(a)
        return s
    }

    enum class Level { EXACT, CONTAINED, CLOSE, DIFFERENT }

    fun compareOpen(text: String, q: Question): Level {
        val cleaned = clean(text)
        if (cleaned.isEmpty()) return Level.DIFFERENT
        val acc = accepted(q)
        if (cleaned in acc) return Level.EXACT
        val words = cleaned.split(' ')
        // "Contida" só quando o resto da frase é muleta ("acho que é X mesmo"), nunca outras palavras
        // (senão "Rio Grande do Sul" contaria como "Rio").
        if ("nao" !in words && acc.any { a -> onlyFillerAround(words, a.split(' ')) }) return Level.CONTAINED
        if (acc.any { TextNormalizer.similarity(cleaned, it) >= 0.75 }) return Level.CLOSE
        return Level.DIFFERENT
    }

    /** Avaliação final usada pelo motor do jogo. */
    fun isCorrectOpen(text: String, q: Question): Boolean = when (compareOpen(text, q)) {
        Level.EXACT, Level.CONTAINED -> true
        else -> false
    }

    private val fillerWords = setOf(
        "eu", "acho", "que", "e", "eh", "a", "o", "os", "as", "resposta", "minha", "final", "mesmo", "certeza",
        "com", "creio", "seria", "sim", "isso", "claro", "tenho", "foi", "era", "uai", "ne", "hum", "hmm", "bom",
        "entao", "pois", "vou", "de", "dizer", "digo",
    )

    private fun onlyFillerAround(words: List<String>, phrase: List<String>): Boolean {
        val i = indexOfPhrase(words, phrase)
        if (i < 0) return false
        val rest = words.subList(0, i) + words.subList(i + phrase.size, words.size)
        return rest.all { it in fillerWords }
    }

    fun containsPhrase(words: List<String>, phrase: List<String>): Boolean {
        if (phrase.isEmpty() || phrase.size > words.size) return false
        for (i in 0..words.size - phrase.size) {
            if (words.subList(i, i + phrase.size) == phrase) return true
        }
        return false
    }

    fun indexOfPhrase(words: List<String>, phrase: List<String>): Int {
        if (phrase.isEmpty() || phrase.size > words.size) return -1
        for (i in 0..words.size - phrase.size) {
            if (words.subList(i, i + phrase.size) == phrase) return i
        }
        return -1
    }
}

/** Converte números falados ("mil novecentos e cinquenta") em dígitos ("1950"). */
object NumberWords {
    private val units = mapOf(
        "zero" to 0, "um" to 1, "uma" to 1, "dois" to 2, "duas" to 2, "tres" to 3, "quatro" to 4, "cinco" to 5,
        "seis" to 6, "sete" to 7, "oito" to 8, "nove" to 9, "dez" to 10, "onze" to 11, "doze" to 12, "treze" to 13,
        "quatorze" to 14, "catorze" to 14, "quinze" to 15, "dezesseis" to 16, "dezessete" to 17, "dezoito" to 18,
        "dezenove" to 19, "vinte" to 20, "trinta" to 30, "quarenta" to 40, "cinquenta" to 50, "sessenta" to 60,
        "setenta" to 70, "oitenta" to 80, "noventa" to 90, "cem" to 100, "cento" to 100, "duzentos" to 200,
        "duzentas" to 200, "trezentos" to 300, "quatrocentos" to 400, "quinhentos" to 500, "seiscentos" to 600,
        "setecentos" to 700, "oitocentos" to 800, "novecentos" to 900,
    )

    fun replace(normalized: String): String {
        if (normalized.isEmpty()) return normalized
        val words = normalized.split(' ')
        val out = mutableListOf<String>()
        var i = 0
        while (i < words.size) {
            val start = i
            var total = 0
            var current = 0
            var consumed = false
            var j = i
            while (j < words.size) {
                val w = words[j]
                when {
                    w in units -> { current += units.getValue(w); consumed = true; j++ }
                    w == "mil" -> { total += (if (current == 0) 1 else current) * 1000; current = 0; consumed = true; j++ }
                    w == "e" && consumed && j + 1 < words.size && (words[j + 1] in units || words[j + 1] == "mil") -> j++
                    w.all { it.isDigit() } && !consumed -> break
                    else -> break
                }
            }
            // "um"/"uma" isolados são artigos, não números.
            val lone = j - start == 1 && words[start] in setOf("um", "uma")
            if (consumed && !lone) {
                out += (total + current).toString()
                i = j
            } else {
                out += words[i]
                i++
            }
        }
        return out.joinToString(" ")
    }
}

/**
 * Interpreta o que foi dito (ou digitado) diante da pergunta atual. Nunca avalia certo/errado:
 * só identifica a escolha e decide se ela é clara, precisa de confirmação ou de esclarecimento.
 */
object AnswerInterpreter {

    private const val LOW_CONFIDENCE = 0.55f

    private val repeatPhrases = listOf(
        "repete", "repetir", "repita", "pode repetir", "repete por favor", "de novo", "outra vez", "nao ouvi",
        "nao entendi", "como", "o que", "fala de novo", "le de novo", "leia de novo", "mais uma vez",
    )
    private val skipPhrases = listOf("passo", "eu passo", "pular", "pula", "passa", "proxima", "proxima pergunta")
    private val dontKnowPhrases = listOf("nao sei", "nao faco ideia", "sei la", "nao tenho ideia", "desisto")

    private val hedgeTokens = setOf("sera", "talvez", "acho", "duvida", "hum", "hmm", "humm", "ou", "pensar", "espera", "calma", "sabe")
    private val markerTokens = setOf("letra", "alternativa", "opcao", "resposta", "item")
    private val letterNames = mapOf(
        "a" to 0, "ah" to 0, "b" to 1, "be" to 1, "c" to 2, "ce" to 2, "d" to 3, "de" to 3,
    )
    private val ordinals = mapOf("primeira" to 0, "segunda" to 1, "terceira" to 2, "quarta" to 3)

    private val trueStrong = listOf("verdadeiro", "verdadeira", "verdade", "e verdade")
    private val falseStrong = listOf("falso", "falsa", "mentira", "e falso", "nao e verdade", "nao e verdadeiro")
    private val trueWeak = listOf("sim", "certo", "correto", "e sim")
    private val falseWeak = listOf("nao", "errado", "incorreto")

    fun interpretTyped(question: Question, text: String): Interpretation =
        interpret(question, listOf(Transcript(text, 1f)), alwaysConfirm = false, typed = true)

    fun interpret(
        question: Question,
        alternatives: List<Transcript>,
        alwaysConfirm: Boolean = false,
        typed: Boolean = false,
    ): Interpretation {
        val usable = alternatives.filter { it.text.isNotBlank() }
        if (usable.isEmpty()) return Interpretation.Unclear("")
        val first = interpretOne(question, usable[0], alwaysConfirm, typed)
        if (first !is Interpretation.Unclear || usable.size == 1) return first
        // A primeira hipótese não serviu: tenta as demais, mas sempre pede confirmação.
        for (alt in usable.drop(1).take(3)) {
            when (val other = interpretOne(question, alt, alwaysConfirm, typed)) {
                is Interpretation.Clear -> return Interpretation.NeedsConfirmation(
                    other.choice, other.description, "Não tenho certeza do que ouvi.", alt.text,
                )
                is Interpretation.NeedsConfirmation -> return other
                else -> Unit
            }
        }
        return first
    }

    private fun interpretOne(q: Question, t: Transcript, alwaysConfirm: Boolean, typed: Boolean): Interpretation {
        val heard = t.text.trim()
        val norm = NumberWords.replace(TextNormalizer.normalize(heard))
        if (norm.isEmpty()) return Interpretation.Unclear(heard)
        val words = norm.split(' ')
        val lowConfidence = !typed && t.confidence != null && t.confidence in 0f..LOW_CONFIDENCE
        val hedged = words.any { it in hedgeTokens }

        if (!typed) {
            if (matchesCommand(norm, repeatPhrases)) return Interpretation.Command(CommandKind.REPEAT, heard)
            if (matchesCommand(norm, skipPhrases)) return Interpretation.Command(CommandKind.SKIP, heard)
        }
        val dontKnow = dontKnowPhrases.any { norm == it || norm.startsWith("$it ") || norm.endsWith(" $it") }

        val result = when (q.format) {
            QuestionFormat.MULTIPLE_CHOICE -> interpretChoice(q, words)
            QuestionFormat.TRUE_FALSE -> interpretTrueFalse(norm, words)
            QuestionFormat.OPEN -> interpretOpen(q, heard, typed)
        }

        if (dontKnow && (result is Interpretation.Unclear || q.format == QuestionFormat.OPEN && result !is Interpretation.Clear)) {
            return Interpretation.Command(CommandKind.DONT_KNOW, heard)
        }

        return when (result) {
            is Interpretation.Clear -> when {
                dontKnow || hedged -> Interpretation.NeedsConfirmation(result.choice, result.description, "Parece que você ficou em dúvida.", heard)
                lowConfidence -> Interpretation.NeedsConfirmation(result.choice, result.description, "Não tenho certeza do que ouvi.", heard)
                alwaysConfirm && !typed -> Interpretation.NeedsConfirmation(result.choice, result.description, "Confirme a resposta.", heard)
                else -> result.copy(heard = heard)
            }
            is Interpretation.NeedsConfirmation -> result.copy(heard = heard)
            is Interpretation.Ambiguous -> result.copy(heard = heard)
            is Interpretation.Unclear -> Interpretation.Unclear(heard)
            is Interpretation.Command -> result
        }
    }

    private fun matchesCommand(norm: String, phrases: List<String>): Boolean =
        phrases.any { p -> norm == p || norm == "$p por favor" || norm == "por favor $p" || norm == "pode $p" }

    // ---------- múltipla escolha ----------

    private enum class Strength { EXACT, PARTIAL }

    private data class Mention(val index: Int, val strength: Strength, val position: Int)

    private fun interpretChoice(q: Question, words: List<String>): Interpretation {
        val mentions = mutableListOf<Mention>()
        val n = q.options.size

        // Letra/ordinal com marcador ("letra b", "alternativa c", "a segunda").
        for (i in words.indices) {
            val w = words[i]
            val prev = words.getOrNull(i - 1)
            val letter = letterNames[w]
            if (letter != null && letter < n && prev != null && prev in markerTokens) {
                mentions += Mention(letter, Strength.EXACT, i)
            }
            // Ordinal só com contexto: "segunda alternativa", "opção terceira" (evita confundir com "segunda-feira").
            val ord = ordinals[w]
            val next = words.getOrNull(i + 1)
            if (ord != null && ord < n && (prev in markerTokens || next in markerTokens)) mentions += Mention(ord, Strength.EXACT, i)
        }
        // Só a letra ("b", "bê"), "é a b" ou "a segunda".
        val core = AnswerMatcher.clean(words.joinToString(" ")).split(' ').filter { it.isNotEmpty() }
        if (core.size == 1) {
            letterNames[core[0]]?.takeIf { it < n }?.let { mentions += Mention(it, Strength.EXACT, words.size - 1) }
            ordinals[core[0]]?.takeIf { it < n && q.options.none { o -> TextNormalizer.normalize(o).startsWith(core[0]) } }
                ?.let { mentions += Mention(it, Strength.EXACT, words.size - 1) }
        }

        // Texto da alternativa (e sinônimos da resposta correta).
        val optionPhrases = q.options.mapIndexed { idx, opt ->
            val phrases = mutableListOf(phraseOf(opt))
            if (idx == q.correctIndex) phrases += q.synonyms.map(::phraseOf)
            phrases.filter { it.isNotEmpty() }
        }
        val exactHits = mutableListOf<Mention>()
        optionPhrases.forEachIndexed { idx, phrases ->
            for (p in phrases) {
                val pos = AnswerMatcher.indexOfPhrase(words, p)
                if (pos >= 0) { exactHits += Mention(idx, Strength.EXACT, pos); break }
            }
        }
        // Remove alternativas cujo texto está contido no texto de outra que também foi citada.
        val filteredExact = exactHits.filter { hit ->
            exactHits.none { other ->
                other.index != hit.index && optionPhrases[other.index].first().size > optionPhrases[hit.index].first().size &&
                    AnswerMatcher.containsPhrase(optionPhrases[other.index].first(), optionPhrases[hit.index].first())
            }
        }
        mentions += filteredExact

        if (filteredExact.isEmpty()) {
            // Correspondência parcial: palavra exclusiva de uma alternativa ou grafia parecida.
            val tokenSets = q.options.map { TextNormalizer.contentTokens(it) }
            q.options.forEachIndexed { idx, opt ->
                val distinctive = tokenSets[idx].filter { tok -> tok.length >= 3 && tokenSets.withIndex().none { (j, s) -> j != idx && tok in s } }
                val stemmedWords = words.map(TextNormalizer::stem)
                val pos = stemmedWords.indexOfFirst { it in distinctive }
                if (pos >= 0) {
                    mentions += Mention(idx, Strength.PARTIAL, pos)
                } else {
                    val p = phraseOf(opt)
                    val fuzzyPos = fuzzyWindow(words, p)
                    if (fuzzyPos >= 0) mentions += Mention(idx, Strength.PARTIAL, fuzzyPos)
                }
            }
        }

        // Menções negadas ("não é a b") não contam.
        val valid = mentions.filter { m -> !isNegated(words, m.position) }
        val negatedOnly = mentions.isNotEmpty() && valid.isEmpty()
        val indices = valid.map { it.index }.distinct()
        return when {
            negatedOnly -> Interpretation.Ambiguous("Ouvi o que você acha que não é. Qual é a sua resposta?", "")
            indices.isEmpty() -> Interpretation.Unclear("")
            indices.size > 1 -> Interpretation.Ambiguous("Você citou mais de uma alternativa. Qual é a resposta final?", "")
            else -> {
                val idx = indices[0]
                val desc = "Alternativa ${'A' + idx} — ${q.options[idx]}"
                if (valid.any { it.strength == Strength.EXACT }) {
                    Interpretation.Clear(AnswerChoice.Option(idx), desc, "")
                } else {
                    Interpretation.NeedsConfirmation(AnswerChoice.Option(idx), desc, "Entendi só parte da resposta.", "")
                }
            }
        }
    }

    private fun phraseOf(text: String): List<String> =
        NumberWords.replace(TextNormalizer.normalize(text)).split(' ').filter { it.isNotEmpty() }

    private fun fuzzyWindow(words: List<String>, phrase: List<String>): Int {
        if (phrase.isEmpty() || phrase.joinToString(" ").length < 4) return -1
        val size = phrase.size
        if (words.size < size) return -1
        val target = phrase.joinToString(" ")
        for (i in 0..words.size - size) {
            val window = words.subList(i, i + size).joinToString(" ")
            if (TextNormalizer.similarity(window, target) >= 0.8) return i
        }
        return -1
    }

    private fun isNegated(words: List<String>, position: Int): Boolean {
        val from = maxOf(0, position - 4)
        return words.subList(from, position).contains("nao")
    }

    // ---------- verdadeiro ou falso ----------

    private fun interpretTrueFalse(norm: String, words: List<String>): Interpretation {
        val padded = " $norm "
        fun has(list: List<String>) = list.any { padded.contains(" $it ") }
        val strongFalse = has(falseStrong)
        // "não é verdade" contém "verdade": só conta como verdadeiro se não for a forma negada.
        val strongTrue = has(trueStrong) && !padded.contains(" nao e verdade") && !padded.contains(" nao e verdadeiro")
        if (strongTrue && strongFalse) return Interpretation.Ambiguous("Ouvi verdadeiro e falso. Qual é a resposta?", "")
        if (strongTrue) return Interpretation.Clear(AnswerChoice.Option(0), "Verdadeiro", "")
        if (strongFalse) return Interpretation.Clear(AnswerChoice.Option(1), "Falso", "")
        val weakTrue = has(trueWeak)
        val weakFalse = words.any { it in falseWeak }
        if (weakTrue && weakFalse) return Interpretation.Ambiguous("Não ficou claro se é verdadeiro ou falso.", "")
        if (weakTrue) return Interpretation.NeedsConfirmation(AnswerChoice.Option(0), "Verdadeiro", "Você quis dizer verdadeiro?", "")
        if (weakFalse) return Interpretation.NeedsConfirmation(AnswerChoice.Option(1), "Falso", "Você quis dizer falso?", "")
        return Interpretation.Unclear("")
    }

    // ---------- resposta aberta ----------

    private fun interpretOpen(q: Question, heard: String, typed: Boolean): Interpretation {
        val cleaned = AnswerMatcher.clean(heard)
        if (cleaned.isEmpty()) return Interpretation.Unclear("")
        val shown = heard.trim()
        return when (AnswerMatcher.compareOpen(heard, q)) {
            AnswerMatcher.Level.EXACT -> Interpretation.Clear(AnswerChoice.Text(shown), "“$shown”", "")
            AnswerMatcher.Level.CONTAINED -> Interpretation.NeedsConfirmation(
                AnswerChoice.Text(shown), "“$shown”", "Confirme se esta é a sua resposta.", "",
            )
            AnswerMatcher.Level.CLOSE -> Interpretation.Ambiguous(
                if (typed) "A resposta não ficou clara. Confira a grafia ou escreva de outro jeito."
                else "A resposta não ficou clara. Fale de novo, com calma, ou digite.",
                "",
                allowGroupDecision = true,
            )
            // Resposta claramente diferente: em voz, confirma a transcrição antes de marcar errado.
            AnswerMatcher.Level.DIFFERENT -> if (typed) {
                Interpretation.Clear(AnswerChoice.Text(shown), "“$shown”", "")
            } else {
                Interpretation.NeedsConfirmation(AnswerChoice.Text(shown), "“$shown”", "Confirme se foi isso que você disse.", "")
            }
        }
    }
}
