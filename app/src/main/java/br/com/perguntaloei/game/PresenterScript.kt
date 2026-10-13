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

    /** Anúncio da vez + tema + dificuldade + pergunta + alternativas. */
    fun questionReading(playerName: String, q: Question, includeTurn: Boolean = true): List<Speech> {
        val parts = mutableListOf<Speech>()
        if (includeTurn) parts += Speech("Vez de $playerName!", 450)
        parts += Speech("Tema: ${q.theme.label}. Dificuldade: ${q.difficulty.label}.", 500)
        parts += Speech(q.text, 700)
        when (q.format) {
            QuestionFormat.MULTIPLE_CHOICE -> q.options.forEachIndexed { i, opt ->
                parts += Speech("${'A' + i}: $opt.", 450)
            }
            QuestionFormat.TRUE_FALSE -> parts += Speech("Verdadeiro ou falso?", 450)
            QuestionFormat.OPEN -> parts += Speech("Responda com suas palavras.", 450)
        }
        parts += Speech("$playerName, pode responder.", 0)
        return parts
    }

    fun result(state: GameState, record: TurnRecord, q: Question): List<Speech> {
        val parts = mutableListOf<Speech>()
        val name = record.playerName
        val answer = if (q.format == QuestionFormat.MULTIPLE_CHOICE) "${'A' + q.correctIndex}, ${q.answer}" else q.answer
        when (record.outcome) {
            Outcome.CORRECT -> parts += Speech(
                if (record.kind == RoundKind.REGULAR) "Certa resposta, $name! Mais um ponto." else "Certa resposta, $name!",
                400,
            )
            Outcome.WRONG -> parts += Speech("Não foi dessa vez, $name. A resposta certa é: $answer.", 400)
            Outcome.SKIPPED -> parts += Speech("Pergunta pulada. A resposta era: $answer.", 400)
            Outcome.NO_ANSWER -> parts += Speech("Sem resposta, sem ponto. A resposta era: $answer.", 400)
            Outcome.ANNULLED, Outcome.REPLACED_REPEATED -> return listOf(Speech("Pergunta anulada. O placar não mudou.", 300))
        }
        parts += Speech(q.explanation, 500)
        if (record.kind == RoundKind.REGULAR) {
            val pts = state.score(record.playerId)
            parts += Speech("$name tem $pts ${if (pts == 1) "ponto" else "pontos"}.", 400)
        }
        state.nextPlayer?.let { parts += Speech("Próxima vez: ${it.name}.", 0) }
        return parts
    }

    fun clarification(reason: String): List<Speech> = listOf(Speech(reason, 0))

    fun confirmation(description: String): List<Speech> = listOf(Speech("Entendi: $description. Confirma?", 0))
}
