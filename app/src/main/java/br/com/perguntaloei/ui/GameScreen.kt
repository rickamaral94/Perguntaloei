package br.com.perguntaloei.ui

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.animation.fadeIn
import androidx.compose.animation.scaleIn
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.LiveRegionMode
import androidx.compose.ui.semantics.liveRegion
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import br.com.perguntaloei.AppDialog
import br.com.perguntaloei.AppViewModel
import br.com.perguntaloei.Pending
import br.com.perguntaloei.Screen
import br.com.perguntaloei.VoiceUi
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.GameState
import br.com.perguntaloei.game.Outcome
import br.com.perguntaloei.game.Phase
import br.com.perguntaloei.game.RoundKind
import br.com.perguntaloei.game.TiePurpose
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Question
import br.com.perguntaloei.model.QuestionFormat
import br.com.perguntaloei.ui.components.ArcadeButton
import br.com.perguntaloei.ui.components.MicIndicator
import br.com.perguntaloei.ui.components.PixelPanel
import br.com.perguntaloei.ui.components.PixelText
import br.com.perguntaloei.ui.components.StarField
import br.com.perguntaloei.ui.components.Tag
import br.com.perguntaloei.ui.theme.Arcade

@Composable
fun GameScreen(vm: AppViewModel) {
    val state = vm.game ?: run {
        LaunchedEffect(Unit) { vm.go(Screen.HOME) }
        return
    }
    Box(Modifier.fillMaxSize()) {
        StarField()
        BoxWithConstraints(Modifier.fillMaxSize()) {
            val wide = maxWidth >= 840.dp || (maxWidth >= 600.dp && maxWidth > maxHeight)
            Column(Modifier.fillMaxSize().padding(horizontal = 16.dp, vertical = 10.dp)) {
                TopBar(vm, state)
                Spacer(Modifier.height(8.dp))
                if (wide) {
                    Row(Modifier.fillMaxSize(), horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                        Column(Modifier.weight(0.62f).verticalScroll(rememberScrollState())) {
                            MainArea(vm, state)
                            Spacer(Modifier.height(24.dp))
                        }
                        Column(Modifier.weight(0.38f).verticalScroll(rememberScrollState())) {
                            SidePanel(vm, state)
                        }
                    }
                } else {
                    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
                        MainArea(vm, state)
                        Spacer(Modifier.height(14.dp))
                        SidePanel(vm, state)
                        Spacer(Modifier.height(24.dp))
                    }
                }
            }
        }
    }
}

@Composable
private fun TopBar(vm: AppViewModel, state: GameState) {
    Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(10.dp)) {
        ArcadeButton("◀ Início", { vm.go(Screen.HOME) }, color = Arcade.Cyan, minHeight = 44.dp, fontSize = 14.sp)
        ArcadeButton("📋 Histórico", { vm.go(Screen.LOG) }, color = Arcade.Purple, minHeight = 44.dp, fontSize = 14.sp)
        Spacer(Modifier.weight(1f))
        if (!state.finished) {
            ArcadeButton("Encerrar", { vm.dialog = AppDialog.ConfirmEndGame }, color = Arcade.Red, minHeight = 44.dp, fontSize = 14.sp)
        }
    }
}

/** Rodada, tema e quem está com a vez: sempre visíveis. */
@Composable
private fun Hud(state: GameState, currentTheme: br.com.perguntaloei.model.Theme?) {
    val round = state.round
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Yellow, padding = 10.dp) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            val roundText = when {
                round == null -> if (state.finished) "FIM DE JOGO" else "PLACAR"
                round.kind == RoundKind.TIEBREAK -> "DESEMPATE ${round.number}"
                state.config.mode == GameMode.BEST_OF_THREE -> "PARTIDA ${state.match}/3 · RODADA ${round.number}/${state.roundsInMatch}"
                else -> "RODADA ${round.number}/${state.roundsInMatch}"
            }
            PixelText(roundText, size = 11.sp, modifier = Modifier.weight(1f), shadow = Color.Transparent)
        }
        if (round != null) {
            Spacer(Modifier.height(6.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically) {
                when {
                    round.theme != null -> ThemeTag(round.theme)
                    currentTheme != null && state.phase != Phase.ROUND_INTRO -> ThemeTag(currentTheme)
                    else -> Tag("Temas variados", Arcade.Muted)
                }
            }
        }
        val current = state.currentPlayer
        if (current != null && (state.phase == Phase.ASKING || state.phase == Phase.REVEAL)) {
            Spacer(Modifier.height(8.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("VEZ DE ", color = Arcade.Muted, fontWeight = FontWeight.Bold, fontSize = 16.sp)
                Text(current.name.uppercase(), color = Arcade.Yellow, fontWeight = FontWeight.Black, fontSize = 28.sp, modifier = Modifier.semantics { liveRegion = LiveRegionMode.Polite })
                current.age?.let { Text("  ($it anos)", color = Arcade.Muted, fontSize = 15.sp) }
            }
        }
    }
}

@Composable
private fun MainArea(vm: AppViewModel, state: GameState) {
    Hud(state, vm.engine.currentQuestion(state)?.theme)
    state.notice?.takeIf { state.phase != Phase.REVEAL }?.let {
        Spacer(Modifier.height(8.dp))
        Notice(it)
    }
    Spacer(Modifier.height(10.dp))
    when (state.phase) {
        Phase.ROUND_INTRO -> RoundIntro(vm, state)
        Phase.ASKING -> Asking(vm, state)
        Phase.REVEAL -> Reveal(vm, state)
        Phase.MATCH_END, Phase.GAME_OVER -> EndPanel(vm, state)
    }
}

@Composable
private fun Notice(text: String) {
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Orange, padding = 10.dp) {
        Text("ℹ️ $text", color = Arcade.White, fontSize = 15.sp)
    }
}

// ---------------------------------------------------------------- introdução da rodada

@Composable
private fun RoundIntro(vm: AppViewModel, state: GameState) {
    val round = state.round ?: return
    val scale by animateFloatAsState(1f, spring(Spring.DampingRatioMediumBouncy), label = "intro")
    PixelPanel(Modifier.fillMaxWidth().scale(scale), border = Arcade.Magenta) {
        PixelText(
            if (round.kind == RoundKind.TIEBREAK) "DESEMPATE!" else "RODADA ${round.number}",
            size = 20.sp, color = Arcade.Yellow, modifier = Modifier.fillMaxWidth(), align = TextAlign.Center,
        )
        Spacer(Modifier.height(10.dp))
        Text(
            round.theme?.let { "${Arcade.themeIcon(it)} Tema: ${it.label}" } ?: "Temas variados para cada jogador",
            color = round.theme?.let { Arcade.themeColor(it) } ?: Arcade.White,
            fontSize = 24.sp, fontWeight = FontWeight.Black, textAlign = TextAlign.Center, modifier = Modifier.fillMaxWidth(),
        )
        if (round.kind == RoundKind.TIEBREAK) {
            Spacer(Modifier.height(6.dp))
            Text(
                "Pergunta inédita para cada empatado. Se só um acertar, vence. Se ninguém ou mais de um acertar, há nova pergunta. Os pontos do placar não mudam.",
                color = Arcade.Muted, fontSize = 15.sp, textAlign = TextAlign.Center,
            )
        }
        Spacer(Modifier.height(12.dp))
        Text("Ordem desta rodada:", color = Arcade.Muted, fontSize = 15.sp)
        state.turnOrder.forEachIndexed { i, p ->
            Text("${i + 1}. ${p.name}", color = Arcade.White, fontSize = 20.sp, fontWeight = FontWeight.Bold)
        }
        Spacer(Modifier.height(14.dp))
        ArcadeButton("Começar rodada ▶", { vm.dispatch(GameAction.BeginRound) }, Modifier.fillMaxWidth(), color = Arcade.Green, minHeight = 60.dp, fontSize = 19.sp)
        if (round.kind == RoundKind.TIEBREAK) {
            Spacer(Modifier.height(10.dp))
            ArcadeButton("Aceitar empate", { vm.dispatch(GameAction.AcceptTie) }, Modifier.fillMaxWidth(), color = Arcade.Muted)
        }
    }
}

// ---------------------------------------------------------------- pergunta

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun Asking(vm: AppViewModel, state: GameState) {
    val q = vm.engine.currentQuestion(state) ?: return
    val slot = state.round?.currentSlot ?: return
    val v = vm.voice
    val canAnswer = (v.readingDone || v.touchMode) && !v.listening && v.pending == null

    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.themeColor(q.theme)) {
        FlowRow(horizontalArrangement = Arrangement.spacedBy(6.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
            ThemeTag(q.theme)
            Tag(q.subtheme, Arcade.PanelLight, textColor = Arcade.White)
            Tag(q.difficulty.label, difficultyColor(q))
            Tag("Faixa ${q.ageLabel}", Arcade.Muted)
            Tag(q.format.label, Arcade.Cyan)
            if (slot.reusedFromHistory) Tag("Já usada em partida anterior", Arcade.Orange) else Tag("Inédita", Arcade.Green)
            if (slot.difficultyAdjusted) Tag("Nível ajustado", Arcade.Purple)
            if (q.brazil) Tag("Brasil", Arcade.Yellow)
        }
        Spacer(Modifier.height(12.dp))
        Text(q.text, color = Arcade.White, fontSize = 24.sp, lineHeight = 32.sp, fontWeight = FontWeight.Bold)
        q.referenceDate?.let {
            Spacer(Modifier.height(4.dp))
            Text("Referência: $it", color = Arcade.Muted, fontSize = 13.sp)
        }
        Spacer(Modifier.height(14.dp))
        when (q.format) {
            QuestionFormat.MULTIPLE_CHOICE, QuestionFormat.TRUE_FALSE -> {
                val colors = listOf(Arcade.Cyan, Arcade.Yellow, Arcade.Green, Arcade.Magenta)
                q.options.forEachIndexed { i, opt ->
                    val label = if (q.format == QuestionFormat.MULTIPLE_CHOICE) "${'A' + i})  $opt" else opt
                    ArcadeButton(
                        label, { vm.touchOption(i) },
                        Modifier.fillMaxWidth().padding(vertical = 5.dp),
                        color = if (q.format == QuestionFormat.TRUE_FALSE) (if (i == 0) Arcade.Green else Arcade.Red) else colors[i % 4],
                        enabled = canAnswer, minHeight = 58.dp, fontSize = 19.sp,
                    )
                }
            }
            QuestionFormat.OPEN -> OpenAnswerBox(vm, enabled = canAnswer)
        }
        if (!v.readingDone && !v.touchMode) {
            Spacer(Modifier.height(6.dp))
            Text("As alternativas liberam quando o apresentador terminar de ler (ou toque em Responder tocando).", color = Arcade.Muted, fontSize = 13.sp)
        }
    }
    Spacer(Modifier.height(10.dp))
    VoiceStatus(vm, v, state)
    v.pending?.let {
        Spacer(Modifier.height(10.dp))
        PendingPanel(vm, it, q)
    }
    Spacer(Modifier.height(12.dp))
    Controls(vm, state, v)
}

private fun difficultyColor(q: Question) = when (q.difficulty.level) {
    1 -> Arcade.Green
    2 -> Arcade.Yellow
    3 -> Arcade.Orange
    else -> Arcade.Red
}

@Composable
private fun OpenAnswerBox(vm: AppViewModel, enabled: Boolean) {
    var text by remember { mutableStateOf("") }
    Text("Resposta aberta: fale a resposta ou digite abaixo.", color = Arcade.Muted, fontSize = 15.sp)
    Spacer(Modifier.height(6.dp))
    OutlinedTextField(
        value = text, onValueChange = { text = it.take(80) }, enabled = enabled,
        label = { Text("Digite a resposta") }, singleLine = true, modifier = Modifier.fillMaxWidth(),
        colors = fieldColors(), keyboardOptions = KeyboardOptions(imeAction = ImeAction.Done),
        keyboardActions = KeyboardActions(onDone = { if (text.isNotBlank()) { vm.typedAnswer(text); text = "" } }),
    )
    Spacer(Modifier.height(8.dp))
    ArcadeButton("Enviar resposta", { vm.typedAnswer(text); text = "" }, Modifier.fillMaxWidth(), enabled = enabled && text.isNotBlank(), color = Arcade.Green)
}

@Composable
private fun VoiceStatus(vm: AppViewModel, v: VoiceUi, state: GameState) {
    val border = when {
        v.listening -> Arcade.Red
        v.speaking -> Arcade.Cyan
        else -> Arcade.PanelLight
    }
    PixelPanel(Modifier.fillMaxWidth().semantics { liveRegion = LiveRegionMode.Polite }, border = border, padding = 10.dp) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            MicIndicator(v.listening, v.micLevel)
            Spacer(Modifier.width(12.dp))
            Column(Modifier.weight(1f)) {
                val title = when {
                    v.listening && v.listeningForConfirmation -> "🎤 OUVINDO — diga SIM ou NÃO"
                    v.listening -> "🎤 MICROFONE ATIVO — ${state.currentPlayer?.name ?: ""}, fale sua resposta"
                    v.speaking -> "🔊 Apresentador falando… aguarde"
                    v.pending != null -> "⏸ Aguardando confirmação"
                    v.readingDone || v.touchMode -> "Microfone desligado. Responda tocando ou toque em Ouvir resposta."
                    else -> "Preparando a pergunta…"
                }
                Text(title, color = if (v.listening) Arcade.Red else Arcade.White, fontWeight = FontWeight.Bold, fontSize = 17.sp)
                if (v.listening && v.partial.isNotBlank()) Text("“${v.partial}”", color = Arcade.Yellow, fontSize = 17.sp)
                v.heard?.takeIf { !v.listening && it.isNotBlank() }?.let { Text("Ouvi: “$it”", color = Arcade.Yellow, fontSize = 17.sp) }
                v.message?.let { Text(it, color = Arcade.Orange, fontSize = 15.sp) }
            }
        }
        if (v.listening) {
            Spacer(Modifier.height(8.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                ArcadeButton("■ Parar e avaliar", { vm.stopListening() }, Modifier.weight(1f), color = Arcade.Yellow, minHeight = 48.dp, fontSize = 15.sp)
                ArcadeButton("✕ Cancelar", { vm.cancelListening() }, Modifier.weight(1f), color = Arcade.Red, minHeight = 48.dp, fontSize = 15.sp)
            }
        }
    }
}

@Composable
private fun PendingPanel(vm: AppViewModel, p: Pending, q: Question) {
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Yellow, background = Arcade.PanelLight) {
        when (p) {
            is Pending.Confirm -> {
                Text(p.reason, color = Arcade.Muted, fontSize = 15.sp)
                if (p.heard.isNotBlank()) Text("Transcrição: “${p.heard}”", color = Arcade.White, fontSize = 17.sp)
                Text("Resposta entendida: ${p.description}", color = Arcade.Yellow, fontSize = 20.sp, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(10.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("✓ Sim, é essa", { vm.resolvePending(true) }, Modifier.weight(1f), color = Arcade.Green)
                    ArcadeButton("✕ Não", { vm.resolvePending(false) }, Modifier.weight(1f), color = Arcade.Red)
                }
            }
            is Pending.Clarify -> {
                Text("Não ficou claro", color = Arcade.Yellow, fontSize = 20.sp, fontWeight = FontWeight.Bold)
                if (p.heard.isNotBlank()) Text("Transcrição: “${p.heard}”", color = Arcade.White, fontSize = 17.sp)
                Text(p.reason, color = Arcade.White, fontSize = 16.sp)
                Spacer(Modifier.height(10.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("Responder de novo", { vm.dismissPending() }, Modifier.weight(1f), color = Arcade.Cyan, fontSize = 15.sp)
                    if (p.allowGroupDecision) {
                        ArcadeButton("Manter esta resposta", { vm.resolvePending(true) }, Modifier.weight(1f), color = Arcade.Yellow, fontSize = 15.sp)
                    }
                }
            }
            is Pending.GroupDecision -> {
                Text("Decisão do grupo", color = Arcade.Yellow, fontSize = 20.sp, fontWeight = FontWeight.Bold)
                Text("Resposta do jogador: “${p.text}”", color = Arcade.White, fontSize = 18.sp)
                Text("Resposta cadastrada: ${q.answer}", color = Arcade.Green, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                if (q.synonyms.isNotEmpty()) Text("Também valem: ${q.synonyms.joinToString(", ")}", color = Arcade.Muted, fontSize = 14.sp)
                Text("A resposta dita é equivalente? O grupo decide.", color = Arcade.Muted, fontSize = 15.sp)
                Spacer(Modifier.height(10.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("Aceitar como certa", { vm.groupDecision(true) }, Modifier.weight(1f), color = Arcade.Green, fontSize = 15.sp)
                    ArcadeButton("Marcar errada", { vm.groupDecision(false) }, Modifier.weight(1f), color = Arcade.Red, fontSize = 15.sp)
                }
            }
            is Pending.ConfirmSkip -> {
                Text("Ouvi “${p.heard}”. Pular esta pergunta (sem ponto)?", color = Arcade.White, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(10.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("Sim, pular", { vm.resolvePending(true) }, Modifier.weight(1f), color = Arcade.Orange)
                    ArcadeButton("Não", { vm.resolvePending(false) }, Modifier.weight(1f), color = Arcade.Cyan)
                }
            }
            is Pending.ConfirmNoAnswer -> {
                Text("Ouvi “${p.heard}”. Encerrar a vez sem ponto?", color = Arcade.White, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(10.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("Sim, encerrar", { vm.resolvePending(true) }, Modifier.weight(1f), color = Arcade.Orange)
                    ArcadeButton("Não", { vm.resolvePending(false) }, Modifier.weight(1f), color = Arcade.Cyan)
                }
            }
        }
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun Controls(vm: AppViewModel, state: GameState, v: VoiceUi) {
    val asking = state.phase == Phase.ASKING
    val reveal = state.phase == Phase.REVEAL
    val micAllowed = state.config.voiceAnswers && vm.recognitionAvailable
    FlowRow(horizontalArrangement = Arrangement.spacedBy(10.dp), verticalArrangement = Arrangement.spacedBy(10.dp), maxItemsInEachRow = 2) {
        val m = Modifier.weight(1f)
        ArcadeButton("Repetir", { vm.repeatQuestion() }, m, enabled = asking && !v.listening, color = Arcade.Cyan, icon = "🔁", fontSize = 15.sp)
        ArcadeButton(
            "Ouvir resposta", { vm.listenForAnswer() }, m,
            enabled = asking && micAllowed && !v.listening && (v.readingDone || v.touchMode),
            color = Arcade.Red, textColor = Arcade.Ink, icon = "🎤", fontSize = 15.sp,
        )
        ArcadeButton("Responder tocando", { vm.answerByTouch() }, m, enabled = asking && !(v.touchMode && !v.speaking && !v.listening), color = Arcade.Yellow, icon = "👆", fontSize = 15.sp)
        ArcadeButton("Pular", { vm.dispatch(GameAction.Skip) }, m, enabled = asking && !v.listening, color = Arcade.Orange, icon = "⏭", fontSize = 15.sp)
        ArcadeButton("Encerrar a vez", { vm.dispatch(GameAction.NoAnswer) }, m, enabled = asking && !v.listening, color = Arcade.Orange, icon = "⏹", fontSize = 15.sp)
        ArcadeButton("Anular pergunta", { vm.dialog = AppDialog.AnnulReasons }, m, enabled = (asking || reveal) && !v.listening, color = Arcade.Purple, icon = "🚫", fontSize = 15.sp)
        ArcadeButton(
            "Desfazer último ponto", { vm.dispatch(GameAction.Undo) }, Modifier.fillMaxWidth(),
            enabled = reveal && state.revealRecord?.let { it.outcome != Outcome.ANNULLED && it.outcome != Outcome.REPLACED_REPEATED } == true,
            color = Arcade.Muted, icon = "↩", fontSize = 15.sp,
        )
    }
}

// ---------------------------------------------------------------- resultado da pergunta

@Composable
private fun Reveal(vm: AppViewModel, state: GameState) {
    val record = state.revealRecord ?: return
    val q = vm.engine.question(record.questionId)
    val (title, color) = when (record.outcome) {
        Outcome.CORRECT -> "✔ CERTO!" to Arcade.Green
        Outcome.WRONG -> "✘ ERRADO" to Arcade.Red
        Outcome.SKIPPED -> "⏭ PULADA" to Arcade.Orange
        Outcome.NO_ANSWER -> "⏹ SEM RESPOSTA" to Arcade.Orange
        Outcome.ANNULLED, Outcome.REPLACED_REPEATED -> "🚫 ANULADA" to Arcade.Purple
    }
    AnimatedVisibility(visible = true, enter = scaleIn() + fadeIn()) {
        PixelPanel(Modifier.fillMaxWidth(), border = color) {
            PixelText(title, size = 22.sp, color = color, modifier = Modifier.fillMaxWidth(), align = TextAlign.Center, shadow = Arcade.Ink)
            Spacer(Modifier.height(10.dp))
            Text(q.text, color = Arcade.Muted, fontSize = 16.sp)
            Spacer(Modifier.height(8.dp))
            record.givenAnswer?.let {
                Text("Resposta de ${record.playerName}: $it (${record.method.label})", color = Arcade.White, fontSize = 18.sp)
            }
            if (record.outcome != Outcome.ANNULLED && record.outcome != Outcome.REPLACED_REPEATED) {
                val ans = if (q.format == QuestionFormat.MULTIPLE_CHOICE) "${'A' + q.correctIndex}) ${q.answer}" else q.answer
                Text("Resposta certa: $ans", color = Arcade.Green, fontSize = 21.sp, fontWeight = FontWeight.Black)
                Spacer(Modifier.height(8.dp))
                Text(q.explanation, color = Arcade.White, fontSize = 17.sp)
                Spacer(Modifier.height(4.dp))
                Text("Fonte: ${q.source}", color = Arcade.Muted, fontSize = 13.sp)
            }
            state.notice?.let { Spacer(Modifier.height(6.dp)); Text(it, color = Arcade.Orange, fontSize = 15.sp) }
            Spacer(Modifier.height(10.dp))
            val pointsText = when {
                record.kind == RoundKind.TIEBREAK -> if (record.outcome == Outcome.CORRECT) "Acertou o desempate (o placar não muda)." else "Não acertou o desempate."
                record.points > 0 -> "+${record.points} ponto para ${record.playerName}. Total: ${state.score(record.playerId)}"
                else -> "Nenhum ponto. ${record.playerName} continua com ${state.score(record.playerId)}."
            }
            Text(pointsText, color = Arcade.Yellow, fontSize = 18.sp, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(10.dp))
            val next = state.nextPlayer
            Text(
                when {
                    next != null && state.isLastTurnOfRound -> "Fim da rodada. Próxima vez: ${next.name} (nova rodada)"
                    next != null -> "Próxima vez: ${next.name}"
                    else -> "Última pergunta desta etapa."
                },
                color = Arcade.Cyan, fontSize = 19.sp, fontWeight = FontWeight.Bold,
            )
            Spacer(Modifier.height(12.dp))
            ArcadeButton("Continuar ▶", { vm.dispatch(GameAction.Next) }, Modifier.fillMaxWidth(), color = Arcade.Green, minHeight = 60.dp, fontSize = 19.sp)
        }
    }
    Spacer(Modifier.height(12.dp))
    Controls(vm, state, vm.voice)
}

// ---------------------------------------------------------------- fim de partida / jogo

@Composable
private fun EndPanel(vm: AppViewModel, state: GameState) {
    fun names(ids: List<String>) = joinNames(ids.mapNotNull { state.player(it)?.name })
    val tie = state.tie
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Yellow) {
        val title = when {
            state.finished -> "FIM DE JOGO"
            state.phase == Phase.MATCH_END -> "FIM DA PARTIDA ${state.match}"
            else -> "EMPATE!"
        }
        PixelText(title, size = 18.sp, modifier = Modifier.fillMaxWidth(), align = TextAlign.Center)
        Spacer(Modifier.height(12.dp))
        when {
            state.finished && state.winners.size == 1 -> Text("🏆 Vitória de ${names(state.winners)}!", color = Arcade.Yellow, fontSize = 26.sp, fontWeight = FontWeight.Black)
            state.finished -> Text("🤝 Empate entre ${names(state.winners)}!", color = Arcade.Yellow, fontSize = 24.sp, fontWeight = FontWeight.Black)
            tie != null -> {
                Text("Empate entre ${names(tie.playerIds)}.", color = Arcade.Yellow, fontSize = 22.sp, fontWeight = FontWeight.Black)
                Text(
                    if (tie.purpose == TiePurpose.MATCH) "Para decidir quem vence esta partida, joguem uma pergunta de desempate inédita ou aceitem o empate (ninguém ganha a partida)."
                    else "Joguem uma pergunta de desempate inédita ou aceitem o empate.",
                    color = Arcade.White, fontSize = 16.sp,
                )
            }
            state.phase == Phase.MATCH_END -> {
                val last = state.matchWinners.lastOrNull().orEmpty()
                Text(if (last.isEmpty()) "Partida empatada (empate aceito)." else "Partida ${state.match} para ${names(last)}!", color = Arcade.Yellow, fontSize = 22.sp, fontWeight = FontWeight.Black)
            }
        }
        state.notice?.let { Spacer(Modifier.height(6.dp)); Text(it, color = Arcade.Orange, fontSize = 15.sp) }
        Spacer(Modifier.height(14.dp))
        if (tie != null && !state.finished) {
            ArcadeButton("Pergunta de desempate", { vm.dispatch(GameAction.StartTiebreak) }, Modifier.fillMaxWidth(), color = Arcade.Magenta, icon = "⚔️")
            Spacer(Modifier.height(10.dp))
            ArcadeButton("Aceitar empate", { vm.dispatch(GameAction.AcceptTie) }, Modifier.fillMaxWidth(), color = Arcade.Muted)
        } else if (state.phase == Phase.MATCH_END && !state.finished) {
            ArcadeButton("Próxima partida ▶", { vm.dispatch(GameAction.NextMatch) }, Modifier.fillMaxWidth(), color = Arcade.Green)
        } else if (state.finished) {
            ArcadeButton("Jogar de novo", { vm.go(Screen.SETUP) }, Modifier.fillMaxWidth(), color = Arcade.Green, icon = "🕹️")
            Spacer(Modifier.height(10.dp))
            ArcadeButton("Voltar ao início", { vm.leaveFinishedGame() }, Modifier.fillMaxWidth(), color = Arcade.Cyan)
        }
    }
}

// ---------------------------------------------------------------- placar e ordem

@Composable
private fun SidePanel(vm: AppViewModel, state: GameState) {
    OrderPanel(state)
    Spacer(Modifier.height(12.dp))
    ScorePanel(vm, state)
    if (state.config.mode == GameMode.BEST_OF_THREE) {
        Spacer(Modifier.height(12.dp))
        ChampionshipPanel(state)
    }
}

@Composable
private fun OrderPanel(state: GameState) {
    val current = state.currentPlayer?.id
    val next = state.nextPlayer?.id
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Cyan, padding = 10.dp) {
        PixelText("ORDEM", size = 11.sp, color = Arcade.Cyan, shadow = Color.Transparent)
        Spacer(Modifier.height(6.dp))
        state.turnOrder.forEachIndexed { i, p ->
            val isCurrent = p.id == current && (state.phase == Phase.ASKING || state.phase == Phase.REVEAL)
            val isNext = p.id == next && !isCurrent
            Row(
                Modifier.fillMaxWidth()
                    .background(if (isCurrent) Arcade.Yellow else Color.Transparent)
                    .padding(horizontal = 6.dp, vertical = 4.dp),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Text("${i + 1}. ${p.name}", color = if (isCurrent) Arcade.Ink else Arcade.White, fontWeight = FontWeight.Bold, fontSize = 18.sp, modifier = Modifier.weight(1f))
                if (isCurrent) Text("◀ VEZ", color = Arcade.Ink, fontWeight = FontWeight.Black, fontSize = 15.sp)
                if (isNext) Text("PRÓXIMO", color = Arcade.Cyan, fontWeight = FontWeight.Black, fontSize = 14.sp)
            }
        }
    }
}

@Composable
private fun ScorePanel(vm: AppViewModel, state: GameState) {
    val ranked = state.players.sortedByDescending { state.score(it.id) }
    val inTiebreak = state.round?.kind == RoundKind.TIEBREAK
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Green, padding = 10.dp) {
        PixelText(
            if (state.config.mode == GameMode.BEST_OF_THREE) "PLACAR · PARTIDA ${state.match}" else "PLACAR",
            size = 11.sp, color = Arcade.Green, shadow = Color.Transparent,
        )
        Spacer(Modifier.height(6.dp))
        val distinctScores = ranked.map { state.score(it.id) }.distinct()
        ranked.forEach { p ->
            val score = state.score(p.id)
            // Empatados recebem a mesma posição (e a mesma medalha).
            val i = if (score == 0) 3 else distinctScores.indexOf(score)
            val pop by animateFloatAsState(1f, spring(Spring.DampingRatioHighBouncy), label = "score")
            Row(Modifier.fillMaxWidth().padding(vertical = 3.dp), verticalAlignment = Alignment.CenterVertically) {
                Text(
                    when (i) { 0 -> "🥇"; 1 -> "🥈"; 2 -> "🥉"; else -> "  " },
                    fontSize = 18.sp, modifier = Modifier.widthIn(min = 30.dp),
                )
                Text(p.name, color = Arcade.White, fontSize = 18.sp, fontWeight = FontWeight.Bold, modifier = Modifier.weight(1f))
                if (inTiebreak || vm.tiebreakHits(state, p.id) > 0) {
                    Text("desemp. ${vm.tiebreakHits(state, p.id)}  ", color = Arcade.Magenta, fontSize = 13.sp)
                }
                Box(
                    Modifier.background(Arcade.Ink).border(2.dp, Arcade.Green).padding(horizontal = 10.dp, vertical = 2.dp),
                ) {
                    Text("$score", color = Arcade.Green, fontSize = 22.sp, fontWeight = FontWeight.Black, modifier = Modifier.scale(pop))
                }
            }
        }
        Spacer(Modifier.height(4.dp))
        Text("1 ponto por acerto, igual para todas as idades.", color = Arcade.Muted, fontSize = 13.sp)
    }
}

@Composable
private fun ChampionshipPanel(state: GameState) {
    PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Magenta, padding = 10.dp) {
        PixelText("CAMPEONATO", size = 11.sp, color = Arcade.Magenta, shadow = Color.Transparent)
        Spacer(Modifier.height(4.dp))
        Text("Vence a partida quem fizer mais pontos nela (empate: desempate ou empate aceito). Campeão: quem vencer 2 partidas.", color = Arcade.Muted, fontSize = 13.sp)
        Spacer(Modifier.height(6.dp))
        state.players.sortedByDescending { state.matchWins(it.id) }.forEach { p ->
            Row(Modifier.fillMaxWidth().padding(vertical = 2.dp)) {
                Text(p.name, color = Arcade.White, fontSize = 17.sp, modifier = Modifier.weight(1f))
                Text("🏆".repeat(state.matchWins(p.id)).ifEmpty { "—" }, fontSize = 17.sp, color = Arcade.Yellow)
            }
        }
        state.matchWinners.forEachIndexed { i, w ->
            Text("Partida ${i + 1}: " + (w.mapNotNull { id -> state.player(id)?.name }.joinToString(" e ").ifEmpty { "empate" }), color = Arcade.Muted, fontSize = 14.sp)
        }
    }
}

/** "Ana", "Ana e Bia", "Ana, Bia e Caio". */
fun joinNames(names: List<String>): String = when (names.size) {
    0 -> ""
    1 -> names[0]
    else -> names.dropLast(1).joinToString(", ") + " e " + names.last()
}
