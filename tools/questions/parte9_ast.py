# Perguntas novas: astronomia. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "ast"

# =========================================================== FÁCEIS (6–8 anos)
tf(T, "Lua", 1, 6, "A Lua gira em volta da Terra.", True,
   "A Lua leva cerca de 27 dias para dar uma volta completa em torno da Terra.",
   "NASA – Moon: Facts")
tf(T, "Sol", 1, 6, "Olhar diretamente para o Sol pode machucar os olhos.", True,
   "A luz do Sol é tão forte que pode lesionar a retina; nunca se deve olhar para ele sem proteção adequada.",
   "NASA – Eye Safety During a Total Solar Eclipse")
tf(T, "Lua", 1, 6, "A Lua é maior do que a Terra.", False,
   "A Lua tem cerca de um quarto do diâmetro da Terra.",
   "NASA – Moon: Facts")
mc(T, "astronautas", 1, 6, "O que o astronauta usa na cabeça, com um visor, para se proteger no espaço?",
   ["Capacete", "Boné", "Chapéu", "Óculos de sol"], "Capacete",
   "O capacete faz parte do traje espacial e protege a cabeça, mantendo o ar para respirar.",
   "NASA – What Is a Spacesuit?")
mc(T, "dia e noite", 1, 6, "Como se chama o momento em que o Sol desaparece no horizonte no fim da tarde?",
   ["Pôr do sol", "Nascer do sol", "Meio-dia", "Madrugada"], "Pôr do sol",
   "No pôr do sol, a rotação da Terra faz o Sol sumir no horizonte, do lado oeste.",
   "Enciclopédia Britannica – verbete 'Sunset'")
op(T, "Lua", 1, 7, "Qual é o astro mais brilhante do céu à noite?", "Lua", ["lua", "a lua"],
   "A Lua cheia brilha muito mais do que qualquer estrela ou planeta, refletindo a luz do Sol.",
   "NASA – Moon: Facts")
mc(T, "dia e noite", 1, 7, "Em que parte do dia o Sol fica mais alto no céu?",
   ["Meio-dia", "Amanhecer", "Fim da tarde", "Meia-noite"], "Meio-dia",
   "Por volta do meio-dia o Sol atinge sua maior altura no céu, e as sombras ficam mais curtas.",
   "Enciclopédia Britannica – verbete 'Noon'")
mc(T, "fases da Lua", 1, 8, "Como se chama a fase em que a Lua aparece pela metade e vai ficando maior a cada noite?",
   ["Quarto crescente", "Quarto minguante", "Lua cheia", "Lua nova"], "Quarto crescente",
   "Depois da lua nova vem o quarto crescente, e a parte iluminada aumenta até a lua cheia.",
   "NASA – Moon Phases")
op(T, "Sistema Solar", 1, 8, "Como se chama o conjunto formado pelo Sol e pelos planetas que giram em volta dele?",
   "Sistema Solar", ["sistema solar", "o sistema solar"],
   "O Sistema Solar inclui o Sol, os oito planetas, suas luas, planetas anões, asteroides e cometas.",
   "NASA – Our Solar System")
mc(T, "gravidade", 1, 8, "Por que as pessoas que moram do outro lado da Terra não caem no espaço?",
   ["A gravidade puxa tudo para a Terra", "Elas usam sapatos especiais", "O vento as segura no chão",
    "Elas ficam presas por cordas"], "A gravidade puxa tudo para a Terra",
   "A gravidade puxa tudo em direção ao centro da Terra, por isso ninguém 'cai' do planeta.",
   "NASA Space Place – What Is Gravity?")

# =========================================================== FÁCEIS (9–12 anos)
tf(T, "Sistema Solar", 1, 9, "O Sol gira em volta da Terra.", False,
   "É a Terra que gira em volta do Sol; o Sol parece se mover no céu por causa da rotação da Terra.",
   "NASA – Earth: Facts")
mc(T, "planetas", 1, 9, "Qual planeta fica entre Vênus e Marte?",
   ["Terra", "Júpiter", "Mercúrio", "Saturno"], "Terra",
   "A Terra é o terceiro planeta a partir do Sol, depois de Mercúrio e Vênus.",
   "NASA – Our Solar System")
mc(T, "estações do ano", 1, 9, "Em qual estação do ano os dias costumam ser mais longos?",
   ["Verão", "Inverno", "Outono", "Primavera"], "Verão",
   "No verão, o hemisfério está mais voltado para o Sol, e o Sol fica mais tempo acima do horizonte.",
   "Enciclopédia Britannica – verbete 'Season'")
mc(T, "ciência", 1, 9, "Como se chama o cientista que estuda as estrelas, os planetas e as galáxias?",
   ["Astrônomo", "Astrólogo", "Geólogo", "Meteorologista"], "Astrônomo",
   "A astronomia é uma ciência; já a astrologia não tem base científica.",
   "Enciclopédia Britannica – verbete 'Astronomy'")
op(T, "Lua", 1, 9, "Como se chamam os buracos redondos na superfície da Lua, formados pelo choque de rochas vindas do espaço?",
   "Crateras", ["crateras", "cratera"],
   "Como a Lua quase não tem atmosfera nem erosão, suas crateras ficam preservadas por bilhões de anos.",
   "NASA – Moon: Facts")
mc(T, "lugares", 1, 9, "Como se chama o lugar com uma cúpula onde se projeta o céu estrelado para o público?",
   ["Planetário", "Aquário", "Observatório meteorológico", "Museu de cera"], "Planetário",
   "No planetário, um projetor mostra estrelas e planetas no teto em forma de cúpula.",
   "Enciclopédia Britannica – verbete 'Planetarium'")
mc(T, "satélites", 1, 9, "Qual destes foi feito pelo ser humano e gira em volta da Terra?",
   ["Satélite artificial", "Lua", "Cometa", "Meteoro"], "Satélite artificial",
   "Satélites artificiais são lançados por foguetes e servem para comunicação, GPS e previsão do tempo.",
   "NASA – What Is a Satellite?")
mc(T, "satélites", 1, 10, "Para que servem os satélites meteorológicos?",
   ["Ajudar na previsão do tempo", "Transmitir rádio para carros", "Levar astronautas à Lua",
    "Medir terremotos no fundo do mar"], "Ajudar na previsão do tempo",
   "Eles fotografam as nuvens e medem a temperatura da atmosfera, ajudando a prever chuvas e tempestades.",
   "INPE – Centro de Previsão de Tempo e Estudos Climáticos")
mc(T, "sondas", 1, 10, "Qual destes robôs andou explorando o chão de Marte?",
   ["Curiosity", "Hubble", "Sputnik", "Voyager 1"], "Curiosity",
   "O jipe-robô Curiosity pousou em Marte em 2012 para estudar se o planeta já teve condições para a vida.",
   "NASA – Mars Science Laboratory: Curiosity Rover")
mc(T, "Lua", 1, 10, "Qual astro é o principal responsável pelas marés dos oceanos?",
   ["Lua", "Sol", "Marte", "Vênus"], "Lua",
   "A gravidade da Lua puxa a água dos oceanos, formando as marés altas e baixas; o Sol tem efeito menor.",
   "NOAA – What Causes Tides?")
mc(T, "astronautas", 1, 10, "Como se chama a atividade em que o astronauta sai da nave e flutua no espaço, preso por cabos?",
   ["Caminhada espacial", "Reentrada", "Decolagem", "Acoplagem"], "Caminhada espacial",
   "Nas caminhadas espaciais, os astronautas consertam equipamentos fora da nave usando trajes especiais.",
   "NASA – What Is a Spacewalk?")
mc(T, "corrida espacial", 1, 10, "Qual país foi o primeiro a levar seres humanos à Lua?",
   ["Estados Unidos", "Rússia", "China", "Japão"], "Estados Unidos",
   "As missões Apollo, da NASA, levaram 12 astronautas a caminhar na Lua entre 1969 e 1972.",
   "NASA – Apollo Program")
mc(T, "Lua", 1, 10, "De que cor é o céu visto da Lua, mesmo durante o dia?",
   ["Preto", "Azul", "Laranja", "Branco"], "Preto",
   "Sem atmosfera para espalhar a luz do Sol, o céu da Lua fica escuro mesmo com o Sol brilhando.",
   "NASA – Moon: Facts")
mc(T, "corrida espacial", 1, 10, "Qual país lançou o primeiro satélite artificial e levou o primeiro ser humano ao espaço?",
   ["União Soviética", "Estados Unidos", "China", "Alemanha"], "União Soviética",
   "A União Soviética lançou o Sputnik em 1957 e mandou Yuri Gagarin ao espaço em 1961.",
   "Enciclopédia Britannica – verbete 'Space exploration'")
mc(T, "asteroides", 1, 10, "Como se chama a rocha que gira em volta do Sol e é bem menor que um planeta, como as que ficam entre Marte e Júpiter?",
   ["Asteroide", "Estrela", "Galáxia", "Nebulosa"], "Asteroide",
   "A maioria dos asteroides conhecidos fica no cinturão principal, entre as órbitas de Marte e Júpiter.",
   "NASA – Asteroids")

# =========================================================== MÉDIAS
tf(T, "espaço", 2, 10, "No espaço, é possível ouvir o barulho de uma explosão.", False,
   "O som precisa de ar ou de outro meio para se propagar, e o espaço é praticamente vazio.",
   "NASA – Can You Hear Sound in Space?")
tf(T, "planetas", 2, 12, "Saturno é o único planeta do Sistema Solar que tem anéis.", False,
   "Júpiter, Urano e Netuno também têm anéis, só que bem mais finos e escuros que os de Saturno.",
   "NASA – Saturn: Facts")
tf(T, "estações do ano", 2, 12, "Quando é verão no hemisfério sul, é inverno no hemisfério norte.", True,
   "Por causa da inclinação da Terra, os hemisférios recebem mais luz do Sol em épocas opostas do ano.",
   "Enciclopédia Britannica – verbete 'Season'")
tf(T, "meteoros", 2, 12, "A maioria das chuvas de meteoros acontece quando a Terra passa pela poeira deixada por um cometa.", True,
   "Os grãos dessa poeira entram na atmosfera em alta velocidade e queimam, formando riscos de luz no céu.",
   "NASA – Meteors & Meteorites")
tf(T, "Lua", 2, 12, "As pegadas dos astronautas na Lua podem durar milhões de anos, porque lá não há vento nem chuva.", True,
   "Sem atmosfera, nada apaga as marcas no solo lunar, a não ser o lento impacto de micrometeoritos.",
   "NASA – Moon: Facts")
tf(T, "planetas", 2, 14, "Um dia em Marte dura quase o mesmo que um dia na Terra.", True,
   "Marte gira em torno de si em cerca de 24 horas e 37 minutos.",
   "NASA – Mars: Facts")
mc(T, "estações do ano", 2, 12, "O que causa as estações do ano na Terra?",
   ["A inclinação do eixo da Terra", "A distância variável entre a Terra e o Sol",
    "As fases da Lua", "A velocidade de rotação da Terra"], "A inclinação do eixo da Terra",
   "O eixo da Terra é inclinado cerca de 23,5 graus, então cada hemisfério recebe mais ou menos luz ao longo do ano.",
   "NASA Space Place – What Causes the Seasons?")
mc(T, "eclipses", 2, 12, "Durante um eclipse lunar total, a Lua costuma ficar com que cor?",
   ["Avermelhada", "Verde", "Azul-clara", "Branca e brilhante"], "Avermelhada",
   "A atmosfera da Terra desvia um pouco de luz avermelhada para a sombra, e por isso se fala em 'lua de sangue'.",
   "NASA – What Is a Lunar Eclipse?")
mc(T, "eclipses", 2, 12, "Em qual fase da Lua pode acontecer um eclipse solar?",
   ["Lua nova", "Lua cheia", "Quarto crescente", "Quarto minguante"], "Lua nova",
   "O eclipse solar só ocorre quando a Lua fica entre a Terra e o Sol, o que acontece na lua nova.",
   "NASA – Eclipses")
mc(T, "estrelas", 2, 12, "Qual é a cor das estrelas mais quentes?",
   ["Azul", "Vermelha", "Laranja", "Amarela"], "Azul",
   "As estrelas azuis passam dos 10 mil graus na superfície; as vermelhas são as mais frias.",
   "Enciclopédia Britannica – verbete 'Star'")
mc(T, "estrelas", 2, 12, "Como se chama a enorme explosão de uma estrela de grande massa no fim da vida?",
   ["Supernova", "Eclipse", "Aurora", "Cometa"], "Supernova",
   "Uma supernova pode brilhar, por algumas semanas, mais do que uma galáxia inteira.",
   "NASA – Supernovae")
mc(T, "galáxias", 2, 12, "Qual é o formato da Via Láctea?",
   ["Espiral", "Elíptica", "Irregular", "Em forma de anel"], "Espiral",
   "A Via Láctea é uma galáxia espiral barrada, com braços que giram em torno de um centro.",
   "NASA – The Milky Way Galaxy")
mc(T, "buracos negros", 2, 12, "O que é um buraco negro?",
   ["Uma região com gravidade tão forte que nem a luz escapa", "Um buraco na superfície da Lua",
    "Uma estrela apagada que perdeu a gravidade", "Um túnel que liga a Terra a Marte"],
   "Uma região com gravidade tão forte que nem a luz escapa",
   "Muitos buracos negros se formam quando uma estrela muito grande colapsa no fim da vida.",
   "NASA – Black Holes")
mc(T, "gravidade", 2, 12, "Se fosse possível ficar em cada um destes planetas, em qual uma pessoa pesaria mais?",
   ["Júpiter", "Marte", "Mercúrio", "Vênus"], "Júpiter",
   "A gravidade de Júpiter é cerca de duas vezes e meia a da Terra.",
   "NASA – Jupiter: Facts")
mc(T, "planetas", 2, 12, "Por que Marte tem cor avermelhada?",
   ["Seu solo tem muito óxido de ferro, como ferrugem", "Ele é muito quente, como brasa",
    "Ele reflete a luz de Júpiter", "Sua atmosfera é feita de fogo"], "Seu solo tem muito óxido de ferro, como ferrugem",
   "O pó rico em óxido de ferro cobre a superfície e até deixa o céu marciano rosado.",
   "NASA – Mars: Facts")
mc(T, "fases da Lua", 2, 12, "Como se chama a lua cheia que parece um pouco maior e mais brilhante por estar mais perto da Terra?",
   ["Superlua", "Lua azul", "Lua nova", "Meia-lua"], "Superlua",
   "A órbita da Lua é oval, e a superlua acontece quando a lua cheia coincide com o ponto mais próximo da Terra.",
   "NASA – What Is a Supermoon?")
mc(T, "unidades", 2, 12, "A unidade astronômica, usada para medir distâncias no Sistema Solar, é a distância média entre a Terra e qual astro?",
   ["Sol", "Lua", "Marte", "Júpiter"], "Sol",
   "Uma unidade astronômica vale cerca de 150 milhões de quilômetros.",
   "União Astronômica Internacional – Resolução B2 (2012)")
mc(T, "agências espaciais", 2, 12, "A ESA é a agência espacial de qual continente?",
   ["Europa", "Ásia", "África", "Oceania"], "Europa",
   "A Agência Espacial Europeia reúne mais de vinte países e tem sede em Paris.",
   "ESA – About Us")
mc(T, "agências espaciais", 2, 12, "Qual órgão coordena o programa espacial brasileiro?",
   ["Agência Espacial Brasileira", "Agência Nacional de Aviação Civil", "Embrapa",
    "Instituto Brasileiro de Geografia e Estatística"], "Agência Espacial Brasileira",
   "A Agência Espacial Brasileira, a AEB, foi criada em 1994 e fica em Brasília.",
   "Agência Espacial Brasileira – Institucional", br=True)
mc(T, "astronautas", 2, 12, "Em qual nave russa o brasileiro Marcos Pontes viajou ao espaço, em 2006?",
   ["Soyuz", "Apollo", "Discovery", "Dragon"], "Soyuz",
   "Ele partiu do Cazaquistão a bordo de uma Soyuz e passou cerca de uma semana na Estação Espacial Internacional.",
   "Agência Espacial Brasileira – Missão Centenário", br=True)
mc(T, "astronautas", 2, 12, "A missão de Marcos Pontes, em 2006, comemorou os cem anos do voo de qual invenção de Santos Dumont?",
   ["14-Bis", "Demoiselle", "Balão Brasil", "Dirigível nº 6"], "14-Bis",
   "Por isso ela se chamou Missão Centenário: o 14-Bis voou em Paris em 1906.",
   "Agência Espacial Brasileira – Missão Centenário", br=True)
op(T, "astronautas", 2, 12, "Como são chamados os viajantes espaciais da Rússia e da antiga União Soviética?",
   "Cosmonautas", ["cosmonautas", "cosmonauta"],
   "O termo vem de 'cosmos'; Yuri Gagarin e Valentina Tereshkova foram cosmonautas.",
   "Enciclopédia Britannica – verbete 'Cosmonaut'")
mc(T, "pesquisa espacial", 2, 12, "Em qual cidade paulista fica a sede do INPE, o Instituto Nacional de Pesquisas Espaciais?",
   ["São José dos Campos", "Campinas", "Santos", "Ribeirão Preto"], "São José dos Campos",
   "O INPE projeta satélites e monitora o desmatamento e o clima a partir de São José dos Campos.",
   "INPE – Institucional", br=True)
mc(T, "satélites", 2, 12, "Os satélites CBERS, que fotografam a Terra, foram desenvolvidos pelo Brasil em parceria com qual país?",
   ["China", "Japão", "Estados Unidos", "Rússia"], "China",
   "CBERS é a sigla em inglês para Satélite Sino-Brasileiro de Recursos Terrestres.",
   "INPE – Programa CBERS", br=True)
op(T, "Universo", 2, 14, "Como se chama a teoria que explica o início do Universo a partir de um estado extremamente quente e denso?",
   "Big Bang", ["big bang", "teoria do big bang", "grande explosão"],
   "Segundo essa teoria, o Universo começou há cerca de 13,8 bilhões de anos e vem se expandindo desde então.",
   "NASA – What Is the Big Bang?")

# =========================================================== DIFÍCEIS
tf(T, "Lua", 3, 14, "O lado da Lua que nunca vemos da Terra fica sempre no escuro.", False,
   "O lado oculto recebe luz do Sol normalmente; na lua nova, por exemplo, ele fica todo iluminado.",
   "NASA – The Far Side of the Moon")
tf(T, "estrelas", 3, 14, "O Sol vai terminar a vida explodindo como uma supernova.", False,
   "O Sol não tem massa suficiente para isso: deve virar uma gigante vermelha e depois uma anã branca.",
   "NASA – The Sun: Facts")
tf(T, "constelações", 3, 14, "O Cruzeiro do Sul é a menor das 88 constelações oficiais.", True,
   "Apesar de pequena, ela é uma das mais conhecidas do hemisfério sul e aparece na bandeira do Brasil.",
   "União Astronômica Internacional – The Constellations", br=True)
mc(T, "Lua", 3, 14, "Por que vemos sempre o mesmo lado da Lua?",
   ["Ela gira em torno de si no mesmo tempo em que gira em volta da Terra",
    "Ela não gira em torno de si mesma", "A Terra bloqueia a visão do outro lado",
    "O outro lado não recebe luz do Sol"],
   "Ela gira em torno de si no mesmo tempo em que gira em volta da Terra",
   "As duas voltas levam cerca de 27 dias, por isso a mesma face fica sempre voltada para nós.",
   "NASA – Moon: Facts")
mc(T, "estações do ano", 3, 14, "Como se chama a data em que o dia e a noite têm quase a mesma duração em todo o planeta?",
   ["Equinócio", "Solstício", "Eclipse", "Afélio"], "Equinócio",
   "Os equinócios acontecem em março e setembro, quando o Sol fica sobre a linha do Equador.",
   "Enciclopédia Britannica – verbete 'Equinox'")
mc(T, "estrelas", 3, 14, "Em que tipo de estrela o Sol deve se transformar quando o hidrogênio do seu centro acabar?",
   ["Gigante vermelha", "Buraco negro", "Estrela de nêutrons", "Quasar"], "Gigante vermelha",
   "Daqui a uns 5 bilhões de anos, o Sol deve inchar e virar uma gigante vermelha.",
   "NASA – The Sun: Facts")
mc(T, "galáxias", 3, 14, "Como se chamam as duas pequenas galáxias vizinhas que podem ser vistas a olho nu no céu do hemisfério sul?",
   ["Nuvens de Magalhães", "Plêiades", "Três Marias", "Nebulosa de Órion"], "Nuvens de Magalhães",
   "Elas são galáxias satélites da Via Láctea e foram descritas por navegantes da expedição de Fernão de Magalhães.",
   "ESA – Magellanic Clouds")
mc(T, "astronautas", 3, 14, "Qual astronauta da Apollo 11 ficou em órbita da Lua enquanto Armstrong e Aldrin desciam?",
   ["Michael Collins", "John Glenn", "Alan Shepard", "Gene Cernan"], "Michael Collins",
   "Collins pilotou o módulo de comando Columbia e esperou os colegas para a viagem de volta.",
   "NASA – Apollo 11 Mission Overview")
mc(T, "sondas", 3, 14, "Qual sonda da NASA passou perto de Plutão em 2015 e fez as primeiras fotos detalhadas dele?",
   ["New Horizons", "Voyager 2", "Cassini", "Juno"], "New Horizons",
   "As fotos revelaram uma grande planície clara em forma de coração na superfície de Plutão.",
   "NASA – New Horizons")
mc(T, "constelações", 3, 14, "Como é chamada popularmente a estrela pequena do Cruzeiro do Sul, que fica fora do desenho da cruz?",
   ["Intrometida", "Estrela d'Alva", "Sete-Estrelo", "Três Marias"], "Intrometida",
   "Na bandeira do Brasil, a Intrometida representa o estado do Espírito Santo.",
   "Lei nº 5.700/1971 – Anexo (Símbolos Nacionais)", br=True)
mc(T, "observatórios", 3, 14, "Qual instituição é responsável pela hora legal do Brasil?",
   ["Observatório Nacional", "IBGE", "Anatel", "Banco Central"], "Observatório Nacional",
   "Fundado em 1827, no Rio de Janeiro, o Observatório Nacional gera e divulga a hora oficial do país.",
   "Observatório Nacional – Divisão Serviço da Hora", br=True)
mc(T, "meteoritos", 3, 14, "Qual meteorito, o maior já encontrado no Brasil, resistiu ao incêndio do Museu Nacional em 2018?",
   ["Bendegó", "Santa Luzia", "Angra dos Reis", "Patos de Minas"], "Bendegó",
   "Feito principalmente de ferro e com mais de 5 toneladas, ele foi achado no sertão da Bahia em 1784.",
   "Museu Nacional/UFRJ – Meteorito Bendegó", br=True)
mc(T, "foguetes", 3, 14, "Qual centro de lançamento de foguetes, inaugurado em 1965, fica no Rio Grande do Norte, perto de Natal?",
   ["Barreira do Inferno", "Alcântara", "Cabo Canaveral", "Baikonur"], "Barreira do Inferno",
   "O Centro de Lançamento da Barreira do Inferno fica em Parnamirim e é operado pela Força Aérea Brasileira.",
   "Força Aérea Brasileira – Centro de Lançamento da Barreira do Inferno", br=True)
op(T, "planetas", 3, 14, "Como se chamam os planetas que giram em torno de outras estrelas, fora do Sistema Solar?",
   "Exoplanetas", ["exoplanetas", "exoplaneta", "planetas extrassolares", "planeta extrassolar"],
   "O primeiro exoplaneta em torno de uma estrela parecida com o Sol foi descoberto em 1995.",
   "NASA – Exoplanet Exploration")

# =========================================================== MUITO DIFÍCEIS
mc(T, "eclipses", 4, 16, "Em qual cidade do Ceará foi observado o eclipse solar de 1919 que ajudou a comprovar a teoria da relatividade de Einstein?",
   ["Sobral", "Juazeiro do Norte", "Crato", "Quixadá"], "Sobral",
   "As fotos do eclipse mostraram que a luz das estrelas se curva ao passar perto do Sol, como Einstein previu.",
   "Observatório Nacional – Eclipse de Sobral (1919)", br=True)
mc(T, "satélites", 4, 16, "Qual foi o primeiro satélite desenvolvido no Brasil, lançado em 1993?",
   ["SCD-1", "Amazonia-1", "CBERS-1", "Brasilsat A1"], "SCD-1",
   "O Satélite de Coleta de Dados 1 foi projetado pelo INPE e recebe informações de estações ambientais em terra.",
   "INPE – Satélite SCD-1", br=True)
mc(T, "constelações", 4, 16, "Na bandeira do Brasil, a estrela mais brilhante do Cruzeiro do Sul representa qual estado?",
   ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia"], "São Paulo",
   "A estrela Alfa do Cruzeiro do Sul representa São Paulo; as outras estrelas da cruz representam os demais estados das opções.",
   "Lei nº 5.700/1971 – Anexo (Símbolos Nacionais)", br=True)
mc(T, "constelações", 4, 16, "Qual ave dá nome a uma grande constelação dos povos guaranis, vista perto do Cruzeiro do Sul?",
   ["Ema", "Arara", "Beija-flor", "Gavião"], "Ema",
   "Para povos guaranis do sul do Brasil, o surgimento da Ema no início da noite, em junho, marca a chegada do inverno.",
   "Germano Bruno Afonso – O Céu dos Índios Tembé / Mitos e Estações no Céu Tupi-Guarani", br=True)
mc(T, "cometas", 4, 16, "Qual cometa se partiu em pedaços e colidiu com Júpiter em 1994?",
   ["Shoemaker-Levy 9", "Halley", "Hale-Bopp", "Encke"], "Shoemaker-Levy 9",
   "Foi a primeira colisão entre dois corpos do Sistema Solar observada diretamente pelos cientistas.",
   "NASA – Comet Shoemaker-Levy 9")
mc(T, "sondas", 4, 16, "Qual sonda estudou Saturno por 13 anos e terminou a missão mergulhando no planeta, em 2017?",
   ["Cassini", "Juno", "Galileo", "Magellan"], "Cassini",
   "O mergulho final evitou que a sonda contaminasse luas que podem ter condições para a vida, como Encélado.",
   "NASA – Cassini Mission")
