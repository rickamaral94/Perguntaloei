package br.com.perguntaloei

import android.Manifest
import android.content.ActivityNotFoundException
import android.content.Intent
import android.provider.Settings
import android.speech.tts.TextToSpeech
import android.os.Bundle
import android.view.WindowManager
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.contract.ActivityResultContracts
import androidx.activity.viewModels
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.safeDrawingPadding
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import br.com.perguntaloei.ui.Dialogs
import br.com.perguntaloei.ui.GameScreen
import br.com.perguntaloei.ui.HomeScreen
import br.com.perguntaloei.ui.LogScreen
import br.com.perguntaloei.ui.PlayersScreen
import br.com.perguntaloei.ui.RulesScreen
import br.com.perguntaloei.ui.SettingsScreen
import br.com.perguntaloei.ui.SetupScreen
import br.com.perguntaloei.ui.theme.Arcade
import br.com.perguntaloei.ui.theme.ArcadeTheme

class MainActivity : ComponentActivity() {

    private val vm: AppViewModel by viewModels()

    private val micPermission = registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
        vm.onMicPermissionResult(granted)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            ArcadeTheme {
                LaunchedEffect(Unit) {
                    vm.events.collect { e ->
                        when (e) {
                            UiEvent.RequestMicPermission -> micPermission.launch(Manifest.permission.RECORD_AUDIO)
                            UiEvent.OpenTtsSettings -> openTtsSettings()
                            is UiEvent.ShareText -> share(e.subject, e.text)
                        }
                    }
                }
                // Primeira abertura: pede as permissões de uma vez, com explicação.
                LaunchedEffect(Unit) { vm.onAppStart() }
                LaunchedEffect(vm.screen) {
                    // Durante a partida a tela fica acesa.
                    if (vm.screen == Screen.GAME) window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
                    else window.clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
                }
                BackHandler(enabled = vm.screen != Screen.HOME) {
                    vm.go(if (vm.screen == Screen.LOG && vm.game != null) Screen.GAME else Screen.HOME)
                }
                Box(Modifier.fillMaxSize().background(Arcade.Bg).safeDrawingPadding()) {
                    when (vm.screen) {
                        Screen.HOME -> HomeScreen(vm)
                        Screen.PLAYERS -> PlayersScreen(vm)
                        Screen.SETUP -> SetupScreen(vm)
                        Screen.GAME -> GameScreen(vm)
                        Screen.LOG -> LogScreen(vm)
                        Screen.RULES -> RulesScreen(vm)
                        Screen.SETTINGS -> SettingsScreen(vm)
                    }
                    Dialogs(vm)
                }
            }
        }
    }

    /** Configurações de voz do Android (onde se instalam vozes de alta qualidade). */
    private fun openTtsSettings() {
        val attempts = listOf(
            Intent("com.android.settings.TTS_SETTINGS"),
            Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA).apply { vm.currentEngine?.let { setPackage(it) } },
            Intent(Settings.ACTION_SETTINGS),
        )
        for (intent in attempts) {
            try {
                startActivity(intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
                return
            } catch (_: ActivityNotFoundException) {
            } catch (_: SecurityException) {
            }
        }
    }

    override fun onStop() {
        super.onStop()
        // Interrupção (ligação, tela bloqueada, troca de app): fala e microfone param; a partida já está salva.
        vm.onAppPaused()
    }

    /** "Compartilhar" do Android: o jogador escolhe o app (WhatsApp, e-mail...). O app não envia nada sozinho. */
    private fun share(subject: String, text: String) {
        val send = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_SUBJECT, subject)
            putExtra(Intent.EXTRA_TEXT, text)
        }
        runCatching { startActivity(Intent.createChooser(send, subject)) }
    }
}
