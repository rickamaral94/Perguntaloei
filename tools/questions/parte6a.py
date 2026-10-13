# Perguntas novas (parte 6a). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== GEOGRAFIA
G = "geo"
mc(G, "países", 1, 7, "Em qual país fica a Torre Eiffel?",
   ["França", "Itália", "Inglaterra", "Espanha"], "França",
   "A torre foi construída em Paris para a Exposição Universal de 1889.",
   "Enciclopédia Britannica – verbete 'Eiffel Tower'", syn=["franca"])
tf(G, "oceanos", 1, 6, "O litoral do Brasil é banhado pelo oceano Atlântico.", True,
   "São mais de 7 mil quilômetros de costa voltada para o Atlântico.",
   "IBGE – Brasil em Síntese", br=True)
mc(G, "paisagens", 1, 7, "Qual destes lugares é coberto de areia e quase não tem chuva?",
   ["Deserto", "Floresta", "Pântano", "Geleira"], "Deserto",
   "O Saara, no norte da África, é o maior deserto quente do mundo.",
   "Enciclopédia Britannica – verbete 'Desert'")
mc(G, "capitais", 1, 8, "Madri é a capital de qual país?",
   ["Espanha", "Portugal", "México", "Argentina"], "Espanha",
   "Madri fica bem no centro da Península Ibérica.",
   "Enciclopédia Britannica – verbete 'Madrid'")
mc(G, "estados", 1, 9, "Qual é a capital de Minas Gerais?",
   ["Belo Horizonte", "Uberlândia", "Juiz de Fora", "Ouro Preto"], "Belo Horizonte",
   "Belo Horizonte foi planejada e inaugurada em 1897 para substituir Ouro Preto.",
   "IBGE – Cidades", br=True)
tf(G, "fronteiras", 1, 9, "O Uruguai faz fronteira com o Brasil.", True,
   "O Uruguai faz divisa com o Rio Grande do Sul.",
   "IBGE – Brasil em Síntese", br=True)
mc(G, "rios", 2, 10, "Como se chama o lugar onde um rio deságua no mar?",
   ["Foz", "Nascente", "Margem", "Leito"], "Foz",
   "A nascente é onde o rio começa; a foz é onde ele termina.",
   "IBGE – Vocabulário Básico de Recursos Naturais")
mc(G, "estados", 2, 10, "Qual é a capital de Pernambuco?",
   ["Recife", "Olinda", "Caruaru", "João Pessoa"], "Recife",
   "Recife é cortada por rios e pontes, e por isso é chamada de 'Veneza brasileira'.",
   "IBGE – Cidades", br=True)
op(G, "estados", 2, 10, "Qual é a capital do Rio Grande do Sul?", "Porto Alegre", ["porto alegre"],
   "Porto Alegre fica às margens do lago Guaíba.", "IBGE – Cidades", br=True)
mc(G, "capitais", 2, 12, "Qual é a capital do Chile?",
   ["Santiago", "Valparaíso", "Lima", "Montevidéu"], "Santiago",
   "Santiago fica num vale aos pés da Cordilheira dos Andes.",
   "Enciclopédia Britannica – verbete 'Santiago'")
mc(G, "biomas", 2, 12, "Qual bioma ocupa quase metade do território brasileiro?",
   ["Amazônia", "Cerrado", "Caatinga", "Pampa"], "Amazônia",
   "A Amazônia brasileira tem a maior floresta tropical do mundo.",
   "IBGE – Biomas do Brasil", syn=["amazonia"], br=True)
mc(G, "biomas", 3, 14, "Qual bioma existe somente no Brasil e é típico do sertão nordestino?",
   ["Caatinga", "Cerrado", "Pampa", "Pantanal"], "Caatinga",
   "O nome vem do tupi e significa 'mata branca', pela vegetação clara na seca.",
   "IBGE – Biomas do Brasil", br=True)
mc(G, "rios", 3, 14, "Qual é o rio mais longo da Europa?",
   ["Volga", "Danúbio", "Reno", "Sena"], "Volga",
   "O Volga corre inteiramente pela Rússia e deságua no mar Cáspio.",
   "Enciclopédia Britannica – verbete 'Volga River'")
tf(G, "ilhas", 3, 14, "A Groenlândia é a maior ilha do mundo.", True,
   "A Austrália é maior, mas é considerada um continente.",
   "Enciclopédia Britannica – verbete 'Greenland'")
mc(G, "mares", 3, 14, "Qual estreito separa a Europa da África, entre a Espanha e o Marrocos?",
   ["Gibraltar", "Bósforo", "Magalhães", "Ormuz"], "Gibraltar",
   "No ponto mais estreito, os dois continentes ficam a cerca de 14 km um do outro.",
   "Enciclopédia Britannica – verbete 'Strait of Gibraltar'")
mc(G, "estados", 3, 14, "Qual é a capital do Tocantins?",
   ["Palmas", "Araguaína", "Gurupi", "Porto Nacional"], "Palmas",
   "Palmas foi planejada e fundada em 1989, sendo a capital mais jovem do país.",
   "IBGE – Cidades", br=True)
mc(G, "capitais", 4, 16, "Qual é a capital da Nova Zelândia?",
   ["Wellington", "Auckland", "Christchurch", "Camberra"], "Wellington",
   "Auckland é a maior cidade, mas a capital é Wellington.",
   "Enciclopédia Britannica – verbete 'Wellington'")
op(G, "lagos", 4, 16, "Qual é o lago mais profundo do mundo, que fica na Sibéria?", "Baikal",
   ["baikal", "baical", "lago baikal"],
   "O Baikal passa de 1.600 metros de profundidade e guarda cerca de 20% da água doce líquida de superfície do planeta.",
   "Enciclopédia Britannica – verbete 'Lake Baikal'")

# =========================================================== HISTÓRIA
H = "his"
mc(H, "antiguidade", 1, 7, "Como se chama o corpo preservado pelos antigos egípcios, enrolado em faixas de pano?",
   ["Múmia", "Estátua", "Esfinge", "Pirâmide"], "Múmia",
   "Os egípcios acreditavam que o corpo precisava ser preservado para a vida após a morte.",
   "Enciclopédia Britannica – verbete 'Mummy'", syn=["mumia"])
mc(H, "antiguidade", 1, 8, "Como eram chamados os reis do antigo Egito?",
   ["Faraós", "Césares", "Czares", "Sultões"], "Faraós",
   "Os faraós eram vistos como deuses vivos pelo seu povo.",
   "Enciclopédia Britannica – verbete 'Pharaoh'", syn=["faraos", "farao"])
mc(H, "brasil colônia", 1, 8, "Qual navegador comandou a frota portuguesa que chegou ao Brasil em 1500?",
   ["Pedro Álvares Cabral", "Vasco da Gama", "Cristóvão Colombo", "Fernão de Magalhães"], "Pedro Álvares Cabral",
   "A frota de Cabral estava a caminho da Índia quando chegou ao litoral da Bahia.",
   "Enciclopédia Britannica – verbete 'Pedro Álvares Cabral'", syn=["cabral"], br=True)
mc(H, "mundo", 1, 8, "Qual país construiu a Grande Muralha para se proteger de invasores?",
   ["China", "Japão", "Índia", "Mongólia"], "China",
   "A muralha foi erguida e reconstruída ao longo de muitos séculos e de várias dinastias.",
   "Enciclopédia Britannica – verbete 'Great Wall of China'")
mc(H, "século xx", 1, 9, "Qual navio famoso afundou em 1912 depois de bater num iceberg?",
   ["Titanic", "Queen Mary", "Lusitania", "Santa Maria"], "Titanic",
   "O Titanic afundou em sua primeira viagem, entre a Inglaterra e Nova York.",
   "Enciclopédia Britannica – verbete 'Titanic'")
tf(H, "brasil", 1, 8, "Brasília sempre foi a capital do Brasil.", False,
   "Antes de Brasília, as capitais foram Salvador e o Rio de Janeiro.",
   "IBGE – Brasil em Síntese", br=True)
tf(H, "idade média", 2, 10, "Os vikings eram povos navegadores do norte da Europa.", True,
   "Eles vinham da Escandinávia e chegaram até a América do Norte por volta do ano 1000.",
   "Enciclopédia Britannica – verbete 'Viking'")
mc(H, "antiguidade", 2, 10, "Qual povo antigo construiu o Coliseu?",
   ["Romanos", "Gregos", "Egípcios", "Persas"], "Romanos",
   "O Coliseu foi inaugurado no ano 80 e recebia lutas de gladiadores.",
   "Enciclopédia Britannica – verbete 'Colosseum'")
mc(H, "brasil colônia", 2, 10, "Qual árvore foi a primeira riqueza explorada pelos portugueses e deu nome ao país?",
   ["Pau-brasil", "Seringueira", "Jacarandá", "Ipê"], "Pau-brasil",
   "Da madeira vermelha do pau-brasil se extraía uma tinta usada para tingir tecidos.",
   "Enciclopédia Britannica – verbete 'Brazilwood'", syn=["pau brasil"], br=True)
mc(H, "mundo", 2, 12, "Em que ano começou a Primeira Guerra Mundial?",
   ["1914", "1918", "1905", "1939"], "1914",
   "O estopim foi o assassinato do arquiduque Francisco Ferdinando, em Sarajevo.",
   "Enciclopédia Britannica – verbete 'World War I'")
mc(H, "brasil colônia", 2, 12, "Qual riqueza descoberta em Minas Gerais, no fim do século 17, atraiu milhares de pessoas para a região?",
   ["Ouro", "Petróleo", "Café", "Prata"], "Ouro",
   "O ciclo do ouro fez surgir cidades como Ouro Preto e Mariana.",
   "Enciclopédia Britannica – verbete 'Minas Gerais'", br=True)
mc(H, "século xx", 3, 14, "Em que ano a missão Apollo 11 levou os primeiros astronautas a caminhar na Lua?",
   ["1969", "1957", "1961", "1975"], "1969",
   "A descida aconteceu em 20 de julho de 1969 e foi vista ao vivo por milhões de pessoas.",
   "NASA – Apollo 11 Mission Overview")
mc(H, "brasil império", 3, 14, "Qual produto da Amazônia gerou um grande ciclo econômico no fim do século 19?",
   ["Borracha", "Algodão", "Cacau", "Açúcar"], "Borracha",
   "A riqueza da borracha financiou o Teatro Amazonas, em Manaus.",
   "Enciclopédia Britannica – verbete 'Manaus'", br=True)
tf(H, "século xx", 3, 14, "O Brasil enviou soldados para lutar na Itália durante a Segunda Guerra Mundial.", True,
   "A Força Expedicionária Brasileira combateu na Itália em 1944 e 1945.",
   "Exército Brasileiro – Força Expedicionária Brasileira", br=True)
mc(H, "república", 3, 14, "Que tipo de regime governou o Brasil de 1964 a 1985?",
   ["Regime militar", "Monarquia", "Parlamentarismo", "Regime colonial"], "Regime militar",
   "O período terminou com a eleição indireta de um presidente civil, em 1985.",
   "Arquivo Nacional – Memórias Reveladas", syn=["ditadura militar", "ditadura"], br=True)
mc(H, "idade média", 3, 16, "Qual era a capital do Império Bizantino?",
   ["Constantinopla", "Roma", "Atenas", "Alexandria"], "Constantinopla",
   "A cidade foi tomada pelos turcos otomanos em 1453 e hoje se chama Istambul.",
   "Enciclopédia Britannica – verbete 'Byzantine Empire'")
mc(H, "antiguidade", 4, 16, "Em que ano caiu o Império Romano do Ocidente?",
   ["476", "1453", "800", "1066"], "476",
   "Nesse ano o último imperador, Rômulo Augústulo, foi deposto.",
   "Enciclopédia Britannica – verbete 'Fall of Rome'")
op(H, "brasil império", 4, 16, "Qual revolta gaúcha durou dez anos, de 1835 a 1845?", "Revolução Farroupilha",
   ["farroupilha", "revolucao farroupilha", "guerra dos farrapos", "farrapos"],
   "O 20 de setembro, início da revolta, é feriado no Rio Grande do Sul.",
   "Enciclopédia Britannica – verbete 'Farrapos War'", br=True)

# =========================================================== POLÍTICA
P = "pol"
mc(P, "cidadania", 1, 7, "Numa eleição, como escolhemos nossos governantes?",
   ["Pelo voto", "Por sorteio", "Por herança", "Por idade"], "Pelo voto",
   "O voto é a forma de cada cidadão participar da escolha dos governantes.",
   "Tribunal Superior Eleitoral", syn=["voto", "votando"], br=True)
tf(P, "eleições", 1, 7, "No Brasil, as pessoas votam usando uma urna eletrônica.", True,
   "A urna eletrônica é usada em todo o país desde o ano 2000.",
   "Tribunal Superior Eleitoral", br=True)
op(P, "eleições", 1, 8, "Como se chama a pessoa que vota numa eleição?", "Eleitor",
   ["eleitor", "eleitora", "eleitores"],
   "Para votar, o eleitor precisa ter o título de eleitor.",
   "Tribunal Superior Eleitoral", br=True)
mc(P, "poderes", 1, 9, "Juízes e tribunais fazem parte de qual Poder?",
   ["Judiciário", "Executivo", "Legislativo", "Moderador"], "Judiciário",
   "O Judiciário decide conflitos aplicando as leis.",
   "Supremo Tribunal Federal", syn=["judiciario", "poder judiciario"], br=True)
mc(P, "poderes", 1, 10, "Quem assume o lugar do presidente da República quando ele viaja ou fica impedido?",
   ["O vice-presidente", "O governador", "O prefeito", "O senador mais velho"], "O vice-presidente",
   "O vice-presidente é eleito na mesma chapa do presidente.",
   "Constituição Federal de 1988 – art. 79", syn=["vice-presidente", "vice presidente", "vice"], br=True)
mc(P, "congresso", 2, 12, "O Congresso Nacional é formado pela Câmara dos Deputados e por qual outra casa?",
   ["Senado Federal", "Supremo Tribunal Federal", "Assembleia Legislativa", "Câmara Municipal"], "Senado Federal",
   "As duas casas funcionam no prédio projetado por Oscar Niemeyer em Brasília.",
   "Senado Federal", syn=["senado"], br=True)
tf(P, "eleições", 2, 12, "No Brasil, o voto é secreto.", True,
   "Ninguém pode saber em quem o eleitor votou, o que protege sua liberdade de escolha.",
   "Constituição Federal de 1988 – art. 14", br=True)
op(P, "estados", 2, 12, "Como se chama a casa onde trabalham os deputados estaduais?", "Assembleia Legislativa",
   ["assembleia legislativa", "assembleia"],
   "Cada estado tem sua Assembleia; no Distrito Federal ela se chama Câmara Legislativa.",
   "Constituição Federal de 1988 – art. 27", br=True)
mc(P, "brasília", 2, 12, "Qual praça de Brasília reúne o Palácio do Planalto, o Congresso e o Supremo?",
   ["Praça dos Três Poderes", "Praça da Sé", "Praça da Liberdade", "Praça da República"], "Praça dos Três Poderes",
   "A praça simboliza o equilíbrio entre Executivo, Legislativo e Judiciário.",
   "IPHAN – Conjunto Urbanístico de Brasília", syn=["tres poderes"], br=True)
mc(P, "mundo", 2, 12, "Em qual cidade fica a sede da Organização das Nações Unidas?",
   ["Nova York", "Genebra", "Paris", "Washington"], "Nova York",
   "O prédio da sede da ONU teve projeto com participação de Oscar Niemeyer.",
   "Organização das Nações Unidas – un.org", syn=["nova iorque", "new york"])
mc(P, "judiciário", 3, 14, "Quantos ministros compõem o Supremo Tribunal Federal?",
   ["11", "9", "13", "15"], "11",
   "Os ministros são indicados pelo presidente e aprovados pelo Senado.",
   "Constituição Federal de 1988 – art. 101", br=True)
tf(P, "constituição", 3, 14, "A Constituição de 1988 ficou conhecida como 'Constituição Cidadã'.", True,
   "O apelido foi dado por Ulysses Guimarães, presidente da Assembleia Constituinte.",
   "Câmara dos Deputados", br=True)
mc(P, "história", 3, 14, "Qual movimento popular de 1984 pediu eleições diretas para presidente?",
   ["Diretas Já", "Caras-Pintadas", "Tenentismo", "Cabanagem"], "Diretas Já",
   "Os comícios das Diretas Já reuniram multidões em várias capitais.",
   "Câmara dos Deputados – Diretas Já", syn=["diretas ja"], br=True)
mc(P, "eleições", 3, 16, "Qual é a idade mínima para alguém se candidatar a presidente da República?",
   ["35 anos", "30 anos", "21 anos", "40 anos"], "35 anos",
   "A mesma idade mínima vale para candidatos a senador e a vice-presidente.",
   "Constituição Federal de 1988 – art. 14", syn=["35"], br=True)
mc(P, "eleições", 4, 16, "Qual é a idade mínima para alguém se candidatar a vereador?",
   ["18 anos", "16 anos", "21 anos", "25 anos"], "18 anos",
   "É a menor idade mínima exigida para um cargo eletivo no Brasil.",
   "Constituição Federal de 1988 – art. 14", syn=["18"], br=True)
mc(P, "história", 4, 16, "Qual era o nome oficial do país entre 1889 e 1967?",
   ["Estados Unidos do Brasil", "Império do Brasil", "Reino do Brasil", "República Federal do Brasil"],
   "Estados Unidos do Brasil",
   "A Constituição de 1967 abandonou esse nome; República Federativa do Brasil foi adotado em 1968 e consolidado em 1969.",
   "Câmara dos Deputados – Constituições Brasileiras", br=True)

# =========================================================== CULTURA BRASILEIRA
C = "cul"
mc(C, "quadrinhos", 1, 6, "Qual é o nome do coelho de pelúcia azul da Mônica?",
   ["Sansão", "Bidu", "Floquinho", "Mingau"], "Sansão",
   "A Mônica usa o Sansão para dar 'coelhadas' no Cebolinha.",
   "Mauricio de Sousa Produções – Turma da Mônica", syn=["sansao"], br=True)
tf(C, "folclore", 1, 7, "A Mula sem Cabeça é uma personagem do folclore brasileiro.", True,
   "Segundo a lenda, ela solta fogo pelo pescoço no lugar da cabeça.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(C, "festas", 1, 8, "Qual comida de festa junina é feita de milho verde e cozida dentro da palha?",
   ["Pamonha", "Pipoca", "Canjica", "Paçoca"], "Pamonha",
   "A pamonha pode ser doce ou salgada, dependendo da região.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(C, "música", 1, 8, "Qual instrumento redondo, cheio de platinelas, é tocado com a mão nas rodas de samba?",
   ["Pandeiro", "Violão", "Cavaquinho", "Flauta"], "Pandeiro",
   "As platinelas são as pequenas chapas de metal que chacoalham na borda.",
   "IPHAN – Matrizes do Samba no Rio de Janeiro", br=True)
mc(C, "folclore", 2, 10, "Qual animal da lenda amazônica vira um rapaz elegante para ir às festas?",
   ["Boto", "Jacaré", "Onça", "Peixe-boi"], "Boto",
   "Na lenda, o rapaz usa chapéu para esconder o furo de respirar no alto da cabeça.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(C, "tradições", 2, 10, "Qual mistura de luta e dança, criada por africanos escravizados no Brasil, é jogada numa roda?",
   ["Capoeira", "Frevo", "Samba", "Jiu-jítsu"], "Capoeira",
   "A roda de capoeira é Patrimônio Cultural Imaterial da Humanidade desde 2014.",
   "IPHAN – Roda de Capoeira", br=True)
mc(C, "religião", 2, 10, "Qual é a padroeira do Brasil?",
   ["Nossa Senhora Aparecida", "Nossa Senhora de Nazaré", "Santa Bárbara", "Nossa Senhora da Penha"],
   "Nossa Senhora Aparecida",
   "Seu dia, 12 de outubro, é feriado nacional.",
   "Lei nº 6.802/1980", syn=["aparecida"], br=True)
tf(C, "festas", 2, 12, "O frevo, ritmo do carnaval pernambucano, é Patrimônio Imaterial da Humanidade.", True,
   "O título foi dado pela UNESCO em 2012.",
   "UNESCO – Frevo, performing arts of the Carnival of Recife", br=True)
mc(C, "festas", 2, 12, "Em qual cidade o carnaval tem trios elétricos no circuito Barra-Ondina?",
   ["Salvador", "Recife", "Fortaleza", "Natal"], "Salvador",
   "O trio elétrico surgiu em Salvador, em 1950, com Dodô e Osmar.",
   "Enciclopédia Britannica – verbete 'Salvador'", br=True)
mc(C, "festas", 2, 12, "Qual cidade vizinha de Recife é famosa pelos bonecos gigantes do carnaval?",
   ["Olinda", "Caruaru", "Petrolina", "Garanhuns"], "Olinda",
   "O centro histórico de Olinda é Patrimônio Mundial da UNESCO.",
   "UNESCO – Historic Centre of the Town of Olinda", br=True)
mc(C, "literatura", 2, 12, "Qual escritor criou o 'Sítio do Picapau Amarelo'?",
   ["Monteiro Lobato", "Ziraldo", "Ruth Rocha", "Mauricio de Sousa"], "Monteiro Lobato",
   "O primeiro livro da série, 'A Menina do Narizinho Arrebitado', saiu em 1920.",
   "Enciclopédia Itaú Cultural – Monteiro Lobato", syn=["lobato"], br=True)
mc(C, "festas", 3, 14, "Qual festa típica do Maranhão tem um boi como personagem principal?",
   ["Bumba meu boi", "Congada", "Reisado", "Cavalhada"], "Bumba meu boi",
   "O Bumba meu boi do Maranhão é Patrimônio Imaterial da Humanidade desde 2019.",
   "IPHAN – Complexo Cultural do Bumba meu boi do Maranhão", br=True)
mc(C, "festas", 3, 16, "Qual manifestação pernambucana tem cortejo com rei, rainha e o batuque das alfaias?",
   ["Maracatu", "Ciranda", "Xaxado", "Coco"], "Maracatu",
   "As alfaias são grandes tambores de madeira tocados com baquetas.",
   "IPHAN – Maracatu Nação", br=True)

mc(C, "quadrinhos", 1, 7, "Como se chama o cachorro do Cebolinha, na Turma da Mônica?",
   ["Floquinho", "Bidu", "Sansão", "Mingau"], "Floquinho",
   "O Floquinho é tão peludo que ninguém sabe onde fica a cabeça e onde fica o rabo.",
   "Mauricio de Sousa Produções – Turma da Mônica", br=True)
mc(C, "festas", 2, 12, "Qual santo é homenageado nas festas juninas do dia 24 de junho?",
   ["São João", "Santo Antônio", "São Pedro", "São Jorge"], "São João",
   "Santo Antônio é festejado em 13 de junho e São Pedro em 29 de junho.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=["sao joao"], br=True)
op(C, "patrimônio", 3, 14, "Qual elevador famoso liga a Cidade Baixa à Cidade Alta, em Salvador?",
   "Elevador Lacerda", ["elevador lacerda", "lacerda"],
   "Inaugurado em 1873, foi o primeiro elevador urbano do Brasil.",
   "IPHAN – Elevador Lacerda", br=True)
mc(C, "patrimônio", 4, 16, "Em que ano Brasília foi declarada Patrimônio Mundial pela UNESCO?",
   ["1987", "1960", "1972", "2001"], "1987",
   "Foi a primeira cidade construída no século 20 a receber esse título.",
   "UNESCO – Brasilia", br=True)

# =========================================================== NOVELAS
N = "nov"
tf(N, "infantis", 1, 8, "A novela 'Chiquititas' é originalmente da Argentina.", True,
   "A primeira versão argentina estreou em 1995 e depois ganhou versões brasileiras no SBT.",
   "Memória SBT – Chiquititas", br=True)
mc(N, "infantis", 1, 8, "Na novela 'Carinha de Anjo', do SBT, como se chama a menina protagonista?",
   ["Dulce Maria", "Maria Joaquina", "Valéria", "Mili"], "Dulce Maria",
   "A novela de 2016 se passa num colégio de freiras.",
   "Memória SBT – Carinha de Anjo", syn=["dulce"], br=True)
mc(N, "infantis", 2, 9, "Qual novela do SBT, de 2015, contava a história das gêmeas Manuela e Isabela?",
   ["Cúmplices de um Resgate", "Carrossel", "Chiquititas", "Carinha de Anjo"], "Cúmplices de um Resgate",
   "As duas gêmeas eram interpretadas pela mesma atriz, Larissa Manoela.",
   "Memória SBT – Cúmplices de um Resgate", syn=["cumplices de um resgate"], br=True)
tf(N, "remakes", 1, 12, "A novela 'Pantanal' ganhou uma nova versão na TV Globo em 2022.", True,
   "O remake foi adaptado por Bruno Luperi, neto do autor original, Benedito Ruy Barbosa.",
   "Memória Globo – Pantanal (2022)", br=True)
mc(N, "personagens", 1, 12, "Em qual novela de 2017 a personagem Ritinha dizia ser uma sereia?",
   ["A Força do Querer", "Amor à Vida", "Avenida Brasil", "Totalmente Demais"], "A Força do Querer",
   "Ritinha foi interpretada por Isis Valverde.",
   "Memória Globo – A Força do Querer", syn=["forca do querer"], br=True)
mc(N, "autores", 2, 14, "Quem escreveu a novela 'Avenida Brasil'?",
   ["João Emanuel Carneiro", "Walcyr Carrasco", "Manoel Carlos", "Aguinaldo Silva"], "João Emanuel Carneiro",
   "O mesmo autor escreveu também 'A Favorita', de 2008.",
   "Memória Globo – Avenida Brasil", syn=["joao emanuel carneiro"], br=True)
mc(N, "personagens", 2, 14, "Em 'O Clone', qual era o nome da protagonista vivida por Giovanna Antonelli?",
   ["Jade", "Latiffa", "Maysa", "Dora"], "Jade",
   "Jade era uma jovem muçulmana que vivia entre o Brasil e o Marrocos.",
   "Memória Globo – O Clone", br=True)
op(N, "personagens", 2, 14, "Em 'Avenida Brasil', que nome usava a personagem de Débora Falabella para se vingar de Carminha?",
   "Nina", ["nina"],
   "Rita voltou adulta disfarçada de Nina e virou cozinheira na casa de Carminha.",
   "Memória Globo – Avenida Brasil", br=True)
mc(N, "autores", 2, 14, "Qual escritor baiano inspirou as novelas 'Gabriela' e 'Tieta'?",
   ["Jorge Amado", "Graciliano Ramos", "José de Alencar", "Érico Veríssimo"], "Jorge Amado",
   "'Tieta' foi adaptada do romance 'Tieta do Agreste'.",
   "Memória Globo – Tieta", br=True)
mc(N, "clássicos", 2, 16, "Qual pergunta parou o Brasil no fim da versão original de 'Vale Tudo', exibida entre 1988 e 1989?",
   ["Quem matou Odete Roitman?", "Quem matou Raquel?", "Quem matou Taís?", "Quem matou Max?"],
   "Quem matou Odete Roitman?",
   "A assassina revelada no último capítulo foi Leila, personagem de Cássia Kis.",
   "Memória Globo – Vale Tudo", br=True)
mc(N, "autores", 3, 16, "Qual autora escreveu as novelas 'Irmãos Coragem' e 'Selva de Pedra'?",
   ["Janete Clair", "Glória Perez", "Ivani Ribeiro", "Lauro César Muniz"], "Janete Clair",
   "Janete Clair ficou conhecida como 'a nossa senhora das oito'.",
   "Memória Globo – Janete Clair", br=True)
mc(N, "atores", 3, 16, "Quem interpretou a protagonista da novela 'Tieta', de 1989?",
   ["Betty Faria", "Regina Duarte", "Sônia Braga", "Vera Fischer"], "Betty Faria",
   "Na trama, Tieta volta rica para a cidade de Santana do Agreste.",
   "Memória Globo – Tieta", br=True)
mc(N, "personagens", 3, 16, "Em qual novela de 1985 Lima Duarte interpretou Sinhozinho Malta?",
   ["Roque Santeiro", "Tieta", "Vale Tudo", "Saramandaia"], "Roque Santeiro",
   "Sinhozinho Malta ficou famoso pelo bordão 'Tô certo ou tô errado?'.",
   "Memória Globo – Roque Santeiro", br=True)
mc(N, "personagens", 3, 16, "Em qual novela Christiane Torloni viveu a vilã Tereza Cristina?",
   ["Fina Estampa", "Insensato Coração", "Caminho das Índias", "Avenida Brasil"], "Fina Estampa",
   "A novela de Aguinaldo Silva foi exibida em 2011 e 2012.",
   "Memória Globo – Fina Estampa", br=True)
tf(N, "prêmios", 3, 16, "A novela 'Caminho das Índias' ganhou o Emmy Internacional de melhor novela.", True,
   "Foi a primeira novela brasileira a ganhar o prêmio na categoria, em 2009.",
   "Memória Globo – Caminho das Índias", br=True)
mc(N, "clássicos", 4, 16, "Qual novela de 1977 deixou o país curioso para saber quem matou Salomão Hayala?",
   ["O Astro", "Pecado Capital", "Dancin' Days", "Selva de Pedra"], "O Astro",
   "A novela de Janete Clair ganhou um remake em 2011.",
   "Memória Globo – O Astro", br=True)
mc(N, "história", 4, 16, "Qual novela da TV Tupi, de 1968, mudou o gênero ao trazer um anti-herói e linguagem do dia a dia?",
   ["Beto Rockfeller", "O Direito de Nascer", "Redenção", "Irmãos Coragem"], "Beto Rockfeller",
   "O protagonista era um rapaz de classe média que fingia ser rico.",
   "Enciclopédia Itaú Cultural – Beto Rockfeller", br=True)
mc(N, "história", 4, 16, "Qual foi a primeira novela diária da TV brasileira, exibida em 1963 pela TV Excelsior?",
   ["2-5499 Ocupado", "O Direito de Nascer", "Beto Rockfeller", "Redenção"], "2-5499 Ocupado",
   "Antes dela, as novelas da TV iam ao ar só duas ou três vezes por semana.",
   "Enciclopédia Itaú Cultural – Telenovela", br=True)

# =========================================================== TELEVISÃO
T = "tv"
mc(T, "desenhos", 1, 6, "No desenho 'Bob Esponja', como se chama o melhor amigo dele, que é uma estrela-do-mar?",
   ["Patrick", "Lula Molusco", "Sirigueijo", "Plankton"], "Patrick",
   "Patrick mora embaixo de uma pedra, vizinho do Bob Esponja.",
   "Nickelodeon – SpongeBob SquarePants")
mc(T, "desenhos", 1, 6, "No desenho 'Peppa Pig', como se chama o irmãozinho da Peppa?",
   ["George", "Pedro", "Richard", "Danny"], "George",
   "O George adora o seu dinossauro de brinquedo.",
   "Entertainment One – Peppa Pig")
mc(T, "desenhos", 1, 6, "De que cor são os Smurfs?",
   ["Azul", "Verde", "Amarelo", "Vermelho"], "Azul",
   "Os Smurfs foram criados pelo desenhista belga Peyo, em 1958.",
   "Enciclopédia Britannica – verbete 'Smurfs'")
mc(T, "seriados", 1, 8, "No seriado 'Chaves', qual é o nome da filha do Seu Madruga?",
   ["Chiquinha", "Paty", "Popis", "Dona Clotilde"], "Chiquinha",
   "A Chiquinha era interpretada por María Antonieta de las Nieves.",
   "Televisa – El Chavo del Ocho", br=False)
tf(T, "desenhos", 1, 8, "No desenho 'Os Flintstones', a família vive na Idade da Pedra.", True,
   "Fred, Wilma e a filha Pedrita moram na cidade de Bedrock.",
   "Enciclopédia Britannica – verbete 'The Flintstones'")
tf(T, "seriados", 1, 9, "O seriado 'Chaves' foi produzido no México.", True,
   "No Brasil, o seriado estreou no SBT em 1984.",
   "Televisa – El Chavo del Ocho")
mc(T, "seriados", 2, 9, "No seriado 'Chaves', como se chama a mãe do Quico?",
   ["Dona Florinda", "Dona Clotilde", "Dona Neves", "Chiquinha"], "Dona Florinda",
   "Dona Florinda sempre chama o Quico de 'tesouro'.",
   "Televisa – El Chavo del Ocho", syn=["florinda"])
mc(T, "infantis", 2, 9, "No 'Sítio do Picapau Amarelo', qual personagem é um sabugo de milho muito sábio?",
   ["Visconde de Sabugosa", "Marquês de Rabicó", "Conselheiro", "Cuca"], "Visconde de Sabugosa",
   "O Visconde foi criado por Tia Nastácia a partir de um sabugo de milho.",
   "Memória Globo – Sítio do Picapau Amarelo", syn=["visconde"], br=True)
mc(T, "desenhos", 2, 10, "Em 'Os Simpsons', qual é o nome da filha que toca saxofone?",
   ["Lisa", "Maggie", "Marge", "Patty"], "Lisa",
   "Lisa é a mais estudiosa da família.",
   "Fox – The Simpsons")
mc(T, "desenhos", 2, 10, "Como se chama o macaco vilão do desenho 'As Meninas Superpoderosas'?",
   ["Macaco Louco", "Ele", "Princesa", "Fuzzy"], "Macaco Louco",
   "No original em inglês, o vilão se chama Mojo Jojo.",
   "Cartoon Network – The Powerpuff Girls", syn=["mojo jojo"])
mc(T, "infantis", 2, 12, "Qual foi o programa infantil que Xuxa estreou na Globo em 1986?",
   ["Xou da Xuxa", "Clube da Criança", "TV Colosso", "Bom Dia & Cia"], "Xou da Xuxa",
   "O programa ia ao ar de manhã, de segunda a sábado.",
   "Memória Globo – Xou da Xuxa", syn=["xou da xuxa", "show da xuxa"], br=True)
mc(T, "humor", 2, 12, "Qual humorista criou e interpretou o Professor Raimundo, da 'Escolinha'?",
   ["Chico Anysio", "Jô Soares", "Renato Aragão", "Ronald Golias"], "Chico Anysio",
   "Chico Anysio criou mais de 200 personagens ao longo da carreira.",
   "Memória Globo – Chico Anysio", syn=["chico anisio"], br=True)
op(T, "esporte", 2, 12, "Qual narrador esportivo da Globo ficou famoso pelo bordão 'Haja coração!'?",
   "Galvão Bueno", ["galvao bueno", "galvao"],
   "Galvão narrou para a Globo várias Copas do Mundo e corridas de Fórmula 1.",
   "Memória Globo – Galvão Bueno", br=True)
mc(T, "emissoras", 2, 12, "Qual emissora de TV Silvio Santos fundou em 1981?",
   ["SBT", "Record", "Bandeirantes", "Manchete"], "SBT",
   "A sigla significa Sistema Brasileiro de Televisão.",
   "Memória SBT – História", br=True)
mc(T, "seriados", 2, 14, "Em qual série da Globo Marco Nanini interpretou o pai de família Lineu?",
   ["A Grande Família", "Sai de Baixo", "Os Normais", "Toma Lá, Dá Cá"], "A Grande Família",
   "A série ficou no ar de 2001 a 2014 e era uma nova versão de um programa dos anos 1970.",
   "Memória Globo – A Grande Família", syn=["grande familia"], br=True)
mc(T, "seriados", 3, 14, "Em 'Friends', qual dos amigos é paleontólogo?",
   ["Ross", "Chandler", "Joey", "Monica"], "Ross",
   "Ross é irmão da Monica e vive um namoro de idas e vindas com a Rachel.",
   "NBC – Friends")
mc(T, "seriados", 3, 14, "Qual ator mexicano criou e interpretou o Chaves?",
   ["Roberto Gómez Bolaños", "Ramón Valdés", "Carlos Villagrán", "Edgar Vivar"], "Roberto Gómez Bolaños",
   "Ele também criou e interpretou o Chapolin Colorado.",
   "Televisa – Chespirito", syn=["roberto gomez bolanos", "chespirito", "bolanos"])
mc(T, "emissoras", 3, 16, "Em que ano a TV Globo foi inaugurada?",
   ["1965", "1950", "1972", "1981"], "1965",
   "A emissora entrou no ar no Rio de Janeiro em 26 de abril de 1965.",
   "Memória Globo – História", br=True)
mc(T, "emissoras", 4, 16, "Qual emissora, fundada por Adolpho Bloch, saiu do ar em 1999?",
   ["Rede Manchete", "TV Tupi", "TV Excelsior", "TV Rio"], "Rede Manchete",
   "A Manchete foi substituída pela RedeTV!, que estreou no mesmo ano.",
   "Enciclopédia Itaú Cultural – Rede Manchete", syn=["manchete"], br=True)
