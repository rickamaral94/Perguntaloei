# Perguntas: Geografia, História, Ciência, Tecnologia, Cinema.
# Formato: mc(tema, subtema, dificuldade 1-4, idade mínima, enunciado, alternativas, resposta, explicação, fonte, ...)
from qdsl import mc, op, tf

# =========================================================== GEOGRAFIA
G = "geo"
mc(G, "capitais", 1, 6, "Qual é a capital do Brasil?",
   ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], "Brasília",
   "Brasília é a capital federal desde 21 de abril de 1960, quando foi inaugurada.",
   "Constituição Federal de 1988, art. 18, §1º; IBGE", br=True)
mc(G, "continentes", 1, 6, "Em qual continente fica o Brasil?",
   ["América do Sul", "Europa", "África", "Ásia"], "América do Sul",
   "O Brasil ocupa cerca de metade da área da América do Sul.",
   "IBGE – Brasil em síntese", br=True)
mc(G, "oceanos", 1, 6, "Qual destes é um oceano?",
   ["Atlântico", "Amazonas", "Saara", "Andes"], "Atlântico",
   "O Atlântico é o oceano que banha todo o litoral brasileiro. Amazonas é um rio, Saara é um deserto e Andes é uma cordilheira.",
   "Enciclopédia Britannica – verbete 'Atlantic Ocean'")
op(G, "relevo", 1, 6, "Como se chama uma porção de terra cercada de água por todos os lados?",
   "Ilha", ["uma ilha", "ilhas"],
   "Ilha é uma porção de terra rodeada de água. Exemplos: Ilha de Marajó (PA) e Florianópolis (SC).",
   "IBGE – Glossário de termos geográficos")
tf(G, "território", 1, 8, "O Brasil é o maior país da América do Sul em área.", True,
   "Com cerca de 8,5 milhões de km², o Brasil é o maior país sul-americano e o 5º maior do mundo.",
   "IBGE – Área territorial brasileira (2022)", br=True)
mc(G, "oceanos", 1, 8, "Qual é o maior oceano do planeta?",
   ["Pacífico", "Atlântico", "Índico", "Ártico"], "Pacífico",
   "O Pacífico cobre cerca de um terço da superfície da Terra, mais que todos os continentes juntos.",
   "NOAA – Ocean facts")
mc(G, "capitais", 1, 8, "Qual é a capital da França?",
   ["Paris", "Londres", "Roma", "Madri"], "Paris",
   "Paris é a capital e a maior cidade da França.",
   "Enciclopédia Britannica – verbete 'Paris'")
op(G, "capitais", 1, 8, "Qual é a capital do estado da Bahia?",
   "Salvador", ["cidade de salvador"],
   "Salvador foi também a primeira capital do Brasil, de 1549 a 1763.",
   "IBGE – Cidades", br=True)
mc(G, "capitais", 1, 9, "Qual é a capital da Argentina?",
   ["Buenos Aires", "Montevidéu", "Santiago", "Lima"], "Buenos Aires",
   "Buenos Aires fica às margens do Rio da Prata. Montevidéu é a capital do Uruguai.",
   "Enciclopédia Britannica – verbete 'Buenos Aires'")
op(G, "cidades", 2, 10, "Qual é a cidade mais populosa do Brasil?",
   "São Paulo", ["sao paulo", "sampa", "cidade de sao paulo"],
   "São Paulo tinha cerca de 11,4 milhões de habitantes no Censo de 2022.",
   "IBGE – Censo Demográfico 2022", br=True, ref="Censo 2022")
mc(G, "estados", 2, 10, "Qual é o maior estado brasileiro em área?",
   ["Amazonas", "Pará", "Mato Grosso", "Minas Gerais"], "Amazonas",
   "O Amazonas tem cerca de 1,56 milhão de km², quase 18% do território nacional.",
   "IBGE – Áreas territoriais (2022)", br=True)
mc(G, "estados", 2, 10, "Quantos estados tem o Brasil, sem contar o Distrito Federal?",
   ["26", "27", "25", "24"], "26",
   "São 26 estados mais o Distrito Federal, somando 27 unidades da federação.",
   "Constituição Federal de 1988, art. 18; IBGE", br=True)
mc(G, "rios", 2, 10, "Qual rio é o maior do mundo em volume de água?",
   ["Amazonas", "Nilo", "Mississippi", "Yangtzé"], "Amazonas",
   "O Amazonas despeja no Atlântico mais água do que qualquer outro rio, cerca de 20% da água doce que chega aos oceanos.",
   "Enciclopédia Britannica – verbete 'Amazon River'", br=True)
tf(G, "território", 2, 10, "A Linha do Equador passa pelo território brasileiro.", True,
   "A Linha do Equador cruza os estados do Amapá, Roraima, Amazonas e Pará. Em Macapá há o monumento Marco Zero.",
   "IBGE – Atlas geográfico escolar", br=True)
mc(G, "paisagens", 2, 10, "Em que estado brasileiro ficam as Cataratas do Iguaçu?",
   ["Paraná", "Santa Catarina", "Mato Grosso do Sul", "São Paulo"], "Paraná",
   "As cataratas ficam na divisa entre o Paraná (Brasil) e a província de Misiones (Argentina).",
   "Parque Nacional do Iguaçu – ICMBio", br=True)
mc(G, "população", 2, 12, "Segundo estimativas da ONU de 2023, qual país passou a ter a maior população do mundo?",
   ["Índia", "China", "Estados Unidos", "Indonésia"], "Índia",
   "Em 2023 a ONU estimou que a Índia ultrapassou a China em número de habitantes.",
   "ONU – World Population Prospects / UNFPA (abril de 2023)", ref="Estimativa da ONU, 2023")
mc(G, "relevo", 3, 12, "Qual é o ponto mais alto do Brasil?",
   ["Pico da Neblina", "Pico da Bandeira", "Monte Roraima", "Pico Paraná"], "Pico da Neblina",
   "O Pico da Neblina, no Amazonas, tem cerca de 2.995 metros de altitude.",
   "IBGE – Altitudes dos pontos culminantes (2016)", br=True, ref="Medição do IBGE de 2016")
mc(G, "capitais", 3, 12, "Qual é a capital da Austrália?",
   ["Camberra", "Sydney", "Melbourne", "Perth"], "Camberra",
   "Camberra foi planejada para ser a capital, como Brasília. Sydney é a maior cidade australiana.",
   "Enciclopédia Britannica – verbete 'Canberra'")
mc(G, "fronteiras", 3, 12, "Com quantos países o Brasil faz fronteira?",
   ["10", "8", "12", "9"], "10",
   "O Brasil faz fronteira com todos os países da América do Sul, exceto Chile e Equador.",
   "IBGE – Brasil em síntese", br=True)
mc(G, "estados", 3, 12, "Qual estado brasileiro tem a menor área territorial?",
   ["Sergipe", "Alagoas", "Rio de Janeiro", "Espírito Santo"], "Sergipe",
   "Sergipe tem cerca de 21,9 mil km². O Distrito Federal é menor, mas não é um estado.",
   "IBGE – Áreas territoriais (2022)", br=True)
mc(G, "paisagens", 3, 14, "Em que estado fica a Chapada dos Veadeiros?",
   ["Goiás", "Bahia", "Mato Grosso", "Tocantins"], "Goiás",
   "O Parque Nacional da Chapada dos Veadeiros fica no nordeste de Goiás, no Cerrado.",
   "ICMBio – Parque Nacional da Chapada dos Veadeiros", br=True)
mc(G, "capitais", 3, 12, "Qual é a capital do Canadá?",
   ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa",
   "Ottawa fica na província de Ontário. Toronto é a maior cidade do país.",
   "Enciclopédia Britannica – verbete 'Ottawa'")
mc(G, "desertos", 4, 14, "Qual é o deserto não polar mais seco do mundo?",
   ["Atacama", "Saara", "Gobi", "Kalahari"], "Atacama",
   "O Atacama, no Chile, tem áreas onde quase nunca chove.",
   "NASA Earth Observatory – Atacama Desert")
mc(G, "montanhas", 4, 14, "O Monte Everest fica na fronteira entre o Nepal e qual país?",
   ["China", "Índia", "Butão", "Paquistão"], "China",
   "O Everest fica entre o Nepal e a Região Autônoma do Tibete, na China.",
   "Enciclopédia Britannica – verbete 'Mount Everest'")

# =========================================================== HISTÓRIA
H = "his"
tf(H, "pré-história", 1, 6, "Os dinossauros viveram antes dos seres humanos.", True,
   "Os dinossauros não aviários foram extintos há cerca de 66 milhões de anos, muito antes do surgimento dos humanos.",
   "Museu de História Natural de Londres – Dinosaur extinction")
mc(H, "povos originários", 1, 6, "Como são chamados os povos que já viviam no Brasil antes da chegada dos portugueses?",
   ["Povos indígenas", "Vikings", "Romanos", "Egípcios"], "Povos indígenas",
   "Milhões de indígenas, de centenas de povos diferentes, já viviam no território quando os europeus chegaram.",
   "FUNAI; IBGE – Os indígenas no Censo", syn=["indigenas", "indios", "povos originarios"], br=True)
mc(H, "idade média", 1, 6, "O que os cavaleiros medievais usavam para se proteger nas batalhas?",
   ["Armadura", "Capa de chuva", "Boia", "Patins"], "Armadura",
   "As armaduras eram feitas de metal, como malhas de ferro e placas de aço.",
   "Metropolitan Museum of Art – Arms and Armor")
mc(H, "navegações", 1, 6, "Que embarcações os navegadores portugueses usavam para atravessar o oceano há mais de 500 anos?",
   ["Caravelas", "Aviões", "Submarinos", "Balões"], "Caravelas",
   "As caravelas eram barcos a vela leves e rápidos, usados nas Grandes Navegações.",
   "Museu de Marinha (Lisboa)", br=True)
mc(H, "brasil colônia", 1, 8, "Em que ano os portugueses chegaram ao território que hoje é o Brasil?",
   ["1500", "1492", "1600", "1822"], "1500",
   "A frota de Pedro Álvares Cabral chegou em 22 de abril de 1500, no litoral da atual Bahia.",
   "Carta de Pero Vaz de Caminha (1500); Arquivo Nacional da Torre do Tombo", br=True)
mc(H, "independência", 1, 9, "Quem proclamou a independência do Brasil?",
   ["Dom Pedro I", "Dom Pedro II", "Tiradentes", "Getúlio Vargas"], "Dom Pedro I",
   "Dom Pedro I proclamou a independência às margens do riacho Ipiranga, em São Paulo.",
   "Arquivo Nacional; Museu do Ipiranga", syn=["pedro primeiro", "dom pedro primeiro", "pedro 1"], br=True)
mc(H, "independência", 1, 10, "Em que ano o Brasil declarou sua independência de Portugal?",
   ["1822", "1500", "1889", "1888"], "1822",
   "A independência foi proclamada em 7 de setembro de 1822.",
   "Arquivo Nacional", br=True)
mc(H, "grandes navegações", 1, 10, "Qual navegador chegou à América em 1492, a serviço da Espanha?",
   ["Cristóvão Colombo", "Pedro Álvares Cabral", "Vasco da Gama", "Fernão de Magalhães"], "Cristóvão Colombo",
   "Colombo chegou às ilhas do Caribe em outubro de 1492, achando que estava na Ásia.",
   "Enciclopédia Britannica – verbete 'Christopher Columbus'", syn=["colombo"])
mc(H, "antiguidade", 1, 9, "Qual civilização construiu as pirâmides de Gizé?",
   ["Egípcios antigos", "Romanos", "Gregos", "Maias"], "Egípcios antigos",
   "As pirâmides de Gizé foram construídas há mais de 4.500 anos, no Egito.",
   "UNESCO – Memphis and its Necropolis", syn=["egipcios", "os egipcios", "egito"])
mc(H, "corrida espacial", 1, 10, "Quem foi o primeiro ser humano a pisar na Lua?",
   ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "Marcos Pontes"], "Neil Armstrong",
   "Armstrong pisou na Lua em 20 de julho de 1969, na missão Apollo 11.",
   "NASA – Apollo 11 Mission Overview", syn=["armstrong"])
mc(H, "abolição", 2, 10, "Qual lei aboliu a escravidão no Brasil, em 1888?",
   ["Lei Áurea", "Lei do Ventre Livre", "Lei dos Sexagenários", "Lei Eusébio de Queirós"], "Lei Áurea",
   "A Lei Áurea foi assinada em 13 de maio de 1888 e extinguiu a escravidão no país.",
   "Lei nº 3.353, de 13 de maio de 1888 – Arquivo Nacional", syn=["aurea"], br=True)
mc(H, "abolição", 2, 12, "Quem assinou a Lei Áurea?",
   ["Princesa Isabel", "Dom Pedro II", "Dom Pedro I", "Marechal Deodoro"], "Princesa Isabel",
   "A princesa Isabel assinou a lei como regente, enquanto Dom Pedro II estava fora do país.",
   "Arquivo Nacional – Lei Áurea", syn=["isabel"], br=True)
mc(H, "república", 2, 12, "Em que ano foi proclamada a República no Brasil?",
   ["1889", "1822", "1891", "1930"], "1889",
   "A República foi proclamada em 15 de novembro de 1889.",
   "Arquivo Nacional", br=True)
mc(H, "república", 2, 12, "Quem foi o primeiro presidente do Brasil?",
   ["Deodoro da Fonseca", "Floriano Peixoto", "Getúlio Vargas", "Prudente de Morais"], "Deodoro da Fonseca",
   "O marechal Deodoro da Fonseca chefiou o governo provisório e foi eleito presidente em 1891.",
   "Biblioteca da Presidência da República", syn=["deodoro", "marechal deodoro"], br=True)
tf(H, "brasil colônia", 2, 12, "Tiradentes foi um dos líderes da Inconfidência Mineira.", True,
   "Joaquim José da Silva Xavier, o Tiradentes, foi executado em 21 de abril de 1792.",
   "Arquivo Nacional – Autos de Devassa da Inconfidência Mineira", br=True)
mc(H, "século XX", 2, 12, "Em que ano começou a Segunda Guerra Mundial?",
   ["1939", "1914", "1945", "1929"], "1939",
   "A guerra começou em 1º de setembro de 1939, com a invasão da Polônia pela Alemanha.",
   "Enciclopédia Britannica – verbete 'World War II'")
mc(H, "brasília", 2, 12, "Qual presidente inaugurou Brasília, em 1960?",
   ["Juscelino Kubitschek", "Getúlio Vargas", "Jânio Quadros", "João Goulart"], "Juscelino Kubitschek",
   "JK prometeu 'cinquenta anos em cinco' e inaugurou Brasília em 21 de abril de 1960.",
   "Biblioteca da Presidência da República", syn=["jk", "juscelino"], br=True)
mc(H, "guerra fria", 2, 12, "Qual muro caiu em 1989, tornando-se símbolo do fim da Guerra Fria?",
   ["Muro de Berlim", "Muralha da China", "Muro das Lamentações", "Muralha de Adriano"], "Muro de Berlim",
   "O Muro de Berlim dividiu a cidade de 1961 até 9 de novembro de 1989.",
   "Enciclopédia Britannica – verbete 'Berlin Wall'", syn=["berlim"])
mc(H, "capitais", 2, 10, "Qual cidade era a capital do Brasil antes de Brasília?",
   ["Rio de Janeiro", "Salvador", "São Paulo", "Recife"], "Rio de Janeiro",
   "O Rio de Janeiro foi capital de 1763 até 1960.",
   "IBGE – Histórico das capitais", br=True)
op(H, "antiguidade", 2, 10, "Qual língua era falada pelos antigos romanos?",
   "Latim", ["latim"],
   "Do latim surgiram línguas como o português, o espanhol, o italiano e o francês.",
   "Enciclopédia Britannica – verbete 'Latin language'")
mc(H, "capitais", 3, 12, "Qual foi a primeira capital do Brasil?",
   ["Salvador", "Rio de Janeiro", "Olinda", "São Vicente"], "Salvador",
   "Salvador foi fundada em 1549 para ser a sede do governo-geral e foi capital até 1763.",
   "IPHAN – Centro Histórico de Salvador", br=True)
mc(H, "república", 3, 14, "Em que ano foi promulgada a atual Constituição brasileira?",
   ["1988", "1985", "1946", "1967"], "1988",
   "A Constituição Cidadã foi promulgada em 5 de outubro de 1988.",
   "Constituição da República Federativa do Brasil de 1988", br=True)
mc(H, "idade moderna", 3, 14, "Qual imperador francês foi derrotado na Batalha de Waterloo, em 1815?",
   ["Napoleão Bonaparte", "Luís XIV", "Carlos Magno", "Luís XVI"], "Napoleão Bonaparte",
   "Depois de Waterloo, Napoleão foi exilado na ilha de Santa Helena.",
   "Enciclopédia Britannica – verbete 'Battle of Waterloo'", syn=["napoleao"])
mc(H, "idade moderna", 3, 14, "Em que ano começou a Revolução Francesa?",
   ["1789", "1776", "1815", "1848"], "1789",
   "A tomada da Bastilha, em 14 de julho de 1789, é o marco do início da Revolução.",
   "Enciclopédia Britannica – verbete 'French Revolution'")
mc(H, "grandes navegações", 4, 14, "Qual navegador português comandou a primeira viagem marítima da Europa até a Índia contornando a África, em 1498?",
   ["Vasco da Gama", "Bartolomeu Dias", "Pedro Álvares Cabral", "Fernão de Magalhães"], "Vasco da Gama",
   "Vasco da Gama chegou a Calicute, na Índia, em 1498. Bartolomeu Dias havia contornado o Cabo da Boa Esperança em 1488.",
   "Enciclopédia Britannica – verbete 'Vasco da Gama'")
mc(H, "brasil colônia", 4, 14, "Qual tratado de 1494 dividiu as terras 'descobertas' e por descobrir entre Portugal e Espanha?",
   ["Tratado de Tordesilhas", "Tratado de Madri", "Tratado de Versalhes", "Tratado de Methuen"], "Tratado de Tordesilhas",
   "A linha imaginária de Tordesilhas ficava 370 léguas a oeste de Cabo Verde.",
   "Arquivo Nacional da Torre do Tombo – Tratado de Tordesilhas", syn=["tordesilhas"], br=True)

# =========================================================== CIÊNCIA
C = "cie"
mc(C, "corpo humano", 1, 6, "Qual órgão bombeia o sangue pelo corpo?",
   ["Coração", "Pulmão", "Estômago", "Fígado"], "Coração",
   "O coração bate cerca de 100 mil vezes por dia, levando sangue a todo o corpo.",
   "Biblioteca Virtual em Saúde – Ministério da Saúde")
mc(C, "estados da matéria", 1, 6, "Em que estado físico a água fica quando vira gelo?",
   ["Sólido", "Líquido", "Gasoso", "Plasma"], "Sólido",
   "Ao nível do mar, a água congela a 0 °C e passa do estado líquido para o sólido.",
   "USGS – Water Science School")
mc(C, "astronomia", 1, 6, "Qual planeta é conhecido como Planeta Vermelho?",
   ["Marte", "Júpiter", "Vênus", "Saturno"], "Marte",
   "A cor avermelhada vem do óxido de ferro (ferrugem) presente no solo marciano.",
   "NASA – Mars Facts")
tf(C, "astronomia", 1, 6, "A Lua tem luz própria.", False,
   "A Lua apenas reflete a luz do Sol. Por isso vemos suas fases.",
   "NASA – Moon Facts")
mc(C, "física", 1, 6, "Qual é o nome da força que nos mantém presos ao chão?",
   ["Gravidade", "Magnetismo", "Atrito", "Eletricidade"], "Gravidade",
   "A gravidade da Terra atrai tudo para o seu centro, por isso as coisas caem.",
   "NASA Space Place – What is gravity?")
mc(C, "astronomia", 1, 8, "Qual é o maior planeta do Sistema Solar?",
   ["Júpiter", "Saturno", "Terra", "Netuno"], "Júpiter",
   "Júpiter é tão grande que caberiam mais de 1.300 Terras dentro dele.",
   "NASA – Jupiter Facts")
mc(C, "astronomia", 1, 8, "Quantos planetas existem no Sistema Solar?",
   ["8", "9", "7", "10"], "8",
   "Desde 2006 Plutão é classificado como planeta-anão, então são 8 planetas.",
   "União Astronômica Internacional – Resolução B5 (2006)", ref="Classificação da UAI de 2006")
mc(C, "astronomia", 1, 9, "Qual é o planeta mais próximo do Sol?",
   ["Mercúrio", "Vênus", "Terra", "Marte"], "Mercúrio",
   "Mercúrio é também o menor planeta do Sistema Solar.",
   "NASA – Mercury Facts")
mc(C, "física", 1, 9, "Ao nível do mar, a quantos graus Celsius a água pura ferve?",
   ["100 graus", "50 graus", "0 grau", "200 graus"], "100 graus",
   "Em lugares altos, onde a pressão do ar é menor, a água ferve abaixo de 100 °C.",
   "USGS – Water Science School", syn=["100", "cem"])
mc(C, "biologia", 2, 10, "Qual gás as plantas absorvem do ar para fazer a fotossíntese?",
   ["Gás carbônico", "Oxigênio", "Hélio", "Nitrogênio"], "Gás carbônico",
   "Na fotossíntese, as plantas usam luz, água e gás carbônico e liberam oxigênio.",
   "Embrapa – Fotossíntese", syn=["dioxido de carbono", "co2", "carbonico"])
op(C, "química", 2, 10, "Qual é a fórmula química da água?",
   "H2O", ["h 2 o", "aga 2 o", "aga dois o", "h dois o"],
   "Cada molécula de água tem dois átomos de hidrogênio e um de oxigênio.",
   "IUPAC – Compendium of Chemical Terminology")
tf(C, "física", 2, 12, "O som se propaga mais rápido no vácuo do que no ar.", False,
   "O som precisa de um meio material para se propagar. No vácuo não há som.",
   "NASA – Sound in space")
mc(C, "cientistas", 2, 12, "Qual cientista formulou a teoria da relatividade?",
   ["Albert Einstein", "Isaac Newton", "Galileu Galilei", "Marie Curie"], "Albert Einstein",
   "Einstein publicou a relatividade restrita em 1905 e a geral em 1915.",
   "Enciclopédia Britannica – verbete 'Albert Einstein'", syn=["einstein"])
mc(C, "biologia", 2, 12, "Qual vitamina o corpo produz quando a pele recebe luz do sol?",
   ["Vitamina D", "Vitamina C", "Vitamina A", "Vitamina B12"], "Vitamina D",
   "A radiação ultravioleta do sol ajuda a pele a produzir vitamina D, importante para os ossos.",
   "Ministério da Saúde – Vitamina D")
mc(C, "cientistas", 2, 12, "Quem propôs a teoria da evolução por seleção natural?",
   ["Charles Darwin", "Jean-Baptiste Lamarck", "Gregor Mendel", "Louis Pasteur"], "Charles Darwin",
   "Darwin publicou 'A Origem das Espécies' em 1859.",
   "Darwin Correspondence Project – Universidade de Cambridge", syn=["darwin"])
mc(C, "corpo humano", 3, 12, "Quantos ossos tem o corpo de um ser humano adulto?",
   ["206", "150", "300", "412"], "206",
   "Os bebês nascem com cerca de 300 ossos; vários se fundem durante o crescimento.",
   "Enciclopédia Britannica – verbete 'human skeleton'")
mc(C, "química", 3, 14, "Qual é o símbolo químico do ouro?",
   ["Au", "Ag", "Fe", "Pb"], "Au",
   "Au vem do latim 'aurum'. Ag é prata, Fe é ferro e Pb é chumbo.",
   "IUPAC – Tabela Periódica")
mc(C, "física", 3, 14, "Qual é a velocidade aproximada da luz no vácuo?",
   ["300 mil km por segundo", "300 km por segundo", "30 mil km por segundo", "3 milhões de km por segundo"], "300 mil km por segundo",
   "O valor exato é 299.792,458 km/s: a luz do Sol leva cerca de 8 minutos para chegar à Terra.",
   "BIPM – Sistema Internacional de Unidades (SI)")
mc(C, "biologia", 3, 14, "Em células eucariontes, qual estrutura guarda o material genético (DNA)?",
   ["Núcleo", "Membrana plasmática", "Citoplasma", "Parede celular"], "Núcleo",
   "Nos eucariontes o DNA fica protegido dentro do núcleo; nas bactérias não há núcleo definido.",
   "NIH – National Human Genome Research Institute")
mc(C, "química", 4, 14, "Qual é o elemento químico mais abundante no Universo?",
   ["Hidrogênio", "Hélio", "Oxigênio", "Carbono"], "Hidrogênio",
   "Cerca de 3/4 da matéria comum do Universo é hidrogênio.",
   "NASA – Universe 101")
mc(C, "química", 4, 14, "Qual é o pH da água pura a 25 °C?",
   ["7", "0", "14", "1"], "7",
   "pH 7 é neutro: abaixo disso é ácido e acima é básico.",
   "IUPAC – Compendium of Chemical Terminology")

# =========================================================== TECNOLOGIA
T = "tec"
mc(T, "videogames", 1, 6, "Qual personagem de videogame é um encanador de bigode e boné vermelho?",
   ["Mario", "Sonic", "Pac-Man", "Link"], "Mario",
   "Mario apareceu pela primeira vez em 1981, no jogo Donkey Kong, da Nintendo.",
   "Nintendo – história do Mario", syn=["super mario"])
mc(T, "aparelhos", 1, 6, "Que aparelho usamos para tirar fotos?",
   ["Câmera", "Geladeira", "Liquidificador", "Ventilador"], "Câmera",
   "Hoje a maioria dos celulares também tem câmera.",
   "Dicionário Houaiss – verbete 'câmera'", syn=["camera", "maquina fotografica"])
mc(T, "videogames", 1, 6, "Qual é o nome do ouriço azul supersônico dos videogames da Sega?",
   ["Sonic", "Mario", "Kirby", "Yoshi"], "Sonic",
   "Sonic the Hedgehog foi lançado pela Sega em 1991.",
   "Sega – Sonic the Hedgehog")
mc(T, "internet", 1, 6, "O que permite conectar o celular à internet sem fio dentro de casa?",
   ["Wi-Fi", "Pen drive", "Fone de ouvido", "Carregador"], "Wi-Fi",
   "O roteador Wi-Fi distribui a internet por ondas de rádio, sem cabos.",
   "Wi-Fi Alliance", syn=["wifi", "uai fai", "wi fi"])
tf(T, "computadores", 1, 8, "O mouse é um dispositivo de entrada do computador.", True,
   "Dispositivos de entrada enviam informações ao computador, como mouse e teclado. Monitor e impressora são de saída.",
   "Enciclopédia Britannica – verbete 'input device'")
op(T, "empresas", 1, 9, "Qual empresa criou o iPhone?",
   "Apple", ["a apple", "eipou"],
   "O primeiro iPhone foi apresentado por Steve Jobs em janeiro de 2007.",
   "Apple Newsroom – 2007")
mc(T, "invenções", 1, 10, "Qual inventor brasileiro voou com o 14-Bis em Paris, em 1906?",
   ["Santos Dumont", "Marcos Pontes", "Bartolomeu de Gusmão", "Oswaldo Cruz"], "Santos Dumont",
   "Em 23 de outubro de 1906, Alberto Santos Dumont voou com o 14-Bis diante de testemunhas.",
   "Força Aérea Brasileira – Santos Dumont", syn=["dumont", "alberto santos dumont"], br=True)
mc(T, "videogames", 2, 10, "Em qual jogo de fliperama de 1980 um personagem amarelo come pastilhas num labirinto fugindo de fantasmas?",
   ["Pac-Man", "Space Invaders", "Donkey Kong", "Tetris"], "Pac-Man",
   "Pac-Man foi criado no Japão pela Namco e virou um ícone dos fliperamas.",
   "Bandai Namco – história do Pac-Man", syn=["pacman", "pac man"])
mc(T, "empresas", 2, 10, "Qual empresa japonesa criou o console PlayStation?",
   ["Sony", "Nintendo", "Sega", "Microsoft"], "Sony",
   "O primeiro PlayStation foi lançado no Japão em dezembro de 1994.",
   "Sony Interactive Entertainment – história")
mc(T, "empresas", 2, 10, "Qual empresa é responsável pelo desenvolvimento do sistema operacional Android?",
   ["Google", "Apple", "Microsoft", "Amazon"], "Google",
   "O Google comprou a startup Android em 2005 e lançou o sistema em 2008.",
   "Android Developers – história do Android")
mc(T, "computadores", 2, 12, "Quantos bits formam um byte?",
   ["8", "4", "16", "10"], "8",
   "Um byte tem 8 bits e pode representar 256 valores diferentes.",
   "IEC 80000-13 – grandezas e unidades da informação")
mc(T, "empresas", 2, 12, "Quem fundou a Microsoft ao lado de Paul Allen?",
   ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"], "Bill Gates",
   "Bill Gates e Paul Allen fundaram a Microsoft em 1975.",
   "Microsoft – Company history", syn=["gates"])
mc(T, "espaço", 2, 12, "Quem foi o primeiro astronauta brasileiro a ir ao espaço?",
   ["Marcos Pontes", "Santos Dumont", "César Lattes", "Oswaldo Cruz"], "Marcos Pontes",
   "Marcos Pontes foi à Estação Espacial Internacional em março de 2006.",
   "Agência Espacial Brasileira – Missão Centenário", syn=["pontes"], br=True)
mc(T, "internet", 2, 12, "Qual destas redes sociais foi criada por Mark Zuckerberg e colegas de faculdade?",
   ["Facebook", "Twitter", "Orkut", "TikTok"], "Facebook",
   "O Facebook foi lançado em 2004 na Universidade Harvard.",
   "Meta – Company info")
mc(T, "celulares", 2, 12, "Em que década foi lançado o primeiro iPhone?",
   ["Anos 2000", "Anos 1990", "Anos 2010", "Anos 1980"], "Anos 2000",
   "O primeiro iPhone chegou às lojas dos EUA em junho de 2007.",
   "Apple Newsroom – 2007", syn=["2000", "decada de 2000"])
mc(T, "computadores", 3, 12, "Qual é a menor unidade de informação em computação, que vale 0 ou 1?",
   ["Bit", "Byte", "Pixel", "Hertz"], "Bit",
   "Bit vem de 'binary digit' (dígito binário).",
   "IEC 80000-13")
mc(T, "computadores", 3, 14, "O que significa a sigla CPU?",
   ["Unidade Central de Processamento", "Computador Pessoal Unificado", "Central de Programas Úteis", "Unidade de Placa Principal"],
   "Unidade Central de Processamento",
   "A CPU (Central Processing Unit) é o processador, que executa as instruções dos programas.",
   "Enciclopédia Britannica – verbete 'central processing unit'", syn=["processador"])
mc(T, "internet", 3, 14, "Qual linguagem é usada para estruturar páginas da web?",
   ["HTML", "SQL", "PDF", "MP3"], "HTML",
   "HTML significa HyperText Markup Language; foi criada por Tim Berners-Lee.",
   "W3C – HTML Standard")
tf(T, "videogames", 3, 12, "O jogo Tetris foi criado na antiga União Soviética.", True,
   "Alexey Pajitnov criou o Tetris em 1984, em Moscou.",
   "The Tetris Company – história")
mc(T, "computação", 4, 14, "Quem descreveu, em 1936, a máquina teórica de computação que hoje leva o seu nome?",
   ["Alan Turing", "Charles Babbage", "John von Neumann", "Ada Lovelace"], "Alan Turing",
   "A máquina de Turing é a base teórica da computação moderna.",
   "Enciclopédia Britannica – verbete 'Turing machine'", syn=["turing"])
mc(T, "computação", 4, 14, "Qual computador eletrônico de uso geral foi apresentado nos Estados Unidos em 1946?",
   ["ENIAC", "UNIVAC", "Apple I", "IBM PC"], "ENIAC",
   "O ENIAC ocupava uma sala inteira e pesava cerca de 27 toneladas.",
   "Universidade da Pensilvânia – ENIAC", syn=["eniac", "eniaque"])

# =========================================================== CINEMA
F = "cin"
mc(F, "super-heróis", 1, 6, "Qual super-herói tem um morcego como símbolo?",
   ["Batman", "Superman", "Homem-Aranha", "Hulk"], "Batman",
   "Batman foi criado em 1939 por Bob Kane e Bill Finger.",
   "DC Comics – Batman")
mc(F, "super-heróis", 1, 6, "Qual super-herói fica verde e muito forte quando está com raiva?",
   ["Hulk", "Thor", "Flash", "Batman"], "Hulk",
   "O Hulk foi criado por Stan Lee e Jack Kirby em 1962.",
   "Marvel – Hulk")
mc(F, "cinema", 1, 6, "Qual comida feita de milho estourado é a cara do cinema?",
   ["Pipoca", "Pamonha", "Canjica", "Curau"], "Pipoca",
   "O milho de pipoca estoura porque a água dentro do grão vira vapor e rompe a casca.",
   "Embrapa – Milho-pipoca")
mc(F, "super-heróis", 1, 6, "Qual super-herói veio do planeta Krypton?",
   ["Superman", "Batman", "Homem-Aranha", "Flash"], "Superman",
   "Superman foi criado em 1938 por Jerry Siegel e Joe Shuster.",
   "DC Comics – Superman", syn=["super homem"])
op(F, "prêmios", 1, 9, "Qual é o nome do principal prêmio do cinema americano, cuja estatueta é dourada?",
   "Oscar", ["o oscar", "premio oscar"],
   "O Oscar é entregue pela Academia de Artes e Ciências Cinematográficas desde 1929.",
   "Academy of Motion Picture Arts and Sciences")
mc(F, "fantasia", 1, 9, "Nos filmes de Harry Potter, qual é o nome da escola de magia?",
   ["Hogwarts", "Nárnia", "Xavier", "Olimpo"], "Hogwarts",
   "Hogwarts é a Escola de Magia e Bruxaria criada por J. K. Rowling.",
   "Wizarding World – Hogwarts")
tf(F, "aventura", 1, 9, "O filme Jurassic Park mostra um parque com dinossauros recriados pela ciência.", True,
   "Dirigido por Steven Spielberg, o filme é de 1993 e foi baseado no livro de Michael Crichton.",
   "AFI Catalog – Jurassic Park (1993)")
mc(F, "clássicos", 1, 10, "Qual filme de 1997 conta a história de um navio que afunda após bater em um iceberg?",
   ["Titanic", "Avatar", "Poseidon", "Piratas do Caribe"], "Titanic",
   "Titanic, de James Cameron, venceu 11 Oscars, incluindo Melhor Filme.",
   "Academy Awards Database – 70º Oscar")
mc(F, "ficção científica", 2, 10, "Em Star Wars, quem é o pai de Luke Skywalker?",
   ["Darth Vader", "Obi-Wan Kenobi", "Han Solo", "Yoda"], "Darth Vader",
   "A revelação 'Eu sou seu pai' aparece em 'O Império Contra-Ataca' (1980). Vader é Anakin Skywalker.",
   "Lucasfilm – StarWars.com Databank", syn=["anakin", "anakin skywalker", "vader"])
mc(F, "ficção científica", 2, 10, "Qual filme de James Cameron, de 2009, se passa na lua Pandora?",
   ["Avatar", "Titanic", "O Exterminador do Futuro", "Aliens"], "Avatar",
   "Avatar está entre as maiores bilheterias da história do cinema.",
   "Box Office Mojo – All Time Worldwide")
mc(F, "super-heróis", 2, 10, "Qual é a identidade secreta do Homem-Aranha?",
   ["Peter Parker", "Bruce Wayne", "Clark Kent", "Tony Stark"], "Peter Parker",
   "Peter Parker foi picado por uma aranha radioativa. Bruce Wayne é o Batman e Clark Kent é o Superman.",
   "Marvel – Spider-Man", syn=["parker"])
mc(F, "diretores", 2, 12, "Quem dirigiu os filmes 'Tubarão' (1975) e 'E.T. – O Extraterrestre' (1982)?",
   ["Steven Spielberg", "George Lucas", "James Cameron", "Martin Scorsese"], "Steven Spielberg",
   "Spielberg também dirigiu 'Jurassic Park' e 'A Lista de Schindler'.",
   "AFI Catalog – Steven Spielberg", syn=["spielberg"])
mc(F, "atores", 2, 12, "Qual ator interpretou o capitão Jack Sparrow em 'Piratas do Caribe'?",
   ["Johnny Depp", "Orlando Bloom", "Brad Pitt", "Tom Cruise"], "Johnny Depp",
   "Depp foi indicado ao Oscar pelo papel no primeiro filme da série, de 2003.",
   "Academy Awards Database – 76º Oscar", syn=["depp"])
mc(F, "clássicos", 2, 12, "Em 'O Mágico de Oz', qual é o nome da menina que vai parar na terra de Oz?",
   ["Dorothy", "Alice", "Wendy", "Matilda"], "Dorothy",
   "No filme de 1939, Dorothy foi interpretada por Judy Garland.",
   "AFI Catalog – The Wizard of Oz (1939)")
mc(F, "atores", 2, 12, "Qual atriz interpretou Hermione Granger nos filmes de Harry Potter?",
   ["Emma Watson", "Emma Stone", "Natalie Portman", "Kristen Stewart"], "Emma Watson",
   "Emma Watson tinha 9 anos quando foi escolhida para o papel.",
   "Warner Bros. – Harry Potter cast")
mc(F, "cinema brasileiro", 3, 14, "Qual filme brasileiro de 2002, dirigido por Fernando Meirelles, retrata o crescimento do crime em um conjunto habitacional do Rio?",
   ["Cidade de Deus", "Tropa de Elite", "Central do Brasil", "Carandiru"], "Cidade de Deus",
   "O filme recebeu 4 indicações ao Oscar de 2004, incluindo Melhor Direção.",
   "Academy Awards Database – 76º Oscar", br=True)
mc(F, "cinema brasileiro", 3, 14, "Qual atriz brasileira foi indicada ao Oscar de Melhor Atriz por 'Central do Brasil'?",
   ["Fernanda Montenegro", "Fernanda Torres", "Sônia Braga", "Glória Pires"], "Fernanda Montenegro",
   "Foi a primeira indicação de uma atriz brasileira nessa categoria, no Oscar de 1999.",
   "Academy Awards Database – 71º Oscar", syn=["montenegro"], br=True)
mc(F, "cinema brasileiro", 3, 12, "Qual filme brasileiro venceu o Oscar de Melhor Filme Internacional em 2025?",
   ["Ainda Estou Aqui", "Central do Brasil", "Cidade de Deus", "O Auto da Compadecida"], "Ainda Estou Aqui",
   "Dirigido por Walter Salles, foi o primeiro filme brasileiro a vencer nessa categoria.",
   "Academy Awards Database – 97º Oscar (março de 2025)", br=True, ref="Oscar 2025")
mc(F, "cinema brasileiro", 3, 16, "Qual filme de 2007, dirigido por José Padilha, tem o Capitão Nascimento como protagonista?",
   ["Tropa de Elite", "Cidade de Deus", "Carandiru", "O Som ao Redor"], "Tropa de Elite",
   "O filme ganhou o Urso de Ouro no Festival de Berlim de 2008.",
   "Berlinale – Prêmios de 2008", br=True)
mc(F, "cinema brasileiro", 4, 14, "Qual diretor brasileiro dirigiu 'Central do Brasil' (1998)?",
   ["Walter Salles", "Fernando Meirelles", "José Padilha", "Glauber Rocha"], "Walter Salles",
   "O filme venceu o Urso de Ouro em Berlim e o Globo de Ouro de filme estrangeiro.",
   "Berlinale – Prêmios de 1998", syn=["salles"], br=True)
mc(F, "cinema brasileiro", 4, 16, "Qual cineasta do Cinema Novo dirigiu 'Deus e o Diabo na Terra do Sol' (1964)?",
   ["Glauber Rocha", "Nelson Pereira dos Santos", "Cacá Diegues", "Anselmo Duarte"], "Glauber Rocha",
   "Glauber é associado à frase 'uma câmera na mão e uma ideia na cabeça'.",
   "Cinemateca Brasileira – Filmografia", syn=["glauber"], br=True)

# ---- perguntas infantis adicionais (6+)
mc(G, "clima", 1, 6, "Em qual destes lugares costuma fazer mais frio?",
   ["No Polo Sul", "No deserto do Saara", "Na praia de Copacabana", "Na Floresta Amazônica"], "No Polo Sul",
   "A Antártida, onde fica o Polo Sul, é o continente mais frio do planeta.",
   "NASA Earth Observatory – Antarctica", syn=["polo sul", "antartida"])
mc(H, "transportes", 1, 6, "Antes de existir o carro, qual animal as pessoas usavam muito para viajar?",
   ["Cavalo", "Pinguim", "Golfinho", "Coelho"], "Cavalo",
   "Cavalos puxavam carroças e carruagens e eram montados para viagens longas.",
   "Museu Imperial (Petrópolis) – Transportes no século XIX")
mc(C, "astronomia", 1, 6, "Qual estrela ilumina a Terra durante o dia?",
   ["O Sol", "A Lua", "Marte", "Vênus"], "O Sol",
   "O Sol é uma estrela; a Lua e os planetas não têm luz própria.",
   "NASA – Sun Facts", syn=["sol"])
mc(T, "aparelhos", 1, 6, "Qual aparelho usamos para fazer ligações e mandar mensagens?",
   ["Celular", "Torradeira", "Bicicleta", "Relógio de parede"], "Celular",
   "Os celulares de hoje também são computadores de bolso.",
   "Anatel – Telefonia móvel", syn=["telefone", "smartphone", "telefone celular"])
mc(F, "super-heróis", 1, 6, "Qual destes super-heróis solta teias, como uma aranha?",
   ["Homem-Aranha", "Batman", "Hulk", "Superman"], "Homem-Aranha",
   "O Homem-Aranha foi criado por Stan Lee e Steve Ditko em 1962.",
   "Marvel – Spider-Man", syn=["homem aranha", "spider man", "aranha"])
