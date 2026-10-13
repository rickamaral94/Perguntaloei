package br.com.perguntaloei.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.Slider
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import br.com.perguntaloei.AppDialog
import br.com.perguntaloei.AppViewModel
import br.com.perguntaloei.SYSTEM_VOICE
import br.com.perguntaloei.Screen
import br.com.perguntaloei.game.GameAction
import br.com.perguntaloei.game.Outcome
import br.com.perguntaloei.game.RoundKind
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.ui.components.ArcadeButton
import br.com.perguntaloei.ui.components.PixelPanel
import br.com.perguntaloei.ui.components.PixelText
import br.com.perguntaloei.ui.components.ScreenScaffold
import br.com.perguntaloei.ui.theme.Arcade
import br.com.perguntaloei.voice.NeuralSpeaker

// ====================================================================== HISTÓRICO DA PARTIDA

@Composable
fun LogScreen(vm: AppViewModel) {
    val state = vm.game
    ScreenScaffold("HISTÓRICO DA PARTIDA", onBack = { vm.go(if (state != null) Screen.GAME else Screen.HOME) }) {
        if (state == null || state.log.isEmpty()) {
            Text("Nenhuma pergunta respondida ainda.", color = Arcade.White, fontSize = 18.sp)
            return@ScreenScaffold
        }
        Text("Mais recente primeiro. Itens riscados foram desfeitos ou anulados e não contam pontos.", color = Arcade.Muted, fontSize = 14.sp)
        Spacer(Modifier.height(8.dp))
        LazyColumn(verticalArrangement = Arrangement.spacedBy(8.dp)) {
            items(state.log.reversed(), key = { it.seq }) { r ->
                val color = when (r.outcome) {
                    Outcome.CORRECT -> Arcade.Green
                    Outcome.WRONG -> Arcade.Red
                    Outcome.ANNULLED, Outcome.REPLACED_REPEATED -> Arcade.Purple
                    else -> Arcade.Orange
                }
                val voided = r.undone || r.outcome == Outcome.ANNULLED || r.outcome == Outcome.REPLACED_REPEATED
                PixelPanel(Modifier.fillMaxWidth(), border = if (r.undone) Arcade.PanelLight else color, padding = 10.dp) {
                    Row {
                        Text(r.playerName, color = Arcade.Yellow, fontWeight = FontWeight.Bold, fontSize = 18.sp, modifier = Modifier.weight(1f))
                        Text(
                            (if (r.kind == RoundKind.TIEBREAK) "Desempate" else "P${r.match} · R${r.round}") + " · ${r.theme.label}",
                            color = Arcade.Muted, fontSize = 13.sp,
                        )
                    }
                    Text(r.questionText, color = Arcade.White, fontSize = 15.sp)
                    Text("Resposta dada: ${r.givenAnswer ?: "—"}  (${r.method.label})", color = Arcade.White, fontSize = 15.sp)
                    Text("Certa: ${r.correctAnswer}", color = Arcade.Muted, fontSize = 14.sp)
                    Row {
                        Text(
                            r.outcome.label + if (r.undone) " — desfeito" else "",
                            color = color, fontWeight = FontWeight.Bold, fontSize = 16.sp, modifier = Modifier.weight(1f),
                            textDecoration = if (r.undone) TextDecoration.LineThrough else null,
                        )
                        Text(
                            if (voided) "0 ponto" else if (r.points == 1) "+1 ponto" else "${r.points} ponto",
                            color = Arcade.Yellow, fontWeight = FontWeight.Bold, fontSize = 16.sp,
                        )
                    }
                }
            }
        }
    }
}

// ====================================================================== REGRAS

@Composable
fun RulesScreen(vm: AppViewModel) {
    ScreenScaffold("COMO JOGAR", onBack = { vm.go(Screen.HOME) }) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            RuleBlock(
                "A VEZ", Arcade.Yellow,
                "• A ordem dos jogadores aparece antes de começar e pode ser ajustada em Jogadores.\n" +
                    "• Uma pergunta por vez, sempre para o jogador indicado em VEZ DE.\n" +
                    "• Só passa para o próximo depois que a resposta for avaliada, pulada ou a vez encerrada.\n" +
                    "• Depois de cada resposta aparecem a resposta certa, uma explicação, o placar e o próximo jogador.",
            )
            RuleBlock(
                "PONTOS", Arcade.Green,
                "• Acerto vale 1 ponto, para todas as idades.\n" +
                    "• Erro, pulo ou falta de resposta: 0 ponto.\n" +
                    "• Repetir a pergunta não conta como resposta.\n" +
                    "• Desfazer último ponto: corrige o último resultado e volta para a mesma pergunta.\n" +
                    "• Anular pergunta (áudio ruim, interrupção, jogador errado ou pergunta repetida): troca a pergunta sem mexer no placar.",
            )
            RuleBlock(
                "MODOS", Arcade.Cyan,
                "• Rodadas por tema: cada rodada tem um tema; todos respondem esse tema antes de mudar.\n" +
                    "• Número de perguntas: você escolhe quantas perguntas cada um responde; os temas se alternam.\n" +
                    "• Melhor de três: partidas curtas. Vence a partida quem fizer mais pontos nela. " +
                    "É campeão quem vencer 2 partidas. Se após 3 partidas ninguém tiver 2 vitórias, os líderes em vitórias vão para o desempate.\n" +
                    "• Conhecimentos do Brasil: só perguntas sobre o Brasil.",
            )
            RuleBlock(
                "IDADES", Arcade.Orange,
                "• Até 9 anos: perguntas fáceis e adequadas à idade.\n" +
                    "• 10 a 12 anos: fáceis e médias.\n• 13 a 15 anos: até difíceis.\n" +
                    "• Adultos (ou idade não informada): as dificuldades escolhidas na partida.\n" +
                    "• Todos recebem o tema da rodada e o mesmo valor de ponto.",
            )
            RuleBlock(
                "RESPONDER FALANDO", Arcade.Red,
                "• O microfone só abre depois que o apresentador termina de ler a pergunta e as alternativas.\n" +
                    "• Quando o microfone está ativo aparece MICROFONE ATIVO em vermelho, com Parar e Cancelar.\n" +
                    "• Diga a letra (\"letra B\") ou o texto da alternativa. Para V/F diga \"verdadeiro\" ou \"falso\".\n" +
                    "• Se a fala ficar em dúvida, o app mostra o que entendeu e pede confirmação antes de avaliar.\n" +
                    "• \"Repete\" pede a pergunta de novo. \"Passo\" pede para pular (com confirmação).\n" +
                    "• Sempre é possível responder tocando na alternativa.",
            )
            RuleBlock(
                "EMPATE", Arcade.Magenta,
                "• No fim, se houver empate na liderança, vocês podem jogar uma pergunta de desempate inédita ou aceitar o empate.\n" +
                    "• No desempate, se só um acertar, vence. Se ninguém ou mais de um acertar, há outra pergunta.",
            )
            RuleBlock(
                "PERGUNTAS INÉDITAS", Arcade.Purple,
                "• Nenhuma pergunta se repete na mesma partida.\n" +
                    "• O histórico fica salvo no aparelho para evitar repetições nas próximas partidas, inclusive de perguntas quase iguais.\n" +
                    "• Quando as inéditas de um tema acabam, o app avisa e marca a pergunta como \"Já usada em partida anterior\".",
            )
            Spacer(Modifier.height(24.dp))
        }
    }
}

@Composable
private fun RuleBlock(title: String, color: Color, text: String) {
    PixelPanel(Modifier.fillMaxWidth(), border = color) {
        PixelText(title, size = 12.sp, color = color, shadow = Color.Transparent)
        Spacer(Modifier.height(8.dp))
        Text(text, color = Arcade.White, fontSize = 17.sp, lineHeight = 25.sp)
    }
}

// ====================================================================== CONFIGURAÇÕES

@Composable
fun SettingsScreen(vm: AppViewModel) {
    val s = vm.settings
    var confirmClear by remember { mutableStateOf(false) }
    ScreenScaffold("CONFIGURAÇÕES", onBack = { vm.go(Screen.HOME) }) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Purple) {
                PixelText("VOZ DO APRESENTADOR", size = 11.sp, color = Arcade.Purple, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                NeuralVoiceCard(vm)
                Spacer(Modifier.height(10.dp))
                VoicePicker(vm)
                Spacer(Modifier.height(10.dp))
                if (!vm.usingNeuralVoice) {
                    Text("Tom da voz: ${"%.2f".format(s.voicePitch)}", color = Arcade.White, fontSize = 17.sp)
                    Slider(value = s.voicePitch, onValueChange = { v -> vm.setVoicePitch((v * 20).toInt() / 20f) }, valueRange = 0.8f..1.2f, colors = sliderColors())
                }
                Text("Velocidade da fala: ${"%.1f".format(s.speechRate)}x", color = Arcade.White, fontSize = 17.sp)
                Slider(value = s.speechRate, onValueChange = { v -> vm.updateSettings { it.copy(speechRate = (v * 10).toInt() / 10f) } }, valueRange = 0.6f..1.4f, colors = sliderColors())
                SwitchRow("Abrir o microfone sozinho após a leitura", s.autoListen) { v -> vm.updateSettings { it.copy(autoListen = v) } }
                SwitchRow("Sempre confirmar respostas faladas", s.alwaysConfirmVoice) { v -> vm.updateSettings { it.copy(alwaysConfirmVoice = v) } }
                SwitchRow("Efeitos sonoros", s.soundEffects) { v -> vm.updateSettings { it.copy(soundEffects = v) } }
                Text(
                    "Voz do apresentador: " + when (vm.ttsStatus) {
                        br.com.perguntaloei.voice.TtsStatus.READY -> "pronta"
                        br.com.perguntaloei.voice.TtsStatus.INITIALIZING -> "carregando…"
                        br.com.perguntaloei.voice.TtsStatus.MISSING_LANGUAGE -> "português não instalado (instale nas configurações de voz do Android)"
                        br.com.perguntaloei.voice.TtsStatus.UNAVAILABLE -> "indisponível neste aparelho"
                    },
                    color = Arcade.Muted, fontSize = 14.sp,
                )
                Text(
                    "Reconhecimento de fala: " + if (vm.recognitionAvailable) "disponível" else "indisponível (use respostas por toque)",
                    color = Arcade.Muted, fontSize = 14.sp,
                )
            }
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Red) {
                PixelText("PRIVACIDADE", size = 11.sp, color = Arcade.Red, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                Text(PRIVACY_TEXT, color = Arcade.White, fontSize = 16.sp)
                Spacer(Modifier.height(8.dp))
                Text(
                    "Consentimento para o reconhecimento de fala: " + when (s.speechConsent) {
                        true -> "aceito"
                        false -> "recusado (só toque)"
                        null -> "ainda não perguntado"
                    },
                    color = Arcade.Yellow, fontSize = 15.sp,
                )
                Spacer(Modifier.height(8.dp))
                if (s.speechConsent == true) {
                    ArcadeButton("Revogar consentimento", { vm.updateSettings { it.copy(speechConsent = false) } }, Modifier.fillMaxWidth(), color = Arcade.Red, fontSize = 15.sp)
                } else {
                    ArcadeButton("Ler aviso e decidir", { vm.dialog = AppDialog.SpeechConsent }, Modifier.fillMaxWidth(), color = Arcade.Cyan, fontSize = 15.sp)
                }
            }
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Green) {
                PixelText("BANCO DE PERGUNTAS", size = 11.sp, color = Arcade.Green, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                Text("${vm.bank.questions.size} perguntas no aparelho · ${vm.historyCount} já usadas em partidas.", color = Arcade.White, fontSize = 16.sp)
                Spacer(Modifier.height(6.dp))
                Theme.entries.forEach { t ->
                    val all = vm.bank.questions.filter { it.theme == t }
                    val used = all.count { vm.usedInHistory(it) }
                    Row(Modifier.fillMaxWidth().padding(vertical = 1.dp)) {
                        Text("${Arcade.themeIcon(t)} ${t.label}", color = Arcade.White, fontSize = 15.sp, modifier = Modifier.weight(1f))
                        Text("${all.size - used} inéditas / ${all.size}", color = Arcade.Muted, fontSize = 15.sp)
                    }
                }
                Spacer(Modifier.height(10.dp))
                ArcadeButton("Limpar histórico de perguntas", { confirmClear = true }, Modifier.fillMaxWidth(), color = Arcade.Orange, fontSize = 15.sp)
            }
            Text("Fonte dos títulos: Silkscreen, de Jason Kottke (SIL Open Font License). Sons sintetizados pelo próprio app.", color = Arcade.Muted, fontSize = 13.sp)
            Spacer(Modifier.height(24.dp))
        }
    }
    if (confirmClear) {
        AlertDialog(
            onDismissRequest = { confirmClear = false },
            title = { Text("Limpar histórico?") },
            text = { Text("Todas as perguntas voltam a ser consideradas inéditas. Jogadores e partida atual não são apagados.") },
            confirmButton = { TextButton({ vm.clearQuestionHistory(); confirmClear = false }) { Text("Limpar", color = Arcade.Orange) } },
            dismissButton = { TextButton({ confirmClear = false }) { Text("Cancelar") } },
        )
    }
}

const val PRIVACY_TEXT =
    "Nomes, idades, respostas, placar e histórico ficam somente neste aparelho e não são enviados para servidores. " +
        "O app só usa a internet se você pedir para baixar a voz neural opcional, e nesse download nada sobre os jogadores é enviado. " +
        "O app não grava nem guarda áudio. Para entender respostas faladas, o app usa o serviço de reconhecimento de fala " +
        "do próprio Android (geralmente do Google). Dependendo do aparelho, esse serviço pode processar o áudio na internet. " +
        "O app pede para usar o processamento no aparelho quando disponível. Se preferir, recuse e respondam tocando na tela."

// ====================================================================== DIÁLOGOS

@Composable
fun Dialogs(vm: AppViewModel) {
    when (val d = vm.dialog) {
        null -> Unit
        is AppDialog.Message -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text(d.title) },
            text = { Text(d.text, fontSize = 17.sp) },
            confirmButton = { TextButton({ vm.dialog = null }) { Text("OK", color = Arcade.Yellow) } },
        )
        AppDialog.SpeechConsent -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text("Responder falando") },
            text = { Text(PRIVACY_TEXT + "\n\nPermitir o uso do reconhecimento de fala?", fontSize = 16.sp) },
            confirmButton = { TextButton({ vm.onSpeechConsent(true) }) { Text("Permitir", color = Arcade.Green) } },
            dismissButton = { TextButton({ vm.onSpeechConsent(false) }) { Text("Só toque", color = Arcade.Orange) } },
        )
        AppDialog.MicRationale -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text("Microfone") },
            text = {
                Text(
                    "O microfone é usado só enquanto o jogo espera a resposta do jogador da vez, com o aviso MICROFONE ATIVO na tela. " +
                        "Nada é gravado. A seguir o Android vai pedir a permissão.",
                    fontSize = 16.sp,
                )
            },
            confirmButton = { TextButton({ vm.onMicRationaleAccepted() }) { Text("Continuar", color = Arcade.Green) } },
            dismissButton = { TextButton({ vm.dialog = null; vm.onMicPermissionResult(false) }) { Text("Agora não") } },
        )
        AppDialog.AnnulReasons -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text("Anular pergunta") },
            text = {
                Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                    Text("A pergunta é trocada por outra para o mesmo jogador. O placar não muda.", fontSize = 15.sp)
                    ArcadeButton("Áudio falhou ou foi interrompida", { vm.dialog = null; vm.dispatch(GameAction.Annul(repeated = false)) }, Modifier.fillMaxWidth(), color = Arcade.Purple, fontSize = 15.sp)
                    ArcadeButton("Foi para o jogador errado", { vm.dialog = null; vm.dispatch(GameAction.Annul(repeated = false)) }, Modifier.fillMaxWidth(), color = Arcade.Cyan, fontSize = 15.sp)
                    ArcadeButton("Já caiu antes (repetida)", { vm.dialog = null; vm.dispatch(GameAction.Annul(repeated = true)) }, Modifier.fillMaxWidth(), color = Arcade.Orange, fontSize = 15.sp)
                }
            },
            confirmButton = { TextButton({ vm.dialog = null }) { Text("Cancelar") } },
        )
        AppDialog.Permissions -> AlertDialog(
            onDismissRequest = { },
            title = { Text("Bem-vindos ao PERGUNTÁ-LO-EI!") },
            text = {
                Text(
                    "Para responder falando, o app precisa do microfone. Ele só fica ligado quando o jogo espera a " +
                        "resposta do jogador da vez, com o aviso MICROFONE ATIVO na tela, e nada é gravado.\n\n" + PRIVACY_TEXT +
                        "\n\nPermitir agora? Você pode mudar depois em Configurações.",
                    fontSize = 16.sp,
                )
            },
            confirmButton = { TextButton({ vm.onPermissionsChoice(true) }) { Text("Permitir microfone", color = Arcade.Green) } },
            dismissButton = { TextButton({ vm.onPermissionsChoice(false) }) { Text("Agora não (só toque)", color = Arcade.Orange) } },
        )
        AppDialog.ConfirmVoiceDownload -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text("Baixar a voz neural?") },
            text = {
                Text(
                    "A voz neural é mais natural que a voz padrão, mas é um arquivo grande (cerca de ${vm.neuralSizeMb} MB). " +
                        "Ela será baixada uma única vez do Hugging Face (huggingface.co), onde o modelo de voz é publicado. " +
                        "Prefira usar Wi-Fi.\n\nO download só busca os arquivos da voz: nenhum nome, idade, resposta ou histórico é enviado. " +
                        "Depois de baixada, a voz funciona sem internet, e você pode voltar para a voz padrão ou apagá-la quando quiser.",
                    fontSize = 16.sp,
                )
            },
            confirmButton = { TextButton({ vm.startNeuralDownload() }) { Text("Baixar", color = Arcade.Green) } },
            dismissButton = { TextButton({ vm.dialog = null }) { Text("Agora não") } },
        )
        AppDialog.ConfirmEndGame -> AlertDialog(
            onDismissRequest = { vm.dialog = null },
            title = { Text("Encerrar partida?") },
            text = { Text("O jogo termina agora com o placar atual. A pergunta em aberto não vale ponto.", fontSize = 16.sp) },
            confirmButton = { TextButton({ vm.dialog = null; vm.dispatch(GameAction.EndEarly) }) { Text("Encerrar", color = Arcade.Red) } },
            dismissButton = { TextButton({ vm.dialog = null }) { Text("Continuar jogando") } },
        )
    }
}

/** Voz neural opcional: baixar (com confirmação), acompanhar o download, usar ou apagar. */
@Composable
private fun NeuralVoiceCard(vm: AppViewModel) {
    Column(
        Modifier.fillMaxWidth().background(Arcade.PanelLight).padding(10.dp),
        verticalArrangement = Arrangement.spacedBy(6.dp),
    ) {
        Text("Voz neural (opcional)", color = Arcade.Yellow, fontSize = 17.sp, fontWeight = FontWeight.Bold)
        val progress = vm.neuralProgress
        when {
            !vm.neuralSupported -> Text(
                "Este aparelho não é compatível com a voz neural. O jogo continua com a voz padrão.",
                color = Arcade.Muted, fontSize = 14.sp,
            )
            progress != null -> {
                Text("Baixando a voz… ${(progress * 100).toInt()}%", color = Arcade.White, fontSize = 15.sp)
                LinearProgressIndicator(
                    progress = { progress }, Modifier.fillMaxWidth().height(10.dp),
                    color = Arcade.Green, trackColor = Arcade.Panel,
                )
                ArcadeButton("Cancelar download", { vm.cancelNeuralDownload() }, Modifier.fillMaxWidth(), color = Arcade.Orange, fontSize = 15.sp)
            }
            !vm.neuralInstalled -> {
                Text(
                    "Uma voz mais natural, que funciona sem internet depois de baixada (cerca de ${vm.neuralSizeMb} MB). " +
                        "Sem ela, o jogo usa a voz padrão.",
                    color = Arcade.Muted, fontSize = 14.sp,
                )
                ArcadeButton("Baixar voz neural (${vm.neuralSizeMb} MB)", { vm.askNeuralDownload() }, Modifier.fillMaxWidth(), color = Arcade.Green, fontSize = 15.sp)
            }
            else -> {
                Text("Voz neural baixada (${vm.neuralSizeMb} MB).", color = Arcade.White, fontSize = 15.sp)
                if (vm.usingNeuralVoice) {
                    ArcadeButton("Usar a voz padrão", { vm.chooseEngine(SYSTEM_VOICE) }, Modifier.fillMaxWidth(), color = Arcade.Cyan, fontSize = 15.sp)
                } else {
                    ArcadeButton("Usar a voz neural", { vm.chooseEngine(NeuralSpeaker.ENGINE_ID) }, Modifier.fillMaxWidth(), color = Arcade.Green, fontSize = 15.sp)
                }
                ArcadeButton("Apagar voz neural (liberar espaço)", { vm.deleteNeuralVoice() }, Modifier.fillMaxWidth(), color = Arcade.Red, fontSize = 15.sp)
            }
        }
    }
}

/** Escolha do mecanismo e da voz, com exemplo e atalho para instalar vozes melhores. */
@Composable
private fun VoicePicker(vm: AppViewModel) {
    val s = vm.settings
    Text(
        if (vm.usingNeuralVoice) "Usando a voz neural baixada: natural, em português do Brasil e funciona sem internet."
        else "Usando a voz padrão do jogo (vozes do sistema Android).",
        color = Arcade.Muted, fontSize = 14.sp,
    )
    if (vm.engineOptions.isNotEmpty()) {
        Spacer(Modifier.height(8.dp))
        Text("Mecanismo de voz", color = Arcade.White, fontSize = 17.sp, fontWeight = FontWeight.Bold)
        vm.engineOptions.forEach { e ->
            val on = e.packageName == vm.currentEngine
            ArcadeButton(
                (if (on) "◉ " else "○ ") + e.label, { vm.chooseEngine(e.packageName) },
                Modifier.fillMaxWidth().padding(vertical = 3.dp),
                color = if (on) Arcade.Purple else Arcade.PanelLight, textColor = if (on) Arcade.Ink else Arcade.White,
                minHeight = 44.dp, fontSize = 15.sp,
            )
        }
    }
    Spacer(Modifier.height(8.dp))
    Text("Voz", color = Arcade.White, fontSize = 17.sp, fontWeight = FontWeight.Bold)
    if (vm.voiceOptions.isEmpty()) {
        Text(
            if (vm.ttsStatus == br.com.perguntaloei.voice.TtsStatus.READY) "Nenhuma voz em português encontrada neste mecanismo."
            else "Carregando vozes…",
            color = Arcade.Muted, fontSize = 14.sp,
        )
    }
    vm.voiceOptions.take(12).forEachIndexed { i, v ->
        val on = v.name == vm.currentVoice
        ArcadeButton(
            (if (on) "◉ " else "○ ") + v.label + (if (i == 0) " ★ mais natural" else "") + (if (v.needsNetwork) " · online" else ""),
            { vm.chooseVoice(v.name) },
            Modifier.fillMaxWidth().padding(vertical = 3.dp),
            color = if (on) Arcade.Yellow else Arcade.PanelLight, textColor = if (on) Arcade.Ink else Arcade.White,
            minHeight = 44.dp, fontSize = 14.sp,
        )
    }
    Spacer(Modifier.height(8.dp))
    Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
        ArcadeButton("▶ Ouvir exemplo", { vm.previewVoice() }, Modifier.weight(1f), color = Arcade.Green, fontSize = 15.sp)
        if (!vm.usingNeuralVoice) ArcadeButton("Instalar vozes", { vm.openTtsSettings() }, Modifier.weight(1f), color = Arcade.Cyan, fontSize = 15.sp)
    }
    if (vm.usingNeuralVoice) return
    SwitchRow("Permitir vozes online (mais naturais)", s.allowNetworkVoices) { vm.setAllowNetworkVoices(it) }
    Text(
        "Vozes online enviam ao provedor de voz (ex.: Google) o texto falado, que inclui as perguntas e os nomes dos jogadores. " +
            "Desligado, o app usa só vozes instaladas no aparelho.",
        color = Arcade.Muted, fontSize = 13.sp,
    )
}
