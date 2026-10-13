package br.com.perguntaloei.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Slider
import androidx.compose.material3.SliderDefaults
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import br.com.perguntaloei.AppViewModel
import br.com.perguntaloei.Screen
import br.com.perguntaloei.model.Difficulty
import br.com.perguntaloei.model.GameConfig
import br.com.perguntaloei.model.GameMode
import br.com.perguntaloei.model.Player
import br.com.perguntaloei.model.Theme
import br.com.perguntaloei.questions.AgePolicy
import br.com.perguntaloei.ui.components.ArcadeButton
import br.com.perguntaloei.ui.components.Blink
import br.com.perguntaloei.ui.components.GameTitle
import br.com.perguntaloei.ui.components.PixelPanel
import br.com.perguntaloei.ui.components.PixelText
import br.com.perguntaloei.ui.components.ScreenScaffold
import br.com.perguntaloei.ui.components.StarField
import br.com.perguntaloei.ui.components.Tag
import br.com.perguntaloei.ui.theme.Arcade

// ====================================================================== INÍCIO

@Composable
fun HomeScreen(vm: AppViewModel) {
    Box(Modifier.fillMaxSize()) {
        StarField()
        Column(
            Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 16.dp, vertical = 24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Spacer(Modifier.height(12.dp))
            Text("❓💬", fontSize = 56.sp)
            Spacer(Modifier.height(8.dp))
            GameTitle()
            Spacer(Modifier.height(6.dp))
            Text(
                "O quiz da família, com apresentador por voz",
                color = Arcade.Muted, fontSize = 16.sp, textAlign = TextAlign.Center,
            )
            Spacer(Modifier.height(10.dp))
            Blink("APERTE START")
            Spacer(Modifier.height(24.dp))
            Column(Modifier.widthIn(max = 480.dp).fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(14.dp)) {
                val saved = vm.game
                if (!vm.bankReady) {
                    // As perguntas carregam em segundo plano (instantes); até lá, só o que não depende delas.
                    Text("Carregando perguntas…", color = Arcade.Muted, fontSize = 16.sp, modifier = Modifier.fillMaxWidth(), textAlign = TextAlign.Center)
                } else {
                    if (saved != null && !saved.finished) {
                        ArcadeButton("Continuar partida", { vm.go(Screen.GAME) }, Modifier.fillMaxWidth(), color = Arcade.Green, icon = "▶")
                    }
                    ArcadeButton("Novo jogo", { vm.go(Screen.SETUP) }, Modifier.fillMaxWidth(), color = Arcade.Yellow, icon = "🕹️")
                }
                ArcadeButton("Jogadores (${vm.players.size})", { vm.go(Screen.PLAYERS) }, Modifier.fillMaxWidth(), color = Arcade.Cyan, icon = "👥")
                ArcadeButton("Como jogar", { vm.go(Screen.RULES) }, Modifier.fillMaxWidth(), color = Arcade.Purple, icon = "📜")
                ArcadeButton("Configurações", { vm.go(Screen.SETTINGS) }, Modifier.fillMaxWidth(), color = Arcade.Orange, icon = "⚙️")
                if (vm.bankReady && saved != null && saved.finished) {
                    ArcadeButton("Ver último resultado", { vm.go(Screen.GAME) }, Modifier.fillMaxWidth(), color = Arcade.Magenta, icon = "🏆")
                }
            }
            if (vm.summaries.isNotEmpty()) {
                Spacer(Modifier.height(24.dp))
                PixelPanel(Modifier.widthIn(max = 480.dp).fillMaxWidth(), border = Arcade.Magenta) {
                    PixelText("ÚLTIMAS PARTIDAS", size = 11.sp, color = Arcade.Magenta, shadow = Color.Transparent)
                    Spacer(Modifier.height(8.dp))
                    vm.summaries.take(5).forEach { s ->
                        val scores = s.players.zip(s.scores).joinToString("  ·  ") { "${it.first} ${it.second}" }
                        Text("🏆 ${s.winners.joinToString(" e ").ifEmpty { "—" }} — ${s.mode}", color = Arcade.White, fontWeight = FontWeight.Bold)
                        Text(scores, color = Arcade.Muted, fontSize = 14.sp)
                        Spacer(Modifier.height(6.dp))
                    }
                }
            }
            Spacer(Modifier.height(16.dp))
            Text(
                "Tudo fica salvo só neste aparelho.",
                color = Arcade.Muted, fontSize = 13.sp, textAlign = TextAlign.Center,
            )
        }
    }
}

// ====================================================================== JOGADORES

@Composable
fun PlayersScreen(vm: AppViewModel) {
    var editing by remember { mutableStateOf<Player?>(null) }
    var name by remember { mutableStateOf("") }
    var age by remember { mutableStateOf("") }

    fun reset() { editing = null; name = ""; age = "" }

    ScreenScaffold("JOGADORES", onBack = { vm.go(Screen.HOME) }) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Yellow) {
                Text(if (editing == null) "Novo jogador" else "Editar ${editing?.name}", color = Arcade.Yellow, fontWeight = FontWeight.Bold, fontSize = 18.sp)
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    value = name, onValueChange = { name = it.take(24) }, label = { Text("Nome") },
                    singleLine = true, modifier = Modifier.fillMaxWidth(), colors = fieldColors(),
                )
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    value = age, onValueChange = { v -> age = v.filter { it.isDigit() }.take(3) },
                    label = { Text("Idade (opcional)") }, singleLine = true,
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                    modifier = Modifier.fillMaxWidth(), colors = fieldColors(),
                )
                Spacer(Modifier.height(12.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                    ArcadeButton(
                        if (editing == null) "Adicionar" else "Salvar",
                        {
                            val a = age.toIntOrNull()?.takeIf { it in 1..120 }
                            val e = editing
                            if (e == null) vm.addPlayer(name, a) else vm.editPlayer(e.id, name, a)
                            reset()
                        },
                        Modifier.weight(1f), enabled = name.isNotBlank(), color = Arcade.Green,
                    )
                    if (editing != null) ArcadeButton("Cancelar", { reset() }, Modifier.weight(1f), color = Arcade.Muted)
                }
            }

            PixelPanel(Modifier.fillMaxWidth()) {
                PixelText("ORDEM DAS VEZES", size = 11.sp, color = Arcade.Cyan, shadow = Color.Transparent)
                Spacer(Modifier.height(4.dp))
                Text(
                    "A partida segue exatamente esta ordem. Use as setas para ajustar. " +
                        "Desligue \"Joga\" para quem não vai participar agora (o cadastro continua salvo).",
                    color = Arcade.Muted, fontSize = 14.sp,
                )
                Spacer(Modifier.height(8.dp))
                if (vm.players.isEmpty()) Text("Nenhum jogador cadastrado.", color = Arcade.White)
                vm.players.forEachIndexed { i, p ->
                    Row(
                        Modifier.fillMaxWidth().padding(top = 8.dp),
                        verticalAlignment = Alignment.CenterVertically,
                    ) {
                        Text("${i + 1}.", color = if (p.active) Arcade.Yellow else Arcade.Muted, fontWeight = FontWeight.Bold, fontSize = 20.sp, modifier = Modifier.widthIn(min = 34.dp))
                        Column(Modifier.weight(1f)) {
                            Text(p.name, color = if (p.active) Arcade.White else Arcade.Muted, fontWeight = FontWeight.Bold, fontSize = 19.sp)
                            Text(
                                (p.age?.let { "$it anos · " } ?: "idade não informada · ") + AgePolicy.groupLabel(p.age),
                                color = Arcade.Muted, fontSize = 13.sp,
                            )
                        }
                        PlayerActiveSwitch(p.active) { vm.setPlayerActive(p.id, it) }
                    }
                    Row(
                        Modifier.fillMaxWidth().padding(start = 34.dp, bottom = 6.dp),
                        verticalAlignment = Alignment.CenterVertically,
                    ) {
                        SmallButton("▲", enabled = i > 0) { vm.movePlayer(p.id, -1) }
                        SmallButton("▼", enabled = i < vm.players.size - 1) { vm.movePlayer(p.id, 1) }
                        SmallButton("✎") { editing = p; name = p.name; age = p.age?.toString() ?: "" }
                        SmallButton("✕", color = Arcade.Red) { vm.removePlayer(p.id); if (editing?.id == p.id) reset() }
                    }
                }
                if (vm.players.size > 1) {
                    Spacer(Modifier.height(8.dp))
                    ArcadeButton("Sortear ordem", { vm.shufflePlayers() }, Modifier.fillMaxWidth(), color = Arcade.Purple, icon = "🎲")
                }
            }
            ArcadeButton("Configurar partida ▶", { vm.go(Screen.SETUP) }, Modifier.fillMaxWidth(), enabled = vm.players.isNotEmpty(), color = Arcade.Yellow)
            Spacer(Modifier.height(24.dp))
        }
    }
}

@Composable
fun SmallButton(text: String, color: Color = Arcade.Cyan, enabled: Boolean = true, onClick: () -> Unit) {
    ArcadeButton(text, onClick, Modifier.padding(start = 6.dp).size(width = 48.dp, height = 48.dp), color = color, enabled = enabled, minHeight = 44.dp, fontSize = 16.sp)
}

@Composable
fun fieldColors() = OutlinedTextFieldDefaults.colors(
    focusedTextColor = Arcade.White, unfocusedTextColor = Arcade.White,
    focusedBorderColor = Arcade.Yellow, unfocusedBorderColor = Arcade.Muted,
    focusedLabelColor = Arcade.Yellow, unfocusedLabelColor = Arcade.Muted, cursorColor = Arcade.Yellow,
)

// ====================================================================== CONFIGURAÇÃO DA PARTIDA

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun SetupScreen(vm: AppViewModel) {
    var config by remember { mutableStateOf(vm.settings.lastConfig) }
    val brazil = config.mode == GameMode.BRAZIL
    val availableThemes = vm.bank.themesWithQuestions(brazil)

    ScreenScaffold("NOVA PARTIDA", onBack = { vm.go(Screen.HOME) }) {
        Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), verticalArrangement = Arrangement.spacedBy(14.dp)) {
            // ---- jogadores e ordem
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Cyan) {
                PixelText("ORDEM", size = 11.sp, color = Arcade.Cyan, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                if (vm.players.isEmpty()) {
                    Text("Cadastre os jogadores primeiro.", color = Arcade.White)
                } else {
                    Text("Quem joga esta partida, na ordem das vezes:", color = Arcade.Muted, fontSize = 14.sp)
                    var n = 0
                    vm.players.forEach { p ->
                        Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                            val label = if (p.active) "${++n}. ${p.name}" else "– ${p.name}"
                            Column(Modifier.weight(1f)) {
                                Text(label + (p.age?.let { " ($it)" } ?: ""), color = if (p.active) Arcade.White else Arcade.Muted, fontSize = 17.sp, fontWeight = FontWeight.Bold)
                                Text(if (p.active) AgePolicy.groupLabel(p.age) else "fora desta partida", color = Arcade.Muted, fontSize = 13.sp)
                            }
                            PlayerActiveSwitch(p.active) { vm.setPlayerActive(p.id, it) }
                        }
                    }
                    if (vm.activePlayers.isEmpty()) Text("Ligue pelo menos um jogador.", color = Arcade.Orange, fontSize = 14.sp)
                }
                Spacer(Modifier.height(8.dp))
                ArcadeButton("Editar jogadores e ordem", { vm.go(Screen.PLAYERS) }, Modifier.fillMaxWidth(), color = Arcade.Cyan, fontSize = 15.sp)
            }

            // ---- modo
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Yellow) {
                PixelText("MODO DE JOGO", size = 11.sp, shadow = Color.Transparent)
                Spacer(Modifier.height(8.dp))
                GameMode.entries.forEach { m ->
                    val selected = config.mode == m
                    PixelPanel(
                        Modifier.fillMaxWidth().padding(vertical = 4.dp),
                        border = if (selected) Arcade.Yellow else Arcade.PanelLight,
                        background = if (selected) Arcade.PanelLight else Arcade.Panel,
                        padding = 10.dp,
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Column(Modifier.weight(1f)) {
                                Text((if (selected) "◉ " else "○ ") + m.label, color = if (selected) Arcade.Yellow else Arcade.White, fontWeight = FontWeight.Bold, fontSize = 18.sp)
                                Text(m.description, color = Arcade.Muted, fontSize = 14.sp)
                            }
                            if (!selected) ArcadeButton("Escolher", { config = config.copy(mode = m) }, color = Arcade.Yellow, minHeight = 44.dp, fontSize = 14.sp)
                        }
                    }
                }
            }

            // ---- tamanho
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Green) {
                if (config.mode == GameMode.BEST_OF_THREE) {
                    Text("Rodadas por partida: ${config.roundsPerMatch}", color = Arcade.White, fontWeight = FontWeight.Bold, fontSize = 18.sp)
                    Text("Cada jogador responde ${config.roundsPerMatch} pergunta(s) por partida. Até 3 partidas.", color = Arcade.Muted, fontSize = 14.sp)
                    Slider(
                        value = config.roundsPerMatch.toFloat(), onValueChange = { config = config.copy(roundsPerMatch = it.toInt()) },
                        valueRange = 1f..5f, steps = 3, colors = sliderColors(),
                    )
                } else {
                    val label = if (config.mode == GameMode.QUESTION_COUNT) "Perguntas por jogador" else "Rodadas"
                    Text("$label: ${config.rounds}", color = Arcade.White, fontWeight = FontWeight.Bold, fontSize = 18.sp)
                    Text(
                        "Total: ${config.rounds * vm.activePlayers.size.coerceAtLeast(1)} perguntas para ${vm.activePlayers.size} jogador(es).",
                        color = Arcade.Muted, fontSize = 14.sp,
                    )
                    Slider(
                        value = config.rounds.toFloat(), onValueChange = { config = config.copy(rounds = it.toInt()) },
                        valueRange = 1f..15f, steps = 13, colors = sliderColors(),
                    )
                }
            }

            // ---- temas
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Magenta) {
                PixelText("TEMAS", size = 11.sp, color = Arcade.Magenta, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    ArcadeButton("Todos", { config = config.copy(themes = Theme.entries) }, Modifier.weight(1f), color = Arcade.Magenta, minHeight = 44.dp, fontSize = 14.sp)
                    ArcadeButton("Nenhum", { config = config.copy(themes = emptyList()) }, Modifier.weight(1f), color = Arcade.Muted, minHeight = 44.dp, fontSize = 14.sp)
                }
                Spacer(Modifier.height(10.dp))
                FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Theme.entries.forEach { t ->
                        val available = t in availableThemes
                        val on = t in config.themes && available
                        ArcadeButton(
                            "${Arcade.themeIcon(t)} ${t.label}",
                            {
                                config = config.copy(themes = if (t in config.themes) config.themes - t else config.themes + t)
                            },
                            color = if (on) Arcade.themeColor(t) else Arcade.PanelLight,
                            textColor = if (on) Arcade.Ink else Arcade.Muted,
                            enabled = available, minHeight = 44.dp, fontSize = 14.sp,
                        )
                    }
                }
                if (brazil) {
                    Spacer(Modifier.height(6.dp))
                    Text("Modo Brasil: só aparecem temas com perguntas sobre o Brasil.", color = Arcade.Muted, fontSize = 13.sp)
                }
            }

            // ---- dificuldade
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Orange) {
                PixelText("DIFICULDADE", size = 11.sp, color = Arcade.Orange, shadow = Color.Transparent)
                Spacer(Modifier.height(4.dp))
                Text(
                    "Vale para adultos. Crianças (até 9 anos) recebem perguntas fáceis; de 10 a 12, fáceis e médias; " +
                        "de 13 a 15, até difíceis. Todos valem 1 ponto e todos recebem o tema da rodada.",
                    color = Arcade.Muted, fontSize = 14.sp,
                )
                Spacer(Modifier.height(8.dp))
                FlowRow(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Difficulty.entries.forEach { d ->
                        val on = d in config.difficulties
                        ArcadeButton(
                            (if (on) "✓ " else "") + d.label,
                            {
                                val set = if (on) config.difficulties - d else config.difficulties + d
                                if (set.isNotEmpty()) config = config.copy(difficulties = set)
                            },
                            color = if (on) Arcade.Orange else Arcade.PanelLight,
                            textColor = if (on) Arcade.Ink else Arcade.Muted, minHeight = 44.dp, fontSize = 14.sp,
                        )
                    }
                }
            }

            // ---- voz
            PixelPanel(Modifier.fillMaxWidth(), border = Arcade.Purple) {
                PixelText("APRESENTADOR", size = 11.sp, color = Arcade.Purple, shadow = Color.Transparent)
                Spacer(Modifier.height(6.dp))
                SwitchRow("Apresentador lê em voz alta", config.voiceHost) { config = config.copy(voiceHost = it) }
                SwitchRow("Responder falando (microfone)", config.voiceAnswers && vm.recognitionAvailable, enabled = vm.recognitionAvailable) {
                    config = config.copy(voiceAnswers = it)
                }
                Text(
                    when {
                        !vm.recognitionAvailable -> "Este aparelho não tem reconhecimento de fala: as respostas serão por toque."
                        !config.voiceHost && !config.voiceAnswers -> "Modo sem voz: perguntas na tela e respostas por toque."
                        else -> "Sempre dá para responder tocando na alternativa."
                    },
                    color = Arcade.Muted, fontSize = 14.sp,
                )
            }

            val canStart = vm.activePlayers.isNotEmpty() && config.themes.any { it in availableThemes }
            ArcadeButton(
                "COMEÇAR!", { vm.startNewGame(config) }, Modifier.fillMaxWidth(),
                enabled = canStart, color = Arcade.Green, icon = "🕹️", minHeight = 64.dp, fontSize = 20.sp,
            )
            if (!canStart) Text("Escolha pelo menos um tema e ligue pelo menos um jogador.", color = Arcade.Orange, fontSize = 14.sp)
            Spacer(Modifier.height(24.dp))
        }
    }
}

@Composable
fun SwitchRow(label: String, checked: Boolean, enabled: Boolean = true, onChange: (Boolean) -> Unit) {
    Row(Modifier.fillMaxWidth().padding(vertical = 4.dp), verticalAlignment = Alignment.CenterVertically) {
        Text(label, color = if (enabled) Arcade.White else Arcade.Muted, fontSize = 17.sp, modifier = Modifier.weight(1f))
        Switch(checked = checked, onCheckedChange = onChange, enabled = enabled)
    }
}

@Composable
fun sliderColors() = SliderDefaults.colors(thumbColor = Arcade.Yellow, activeTrackColor = Arcade.Yellow, inactiveTrackColor = Arcade.PanelLight)

@Composable
fun ThemeTag(t: Theme) = Tag("${Arcade.themeIcon(t)} ${t.label}", Arcade.themeColor(t))

/** Chave "Joga": o jogador participa (ou não) da partida, sem apagar o cadastro. */
@Composable
fun PlayerActiveSwitch(active: Boolean, onChange: (Boolean) -> Unit) {
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Switch(
            checked = active, onCheckedChange = onChange,
            modifier = Modifier.semantics { contentDescription = if (active) "Joga: sim" else "Joga: não" },
        )
        Text("Joga", color = if (active) Arcade.Green else Arcade.Muted, fontSize = 12.sp, fontWeight = FontWeight.Bold)
    }
}
