# Perguntas novas: cultura brasileira. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "cul"

# ================================================== FÁCEIS
mc(T, "cantigas de roda", 1, 6, "Na cantiga 'Marcha, soldado', o soldado tem cabeça de quê?",
   ["Papel", "Pano", "Madeira", "Algodão"], "Papel",
   "A cantiga diz: 'Marcha, soldado, cabeça de papel; quem não marchar direito vai preso no quartel'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cantigas de roda", 1, 6, "Na cantiga 'Borboletinha', onde está a borboletinha?",
   ["Na cozinha", "No jardim", "Na escola", "Na praia"], "Na cozinha",
   "A borboletinha 'tá na cozinha, fazendo chocolate para a madrinha'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cantigas de roda", 1, 6, "Na cantiga 'O sapo não lava o pé', onde o sapo mora?",
   ["Na lagoa", "No telhado", "Na floresta", "No poço"], "Na lagoa",
   "A cantiga diz: 'Ele mora lá na lagoa, não lava o pé porque não quer'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "cantigas de roda", 1, 6, "Na cantiga 'Boi da cara preta', o boi vem pegar a criança que tem medo de careta.", True,
   "Os versos são 'Boi, boi, boi, boi da cara preta, pega essa criança que tem medo de careta'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "brincadeiras", 1, 6, "Qual brincadeira é feita pulando num desenho de casas numeradas riscado no chão, até chegar ao 'céu'?",
   ["Amarelinha", "Pique-esconde", "Cabra-cega", "Passa-anel"], "Amarelinha",
   "Na amarelinha, a criança joga uma pedrinha numa casa e pula com um pé só pelas outras.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "brincadeiras", 1, 6, "Qual brinquedo de origem indígena tem penas e é rebatido com a palma da mão?",
   ["Peteca", "Bilboquê", "Ioiô", "Pião"], "Peteca",
   "A peteca já era usada pelos povos indígenas antes da chegada dos portugueses; o nome vem do tupi e quer dizer 'bater'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "brincadeiras", 1, 6, "Qual brincadeira usa pequenas bolinhas de vidro coloridas, lançadas com a ponta do dedo?",
   ["Bolinha de gude", "Pião", "Peteca", "Pipa"], "Bolinha de gude",
   "No jogo de bolinha de gude, cada jogador tenta acertar as bolinhas dos outros com um peteleco.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "brincadeiras", 1, 6, "Na brincadeira de cabra-cega, quem tenta pegar os outros fica de olhos vendados.", True,
   "Com os olhos tapados por um pano, a 'cabra-cega' precisa encontrar e reconhecer os colegas.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cultura indígena", 1, 6, "Como se chama a casa tradicional de muitos povos indígenas brasileiros, feita de madeira e palha?",
   ["Oca", "Iglu", "Castelo", "Chalé"], "Oca",
   "Oca é uma palavra tupi; em muitas aldeias, várias famílias moram juntas na mesma oca.",
   "Funai – Fundação Nacional dos Povos Indígenas", br=True)
mc(T, "cultura indígena", 1, 7, "Como se chama o enfeite de penas que muitos indígenas usam na cabeça?",
   ["Cocar", "Turbante", "Boné", "Coroa de flores"], "Cocar",
   "Os cocares são feitos com penas de aves e têm cores e formatos diferentes em cada povo.",
   "Funai – Fundação Nacional dos Povos Indígenas", br=True)
mc(T, "cultura indígena", 1, 7, "Qual objeto de origem indígena serve para deitar e balançar, preso em dois ganchos na parede?",
   ["Rede", "Esteira", "Colchão", "Cadeira"], "Rede",
   "Os portugueses conheceram a rede de dormir com os indígenas e o costume se espalhou por todo o Brasil.",
   "Câmara Cascudo – Rede de Dormir", br=True)
tf(T, "símbolos nacionais", 1, 7, "Durante o Hino Nacional, o costume é ficar de pé e em silêncio.", True,
   "A Lei dos Símbolos Nacionais pede atitude de respeito, de pé e em silêncio, durante a execução do hino.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", br=True)
mc(T, "brincadeiras", 1, 7, "Qual brincadeira com bola tem dois times que tentam acertar os adversários para tirá-los do jogo?",
   ["Queimada", "Amarelinha", "Pega-pega", "Cabra-cega"], "Queimada",
   "Na queimada, quem é atingido pela bola fica 'queimado' e vai para o fundo do campo adversário.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "brincadeiras", 1, 8, "Qual brincadeira usa um barbante enrolado nos dedos para formar desenhos, passando de mão em mão?", "Cama de gato",
   ["cama de gato", "cama-de-gato"],
   "A cama de gato é brincada em muitos povos do mundo, e cada troca de mãos forma uma figura nova.",
   "Enciclopédia Britannica – verbete 'Cat's cradle'", br=True)
mc(T, "cantigas de roda", 1, 8, "Na cantiga 'Escravos de Jó', qual é o nome do jogo que eles jogavam?",
   ["Caxangá", "Peteca", "Amarelinha", "Dominó"], "Caxangá",
   "A cantiga começa com 'Escravos de Jó jogavam caxangá' e é brincada passando objetos de mão em mão no ritmo.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "festas juninas", 1, 8, "Qual dança de festa junina tem comandos como 'olha a chuva', 'é mentira' e 'anarriê'?",
   ["Quadrilha", "Ciranda", "Frevo", "Catira"], "Quadrilha",
   "A quadrilha veio de uma dança de salão europeia, e muitos comandos são palavras francesas aportuguesadas.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "símbolos nacionais", 1, 8, "Na faixa da bandeira do Brasil está escrito 'Independência ou Morte'.", False,
   "Na faixa branca da bandeira está escrito o lema positivista 'Ordem e Progresso'.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", br=True)
tf(T, "cultura indígena", 1, 8, "Todos os povos indígenas do Brasil falam a mesma língua.", False,
   "O Censo 2022 do IBGE registrou 295 línguas indígenas faladas no Brasil.",
   "IBGE – Censo Demográfico 2022", br=True, ref="2026-10-13")
mc(T, "danças regionais", 1, 9, "Qual objeto colorido os passistas de frevo seguram enquanto dançam?",
   ["Sombrinha", "Leque", "Pandeiro", "Lenço"], "Sombrinha",
   "A pequena sombrinha colorida ajuda o passista a se equilibrar nos passos acrobáticos do frevo.",
   "IPHAN – Frevo", br=True)
op(T, "carnaval", 1, 9, "Como se chama o rei do Carnaval, que recebe a chave da cidade do prefeito?", "Rei Momo",
   ["rei momo", "momo"],
   "O nome vem de Momo, o deus grego do sarcasmo e da zombaria.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "falares regionais", 1, 9, "'Oxente' é uma expressão de espanto típica do falar gaúcho.", False,
   "'Oxente', também dito 'oxe', é marca do falar nordestino, muito ouvida na Bahia e em Pernambuco.",
   "Dicionário Houaiss – verbete 'oxente'", br=True)
mc(T, "falares regionais", 1, 10, "Qual expressão de surpresa é típica do jeito de falar gaúcho?",
   ["Bah", "Uai", "Oxente", "Égua"], "Bah",
   "'Bah' serve para quase tudo no Rio Grande do Sul: espanto, alegria ou indignação.",
   "Dicionário Houaiss – verbete 'bah'", br=True)
op(T, "símbolos nacionais", 1, 10, "No Hino Nacional, o Brasil é chamado de 'gigante pela própria' o quê?", "Natureza",
   ["natureza"],
   "O verso 'Gigante pela própria natureza' fala do tamanho e das riquezas naturais do país.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", br=True)
op(T, "cultura indígena", 1, 10, "Qual semente vermelha muitos povos indígenas usam para pintar o corpo?", "Urucum",
   ["urucum", "urucu"],
   "O urucum dá uma tinta vermelha que também protege a pele do sol e dos insetos.",
   "Embrapa – Urucum", br=True)
mc(T, "religiosidade popular", 1, 10, "Qual santo junino é conhecido como o 'santo casamenteiro'?",
   ["Santo Antônio", "São João", "São Pedro", "São Jorge"], "Santo Antônio",
   "Santo Antônio, festejado em 13 de junho, é procurado por quem quer arrumar namorado.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "brincadeiras", 1, 10, "Qual brinquedo tem uma bola furada presa por um cordão a um bastão, e o desafio é encaixar uma no outro?",
   ["Bilboquê", "Ioiô", "Pião", "Peteca"], "Bilboquê",
   "O bilboquê exige pontaria: é preciso jogar a bola para cima e encaixá-la na ponta do bastão.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "religiosidade popular", 1, 10, "Segundo a tradição, quantos nós se dão na fitinha do Senhor do Bonfim, fazendo um pedido em cada?", "3",
   ["3", "três", "tres"],
   "Diz a tradição que os três pedidos se realizam quando a fitinha arrebenta sozinha.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)

# ================================================== MÉDIAS
mc(T, "danças regionais", 2, 10, "Qual instrumento parecido com um tambor, tocado com as mãos, acompanha a capoeira e o candomblé?",
   ["Atabaque", "Sanfona", "Flauta", "Violão"], "Atabaque",
   "O atabaque é um tambor alto e estreito, de origem africana, coberto com couro.",
   "IPHAN – Roda de Capoeira", br=True)
mc(T, "costumes regionais", 2, 10, "Como se chama o barco de pesca de troncos ou tábuas, com vela triangular, usado no litoral do Nordeste?",
   ["Jangada", "Gôndola", "Caravela", "Canoa a remo"], "Jangada",
   "As jangadas saem das praias do Ceará e de outros estados para a pesca em alto-mar.",
   "Câmara Cascudo – Jangada", br=True)
tf(T, "cultura indígena", 2, 10, "O Dia dos Povos Indígenas é comemorado em 19 de abril.", True,
   "Em 2022, a data antes chamada de 'Dia do Índio' passou a se chamar Dia dos Povos Indígenas.",
   "Lei nº 14.402/2022", br=True)
mc(T, "festas populares", 2, 10, "A Folia de Reis homenageia quais personagens da história do Natal?",
   ["Os Reis Magos", "Os pastores", "Os anjos", "Os apóstolos"], "Os Reis Magos",
   "Os foliões cantam de casa em casa lembrando a viagem dos Magos até o Menino Jesus.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "costumes regionais", 2, 10, "O chimarrão gaúcho é preparado com água gelada.", False,
   "O chimarrão leva água quente; a versão gelada da erva-mate é o tereré.",
   "Embrapa – Erva-mate", br=True)
op(T, "carnaval", 2, 12, "Como se chamam as músicas animadas de Carnaval, como 'Mamãe eu quero' e 'Cidade Maravilhosa'?", "Marchinhas",
   ["marchinhas", "marchinha", "marchinhas de carnaval", "marchas", "marcha"],
   "As marchinhas fizeram sucesso nos bailes e blocos de rua a partir dos anos 1920 e 1930.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(T, "religiosidade popular", 2, 12, "Qual santo é festejado em 29 de junho, encerrando o ciclo das festas juninas?",
   ["São Pedro", "São João", "Santo Antônio", "São Sebastião"], "São Pedro",
   "São Pedro, padroeiro dos pescadores, fecha as festas juninas no fim do mês.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "festas populares", 2, 12, "No Festival de Parintins, qual é a cor do boi Garantido?",
   ["Vermelho", "Azul", "Verde", "Amarelo"], "Vermelho",
   "O Garantido é vermelho e branco, e seu rival, o Caprichoso, é azul e branco.",
   "IPHAN – Complexo Cultural do Boi Bumbá do Médio Amazonas e Parintins", br=True)
mc(T, "festas populares", 2, 12, "No Círio de Nazaré, milhares de promesseiros seguram e puxam o que, junto da berlinda da santa?",
   ["Uma corda", "Uma bandeira", "Um andor de flores", "Uma fita dourada"], "Uma corda",
   "A corda do Círio, com centenas de metros, é disputada pelos fiéis que pagam promessas.",
   "IPHAN – Círio de Nossa Senhora de Nazaré", br=True)
mc(T, "festas populares", 2, 12, "Qual é o símbolo do Divino Espírito Santo, que aparece nas bandeiras vermelhas da Festa do Divino?",
   ["Uma pomba branca", "Um peixe", "Uma estrela", "Um cordeiro"], "Uma pomba branca",
   "Na tradição cristã, o Espírito Santo é representado por uma pomba.",
   "IPHAN – Festa do Divino Espírito Santo de Pirenópolis", br=True)
tf(T, "festas populares", 2, 12, "As Folias de Reis costumam visitar as casas entre o Carnaval e a Páscoa.", False,
   "O ciclo da Folia de Reis costuma ir do Natal até 6 de janeiro, o Dia de Reis.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(T, "religiosidade popular", 2, 12, "Na Lavagem do Bonfim, em Salvador, as baianas lavam as escadarias da igreja com água de cheiro.", True,
   "A Lavagem acontece em janeiro e reúne fé católica e tradições afro-brasileiras.",
   "IPHAN – Festa do Senhor Bom Jesus do Bonfim", br=True)
mc(T, "danças regionais", 2, 12, "Qual dança do sertão nordestino, ligada aos cangaceiros, tem nome que imita o barulho das sandálias arrastando no chão?",
   ["Xaxado", "Frevo", "Carimbó", "Catira"], "Xaxado",
   "Os cangaceiros dançavam o xaxado arrastando as alpercatas, num som de 'xa-xa-xa'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "danças regionais", 2, 12, "Qual dança de roda, famosa na Ilha de Itamaracá, em Pernambuco, é dançada de mãos dadas num grande círculo?",
   ["Ciranda", "Xaxado", "Frevo", "Catira"], "Ciranda",
   "A cirandeira Lia de Itamaracá tornou-se o maior símbolo dessa dança praieira.",
   "Fundação Joaquim Nabuco – Ciranda", br=True)
mc(T, "artesanato", 2, 12, "Qual renda é feita sobre uma almofada, trocando rapidamente pequenos carretéis de madeira?",
   ["Renda de bilro", "Crochê", "Tricô", "Ponto-cruz"], "Renda de bilro",
   "Os bilros são as pecinhas de madeira que as rendeiras do Nordeste trocam de lugar para trançar a linha.",
   "Fundação Joaquim Nabuco – Pesquisa Escolar: Renda de bilro", br=True)
mc(T, "artesanato", 2, 12, "As carrancas, esculturas de cabeças assustadoras colocadas na frente dos barcos, são típicas de qual rio?",
   ["São Francisco", "Amazonas", "Tietê", "Paraná"], "São Francisco",
   "Segundo a crença dos barqueiros, as carrancas espantavam os maus espíritos das águas do Velho Chico.",
   "Fundação Joaquim Nabuco – Pesquisa Escolar: Carrancas", br=True)
mc(T, "religiosidade popular", 2, 12, "Como se chama o templo onde se pratica o candomblé?",
   ["Terreiro", "Sinagoga", "Mesquita", "Mosteiro"], "Terreiro",
   "O Terreiro da Casa Branca, em Salvador, foi o primeiro templo afro-brasileiro tombado pelo IPHAN, nos anos 1980.",
   "IPHAN – Terreiro da Casa Branca", br=True)
mc(T, "religiosidade popular", 2, 12, "Como se chama a pessoa que, na tradição popular, reza com um raminho de folhas contra quebranto e mau-olhado?",
   ["Benzedeira", "Parteira", "Rendeira", "Doceira"], "Benzedeira",
   "As benzedeiras usam rezas e ramos de plantas como arruda e alecrim.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "manifestações populares", 2, 12, "Como se chama o desafio de versos improvisados entre dois cantadores com viola, no Nordeste?",
   ["Repente", "Modinha", "Lundu", "Toada"], "Repente",
   "No repente, cada cantador tem de responder ao outro na hora, rimando e seguindo a métrica.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=("cantoria", "cantoria de viola"), br=True)
op(T, "personagens", 2, 12, "Qual era o apelido de Virgulino Ferreira da Silva, o mais famoso cangaceiro do sertão?", "Lampião",
   ["lampião", "lampiao"],
   "Lampião e seu bando percorreram o sertão nordestino até 1938, quando ele morreu em Sergipe.",
   "Fundação Joaquim Nabuco – Lampião", br=True)
mc(T, "patrimônio", 2, 12, "O modo artesanal de fazer queijo, registrado como patrimônio cultural pelo IPHAN em 2008, é tradição de qual estado?",
   ["Minas Gerais", "Rio Grande do Sul", "Pernambuco", "Pará"], "Minas Gerais",
   "Regiões como a Serra da Canastra e o Serro guardam receitas de queijo passadas de geração em geração.",
   "IPHAN – Modo Artesanal de Fazer Queijo de Minas", br=True)
tf(T, "patrimônio", 2, 12, "Em 2014, a roda de capoeira entrou na lista de patrimônios imateriais da UNESCO.", True,
   "A UNESCO reconheceu a roda de capoeira como Patrimônio Cultural Imaterial da Humanidade em novembro de 2014.",
   "UNESCO – Capoeira circle", br=True)

# ================================================== DIFÍCEIS
mc(T, "cultura indígena", 3, 14, "Qual povo indígena vive entre Roraima e o Amazonas, e também tem aldeias na Venezuela?",
   ["Yanomami", "Pataxó", "Kaingang", "Terena"], "Yanomami",
   "A Terra Indígena Yanomami, coberta pela floresta amazônica, é uma das maiores do Brasil.",
   "Instituto Socioambiental – Povos Indígenas no Brasil", syn=("ianomâmi",), br=True)
mc(T, "símbolos nacionais", 3, 14, "Quem escreveu a letra do Hino Nacional Brasileiro?",
   ["Joaquim Osório Duque Estrada", "Olavo Bilac", "Castro Alves", "Gonçalves Dias"], "Joaquim Osório Duque Estrada",
   "A letra de Osório Duque Estrada foi escolhida para a música de Francisco Manuel da Silva.",
   "Academia Brasileira de Letras – Osório Duque-Estrada", syn=("osório duque estrada", "duque estrada"), br=True)
mc(T, "patrimônio", 3, 14, "Qual foi a primeira cidade brasileira declarada Patrimônio Mundial pela UNESCO, em 1980?",
   ["Ouro Preto", "Olinda", "Salvador", "Paraty"], "Ouro Preto",
   "A antiga Vila Rica, centro do ciclo do ouro, abriu a lista brasileira de Patrimônios Mundiais.",
   "UNESCO – Historic Town of Ouro Preto", br=True)
mc(T, "patrimônio", 3, 14, "Qual órgão federal cuida do patrimônio histórico do Brasil, tombando prédios e registrando tradições?",
   ["IPHAN", "IBGE", "INPE", "Embrapa"], "IPHAN",
   "O Instituto do Patrimônio Histórico e Artístico Nacional foi criado em 1937, com o nome de SPHAN.",
   "IPHAN – Institucional", syn=("instituto do patrimônio histórico e artístico nacional",), br=True)
mc(T, "carnaval", 3, 14, "Qual bloco de Recife entrou para o Guinness como o maior bloco de carnaval do mundo?",
   ["Galo da Madrugada", "Cordão da Bola Preta", "Filhos de Gandhy", "Bloco da Lama"], "Galo da Madrugada",
   "O Galo da Madrugada desfila no Sábado de Zé Pereira e arrasta multidões pelo centro do Recife.",
   "Guinness World Records", br=True)
mc(T, "danças regionais", 3, 14, "Qual dança caipira tem filas de dançarinos que batem palmas e sapateiam ao som da viola?",
   ["Catira", "Xote", "Frevo", "Ciranda"], "Catira",
   "A catira, também chamada de cateretê, é forte no interior de Goiás, Minas Gerais e São Paulo.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=("cateretê",), br=True)
mc(T, "danças regionais", 3, 14, "Qual dança afro-brasileira do Sudeste, com tambores e versos chamados 'pontos', é considerada uma das raízes do samba?",
   ["Jongo", "Xote", "Vanerão", "Catira"], "Jongo",
   "O jongo foi registrado como patrimônio cultural do Brasil pelo IPHAN em 2005.",
   "IPHAN – Jongo no Sudeste", br=True)
mc(T, "trajes típicos", 3, 14, "Como se chama o traje típico gaúcho, com bombacha, lenço e botas?",
   ["Pilcha", "Gibão", "Abadá", "Bata"], "Pilcha",
   "No Rio Grande do Sul, a pilcha é reconhecida por lei estadual como traje de honra.",
   "Movimento Tradicionalista Gaúcho – Pilcha", br=True)
mc(T, "trajes típicos", 3, 14, "Como se chama o casaco de couro que o vaqueiro nordestino usa para se proteger dos espinhos da caatinga?",
   ["Gibão", "Poncho", "Pala", "Colete de lã"], "Gibão",
   "O vaqueiro se veste de couro da cabeça aos pés: chapéu, gibão, perneiras e luvas.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "festas populares", 3, 14, "Qual festa afro-brasileira coroa reis do Congo e homenageia Nossa Senhora do Rosário e São Benedito?",
   ["Congada", "Cavalhada", "Quadrilha", "Pastoril"], "Congada",
   "As congadas são muito fortes em Minas Gerais, Goiás e São Paulo, com cortejos, tambores e coroações.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=("congado",), br=True)
tf(T, "cultura indígena", 3, 14, "Os povos indígenas usam o fruto do jenipapo para fazer pinturas vermelhas no corpo.", False,
   "A tinta do jenipapo verde fica preta-azulada na pele; o vermelho vem do urucum.",
   "Embrapa – Jenipapo", br=True)
tf(T, "patrimônio", 3, 14, "O centro histórico de Olinda é reconhecido pela UNESCO como Patrimônio Mundial.", True,
   "Olinda entrou na lista de Patrimônio Mundial da UNESCO em 1982.",
   "UNESCO – Historic Centre of the Town of Olinda", br=True)
mc(T, "falares regionais", 3, 14, "Qual palavra, usada para espanto, alegria ou raiva, é marca do falar paraense?",
   ["Égua", "Bah", "Uai", "Tchê"], "Égua",
   "No Pará, 'égua!' pode significar quase tudo, dependendo da entonação.",
   "Dicionário Houaiss – verbete 'égua'", br=True)

# ================================================== MUITO DIFÍCEIS
mc(T, "símbolos nacionais", 4, 16, "Quem compôs a música do Hino da Independência do Brasil?",
   ["Dom Pedro I", "Carlos Gomes", "Heitor Villa-Lobos", "Chiquinha Gonzaga"], "Dom Pedro I",
   "O imperador era músico e compôs a melodia; a letra é do jornalista Evaristo da Veiga.",
   "Enciclopédia Itaú Cultural", syn=("pedro i", "d. pedro i"), br=True)
tf(T, "símbolos nacionais", 4, 16, "A letra do Hino Nacional Brasileiro foi oficializada em 1922, no centenário da Independência.", True,
   "A música era tocada desde o século XIX, mas a letra de Osório Duque Estrada só foi oficializada em 6 de setembro de 1922.",
   "Decreto nº 15.671/1922 – Hino Nacional", br=True)
mc(T, "patrimônio", 4, 16, "O Cais do Valongo, antigo porto de chegada de africanos escravizados e Patrimônio Mundial, fica em qual cidade?",
   ["Rio de Janeiro", "Salvador", "Recife", "São Luís"], "Rio de Janeiro",
   "Redescoberto em obras de 2011, o cais entrou na lista da UNESCO em 2017.",
   "UNESCO – Valongo Wharf Archaeological Site", br=True)
mc(T, "danças regionais", 4, 16, "Qual dança afro-brasileira do Maranhão, em louvor a São Benedito, tem a 'punga', uma umbigada entre as dançarinas?",
   ["Tambor de crioula", "Carimbó", "Xaxado", "Fandango"], "Tambor de crioula",
   "O tambor de crioula foi registrado como patrimônio cultural do Brasil pelo IPHAN em 2007.",
   "IPHAN – Tambor de Crioula do Maranhão", br=True)
mc(T, "danças regionais", 4, 16, "No maracatu rural, qual personagem usa uma longa lança enfeitada e uma enorme cabeleira de tiras coloridas e brilhantes?",
   ["Caboclo de lança", "Mestre-sala", "Pierrô", "Rei Momo"], "Caboclo de lança",
   "O caboclo de lança, da Zona da Mata pernambucana, carrega chocalhos nas costas que soam a cada passo.",
   "IPHAN – Maracatu de Baque Solto", br=True)
mc(T, "religiosidade popular", 4, 16, "Como se chamam os objetos, como pernas e cabeças de cera, deixados em igrejas para agradecer uma graça?",
   ["Ex-votos", "Relicários", "Andores", "Escapulários"], "Ex-votos",
   "Salas de milagres ou de promessas, como a do Santuário de Aparecida, guardam milhares de ex-votos.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=("ex-voto", "ex voto", "ex votos"), br=True)
