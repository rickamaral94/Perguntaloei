# Temas novos (continuação): Astronomia e espaço, Corpo humano e saúde, Culinária.
from qdsl import mc, op, tf

# =========================================================== ASTRONOMIA E ESPAÇO
S = "ast"
mc(S, "Lua", 1, 6, "Qual é o único satélite natural da Terra?",
   ["A Lua", "O Sol", "Marte", "Vênus"], "A Lua",
   "A Lua fica a cerca de 384 mil km da Terra.",
   "NASA – Moon Facts", syn=["lua"])
mc(S, "astronautas", 1, 6, "Em que veículo os astronautas viajam para o espaço?",
   ["Foguete", "Avião", "Helicóptero", "Balão"], "Foguete",
   "Os foguetes precisam de muita força para vencer a gravidade da Terra.",
   "NASA Space Place – What is a rocket?")
mc(S, "astronautas", 1, 6, "O que os astronautas usam para respirar fora da nave?",
   ["Um traje espacial com oxigênio", "Um guarda-chuva", "Um chapéu de festa", "Nada, lá tem ar"],
   "Um traje espacial com oxigênio",
   "No espaço não há ar para respirar; o traje leva o oxigênio.",
   "NASA – Spacesuits", syn=["traje espacial", "roupa de astronauta"])
mc(S, "céu", 1, 6, "Quando conseguimos ver mais estrelas no céu?",
   ["De noite", "De dia", "Ao meio-dia"], "De noite",
   "De dia as estrelas continuam lá, mas a luz do Sol esconde o brilho delas.",
   "NASA Space Place – Why can't we see stars during the day?", syn=["a noite", "noite"])
mc(S, "planetas", 1, 7, "Qual planeta tem os anéis mais famosos e visíveis?",
   ["Saturno", "Terra", "Mercúrio", "Marte"], "Saturno",
   "Os anéis de Saturno são feitos de gelo e rocha.",
   "NASA – Saturn Facts")
mc(S, "movimentos da Terra", 1, 9, "Quanto tempo a Terra leva para dar uma volta completa em torno do Sol?",
   ["Cerca de 365 dias", "24 horas", "30 dias", "7 dias"], "Cerca de 365 dias",
   "São cerca de 365 dias e 6 horas; por isso existe o ano bissexto.",
   "NASA – Earth Facts", syn=["um ano", "365 dias", "1 ano"])
mc(S, "movimentos da Terra", 1, 9, "Quanto tempo a Terra leva para girar uma vez em torno de si mesma?",
   ["Cerca de 24 horas", "Cerca de 1 hora", "Cerca de 7 dias", "Cerca de 1 ano"], "Cerca de 24 horas",
   "Esse giro faz o dia e a noite.",
   "NASA – Earth Facts", syn=["24 horas", "um dia", "1 dia"])
mc(S, "agências", 1, 10, "Como se chama a agência espacial dos Estados Unidos?",
   ["NASA", "ESA", "INPE", "AEB"], "NASA",
   "A NASA foi criada em 1958. ESA é a agência europeia e AEB a brasileira.",
   "NASA – About")
mc(S, "galáxias", 1, 10, "Como se chama a galáxia onde fica o Sistema Solar?",
   ["Via Láctea", "Andrômeda", "Nuvem de Magalhães", "Sombrero"], "Via Láctea",
   "A Via Láctea tem centenas de bilhões de estrelas.",
   "NASA – The Milky Way Galaxy", syn=["via lactea"])
mc(S, "céu do Brasil", 1, 10, "Qual constelação aparece na bandeira do Brasil e ajuda a encontrar o ponto cardeal Sul?",
   ["Cruzeiro do Sul", "Órion", "Ursa Maior", "Escorpião"], "Cruzeiro do Sul",
   "O Cruzeiro do Sul só é visível no Hemisfério Sul e em parte do Norte, perto do Equador.",
   "Observatório Nacional – Constelações", syn=["cruzeiro"], br=True)
mc(S, "movimentos da Terra", 2, 10, "Como se chama o movimento da Terra em volta do Sol?",
   ["Translação", "Rotação", "Precessão", "Nutação"], "Translação",
   "A translação, junto com a inclinação do eixo da Terra, causa as estações do ano.",
   "Observatório Nacional – Movimentos da Terra", syn=["translacao"])
mc(S, "movimentos da Terra", 2, 10, "Como se chama o giro da Terra em torno do próprio eixo, que forma os dias e as noites?",
   ["Rotação", "Translação", "Órbita", "Eclipse"], "Rotação",
   "A Terra gira de oeste para leste; por isso o Sol 'nasce' no leste.",
   "Observatório Nacional – Movimentos da Terra", syn=["rotacao"])
mc(S, "planetas", 2, 10, "Qual é o planeta mais distante do Sol no Sistema Solar?",
   ["Netuno", "Urano", "Saturno", "Plutão"], "Netuno",
   "Plutão, que é mais distante, é classificado como planeta-anão.",
   "NASA – Neptune Facts")
mc(S, "Lua", 2, 10, "O que causa as fases da Lua?",
   ["A posição da Lua em relação ao Sol e à Terra", "Nuvens que tampam a Lua", "A Lua encolhendo e crescendo", "A sombra de Marte"],
   "A posição da Lua em relação ao Sol e à Terra",
   "Vemos partes diferentes da metade iluminada da Lua conforme ela gira em volta da Terra.",
   "NASA – Moon Phases")
mc(S, "eclipses", 2, 10, "Como se chama o fenômeno em que a Lua passa entre a Terra e o Sol e esconde o Sol?",
   ["Eclipse solar", "Eclipse lunar", "Aurora boreal", "Chuva de meteoros"], "Eclipse solar",
   "Nunca olhe para um eclipse solar sem proteção adequada.",
   "NASA – Eclipses", syn=["eclipse do sol"])
mc(S, "fenômenos", 2, 10, "Como se chamam as luzes coloridas que aparecem no céu perto do Polo Norte?",
   ["Aurora boreal", "Arco-íris", "Via Láctea", "Estrela cadente"], "Aurora boreal",
   "Elas surgem quando partículas do Sol encontram o campo magnético da Terra. No Sul, é a aurora austral.",
   "NOAA – Aurora", syn=["aurora"])
mc(S, "fenômenos", 2, 10, "O que é a chamada 'estrela cadente' que vemos riscando o céu?",
   ["Um meteoro", "Uma estrela caindo", "Um avião", "Um planeta"], "Um meteoro",
   "É um pedacinho de rocha que pega fogo ao entrar na atmosfera.",
   "NASA – Meteors & Meteorites", syn=["meteoro"])
mc(S, "planetas-anões", 2, 10, "Qual corpo celeste deixou de ser considerado planeta em 2006?",
   ["Plutão", "Ceres", "Netuno", "Mercúrio"], "Plutão",
   "A União Astronômica Internacional o reclassificou como planeta-anão.",
   "União Astronômica Internacional – Resolução B5 (2006)", syn=["plutao"])
mc(S, "corrida espacial", 2, 12, "Quem foi o primeiro ser humano a ir ao espaço, em 1961?",
   ["Yuri Gagarin", "Neil Armstrong", "John Glenn", "Valentina Tereshkova"], "Yuri Gagarin",
   "Gagarin teria dito: 'A Terra é azul!'.",
   "Agência Espacial Europeia – Yuri Gagarin", syn=["gagarin"])
mc(S, "telescópios", 2, 12, "Qual telescópio espacial, lançado em 1990, fez algumas das fotos mais famosas do Universo?",
   ["Hubble", "James Webb", "Kepler", "Galileu"], "Hubble",
   "O Hubble orbita a Terra a cerca de 540 km de altitude.",
   "NASA – Hubble Space Telescope")
mc(S, "planetas", 2, 12, "Qual planeta tem a Grande Mancha Vermelha, uma tempestade gigante?",
   ["Júpiter", "Marte", "Saturno", "Vênus"], "Júpiter",
   "A tempestade é maior do que a Terra e existe há séculos.",
   "NASA – Jupiter's Great Red Spot", syn=["jupiter"])
mc(S, "distâncias", 2, 12, "O que é um ano-luz?",
   ["A distância que a luz percorre em um ano", "O tempo de um ano em outro planeta", "Um ano com mais dias de sol", "A idade de uma estrela"],
   "A distância que a luz percorre em um ano",
   "Um ano-luz equivale a cerca de 9,5 trilhões de quilômetros.",
   "União Astronômica Internacional – Light-year")
mc(S, "corrida espacial", 2, 12, "Em que ano a missão Apollo 11 pousou na Lua?",
   ["1969", "1957", "1972", "1961"], "1969",
   "O módulo lunar Eagle pousou em 20 de julho de 1969.",
   "NASA – Apollo 11 Mission Overview")
mc(S, "céu do Brasil", 3, 12, "Quantas estrelas há na bandeira do Brasil?",
   ["27", "26", "22", "21"], "27",
   "Cada estrela representa um estado ou o Distrito Federal.",
   "Lei nº 8.421/1992 – Símbolos Nacionais", br=True)
mc(S, "cometas", 3, 12, "Qual cometa famoso passa perto da Terra a cada 75 ou 76 anos?",
   ["Halley", "Hale-Bopp", "Encke", "Shoemaker-Levy"], "Halley",
   "Sua última passagem foi em 1986; a próxima está prevista para 2061.",
   "NASA – Comet Halley")
mc(S, "corrida espacial", 3, 14, "Qual foi o primeiro satélite artificial lançado ao espaço, em 1957?",
   ["Sputnik", "Apollo", "Explorer", "Hubble"], "Sputnik",
   "Lançado pela União Soviética, o Sputnik 1 deu início à corrida espacial.",
   "NASA – Sputnik and the Origins of the Space Age", syn=["sputnik 1"])
mc(S, "telescópios", 3, 14, "Qual telescópio espacial, lançado em 2021, observa o Universo em luz infravermelha?",
   ["James Webb", "Hubble", "Chandra", "Spitzer"], "James Webb",
   "O Webb fica a cerca de 1,5 milhão de km da Terra.",
   "NASA – James Webb Space Telescope", syn=["webb"])
mc(S, "planetas", 3, 14, "Qual planeta gira 'deitado', com o eixo quase paralelo à sua órbita?",
   ["Urano", "Netuno", "Júpiter", "Mercúrio"], "Urano",
   "Urano tem o eixo inclinado em cerca de 98 graus.",
   "NASA – Uranus Facts")
mc(S, "estrelas", 3, 14, "Qual é a estrela mais brilhante do céu noturno?",
   ["Sirius", "Polaris", "Betelgeuse", "Vega"], "Sirius",
   "Sirius fica na constelação do Cão Maior.",
   "NASA – Sirius")
mc(S, "galáxias", 3, 14, "Qual grande galáxia espiral vizinha está em rota de colisão com a nossa, daqui a bilhões de anos?",
   ["Andrômeda", "Triângulo", "Sombrero", "Redemoinho"], "Andrômeda",
   "Andrômeda fica a cerca de 2,5 milhões de anos-luz.",
   "NASA – Andromeda Galaxy", syn=["andromeda"])
mc(S, "estrelas", 4, 14, "Depois do Sol, qual é a estrela mais próxima da Terra?",
   ["Proxima Centauri", "Sirius", "Polaris", "Betelgeuse"], "Proxima Centauri",
   "Ela fica a cerca de 4,2 anos-luz de distância.",
   "NASA – Proxima Centauri", syn=["proxima"])
mc(S, "planetas", 4, 16, "Qual é o maior vulcão conhecido do Sistema Solar?",
   ["Monte Olimpo, em Marte", "Mauna Kea, no Havaí", "Monte Etna, na Itália", "Maat Mons, em Vênus"], "Monte Olimpo, em Marte",
   "O Olympus Mons tem cerca de 22 km de altura, quase três vezes o Everest.",
   "NASA – Olympus Mons", syn=["olympus mons", "monte olimpo"])

# =========================================================== CORPO HUMANO E SAÚDE
C = "cor"
mc(C, "órgãos", 1, 6, "Qual órgão usamos para respirar?",
   ["Pulmões", "Rins", "Estômago", "Fígado"], "Pulmões",
   "Os pulmões levam o oxigênio do ar para o sangue.",
   "Biblioteca Virtual em Saúde – Ministério da Saúde", syn=["pulmao", "pulmoes"])
mc(C, "sentidos", 1, 6, "Com qual parte do corpo sentimos os cheiros?",
   ["Nariz", "Orelha", "Mão", "Joelho"], "Nariz",
   "O olfato também ajuda a sentir o sabor dos alimentos.",
   "Biblioteca Virtual em Saúde – Ministério da Saúde")
mc(C, "higiene", 1, 6, "O que devemos fazer antes das refeições para evitar doenças?",
   ["Lavar as mãos", "Pular corda", "Assistir TV", "Dormir"], "Lavar as mãos",
   "Lavar as mãos com água e sabão por pelo menos 20 segundos elimina muitos germes.",
   "Ministério da Saúde – Higienização das mãos", syn=["lavar a mao", "lavar as maos"])
mc(C, "alimentação", 1, 6, "Qual destes alimentos é uma fruta?",
   ["Maçã", "Batata frita", "Pirulito", "Pão"], "Maçã",
   "O Guia Alimentar recomenda frutas todos os dias.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira", syn=["maca"])
mc(C, "sentidos", 1, 7, "Com qual sentido percebemos se algo é doce ou salgado?",
   ["Paladar", "Olfato", "Audição", "Visão"], "Paladar",
   "As papilas gustativas da língua captam os sabores.",
   "Biblioteca Virtual em Saúde – Ministério da Saúde")
mc(C, "dentes", 1, 8, "Quantos dentes de leite uma criança costuma ter?",
   ["20", "32", "10", "28"], "20",
   "Os dentes de leite começam a cair por volta dos 6 anos.",
   "Ministério da Saúde – Saúde Bucal")
mc(C, "sentidos", 1, 8, "Quais são os cinco sentidos do corpo humano?",
   ["Visão, audição, olfato, paladar e tato", "Visão, fome, sono, sede e tato", "Força, equilíbrio, visão, fala e audição", "Olfato, memória, fala, tato e fome"],
   "Visão, audição, olfato, paladar e tato",
   "Cada sentido tem órgãos próprios: olhos, ouvidos, nariz, língua e pele.",
   "Biblioteca Virtual em Saúde – Ministério da Saúde")
mc(C, "órgãos", 1, 8, "Qual órgão é o principal responsável pelo pensamento e pela memória?",
   ["Cérebro", "Coração", "Pulmão", "Estômago"], "Cérebro",
   "O cérebro tem cerca de 86 bilhões de neurônios.",
   "NIH – Brain Basics", syn=["cerebro"])
mc(C, "vitaminas", 1, 9, "Qual vitamina é abundante na laranja e no limão?",
   ["Vitamina C", "Vitamina D", "Vitamina K", "Vitamina B12"], "Vitamina C",
   "A vitamina C ajuda o sistema de defesa do corpo.",
   "Ministério da Saúde – Biblioteca Virtual em Saúde")
mc(C, "dentes", 2, 10, "Quantos dentes tem um adulto com a dentição completa, incluindo os sisos?",
   ["32", "20", "28", "36"], "32",
   "Sem os quatro sisos, são 28 dentes.",
   "Ministério da Saúde – Saúde Bucal")
mc(C, "órgãos", 2, 10, "Qual órgão filtra o sangue e produz a urina?",
   ["Rins", "Fígado", "Pulmões", "Baço"], "Rins",
   "Temos dois rins, cada um do tamanho de um punho fechado.",
   "Sociedade Brasileira de Nefrologia", syn=["rim"])
mc(C, "hábitos", 2, 10, "Quantas horas de sono por noite são recomendadas, em média, para um adulto?",
   ["De 7 a 9 horas", "De 2 a 3 horas", "De 12 a 14 horas", "Exatamente 5 horas"], "De 7 a 9 horas",
   "Crianças e adolescentes precisam de ainda mais horas de sono.",
   "National Sleep Foundation – How Much Sleep Do We Really Need?", syn=["7 a 9 horas", "8 horas"])
mc(C, "corpo", 2, 10, "Qual é a temperatura normal aproximada do corpo humano?",
   ["Cerca de 36,5 °C", "Cerca de 30 °C", "Cerca de 40 °C", "Cerca de 25 °C"], "Cerca de 36,5 °C",
   "Acima de 37,8 °C já costuma ser considerado febre.",
   "Ministério da Saúde – Febre", syn=["36 e meio", "36 5", "37 graus"])
mc(C, "olhos", 2, 12, "Qual parte do olho dá cor aos nossos olhos?",
   ["Íris", "Pupila", "Córnea", "Retina"], "Íris",
   "A pupila é a 'bolinha preta' no centro da íris, que controla a entrada de luz.",
   "American Academy of Ophthalmology – Eye Anatomy", syn=["iris"])
mc(C, "sangue", 2, 12, "Qual célula do sangue transporta o oxigênio?",
   ["Glóbulo vermelho", "Glóbulo branco", "Plaqueta", "Neurônio"], "Glóbulo vermelho",
   "Os glóbulos vermelhos (hemácias) têm hemoglobina, que se liga ao oxigênio.",
   "NIH – Red Blood Cells", syn=["hemacia", "hemacias", "globulos vermelhos", "eritrocito"])
mc(C, "coração", 2, 12, "Quantas cavidades (câmaras) tem o coração humano?",
   ["4", "2", "3", "6"], "4",
   "Dois átrios e dois ventrículos.",
   "American Heart Association – How the Heart Works")
mc(C, "coração", 2, 12, "Quantas vezes por minuto bate, em repouso, o coração de um adulto saudável?",
   ["Entre 60 e 100", "Entre 10 e 20", "Entre 150 e 200", "Exatamente 120"], "Entre 60 e 100",
   "Atletas podem ter frequência de repouso ainda menor.",
   "American Heart Association – Target Heart Rates")
mc(C, "história da medicina", 2, 12, "Qual cientista descobriu a penicilina, em 1928?",
   ["Alexander Fleming", "Louis Pasteur", "Oswaldo Cruz", "Robert Koch"], "Alexander Fleming",
   "Fleming percebeu que um mofo matava as bactérias da sua placa de cultura.",
   "Nobel Prize – Alexander Fleming (1945)", syn=["fleming"])
mc(C, "órgãos", 2, 12, "Qual órgão, do lado direito do abdome, é o maior dentro do corpo?",
   ["Fígado", "Baço", "Estômago", "Pâncreas"], "Fígado",
   "O fígado produz a bile e ajuda a eliminar substâncias tóxicas.",
   "NIH – The Liver", syn=["figado"])
mc(C, "sangue", 3, 12, "Quantos litros de sangue tem, aproximadamente, um adulto?",
   ["Cerca de 5 litros", "Cerca de 1 litro", "Cerca de 15 litros", "Cerca de 50 litros"], "Cerca de 5 litros",
   "O volume varia com o peso, girando em torno de 7% do peso corporal.",
   "Fundação Pró-Sangue – Hemocentro de São Paulo", syn=["5 litros", "cinco litros"])
mc(C, "ossos", 3, 14, "Qual é o menor osso do corpo humano, que fica dentro do ouvido?",
   ["Estribo", "Martelo", "Bigorna", "Falange"], "Estribo",
   "O estribo mede cerca de 3 milímetros.",
   "Enciclopédia Britannica – verbete 'stapes'")
mc(C, "sangue", 3, 14, "Qual tipo de sangue é considerado 'doador universal' para transfusões?",
   ["O negativo", "AB positivo", "A positivo", "B negativo"], "O negativo",
   "O sangue O negativo pode ser dado a qualquer tipo em emergências.",
   "Fundação Pró-Sangue – Hemocentro de São Paulo", syn=["o menos"])
mc(C, "sangue", 3, 14, "Qual tipo sanguíneo é considerado 'receptor universal'?",
   ["AB positivo", "O negativo", "A negativo", "B positivo"], "AB positivo",
   "Quem é AB positivo pode receber hemácias de todos os tipos.",
   "Fundação Pró-Sangue – Hemocentro de São Paulo", syn=["ab mais"])
mc(C, "história da medicina", 3, 14, "Qual médico brasileiro liderou a campanha de vacinação que gerou a Revolta da Vacina, em 1904?",
   ["Oswaldo Cruz", "Carlos Chagas", "Vital Brazil", "Adolfo Lutz"], "Oswaldo Cruz",
   "A vacinação obrigatória contra a varíola provocou protestos no Rio de Janeiro.",
   "Fiocruz – Oswaldo Cruz", br=True)
mc(C, "história da medicina", 3, 14, "Quem desenvolveu a primeira vacina, contra a varíola, no fim do século XVIII?",
   ["Edward Jenner", "Louis Pasteur", "Alexander Fleming", "Jonas Salk"], "Edward Jenner",
   "Jenner usou material da varíola bovina em 1796; daí vem a palavra 'vacina' (de vaca).",
   "Enciclopédia Britannica – verbete 'Edward Jenner'", syn=["jenner"])
mc(C, "órgãos", 3, 14, "Qual órgão produz a insulina?",
   ["Pâncreas", "Fígado", "Rins", "Estômago"], "Pâncreas",
   "A insulina controla o açúcar no sangue; sua falta causa o diabetes tipo 1.",
   "Sociedade Brasileira de Diabetes", syn=["pancreas"])
mc(C, "músculos", 3, 14, "Qual músculo separa o tórax do abdome e é essencial para a respiração?",
   ["Diafragma", "Bíceps", "Abdominal", "Peitoral"], "Diafragma",
   "O soluço é uma contração involuntária do diafragma.",
   "NIH – How the Lungs Work")
mc(C, "sangue", 3, 14, "Qual é a maior artéria do corpo humano?",
   ["Aorta", "Veia cava", "Jugular", "Carótida"], "Aorta",
   "Ela leva o sangue rico em oxigênio para todo o corpo.",
   "American Heart Association – How the Heart Works")
tf(C, "músculos", 3, 14, "O corpo humano tem mais de 600 músculos.", True,
   "São cerca de 640 músculos esqueléticos, segundo a contagem mais usada.",
   "Enciclopédia Britannica – verbete 'human muscle system'")
mc(C, "músculos", 4, 16, "Qual músculo, usado para mastigar, é um dos mais fortes do corpo em relação ao tamanho?",
   ["Masseter", "Glúteo máximo", "Bíceps", "Deltoide"], "Masseter",
   "O masseter fica na lateral do rosto e fecha a mandíbula.",
   "Enciclopédia Britannica – verbete 'masseter muscle'")

# =========================================================== CULINÁRIA
K = "gas"
mc(K, "frutas", 1, 6, "Qual fruta amarela os macacos adoram comer?",
   ["Banana", "Uva", "Melancia", "Kiwi"], "Banana",
   "A banana é uma das frutas mais consumidas no Brasil.",
   "Embrapa – Banana")
mc(K, "alimentos", 1, 6, "Que bebida branca vem da vaca?",
   ["Leite", "Suco", "Café", "Chá"], "Leite",
   "O leite é rico em cálcio, importante para ossos e dentes.",
   "Embrapa Gado de Leite")
mc(K, "doces", 1, 6, "Qual destes é um doce?",
   ["Bolo de chocolate", "Alface", "Arroz", "Sal"], "Bolo de chocolate",
   "Doces são gostosos, mas o ideal é comer com moderação.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira", syn=["bolo"])
mc(K, "frutas", 1, 6, "Qual fruta vermelha tem as sementinhas do lado de fora?",
   ["Morango", "Maçã", "Cereja", "Melancia"], "Morango",
   "Os pontinhos do morango são, na verdade, os frutos verdadeiros da planta.",
   "Embrapa – Morango")
mc(K, "salgados", 1, 7, "Qual salgadinho frito tem recheio de frango e formato de gota?",
   ["Coxinha", "Pastel", "Empada", "Quibe"], "Coxinha",
   "A coxinha é um dos salgados mais populares das festas brasileiras.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(K, "chocolate", 1, 7, "De qual fruto é feito o chocolate?",
   ["Cacau", "Café", "Coco", "Castanha"], "Cacau",
   "As sementes do cacau são fermentadas, secas e torradas.",
   "Embrapa – Cacau", syn=["semente de cacau"])
mc(K, "pratos do mundo", 1, 8, "Em qual país nasceu a pizza?",
   ["Itália", "Estados Unidos", "França", "Grécia"], "Itália",
   "A pizza moderna surgiu em Nápoles; a margherita é de 1889.",
   "Associazione Verace Pizza Napoletana", syn=["italia"])
mc(K, "pratos do mundo", 1, 8, "Qual prato italiano tem camadas de massa, molho e queijo, assadas no forno?",
   ["Lasanha", "Risoto", "Nhoque", "Ravióli"], "Lasanha",
   "A lasanha à bolonhesa é uma das versões mais famosas.",
   "Accademia Italiana della Cucina")
mc(K, "pratos brasileiros", 1, 8, "Qual prato gaúcho é feito com carne assada no espeto, na brasa?",
   ["Churrasco", "Moqueca", "Baião de dois", "Vatapá"], "Churrasco",
   "No Sul, o churrasco tradicional leva só sal grosso.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(K, "doces", 1, 8, "Qual doce de festa junina é feito com amendoim e açúcar?",
   ["Paçoca", "Canjica", "Quindim", "Cocada"], "Paçoca",
   "A paçoca é feita de amendoim torrado e moído, açúcar e farinha.",
   "Câmara Cascudo – História da Alimentação no Brasil", syn=["pacoca"], br=True)
mc(K, "alimentação", 1, 8, "Qual destes alimentos é rico em proteína?",
   ["Ovo", "Alface", "Maçã", "Açúcar"], "Ovo",
   "Ovos, carnes, feijão e leite são boas fontes de proteína.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
mc(K, "temperos", 1, 8, "Qual destes é um tempero, e não uma fruta?",
   ["Orégano", "Manga", "Uva", "Pera"], "Orégano",
   "O orégano é uma erva muito usada na pizza.",
   "Embrapa Hortaliças – Ervas aromáticas", syn=["oregano"])
mc(K, "frutas", 1, 9, "Qual fruta amazônica é servida na tigela, com granola e banana?",
   ["Açaí", "Cupuaçu", "Graviola", "Pitanga"], "Açaí",
   "Na Amazônia, o açaí é tradicionalmente comido com peixe e farinha.",
   "Embrapa Amazônia Oriental – Açaí", syn=["acai"], br=True)
mc(K, "pratos do mundo", 1, 9, "Além do peixe, qual é o ingrediente principal do sushi?",
   ["Arroz", "Feijão", "Batata", "Macarrão"], "Arroz",
   "O arroz do sushi é temperado com vinagre de arroz.",
   "Japan National Tourism Organization – Sushi")
mc(K, "panificação", 1, 9, "Qual ingrediente faz a massa do pão crescer?",
   ["Fermento", "Sal", "Açúcar", "Óleo"], "Fermento",
   "O fermento biológico produz gás carbônico, que forma as bolhas da massa.",
   "Embrapa Trigo – Panificação")
mc(K, "pratos brasileiros", 1, 10, "De qual estado brasileiro é típico o pão de queijo?",
   ["Minas Gerais", "Bahia", "Pará", "Rio Grande do Sul"], "Minas Gerais",
   "O Modo Artesanal de Fazer Queijo de Minas é patrimônio cultural do Brasil.",
   "IPHAN – Queijo Artesanal de Minas", br=True)
mc(K, "pratos do mundo", 2, 10, "De qual fruta se faz o guacamole?",
   ["Abacate", "Tomate", "Limão", "Manga"], "Abacate",
   "O guacamole é um prato típico do México.",
   "Gobierno de México – Gastronomía mexicana")
mc(K, "pratos brasileiros", 2, 10, "Qual é o ingrediente principal do pão de queijo, além do queijo?",
   ["Polvilho", "Farinha de trigo", "Fubá", "Aveia"], "Polvilho",
   "O polvilho vem da mandioca, por isso o pão de queijo não tem glúten.",
   "Embrapa Mandioca e Fruticultura – Polvilho", br=True)
mc(K, "pratos brasileiros", 2, 10, "O que é a tapioca?",
   ["Uma massa feita de goma de mandioca", "Um tipo de peixe", "Um queijo", "Uma fruta"],
   "Uma massa feita de goma de mandioca",
   "A tapioca é herança dos povos indígenas.",
   "Embrapa Mandioca e Fruticultura", br=True)
mc(K, "pratos do mundo", 2, 10, "De qual país vem a paella, prato de arroz com frutos do mar?",
   ["Espanha", "Itália", "Portugal", "México"], "Espanha",
   "A paella nasceu na região de Valência.",
   "Turespaña – Paella valenciana")
mc(K, "pães e doces", 2, 10, "Qual país é famoso pelo croissant?",
   ["França", "Alemanha", "Inglaterra", "Japão"], "França",
   "Apesar da fama francesa, a receita foi inspirada num pão austríaco.",
   "Enciclopédia Britannica – verbete 'croissant'", syn=["franca"])
mc(K, "queijos", 2, 10, "Qual queijo italiano é usado na pizza margherita?",
   ["Muçarela", "Parmesão", "Gorgonzola", "Provolone"], "Muçarela",
   "A margherita tem as cores da Itália: manjericão, muçarela e tomate.",
   "Associazione Verace Pizza Napoletana", syn=["mussarela", "mozzarella"])
mc(K, "café", 2, 10, "Qual país é o maior produtor de café do mundo?",
   ["Brasil", "Colômbia", "Vietnã", "Etiópia"], "Brasil",
   "O Brasil lidera a produção mundial de café há mais de 150 anos.",
   "Embrapa Café; USDA – Coffee: World Markets and Trade", br=True, ref="Safra 2024/25")
mc(K, "pratos brasileiros", 2, 12, "Qual prato mineiro mistura feijão, farinha de mandioca, linguiça e ovo?",
   ["Feijão tropeiro", "Baião de dois", "Arroz carreteiro", "Virado à paulista"], "Feijão tropeiro",
   "O nome vem dos tropeiros, que viajavam com tropas de mulas.",
   "Câmara Cascudo – História da Alimentação no Brasil", syn=["tropeiro"], br=True)
mc(K, "bebidas", 2, 12, "Como se chama a bebida de erva-mate servida gelada no Mato Grosso do Sul e no Paraguai?",
   ["Tereré", "Chimarrão", "Mate leão", "Chá-mate"], "Tereré",
   "O tereré é patrimônio cultural imaterial da humanidade pela UNESCO (2020).",
   "UNESCO – Tereré (2020)", syn=["terere"], br=True)
mc(K, "pratos do mundo", 2, 12, "Como se chama o prato japonês de peixe cru fatiado, servido sem arroz?",
   ["Sashimi", "Sushi", "Tempurá", "Yakisoba"], "Sashimi",
   "O sushi leva arroz; o sashimi é só o peixe fatiado.",
   "Japan National Tourism Organization – Sashimi")
mc(K, "temperos", 3, 14, "Qual tempero dá a cor amarela à paella e é um dos mais caros do mundo?",
   ["Açafrão", "Cúrcuma", "Páprica", "Cominho"], "Açafrão",
   "O açafrão vem dos estigmas de uma flor, colhidos à mão.",
   "Enciclopédia Britannica – verbete 'saffron'", syn=["acafrao"])
mc(K, "bebidas", 2, 16, "Qual fruta é usada na caipirinha tradicional?",
   ["Limão", "Morango", "Maracujá", "Abacaxi"], "Limão",
   "A caipirinha (limão, açúcar, gelo e cachaça) é reconhecida em lei como bebida típica brasileira.",
   "Decreto nº 6.871/2009 (padronização de bebidas)", syn=["limao"], br=True)
