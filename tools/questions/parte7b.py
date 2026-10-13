# Perguntas novas (parte 7b). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== CIÊNCIA
C = "cie"
mc(C, "física", 1, 6, "Qual instrumento usamos para medir a temperatura?",
   ["Termômetro", "Régua", "Balança", "Relógio"], "Termômetro",
   "O termômetro indica a temperatura, por exemplo, do ar, da água ou do corpo.",
   "Enciclopédia Britannica – verbete 'Thermometer'")
tf(C, "luz", 1, 6, "A sombra se forma quando um objeto bloqueia a passagem da luz.", True,
   "A luz anda em linha reta, e a região atrás do objeto que ela não alcança fica escura.",
   "Enciclopédia Britannica – verbete 'Shadow'")
mc(C, "eletricidade", 1, 7, "Qual destes materiais conduz bem a eletricidade?",
   ["Cobre", "Borracha", "Madeira", "Plástico"], "Cobre",
   "O cobre é um metal ótimo condutor, por isso é usado nos fios elétricos; borracha, madeira seca e plástico são isolantes.",
   "Enciclopédia Britannica – verbete 'Copper'")
mc(C, "som", 1, 8, "Como se chama o som que volta até nós depois de bater numa parede ou montanha?",
   ["Eco", "Ruído", "Chiado", "Assobio"], "Eco",
   "O eco é o som refletido por uma superfície que chega aos nossos ouvidos um pouco depois do som original.",
   "Enciclopédia Britannica – verbete 'Echo'")
mc(C, "magnetismo", 1, 8, "Qual instrumento tem uma agulha magnetizada que aponta para o norte?",
   ["Bússola", "Barômetro", "Termômetro", "Cronômetro"], "Bússola",
   "A agulha da bússola é um pequeno ímã que se alinha ao campo magnético da Terra, apontando para o norte magnético.",
   "Enciclopédia Britannica – verbete 'Compass'")
tf(C, "química", 1, 9, "A ferrugem aparece quando o ferro reage com o oxigênio na presença de água.", True,
   "A ferrugem é um óxido de ferro formado pela reação do ferro com o oxigênio e a umidade.",
   "Enciclopédia Britannica – verbete 'Rust'")
op(C, "estados da matéria", 2, 10, "Como se chama a mudança de estado em que a água líquida vira gelo?",
   "Solidificação", ["solidificação", "solidificacao", "congelamento", "congelação", "congelacao"],
   "Na solidificação, um líquido perde calor e passa para o estado sólido.",
   "Enciclopédia Britannica – verbete 'Freezing'")
mc(C, "misturas", 2, 10, "Qual processo separa a areia da água fazendo a mistura passar por um papel ou pano?",
   ["Filtração", "Destilação", "Evaporação", "Imantação"], "Filtração",
   "Na filtração, o papel ou pano deixa a água passar e retém os grãos de areia.",
   "Enciclopédia Britannica – verbete 'Filtration'")
mc(C, "química", 2, 10, "No Brasil, as latas de refrigerante são feitas principalmente de qual metal?",
   ["Alumínio", "Chumbo", "Cobre", "Estanho"], "Alumínio",
   "As latas de bebida no Brasil são de alumínio, e o país está entre os que mais reciclam esse tipo de lata.",
   "Abralatas – Associação Brasileira dos Fabricantes de Latas de Alumínio", br=True)
mc(C, "eletricidade", 2, 12, "Qual peça transforma energia elétrica em movimento dentro de um ventilador?",
   ["Motor elétrico", "Pilha", "Transformador", "Resistor"], "Motor elétrico",
   "O motor elétrico usa a eletricidade e ímãs para fazer o eixo girar, movendo as hélices.",
   "Enciclopédia Britannica – verbete 'Electric motor'")
mc(C, "cientistas", 2, 12,
   "Segundo uma lenda antiga, qual sábio grego gritou 'Eureca!' na banheira ao descobrir como verificar se uma coroa era de ouro puro?",
   ["Arquimedes", "Pitágoras", "Aristóteles", "Euclides"], "Arquimedes",
   "A história, contada pelo romano Vitrúvio, diz que Arquimedes percebeu que a água deslocada permitia medir o volume da coroa.",
   "Enciclopédia Britannica – verbete 'Archimedes'")
tf(C, "física", 2, 12, "Uma pessoa pesa menos na Lua do que na Terra.", True,
   "A gravidade na superfície da Lua é cerca de um sexto da terrestre, então o peso fica bem menor, embora a massa seja a mesma.",
   "NASA")
mc(C, "luz", 3, 12, "Qual fenômeno faz um canudo parecer quebrado dentro de um copo com água?",
   ["Refração", "Reflexão", "Difração", "Dispersão"], "Refração",
   "A luz muda de direção ao passar da água para o ar, o que desloca a imagem da parte submersa do canudo.",
   "Enciclopédia Britannica – verbete 'Refraction'")
tf(C, "química", 3, 12, "O diamante e o grafite da ponta do lápis são formados pelo mesmo elemento químico.", True,
   "Os dois são feitos só de carbono; o que muda é a forma como os átomos estão organizados.",
   "Enciclopédia Britannica – verbete 'Carbon'")
mc(C, "cientistas", 3, 14, "Qual cientista francês descobriu a radioatividade, em 1896, estudando sais de urânio?",
   ["Henri Becquerel", "Wilhelm Röntgen", "Ernest Rutherford", "Niels Bohr"], "Henri Becquerel",
   "Becquerel notou que o urânio emitia radiação capaz de marcar chapas fotográficas, e dividiu o Nobel de 1903 com Pierre e Marie Curie.",
   "Prêmio Nobel – The Nobel Prize in Physics 1903")
mc(C, "química", 3, 14, "Qual é o número atômico do carbono?",
   ["6", "12", "8", "14"], "6",
   "O carbono tem seis prótons no núcleo; o número doze corresponde à massa do seu isótopo mais comum.",
   "IUPAC – Tabela Periódica dos Elementos")
op(C, "cientistas", 4, 16, "Qual cientista neozelandês concluiu, em 1911, que o átomo tem um núcleo pequeno e denso?",
   "Ernest Rutherford", ["ernest rutherford", "rutherford", "ernesto rutherford"],
   "Com o experimento da folha de ouro, Rutherford mostrou que quase toda a massa do átomo está num núcleo minúsculo.",
   "Enciclopédia Britannica – verbete 'Ernest Rutherford'")

# =========================================================== NATUREZA
C = "nat"
mc(C, "animais", 1, 6, "Qual animal tem uma tromba comprida?",
   ["Elefante", "Rinoceronte", "Hipopótamo", "Girafa"], "Elefante",
   "A tromba do elefante é o nariz unido ao lábio superior e serve para respirar, pegar comida e beber água.",
   "Enciclopédia Britannica – verbete 'Elephant'")
mc(C, "animais", 1, 6, "Qual animal da fazenda canta 'cocoricó' de manhã?",
   ["Galo", "Pato", "Peru", "Ganso"], "Galo",
   "O canto do galo, que em português imitamos como 'cocoricó', costuma ser ouvido ao amanhecer.",
   "Embrapa")
tf(C, "aves", 1, 6, "Todos os passarinhos nascem de ovos.", True,
   "Todas as aves botam ovos, e os filhotes se desenvolvem dentro deles até nascer.",
   "Enciclopédia Britannica – verbete 'Bird'")
mc(C, "animais", 1, 7, "Qual destes animais tem listras pretas e brancas?",
   ["Zebra", "Cavalo", "Burro", "Anta"], "Zebra",
   "A zebra é parente do cavalo e tem o corpo coberto de listras pretas e brancas.",
   "Enciclopédia Britannica – verbete 'Zebra'")
mc(C, "botânica", 1, 7, "Qual parte da planta fica embaixo da terra e absorve a água?",
   ["Raiz", "Caule", "Folha", "Flor"], "Raiz",
   "A raiz prende a planta ao solo e absorve água e sais minerais.",
   "Embrapa")
tf(C, "aves", 1, 9, "Os pinguins vivem no Polo Norte.", False,
   "Os pinguins vivem quase todos no Hemisfério Sul, e não há pinguins selvagens no Ártico.",
   "Enciclopédia Britannica – verbete 'Penguin'")
mc(C, "peixes", 2, 10, "Qual é o maior peixe do mundo?",
   ["Tubarão-baleia", "Tubarão-branco", "Pirarucu", "Peixe-lua"], "Tubarão-baleia",
   "O tubarão-baleia pode passar de doze metros de comprimento e se alimenta de plâncton.",
   "Enciclopédia Britannica – verbete 'Whale shark'")
mc(C, "animais", 2, 10, "Qual animal constrói represas nos rios usando galhos e troncos?",
   ["Castor", "Lontra", "Capivara", "Ariranha"], "Castor",
   "O castor corta árvores com os dentes e represa riachos para formar lagos onde faz sua toca.",
   "Enciclopédia Britannica – verbete 'Beaver'")
tf(C, "mamíferos", 2, 10, "O peixe-boi é um mamífero.", True,
   "Apesar do nome, o peixe-boi respira ar com pulmões e amamenta os filhotes.",
   "ICMBio – Centro Nacional de Pesquisa e Conservação de Mamíferos Aquáticos")
op(C, "alimentação", 2, 10,
   "Seres humanos, porcos e ursos comem tanto plantas quanto carne. Como são chamados os animais com esse tipo de alimentação?",
   "Onívoros", ["onívoros", "onívoro", "onivoros", "onivoro"],
   "Onívoros são os animais que se alimentam de vegetais e também de outros animais.",
   "Enciclopédia Britannica – verbete 'Omnivore'")
mc(C, "botânica", 2, 12, "Qual árvore nativa da Amazônia fornece o látex usado para fazer borracha natural?",
   ["Seringueira", "Carnaúba", "Jatobá", "Castanheira"], "Seringueira",
   "O látex extraído do tronco da seringueira é a matéria-prima da borracha natural.",
   "Embrapa", br=True)
mc(C, "mamíferos", 2, 9, "Qual animal brasileiro consegue se fechar completamente, como uma bola, para se proteger?",
   ["Tatu-bola", "Quati", "Gambá", "Paca"], "Tatu-bola",
   "O tatu-bola, da Caatinga e do Cerrado, encaixa a cabeça e o rabo na carapaça e vira uma bola dura.",
   "ICMBio", br=True)
mc(C, "botânica", 3, 12, "Depois da fecundação, qual parte da flor se transforma no fruto?",
   ["Ovário", "Pétala", "Sépala", "Antera"], "Ovário",
   "O ovário da flor se desenvolve e forma o fruto, enquanto os óvulos dentro dele viram sementes.",
   "Enciclopédia Britannica – verbete 'Fruit'")
mc(C, "mamíferos", 3, 12, "Qual destes animais brasileiros é um marsupial, que carrega os filhotes numa bolsa?",
   ["Gambá", "Tatu", "Quati", "Ouriço-cacheiro"], "Gambá",
   "O gambá, também chamado de saruê ou mucura, é um marsupial e tem uma bolsa onde os filhotes terminam de se desenvolver.",
   "ICMBio", br=True)
mc(C, "aves", 3, 12,
   "Qual ave brasileira, que desapareceu da natureza em 2000 e voltou a ser solta na Bahia em 2022, inspirou o personagem Blu do filme 'Rio'?",
   ["Ararinha-azul", "Arara-azul-grande", "Arara-canindé", "Papagaio-verdadeiro"], "Ararinha-azul",
   "A ararinha-azul sobreviveu apenas em cativeiro e foi reintroduzida em Curaçá, na Bahia, a partir de 2022.",
   "ICMBio", br=True)
mc(C, "ecologia", 3, 14, "Como se chama a relação em que duas espécies diferentes se ajudam, como as abelhas e as flores?",
   ["Mutualismo", "Parasitismo", "Predação", "Competição"], "Mutualismo",
   "No mutualismo as duas espécies ganham: a abelha obtém néctar e a flor é polinizada.",
   "Enciclopédia Britannica – verbete 'Mutualism'")
mc(C, "mamíferos", 4, 16, "Qual mamífero é considerado o de vida mais longa, podendo passar dos duzentos anos?",
   ["Baleia-da-groenlândia", "Elefante-asiático", "Orca", "Baleia-azul"], "Baleia-da-groenlândia",
   "Estudos com amostras dos olhos de baleias-da-groenlândia estimaram idades acima de duzentos anos.",
   "Enciclopédia Britannica – verbete 'Bowhead whale'")

# =========================================================== ASTRONOMIA
C = "ast"
tf(C, "estrelas", 1, 6, "As estrelas só existem durante a noite.", False,
   "As estrelas continuam no céu de dia, mas a luz forte do Sol impede que a gente as veja.",
   "NASA – Space Place")
tf(C, "Terra", 1, 6, "A Terra é plana.", False,
   "A Terra tem forma quase esférica, levemente achatada nos polos, como mostram as fotos tiradas do espaço.",
   "NASA")
mc(C, "planetas", 1, 6, "Qual destes é um planeta?",
   ["Marte", "Lua", "Sol", "Cometa"], "Marte",
   "Marte é o quarto planeta a partir do Sol; a Lua é um satélite e o Sol é uma estrela.",
   "NASA")
mc(C, "exploração espacial", 1, 6, "Como se chama a pessoa treinada para viajar ao espaço?",
   ["Astronauta", "Astrônomo", "Aviador", "Marinheiro"], "Astronauta",
   "O astronauta viaja ao espaço; o astrônomo é o cientista que estuda os astros.",
   "NASA")
mc(C, "Sol", 1, 7, "De qual lado do horizonte o Sol nasce, aproximadamente?",
   ["Leste", "Oeste", "Norte", "Sul"], "Leste",
   "Como a Terra gira de oeste para leste, o Sol parece surgir no lado leste e se pôr no oeste.",
   "NASA – Space Place")
mc(C, "Lua", 1, 8, "Como se chama a fase em que praticamente não conseguimos ver a Lua no céu?",
   ["Lua nova", "Lua cheia", "Quarto crescente", "Quarto minguante"], "Lua nova",
   "Na lua nova, a face iluminada pelo Sol fica voltada para o lado oposto ao da Terra.",
   "NASA")
mc(C, "planetas", 2, 12, "Qual planeta azul tem os ventos mais fortes já medidos no Sistema Solar?",
   ["Netuno", "Saturno", "Terra", "Mercúrio"], "Netuno",
   "Os ventos de Netuno passam de dois mil quilômetros por hora, mais rápidos que em qualquer outro planeta.",
   "NASA")
mc(C, "corpos celestes", 2, 10, "Qual corpo celeste feito de gelo e poeira forma uma cauda brilhante ao se aproximar do Sol?",
   ["Cometa", "Asteroide", "Meteoro", "Satélite"], "Cometa",
   "O calor do Sol faz o gelo do cometa virar gás, que forma a cabeleira e a cauda.",
   "NASA")
mc(C, "corpos celestes", 2, 10, "Como se chama o pedaço de rocha vindo do espaço que atravessa a atmosfera e chega até o chão?",
   ["Meteorito", "Meteoro", "Cometa", "Asteroide"], "Meteorito",
   "Meteoro é o risco de luz no céu; meteorito é o fragmento que sobrevive e cai na superfície.",
   "NASA")
mc(C, "astrônomos", 2, 12, "Qual astrônomo propôs, no século XVI, que a Terra gira em torno do Sol?",
   ["Nicolau Copérnico", "Ptolomeu", "Aristóteles", "Tycho Brahe"], "Nicolau Copérnico",
   "Copérnico publicou seu modelo com o Sol no centro em 1543, no livro 'Sobre as revoluções das esferas celestes'.",
   "Enciclopédia Britannica – verbete 'Nicolaus Copernicus'")
op(C, "astrônomos", 2, 12, "Qual cientista italiano apontou um telescópio para Júpiter, em 1610, e descobriu quatro de suas luas?",
   "Galileu Galilei", ["galileu galilei", "galileu", "galileo galilei", "galileo"],
   "Io, Europa, Ganimedes e Calisto são chamadas de luas galileanas em homenagem a ele.",
   "NASA")
mc(C, "exploração espacial", 2, 12, "Qual estação espacial é habitada sem interrupção, desde o ano 2000, por astronautas de vários países?",
   ["Estação Espacial Internacional", "Mir", "Skylab", "Tiangong"], "Estação Espacial Internacional",
   "A Estação Espacial Internacional recebe tripulações desde novembro de 2000.",
   "NASA")
tf(C, "planetas", 3, 14, "Vênus gira em torno de si mesmo no sentido contrário ao da maioria dos planetas.", True,
   "Vênus tem rotação retrógrada e muito lenta, de modo que em Vênus o Sol nasceria no oeste.",
   "NASA")
mc(C, "estrelas", 3, 14, "Como o Sol é chamado popularmente, de acordo com seu tipo de estrela?",
   ["Anã amarela", "Gigante vermelha", "Anã branca", "Supergigante azul"], "Anã amarela",
   "O Sol é uma estrela de tipo G da sequência principal, conhecida popularmente como anã amarela.",
   "NASA")
op(C, "planetas", 3, 12, "Qual é o sétimo planeta a partir do Sol, de cor azul-esverdeada?",
   "Urano", ["urano", "planeta urano"],
   "Urano tem essa cor por causa do gás metano em sua atmosfera, que absorve a luz vermelha.",
   "NASA")
mc(C, "exploração espacial", 3, 14, "Qual centro de lançamento de foguetes brasileiro fica no Maranhão?",
   ["Alcântara", "Barreira do Inferno", "Cabo Canaveral", "Baikonur"], "Alcântara",
   "O Centro de Lançamento de Alcântara fica perto da linha do Equador, o que economiza combustível nos lançamentos.",
   "Agência Espacial Brasileira", br=True)
mc(C, "Terra", 4, 16, "Como se chama o ponto da órbita da Terra em que ela fica mais perto do Sol?",
   ["Periélio", "Afélio", "Perigeu", "Apogeu"], "Periélio",
   "A Terra passa pelo periélio no começo de janeiro, a cerca de cento e quarenta e sete milhões de quilômetros do Sol.",
   "NASA")

# =========================================================== CORPO HUMANO
C = "cor"
mc(C, "sentidos", 1, 6, "Qual órgão dos sentidos usamos para ver as cores?",
   ["Olhos", "Orelhas", "Nariz", "Língua"], "Olhos",
   "Os olhos captam a luz, e o cérebro transforma esses sinais nas imagens e cores que vemos.",
   "Enciclopédia Britannica – verbete 'Eye'")
tf(C, "higiene", 1, 6, "Escovar os dentes ajuda a evitar cáries.", True,
   "A escovação remove restos de comida e a placa bacteriana que causam as cáries.",
   "Ministério da Saúde")
mc(C, "partes do corpo", 1, 7, "Qual parte do corpo liga a cabeça ao tronco?",
   ["Pescoço", "Ombro", "Cintura", "Quadril"], "Pescoço",
   "O pescoço sustenta a cabeça e por ele passam a coluna, a traqueia e o esôfago.",
   "Enciclopédia Britannica – verbete 'Neck'")
mc(C, "articulações", 1, 8, "Qual articulação dobra no meio do braço?",
   ["Cotovelo", "Joelho", "Tornozelo", "Ombro"], "Cotovelo",
   "O cotovelo liga o osso do braço aos ossos do antebraço e permite dobrar o braço.",
   "Enciclopédia Britannica – verbete 'Elbow'")
mc(C, "órgãos", 1, 8, "Qual órgão cobre todo o lado de fora do corpo e nos protege contra germes?",
   ["Pele", "Fígado", "Coração", "Estômago"], "Pele",
   "A pele é o maior órgão do corpo e funciona como barreira contra microrganismos.",
   "Enciclopédia Britannica – verbete 'Skin'")
op(C, "digestão", 1, 8, "Como se chama o líquido produzido na boca que começa a digestão dos alimentos?",
   "Saliva", ["saliva", "cuspe", "baba"],
   "A saliva umedece a comida e contém uma enzima que começa a digerir o amido.",
   "Enciclopédia Britannica – verbete 'Saliva'")
tf(C, "coração", 1, 9, "O coração bate mais rápido quando fazemos exercício físico.", True,
   "Durante o exercício os músculos precisam de mais oxigênio, e o coração acelera para bombear mais sangue.",
   "Ministério da Saúde")
mc(C, "digestão", 2, 10, "Por qual tubo a comida desce da boca até o estômago?",
   ["Esôfago", "Traqueia", "Laringe", "Uretra"], "Esôfago",
   "O esôfago leva o alimento da garganta ao estômago por meio de contrações musculares.",
   "Enciclopédia Britannica – verbete 'Esophagus'")
mc(C, "respiração", 2, 12, "Qual tubo leva o ar da garganta até os pulmões?",
   ["Traqueia", "Esôfago", "Aorta", "Uretra"], "Traqueia",
   "A traqueia é reforçada por anéis de cartilagem e se divide nos brônquios, que entram nos pulmões.",
   "Enciclopédia Britannica – verbete 'Trachea'")
mc(C, "vitaminas", 2, 12, "Qual vitamina, importante para a visão, o corpo produz a partir do betacaroteno da cenoura?",
   ["Vitamina A", "Vitamina C", "Vitamina D", "Vitamina K"], "Vitamina A",
   "O betacaroteno é convertido em vitamina A, essencial para enxergar com pouca luz.",
   "Ministério da Saúde")
mc(C, "nutrição", 2, 12, "Qual mineral, presente no feijão e na carne, ajuda a prevenir a anemia?",
   ["Ferro", "Sódio", "Iodo", "Flúor"], "Ferro",
   "O ferro é necessário para formar a hemoglobina, e a falta dele é a causa mais comum de anemia.",
   "Ministério da Saúde")
mc(C, "ossos", 3, 14, "Qual osso do rosto se move quando abrimos a boca para mastigar?",
   ["Mandíbula", "Maxila", "Osso hioide", "Osso zigomático"], "Mandíbula",
   "A mandíbula é o único osso do crânio que se articula de forma móvel; a maxila, de cima, fica fixa.",
   "Enciclopédia Britannica – verbete 'Mandible'")
tf(C, "respiração", 3, 12, "Os dois pulmões humanos têm exatamente o mesmo tamanho.", False,
   "O pulmão esquerdo é menor, com dois lobos em vez de três, porque divide espaço com o coração.",
   "Enciclopédia Britannica – verbete 'Lung'")
mc(C, "doenças", 3, 14, "Quais glândulas, que ficam perto das orelhas, incham na caxumba?",
   ["Parótidas", "Tireoide", "Suprarrenais", "Amígdalas"], "Parótidas",
   "A caxumba é uma infecção viral que inflama as parótidas, as maiores glândulas salivares.",
   "Ministério da Saúde")
mc(C, "sangue", 3, 14, "Como se chamam os vasos sanguíneos finíssimos onde o sangue troca gases com as células?",
   ["Capilares", "Artérias", "Veias", "Linfonodos"], "Capilares",
   "As paredes dos capilares têm uma só camada de células, o que permite a passagem de oxigênio e gás carbônico.",
   "Enciclopédia Britannica – verbete 'Capillary'")
op(C, "história da medicina", 3, 14, "Qual médico brasileiro descobriu, em 1909, a doença transmitida pelo inseto barbeiro?",
   "Carlos Chagas", ["carlos chagas", "chagas", "carlos justiniano chagas"],
   "Carlos Chagas descreveu o parasita, o inseto transmissor e a doença, que recebeu o seu nome.",
   "Fiocruz", br=True)
mc(C, "hormônios", 4, 16, "Qual hormônio, produzido pela glândula pineal quando escurece, ajuda a regular o sono?",
   ["Melatonina", "Adrenalina", "Insulina", "Cortisol"], "Melatonina",
   "A produção de melatonina aumenta no escuro e sinaliza ao corpo que é hora de dormir.",
   "Enciclopédia Britannica – verbete 'Melatonin'")

# =========================================================== TECNOLOGIA
C = "tec"
mc(C, "aparelhos", 1, 6, "Qual aparelho usamos para secar o cabelo depois do banho?",
   ["Secador", "Liquidificador", "Aspirador", "Ferro de passar"], "Secador",
   "O secador de cabelo sopra ar aquecido por uma resistência elétrica.",
   "Enciclopédia Britannica – verbete 'Hair dryer'")
tf(C, "aparelhos", 1, 6, "O controle remoto serve para mudar o canal da televisão sem precisar tocar nela.", True,
   "O controle envia sinais, geralmente de luz infravermelha invisível, que a televisão recebe.",
   "Enciclopédia Britannica – verbete 'Remote control'")
mc(C, "celulares", 1, 6, "O que devemos fazer quando a bateria do celular está acabando?",
   ["Colocar para carregar", "Colocar no congelador", "Sacudir o celular", "Molhar o celular"], "Colocar para carregar",
   "Ligar o celular ao carregador repõe a energia guardada na bateria.",
   "Enciclopédia Britannica – verbete 'Battery'")
mc(C, "computadores", 1, 7, "Qual parte do computador mostra as imagens e os textos?",
   ["Monitor", "Teclado", "Mouse", "Gabinete"], "Monitor",
   "O monitor é o dispositivo de saída que exibe na tela o que o computador está fazendo.",
   "Enciclopédia Britannica – verbete 'Computer'")
op(C, "celulares", 1, 8, "Como se chama um programa que instalamos no celular, como um jogo ou um mapa?",
   "Aplicativo", ["aplicativo", "aplicativos", "app", "apps", "aplicação"],
   "Aplicativo é um programa feito para uma tarefa específica no celular ou no computador.",
   "Enciclopédia Britannica – verbete 'Application'")
mc(C, "internet", 1, 9, "Qual site de vídeos, criado em 2005, tem um botão vermelho de 'play' no logotipo?",
   ["YouTube", "Netflix", "Instagram", "Twitter"], "YouTube",
   "O YouTube foi fundado em 2005 e comprado pelo Google em 2006.",
   "Enciclopédia Britannica – verbete 'YouTube'")
tf(C, "inteligência artificial", 1, 10, "A sigla IA significa inteligência artificial.", True,
   "Inteligência artificial é a área da computação que cria sistemas capazes de realizar tarefas que exigem raciocínio.",
   "Enciclopédia Britannica – verbete 'Artificial intelligence'")
mc(C, "celulares", 2, 10, "Qual é o sistema operacional usado nos iPhones?",
   ["iOS", "Android", "Windows", "Linux"], "iOS",
   "O iOS é desenvolvido pela Apple e roda apenas nos seus aparelhos.",
   "Apple")
mc(C, "computadores", 2, 10, "Qual tecla do teclado apaga a letra que está à esquerda do cursor?",
   ["Backspace", "Enter", "Shift", "Tab"], "Backspace",
   "A tecla Backspace volta uma posição e apaga o caractere anterior ao cursor.",
   "Enciclopédia Britannica – verbete 'Computer keyboard'")
mc(C, "invenções", 2, 12, "Qual invenção de Johannes Gutenberg, por volta de 1450, revolucionou a produção de livros?",
   ["Prensa de tipos móveis", "Máquina de escrever", "Papel", "Caneta-tinteiro"], "Prensa de tipos móveis",
   "A prensa de Gutenberg permitiu imprimir muitas cópias de um livro de forma rápida e barata.",
   "Enciclopédia Britannica – verbete 'Johannes Gutenberg'")
mc(C, "computação", 2, 12, "Como se chama o sistema de numeração de base dois, usado pelos computadores?",
   ["Binário", "Decimal", "Hexadecimal", "Romano"], "Binário",
   "No sistema binário só existem os algarismos zero e um, que representam os estados dos circuitos.",
   "Enciclopédia Britannica – verbete 'Binary number system'")
mc(C, "inventores", 3, 14,
   "Qual inventor escocês aperfeiçoou a máquina a vapor no século XVIII e deu nome à unidade de potência?",
   ["James Watt", "Thomas Newcomen", "Alessandro Volta", "André-Marie Ampère"], "James Watt",
   "Watt criou o condensador separado, que tornou a máquina a vapor muito mais eficiente, e a unidade watt homenageia seu nome.",
   "Enciclopédia Britannica – verbete 'James Watt'")
mc(C, "Brasil", 3, 14,
   "Qual satélite, lançado em 2021, foi o primeiro de observação da Terra totalmente projetado, montado e operado pelo Brasil?",
   ["Amazonia-1", "CBERS-4", "SCD-1", "SGDC-1"], "Amazonia-1",
   "O Amazonia-1, desenvolvido pelo INPE, foi lançado em fevereiro de 2021 e fotografa o território brasileiro para monitorar o desmatamento.",
   "INPE", br=True)
op(C, "segurança digital", 3, 14,
   "Como se chama o golpe em que criminosos enviam mensagens falsas, imitando bancos ou lojas, para roubar senhas?",
   "Phishing", ["phishing", "fishing", "pishing", "phising"],
   "O nome vem da ideia de 'pescar' dados das vítimas com iscas, como links e e-mails falsos.",
   "CERT.br – Cartilha de Segurança para Internet", br=False)
tf(C, "internet", 3, 14, "O primeiro e-mail foi enviado antes da criação da World Wide Web.", True,
   "Ray Tomlinson enviou e-mail entre computadores da rede ARPANET em 1971, e a Web só surgiu em 1989.",
   "Enciclopédia Britannica – verbete 'E-mail'")
mc(C, "inventores", 4, 16, "Qual inventor escocês fez a primeira demonstração pública de televisão, em Londres, em 1926?",
   ["John Logie Baird", "Guglielmo Marconi", "Nikola Tesla", "Thomas Edison"], "John Logie Baird",
   "Baird mostrou imagens em movimento transmitidas por seu sistema mecânico de televisão em janeiro de 1926.",
   "Enciclopédia Britannica – verbete 'John Logie Baird'")
mc(C, "computação", 4, 16, "Qual empresa lançou o 4004, o primeiro microprocessador comercial, em 1971?",
   ["Intel", "IBM", "AMD", "Texas Instruments"], "Intel",
   "O Intel 4004 reunia toda a unidade de processamento num único chip.",
   "Enciclopédia Britannica – verbete 'Intel Corporation'")

# =========================================================== MATEMÁTICA
C = "mat"
op(C, "aritmética", 1, 6, "Quanto é quatro mais quatro?", "8", ["8", "oito"],
   "Quatro mais quatro é igual a oito.", "Aritmética básica")
mc(C, "problemas", 1, 6, "Pedro tinha cinco carrinhos e ganhou mais dois. Quantos carrinhos ele tem agora?",
   ["7", "6", "8", "3"], "7",
   "Cinco mais dois é igual a sete.", "Aritmética básica")
mc(C, "números", 1, 7, "Qual destes números é o maior?",
   ["98", "89", "97", "79"], "98",
   "Noventa e oito tem nove dezenas e oito unidades, mais que todos os outros.", "Aritmética básica")
tf(C, "números", 1, 7, "O número quinze é par.", False,
   "Quinze termina em cinco e não pode ser dividido em duas partes inteiras iguais, por isso é ímpar.",
   "Aritmética básica")
mc(C, "horas", 1, 8, "Uma aula começa às oito horas e dura duas horas. A que horas ela termina?",
   ["Às dez horas", "Às nove horas", "Às onze horas", "Às seis horas"], "Às dez horas",
   "Oito horas mais duas horas dá dez horas.", "Aritmética básica")
mc(C, "dinheiro", 1, 9, "Quem paga uma compra de trinta e cinco reais com uma nota de cinquenta recebe quanto de troco?",
   ["15 reais", "25 reais", "20 reais", "10 reais"], "15 reais",
   "Cinquenta menos trinta e cinco é igual a quinze.", "Aritmética básica")
mc(C, "sequências", 1, 9, "Qual é o próximo número da sequência três, seis, nove, doze?",
   ["15", "14", "16", "18"], "15",
   "A sequência aumenta de três em três, então depois do doze vem o quinze.", "Aritmética básica")
mc(C, "frações", 2, 10, "Quanto é um terço de trinta?",
   ["10", "3", "15", "9"], "10",
   "Dividindo trinta em três partes iguais, cada parte vale dez.", "Aritmética básica")
mc(C, "medidas", 2, 10, "Quantos meses há em dois anos e meio?",
   ["30", "25", "24", "36"], "30",
   "Dois anos têm vinte e quatro meses e meio ano tem seis, totalizando trinta.", "Aritmética básica")
mc(C, "frações", 2, 12, "Quanto é dois quintos mais um quinto?",
   ["Três quintos", "Três décimos", "Dois quintos", "Um terço"], "Três quintos",
   "Frações com o mesmo denominador se somam pelos numeradores: dois mais um dá três quintos.",
   "Aritmética básica")
mc(C, "porcentagem", 2, 12, "Numa turma de vinte alunos, cinco usam óculos. Que porcentagem da turma usa óculos?",
   ["Vinte e cinco por cento", "Cinco por cento", "Vinte por cento", "Quinze por cento"], "Vinte e cinco por cento",
   "Cinco de vinte é um quarto da turma, ou seja, vinte e cinco por cento.", "Aritmética básica")
mc(C, "geometria", 2, 12, "Como se chama o triângulo que tem os três lados com a mesma medida?",
   ["Equilátero", "Isósceles", "Escaleno", "Retângulo"], "Equilátero",
   "No triângulo equilátero os três lados e os três ângulos são iguais, cada ângulo com sessenta graus.",
   "Enciclopédia Britannica – verbete 'Equilateral triangle'")
tf(C, "geometria", 3, 12, "Todo quadrado também é um retângulo.", True,
   "Retângulo é todo quadrilátero com quatro ângulos retos, e o quadrado cumpre essa condição.",
   "Enciclopédia Britannica – verbete 'Square'")
mc(C, "geometria", 3, 12, "Quando um relógio de ponteiros marca três horas em ponto, qual é o ângulo entre os ponteiros?",
   ["90 graus", "45 graus", "120 graus", "180 graus"], "90 graus",
   "O mostrador tem trezentos e sessenta graus divididos em doze horas, trinta graus cada; três horas dão noventa graus.",
   "Geometria básica")
mc(C, "múltiplos", 3, 12, "Qual é o mínimo múltiplo comum entre quatro e seis?",
   ["12", "24", "10", "2"], "12",
   "Doze é o menor número que é múltiplo de quatro e de seis ao mesmo tempo.", "Aritmética básica")
mc(C, "medidas", 3, 14, "Quantos metros quadrados tem um hectare?",
   ["10.000", "1.000", "100.000", "100"], "10.000",
   "Um hectare equivale a um quadrado de cem metros de lado, ou seja, dez mil metros quadrados.",
   "Inmetro – Sistema Internacional de Unidades")
op(C, "lógica", 4, 14,
   "Se três gatos pegam três ratos em três minutos, quantos gatos, no mesmo ritmo, pegam cem ratos em cem minutos?",
   "3", ["3", "três", "tres", "3 gatos", "três gatos", "tres gatos"],
   "Cada gato pega um rato a cada três minutos; em cem minutos os mesmos três gatos pegam cem ratos.",
   "Raciocínio lógico")
