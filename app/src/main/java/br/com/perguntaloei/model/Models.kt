package br.com.perguntaloei.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** Níveis de dificuldade das perguntas. */
@Serializable
enum class Difficulty(val label: String, val level: Int) {
    @SerialName("facil") FACIL("Fácil", 1),
    @SerialName("media") MEDIA("Média", 2),
    @SerialName("dificil") DIFICIL("Difícil", 3),
    @SerialName("muito_dificil") MUITO_DIFICIL("Muito difícil", 4);
}

/** Formato da pergunta. */
@Serializable
enum class QuestionFormat(val label: String) {
    @SerialName("multipla_escolha") MULTIPLE_CHOICE("Múltipla escolha"),
    @SerialName("verdadeiro_falso") TRUE_FALSE("Verdadeiro ou falso"),
    @SerialName("aberta") OPEN("Resposta aberta");
}

/** Temas disponíveis no banco de perguntas. */
@Serializable
enum class Theme(val label: String) {
    @SerialName("geografia") GEOGRAFIA("Geografia"),
    @SerialName("historia") HISTORIA("História"),
    @SerialName("ciencia") CIENCIA("Ciência"),
    @SerialName("tecnologia") TECNOLOGIA("Tecnologia"),
    @SerialName("cinema") CINEMA("Cinema"),
    @SerialName("filmes_infantis") FILMES_INFANTIS("Filmes infantis"),
    @SerialName("novelas") NOVELAS("Novelas"),
    @SerialName("televisao") TELEVISAO("Televisão"),
    @SerialName("esportes") ESPORTES("Esportes"),
    @SerialName("marcas") MARCAS("Marcas e slogans"),
    @SerialName("musica") MUSICA("Música"),
    @SerialName("literatura") LITERATURA("Literatura"),
    @SerialName("natureza") NATUREZA("Natureza"),
    @SerialName("cultura_brasileira") CULTURA_BRASILEIRA("Cultura brasileira"),
    @SerialName("curiosidades") CURIOSIDADES("Curiosidades");
}

/**
 * Uma pergunta do banco. Para verdadeiro/falso as alternativas são sempre
 * "Verdadeiro" e "Falso". Para múltipla escolha a resposta é igual a uma das alternativas.
 */
@Serializable
data class Question(
    val id: String,
    val text: String,
    val theme: Theme,
    val subtheme: String,
    val difficulty: Difficulty,
    /** Idade mínima sugerida (faixa etária "N+"). */
    val minAge: Int = 0,
    val format: QuestionFormat,
    val options: List<String> = emptyList(),
    val answer: String,
    /** Sinônimos e variações aceitáveis da resposta correta (para voz e digitação). */
    val synonyms: List<String> = emptyList(),
    val explanation: String,
    val source: String,
    /** Data/contexto de referência para fatos que podem mudar. */
    val referenceDate: String? = null,
    /** Pergunta sobre o Brasil (usada no modo Conhecimentos gerais do Brasil). */
    val brazil: Boolean = false,
) {
    val correctIndex: Int get() = options.indexOf(answer)
    val ageLabel: String get() = if (minAge <= 0) "Livre" else "$minAge+"
}

@Serializable
data class Player(
    val id: String,
    val name: String,
    val age: Int? = null,
)

@Serializable
enum class GameMode(val label: String, val description: String) {
    @SerialName("tema") THEMED_ROUNDS(
        "Rodadas por tema",
        "Cada rodada tem um tema único. Todos respondem uma pergunta do mesmo tema antes de o tema mudar.",
    ),
    @SerialName("quantidade") QUESTION_COUNT(
        "Número de perguntas",
        "Você escolhe quantas perguntas cada jogador vai responder. Os temas se alternam entre os escolhidos.",
    ),
    @SerialName("melhor_de_tres") BEST_OF_THREE(
        "Melhor de três",
        "Campeonato de partidas curtas. Vence a partida quem fizer mais pontos nela. " +
            "É campeão quem vencer 2 partidas primeiro (no máximo 3 partidas).",
    ),
    @SerialName("brasil") BRAZIL(
        "Conhecimentos do Brasil",
        "Rodadas por tema, só com perguntas sobre o Brasil.",
    ),
}

@Serializable
data class GameConfig(
    val mode: GameMode = GameMode.THEMED_ROUNDS,
    /** Rodadas da partida (em "Número de perguntas" = perguntas por jogador). */
    val rounds: Int = 5,
    /** Rodadas por partida no modo Melhor de três. */
    val roundsPerMatch: Int = 2,
    val themes: List<Theme> = Theme.entries,
    /** Dificuldades permitidas para adultos; crianças e adolescentes são adaptados pela idade. */
    val difficulties: Set<Difficulty> = setOf(Difficulty.FACIL, Difficulty.MEDIA, Difficulty.DIFICIL),
    /** Apresentador lê em voz alta. Falso = modo sem voz (tudo na tela, respostas por toque). */
    val voiceHost: Boolean = true,
    /** Respostas faladas (microfone). Falso = só toque. */
    val voiceAnswers: Boolean = true,
)
