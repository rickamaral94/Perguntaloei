# Perguntas novas: artes. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "art"

# ================================================================ FÁCEIS
op(T, "cores e tintas", 1, 6, "Que cor obtemos ao misturar tinta preta com tinta branca?", "Cinza",
   ["cinza", "cinzento", "cinzenta"],
   "Quanto mais branco na mistura, mais claro fica o cinza; quanto mais preto, mais escuro.",
   "Enciclopédia Britannica – verbete 'color'")
tf(T, "cores e tintas", 1, 7, "Para deixar uma tinta mais clara, o pintor mistura nela um pouco de tinta preta.", False,
   "Para clarear uma cor, mistura-se branco; o preto deixa a tinta mais escura.",
   "Enciclopédia Britannica – verbete 'color'")
mc(T, "cores e tintas", 1, 7, "Qual cor de tinta, misturada a outra, deixa essa cor mais escura?",
   ["Preto", "Branco", "Amarelo", "Rosa"], "Preto",
   "Um pouquinho de preto escurece qualquer cor; o branco faz o contrário e clareia.",
   "Enciclopédia Britannica – verbete 'color'")
tf(T, "cores e tintas", 1, 8, "Na pintura tradicional, o verde é uma das cores primárias.", False,
   "O verde é uma cor secundária: nasce da mistura de duas primárias, o azul e o amarelo.",
   "Enciclopédia Britannica – verbete 'color wheel'")
op(T, "cores e tintas", 1, 9, "Quantas são as cores secundárias na pintura tradicional?", "3",
   ["3", "três", "tres"],
   "São o verde, o laranja e o roxo, cada uma feita com duas cores primárias.",
   "Enciclopédia Britannica – verbete 'color wheel'")
mc(T, "materiais", 1, 6, "Que material macio e colorido as crianças apertam e moldam com as mãos para fazer bonequinhos?",
   ["Massinha", "Giz de cera", "Lápis de cor", "Papel crepom"], "Massinha",
   "A massinha pode ser moldada muitas vezes e é ótima para treinar escultura desde pequeno.",
   "Enciclopédia Britannica – verbete 'modeling clay'")
mc(T, "materiais", 1, 6, "Na aula de artes, que objeto usamos para recortar papel?",
   ["Tesoura", "Régua", "Borracha", "Apontador"], "Tesoura",
   "A tesoura escolar tem ponta arredondada para as crianças recortarem com segurança.",
   "Enciclopédia Britannica – verbete 'scissors'")
mc(T, "materiais", 1, 6, "Qual destes materiais usamos para colorir um desenho?",
   ["Lápis de cor", "Régua", "Cola", "Apontador"], "Lápis de cor",
   "O lápis de cor tem uma mina feita de pigmento com cera, que deixa a cor no papel.",
   "Enciclopédia Britannica – verbete 'pencil'")
tf(T, "materiais", 1, 8, "Depois de ir ao forno bem quente, a argila fica dura e vira cerâmica.", True,
   "O calor do forno transforma a argila de vez, e ela não volta a amolecer com água.",
   "Enciclopédia Britannica – verbete 'pottery'")
mc(T, "materiais", 1, 9, "Como se chama a placa onde o pintor coloca e mistura as tintas enquanto pinta?",
   ["Paleta", "Moldura", "Tela", "Espátula"], "Paleta",
   "A paleta costuma ter um furo para o pintor encaixar o polegar e segurá-la com uma das mãos.",
   "Enciclopédia Britannica – verbete 'palette'")
mc(T, "fotografia", 1, 9, "Qual suporte de três pés o fotógrafo usa para deixar a câmera bem parada?",
   ["Tripé", "Pincel", "Paleta", "Cinzel"], "Tripé",
   "Com a câmera firme no tripé, as fotos não saem tremidas, mesmo com pouca luz.",
   "Enciclopédia Britannica – verbete 'tripod'")
mc(T, "tipos de pintura", 1, 8, "Como se chama o quadro que mostra montanhas, rios, árvores e o céu de um lugar?",
   ["Paisagem", "Retrato", "Natureza-morta", "Caricatura"], "Paisagem",
   "A paisagem retrata a natureza ou uma cidade vista de longe.",
   "Enciclopédia Britannica – verbete 'landscape painting'")
mc(T, "tipos de pintura", 1, 8, "Como se chama a pintura feita para mostrar o rosto e a aparência de uma pessoa?",
   ["Retrato", "Paisagem", "Natureza-morta", "Mosaico"], "Retrato",
   "Antes da fotografia, quem queria guardar a própria imagem precisava encomendar um retrato a um pintor.",
   "Enciclopédia Britannica – verbete 'portraiture'")
mc(T, "museus", 1, 7, "Como se chama o lugar onde ficam expostas obras de arte para o público visitar?",
   ["Museu", "Biblioteca", "Cartório", "Ginásio"], "Museu",
   "Os museus guardam, estudam e mostram ao público obras de arte e objetos importantes.",
   "Conselho Internacional de Museus (ICOM) – definição de museu")
mc(T, "dança", 1, 6, "Como se chama a moça que dança balé?",
   ["Bailarina", "Maestrina", "Ginasta", "Cantora"], "Bailarina",
   "Quem dança balé é chamado de bailarino ou bailarina.",
   "Enciclopédia Britannica – verbete 'ballet'")
op(T, "teatro", 1, 7, "Que boneco de teatro a gente veste na mão, como uma luva, para fazê-lo falar e mexer?", "Fantoche",
   ["fantoche", "fantoches", "boneco de luva"],
   "O fantoche é movido pelos dedos do artista, que fica escondido atrás de uma pequena tenda ou cortina.",
   "Enciclopédia Britannica – verbete 'puppetry'")
tf(T, "teatro", 1, 7, "As duas máscaras símbolo do teatro mostram um rosto alegre e um rosto triste.", True,
   "O rosto alegre representa a comédia e o triste, a tragédia, os dois gêneros do teatro grego antigo.",
   "Enciclopédia Britannica – verbete 'mask'")
mc(T, "teatro", 1, 6, "No fim de um espetáculo, o que o público costuma fazer para mostrar que gostou?",
   ["Bater palmas", "Apagar as luzes", "Subir no palco", "Fechar a cortina"], "Bater palmas",
   "Os aplausos são o agradecimento da plateia, e os artistas voltam ao palco para se curvar.",
   "Enciclopédia Britannica – verbete 'theatre'")
mc(T, "teatro", 1, 7, "Como se chama a parte do teatro onde o público fica sentado assistindo?",
   ["Plateia", "Palco", "Camarim", "Bastidores"], "Plateia",
   "A plateia fica de frente para o palco, onde os atores se apresentam.",
   "Enciclopédia Britannica – verbete 'theatre'")
mc(T, "teatro", 1, 7, "Como se chama o grande pano que se abre no começo de um espetáculo e se fecha no final?",
   ["Cortina", "Bandeira", "Toalha", "Tapete"], "Cortina",
   "A cortina do palco também esconde a troca de cenários entre um ato e outro.",
   "Enciclopédia Britannica – verbete 'theatre'")
mc(T, "teatro", 1, 8, "Como se chama o treino que os atores fazem várias vezes antes da estreia de uma peça?",
   ["Ensaio", "Intervalo", "Bilheteria", "Aplauso"], "Ensaio",
   "Nos ensaios, os atores decoram as falas e combinam os movimentos no palco.",
   "Enciclopédia Britannica – verbete 'theatre'")
mc(T, "teatro", 1, 7, "Numa peça de teatro, como se chama o artista que interpreta um personagem?",
   ["Ator", "Cenógrafo", "Bilheteiro", "Porteiro"], "Ator",
   "O ator dá voz, corpo e emoção ao personagem diante da plateia.",
   "Enciclopédia Britannica – verbete 'acting'")
mc(T, "monumentos", 1, 9, "No alto de qual morro do Rio de Janeiro fica o Cristo Redentor?",
   ["Corcovado", "Pão de Açúcar", "Morro da Urca", "Dois Irmãos"], "Corcovado",
   "A estátua fica a cerca de 700 metros de altitude, no Parque Nacional da Tijuca.",
   "Santuário Cristo Redentor – história", br=True)
mc(T, "obras famosas", 1, 9, "Qual pintura famosa mostra uma mulher de sorriso misterioso, com as mãos cruzadas à frente do corpo?",
   ["Mona Lisa", "O Grito", "Abaporu", "A Noite Estrelada"], "Mona Lisa",
   "Leonardo da Vinci pintou a Mona Lisa no começo do século XVI, e o sorriso dela é discutido até hoje.",
   "Museu do Louvre – 'Portrait de Lisa Gherardini, dite Mona Lisa'")
mc(T, "obras famosas", 1, 10, "Qual quadro famoso mostra uma figura com as mãos no rosto e a boca aberta, diante de um céu alaranjado?",
   ["O Grito", "Mona Lisa", "A Noite Estrelada", "Abaporu"], "O Grito",
   "Edvard Munch fez várias versões de 'O Grito', em pintura e em gravura.",
   "Enciclopédia Britannica – verbete 'The Scream'")
mc(T, "pintores", 1, 10, "Qual pintor holandês ficou famoso pelos quadros de girassóis amarelos num vaso?",
   ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci"], "Vincent van Gogh",
   "Van Gogh pintou a série 'Girassóis' em Arles, na França, para decorar o quarto de um amigo pintor.",
   "Museu Van Gogh – 'Sunflowers'")
mc(T, "pintores", 1, 10, "Qual artista pernambucano ficou famoso no mundo com quadros de cores vibrantes e contornos pretos, cheios de corações e gatos?",
   ["Romero Britto", "Vik Muniz", "Alfredo Volpi", "Candido Portinari"], "Romero Britto",
   "Nascido no Recife, Romero Britto fez carreira em Miami, onde suas obras de estilo pop ficaram muito conhecidas.",
   "Enciclopédia Itaú Cultural – verbete 'Romero Britto'", br=True)

# ================================================================ MÉDIAS
mc(T, "arquitetura", 2, 12, "Em qual cidade fica a catedral de Oscar Niemeyer cujas colunas curvas parecem mãos voltadas para o céu?",
   ["Brasília", "Rio de Janeiro", "São Paulo", "Belo Horizonte"], "Brasília",
   "A Catedral Metropolitana de Brasília tem 16 colunas de concreto curvas e foi inaugurada em 1970.",
   "IPHAN – Catedral Metropolitana de Brasília", br=True)
tf(T, "arquitetura", 2, 12, "Oscar Niemeyer ficou famoso por prédios só de linhas retas, evitando as curvas.", False,
   "Ao contrário: Niemeyer dizia que o que o atraía era a curva livre e sensual, como as das montanhas e dos rios.",
   "Fundação Oscar Niemeyer", br=True)
mc(T, "obras famosas", 2, 12, "Qual pintora brasileira pintou 'Operários' (1933), quadro com dezenas de rostos de trabalhadores diante das chaminés de fábricas?",
   ["Tarsila do Amaral", "Anita Malfatti", "Lygia Clark", "Djanira"], "Tarsila do Amaral",
   "Pintado depois de uma viagem à União Soviética, o quadro mostra a mistura de povos que trabalhavam na indústria de São Paulo.",
   "Acervo Artístico-Cultural dos Palácios do Governo de São Paulo – 'Operários'", br=True)
mc(T, "obras famosas", 2, 12, "Qual pintor brasileiro pintou 'O Lavrador de Café', que mostra um trabalhador de pés e mãos enormes segurando uma enxada?",
   ["Candido Portinari", "Di Cavalcanti", "Alfredo Volpi", "Romero Britto"], "Candido Portinari",
   "Portinari cresceu numa fazenda de café em Brodowski (SP), e o quadro de 1934 está no MASP.",
   "MASP – 'O Lavrador de Café'", br=True)
mc(T, "movimentos artísticos", 2, 12, "Qual período artístico, entre os séculos XIV e XVI, valorizou o ser humano e a arte da Grécia e da Roma antigas?",
   ["Renascimento", "Barroco", "Impressionismo", "Cubismo"], "Renascimento",
   "Leonardo da Vinci, Michelangelo e Rafael são os nomes mais famosos desse período.",
   "Enciclopédia Britannica – verbete 'Renaissance'")
mc(T, "pintores", 2, 12, "Qual destes pintores cortou parte da própria orelha, em 1888?",
   ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci"], "Vincent van Gogh",
   "Van Gogh se feriu em Arles, na França, depois de uma briga com o amigo Paul Gauguin, e depois pintou autorretratos com a orelha enfaixada.",
   "Museu Van Gogh – 'Van Gogh's ear'")
tf(T, "pintores", 2, 12, "Leonardo da Vinci, além de pintor, desenhou projetos de máquinas voadoras.", True,
   "Seus cadernos têm desenhos de máquinas com asas inspiradas nos pássaros e nos morcegos.",
   "Enciclopédia Britannica – verbete 'Leonardo da Vinci'")
mc(T, "movimentos artísticos", 2, 12, "Qual movimento artístico, do qual Salvador Dalí fez parte, pintava cenas estranhas e parecidas com sonhos?",
   ["Surrealismo", "Impressionismo", "Renascimento", "Barroco"], "Surrealismo",
   "O Surrealismo surgiu em Paris nos anos 1920 e se inspirava no inconsciente e no mundo dos sonhos.",
   "Enciclopédia Britannica – verbete 'Surrealism'")
tf(T, "museus", 2, 10, "A pirâmide de vidro na entrada do Museu do Louvre foi construída pelos antigos egípcios.", False,
   "A pirâmide é moderna: foi projetada pelo arquiteto I. M. Pei e inaugurada em 1989.",
   "Museu do Louvre – 'La Pyramide'")
tf(T, "pintores", 2, 12, "A pintora Frida Kahlo nasceu na Espanha.", False,
   "Frida nasceu em 1907 em Coyoacán, na Cidade do México, na Casa Azul que hoje é um museu.",
   "Museo Frida Kahlo – Casa Azul")
tf(T, "obras famosas", 2, 10, "A 'Mona Lisa' é uma pintura enorme, que ocupa uma parede inteira do museu.", False,
   "O quadro é pequeno, com cerca de 77 por 53 centímetros, e fica protegido por um vidro no Louvre.",
   "Museu do Louvre – 'Portrait de Lisa Gherardini, dite Mona Lisa'")
mc(T, "técnicas", 2, 12, "Com que tipo de tinta, que demora bastante para secar, foi pintada a 'Mona Lisa'?",
   ["Tinta a óleo", "Aquarela", "Tinta spray", "Giz pastel"], "Tinta a óleo",
   "A tinta a óleo seca devagar e permitiu a Leonardo fazer passagens suaves entre luz e sombra.",
   "Museu do Louvre – 'Portrait de Lisa Gherardini, dite Mona Lisa'")
op(T, "dança", 2, 10, "Como se chama a saia curta e armada que as bailarinas usam no balé clássico?", "Tutu",
   ["tutu", "tutus"],
   "O tutu é feito de várias camadas de tule, um tecido leve que deixa as pernas livres para os passos.",
   "Enciclopédia Britannica – verbete 'tutu'")
mc(T, "dança", 2, 10, "Qual dança, nascida na região de Buenos Aires e Montevidéu, é dançada em par ao som do bandoneón?",
   ["Tango", "Salsa", "Valsa", "Flamenco"], "Tango",
   "O tango é Patrimônio Cultural Imaterial da Humanidade, reconhecido pela UNESCO em 2009.",
   "UNESCO – 'Tango'")
op(T, "teatro", 2, 10, "Como se chama a salinha do teatro onde os atores se maquiam e trocam de roupa?", "Camarim",
   ["camarim", "camarins"],
   "O camarim fica nos bastidores, longe da vista da plateia.",
   "Enciclopédia Britannica – verbete 'theatre'")
mc(T, "teatro", 2, 12, "Que nome se dá à pessoa que escreve peças de teatro?",
   ["Dramaturgo", "Cenógrafo", "Figurinista", "Iluminador"], "Dramaturgo",
   "Shakespeare, Nelson Rodrigues e Ariano Suassuna são dramaturgos famosos.",
   "Enciclopédia Britannica – verbete 'dramatic literature'")
mc(T, "arquitetura", 2, 10, "Como se chamam as janelas feitas de pedaços de vidro colorido, comuns nas igrejas antigas?",
   ["Vitrais", "Azulejos", "Afrescos", "Tapeçarias"], "Vitrais",
   "Os pedaços de vidro são presos por tiras de chumbo e formam desenhos que brilham com a luz do sol.",
   "Enciclopédia Britannica – verbete 'stained glass'")
op(T, "escultura", 2, 10, "Qual ferramenta de metal o escultor bate com o martelo para tirar lascas da pedra?", "Cinzel",
   ["cinzel", "cinzéis", "talhadeira"],
   "Com o cinzel e o martelo, o escultor vai tirando pedaços do bloco até a figura aparecer.",
   "Enciclopédia Britannica – verbete 'sculpture'")
op(T, "arquitetura", 2, 12, "Qual famosa catedral gótica de Paris teve o telhado e o pináculo destruídos por um incêndio em 2019?", "Notre-Dame",
   ["notre-dame", "notre dame", "catedral de notre-dame", "nossa senhora de paris"],
   "Depois de cinco anos de restauração, a catedral foi reaberta em dezembro de 2024.",
   "Enciclopédia Britannica – verbete 'Notre-Dame de Paris'")
tf(T, "modernismo", 2, 12, "A Semana de Arte Moderna aconteceu no ano em que a Independência do Brasil completou cem anos.", True,
   "A Semana foi em fevereiro de 1922, ano do centenário da Independência, de 1822.",
   "Enciclopédia Itaú Cultural – verbete 'Semana de Arte Moderna'", br=True)
mc(T, "museus", 2, 10, "Em qual cidade fica o MASP, museu de arte cujo prédio é sustentado por quatro grandes pilares vermelhos?",
   ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"], "São Paulo",
   "O MASP fica na Avenida Paulista, e debaixo do prédio há uma grande praça aberta ao público.",
   "MASP – Museu de Arte de São Paulo Assis Chateaubriand", br=True)
mc(T, "carnaval", 2, 10, "Como se chamam os enormes carros enfeitados que desfilam nas escolas de samba contando o enredo?",
   ["Carros alegóricos", "Trios elétricos", "Carros de som", "Bonecos gigantes"], "Carros alegóricos",
   "Os carros alegóricos são esculturas gigantes feitas por artistas nos barracões das escolas de samba.",
   "Liesa – Liga Independente das Escolas de Samba do Rio de Janeiro", br=True)
mc(T, "arte de rua", 2, 12, "Qual dupla de irmãos paulistanos ficou famosa no mundo todo com grafites de personagens de pele amarela?",
   ["Os Gêmeos", "Eduardo Kobra", "Banksy", "Jean-Michel Basquiat"], "Os Gêmeos",
   "Os irmãos gêmeos Otávio e Gustavo Pandolfo começaram a grafitar no bairro do Cambuci, em São Paulo, nos anos 1980.",
   "Enciclopédia Itaú Cultural – verbete 'Osgemeos'", br=True)

# ================================================================ DIFÍCEIS
mc(T, "obras famosas", 3, 14, "O nome do quadro 'Abaporu', de Tarsila do Amaral, vem de qual língua?",
   ["Tupi", "Latim", "Grego", "Iorubá"], "Tupi",
   "Em tupi, 'abaporu' quer dizer 'homem que come gente', ideia que inspirou o Manifesto Antropófago.",
   "MALBA – 'Abaporu'", br=True)
mc(T, "modernismo", 3, 14, "Qual pintor carioca, um dos idealizadores da Semana de Arte Moderna de 1922, ficou famoso por retratar mulheres, sambistas e o morro?",
   ["Di Cavalcanti", "Candido Portinari", "Alfredo Volpi", "Almeida Júnior"], "Di Cavalcanti",
   "Emiliano Di Cavalcanti também desenhou o catálogo e o cartaz da Semana de 1922.",
   "Enciclopédia Itaú Cultural – verbete 'Di Cavalcanti'", br=True)
mc(T, "movimentos artísticos", 3, 14, "A Igreja de São Francisco, em Salvador, toda coberta de ouro por dentro, é um exemplo de qual estilo artístico?",
   ["Barroco", "Gótico", "Modernismo", "Cubismo"], "Barroco",
   "O Barroco chegou ao Brasil com os portugueses e se espalhou pelas igrejas, com talhas douradas e muito movimento.",
   "IPHAN – Igreja e Convento de São Francisco (Salvador)", br=True)
mc(T, "movimentos artísticos", 3, 14, "Qual pintor espanhol criou o Cubismo junto com o francês Georges Braque?",
   ["Pablo Picasso", "Salvador Dalí", "Diego Velázquez", "Francisco de Goya"], "Pablo Picasso",
   "Picasso e Braque trabalharam lado a lado em Paris, a partir de 1907, desmontando as figuras em formas geométricas.",
   "Enciclopédia Britannica – verbete 'Cubism'")
mc(T, "museus", 3, 14, "Em qual cidade italiana fica a Galeria Uffizi, onde está 'O Nascimento de Vênus', de Botticelli?",
   ["Florença", "Roma", "Veneza", "Milão"], "Florença",
   "O prédio da Uffizi foi construído no século XVI para abrigar escritórios do governo dos Médici.",
   "Gallerie degli Uffizi")
mc(T, "escultura", 3, 14, "Qual artista renascentista esculpiu a 'Pietà', que mostra Maria com Jesus nos braços, na Basílica de São Pedro?",
   ["Michelangelo", "Donatello", "Bernini", "Rafael"], "Michelangelo",
   "Michelangelo terminou a Pietà com pouco mais de 20 anos, e é a única obra que ele assinou.",
   "Enciclopédia Britannica – verbete 'Pietà'")
mc(T, "arquitetura", 3, 14, "Qual estilo das catedrais da Idade Média tem arcos pontudos, torres altas e grandes vitrais?",
   ["Gótico", "Barroco", "Neoclássico", "Modernista"], "Gótico",
   "Os arcos pontudos permitiram paredes mais altas e finas, abrindo espaço para janelas enormes.",
   "Enciclopédia Britannica – verbete 'Gothic architecture'")
tf(T, "técnicas", 3, 14, "Na xilogravura, as partes da madeira que o artista escava ficam sem tinta e aparecem brancas no papel.", True,
   "A tinta só pega nas partes que ficaram altas na madeira, e são elas que marcam o papel.",
   "Enciclopédia Britannica – verbete 'woodcut'")
tf(T, "dança", 3, 14, "Muitos passos do balé clássico têm nomes em francês, como 'plié' e 'pas de deux'.", True,
   "O balé se desenvolveu na corte francesa, e Luís XIV criou em 1661 a Academia Real de Dança.",
   "Enciclopédia Britannica – verbete 'ballet'")
mc(T, "pintores", 3, 14, "Qual pintor paraibano pintou 'Independência ou Morte!', que mostra Dom Pedro I às margens do Ipiranga?",
   ["Pedro Américo", "Victor Meirelles", "Almeida Júnior", "Di Cavalcanti"], "Pedro Américo",
   "O enorme quadro, de 1888, fica no Museu do Ipiranga, em São Paulo.",
   "Museu Paulista da USP – 'Independência ou Morte!'", br=True)
mc(T, "teatro", 3, 14, "Qual personagem da comédia italiana antiga usa uma roupa colorida de losangos?",
   ["Arlequim", "Pierrô", "Colombina", "Polichinelo"], "Arlequim",
   "O Arlequim é um criado esperto e brincalhão da commedia dell'arte, teatro popular italiano.",
   "Enciclopédia Britannica – verbete 'Harlequin'")
mc(T, "arte de rua", 3, 14, "Qual grafiteiro paulistano pintou 'Etnias', mural gigante com rostos de povos nativos, para a Olimpíada do Rio em 2016?",
   ["Eduardo Kobra", "Vik Muniz", "Romero Britto", "Hélio Oiticica"], "Eduardo Kobra",
   "O mural, no Boulevard Olímpico, entrou para o Guinness como o maior grafite do mundo na época.",
   "Guinness World Records – 'Largest spray paint mural'", br=True)

# ================================================================ MUITO DIFÍCEIS
mc(T, "pintores", 4, 16, "Qual pintor francês chegou ao Brasil com a Missão Artística Francesa de 1816 e retratou o dia a dia do Rio de Janeiro?",
   ["Jean-Baptiste Debret", "Claude Monet", "Eugène Delacroix", "Paul Cézanne"], "Jean-Baptiste Debret",
   "Suas aquarelas foram reunidas no livro 'Viagem Pitoresca e Histórica ao Brasil'.",
   "Enciclopédia Itaú Cultural – verbete 'Jean-Baptiste Debret'", br=True)
mc(T, "paisagismo", 4, 16, "Qual paisagista brasileiro projetou os jardins do Aterro do Flamengo, no Rio de Janeiro?",
   ["Roberto Burle Marx", "Oscar Niemeyer", "Lúcio Costa", "Lina Bo Bardi"], "Roberto Burle Marx",
   "Burle Marx usava plantas nativas brasileiras e também desenhou o calçadão da Avenida Atlântica, em Copacabana.",
   "Sítio Roberto Burle Marx – IPHAN", br=True)
mc(T, "técnicas", 4, 16, "Qual mestre pernambucano da xilogravura, de Bezerros, ilustrou centenas de folhetos de cordel?",
   ["J. Borges", "Mestre Vitalino", "Ariano Suassuna", "Patativa do Assaré"], "J. Borges",
   "José Francisco Borges começou vendendo folhetos e virou um dos gravadores brasileiros mais conhecidos no exterior.",
   "Enciclopédia Itaú Cultural – verbete 'J. Borges'", br=True)
tf(T, "fotografia", 4, 16, "O francês Hercule Florence, que vivia em Campinas, fez experiências com fotografia nos anos 1830 e já usava a palavra 'photographie'.", True,
   "Florence chegou a resultados por conta própria, ao mesmo tempo que os pioneiros europeus, como mostrou o pesquisador Boris Kossoy.",
   "Boris Kossoy – 'Hercule Florence: a descoberta isolada da fotografia no Brasil'", br=True)
mc(T, "modernismo", 4, 16, "Qual destes quadros foi pintado por Anita Malfatti?",
   ["O Homem Amarelo", "Abaporu", "Operários", "O Lavrador de Café"], "O Homem Amarelo",
   "Mário de Andrade gostou tanto do quadro que o comprou, e hoje ele faz parte da coleção do escritor no IEB-USP.",
   "Instituto de Estudos Brasileiros (IEB-USP) – Coleção Mário de Andrade", br=True)
mc(T, "pintores", 4, 16, "Qual pintor paulista pintou 'Caipira Picando Fumo' (1893)?",
   ["Almeida Júnior", "Pedro Américo", "Victor Meirelles", "Di Cavalcanti"], "Almeida Júnior",
   "Natural de Itu, Almeida Júnior ficou conhecido por retratar o homem do interior paulista; o quadro está na Pinacoteca.",
   "Pinacoteca de São Paulo – 'Caipira Picando Fumo'", br=True)
