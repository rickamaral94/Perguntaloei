# Perguntas novas: televisão. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "tv"

# =========================================================== FÁCEIS
mc(T, "desenhos clássicos", 1, 6, "Qual pássaro de topete vermelho dos desenhos tem uma risada famosa e vive aprontando?",
   ["Pica-Pau", "Piu-Piu", "Papa-Léguas", "Patolino"], "Pica-Pau",
   "O Pica-Pau foi criado pelo animador americano Walter Lantz em 1940.",
   "Enciclopédia Britannica – verbete 'Woody Woodpecker'")
mc(T, "desenhos clássicos", 1, 6, "Que animal vive tentando pegar o Papa-Léguas, sem nunca conseguir?",
   ["Coiote", "Lobo", "Raposa", "Gato"], "Coiote",
   "O Coiote usa armadilhas da empresa Acme, mas elas sempre dão errado.",
   "Enciclopédia Britannica – verbete 'Road Runner and Wile E. Coyote'")
mc(T, "desenhos clássicos", 1, 6, "Qual marinheiro dos desenhos fica muito forte depois de comer espinafre?",
   ["Popeye", "Brutus", "Pernalonga", "Fred Flintstone"], "Popeye",
   "Popeye nasceu nos quadrinhos americanos em 1929 e depois virou desenho animado.",
   "Enciclopédia Britannica – verbete 'Popeye'")
mc(T, "desenhos atuais", 1, 6, "De que cor é a roupa do Pocoyo?",
   ["Azul", "Vermelha", "Verde", "Amarela"], "Azul",
   "O menino Pocoyo usa macacão e touca azuis e brinca com a pata Pato e a elefanta Elly.",
   "Enciclopédia Britannica – verbete 'Pocoyo'")
mc(T, "desenhos atuais", 1, 6, "Que animal é a Bluey, do desenho australiano?",
   ["Cachorrinha", "Gatinha", "Coelhinha", "Ursinha"], "Cachorrinha",
   "Bluey é uma filhote de cão da raça boiadeiro australiano, de pelo azulado.",
   "ABC Kids – série 'Bluey'")
tf(T, "desenhos clássicos", 1, 6, "No desenho 'Tom e Jerry', o Tom é o rato.", False,
   "Tom é o gato e Jerry é o ratinho esperto que sempre escapa dele.",
   "Enciclopédia Britannica – verbete 'Tom and Jerry'")
mc(T, "desenhos clássicos", 1, 7, "Qual personagem de desenho é um felino magro e cor-de-rosa que nunca fala?",
   ["Pantera Cor-de-Rosa", "Frajola", "Garfield", "Manda-Chuva"], "Pantera Cor-de-Rosa",
   "A Pantera Cor-de-Rosa surgiu na abertura de um filme de 1963 e ganhou desenhos próprios.",
   "Enciclopédia Britannica – verbete 'The Pink Panther'")
op(T, "desenhos clássicos", 1, 7, "Qual gato laranja dos desenhos e quadrinhos adora lasanha e odeia segunda-feira?",
   "Garfield", ["garfield"],
   "Garfield foi criado pelo cartunista americano Jim Davis em 1978.",
   "Enciclopédia Britannica – verbete 'Garfield'")
mc(T, "desenhos clássicos", 1, 6, "No desenho 'Os Flintstones', como se chama o pai da família?",
   ["Fred", "Barney", "George", "Homer"], "Fred",
   "Fred Flintstone é casado com Wilma e trabalha numa pedreira.",
   "Enciclopédia Britannica – verbete 'The Flintstones'")
mc(T, "programas infantis", 1, 8, "Qual monstro azul da 'Vila Sésamo' é louco por biscoitos?",
   ["Come-Come", "Garibaldo", "Caco", "Elmo"], "Come-Come",
   "O Come-Come é a versão brasileira do Cookie Monster, da 'Sesame Street' americana.",
   "Enciclopédia Britannica – verbete 'Sesame Street'")
mc(T, "programas infantis", 1, 8, "Qual sapo verde é o apresentador e líder dos Muppets?",
   ["Caco", "Gonzo", "Fozzie", "Garibaldo"], "Caco",
   "O sapo Caco, chamado Kermit em inglês, foi criado pelo bonequeiro Jim Henson.",
   "Enciclopédia Britannica – verbete 'Kermit the Frog'")
mc(T, "desenhos atuais", 1, 7, "Qual desenho mostra um menino de dez anos que vira alienígenas usando um relógio?",
   ["Ben 10", "Danny Phantom", "Jimmy Nêutron", "Kim Possible"], "Ben 10",
   "Ben Tennyson encontra o Omnitrix, aparelho que o transforma em vários alienígenas.",
   "Cartoon Network – série 'Ben 10'")
mc(T, "desenhos atuais", 1, 8, "Em 'Hora de Aventura', que animal é o Jake, melhor amigo do Finn?",
   ["Cachorro", "Gato", "Urso", "Coelho"], "Cachorro",
   "Jake é um cachorro mágico que consegue esticar e mudar o formato do corpo.",
   "Cartoon Network – série 'Hora de Aventura'")
op(T, "desenhos clássicos", 1, 7, "Qual é o nome do cachorro beagle do Charlie Brown?",
   "Snoopy", ["snoopy"],
   "Snoopy nasceu na tirinha 'Peanuts', de Charles Schulz, e ganhou vários desenhos na TV.",
   "Enciclopédia Britannica – verbete 'Peanuts'")
tf(T, "desenhos atuais", 1, 8, "No desenho 'Bob Esponja', o Lula Molusco é vizinho do Bob Esponja.", True,
   "A casa do Lula Molusco, em forma de cabeça de pedra, fica entre o abacaxi do Bob e a pedra do Patrick.",
   "Nickelodeon – série 'Bob Esponja Calça Quadrada'")
mc(T, "desenhos clássicos", 1, 8, "Qual bruxo malvado vive tentando capturar os Smurfs?",
   ["Gargamel", "Mumm-Ra", "Esqueleto", "Dr. Robotnik"], "Gargamel",
   "Gargamel mora num casebre com o gato Cruel e nunca consegue pegar os Smurfs.",
   "Enciclopédia Britannica – verbete 'Smurfs'")
mc(T, "desenhos clássicos", 1, 7, "Nos Smurfs, como se chama o líder da vila, que usa roupa vermelha?",
   ["Papai Smurf", "Smurfette", "Ranzinza", "Gênio"], "Papai Smurf",
   "O Papai Smurf tem barba branca e é o mais velho e sábio da vila.",
   "Enciclopédia Britannica – verbete 'Smurfs'")
tf(T, "desenhos clássicos", 1, 8, "O Patolino, dos desenhos 'Looney Tunes', é um pato preto.", True,
   "Patolino, chamado Daffy Duck em inglês, é o pato preto e atrapalhado da Warner Bros.",
   "Enciclopédia Britannica – verbete 'Daffy Duck'")
mc(T, "desenhos clássicos", 1, 9, "Qual menino gênio de desenho tem um laboratório secreto que esconde da irmã Dee Dee?",
   ["Dexter", "Jimmy Nêutron", "Johnny Bravo", "Timmy Turner"], "Dexter",
   "'O Laboratório de Dexter' estreou no Cartoon Network em 1996.",
   "Cartoon Network – série 'O Laboratório de Dexter'")
op(T, "culinária na TV", 1, 9, "Qual era o nome do papagaio de pelúcia que fazia dupla com Ana Maria Braga na TV?",
   "Louro José", ["louro josé", "louro jose"],
   "O boneco Louro José era animado e dublado pelo ator Tom Veiga.",
   "Memória Globo – programa 'Mais Você'", br=True)
op(T, "programas infantis", 1, 10, "Como eram chamadas as jovens assistentes de palco da Xuxa?",
   "Paquitas", ["paquitas", "paquita", "as paquitas"],
   "As Paquitas dançavam e ajudavam a Xuxa nos programas infantis desde os anos 1980.",
   "Memória Globo – programa 'Xou da Xuxa'", br=True)
op(T, "grade de programação", 1, 10, "Como se chama a tradicional faixa de filmes exibida à tarde pela TV Globo?",
   "Sessão da Tarde", ["sessão da tarde", "sessao da tarde"],
   "A 'Sessão da Tarde' exibe filmes leves para toda a família desde 1974.",
   "Memória Globo – 'Sessão da Tarde'", br=True)
tf(T, "desenhos clássicos", 1, 9, "O desenho 'Os Simpsons' é produzido no Japão.", False,
   "'Os Simpsons' é uma produção dos Estados Unidos, exibida desde 1989.",
   "Enciclopédia Britannica – verbete 'The Simpsons'")
tf(T, "desenhos clássicos", 1, 10, "O Pica-Pau é um personagem criado no Brasil.", False,
   "Ele foi criado nos Estados Unidos, mas fez tanto sucesso aqui que foi exibido por décadas na TV brasileira.",
   "Enciclopédia Britannica – verbete 'Woody Woodpecker'")
mc(T, "desenhos clássicos", 1, 10, "Qual herói de desenho erguia a espada e gritava 'Eu tenho a força!'?",
   ["He-Man", "Lion-O", "Capitão Planeta", "Batman"], "He-Man",
   "He-Man é o príncipe Adam, que se transforma ao invocar os poderes de Grayskull.",
   "Enciclopédia Britannica – verbete 'He-Man and the Masters of the Universe'")
tf(T, "programas infantis", 1, 10, "A 'Vila Sésamo' brasileira foi uma versão de um programa infantil norte-americano.", True,
   "A versão brasileira, de 1972, adaptou a 'Sesame Street', criada nos Estados Unidos em 1969.",
   "Enciclopédia Britannica – verbete 'Sesame Street'", br=True)
mc(T, "animes", 1, 10, "Em qual desenho japonês o protagonista é um ninja de cabelo amarelo que sonha em ser Hokage?",
   ["Naruto", "Dragon Ball", "One Piece", "Pokémon"], "Naruto",
   "Hokage é o título do líder da Vila da Folha, onde Naruto Uzumaki mora.",
   "Enciclopédia Britannica – verbete 'Naruto'")

# =========================================================== MÉDIAS
mc(T, "programas infantis", 2, 9, "Em 'Castelo Rá-Tim-Bum', qual é o nome da tia feiticeira do Nino?",
   ["Morgana", "Celeste", "Penélope", "Biba"], "Morgana",
   "A tia Morgana é uma feiticeira de milhares de anos que mora no castelo com o Nino e o tio Victor.",
   "TV Cultura – 'Castelo Rá-Tim-Bum'", br=True)
mc(T, "programas infantis", 2, 9, "Em 'Castelo Rá-Tim-Bum', qual personagem é o entregador de pizza?",
   ["Bongô", "Zequinha", "Pedro", "Etevaldo"], "Bongô",
   "Bongô vivia aparecendo no castelo para entregar pizzas.",
   "TV Cultura – 'Castelo Rá-Tim-Bum'", br=True)
mc(T, "desenhos atuais", 2, 8, "No desenho brasileiro 'O Show da Luna!', como se chama o irmão caçula da Luna?",
   ["Júpiter", "Cláudio", "Saturno", "Marte"], "Júpiter",
   "Luna faz experiências científicas com o irmão Júpiter e o furão Cláudio.",
   "TV Pinguim – 'O Show da Luna!'", br=True)
mc(T, "desenhos atuais", 2, 9, "Qual das Meninas Superpoderosas é ruiva, usa laço vermelho e lidera o trio?",
   ["Florzinha", "Lindinha", "Docinho", "Princesa"], "Florzinha",
   "Florzinha, Lindinha e Docinho foram criadas pelo Professor Utônio numa experiência.",
   "Cartoon Network – série 'As Meninas Superpoderosas'")
op(T, "animes", 2, 10, "Qual é o nome do protagonista de 'Dragon Ball', que tinha cauda de macaco quando criança?",
   "Goku", ["goku", "son goku"],
   "Goku é um guerreiro saiyajin criado pelo mangaká japonês Akira Toriyama.",
   "Enciclopédia Britannica – verbete 'Dragon Ball'")
mc(T, "programas infantis", 2, 10, "Qual grande pássaro amarelo era personagem da 'Vila Sésamo' brasileira?",
   ["Garibaldo", "Come-Come", "Elmo", "Caco"], "Garibaldo",
   "Garibaldo é a versão brasileira do Big Bird, da 'Sesame Street'.",
   "Memória Globo – programa 'Vila Sésamo'", br=True)
mc(T, "seriados latinos", 2, 10, "Qual é a arma mais famosa do Chapolin Colorado?",
   ["Marreta biônica", "Espada laser", "Laço dourado", "Escudo mágico"], "Marreta biônica",
   "A marreta biônica é um martelo de brinquedo amarelo e vermelho que o herói usa para se defender.",
   "Enciclopédia Britannica – verbete 'Roberto Gómez Bolaños'")
mc(T, "animes", 2, 12, "Qual desenho japonês mostra guerreiros com armaduras de constelações que protegem a deusa Atena?",
   ["Os Cavaleiros do Zodíaco", "Dragon Ball", "Naruto", "Sailor Moon"], "Os Cavaleiros do Zodíaco",
   "Seiya e seus amigos usam armaduras ligadas às constelações, como Pégaso e Dragão.",
   "Enciclopédia Britannica – verbete 'Saint Seiya'")
mc(T, "humorísticos", 2, 12, "Qual dos Trapalhões tinha o famoso bordão 'Cacildis'?",
   ["Mussum", "Didi", "Dedé", "Zacarias"], "Mussum",
   "Mussum colocava o final 'is' em várias palavras, criando um jeito de falar inconfundível.",
   "Memória Globo – programa 'Os Trapalhões'", br=True)
mc(T, "humorísticos", 2, 12, "Na 'Escolinha do Professor Raimundo', qual era o bordão do professor ao reclamar do que ganhava?",
   ["E o salário, ó!", "Ô loco, meu!", "Haja coração!", "Isso é uma vergonha!"], "E o salário, ó!",
   "Chico Anysio fazia um gesto com os dedos mostrando como o salário do professor era pequeno.",
   "Memória Globo – programa 'Escolinha do Professor Raimundo'", br=True)
mc(T, "programas infantis", 2, 12, "Qual apresentadora infantil ficou famosa com a música 'Os Dedinhos'?",
   ["Eliana", "Angélica", "Mara Maravilha", "Xuxa"], "Eliana",
   "A música 'Os Dedinhos' fez sucesso nos anos 1990, quando Eliana apresentava programas infantis.",
   "Dicionário Cravo Albin da Música Popular Brasileira – verbete 'Eliana'", br=True)
mc(T, "programas infantis", 2, 12, "Qual apresentadora infantil gravou o sucesso 'Vou de Táxi', em 1988?",
   ["Angélica", "Eliana", "Xuxa", "Mara Maravilha"], "Angélica",
   "'Vou de Táxi' é a versão brasileira da canção francesa 'Joe le taxi'.",
   "Dicionário Cravo Albin da Música Popular Brasileira – verbete 'Angélica'", br=True)
mc(T, "séries estrangeiras", 2, 12, "Qual personagem da Família Addams ganhou uma série própria na Netflix em 2022?",
   ["Wandinha", "Mortícia", "Feioso", "Tropeço"], "Wandinha",
   "Na série, Wandinha Addams estuda na escola Nunca Mais e investiga mistérios.",
   "Netflix – série 'Wandinha'")
mc(T, "reality shows", 2, 12, "No 'Big Brother Brasil', qual prova dá ao vencedor imunidade e o poder de indicar alguém ao paredão?",
   ["Prova do Líder", "Raio-X", "Repescagem", "Jogo da Discórdia"], "Prova do Líder",
   "O Líder da semana não pode ser votado e ganha um quarto especial na casa.",
   "Memória Globo – 'Big Brother Brasil'", br=True)
mc(T, "humorísticos", 2, 14, "Em 'A Grande Família', qual era a profissão de Agostinho Carrara?",
   ["Taxista", "Médico", "Professor", "Padeiro"], "Taxista",
   "Agostinho, vivido por Pedro Cardoso, era o genro malandro de Lineu e Nenê.",
   "Memória Globo – série 'A Grande Família'", br=True)
mc(T, "séries estrangeiras", 2, 14, "A série 'Todo Mundo Odeia o Chris' é inspirada na infância de qual comediante?",
   ["Chris Rock", "Eddie Murphy", "Will Smith", "Kevin Hart"], "Chris Rock",
   "Chris Rock também narra a série, que mostra sua adolescência no Brooklyn dos anos 1980.",
   "Enciclopédia Britannica – verbete 'Chris Rock'")
tf(T, "séries estrangeiras", 2, 12, "A série 'Friends' se passa em Londres.", False,
   "Os seis amigos de 'Friends' moram em Nova York, nos Estados Unidos.",
   "Enciclopédia Britannica – verbete 'Friends'")
tf(T, "séries estrangeiras", 2, 14, "A série 'Lost' começa com a queda de um avião numa ilha misteriosa.", True,
   "Os sobreviventes do voo 815 da Oceanic enfrentam os segredos da ilha ao longo de seis temporadas.",
   "Enciclopédia Britannica – verbete 'Lost'")
mc(T, "vinhetas e mascotes", 2, 14, "Como se chama a vinheta de Carnaval da TV Globo, com uma dançarina de samba?",
   ["Globeleza", "Sambalelê", "Carnavália", "Folia Brasil"], "Globeleza",
   "A vinheta da Globeleza, criada nos anos 1990, virou símbolo do Carnaval na TV.",
   "Memória Globo – 'Globeleza'", br=True)
mc(T, "programas esportivos", 2, 14, "Qual programa esportivo da Globo vai ao ar nas manhãs de domingo desde os anos 1970?",
   ["Esporte Espetacular", "Globo Esporte", "Jogo Aberto", "Os Donos da Bola"], "Esporte Espetacular",
   "O 'Esporte Espetacular' estreou em 1973 e mostra várias modalidades, não só futebol.",
   "Memória Globo – programa 'Esporte Espetacular'", br=True, ref="2026-10-13")
mc(T, "desenhos clássicos", 2, 14, "No desenho 'Caverna do Dragão', qual personagem guia os jovens e some misteriosamente?",
   ["Mestre dos Magos", "Vingador", "Uni", "Tiamat"], "Mestre dos Magos",
   "O pequeno Mestre dos Magos dá conselhos enigmáticos e desaparece logo em seguida.",
   "Enciclopédia Britannica – verbete 'Dungeons & Dragons'")
mc(T, "reality shows", 2, 14, "Qual reality show da Record confina famosos num ambiente rural, cuidando de animais?",
   ["A Fazenda", "Big Brother Brasil", "No Limite", "Casa dos Artistas"], "A Fazenda",
   "'A Fazenda' estreou em 2009 e os participantes cuidam de bichos e plantações.",
   "Record TV – programa 'A Fazenda'", br=True, ref="2026-10-13")
mc(T, "programas de variedades", 2, 14, "Qual programa da Globo mostrava bastidores da emissora e erros de gravação, de 1983 a 2019?",
   ["Vídeo Show", "Fantástico", "Mais Você", "Domingão"], "Vídeo Show",
   "O quadro de erros de gravação do 'Vídeo Show' ficou conhecido como 'Falha Nossa'.",
   "Memória Globo – programa 'Vídeo Show'", br=True)

# =========================================================== DIFÍCEIS
mc(T, "humorísticos", 3, 14, "Qual empresa fictícia vendia produtos absurdos nos quadros do 'Casseta & Planeta'?",
   ["Organizações Tabajara", "Empresas Acme", "Indústrias Pirulito", "Grupo Patropi"], "Organizações Tabajara",
   "Os comerciais falsos das Organizações Tabajara satirizavam as propagandas da TV.",
   "Memória Globo – programa 'Casseta & Planeta, Urgente!'", br=True)
mc(T, "programas infantis", 3, 14, "Qual cantor compôs e gravou a música de abertura do 'Sítio do Picapau Amarelo' de 1977?",
   ["Gilberto Gil", "Caetano Veloso", "Chico Buarque", "Toquinho"], "Gilberto Gil",
   "A canção 'Sítio do Picapau Amarelo', de Gilberto Gil, marcou gerações de crianças.",
   "Memória Globo – série 'Sítio do Picapau Amarelo' (1977)", br=True)
mc(T, "programas infantis", 3, 14, "Qual emissora exibiu a versão de 1977 do 'Sítio do Picapau Amarelo'?",
   ["TV Globo", "TV Tupi", "TV Cultura", "Rede Bandeirantes"], "TV Globo",
   "A série ficou no ar até 1986 e foi feita em parceria com a TVE.",
   "Memória Globo – série 'Sítio do Picapau Amarelo' (1977)", br=True)
mc(T, "programas de ciência", 3, 14, "Qual programa americano de ciência tinha um cientista de jaleco verde e um rato gigante chamado Lester?",
   ["O Mundo de Beakman", "Cosmos", "Mundo da Lua", "X-Tudo"], "O Mundo de Beakman",
   "Beakman respondia a perguntas de crianças com experiências malucas; no Brasil, passou na TV Cultura.",
   "TV Cultura – 'O Mundo de Beakman'")
mc(T, "desenhos clássicos", 3, 14, "Qual cartunista criou 'Os Simpsons'?",
   ["Matt Groening", "Seth MacFarlane", "Stephen Hillenburg", "Walt Disney"], "Matt Groening",
   "Matt Groening deu à família os nomes de parentes seus, como o pai Homer e a mãe Margaret.",
   "Enciclopédia Britannica – verbete 'Matt Groening'")
mc(T, "desenhos clássicos", 3, 14, "O estúdio de qual dupla de animadores produziu 'Os Flintstones' e 'Scooby-Doo'?",
   ["William Hanna e Joseph Barbera", "Walt Disney e Ub Iwerks", "Os irmãos Warner", "Matt Groening e Seth MacFarlane"],
   "William Hanna e Joseph Barbera",
   "Antes de fundar a Hanna-Barbera, a dupla criou 'Tom e Jerry' para a MGM.",
   "Enciclopédia Britannica – verbete 'Hanna-Barbera Productions'", syn=("hanna-barbera",))
tf(T, "programas de ciência", 3, 14, "A série 'Cosmos', de 1980, foi apresentada pelo astrônomo Carl Sagan.", True,
   "'Cosmos' explicava o Universo de forma simples e foi vista em dezenas de países.",
   "Enciclopédia Britannica – verbete 'Carl Sagan'")
tf(T, "história da TV", 3, 14, "A TV Tupi, primeira emissora do Brasil, foi inaugurada no Rio de Janeiro.", False,
   "A TV Tupi foi inaugurada em São Paulo, em 18 de setembro de 1950.",
   "Enciclopédia Britannica – verbete 'Assis Chateaubriand'", br=True)
op(T, "reality shows", 3, 14, "Qual reality show da Globo, de 2000, levava participantes a sobreviver em lugares selvagens?",
   "No Limite", ["no limite"],
   "A primeira temporada de 'No Limite' foi apresentada por Zeca Camargo.",
   "Memória Globo – programa 'No Limite'", br=True)
mc(T, "programas de auditório", 3, 14, "Qual apresentador ficou famoso pelos calouros e pelo quadro 'Pra quem você tira o chapéu?'.",
   ["Raul Gil", "Silvio Santos", "Chacrinha", "Gugu Liberato"], "Raul Gil",
   "No quadro, Raul Gil pedia aos convidados que dissessem a quem tirariam o chapéu.",
   "SBT – 'Programa Raul Gil'", br=True)
mc(T, "programas infantis", 3, 14, "Qual programa infantil da Globo, dos anos 1980, tinha a turma de Simony e Jairzinho?",
   ["Balão Mágico", "Xou da Xuxa", "TV Colosso", "Bambalalão"], "Balão Mágico",
   "O 'Balão Mágico' foi exibido de 1983 a 1986 e seu grupo musical também gravou discos de sucesso.",
   "Memória Globo – programa 'Balão Mágico'", br=True)
tf(T, "programas infantis", 3, 14, "O 'Castelo Rá-Tim-Bum' estreou na TV Cultura em 1994.", True,
   "A série teve 90 episódios e ganhou um filme em 1999.",
   "TV Cultura – 'Castelo Rá-Tim-Bum'", br=True)

# =========================================================== MUITO DIFÍCEIS
mc(T, "história da TV", 4, 16, "Em que ano a TV Tupi, pioneira da televisão brasileira, saiu do ar?",
   ["1980", "1975", "1985", "1990"], "1980",
   "A concessão da Tupi foi cassada pelo governo federal em julho de 1980, depois de uma grave crise financeira.",
   "Enciclopédia Britannica – verbete 'Assis Chateaubriand'", br=True)
mc(T, "história da TV", 4, 16, "Em que ano começaram as transmissões de TV digital aberta no Brasil?",
   ["2007", "2000", "2012", "2016"], "2007",
   "A primeira transmissão digital aberta foi em São Paulo, em 2 de dezembro de 2007.",
   "Agência Nacional de Telecomunicações (Anatel)", br=True)
mc(T, "vinhetas e mascotes", 4, 16, "Qual designer austríaco criou o logotipo da TV Globo usado desde os anos 1970?",
   ["Hans Donner", "Aloísio Magalhães", "Ziraldo", "Oscar Niemeyer"], "Hans Donner",
   "Hans Donner chegou ao Brasil em 1974 e também criou muitas vinhetas da emissora.",
   "Memória Globo – 'Hans Donner'", br=True)
tf(T, "história da TV", 4, 16, "A primeira transmissão oficial em cores da TV brasileira mostrou a Festa da Uva, em Caxias do Sul.", True,
   "A transmissão aconteceu em 19 de fevereiro de 1972, a partir da festa gaúcha.",
   "Ministério das Comunicações – história da televisão no Brasil", br=True)
tf(T, "humorísticos", 4, 16, "O programa 'Os Trapalhões' sempre foi exibido apenas pela TV Globo.", False,
   "Antes de chegar à Globo, em 1977, o grupo passou pela TV Excelsior e pela TV Tupi.",
   "Memória Globo – programa 'Os Trapalhões'", br=True)
mc(T, "reality shows", 4, 16, "Qual emissora exibiu a 'Casa dos Artistas', reality show de 2001 que disputou audiência com o 'Fantástico'?",
   ["SBT", "TV Globo", "Record", "Band"], "SBT",
   "Apresentada por Silvio Santos, a 'Casa dos Artistas' estreou meses antes do primeiro 'Big Brother Brasil'.",
   "SBT – programa 'Casa dos Artistas'", br=True)
