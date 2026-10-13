package br.com.perguntaloei.game

import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat

/** Um trecho de fala do apresentador seguido de uma pausa. */
data class Speech(val text: String, val pauseAfterMs: Long = 350)

/**
 * Textos do apresentador. A leitura da pergunta nunca inclui a resposta: ela só
 * aparece no roteiro do resultado, depois da avaliação.
 */
object PresenterScript {

    fun roundIntro(state: GameState): List<Speech> {
        val round = state.round ?: return emptyList()
        val order = state.turnOrder.joinToString(", ") { it.name }
        val title = when (round.kind) {
            RoundKind.TIEBREAK -> "Desempate!"
            RoundKind.REGULAR -> if (state.config.mode == br.com.perguntaloei.model.GameMode.BEST_OF_THREE) {
                "Partida ${state.match}, rodada ${round.number}."
            } else {
                "Rodada ${round.number} de ${state.roundsInMatch}."
            }
        }
        val theme = round.theme?.let { "Tema: ${it.label}." } ?: "Temas variados."
        return listOf(Speech(title, 300), Speech(theme, 300), Speech("Ordem: $order.", 500))
    }

    /** Escolha determinística entre variações, para o apresentador não soar repetitivo. */
    private fun pick(seed: String, options: List<String>): String = options[Math.floorMod(seed.hashCode(), options.size)]

    /** Anúncio da vez + tema + dificuldade + pergunta + alternativas. */
    fun questionReading(playerName: String, q: Question, includeTurn: Boolean = true): List<Speech> {
        val parts = mutableListOf<Speech>()
        val seed = q.id + playerName
        if (includeTurn) {
            parts += Speech(
                pick(seed, listOf("Vez de $playerName!", "$playerName, é com você!", "Agora é a vez de $playerName!", "Atenção, $playerName!")),
                450,
            )
        }
        parts += Speech("Tema, ${q.theme.label}. Nível ${q.difficulty.label.lowercase()}.", 550)
        parts += Speech(q.text, 750)
        when (q.format) {
            QuestionFormat.MULTIPLE_CHOICE -> q.options.forEachIndexed { i, opt ->
                // Vírgula em vez de dois-pontos: a leitura sai mais fluida.
                parts += Speech("${'A' + i}, $opt.", 420)
            }
            QuestionFormat.TRUE_FALSE -> parts += Speech("Verdadeiro, ou falso?", 450)
            QuestionFormat.OPEN -> parts += Speech("Pode responder com suas palavras.", 450)
        }
        parts += Speech(pick(seed + "fim", listOf("Valendo, $playerName!", "$playerName, pode responder.", "Qual é a sua resposta, $playerName?")), 0)
        return parts
    }

    fun result(state: GameState, record: TurnRecord, q: Question): List<Speech> {
        val parts = mutableListOf<Speech>()
        val name = record.playerName
        val seed = q.id + name
        val answer = if (q.format == QuestionFormat.MULTIPLE_CHOICE) "${'A' + q.correctIndex}, ${q.answer}" else q.answer
        when (record.outcome) {
            Outcome.CORRECT -> parts += Speech(
                pick(seed, listOf("Acertou, $name!", "Isso mesmo, $name!", "Resposta certa, $name!", "Muito bem, $name!")) +
                    if (record.kind == RoundKind.REGULAR) " Mais um ponto." else "",
                400,
            )
            Outcome.WRONG -> parts += Speech(
                pick(seed, listOf("Não foi dessa vez, $name.", "Ih, quase, $name!", "Que pena, $name.")) + " A resposta certa é $answer.",
                400,
            )
            Outcome.SKIPPED -> parts += Speech("Pergunta pulada. A resposta era $answer.", 400)
            Outcome.NO_ANSWER -> parts += Speech("Sem resposta, sem ponto. A resposta era $answer.", 400)
            Outcome.ANNULLED, Outcome.REPLACED_REPEATED -> return listOf(Speech("Pergunta anulada. O placar não mudou.", 300))
        }
        parts += Speech(q.explanation, 500)
        if (record.kind == RoundKind.REGULAR) {
            val pts = state.score(record.playerId)
            parts += Speech("$name está com $pts ${if (pts == 1) "ponto" else "pontos"}.", 400)
        }
        state.nextPlayer?.let { parts += Speech("Próxima vez: ${it.name}.", 0) }
        return parts
    }

    fun clarification(reason: String): List<Speech> = listOf(Speech(reason, 0))

    fun confirmation(description: String): List<Speech> = listOf(Speech("Entendi: $description. Confirma?", 0))
}
