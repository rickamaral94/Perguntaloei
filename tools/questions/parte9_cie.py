# Perguntas novas: ciência. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "cie"

# =========================================================== FÁCEIS
mc(T, "estados físicos", 1, 6, "O que acontece com uma poça de água no chão depois de um dia de sol forte?",
   ["Ela seca e some", "Ela vira gelo", "Ela fica maior", "Ela vira areia"], "Ela seca e some",
   "O calor do sol faz a água evaporar, e ela vai para o ar na forma de vapor.",
   "Enciclopédia Britannica – verbete 'Evaporation'")
tf(T, "segurança elétrica", 1, 6, "É seguro mexer em aparelhos ligados na tomada com as mãos molhadas.", False,
   "A água facilita a passagem da corrente elétrica pelo corpo e aumenta muito o risco de choque.",
   "Abracopel – Associação Brasileira de Conscientização para os Perigos da Eletricidade")
tf(T, "segurança elétrica", 1, 6, "Soltar pipa perto dos fios da rede elétrica é perigoso.", True,
   "A linha pode encostar nos fios e conduzir a eletricidade até quem está segurando a pipa.",
   "ANEEL – Agência Nacional de Energia Elétrica", br=True)
mc(T, "som", 1, 6, "Quando batemos num tambor, ele vibra e produz o quê?",
   ["Som", "Luz", "Chuva", "Fumaça"], "Som",
   "Todo som nasce de uma vibração, que faz o ar tremer até chegar aos nossos ouvidos.",
   "Enciclopédia Britannica – verbete 'Sound'")
mc(T, "luz", 1, 6, "Qual objeto reflete a nossa imagem e usamos para pentear o cabelo?",
   ["Espelho", "Travesseiro", "Toalha", "Cortina"], "Espelho",
   "O espelho é uma superfície bem lisa que reflete a luz e forma a nossa imagem.",
   "Enciclopédia Britannica – verbete 'Mirror'")
mc(T, "reciclagem", 1, 6, "O que devemos fazer com uma garrafa de plástico vazia para ajudar o planeta?",
   ["Colocar no lixo reciclável", "Jogar no rio", "Jogar na rua", "Enterrar no quintal"], "Colocar no lixo reciclável",
   "Separado para a reciclagem, o plástico pode virar novos objetos em vez de poluir a natureza.",
   "Ministério do Meio Ambiente – Coleta seletiva")
mc(T, "medidas", 1, 6, "Qual objeto usamos para medir o comprimento de um lápis?",
   ["Régua", "Balança", "Relógio", "Termômetro"], "Régua",
   "A régua mostra o comprimento em centímetros e milímetros.",
   "Inmetro – Unidades de medida")
mc(T, "medidas", 1, 6, "Qual aparelho mostra quantos quilos uma pessoa pesa?",
   ["Balança", "Régua", "Bússola", "Relógio"], "Balança",
   "A balança mede a massa, que no dia a dia chamamos de peso, em quilogramas.",
   "Inmetro – Unidades de medida")
mc(T, "luz", 1, 6, "Qual destes objetos usamos para ver bem maiores coisas pequenas, como uma formiga?",
   ["Lupa", "Espelho", "Peneira", "Régua"], "Lupa",
   "A lupa tem uma lente que aumenta a imagem do que olhamos de perto.",
   "Enciclopédia Britannica – verbete 'Magnifying glass'")
mc(T, "forças", 1, 6, "O que sentimos quando esfregamos as mãos uma na outra bem rápido?",
   ["As mãos esquentam", "As mãos ficam geladas", "As mãos ficam molhadas", "As mãos mudam de cor"],
   "As mãos esquentam",
   "O atrito entre as mãos transforma o movimento em calor.",
   "Enciclopédia Britannica – verbete 'Friction'")
op(T, "luz", 1, 6, "Como se chama o arco colorido que aparece no céu quando faz sol e chove ao mesmo tempo?",
   "Arco-íris", ["arco-íris", "arco-iris", "arco íris", "arco iris"],
   "A luz do sol se divide em cores ao entrar nas gotas de chuva, refletir dentro delas e sair de volta.",
   "Enciclopédia Britannica – verbete 'Rainbow'")
mc(T, "eletricidade", 1, 7, "Qual destes materiais cobre os fios elétricos para proteger contra choques?",
   ["Plástico", "Cobre", "Ferro", "Alumínio"], "Plástico",
   "O plástico é isolante, ou seja, não deixa a corrente elétrica passar com facilidade.",
   "Enciclopédia Britannica – verbete 'Insulator'")
mc(T, "misturas", 1, 7, "Quando mexemos açúcar num copo de água até ele sumir, o que aconteceu com o açúcar?",
   ["Dissolveu-se", "Evaporou", "Congelou", "Derreteu"], "Dissolveu-se",
   "O açúcar não derrete: ele se espalha entre as partículas de água, formando uma mistura doce.",
   "Enciclopédia Britannica – verbete 'Solution'", syn=("dissolveu", "se dissolveu"))
tf(T, "flutuação", 1, 7, "Uma moeda de metal jogada numa bacia com água fica boiando.", False,
   "A moeda é mais densa que a água e por isso afunda.",
   "Enciclopédia Britannica – verbete 'Buoyancy'")
mc(T, "luz", 1, 7, "Qual destes produz a própria luz?",
   ["Uma vela acesa", "Um espelho", "A Lua", "Uma janela"], "Uma vela acesa",
   "A chama da vela emite luz, enquanto o espelho e a Lua apenas refletem a luz de outras fontes.",
   "Enciclopédia Britannica – verbete 'Light'")
mc(T, "magnetismo", 1, 8, "O que acontece quando aproximamos dois ímãs pelos polos iguais?",
   ["Eles se empurram", "Eles grudam", "Eles esquentam", "Eles acendem"], "Eles se empurram",
   "Polos iguais se repelem e polos diferentes se atraem.",
   "Enciclopédia Britannica – verbete 'Magnet'")
mc(T, "máquinas simples", 1, 8, "Qual brinquedo de parquinho funciona como uma alavanca, com uma criança em cada ponta?",
   ["Gangorra", "Escorregador", "Balanço", "Carrossel"], "Gangorra",
   "A gangorra é uma barra apoiada no meio, que é exatamente o funcionamento de uma alavanca.",
   "Enciclopédia Britannica – verbete 'Lever'")
tf(T, "calor", 1, 8, "Ao sol, uma camiseta preta esquenta mais do que uma camiseta branca.", True,
   "As cores escuras absorvem mais luz e a transformam em calor; o branco reflete a maior parte dela.",
   "Enciclopédia Britannica – verbete 'Absorption'")
mc(T, "química da cozinha", 1, 8, "O que acontece quando misturamos vinagre com bicarbonato de sódio?",
   ["Formam muitas bolhas", "Viram gelo", "Ficam azuis", "Ficam duros como pedra"], "Formam muitas bolhas",
   "O ácido do vinagre reage com o bicarbonato e libera gás carbônico, que forma as bolhas.",
   "Enciclopédia Britannica – verbete 'Sodium bicarbonate'")
mc(T, "calor", 1, 8, "Para que serve uma garrafa térmica?",
   ["Manter a bebida quente ou fria por mais tempo", "Ferver a água sozinha", "Congelar a bebida",
    "Adoçar a bebida"], "Manter a bebida quente ou fria por mais tempo",
   "Ela tem paredes duplas, quase sem ar entre elas, que dificultam a passagem do calor.",
   "Enciclopédia Britannica – verbete 'Vacuum flask'")
mc(T, "materiais", 1, 8, "O papel é feito principalmente de fibras de qual material?",
   ["Madeira", "Plástico", "Areia", "Pedra"], "Madeira",
   "As fibras de celulose da madeira são separadas, prensadas e secas até virar folhas de papel.",
   "Enciclopédia Britannica – verbete 'Paper'")
mc(T, "energia", 1, 8, "Qual destes meios de transporte usa a força do vento para se mover?",
   ["Barco a vela", "Bicicleta", "Trem elétrico", "Carro a gasolina"], "Barco a vela",
   "A vela recebe o empurrão do vento, que movimenta o barco sem precisar de motor.",
   "Enciclopédia Britannica – verbete 'Sailing'")
mc(T, "energia", 1, 9, "Nas barragens, a queda da água represada gira turbinas. Que usina é essa?",
   ["Hidrelétrica", "Eólica", "Solar", "Nuclear"], "Hidrelétrica",
   "As hidrelétricas são a principal fonte de eletricidade do Brasil, país cheio de rios caudalosos.",
   "Empresa de Pesquisa Energética – Matriz Elétrica Brasileira", br=True, ref="2026-10-13")
mc(T, "energia", 1, 9, "De qual planta é feita a maior parte do etanol usado como combustível no Brasil?",
   ["Cana-de-açúcar", "Mandioca", "Soja", "Café"], "Cana-de-açúcar",
   "O caldo da cana é fermentado e depois destilado para produzir o etanol que abastece os carros.",
   "Embrapa – Agroenergia", br=True, ref="2026-10-13")
op(T, "magnetismo", 1, 9, "Como se chamam as duas pontas de um ímã, onde a força de atração é mais forte?",
   "Polos", ["polos", "polo", "polo norte e polo sul", "polos norte e sul"],
   "Todo ímã tem um polo norte e um polo sul, e se for partido ao meio cada pedaço ganha os dois polos.",
   "Enciclopédia Britannica – verbete 'Magnet'")
tf(T, "segurança elétrica", 1, 9, "Durante uma tempestade com raios, ficar debaixo de uma árvore isolada no meio do campo é uma boa forma de se proteger.",
   False,
   "Árvores isoladas são alvos comuns de raios; o mais seguro é se abrigar dentro de casas ou de carros fechados.",
   "INPE – Grupo de Eletricidade Atmosférica (ELAT)")
mc(T, "eletricidade", 1, 9, "Por que o cabelo fica arrepiado e gruda num balão de festa esfregado nele?",
   ["Por causa da eletricidade estática", "Por causa do vento", "Por causa da gravidade",
    "Por causa do calor"], "Por causa da eletricidade estática",
   "Ao esfregar, o balão e o cabelo trocam elétrons e ficam com cargas opostas, que se atraem.",
   "Enciclopédia Britannica – verbete 'Static electricity'")

# =========================================================== MÉDIAS
mc(T, "energia", 2, 10, "Qual usina hidrelétrica, no rio Paraná, pertence ao mesmo tempo ao Brasil e ao Paraguai?",
   ["Itaipu", "Belo Monte", "Tucuruí", "Sobradinho"], "Itaipu",
   "A Itaipu Binacional fica na fronteira entre os dois países, perto de Foz do Iguaçu.",
   "Itaipu Binacional – Institucional", br=True)
mc(T, "energia", 2, 10, "Como se chamam as grandes torres com hélices que transformam a força do vento em eletricidade?",
   ["Aerogeradores", "Painéis solares", "Turbinas a vapor", "Geradores a diesel"], "Aerogeradores",
   "No Brasil, a maior parte da energia eólica é produzida no Nordeste, onde os ventos são fortes e constantes.",
   "Empresa de Pesquisa Energética – Energia eólica", br=True)
mc(T, "química da cozinha", 2, 10, "Qual gás é colocado nos refrigerantes para formar as bolhinhas?",
   ["Gás carbônico", "Oxigênio", "Hélio", "Gás de cozinha"], "Gás carbônico",
   "O gás carbônico é dissolvido sob pressão e escapa em bolhas quando a garrafa é aberta.",
   "Enciclopédia Britannica – verbete 'Carbonation'")
tf(T, "estados físicos", 2, 10, "Uma garrafa de vidro cheia de água pode rachar no congelador, porque a água aumenta de volume ao congelar.",
   True,
   "Ao virar gelo, a água ocupa cerca de nove por cento a mais de espaço e pressiona o vidro.",
   "Enciclopédia Britannica – verbete 'Ice'")
op(T, "luz", 2, 10, "Qual peça de vidro em forma de triângulo separa a luz branca nas cores do arco-íris?",
   "Prisma", ["prisma", "prisma de vidro"],
   "Isaac Newton usou prismas para mostrar que a luz branca é uma mistura de cores.",
   "Enciclopédia Britannica – verbete 'Prism'")
mc(T, "forças", 2, 10, "Qual força faz uma bola rolando na grama ir parando aos poucos?",
   ["Atrito", "Magnetismo", "Eletricidade", "Empuxo"], "Atrito",
   "O atrito entre a bola e a grama se opõe ao movimento e vai freando a bola até ela parar.",
   "Enciclopédia Britannica – verbete 'Friction'")
tf(T, "flutuação", 2, 10, "É mais fácil boiar na água do mar do que na água de uma piscina.", True,
   "O sal deixa a água do mar mais densa, e ela empurra o corpo para cima com mais força.",
   "Enciclopédia Britannica – verbete 'Buoyancy'")
tf(T, "flutuação", 2, 10, "Objetos pesados sempre afundam na água.", False,
   "Navios enormes de aço flutuam porque o casco, cheio de ar, desloca muita água.",
   "Enciclopédia Britannica – verbete 'Archimedes' principle'")
mc(T, "eletricidade", 2, 10, "Para uma lâmpada ligada a uma pilha acender, como precisa estar o caminho da eletricidade?",
   ["Fechado", "Aberto", "Cortado ao meio", "Desligado da pilha"], "Fechado",
   "A corrente só passa num circuito fechado, quando os fios formam um caminho completo.",
   "Enciclopédia Britannica – verbete 'Electric circuit'")
tf(T, "magnetismo", 2, 10, "Um ímã comum atrai as latinhas de alumínio.", False,
   "O alumínio não é atraído por ímãs comuns; os principais metais atraídos são ferro, níquel e cobalto.",
   "Enciclopédia Britannica – verbete 'Ferromagnetism'")
mc(T, "luz", 2, 10, "Qual cor aparece na parte de cima, por fora, de um arco-íris comum?",
   ["Vermelho", "Violeta", "Verde", "Azul"], "Vermelho",
   "No arco-íris principal, o vermelho fica por fora e o violeta por dentro.",
   "Enciclopédia Britannica – verbete 'Rainbow'")
mc(T, "reciclagem", 2, 10, "Nas lixeiras coloridas da coleta seletiva no Brasil, qual cor é a do papel?",
   ["Azul", "Verde", "Amarelo", "Vermelho"], "Azul",
   "Pelo padrão do Conama, azul é papel, vermelho é plástico, verde é vidro e amarelo é metal.",
   "Conama – Resolução nº 275/2001", br=True)
mc(T, "química da cozinha", 2, 10, "Como se chamam os lugares no litoral onde a água do mar evapora para produzir sal?",
   ["Salinas", "Manguezais", "Restingas", "Dunas"], "Salinas",
   "O Rio Grande do Norte é o maior produtor de sal marinho do Brasil, graças às suas salinas.",
   "IBGE – Produção mineral", br=True)
op(T, "máquinas simples", 2, 10, "Qual máquina simples, formada por uma roda com uma corda, ajuda a puxar baldes de um poço?",
   "Roldana", ["roldana", "polia", "carretilha"],
   "A roldana muda a direção da força: puxamos para baixo e o balde sobe.",
   "Enciclopédia Britannica – verbete 'Pulley'")
mc(T, "calor", 2, 10, "Por que as roupas de lã nos deixam aquecidos no frio?",
   ["Ajudam a manter o calor do corpo", "Produzem calor sozinhas", "Puxam o calor do sol",
    "Esfriam o vento"], "Ajudam a manter o calor do corpo",
   "A lã guarda ar entre os fios, e esse ar dificulta a saída do calor que o corpo produz.",
   "Enciclopédia Britannica – verbete 'Thermal insulation'")
mc(T, "química da cozinha", 2, 12, "O suco de limão e o vinagre são substâncias de que tipo?",
   ["Ácidas", "Básicas", "Neutras", "Gasosas"], "Ácidas",
   "Os ácidos têm gosto azedo: o limão tem ácido cítrico e o vinagre tem ácido acético.",
   "Enciclopédia Britannica – verbete 'Acid'")
mc(T, "medidas", 2, 12, "Qual é a unidade básica de massa no Sistema Internacional de Unidades?",
   ["Quilograma", "Grama", "Libra", "Tonelada"], "Quilograma",
   "O quilograma é a única unidade de base do Sistema Internacional que tem um prefixo no nome.",
   "Inmetro – Sistema Internacional de Unidades")
mc(T, "segurança elétrica", 2, 12, "Para que serve o pino do meio das tomadas de três pinos usadas no Brasil?",
   ["Fazer o aterramento e proteger contra choques", "Deixar a energia mais forte",
    "Economizar energia", "Ligar dois aparelhos ao mesmo tempo"],
   "Fazer o aterramento e proteger contra choques",
   "O fio terra leva para o chão a eletricidade que escapa da carcaça de um aparelho com defeito.",
   "Inmetro – Padrão brasileiro de plugues e tomadas", br=True)
mc(T, "eletricidade", 2, 12, "Qual peça do quadro de luz desliga a energia sozinha quando há sobrecarga ou curto-circuito?",
   ["Disjuntor", "Interruptor", "Benjamim", "Extensão"], "Disjuntor",
   "O disjuntor corta a corrente quando ela fica alta demais, evitando aquecimento e incêndios nos fios.",
   "Enciclopédia Britannica – verbete 'Circuit breaker'")
mc(T, "cientistas", 2, 12, "Qual processo, que aquece o leite para eliminar micróbios, recebeu o nome de um cientista francês?",
   ["Pasteurização", "Fermentação", "Destilação", "Evaporação"], "Pasteurização",
   "O nome homenageia Louis Pasteur, que mostrou que um aquecimento moderado elimina a maior parte dos micróbios que estragam os alimentos.",
   "Enciclopédia Britannica – verbete 'Pasteurization'")
mc(T, "método científico", 2, 12, "No método científico, como se chama a explicação provável que o cientista testa com experimentos?",
   ["Hipótese", "Conclusão", "Observação", "Tabela"], "Hipótese",
   "Se os experimentos não confirmarem a hipótese, o cientista a corrige ou cria outra.",
   "Enciclopédia Britannica – verbete 'Scientific method'")
mc(T, "recursos naturais", 2, 12, "O pré-sal é uma camada de rocha bem abaixo do fundo do mar com grandes reservas de qual recurso?",
   ["Petróleo", "Ouro", "Carvão", "Água doce"], "Petróleo",
   "As reservas do pré-sal ficam no litoral do Sudeste, a vários quilômetros de profundidade.",
   "Petrobras – Pré-sal", br=True)
op(T, "estados físicos", 2, 12, "Qual é o nome científico do derretimento, a passagem do estado sólido para o líquido?",
   "Fusão", ["fusão", "fusao"],
   "O gelo, por exemplo, passa por fusão a zero grau Celsius e vira água líquida.",
   "Enciclopédia Britannica – verbete 'Melting'")

# =========================================================== DIFÍCEIS
tf(T, "eletricidade", 3, 12, "Segundo o INPE, o Brasil é o país com o maior número de raios do mundo.", True,
   "Pelos dados do INPE, dezenas de milhões de raios atingem o território brasileiro todos os anos.",
   "INPE – Grupo de Eletricidade Atmosférica (ELAT)", br=True, ref="2026-10-13")
op(T, "forças", 3, 12, "Como se chama a força que a água faz para cima e ajuda os objetos a flutuar?",
   "Empuxo", ["empuxo", "força de empuxo"],
   "Pelo princípio de Arquimedes, o empuxo é igual ao peso da água que o objeto desloca.",
   "Enciclopédia Britannica – verbete 'Buoyancy'")
tf(T, "luz", 3, 12, "Para ver um arco-íris, a pessoa precisa estar de costas para o Sol.", True,
   "O arco-íris se forma no lado oposto ao Sol, porque as gotas devolvem a luz na direção de quem olha.",
   "Enciclopédia Britannica – verbete 'Rainbow'")
tf(T, "estados físicos", 3, 12, "A água salgada congela a uma temperatura mais alta do que a água doce.", False,
   "O sal abaixa o ponto de congelamento: a água do mar só congela por volta de dois graus negativos.",
   "Enciclopédia Britannica – verbete 'Seawater'")
mc(T, "energia", 3, 12, "Em qual município do Rio de Janeiro ficam as usinas nucleares brasileiras?",
   ["Angra dos Reis", "Paraty", "Macaé", "Niterói"], "Angra dos Reis",
   "A Central Nuclear Almirante Álvaro Alberto reúne as usinas Angra 1 e Angra 2.",
   "Eletronuclear – Institucional", br=True, ref="2026-10-13")
tf(T, "calor", 3, 14, "No alto de montanhas muito altas, a água ferve a uma temperatura menor que cem graus Celsius.", True,
   "Com menos pressão do ar, a água precisa de menos calor para ferver.",
   "Enciclopédia Britannica – verbete 'Boiling point'")
mc(T, "calor", 3, 14, "Em qual escala de temperatura, usada pelos cientistas, o zero corresponde ao zero absoluto?",
   ["Kelvin", "Celsius", "Fahrenheit", "Réaumur"], "Kelvin",
   "O zero absoluto, a menor temperatura possível, equivale a cerca de 273 graus Celsius negativos.",
   "Inmetro – Sistema Internacional de Unidades")
op(T, "luz", 3, 14, "As cores primárias da luz, usadas nas telas, são vermelho, verde e qual outra?",
   "Azul", ["azul"],
   "Combinando pontinhos vermelhos, verdes e azuis, as telas formam todas as outras cores.",
   "Enciclopédia Britannica – verbete 'Additive color'")
mc(T, "cientistas", 3, 14, "Qual monge estudou ervilhas e descobriu as leis básicas da hereditariedade?",
   ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Robert Hooke"], "Gregor Mendel",
   "Mendel cruzou milhares de pés de ervilha e é considerado o pai da genética.",
   "Enciclopédia Britannica – verbete 'Gregor Mendel'")
tf(T, "cientistas", 3, 14, "O naturalista Charles Darwin passou pelo Brasil durante a viagem do navio Beagle.", True,
   "Em 1832, Darwin esteve em Salvador e no Rio de Janeiro e se encantou com a Mata Atlântica.",
   "Enciclopédia Britannica – verbete 'Charles Darwin'", br=True)
mc(T, "pesquisa brasileira", 3, 14, "Qual empresa pública brasileira de pesquisa ajudou a adaptar a soja ao clima do Cerrado?",
   ["Embrapa", "Petrobras", "Fiocruz", "Eletrobras"], "Embrapa",
   "As pesquisas da Embrapa permitiram plantar soja em regiões quentes e transformaram o Cerrado em grande produtor.",
   "Embrapa Soja – Histórico", br=True)
mc(T, "pesquisa brasileira", 3, 14, "Qual instituto brasileiro usa imagens de satélite para medir o desmatamento da Amazônia?",
   ["INPE", "IBGE", "Fiocruz", "Instituto Butantan"], "INPE",
   "O Instituto Nacional de Pesquisas Espaciais faz esse acompanhamento com os sistemas Prodes e Deter.",
   "INPE – Programa de Monitoramento da Amazônia", br=True,
   syn=("instituto nacional de pesquisas espaciais",))

# =========================================================== MUITO DIFÍCEIS
mc(T, "energia", 4, 16, "Qual programa do governo brasileiro, lançado em 1975, incentivou o uso do álcool como combustível?",
   ["Proálcool", "Procel", "Luz para Todos", "Pró-Sal"], "Proálcool",
   "O Proálcool foi criado na crise do petróleo dos anos 1970 e levou aos carros movidos a álcool.",
   "Embrapa – Agroenergia", br=True)
mc(T, "tabela periódica", 4, 16, "Qual elemento químico Marie Curie batizou em homenagem à sua terra natal?",
   ["Polônio", "Rádio", "Urânio", "Frâncio"], "Polônio",
   "Marie Curie nasceu na Polônia, e o polônio foi descoberto por ela e Pierre Curie em 1898.",
   "Enciclopédia Britannica – verbete 'Polonium'")
mc(T, "cientistas", 4, 16, "Qual bióloga do Museu Nacional, especialista em sapos e pererecas, também liderou a luta pelo voto feminino no Brasil?",
   ["Bertha Lutz", "Johanna Döbereiner", "Graziela Barroso", "Nise da Silveira"], "Bertha Lutz",
   "Bertha Lutz estudou anfíbios no Museu Nacional e foi uma das líderes do movimento pelo voto das mulheres.",
   "Museu Nacional/UFRJ – Bertha Lutz", br=True)
mc(T, "cientistas", 4, 16, "Qual pesquisadora da Embrapa ficou famosa por estudar bactérias que ajudam a soja a aproveitar o nitrogênio do ar?",
   ["Johanna Döbereiner", "Bertha Lutz", "Graziela Barroso", "Mayana Zatz"], "Johanna Döbereiner",
   "Seus estudos de fixação biológica de nitrogênio permitiram plantar soja quase sem adubo nitrogenado.",
   "Embrapa Agrobiologia – Johanna Döbereiner", br=True)
mc(T, "pesquisa brasileira", 4, 16, "Qual é o nome do acelerador de partículas brasileiro, uma grande fonte de luz síncrotron instalada em Campinas?",
   ["Sirius", "Atlas", "Vega", "Antares"], "Sirius",
   "O Sirius, do Centro Nacional de Pesquisa em Energia e Materiais, produz uma luz potente que revela a estrutura dos materiais.",
   "CNPEM – Sirius", br=True)
tf(T, "cientistas", 4, 16, "Albert Einstein ganhou o Prêmio Nobel de Física por causa da teoria da relatividade.", False,
   "O Nobel de Física de 1921 foi dado a Einstein por explicar o efeito fotoelétrico, não pela relatividade.",
   "Nobel Prize – Albert Einstein, Facts")
