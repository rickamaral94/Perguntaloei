# PERGUNTÁ-LO-EI

Quiz familiar para Android, com **apresentador por voz**, visual de fliperama dos anos 90 e regras que mantêm a ordem dos jogadores e o placar sempre corretos.

<p align="center"><img src="docs/icone-512.png" width="128" alt="Ícone do PERGUNTÁ-LO-EI"></p>

| Início | Configuração | Rodada | Pergunta | Resultado |
|---|---|---|---|---|
| ![](docs/telas/01-inicio.png) | ![](docs/telas/03-configuracao.png) | ![](docs/telas/04-rodada.png) | ![](docs/telas/05-pergunta.png) | ![](docs/telas/06-resultado.png) |

Tablet (pergunta e placar lado a lado): ![](docs/telas/09-tablet-pergunta.png)

> As capturas foram geradas automaticamente pelo teste de interface (`TouchUiTest`), com as animações desligadas.

## APK de teste

| Arquivo | Uso |
|---|---|
| [`apk/PERGUNTALOEI-1.3.0-teste-arm64.apk`](apk/PERGUNTALOEI-1.3.0-teste-arm64.apk) (24 MB) | **Para testar.** Build *debug* para celulares arm64 (praticamente todos os aparelhos atuais). É exatamente o código coberto pelos testes. |

A voz neural **não vem dentro do APK**: é um download opcional (~61 MB) feito em Configurações, só se o jogador quiser. Sem ela, o jogo usa a voz padrão (vozes do sistema Android).
Para celulares antigos de 32 bits, gere o APK `armeabi-v7a` com `./gradlew assembleDebug` (sai em `app/build/outputs/apk/debug/`).

Para instalar: copie o APK para o celular e abra-o (permita "instalar apps desconhecidos"), ou `adb install apk/PERGUNTALOEI-1.3.0-teste-arm64.apk`. Android 7.0 (API 24) ou superior. Instala por cima das versões anteriores, mantendo jogadores e histórico.

## Estrutura do projeto

```
app/src/main/java/br/com/perguntaloei/
├─ model/       Pergunta, Jogador, Tema, Dificuldade, Modo de jogo, Configuração
├─ questions/   Banco (carga + validação), normalização de texto, quase-duplicatas,
│               seleção por idade/tema/histórico (AgePolicy, QuestionSelector)
├─ game/        Motor de regras puro (GameEngine/GameState), interpretação de respostas
│               (AnswerInterpreter), roteiro do apresentador (PresenterScript)
├─ data/        Armazenamento local com escrita atômica (jogadores, configurações,
│               histórico de perguntas, partida em andamento, partidas anteriores)
├─ voice/       Voz neural opcional (NeuralVoicePack baixa e confere; NeuralSpeaker: Piper pt-BR via sherpa-onnx), vozes do
│               sistema (VoiceHost/TextToSpeech) e reconhecimento de fala (SpeechInput),
│               atrás de interfaces testáveis
├─ audio/       Efeitos sonoros 8 bits sintetizados no próprio app (sem arquivos de áudio)
├─ ui/          Telas Compose: início, jogadores, configuração, jogo, histórico, regras, ajustes
├─ AppViewModel.kt  Orquestra motor + voz + microfone + persistência
└─ MainActivity.kt
app/src/main/assets/questions.json   Banco de perguntas (gerado, offline)
app/src/test/                        Testes (JVM + Robolectric)
tools/questions/                     Fonte do banco (parte1…5.py) + validador/gerador
tools/voz-neural/verificar.sh        Baixa a voz neural como o app (mesmos hashes) e gera áudio real, num PC Linux
tools/make_icons.py                  Gerador do ícone (adaptativo + PNGs por densidade)
```

## Como compilar

Requisitos: JDK 17+ e Android SDK (platform 35, build-tools 35).

```bash
echo "sdk.dir=/caminho/do/android-sdk" > local.properties
./gradlew testDebugUnitTest      # 79 testes
./gradlew assembleDebug          # app/build/outputs/apk/debug/app-arm64-v8a-debug.apk
./gradlew assembleRelease        # app/build/outputs/apk/release/app-arm64-v8a-release.apk
```

Para alterar perguntas: edite `tools/questions/parte*.py` e rode `python3 tools/questions/build_questions.py`
(valida tudo e regrava o `questions.json`; falha se houver erro). Ícones: `python3 tools/make_icons.py`.

## O que foi implementado

**Identidade visual** — tema arcade de alto contraste, fonte pixel (Silkscreen, OFL) só em títulos e texto comum grande nas perguntas; botões grandes com sombra pixelada; céu estrelado, título pulando e "APERTE START" piscando (respeitam "Remover animações" do Android); ícone adaptativo original (balão + "?" em pixel art) com versão monocromática e PNGs mdpi→xxxhdpi; efeitos sonoros originais sintetizados (onda quadrada, volume baixo, podem ser desligados).

**Jogadores** — cadastrar, editar, remover, reordenar (▲▼) ou sortear; idade opcional; nomes repetidos são recusados (o apresentador chama pelo nome). Os jogadores ficam salvos e cada um tem a chave **"Joga"** (em Jogadores e em Nova partida) para participar ou ficar fora da próxima partida sem apagar o cadastro. O app começa sem jogadores pré-cadastrados.

**Modos** — Rodadas por tema; Número de perguntas (por jogador, temas alternados); Melhor de três (vence a partida quem fizer mais pontos nela; campeão quem vencer 2 partidas; se após 3 partidas ninguém tiver 2 vitórias, os líderes vão ao desempate — a regra aparece na tela); Conhecimentos do Brasil. Temas e dificuldades escolhidos antes da partida.

**Idades** — até 9 anos: perguntas fáceis; 10–12: fáceis e médias; 13–15: até difíceis; adultos/idade não informada: as dificuldades escolhidas. A faixa etária da pergunta nunca é ultrapassada. Todos recebem o tema da rodada e o acerto vale 1 ponto para todos.

**Condução** — rodada, tema, jogador da vez, ordem (com "PRÓXIMO") e placar sempre visíveis. Uma pergunta por vez; não avança sem avaliação, pulo ou fim da vez. Botões: Repetir, Ouvir resposta, Responder tocando, Pular, Encerrar a vez, Anular pergunta (áudio/interrupção, jogador errado, repetida — troca sem mexer no placar) e Desfazer último ponto. Depois de cada resposta: certo/errado, resposta certa, explicação, fonte, placar e próximo jogador. Empate no fim: pergunta de desempate inédita (não altera o placar) ou empate aceito. "Encerrar" termina a partida com o placar atual.

**Voz padrão** — o jogo já vem pronto com a voz do sistema Android (detalhes abaixo).

**Voz neural (download opcional)** — em Configurações › Voz do apresentador há o botão "Baixar voz neural". Antes de baixar, o app explica o tamanho (~61 MB), de onde vem (Hugging Face, versão fixa do repositório público do modelo) e que nada sobre os jogadores é enviado; só baixa se o jogador confirmar. Há barra de progresso e "Cancelar" (o download pode ser retomado sem rebaixar o que já veio). Cada arquivo só é aceito se o tamanho e o SHA-256 baterem com os valores fixados no app. Depois de baixada, a voz (modelo Piper "faber", rodando no próprio celular com o sherpa-onnx) é bem mais natural e **funciona sem internet**; dá para alternar entre "Usar a voz neural" e "Usar a voz padrão" e "Apagar voz neural (liberar espaço)" a qualquer momento. Cada frase é gerada em segundo plano enquanto a anterior toca, e o aviso de "fim da leitura" só vem quando o último som termina — o microfone continua abrindo só depois da leitura. Se a voz neural não carregar no aparelho, o app volta sozinho para a voz do sistema. Amostras em [`docs/vozes/`](docs/vozes/).

**Vozes do sistema (padrão)** — o app escolhe automaticamente a voz em português mais natural instalada no aparelho (maior qualidade informada pelo mecanismo, preferindo pt-BR e vozes que funcionam sem internet). Em Configurações › Voz do apresentador dá para trocar o mecanismo (ex.: Google, Samsung), escolher a voz (a mais natural vem marcada com ★), ajustar tom e velocidade, ouvir um exemplo e abrir a instalação de vozes de alta qualidade do Android. Vozes online, que costumam ser ainda mais naturais, só aparecem se você ativar "Permitir vozes online", com o aviso de que o texto falado (perguntas e nomes) vai para o provedor. As falas variam ("Paula, é com você!", "Valendo!", "Isso mesmo!") para soar menos mecânico.

**Apresentador por voz** — anuncia a vez, tema e dificuldade, lê a pergunta e todas as alternativas com pausas; o microfone só abre quando a fala termina (cada leitura tem uma ficha: aviso atrasado de leitura antiga é ignorado). Indicador vermelho "MICROFONE ATIVO" com Parar e Cancelar; mostra a transcrição parcial e final. Interpretação das respostas:
- "letra B", "alternativa C", "a segunda", o texto da alternativa, "verdadeiro/falso", números falados ("mil oitocentos e vinte e dois");
- dúvida ("acho que…", "será…"), confiança baixa ou correspondência parcial → mostra a transcrição e pede confirmação (toque ou "sim/não" falado);
- duas alternativas citadas, menção negada ("não é a B") ou resposta aberta quase igual → pede esclarecimento; em resposta aberta o jogador pode manter a resposta e o grupo decide;
- "repete", "não entendi" → relê (não é resposta); "passo", "não sei" → pede confirmação antes de pular/encerrar a vez;
- silêncio → "Não ouvi", nenhum ponto. A fala é sempre atribuída ao jogador da vez.

**Banco de perguntas** — **788 perguntas** em **23 temas**: Geografia, História, Ciência, Tecnologia, Cinema, Filmes infantis, Novelas, Televisão, Esportes, Marcas e slogans, Música, Literatura, Natureza, Cultura brasileira, Curiosidades, Língua portuguesa, Matemática, Política e cidadania, Artes, Mitologia e lendas, Astronomia e espaço, Corpo humano e saúde e Culinária. São 331 fáceis, 272 médias, 146 difíceis e 39 muito difíceis; 253 são sobre o Brasil. Cada uma tem id, texto, tema, subtema, dificuldade, faixa etária, formato, alternativas, resposta, sinônimos, explicação, fonte e, quando o fato pode mudar, data de referência (ex.: "Censo 2022", "Até a Copa de 2022"). O validador recusa alternativas duplicadas, resposta fora das alternativas, enunciado que contém a resposta e quase-duplicatas; uma auditoria extra procurou perguntas que entregassem a resposta de outra do mesmo assunto. Todos os temas têm pelo menos 4 perguntas para crianças de 6 anos. Política e cidadania trata só de instituições e regras (Constituição, eleições, Poderes), sem temas partidários.

**Inéditas e histórico** — nenhuma pergunta (nem quase igual) se repete na partida; o histórico fica no aparelho e é consultado na seleção (por id e por "impressão digital" do enunciado, que pega pequenas reescritas). As perguntas de cada rodada são escolhidas antes de ela começar. Quando as inéditas de um tema acabam, o app avisa e marca "Já usada em partida anterior" — nunca diz "Inédita" sem consultar o histórico. Em Configurações: inéditas por tema e "Limpar histórico".

**Placar e integridade** — o placar é sempre calculado a partir do registro de perguntas avaliadas (não existe outro caminho para mudar pontos). Histórico da partida com jogador, pergunta, resposta dada, forma (voz/toque/digitada/grupo), resultado e ponto; itens desfeitos aparecem riscados. A partida é salva a cada ação (escrita atômica) e retomada após o app ser fechado ou interrompido.

**Permissões** — na primeira abertura o app explica e pede, de uma vez, o microfone e o consentimento para o reconhecimento de fala ("Permitir microfone" ou "Agora não (só toque)"). Não pergunta de novo a cada partida; dá para mudar depois em Configurações.

**Privacidade** — a internet só é usada se o jogador pedir para baixar a voz neural opcional (o download apenas busca os arquivos públicos da voz, sem enviar nada sobre os jogadores); nomes, idades, respostas e histórico ficam no aparelho; backup em nuvem desativado. Não grava nem guarda áudio. O microfone é pedido na primeira abertura, com explicação, e só é usado quando o jogo espera a resposta. Como o reconhecimento de fala do Android pode usar serviço online (geralmente Google), o app mostra um aviso e pede consentimento; recusando, tudo funciona por toque. Também há modo sem voz.

## Validação feita

79 testes automatizados, todos passando (`./gradlew testDebugUnitTest`):

| Requisito | Como foi verificado |
|---|---|
| 7 jogadores, ordem nunca se perde | `GameEngineTest.sevenPlayersKeepStrictTurnOrderThroughRandomActions`: 25 partidas de 8 rodadas com 7 jogadores (incl. 6, 9 e 13 anos) e ações aleatórias (repetir, anular, pular, sem resposta, desfazer, Continuar fora de hora, desempates); confere a vez a cada passo e a ordem de cada rodada. `TouchUiTest` joga uma partida inteira de 7 jogadores pela interface. |
| Respostas certas, erradas, inaudíveis, repetidas, interrompidas | `VoiceFlowTest` (resposta clara, confirmação, "repete", silêncio, interrupção com retomada do disco, desfazer após erro de escuta) e `AnswerInterpreterTest` (17 casos, incluindo falar exatamente cada uma das 334 respostas). |
| Placar só muda com resposta avaliada | `scoreChangesOnlyAfterAnEvaluatedAnswer`, invariante checada a cada passo da simulação, `undoFixesTheLastResultOnlyForThatPlayer`. |
| Repetir não conta nem altera pontos | `repeatIsNotAnAnswerAndChangesNothing`, `askingToRepeatIsNotAnAnswer`. |
| Perguntas usadas não voltam | `usedQuestionsDoNotReturnInLaterGames`, `rewordedQuestionIsDetectedThroughHistoryFingerprint`, `whenFreshQuestionsRunOutTheReuseIsFlagged`, sem repetição/quase-duplicata na simulação. |
| Crianças recebem perguntas adequadas | `childrenReceiveAgeAppropriateQuestions` (criança de 6 anos em todos os temas, mesmo com adultos em "muito difícil") e checagem em todas as simulações. |
| Modo por toque sem microfone | `touchOnlyGameWorksWithoutAnySpeechRecognizer` (ViewModel) e `TouchUiTest` (partida completa por toques, celular e tablet). |
| Permissões na primeira abertura | `permissionsAreRequestedOnceAtFirstLaunch`, `decliningAtLaunchKeepsTheGameTouchOnly`. |
| Jogadores salvos que não jogam | `inactivePlayersStaySavedButDoNotPlay` e `TouchUiTest` (desliga um jogador pela tela; a partida segue só com os demais, na ordem). |
| Voz mais natural | `NeuralSpeakerTest` (fila, ordem, fim só após o último som, interrupção, falha do modelo), `NeuralVoicePackTest` (download contra servidor local: hashes conferidos, arquivo adulterado ou grande demais rejeitado, erro do servidor, cancelar e retomar, apagar), `theDefaultVoiceIsTheSystemOneAndTheNeuralVoiceNeedsToBeDownloaded` e `tools/voz-neural/verificar.sh`, que baixa os arquivos reais e gera áudio de verdade; `theMostNaturalOfflineVoiceIsChosenAndCanBeChanged` para as vozes do sistema. |
| Banco de perguntas | `QuestionBankTest` (788 perguntas válidas, sem quase-duplicatas, cobertura por tema/idade) e `everyBankAnswerIsRecognizedWhenSpokenExactly` (as 788 respostas faladas são entendidas). |
| Microfone só ao esperar resposta | `microphoneOpensOnlyAfterTheQuestionAndOptionsAreRead`, `lateCallbackFromAnInterruptedReadingNeverOpensTheMicrophone`, `microphoneNeverOpensOutsideAQuestion`, `speechNeedsConsentAndPermissionFirst`. |

## Limitações conhecidas

- **Não foi testado em aparelho físico nem em emulador** (o ambiente de desenvolvimento não tem aceleração de hardware para emulador). A interface foi executada com Robolectric; a voz e o microfone foram testados com implementações falsas que seguem o contrato do TextToSpeech/SpeechRecognizer. Vale um teste real de voz: sotaques, ruído da sala e o comportamento do serviço de reconhecimento variam de aparelho para aparelho.
- **Voz neural no celular:** o download real foi verificado com o próprio código do app (64 MB do Hugging Face, hashes conferidos) e a síntese gerando áudio real num PC com esses arquivos, e a lógica de reprodução foi testada com falsos, mas ela ainda não rodou num celular de verdade. No PC, 25 s de fala saem em ~2,5 s; em celulares muito antigos pode haver uma pequena pausa antes de cada frase. Se algo falhar, o app usa a voz do sistema automaticamente.
- **Tamanho:** o APK tem ~24 MB (debug). A voz neural (~61 MB) só ocupa espaço se for baixada. Há uma só voz neural (faber); amostras de outras vozes estão em `docs/vozes/`.
- **Download da voz:** depende do Hugging Face continuar servindo a versão fixada do modelo. Se ele sair do ar, o download falha com uma mensagem e o jogo segue com a voz padrão.
- O reconhecimento de fala depende do serviço instalado (normalmente Google). O app pede processamento no aparelho, mas não consegue garantir que o serviço não use a internet — por isso o aviso e o consentimento. Sem voz em português instalada, o app avisa e segue no modo tela/toque.
- O APK *release* minificado não foi executado; use o APK de teste (*debug*) para avaliação.
- As perguntas foram escritas e revisadas com cuidado, e as fontes indicam onde checar cada fato, mas as referências não foram consultadas online nesta sessão. Recomendo uma revisão humana, especialmente de novelas, marcas/slogans e datas.
- O desempate usa apenas perguntas inéditas; se acabarem, a opção é aceitar o empate.
- "Desfazer último ponto" vale para o resultado exibido na hora (antes de tocar em Continuar). Para resultados anteriores, o histórico mostra tudo, mas não edita.
- A dificuldade é adaptada pela idade; não há ajuste manual de nível por jogador.
- O histórico de perguntas é por aparelho (não sincroniza entre celulares).

## Licenças

Código e perguntas: deste projeto. Sons e ícone: criados para este app.
- Fonte Silkscreen © The Silkscreen Project Authors — SIL Open Font License 1.1 (`licenses/Silkscreen-OFL.txt`).
- sherpa-onnx (motor da voz neural) — Apache 2.0 (`licenses/sherpa-onnx-LICENSE.txt`).
- Voz Piper pt_BR "faber" — dados de treino CC0 (`licenses/voz-faber-MODEL_CARD.txt`).
- Dados de fonética do espeak-ng (baixados junto com a voz neural opcional) — GPL v3 (`licenses/espeak-ng-COPYING.txt`). O código-fonte completo deste app está neste repositório.
