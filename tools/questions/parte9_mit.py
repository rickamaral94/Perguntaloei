# Perguntas novas: mitologia e lendas. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "mit"

# ------------------------------------------------------------------ FÁCEIS
mc(T, "criaturas fantásticas", 1, 6, "Segundo as lendas, qual tempero de cheiro forte espanta os vampiros?",
   ["Alho", "Canela", "Açúcar", "Orégano"], "Alho",
   "Nas lendas do Leste Europeu, réstias de alho penduradas nas portas protegiam as casas dos vampiros.",
   "Enciclopédia Britannica – verbete 'Vampire'")
mc(T, "folclore brasileiro", 1, 6, "Na cantiga de ninar 'Nana, neném', quem vem pegar a criança que não dorme?",
   ["Cuca", "Iara", "Sereia", "Fada"], "Cuca",
   "A cantiga diz 'Nana, neném, que a Cuca vem pegar', e a Cuca é um dos bichos-papões mais antigos do Brasil.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "criaturas fantásticas", 1, 6, "Qual ser das histórias é um homenzinho de barba branca e gorro pontudo que vive debaixo da terra ou nos jardins?",
   ["Gnomo", "Gigante", "Centauro", "Ciclope"], "Gnomo",
   "Nas lendas europeias, os gnomos são pequenos guardiões da terra, das pedras e dos tesouros escondidos.",
   "Enciclopédia Britannica – verbete 'Gnome'")
tf(T, "criaturas fantásticas", 1, 6, "Os dragões existiram de verdade e viveram junto com os dinossauros.", False,
   "Os dragões são seres imaginários das lendas; os dinossauros, sim, existiram e deixaram fósseis.",
   "Enciclopédia Britannica – verbete 'Dragon'")
mc(T, "folclore brasileiro", 1, 6, "Qual destes seres faz parte do folclore brasileiro?",
   ["Curupira", "Leprechaun", "Troll", "Grifo"], "Curupira",
   "O Curupira é o protetor das matas brasileiras; os outros vêm de lendas da Irlanda, da Escandinávia e da Grécia antiga.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "folclore brasileiro", 1, 7, "Segundo a lenda, onde se pode capturar o Saci jogando uma peneira?",
   ["Num redemoinho de vento", "Numa poça de lama", "Num formigueiro", "Numa fogueira"], "Num redemoinho de vento",
   "Diz a tradição que o Saci viaja dentro dos redemoinhos, e quem joga uma peneira sobre eles consegue prendê-lo.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "folclore brasileiro", 1, 8, "Segundo a lenda, que travessura o Saci faz com a crina dos cavalos à noite?",
   ["Faz tranças", "Pinta de azul", "Corta bem curta", "Enche de lama"], "Faz tranças",
   "Contam que, de manhã, os cavalos aparecem com a crina toda trançada, sinal de que o Saci passou por ali.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "folclore brasileiro", 1, 7, "Segundo a lenda, a Iara atrai os pescadores com o seu canto.", True,
   "A Iara canta à beira dos rios, e quem se encanta com a sua voz é levado para o fundo das águas.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "folclore brasileiro", 1, 8, "Segundo a lenda amazônica, o que o boto usa na cabeça para esconder o furo por onde respira?",
   ["Um chapéu", "Uma coroa", "Um capacete", "Uma peruca"], "Um chapéu",
   "Quando vira rapaz para ir às festas, o boto usa um chapéu, quase sempre branco, para disfarçar o furo no alto da cabeça.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "contos de fadas", 1, 6, "Na história 'João e o Pé de Feijão', quem mora no castelo lá no alto, acima das nuvens?",
   ["Um gigante", "Um dragão", "Uma sereia", "Um unicórnio"], "Um gigante",
   "João sobe pelo pé de feijão, chega ao castelo de um gigante e foge levando a galinha dos ovos de ouro.",
   "Enciclopédia Britannica – verbete 'Jack and the Beanstalk'")
mc(T, "mil e uma noites", 1, 8, "Nas 'Mil e Uma Noites', qual jovem encontra uma lâmpada mágica com um gênio dentro?",
   ["Aladim", "Simbad", "Ali Babá", "Sherazade"], "Aladim",
   "O gênio aparece quando Aladim esfrega a lâmpada para limpá-la.",
   "Enciclopédia Britannica – verbete 'Aladdin'")
tf(T, "mil e uma noites", 1, 8, "Na história de Ali Babá, a senha para abrir a caverna dos ladrões era 'Abracadabra'.", False,
   "A senha era 'Abre-te, Sésamo', e sésamo é o nome do gergelim.",
   "Enciclopédia Britannica – verbete 'Ali Baba'")
op(T, "deuses e planetas", 1, 9, "Qual planeta tem o nome da deusa romana do amor e da beleza?", "Vênus",
   ["vênus", "venus", "planeta vênus"],
   "Vênus é a deusa romana que corresponde à Afrodite dos gregos, e o planeta é o mais brilhante no céu depois da Lua.",
   "NASA – 'Venus'")
mc(T, "mitologia chinesa", 1, 9, "Qual criatura lendária, símbolo de poder e boa sorte, aparece em danças nas ruas no Ano-Novo chinês?",
   ["Dragão", "Unicórnio", "Grifo", "Sereia"], "Dragão",
   "Na dança do dragão, várias pessoas carregam um longo dragão de pano em varas, fazendo-o ondular pelas ruas.",
   "Enciclopédia Britannica – verbete 'Chinese New Year'")
tf(T, "mitologia grega", 1, 9, "Na mitologia grega, Hércules era filho de Poseidon, o deus dos mares.", False,
   "Hércules, chamado Héracles pelos gregos, era filho de Zeus com a mortal Alcmena.",
   "Enciclopédia Britannica – verbete 'Heracles'")
mc(T, "mitologia chinesa", 1, 9, "Qual cor enfeita as festas do Ano-Novo chinês, porque espantaria o azar e o monstro Nian?",
   ["Vermelho", "Preto", "Branco", "Roxo"], "Vermelho",
   "Segundo a lenda, o monstro Nian tinha medo da cor vermelha e do barulho, por isso há lanternas vermelhas e fogos.",
   "Enciclopédia Britannica – verbete 'Chinese New Year'")
mc(T, "mitologia grega", 1, 10, "Qual herói grego, ainda bebê, estrangulou duas serpentes que entraram no seu berço?",
   ["Hércules", "Perseu", "Teseu", "Jasão"], "Hércules",
   "As serpentes foram mandadas pela deusa Hera, e a façanha mostrou desde cedo a força do herói.",
   "Enciclopédia Britannica – verbete 'Heracles'")
mc(T, "orixás", 1, 10, "Em 2 de fevereiro, uma grande festa no bairro do Rio Vermelho, em Salvador, leva presentes ao mar para qual orixá?",
   ["Iemanjá", "Xangô", "Ogum", "Oxóssi"], "Iemanjá",
   "Na festa, barcos levam flores, perfumes e espelhos para a rainha do mar.",
   "IPHAN – Festa de Iemanjá", br=True)
mc(T, "mitologia chinesa", 1, 9, "Segundo uma lenda chinesa, qual animal vive na Lua, ao lado da deusa Chang'e?",
   ["Um coelho", "Um gato", "Um cavalo", "Um sapo"], "Um coelho",
   "O coelho de jade da Lua prepara o elixir da imortalidade, e a lenda é lembrada na Festa do Meio do Outono.",
   "Enciclopédia Britannica – verbete 'Mid-Autumn Festival'")
op(T, "criaturas fantásticas", 1, 10, "Qual criatura enorme e peluda viveria nas florestas da América do Norte, deixando pegadas gigantes?", "Pé-Grande",
   ["pé-grande", "pé grande", "bigfoot", "sasquatch"],
   "Apesar de muitas fotos e relatos, nunca se encontrou prova científica de que o Pé-Grande exista.",
   "Enciclopédia Britannica – verbete 'Sasquatch'")
mc(T, "mitologia grega", 1, 10, "Em qual guerra lutou o herói grego Aquiles?",
   ["Guerra de Troia", "Guerra dos Cem Anos", "Guerras Púnicas", "Guerra do Peloponeso"], "Guerra de Troia",
   "Aquiles foi o maior guerreiro dos gregos no cerco à cidade de Troia, contado na 'Ilíada', de Homero.",
   "Enciclopédia Britannica – verbete 'Achilles'")
mc(T, "lendas medievais", 1, 10, "Nas lendas do rei Artur, como se chama a mesa onde os cavaleiros se sentavam sem que nenhum ficasse num lugar de honra?",
   ["Távola Redonda", "Mesa Dourada", "Altar de Pedra", "Trono de Ferro"], "Távola Redonda",
   "Por ser redonda, a mesa não tinha cabeceira, e todos os cavaleiros ficavam em pé de igualdade.",
   "Enciclopédia Britannica – verbete 'Round Table'")
op(T, "mitologia grega", 1, 10, "Qual é a capital da Grécia, cujo nome homenageia a deusa da sabedoria?", "Atenas",
   ["atenas"],
   "Segundo o mito, a deusa Atena venceu Poseidon na disputa pela cidade ao oferecer uma oliveira.",
   "Enciclopédia Britannica – verbete 'Athena'")
mc(T, "mitologia grega", 1, 10, "Qual objeto o herói Perseu usou como espelho para não olhar diretamente para a Medusa?",
   ["Um escudo", "Uma espada", "Um capacete", "Uma taça"], "Um escudo",
   "Olhando apenas o reflexo no escudo polido, Perseu não virou pedra e conseguiu se aproximar da Medusa.",
   "Enciclopédia Britannica – verbete 'Perseus'")
mc(T, "mitologia grega", 1, 10, "Os Jogos Olímpicos da Grécia antiga eram realizados em homenagem a qual deus?",
   ["Zeus", "Hades", "Dionísio", "Hefesto"], "Zeus",
   "Os jogos aconteciam no santuário de Olímpia, onde havia um grande templo e uma estátua de Zeus.",
   "Comitê Olímpico Internacional – 'Ancient Olympic Games'")
tf(T, "criaturas fantásticas", 1, 10, "O unicórnio é o animal nacional da Escócia.", True,
   "O unicórnio aparece no brasão real escocês há séculos e é considerado o animal nacional da Escócia.",
   "VisitScotland – 'Scotland's national animal: the unicorn'")
tf(T, "mitologia romana", 1, 10, "O mês de março recebeu esse nome por causa de Marte, o deus romano da guerra.", True,
   "No antigo calendário romano, março era o primeiro mês do ano e homenageava Marte.",
   "Enciclopédia Britannica – verbete 'March'")

# ------------------------------------------------------------------ MÉDIAS
mc(T, "mitologia grega", 2, 12, "Qual monstro de muitas cabeças, que nasciam de novo quando eram cortadas, foi enfrentado por Hércules?",
   ["Hidra", "Quimera", "Esfinge", "Górgona"], "Hidra",
   "Para vencer a Hidra de Lerna, Hércules contou com o sobrinho Iolau, que queimava cada pescoço cortado.",
   "Enciclopédia Britannica – verbete 'Hydra'")
op(T, "mitologia grega", 2, 12, "Na mitologia grega, qual era o nome do pai de Ícaro, que construiu as asas para os dois fugirem de Creta?", "Dédalo",
   ["dédalo", "dedalo"],
   "Dédalo era um inventor genial e também construiu o labirinto do Minotauro.",
   "Enciclopédia Britannica – verbete 'Daedalus'")
mc(T, "mitologia grega", 2, 12, "Na 'Odisseia', qual é o nome da esposa de Ulisses, que esperou por ele durante 20 anos?",
   ["Penélope", "Helena", "Andrômeda", "Medeia"], "Penélope",
   "Para enganar os pretendentes, Penélope tecia uma mortalha de dia e a desmanchava à noite.",
   "Enciclopédia Britannica – verbete 'Penelope'")
mc(T, "orixás", 2, 12, "Qual orixá é a senhora das águas doces, dos rios e das cachoeiras?",
   ["Oxum", "Iansã", "Nanã", "Obá"], "Oxum",
   "Oxum é ligada ao amor, à fertilidade e ao ouro, e costuma ser representada com um espelho e roupas amarelas.",
   "Pierre Verger – Orixás", br=True)
mc(T, "mitologia japonesa", 2, 12, "Segundo um conto japonês, de qual fruta nasceu o menino Momotaro, que derrotou os ogros?",
   ["Pêssego", "Melancia", "Maçã", "Laranja"], "Pêssego",
   "'Momo' quer dizer pêssego em japonês, e Momotaro parte para a aventura com um cão, um macaco e um faisão.",
   "Enciclopédia Britannica – verbete 'Momotarō'")
tf(T, "mitologia grega", 2, 12, "Na 'Odisseia', Ulisses manda tapar com cera os ouvidos dos marinheiros para que não ouçam o canto das sereias.", True,
   "Ulisses quis ouvir o canto, então pediu que o amarrassem ao mastro enquanto os marinheiros remavam sem escutar nada.",
   "Enciclopédia Britannica – verbete 'Siren'")
mc(T, "mitologia chinesa", 2, 12, "Qual destes animais NÃO faz parte do zodíaco chinês?",
   ["Gato", "Macaco", "Galo", "Cachorro"], "Gato",
   "Uma lenda conta que o rato não acordou o gato no dia da grande corrida, e por isso o gato ficou de fora.",
   "Enciclopédia Britannica – verbete 'Chinese zodiac'")
op(T, "mitologia chinesa", 2, 12, "Qual é o último dos 12 animais do zodíaco chinês?", "Porco",
   ["porco", "javali", "o porco"],
   "A ordem começa com o rato e termina com o porco, que chegou por último na corrida da lenda.",
   "Enciclopédia Britannica – verbete 'Chinese zodiac'")
mc(T, "mitologia indígena", 2, 12, "Na língua tupi, qual astro é chamado de Guaraci?",
   ["Sol", "Lua", "Estrela-d'alva", "Cometa"], "Sol",
   "Nas narrativas tupis, Guaraci, o Sol, e Jaci, a Lua, são vistos como grandes forças da natureza.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "lendas medievais", 2, 12, "Em qual floresta da Inglaterra viveria Robin Hood com o seu bando?",
   ["Sherwood", "Floresta Negra", "Brocéliande", "Amazônia"], "Sherwood",
   "A floresta de Sherwood fica perto de Nottingham, cidade do xerife que perseguia Robin Hood.",
   "Enciclopédia Britannica – verbete 'Robin Hood'")
mc(T, "mitologia grega", 2, 12, "Segundo o mito, o que ficou no fundo da caixa de Pandora depois que ela a fechou?",
   ["A esperança", "A tristeza", "O medo", "A preguiça"], "A esperança",
   "Os males escaparam para o mundo, mas a esperança permaneceu guardada dentro do jarro, que depois virou 'caixa' nas versões modernas.",
   "Enciclopédia Britannica – verbete 'Pandora'")
mc(T, "orixás", 2, 12, "Qual orixá guerreiro é ligado ao ferro, às ferramentas e aos caminhos?",
   ["Ogum", "Oxalá", "Oxum", "Iemanjá"], "Ogum",
   "No Brasil, Ogum é muitas vezes associado a São Jorge, especialmente no Rio de Janeiro.",
   "Pierre Verger – Orixás", br=True)
mc(T, "orixás", 2, 12, "Qual orixá é a senhora dos ventos e das tempestades?",
   ["Iansã", "Oxum", "Nanã", "Iemanjá"], "Iansã",
   "Iansã, também chamada Oyá, é uma guerreira e costuma ser associada a Santa Bárbara.",
   "Pierre Verger – Orixás", br=True)
tf(T, "orixás", 2, 12, "Na tradição dos orixás, Oxóssi é o senhor dos mares.", False,
   "Oxóssi é o caçador das matas, de arco e flecha; o mar pertence a Iemanjá.",
   "Pierre Verger – Orixás", br=True)
tf(T, "lendas e mistérios", 2, 10, "Cientistas já comprovaram que o Monstro do Lago Ness existe.", False,
   "Muitas buscas com sonar e até um estudo do DNA da água do lago, em 2018, não encontraram nenhum sinal do monstro.",
   "Enciclopédia Britannica – verbete 'Loch Ness monster'")
mc(T, "mitologia grega", 2, 12, "Qual deus grego dos pastores tinha pernas de bode e tocava uma flauta?",
   ["Pã", "Apolo", "Hermes", "Dionísio"], "Pã",
   "O grito de Pã assustava os viajantes, e daí vem a palavra 'pânico'.",
   "Enciclopédia Britannica – verbete 'Pan'")
op(T, "mitologia grega", 2, 12, "Qual ninfa grega foi castigada a apenas repetir as últimas palavras que ouvia?", "Eco",
   ["eco", "a ninfa eco"],
   "Apaixonada por Narciso, Eco foi definhando até restar só a sua voz, que dá nome ao som que volta para nós.",
   "Enciclopédia Britannica – verbete 'Echo'")
mc(T, "mitologia romana", 2, 12, "Qual deus romano do fogo e dos ferreiros deu origem à palavra 'vulcão'?",
   ["Vulcano", "Netuno", "Mercúrio", "Saturno"], "Vulcano",
   "Vulcano corresponde ao Hefesto grego, e os romanos imaginavam sua forja debaixo das montanhas que soltam fogo.",
   "Enciclopédia Britannica – verbete 'Vulcan'")
mc(T, "lendas indígenas", 2, 12, "O nome do rio Amazonas vem de mulheres guerreiras de qual mitologia?",
   ["Grega", "Nórdica", "Egípcia", "Asteca"], "Grega",
   "O explorador espanhol Francisco de Orellana disse ter lutado contra mulheres guerreiras e as comparou às amazonas dos mitos gregos.",
   "Enciclopédia Britannica – verbete 'Amazon River'", br=True)
mc(T, "mitologia chinesa", 2, 12, "Diferente dos dragões das lendas europeias, o dragão chinês costuma estar ligado a quê?",
   ["À água e à chuva", "Às cavernas de tesouro", "Ao gelo e à neve", "À areia do deserto"], "À água e à chuva",
   "Na China, o dragão é um ser bondoso que vive nos rios e mares e controla as chuvas.",
   "Enciclopédia Britannica – verbete 'Long (Chinese mythology)'")
tf(T, "mitologia nórdica", 2, 14, "Na mitologia nórdica, Odin tinha dois corvos que voavam pelo mundo e lhe contavam tudo o que viam.", True,
   "Os corvos se chamavam Hugin e Munin, nomes ligados ao pensamento e à memória.",
   "Enciclopédia Britannica – verbete 'Odin'")
tf(T, "folclore brasileiro", 2, 12, "Segundo a lenda, a Mula sem cabeça é uma mulher castigada por namorar um padre.", True,
   "Na versão mais conhecida, ela se transforma na mula nas noites de quinta para sexta-feira.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "criaturas fantásticas", 2, 12, "Qual monstro gigante das lendas dos marinheiros nórdicos tinha tentáculos e afundava navios?", "Kraken",
   ["kraken", "cráquen", "craken"],
   "A lenda do Kraken pode ter nascido de avistamentos de lulas-gigantes, que existem de verdade.",
   "Enciclopédia Britannica – verbete 'Kraken'")

# ------------------------------------------------------------------ DIFÍCEIS
tf(T, "mitologia grega", 3, 14, "Segundo o mito grego, o cavalo alado Pégaso nasceu do sangue da Medusa quando Perseu cortou a cabeça dela.", True,
   "Junto com Pégaso, nasceu também o gigante Crisaor, ambos filhos de Medusa com Poseidon.",
   "Enciclopédia Britannica – verbete 'Pegasus'")
mc(T, "mitologia nórdica", 3, 14, "Na mitologia nórdica, quais animais puxam a carruagem do deus Thor?",
   ["Dois bodes", "Dois lobos", "Dois gatos", "Dois ursos"], "Dois bodes",
   "Os bodes de Thor podiam ser cozidos para o jantar e voltavam à vida no dia seguinte, quando ele erguia o martelo sobre os ossos.",
   "Enciclopédia Britannica – verbete 'Thor'")
mc(T, "mitologia grega", 3, 14, "Qual músico grego perdeu a amada Eurídice para sempre porque olhou para trás ao sair do mundo dos mortos?",
   ["Orfeu", "Apolo", "Narciso", "Adônis"], "Orfeu",
   "Com sua lira, Orfeu encantou Hades, que deixou Eurídice partir se ele não olhasse para ela antes de chegar à luz.",
   "Enciclopédia Britannica – verbete 'Orpheus'")
mc(T, "mitologia hindu", 3, 14, "Na mitologia hindu, qual deus em forma de macaco ajudou o príncipe Rama a resgatar a esposa Sita?",
   ["Hanuman", "Ganesha", "Krishna", "Garuda"], "Hanuman",
   "Hanuman é um dos heróis do épico 'Ramayana' e é admirado pela força, pela coragem e pela lealdade.",
   "Enciclopédia Britannica – verbete 'Hanuman'")
mc(T, "mitologia africana", 3, 14, "Nos contos dos povos da África Ocidental, que animal é o esperto Anansi, dono de todas as histórias?",
   ["Aranha", "Tartaruga", "Lebre", "Hiena"], "Aranha",
   "Os contos de Anansi nasceram entre os povos acãs, de Gana, e viajaram para o Caribe com os africanos escravizados.",
   "Enciclopédia Britannica – verbete 'Anansi'")
tf(T, "lendas e mistérios", 3, 14, "Desaparecem muito mais navios e aviões no Triângulo das Bermudas do que em outras áreas movimentadas do oceano.", False,
   "Segundo a agência americana NOAA, não há provas de que ali ocorram mais desaparecimentos do que em outras regiões de tráfego intenso.",
   "NOAA – 'What is the Bermuda Triangle?'")
tf(T, "mitologia nórdica", 3, 14, "Na mitologia nórdica antiga, Loki é irmão de Thor.", False,
   "Loki é filho de gigantes e, nos mitos, aparece como irmão de sangue de Odin; a ideia de irmão de Thor vem dos quadrinhos.",
   "Enciclopédia Britannica – verbete 'Loki'")
mc(T, "lendas indígenas", 3, 14, "Qual é o outro nome da Cobra Grande, serpente gigante das lendas amazônicas?",
   ["Boiuna", "Matinta Perera", "Mapinguari", "Caipora"], "Boiuna",
   "Diz a lenda que a Boiuna vira os barcos, e que seus olhos brilhando à noite parecem as luzes de um navio.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "folclore brasileiro", 3, 14, "Qual personagem das lendas do Norte é uma velha que vira pássaro e assobia à noite perto das casas?",
   ["Matinta Perera", "Cuca", "Iara", "Pisadeira"], "Matinta Perera",
   "Quem ouve o assobio promete fumo ou café, e no dia seguinte uma velha aparece para buscar o presente.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "folclore brasileiro", 3, 14, "Segundo o folclore, qual figura pisa no peito de quem vai dormir de barriga cheia?",
   ["Pisadeira", "Cuca", "Comadre Fulozinha", "Mãe-d'água"], "Pisadeira",
   "A Pisadeira é uma velha magra de unhas compridas que vive nos telhados, lenda comum em Minas Gerais e São Paulo.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "lendas indígenas", 3, 14, "Segundo a crença amazônica, ouvir o canto de qual pássaro traz sorte?",
   ["Uirapuru", "Sabiá", "Bem-te-vi", "Tucano"], "Uirapuru",
   "O canto do uirapuru é tão bonito e raro que, dizem, os outros pássaros se calam para ouvi-lo.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "orixás", 3, 14, "Qual orixá, ligado à criação e à paz, é homenageado com roupas brancas?",
   ["Oxalá", "Ogum", "Xangô", "Oxóssi"], "Oxalá",
   "Na Bahia, Oxalá é associado ao Senhor do Bonfim, e muitos fiéis se vestem de branco às sextas-feiras.",
   "Pierre Verger – Orixás", br=True)

# ------------------------------------------------------------------ MUITO DIFÍCEIS
mc(T, "mitologia nórdica", 4, 16, "Na mitologia nórdica, como se chama o cavalo de oito patas do deus Odin?",
   ["Sleipnir", "Fenrir", "Bifrost", "Mjölnir"], "Sleipnir",
   "Sleipnir era o mais veloz dos cavalos e, segundo os mitos, filho de Loki.",
   "Enciclopédia Britannica – verbete 'Sleipnir'")
mc(T, "mitologia grega", 4, 16, "Qual centauro sábio foi o professor de heróis gregos como Aquiles e Jasão?",
   ["Quíron", "Nesso", "Folo", "Eurítion"], "Quíron",
   "Ao contrário dos centauros selvagens, Quíron era gentil e ensinava medicina, música e caça.",
   "Enciclopédia Britannica – verbete 'Chiron'")
mc(T, "mitologia celta", 4, 16, "De qual antiga festa celta, que marcava o fim das colheitas e o começo do inverno, se originou o Halloween?",
   ["Samhain", "Beltane", "Yule", "Ostara"], "Samhain",
   "Os celtas acreditavam que, no Samhain, a fronteira entre o mundo dos vivos e o dos mortos ficava mais fina.",
   "Enciclopédia Britannica – verbete 'Samhain'")
mc(T, "lendas indígenas", 4, 16, "Na lenda da vitória-régia, como se chama a jovem indígena que se transformou na planta?",
   ["Naiá", "Mani", "Iracema", "Moema"], "Naiá",
   "Naiá caiu no rio ao tentar alcançar o reflexo da Lua, e Jaci a transformou na 'estrela das águas'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "lendas indígenas", 4, 16, "Como se chama o amuleto de pedra verde, muitas vezes em forma de sapo, ligado à lenda das guerreiras icamiabas?",
   ["Muiraquitã", "Maracá", "Cocar", "Tacape"], "Muiraquitã",
   "Segundo a lenda, as icamiabas davam o muiraquitã de presente aos homens que as visitavam uma vez por ano.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "mitologia egípcia", 4, 16, "Qual deus egípcio da escrita e da sabedoria era representado com cabeça de íbis?",
   ["Tot", "Sobek", "Ptá", "Set"], "Tot",
   "Os egípcios atribuíam a Tot a invenção dos hieróglifos, e os escribas o tinham como protetor.",
   "Enciclopédia Britannica – verbete 'Thoth'")
