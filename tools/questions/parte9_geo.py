# Perguntas novas: geografia. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "geo"
REF = "2026-10-13"

# ======================================================== FÁCEIS (idade 6–8)
mc(T, "mapas", 1, 6, "Na maioria dos mapas, qual ponto cardeal fica na parte de cima?",
   ["Norte", "Sul", "Leste", "Oeste"], "Norte",
   "Por convenção, quase todos os mapas são desenhados com o norte voltado para cima.",
   "IBGE – Atlas Geográfico Escolar")
op(T, "pontos cardeais", 1, 7, "Quantos são os pontos cardeais?", "4", ["4", "quatro"],
   "Os pontos cardeais são quatro: norte, sul, leste e oeste.",
   "IBGE – Atlas Geográfico Escolar")
op(T, "mapas", 1, 6, "Que cor costuma representar os rios, os lagos e os mares nos mapas?", "Azul", ["azul"],
   "Nos mapas, a água é quase sempre pintada de azul, para ficar fácil de reconhecer.",
   "IBGE – Atlas Geográfico Escolar")
mc(T, "paisagens", 1, 6, "Como se chama o lugar onde o mar encontra a terra, com areia e ondas?",
   ["Praia", "Floresta", "Montanha", "Caverna"], "Praia",
   "A praia é a faixa de areia ou pedrinhas que fica à beira do mar.",
   "IBGE – Vocabulário Básico de Recursos Naturais e Meio Ambiente")
mc(T, "paisagens", 1, 6, "Qual destes lugares é cheio de árvores bem próximas umas das outras?",
   ["Floresta", "Deserto", "Geleira", "Praia"], "Floresta",
   "Uma floresta é uma área grande coberta por muitas árvores, como a Floresta Amazônica.",
   "IBGE – Vocabulário Básico de Recursos Naturais e Meio Ambiente")
tf(T, "clima", 1, 6, "No Polo Norte faz muito calor o ano inteiro.", False,
   "O Polo Norte é uma das regiões mais frias da Terra, coberta por gelo flutuando no mar.",
   "Enciclopédia Britannica – verbete 'North Pole'")
mc(T, "mapas", 1, 7, "Como se chama a bola com o mapa do planeta desenhado, usada nas escolas?",
   ["Globo terrestre", "Bússola", "Telescópio", "Ampulheta"], "Globo terrestre",
   "O globo terrestre é a representação da Terra mais parecida com o formato real do planeta.",
   "IBGE – Atlas Geográfico Escolar", syn=("globo",))
mc(T, "paisagens", 1, 7, "Como se chama um rio pequeno, estreito e com pouca água?",
   ["Riacho", "Oceano", "Golfo", "Lago"], "Riacho",
   "Riacho, ou córrego, é um curso de água pequeno que muitas vezes deságua num rio maior.",
   "IBGE – Vocabulário Básico de Recursos Naturais e Meio Ambiente")
tf(T, "continentes", 1, 8, "A Antártida é um continente quase todo coberto de gelo.", True,
   "Cerca de 98% da Antártida fica debaixo de uma enorme camada de gelo.",
   "Enciclopédia Britannica – verbete 'Antarctica'")
op(T, "países", 1, 8, "Em qual país ficam as pirâmides de Gizé?", "Egito", ["egito"],
   "As pirâmides de Gizé ficam bem perto da cidade do Cairo, a capital do Egito.",
   "Enciclopédia Britannica – verbete 'Pyramids of Giza'")
mc(T, "continentes", 1, 8, "Qual destes países fica na Europa?",
   ["Itália", "Egito", "Peru", "Japão"], "Itália",
   "A Itália fica no sul da Europa e tem o formato de uma bota.",
   "Enciclopédia Britannica – verbete 'Italy'")

# ======================================================== FÁCEIS (idade 9–10)
mc(T, "línguas", 1, 8, "Qual é a língua falada pela maioria das pessoas na Argentina?",
   ["Espanhol", "Português", "Inglês", "Francês"], "Espanhol",
   "A Argentina foi colônia da Espanha, por isso quase todo mundo lá fala espanhol.",
   "Enciclopédia Britannica – verbete 'Argentina'")
op(T, "cidades do mundo", 1, 9, "Em qual país fica a cidade de Nova York?", "Estados Unidos",
   ["estados unidos", "eua", "estados unidos da américa", "estados unidos da america"],
   "Nova York é a cidade mais populosa dos Estados Unidos.",
   "Enciclopédia Britannica – verbete 'New York City'")
mc(T, "oceanos", 1, 9, "Qual oceano fica entre a América e a Europa?",
   ["Atlântico", "Pacífico", "Índico", "Glacial Antártico"], "Atlântico",
   "O oceano Atlântico separa as Américas, a oeste, da Europa e da África, a leste.",
   "Enciclopédia Britannica – verbete 'Atlantic Ocean'")
mc(T, "mapas", 1, 9, "Como se chama a parte do mapa que explica o significado de cada cor e símbolo?",
   ["Legenda", "Escala", "Rosa dos ventos", "Coordenada"], "Legenda",
   "A legenda funciona como um dicionário do mapa, mostrando o que cada símbolo representa.",
   "IBGE – Atlas Geográfico Escolar")
mc(T, "mapas", 1, 9, "Qual desenho, num mapa, indica as direções norte, sul, leste e oeste?",
   ["Rosa dos ventos", "Legenda", "Escala", "Fuso horário"], "Rosa dos ventos",
   "A rosa dos ventos mostra os pontos cardeais e, às vezes, também os colaterais, como nordeste.",
   "IBGE – Atlas Geográfico Escolar")
tf(T, "ilhas", 1, 9, "O Japão é um país formado por ilhas.", True,
   "O Japão é um arquipélago; suas quatro maiores ilhas são Honshu, Hokkaido, Kyushu e Shikoku.",
   "Enciclopédia Britannica – verbete 'Japan'")
tf(T, "rios", 1, 9, "A água dos rios corre das partes mais altas do terreno para as mais baixas.", True,
   "Puxada pela gravidade, a água desce da nascente, nas partes altas, até a foz.",
   "IBGE – Vocabulário Básico de Recursos Naturais e Meio Ambiente")
mc(T, "regiões do Brasil", 1, 9, "Em qual região do Brasil fica o estado do Amazonas?",
   ["Norte", "Nordeste", "Centro-Oeste", "Sudeste"], "Norte",
   "O Amazonas é o maior dos sete estados da região Norte.",
   "IBGE – Divisão Regional do Brasil", br=True)
mc(T, "regiões do Brasil", 1, 10, "Em qual região do Brasil fica Brasília?",
   ["Centro-Oeste", "Sudeste", "Norte", "Nordeste"], "Centro-Oeste",
   "Brasília fica no Distrito Federal, que faz parte da região Centro-Oeste.",
   "IBGE – Divisão Regional do Brasil", br=True)
tf(T, "regiões do Brasil", 1, 9, "O Rio Grande do Sul fica na região Nordeste.", False,
   "O Rio Grande do Sul faz parte da região Sul, junto com o Paraná e Santa Catarina.",
   "IBGE – Divisão Regional do Brasil", br=True)
tf(T, "florestas", 1, 10, "A Floresta Amazônica fica somente no território brasileiro.", False,
   "A floresta se espalha por nove países e territórios da América do Sul, embora a maior parte esteja no Brasil.",
   "Enciclopédia Britannica – verbete 'Amazon Rainforest'", br=True)
mc(T, "linhas imaginárias", 1, 10, "Qual linha imaginária divide a Terra em hemisfério norte e hemisfério sul?",
   ["Linha do Equador", "Meridiano de Greenwich", "Trópico de Capricórnio", "Círculo Polar Ártico"],
   "Linha do Equador",
   "A Linha do Equador dá a volta na Terra exatamente no meio, entre os dois polos.",
   "IBGE – Atlas Geográfico Escolar", syn=("equador",))
mc(T, "população", 1, 10, "Qual é o país mais populoso da América do Sul?",
   ["Brasil", "Argentina", "Colômbia", "Peru"], "Brasil",
   "Com cerca de 203 milhões de habitantes no Censo 2022, o Brasil tem mais gente que todos os vizinhos.",
   "IBGE – Censo Demográfico 2022", br=True, ref=REF)
tf(T, "fronteiras", 1, 10, "O Chile faz fronteira com o Brasil.", False,
   "Na América do Sul, só o Chile e o Equador não fazem fronteira com o Brasil.",
   "IBGE – Países Vizinhos", br=True)
mc(T, "cidades do mundo", 1, 10, "Qual cidade italiana tem canais no lugar de muitas ruas e passeios de gôndola?",
   ["Veneza", "Roma", "Milão", "Nápoles"], "Veneza",
   "Veneza foi construída sobre mais de cem ilhas numa lagoa, ligadas por canais e pontes.",
   "Enciclopédia Britannica – verbete 'Venice'")
mc(T, "países", 1, 10, "Qual país sul-americano tem Lima como capital?",
   ["Peru", "Equador", "Bolívia", "Colômbia"], "Peru",
   "Lima fica no litoral do oceano Pacífico e foi fundada pelos espanhóis em 1535.",
   "Enciclopédia Britannica – verbete 'Lima'")

# ======================================================== MÉDIAS
mc(T, "cidades turísticas", 2, 12, "Qual cidade paranaense fica na tríplice fronteira entre Brasil, Argentina e Paraguai?",
   ["Foz do Iguaçu", "Cascavel", "Londrina", "Maringá"], "Foz do Iguaçu",
   "Foz do Iguaçu recebe turistas do mundo todo por causa das cataratas e da usina de Itaipu.",
   "IBGE – Cidades", br=True)
mc(T, "cidades turísticas", 2, 12, "Bonito, cidade famosa por rios de água cristalina onde se pode flutuar entre peixes, fica em qual estado?",
   ["Mato Grosso do Sul", "Mato Grosso", "Goiás", "Tocantins"], "Mato Grosso do Sul",
   "Os rios de Bonito são transparentes porque a água passa por rochas de calcário.",
   "IBGE – Cidades", br=True)
mc(T, "cidades turísticas", 2, 10, "Qual parque nacional tem enormes dunas de areia branca com lagoas de água da chuva entre elas?",
   ["Lençóis Maranhenses", "Chapada Diamantina", "Serra da Capivara", "Aparados da Serra"],
   "Lençóis Maranhenses",
   "As lagoas dos Lençóis Maranhenses se enchem na época das chuvas, entre as dunas do litoral do Maranhão.",
   "ICMBio – Parque Nacional dos Lençóis Maranhenses", br=True)
mc(T, "cidades turísticas", 2, 12, "Qual chapada da Bahia é famosa por grutas, cachoeiras e pelo Morro do Pai Inácio?",
   ["Chapada Diamantina", "Chapada dos Veadeiros", "Chapada dos Guimarães", "Chapada do Araripe"],
   "Chapada Diamantina",
   "A Chapada Diamantina recebeu esse nome por causa da exploração de diamantes no século 19.",
   "ICMBio – Parque Nacional da Chapada Diamantina", br=True)
mc(T, "regiões do Brasil", 2, 12, "O Espírito Santo pertence a qual região do Brasil?",
   ["Sudeste", "Nordeste", "Sul", "Centro-Oeste"], "Sudeste",
   "O Sudeste é formado por São Paulo, Rio de Janeiro, Minas Gerais e Espírito Santo.",
   "IBGE – Divisão Regional do Brasil", br=True)
op(T, "regiões do Brasil", 2, 12, "Em quantas grandes regiões o IBGE divide o Brasil?", "5", ["5", "cinco"],
   "As cinco regiões são Norte, Nordeste, Centro-Oeste, Sudeste e Sul.",
   "IBGE – Divisão Regional do Brasil", br=True)
mc(T, "população", 2, 12, "Qual é a região mais populosa do Brasil?",
   ["Sudeste", "Nordeste", "Sul", "Norte"], "Sudeste",
   "No Censo 2022, o Sudeste tinha cerca de 84,8 milhões de habitantes, perto de 42% da população do país.",
   "IBGE – Censo Demográfico 2022", br=True, ref=REF)
mc(T, "população", 2, 12, "Qual estado brasileiro tem a maior população?",
   ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia"], "São Paulo",
   "No Censo 2022, São Paulo tinha mais de 44 milhões de habitantes, cerca de um quinto dos brasileiros.",
   "IBGE – Censo Demográfico 2022", br=True, ref=REF)
mc(T, "população", 2, 13, "Segundo o Censo 2022 do IBGE, quantas pessoas viviam no Brasil, aproximadamente?",
   ["203 milhões", "150 milhões", "250 milhões", "120 milhões"], "203 milhões",
   "O Censo 2022 contou 203.080.756 habitantes no Brasil.",
   "IBGE – Censo Demográfico 2022", br=True, ref=REF,
   syn=("203 milhões", "duzentos e três milhões"))
mc(T, "linhas imaginárias", 2, 12, "Qual capital brasileira é cortada pela Linha do Equador e tem um monumento chamado Marco Zero?",
   ["Macapá", "Belém", "Boa Vista", "São Luís"], "Macapá",
   "O monumento Marco Zero do Equador, em Macapá, marca o lugar por onde passa a linha.",
   "IBGE – Cidades", br=True)
tf(T, "linhas imaginárias", 2, 13, "O Trópico de Capricórnio passa pelo estado de São Paulo.", True,
   "O Trópico de Capricórnio atravessa o Mato Grosso do Sul, o Paraná e São Paulo, passando perto da capital paulista.",
   "IBGE – Atlas Geográfico Escolar", br=True)
tf(T, "linhas imaginárias", 2, 13, "O Trópico de Câncer fica no hemisfério sul.", False,
   "O Trópico de Câncer fica no hemisfério norte; no hemisfério sul fica o Trópico de Capricórnio.",
   "IBGE – Atlas Geográfico Escolar")
mc(T, "linhas imaginárias", 2, 13, "Qual linha imaginária passa por Londres e serve de referência para os fusos horários do mundo?",
   ["Meridiano de Greenwich", "Linha do Equador", "Trópico de Câncer", "Círculo Polar Ártico"],
   "Meridiano de Greenwich",
   "O meridiano de Greenwich marca a longitude zero e passa pelo Observatório Real, em Londres.",
   "Royal Museums Greenwich – 'The Prime Meridian'", syn=("greenwich",))
mc(T, "capitais", 2, 12, "São Luís, capital construída sobre uma ilha, é capital de qual estado?",
   ["Maranhão", "Piauí", "Pará", "Ceará"], "Maranhão",
   "São Luís fica na Ilha do Maranhão e tem um centro histórico tombado como Patrimônio Mundial.",
   "IBGE – Cidades", br=True)
op(T, "capitais", 2, 12, "Qual é a capital do Espírito Santo, cidade construída em grande parte sobre uma ilha?",
   "Vitória", ["vitória", "vitoria"],
   "O centro de Vitória fica numa ilha cercada pela baía de Vitória e pelo oceano Atlântico.",
   "IBGE – Cidades", br=True)
tf(T, "fronteiras", 2, 12, "A Guiana Francesa, vizinha do Amapá, é um território da França.", True,
   "Por causa da Guiana Francesa, a fronteira mais longa da França com outro país é a fronteira com o Brasil.",
   "Enciclopédia Britannica – verbete 'French Guiana'", br=True)
mc(T, "clima", 2, 12, "Qual é o tipo de clima do sertão nordestino, quente e com pouca chuva?",
   ["Semiárido", "Equatorial", "Temperado", "Polar"], "Semiárido",
   "No semiárido, as chuvas são escassas e se concentram em poucos meses do ano.",
   "IBGE – Mapa de Clima do Brasil", br=True)
mc(T, "montanhas", 2, 13, "Qual é a montanha mais alta das Américas, que fica na Argentina?",
   ["Aconcágua", "Chimborazo", "Denali", "Huascarán"], "Aconcágua",
   "O Aconcágua, nos Andes, tem cerca de 6.960 metros de altitude.",
   "Enciclopédia Britannica – verbete 'Aconcagua'")
mc(T, "maravilhas naturais", 2, 12, "Qual cânion gigante, cavado pelo rio Colorado, fica nos Estados Unidos?",
   ["Grand Canyon", "Cânion do Itaimbezinho", "Cânion de Colca", "Cânion de Fish River"], "Grand Canyon",
   "O Grand Canyon, no Arizona, chega a cerca de 1.800 metros de profundidade.",
   "Enciclopédia Britannica – verbete 'Grand Canyon'")
mc(T, "maravilhas naturais", 2, 12, "Quais famosas quedas-d'água ficam na fronteira entre os Estados Unidos e o Canadá?",
   ["Cataratas do Niágara", "Cataratas Vitória", "Cataratas do Iguaçu", "Salto Ángel"], "Cataratas do Niágara",
   "As Cataratas do Niágara ficam no rio Niágara, entre os lagos Erie e Ontário.",
   "Enciclopédia Britannica – verbete 'Niagara Falls'", syn=("niágara", "niagara"))
mc(T, "mares", 2, 12, "Qual mar, entre Israel e a Jordânia, é tão salgado que as pessoas boiam com facilidade?",
   ["Mar Morto", "Mar Vermelho", "Mar Negro", "Mar Cáspio"], "Mar Morto",
   "O Mar Morto tem água muitas vezes mais salgada que a do oceano, e nenhum peixe consegue viver nela.",
   "Enciclopédia Britannica – verbete 'Dead Sea'")
mc(T, "canais", 2, 12, "Qual canal, na América Central, liga o oceano Atlântico ao oceano Pacífico?",
   ["Canal do Panamá", "Canal de Suez", "Canal da Mancha", "Canal de Corinto"], "Canal do Panamá",
   "O Canal do Panamá foi inaugurado em 1914 e poupa os navios de contornar toda a América do Sul.",
   "Enciclopédia Britannica – verbete 'Panama Canal'")
mc(T, "línguas", 2, 12, "Qual é a língua oficial do Egito?",
   ["Árabe", "Francês", "Grego", "Inglês"], "Árabe",
   "O árabe é a língua oficial do Egito e de muitos outros países do norte da África e do Oriente Médio.",
   "Enciclopédia Britannica – verbete 'Egypt'")

# ======================================================== DIFÍCEIS
mc(T, "pontos extremos", 3, 14, "Em qual estado fica o monte Caburaí, ponto extremo norte do Brasil?",
   ["Roraima", "Amapá", "Amazonas", "Pará"], "Roraima",
   "O monte Caburaí fica na fronteira com a Guiana e substituiu o Oiapoque como extremo norte nos livros.",
   "IBGE – Pontos Extremos do Brasil", br=True)
tf(T, "pontos extremos", 3, 14, "O ponto extremo sul do Brasil fica no arroio Chuí, no Rio Grande do Sul.", True,
   "O arroio Chuí, na fronteira com o Uruguai, marca o ponto mais ao sul do território brasileiro.",
   "IBGE – Pontos Extremos do Brasil", br=True)
mc(T, "ilhas", 3, 14, "Qual é a maior ilha fluviomarinha do mundo, cercada por rios e pelo oceano, no Pará?",
   ["Marajó", "Bananal", "Ilha Grande", "Ilhabela"], "Marajó",
   "A Ilha de Marajó, na foz do Amazonas, é famosa pelos búfalos e pela cerâmica marajoara.",
   "IBGE – Cidades", br=True)
tf(T, "ilhas", 3, 14, "A Ilha do Bananal, no Tocantins, é considerada a maior ilha fluvial do mundo.", True,
   "A Ilha do Bananal fica entre os rios Araguaia e Javaés e é cercada apenas por água doce.",
   "IBGE – Cidades", br=True)
op(T, "rios", 3, 14, "Como se chama o fenômeno de ondas que sobem a foz de um rio quando a maré encontra a correnteza, comum no Pará e no Amapá?",
   "Pororoca", ["pororoca"],
   "O nome vem do tupi e lembra o estrondo das águas quando a onda avança rio acima.",
   "Enciclopédia Britannica – verbete 'Bore'", br=True)
tf(T, "rios", 3, 14, "O rio Amazonas nasce no Brasil.", False,
   "O Amazonas nasce na cordilheira dos Andes, no Peru (o ponto exato da nascente ainda é debatido), e entra no Brasil já como um rio caudaloso.",
   "Enciclopédia Britannica – verbete 'Amazon River'", br=True)
mc(T, "rios", 3, 14, "Qual é o rio mais longo da Ásia?",
   ["Yangtzé", "Ganges", "Mekong", "Eufrates"], "Yangtzé",
   "O Yangtzé, na China, tem cerca de 6.300 quilômetros e é o terceiro rio mais longo do mundo.",
   "Enciclopédia Britannica – verbete 'Yangtze River'", syn=("yangtze", "rio azul"))
mc(T, "línguas", 3, 14, "Qual país do Sudeste Asiático tem o português como uma de suas línguas oficiais?",
   ["Timor-Leste", "Filipinas", "Tailândia", "Vietnã"], "Timor-Leste",
   "Timor-Leste foi colônia portuguesa e tem o português e o tétum como línguas oficiais.",
   "Comunidade dos Países de Língua Portuguesa (CPLP)")
mc(T, "lagos", 3, 14, "Qual é o maior lago do mundo em área, que fica entre a Europa e a Ásia mas é chamado de mar?",
   ["Mar Cáspio", "Mar de Aral", "Mar Negro", "Mar Báltico"], "Mar Cáspio",
   "O Cáspio é cercado de terra por todos os lados, por isso é considerado o maior lago do planeta.",
   "Enciclopédia Britannica – verbete 'Caspian Sea'", syn=("cáspio", "caspio"))
mc(T, "maravilhas naturais", 3, 14, "Em qual país fica o Salto Ángel, a cachoeira mais alta do mundo?",
   ["Venezuela", "Colômbia", "Brasil", "Guiana"], "Venezuela",
   "O Salto Ángel tem cerca de 979 metros de queda e fica no Parque Nacional Canaima.",
   "Enciclopédia Britannica – verbete 'Angel Falls'")
tf(T, "desertos", 3, 14, "Contando também os desertos gelados, o Saara é o maior deserto do mundo.", False,
   "Deserto é todo lugar onde cai pouquíssima chuva ou neve, e a Antártida, o maior deserto polar, é maior que o Saara.",
   "Enciclopédia Britannica – verbete 'Desert'")
mc(T, "estados", 3, 14, "Qual é o único estado brasileiro que faz divisa com apenas um outro estado?",
   ["Rio Grande do Sul", "Santa Catarina", "Acre", "Amapá"], "Rio Grande do Sul",
   "O Rio Grande do Sul só faz divisa com Santa Catarina; o resto de suas fronteiras é com o Uruguai e a Argentina.",
   "IBGE – Divisão Regional do Brasil", br=True)

# ======================================================== MUITO DIFÍCEIS
mc(T, "estados", 4, 16, "Qual estado brasileiro faz divisa com o maior número de outros estados?",
   ["Bahia", "Minas Gerais", "Goiás", "Tocantins"], "Bahia",
   "A Bahia faz divisa com oito estados: Sergipe, Alagoas, Pernambuco, Piauí, Tocantins, Goiás, Minas Gerais e Espírito Santo.",
   "IBGE – Divisão Regional do Brasil", br=True)
mc(T, "população", 4, 16, "Segundo o Censo 2022, qual região brasileira é a menos populosa?",
   ["Centro-Oeste", "Norte", "Sul", "Nordeste"], "Centro-Oeste",
   "O Censo 2022 contou cerca de 16,3 milhões de pessoas no Centro-Oeste, um pouco menos que os 17,3 milhões do Norte.",
   "IBGE – Censo Demográfico 2022", br=True, ref=REF)
mc(T, "lagos", 4, 16, "Qual é o maior lago da África, de onde sai o Nilo Branco?",
   ["Lago Vitória", "Lago Tanganica", "Lago Malawi", "Lago Chade"], "Lago Vitória",
   "O lago Vitória é dividido entre Uganda, Quênia e Tanzânia.",
   "Enciclopédia Britannica – verbete 'Lake Victoria'", syn=("vitória", "vitoria"))
mc(T, "estreitos", 4, 16, "Qual estreito separa a Ásia da América do Norte?",
   ["Estreito de Bering", "Estreito de Magalhães", "Estreito de Ormuz", "Estreito de Dardanelos"],
   "Estreito de Bering",
   "No ponto mais estreito, a Rússia e o Alasca ficam a cerca de 85 quilômetros de distância.",
   "Enciclopédia Britannica – verbete 'Bering Strait'", syn=("bering",))
mc(T, "montanhas", 4, 16, "Qual é a montanha mais alta dos Alpes?",
   ["Mont Blanc", "Matterhorn", "Monte Rosa", "Eiger"], "Mont Blanc",
   "O Mont Blanc, na fronteira entre a França e a Itália, tem cerca de 4.800 metros.",
   "Enciclopédia Britannica – verbete 'Mont Blanc'", syn=("monte branco",))
mc(T, "ilhas", 4, 16, "Qual país é o maior arquipélago do mundo, com milhares de ilhas entre a Ásia e a Oceania?",
   ["Indonésia", "Filipinas", "Japão", "Nova Zelândia"], "Indonésia",
   "A Indonésia tem mais de 17 mil ilhas, entre elas Java, Sumatra e Bali.",
   "Enciclopédia Britannica – verbete 'Indonesia'")