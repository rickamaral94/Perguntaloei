# Ampliação dos temas originais (perguntas novas, sem repetir as existentes).
# IDs continuam a numeração de cada tema, então os antigos não mudam.
from qdsl import mc, op, tf

# =========================================================== GEOGRAFIA
G = "geo"
mc(G, "países", 1, 9, "Qual é o maior país do mundo em área?",
   ["Rússia", "Canadá", "China", "Estados Unidos"], "Rússia",
   "A Rússia tem cerca de 17 milhões de km², quase o dobro do Brasil.",
   "Enciclopédia Britannica – verbete 'Russia'", syn=["russia"])
mc(G, "continentes", 1, 9, "Qual é o maior continente do mundo?",
   ["Ásia", "África", "América", "Europa"], "Ásia",
   "A Ásia ocupa cerca de 30% das terras do planeta.",
   "Enciclopédia Britannica – verbete 'Asia'", syn=["asia"])
mc(G, "capitais", 1, 9, "Qual é a capital de Portugal?",
   ["Lisboa", "Porto", "Coimbra", "Braga"], "Lisboa",
   "Lisboa fica às margens do rio Tejo.",
   "Enciclopédia Britannica – verbete 'Lisbon'")
mc(G, "capitais", 1, 9, "Qual é a capital do Japão?",
   ["Tóquio", "Osaka", "Quioto", "Pequim"], "Tóquio",
   "A região metropolitana de Tóquio é uma das mais populosas do mundo.",
   "Enciclopédia Britannica – verbete 'Tokyo'", syn=["toquio", "tokyo"])
mc(G, "continentes", 1, 9, "Em qual continente fica o Egito?",
   ["África", "Ásia", "Europa", "Oceania"], "África",
   "O Egito fica no nordeste da África; a península do Sinai fica na Ásia.",
   "Enciclopédia Britannica – verbete 'Egypt'", syn=["africa"])
mc(G, "capitais", 1, 8, "Qual cidade é a capital da Itália?",
   ["Roma", "Milão", "Veneza", "Nápoles"], "Roma",
   "No meio de Roma fica o Vaticano, um país independente.",
   "Enciclopédia Britannica – verbete 'Rome'")
mc(G, "capitais", 2, 10, "Qual cidade é a capital paraense?",
   ["Belém", "Manaus", "Macapá", "Santarém"], "Belém",
   "Belém fica na foz do rio Pará e é famosa pelo mercado Ver-o-Peso.",
   "IBGE – Cidades", syn=["belem"], br=True)
mc(G, "capitais", 2, 10, "Qual cidade é a capital do Amazonas?",
   ["Manaus", "Belém", "Porto Velho", "Rio Branco"], "Manaus",
   "Em Manaus acontece o Encontro das Águas dos rios Negro e Solimões.",
   "IBGE – Cidades", br=True)
mc(G, "países", 2, 10, "Qual é o menor país do mundo?",
   ["Vaticano", "Mônaco", "San Marino", "Malta"], "Vaticano",
   "O Vaticano tem menos de 0,5 km² e fica dentro de Roma.",
   "Enciclopédia Britannica – verbete 'Vatican City'")
mc(G, "relevo", 2, 10, "Qual cordilheira atravessa a América do Sul de norte a sul, pelo lado oeste?",
   ["Andes", "Alpes", "Himalaia", "Montanhas Rochosas"], "Andes",
   "É a cordilheira mais longa do mundo, com cerca de 7 mil km.",
   "Enciclopédia Britannica – verbete 'Andes'")
mc(G, "oceanos", 2, 12, "Qual oceano banha o litoral do Chile e do Peru?",
   ["Pacífico", "Atlântico", "Índico", "Glacial Ártico"], "Pacífico",
   "O Brasil é banhado pelo Atlântico; o Pacífico fica do outro lado dos Andes.",
   "IBGE – Atlas geográfico escolar", syn=["pacifico"])
mc(G, "regiões", 2, 12, "Qual região brasileira tem mais estados?",
   ["Nordeste", "Norte", "Sudeste", "Sul"], "Nordeste",
   "O Nordeste tem 9 estados; o Norte tem 7, o Sudeste 4 e o Sul 3.",
   "IBGE – Divisão regional do Brasil", br=True)
mc(G, "rios", 3, 14, "Qual é o maior rio totalmente brasileiro, conhecido como 'Velho Chico'?",
   ["São Francisco", "Paraná", "Tocantins", "Tietê"], "São Francisco",
   "Ele nasce em Minas Gerais e deságua entre Alagoas e Sergipe.",
   "Agência Nacional de Águas – Bacia do São Francisco", syn=["rio sao francisco", "sao francisco"], br=True)
mc(G, "litoral", 3, 14, "Qual estado brasileiro tem o maior litoral?",
   ["Bahia", "Rio de Janeiro", "Santa Catarina", "Maranhão"], "Bahia",
   "O litoral baiano tem cerca de 930 km.",
   "IBGE – Brasil em síntese", br=True)
mc(G, "fusos horários", 4, 16, "Quantos fusos horários existem no território brasileiro?",
   ["4", "3", "2", "5"], "4",
   "Do horário de Fernando de Noronha ao do Acre, são quatro fusos.",
   "Observatório Nacional – Hora Legal Brasileira", br=True)
mc(G, "pontos extremos", 4, 16, "Qual é o ponto mais oriental das Américas, que fica na Paraíba?",
   ["Ponta do Seixas", "Cabo de São Roque", "Ponta do Calcanhar", "Cabo Frio"], "Ponta do Seixas",
   "Fica em João Pessoa, perto do farol do Cabo Branco.",
   "IBGE – Pontos extremos do Brasil", br=True)

# =========================================================== HISTÓRIA
H = "his"
mc(H, "comunicação", 1, 6, "Antes do telefone, como as pessoas mandavam notícias para quem estava longe?",
   ["Por cartas", "Por e-mail", "Por mensagem no celular", "Por videochamada"], "Por cartas",
   "As cartas viajavam a cavalo, em navios e depois em trens.",
   "Museu Nacional dos Correios", syn=["cartas", "carta"])
mc(H, "pré-história", 1, 7, "O que os povos pré-históricos usavam para pintar nas paredes das cavernas?",
   ["Pigmentos de terra, carvão e plantas", "Canetinhas coloridas", "Tinta spray", "Giz de cera"], "Pigmentos de terra, carvão e plantas",
   "No Brasil há pinturas rupestres famosas na Serra da Capivara, no Piauí.",
   "IPHAN – Parque Nacional Serra da Capivara", br=False)
mc(H, "Brasil Império", 1, 10, "Quem foi o último imperador do Brasil?",
   ["Dom Pedro II", "Dom Pedro I", "Dom João VI", "Dom Manuel"], "Dom Pedro II",
   "Dom Pedro II reinou de 1840 a 1889 e foi exilado com a Proclamação da República.",
   "Museu Imperial (Petrópolis)", syn=["pedro segundo", "dom pedro segundo"], br=True)
mc(H, "civilizações", 2, 10, "Qual povo construiu a cidade de Machu Picchu, no Peru?",
   ["Incas", "Maias", "Astecas", "Olmecas"], "Incas",
   "Machu Picchu foi construída no século XV, no alto dos Andes.",
   "UNESCO – Historic Sanctuary of Machu Picchu", syn=["os incas", "inca"])
mc(H, "Japão", 2, 10, "Como eram chamados os guerreiros do Japão feudal que seguiam o código bushido?",
   ["Samurais", "Ninjas", "Vikings", "Gladiadores"], "Samurais",
   "Os samurais serviam aos senhores feudais, os daimiôs.",
   "Enciclopédia Britannica – verbete 'samurai'", syn=["samurai"])
mc(H, "Brasil Colônia", 2, 12, "Em que ano a família real portuguesa chegou ao Brasil, fugindo de Napoleão?",
   ["1808", "1822", "1789", "1500"], "1808",
   "A corte de Dom João desembarcou em Salvador e depois se instalou no Rio de Janeiro.",
   "Arquivo Nacional – A Corte no Brasil", br=True)
mc(H, "século XX", 2, 12, "A Segunda Guerra Mundial acabou em qual ano?",
   ["1945", "1944", "1918", "1950"], "1945",
   "A guerra terminou na Europa em maio e no Pacífico em setembro de 1945.",
   "Enciclopédia Britannica – verbete 'World War II'")
mc(H, "século XX", 2, 12, "Qual cidade japonesa foi a primeira atingida por uma bomba atômica, em 1945?",
   ["Hiroshima", "Nagasaki", "Tóquio", "Osaka"], "Hiroshima",
   "Três dias depois, Nagasaki também foi bombardeada.",
   "Hiroshima Peace Memorial Museum")
mc(H, "século XX", 2, 12, "Qual líder sul-africano ficou 27 anos preso e depois se tornou presidente do país?",
   ["Nelson Mandela", "Desmond Tutu", "Steve Biko", "Kofi Annan"], "Nelson Mandela",
   "Mandela ganhou o Nobel da Paz em 1993 e foi eleito presidente em 1994.",
   "Nelson Mandela Foundation", syn=["mandela"])
mc(H, "Antiguidade", 2, 12, "Qual rainha do Egito ficou famosa pelas alianças com Júlio César e Marco Antônio?",
   ["Cleópatra", "Nefertiti", "Hatshepsut", "Rainha de Sabá"], "Cleópatra",
   "Cleópatra VII foi a última governante do Egito ptolomaico.",
   "Enciclopédia Britannica – verbete 'Cleopatra'", syn=["cleopatra"])
mc(H, "resistência", 2, 12, "Qual foi o maior quilombo do Brasil colonial, na Serra da Barriga, atual Alagoas?",
   ["Palmares", "Canudos", "Quilombo do Ambrósio", "Kalunga"], "Palmares",
   "Palmares resistiu por quase um século.",
   "Fundação Cultural Palmares", syn=["quilombo dos palmares"], br=True)
mc(H, "resistência", 2, 12, "O Dia da Consciência Negra, em 20 de novembro, homenageia qual líder quilombola?",
   ["Zumbi dos Palmares", "Tiradentes", "Ganga Zumba", "Chico Rei"], "Zumbi dos Palmares",
   "Zumbi foi morto em 20 de novembro de 1695.",
   "Lei nº 14.759/2023 (feriado nacional)", syn=["zumbi"], br=True)
mc(H, "Revolução Industrial", 2, 12, "O que foi a Revolução Industrial, iniciada na Inglaterra no século XVIII?",
   ["A troca do trabalho manual por máquinas nas fábricas", "Uma guerra entre fábricas", "A invenção da internet", "A descoberta do petróleo no Brasil"],
   "A troca do trabalho manual por máquinas nas fábricas",
   "A máquina a vapor foi o símbolo dessa transformação.",
   "Enciclopédia Britannica – verbete 'Industrial Revolution'")
mc(H, "Era Vargas", 3, 14, "Como ficou conhecido o período de 1930 a 1945 em que Getúlio Vargas governou o Brasil?",
   ["Era Vargas", "República Velha", "Período Regencial", "Brasil Colônia"], "Era Vargas",
   "Inclui o Governo Provisório, o Constitucional e o Estado Novo (1937–1945).",
   "CPDOC/FGV – A Era Vargas", br=True)
mc(H, "conflitos", 3, 14, "Qual foi o maior conflito armado da América do Sul, entre 1864 e 1870, opondo Brasil, Argentina e Uruguai a um país vizinho?",
   ["Guerra do Paraguai", "Guerra dos Farrapos", "Guerra de Canudos", "Guerra da Cisplatina"], "Guerra do Paraguai",
   "Também chamada de Guerra da Tríplice Aliança.",
   "Arquivo Nacional – Guerra do Paraguai", syn=["guerra da triplice alianca"], br=True)
mc(H, "grandes navegações", 3, 14, "Qual navegador português iniciou, em 1519, a primeira viagem de volta ao mundo?",
   ["Fernão de Magalhães", "Bartolomeu Dias", "Vasco da Gama", "Pedro Álvares Cabral"], "Fernão de Magalhães",
   "Magalhães morreu nas Filipinas; Juan Sebastián Elcano completou a viagem em 1522.",
   "Enciclopédia Britannica – verbete 'Ferdinand Magellan'", syn=["magalhaes", "fernao de magalhaes"])
mc(H, "Antiguidade", 3, 14, "Qual faraó egípcio teve a tumba descoberta quase intacta em 1922?",
   ["Tutancâmon", "Ramsés II", "Quéops", "Akhenaton"], "Tutancâmon",
   "A tumba foi encontrada pelo arqueólogo Howard Carter, no Vale dos Reis.",
   "Enciclopédia Britannica – verbete 'Tutankhamun'", syn=["tutancamon", "tutankamon"])
mc(H, "Brasil Império", 4, 16, "Quantos anos Dom Pedro II tinha quando foi declarado maior de idade e assumiu o trono, em 1840?",
   ["14", "18", "21", "16"], "14",
   "O episódio ficou conhecido como Golpe da Maioridade.",
   "Museu Imperial (Petrópolis)", br=True)

# =========================================================== CIÊNCIA
C = "cie"
mc(C, "física", 1, 7, "Os ímãs atraem qual destes materiais?",
   ["Ferro", "Madeira", "Plástico", "Vidro"], "Ferro",
   "Ímãs atraem metais como ferro, níquel e cobalto.",
   "NASA Space Place – Magnetism")
mc(C, "luz", 1, 8, "O arco-íris aparece quando a luz do sol atravessa o quê?",
   ["Gotas de água", "Pedras", "Folhas", "Areia"], "Gotas de água",
   "As gotas funcionam como prismas e separam a luz branca em cores.",
   "NOAA – How rainbows form", syn=["gotas de chuva", "chuva", "agua"])
mc(C, "botânica", 1, 9, "Qual parte da planta faz a maior parte da fotossíntese?",
   ["A folha", "A raiz", "A semente", "A flor"], "A folha",
   "As folhas têm cloroplastos, onde acontece a fotossíntese.",
   "Embrapa – Fotossíntese", syn=["folha", "folhas"])
mc(C, "estados da matéria", 1, 9, "Em graus Celsius, a partir de qual temperatura a água pura vira gelo?",
   ["0 grau", "10 graus", "100 graus", "37 graus"], "0 grau",
   "Ao nível do mar, a água congela a 0 °C.",
   "USGS – Water Science School", syn=["zero", "0", "zero grau"])
mc(C, "botânica", 2, 10, "Qual substância dá a cor verde às plantas?",
   ["Clorofila", "Hemoglobina", "Melanina", "Caroteno"], "Clorofila",
   "A clorofila absorve a luz usada na fotossíntese.",
   "Embrapa – Fotossíntese")
mc(C, "estados da matéria", 2, 10, "Como se chama a passagem da água do estado líquido para o gasoso?",
   ["Vaporização", "Condensação", "Solidificação", "Fusão"], "Vaporização",
   "A evaporação e a ebulição são tipos de vaporização.",
   "USGS – Water Cycle", syn=["evaporacao", "vaporizacao", "ebulicao"])
mc(C, "atmosfera", 2, 12, "Qual é o gás mais abundante no ar que respiramos?",
   ["Nitrogênio", "Oxigênio", "Gás carbônico", "Hélio"], "Nitrogênio",
   "O ar tem cerca de 78% de nitrogênio e 21% de oxigênio.",
   "NASA – Earth's Atmosphere", syn=["nitrogenio", "azoto"])
mc(C, "cientistas", 2, 12, "Qual cientista formulou as leis do movimento e da gravitação universal?",
   ["Isaac Newton", "Galileu Galilei", "Nicolau Copérnico", "Johannes Kepler"], "Isaac Newton",
   "Newton publicou os 'Principia' em 1687.",
   "Enciclopédia Britannica – verbete 'Isaac Newton'", syn=["newton"])
mc(C, "química", 2, 12, "Qual é a fórmula química do gás carbônico?",
   ["CO2", "O2", "H2O", "CH4"], "CO2",
   "Um átomo de carbono e dois de oxigênio.",
   "IUPAC – Compendium of Chemical Terminology", syn=["c o 2", "ce o dois"])
mc(C, "profissões", 2, 12, "Como se chama o cientista que estuda os fósseis?",
   ["Paleontólogo", "Astrônomo", "Geógrafo", "Botânico"], "Paleontólogo",
   "No Brasil há muitos fósseis de dinossauros, como no interior de São Paulo e no Rio Grande do Sul.",
   "Museu Nacional/UFRJ – Paleontologia", syn=["paleontologo", "paleontologista"])
mc(C, "cientistas", 3, 14, "Qual cientista polonesa ganhou dois prêmios Nobel, em Física e em Química?",
   ["Marie Curie", "Rosalind Franklin", "Lise Meitner", "Ada Lovelace"], "Marie Curie",
   "Ela recebeu o Nobel de Física em 1903 e o de Química em 1911.",
   "Nobel Prize – Marie Curie", syn=["curie"])
mc(C, "eletricidade", 3, 14, "Qual unidade mede a corrente elétrica?",
   ["Ampère", "Volt", "Watt", "Ohm"], "Ampère",
   "Volt mede tensão, watt mede potência e ohm mede resistência.",
   "BIPM – Sistema Internacional de Unidades (SI)", syn=["ampere", "amper"])

# =========================================================== TECNOLOGIA
T = "tec"
mc(T, "aparelhos", 1, 6, "Qual aparelho da sala usamos para assistir desenhos?",
   ["Televisão", "Geladeira", "Fogão", "Máquina de lavar"], "Televisão",
   "Hoje também dá para ver desenhos no celular e no tablet.",
   "Anatel – Televisão", syn=["tv", "televisao"])
mc(T, "jogos", 1, 9, "Qual jogo de construção com blocos quadrados, lançado em 2011, é um dos mais vendidos da história?",
   ["Minecraft", "Tetris", "Roblox", "Fortnite"], "Minecraft",
   "Minecraft já vendeu centenas de milhões de cópias.",
   "Mojang Studios – Minecraft")
mc(T, "internet", 1, 9, "O que é um pen drive?",
   ["Um dispositivo para guardar arquivos", "Um tipo de caneta", "Um jogo de corrida", "Um cabo de energia"],
   "Um dispositivo para guardar arquivos",
   "O pen drive usa memória flash e se conecta pela porta USB.",
   "Enciclopédia Britannica – verbete 'flash memory'")
mc(T, "empresas", 1, 10, "Qual empresa criou o sistema operacional Windows?",
   ["Microsoft", "Apple", "Google", "IBM"], "Microsoft",
   "O Windows 1.0 foi lançado em 1985.",
   "Microsoft – Windows history")
mc(T, "internet", 1, 10, "Qual destes programas é um navegador de internet?",
   ["Google Chrome", "Excel", "Photoshop", "Spotify"], "Google Chrome",
   "Outros navegadores: Firefox, Safari e Edge.",
   "Google – Chrome", syn=["chrome"])
mc(T, "assistentes", 1, 10, "Qual é o nome da assistente de voz da Apple?",
   ["Siri", "Alexa", "Cortana", "Bixby"], "Siri",
   "Alexa é da Amazon, Cortana da Microsoft e Bixby da Samsung.",
   "Apple – Siri")
mc(T, "redes sociais", 1, 10, "Qual rede social é focada em vídeos curtos e tem uma nota musical no logotipo?",
   ["TikTok", "LinkedIn", "Pinterest", "Twitch"], "TikTok",
   "O TikTok é da empresa chinesa ByteDance.",
   "TikTok – About", syn=["tik tok"])
mc(T, "invenções", 2, 12, "Qual invento, patenteado por Alexander Graham Bell em 1876, permitiu falar a distância?",
   ["Telefone", "Rádio", "Telégrafo", "Televisão"], "Telefone",
   "Dom Pedro II conheceu o telefone de Bell numa exposição nos Estados Unidos, em 1876.",
   "Enciclopédia Britannica – verbete 'telephone'")
mc(T, "invenções", 2, 12, "Quem desenvolveu uma lâmpada incandescente prática para uso comercial, em 1879?",
   ["Thomas Edison", "Nikola Tesla", "Benjamin Franklin", "James Watt"], "Thomas Edison",
   "Outros inventores já tinham feito lâmpadas, mas a de Edison durava muito mais.",
   "Enciclopédia Britannica – verbete 'Thomas Edison'", syn=["edison"])
mc(T, "videogames", 2, 12, "Qual console da Nintendo, lançado no Japão em 1990, trouxe o jogo 'Super Mario World'?",
   ["Super Nintendo", "Nintendo 64", "Game Boy", "Mega Drive"], "Super Nintendo",
   "O Mega Drive era o concorrente da Sega na mesma época.",
   "Nintendo – história", syn=["snes", "super nes"])
mc(T, "internet", 3, 14, "Quem criou a World Wide Web, em 1989?",
   ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Vint Cerf"], "Tim Berners-Lee",
   "Ele trabalhava no CERN, na Suíça, quando propôs a web.",
   "CERN – The birth of the Web", syn=["berners lee", "tim berners lee"])
mc(T, "siglas", 3, 14, "A conexão USB, usada em cabos e pen drives, é a sigla de quê?",
   ["Universal Serial Bus", "Unidade de Sistema Básico", "Ultra Speed Bit", "Universal System Board"], "Universal Serial Bus",
   "O padrão USB surgiu em 1996.",
   "USB Implementers Forum")
mc(T, "empresas", 3, 14, "Em que ano o Google foi fundado?",
   ["1998", "1994", "2004", "2001"], "1998",
   "Larry Page e Sergey Brin fundaram a empresa na Califórnia.",
   "Google – Our story")

# =========================================================== CINEMA
F = "cin"
mc(F, "super-heróis", 1, 6, "Qual super-heroína usa um laço mágico que obriga as pessoas a dizer a verdade?",
   ["Mulher-Maravilha", "Mulher-Gato", "Supergirl", "Viúva Negra"], "Mulher-Maravilha",
   "Ela foi criada em 1941 e é princesa das amazonas.",
   "DC Comics – Wonder Woman", syn=["mulher maravilha"])
mc(F, "fantasia", 1, 10, "Qual saga de filmes tem os personagens Frodo e Gandalf?",
   ["O Senhor dos Anéis", "Harry Potter", "As Crônicas de Nárnia", "Star Wars"], "O Senhor dos Anéis",
   "A trilogia de Peter Jackson foi filmada na Nova Zelândia.",
   "Warner Bros. – The Lord of the Rings", syn=["senhor dos aneis"])
mc(F, "fantasia", 1, 10, "Qual vilão de Harry Potter é chamado de 'Aquele-que-não-deve-ser-nomeado'?",
   ["Voldemort", "Draco Malfoy", "Severo Snape", "Bellatrix"], "Voldemort",
   "O nome verdadeiro dele é Tom Riddle.",
   "Wizarding World – Lord Voldemort", syn=["lord voldemort"])
mc(F, "ficção científica", 2, 12, "Em 'De Volta para o Futuro', qual carro vira máquina do tempo?",
   ["DeLorean", "Fusca", "Ferrari", "Mustang"], "DeLorean",
   "O carro precisava chegar a 88 milhas por hora para viajar no tempo.",
   "Universal Pictures – Back to the Future (1985)", syn=["de lorean"])
mc(F, "super-heróis", 2, 12, "Qual ator interpretou o Homem de Ferro nos filmes da Marvel?",
   ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"], "Robert Downey Jr.",
   "Ele viveu Tony Stark de 2008 a 2019.",
   "Marvel Studios – Iron Man", syn=["robert downey", "downey junior"])
mc(F, "ficção científica", 2, 12, "Em 'Star Wars', qual princesa é irmã gêmea de Luke?",
   ["Leia", "Padmé", "Rey", "Jyn"], "Leia",
   "A princesa Leia foi interpretada por Carrie Fisher.",
   "Lucasfilm – StarWars.com Databank", syn=["princesa leia"])
mc(F, "ficção científica", 2, 14, "Em qual filme de 1999 o personagem Neo escolhe entre a pílula vermelha e a azul?",
   ["Matrix", "Exterminador do Futuro", "Blade Runner", "Inception"], "Matrix",
   "O filme é das irmãs Wachowski.",
   "Warner Bros. – The Matrix (1999)", syn=["the matrix"])
mc(F, "cinema brasileiro", 2, 12, "Qual filme brasileiro de 2000, baseado em obra de Ariano Suassuna, tem os personagens João Grilo e Chicó?",
   ["O Auto da Compadecida", "Lisbela e o Prisioneiro", "Central do Brasil", "Bicho de Sete Cabeças"], "O Auto da Compadecida",
   "Dirigido por Guel Arraes, ganhou continuação em 2024.",
   "Globo Filmes – O Auto da Compadecida", syn=["auto da compadecida"], br=True)
mc(F, "clássicos", 3, 14, "Como era chamado no Brasil o personagem de Charles Chaplin de chapéu-coco, bengala e bigodinho?",
   ["Carlitos", "Gordo", "Magro", "Mr. Bean"], "Carlitos",
   "Em inglês ele era 'The Tramp', o vagabundo.",
   "Charlie Chaplin Official – The Tramp", syn=["o vagabundo"])
mc(F, "festivais", 3, 14, "Em qual cidade acontece o festival de cinema que entrega a Palma de Ouro?",
   ["Cannes", "Veneza", "Berlim", "Gramado"], "Cannes",
   "O festival acontece todo ano no sul da França.",
   "Festival de Cannes")
mc(F, "prêmios", 3, 14, "Qual filme sul-coreano de 2019 foi o primeiro não falado em inglês a ganhar o Oscar de Melhor Filme?",
   ["Parasita", "Oldboy", "Round 6", "Em Chamas"], "Parasita",
   "O diretor Bong Joon-ho também levou os Oscars de Direção e Roteiro.",
   "Academy Awards Database – 92º Oscar")
mc(F, "cinema brasileiro", 3, 14, "Qual ator interpretou João Grilo no filme de 2000 baseado na obra de Ariano Suassuna?",
   ["Matheus Nachtergaele", "Selton Mello", "Wagner Moura", "Lázaro Ramos"], "Matheus Nachtergaele",
   "Selton Mello interpretou o parceiro dele, Chicó.",
   "Globo Filmes – O Auto da Compadecida", syn=["matheus"], br=True)
mc(F, "diretores", 3, 16, "Quem dirigiu o filme 'Pulp Fiction' (1994)?",
   ["Quentin Tarantino", "Martin Scorsese", "Steven Spielberg", "Christopher Nolan"], "Quentin Tarantino",
   "O filme ganhou a Palma de Ouro em Cannes e o Oscar de Roteiro Original.",
   "Academy Awards Database – 67º Oscar", syn=["tarantino"])

# =========================================================== FILMES INFANTIS
I = "inf"
mc(I, "Pixar", 1, 6, "Em 'Toy Story', qual é o nome do patrulheiro espacial de brinquedo?",
   ["Buzz Lightyear", "Woody", "Rex", "Senhor Cabeça de Batata"], "Buzz Lightyear",
   "O lema dele é: 'Ao infinito e além!'.",
   "Disney/Pixar – Toy Story (1995)", syn=["buzz"])
mc(I, "princesas", 1, 6, "Qual princesa tem cabelos mágicos muito longos e vivia presa numa torre?",
   ["Rapunzel", "Bela", "Jasmine", "Mulan"], "Rapunzel",
   "No filme 'Enrolados' (2010), ela foge da torre com Flynn Rider.",
   "Disney – Enrolados (2010)")
mc(I, "DreamWorks", 1, 6, "Em 'Shrek', qual animal falador é o melhor amigo do ogro?",
   ["O Burro", "O Gato", "O Dragão", "O Lobo"], "O Burro",
   "Na versão brasileira, o Burro ganhou a voz de Mário Jorge.",
   "DreamWorks – Shrek (2001)", syn=["burro", "o burrinho"])
mc(I, "Disney", 1, 6, "Qual é o nome do elefantinho da Disney que voa com suas orelhas enormes?",
   ["Dumbo", "Babar", "Horton", "Manny"], "Dumbo",
   "O filme foi lançado em 1941.",
   "The Walt Disney Company – Dumbo (1941)")
mc(I, "Illumination", 1, 6, "Em 'Meu Malvado Favorito', como se chamam os ajudantes amarelos?",
   ["Minions", "Smurfs", "Gremlins", "Ewoks"], "Minions",
   "Eles falam uma língua própria, cheia de palavras misturadas.",
   "Illumination – Despicable Me (2010)", syn=["minion"])
mc(I, "Disney", 1, 7, "Em 'Lilo & Stitch', de onde vem o Stitch?",
   ["Do espaço", "Do fundo do mar", "De uma floresta", "Do Polo Norte"], "Do espaço",
   "Stitch é o 'Experimento 626', criado por um cientista alienígena.",
   "Disney – Lilo & Stitch (2002)", syn=["espaco", "de outro planeta"])
mc(I, "DreamWorks", 1, 7, "Em 'Kung Fu Panda', qual é o nome do panda protagonista?",
   ["Po", "Shifu", "Tai Lung", "Oogway"], "Po",
   "Po trabalhava na loja de macarrão do pai antes de virar o Dragão Guerreiro.",
   "DreamWorks – Kung Fu Panda (2008)")
mc(I, "Disney", 1, 8, "Em 'O Rei Leão', qual é a frase de Timão e Pumba que quer dizer 'sem preocupações'?",
   ["Hakuna Matata", "Bibbidi-Bobbidi-Boo", "Supercalifragilístico", "Ao infinito e além"], "Hakuna Matata",
   "A expressão vem do suaíli.",
   "Disney – O Rei Leão (1994)")
mc(I, "Pixar", 1, 8, "Qual é o nome do robozinho que limpa o lixo da Terra num filme da Pixar de 2008?",
   ["WALL-E", "EVA", "Baymax", "R2-D2"], "WALL-E",
   "WALL-E se apaixona pela robô EVA.",
   "Disney/Pixar – WALL-E (2008)", syn=["wall e", "wally"])
mc(I, "Pixar", 2, 9, "Em 'Monstros S.A.', qual é o nome do monstro grande, azul e peludo?",
   ["Sulley", "Mike", "Randall", "Boo"], "Sulley",
   "Sulley e Mike trabalham assustando crianças para gerar energia.",
   "Disney/Pixar – Monstros S.A. (2001)", syn=["sullivan", "james p sullivan"])
mc(I, "Pixar", 2, 9, "Em 'Os Incríveis', qual é o superpoder do pequeno Flecha?",
   ["Supervelocidade", "Invisibilidade", "Superforça", "Elasticidade"], "Supervelocidade",
   "A irmã dele, Violeta, fica invisível e cria campos de força.",
   "Disney/Pixar – Os Incríveis (2004)", syn=["velocidade", "correr muito rapido"])
mc(I, "Blue Sky", 2, 9, "Em 'A Era do Gelo', qual é o nome do esquilo obcecado por uma bolota?",
   ["Scrat", "Sid", "Manny", "Diego"], "Scrat",
   "Sid é a preguiça, Manny o mamute e Diego o tigre-dentes-de-sabre.",
   "20th Century Studios – A Era do Gelo (2002)")
mc(I, "Disney", 2, 10, "Em 'A Bela e a Fera', qual objeto encantado é um castiçal?",
   ["Lumière", "Horloge", "Madame Samovar", "Zip"], "Lumière",
   "Horloge é o relógio e Madame Samovar, o bule.",
   "Disney – A Bela e a Fera (1991)", syn=["lumiere"])

# =========================================================== NOVELAS
N = "nov"
mc(N, "personagens", 2, 14, "Em 'A Força do Querer' (2017), qual era o apelido da personagem de Juliana Paes, que ganhou fama de 'Perigosa'?",
   ["Bibi", "Ritinha", "Jeiza", "Irene"], "Bibi",
   "Ritinha foi vivida por Isis Valverde e Jeiza por Paolla Oliveira.",
   "Memória Globo – A Força do Querer", syn=["fabiana", "bibi perigosa"], br=True)
mc(N, "dramas", 2, 14, "Em 'Laços de Família' (2000), qual doença a personagem Camila, de Carolina Dieckmann, enfrentava?",
   ["Leucemia", "Tuberculose", "Malária", "Sarampo"], "Leucemia",
   "A cena em que Camila raspa o cabelo é uma das mais lembradas da teledramaturgia.",
   "Memória Globo – Laços de Família", br=True)
mc(N, "autores", 2, 14, "Qual novela de Benedito Ruy Barbosa contava a história de imigrantes italianos nas fazendas de café?",
   ["Terra Nostra", "O Rei do Gado", "Esperança", "Renascer"], "Terra Nostra",
   "Terra Nostra foi exibida em 1999 e 2000.",
   "Memória Globo – Terra Nostra", br=True)
mc(N, "estrangeiras", 2, 14, "Qual novela mexicana tinha as gêmeas Paola e Paulina, uma vilã e outra boazinha?",
   ["A Usurpadora", "Maria do Bairro", "Marimar", "Rubi"], "A Usurpadora",
   "As duas eram interpretadas por Gabriela Spanic.",
   "Televisa – La Usurpadora (1998)", syn=["usurpadora"])
mc(N, "elenco", 3, 16, "Em qual novela Fernanda Montenegro interpretou a vilã Bia Falcão?",
   ["Belíssima", "Senhora do Destino", "Passione", "Avenida Brasil"], "Belíssima",
   "Belíssima foi exibida entre 2005 e 2006.",
   "Memória Globo – Belíssima", syn=["belissima"], br=True)
mc(N, "elenco", 3, 16, "Em 'O Rei do Gado' (1996), qual ator interpretou o protagonista Bruno Mezenga?",
   ["Antonio Fagundes", "Tarcísio Meira", "Marcos Palmeira", "José Mayer"], "Antonio Fagundes",
   "A novela também tinha Patrícia Pillar como a sem-terra Luana.",
   "Memória Globo – O Rei do Gado", syn=["fagundes"], br=True)
mc(N, "elenco", 3, 16, "Em qual novela Glória Pires interpretou as gêmeas Ruth e Raquel?",
   ["Mulheres de Areia", "Vale Tudo", "O Rei do Gado", "Paraíso Tropical"], "Mulheres de Areia",
   "A versão de 1993 é um remake da novela de 1973.",
   "Memória Globo – Mulheres de Areia", br=True)
mc(N, "personagens", 3, 16, "Em 'A Favorita' (2008), qual era o nome da personagem de Patrícia Pillar, revelada como a vilã?",
   ["Flora", "Donatela", "Carminha", "Nazaré"], "Flora",
   "O mistério sobre quem era a vilã, Flora ou Donatela, prendeu o público durante meses.",
   "Memória Globo – A Favorita", br=True)
mc(N, "personagens", 4, 16, "Em 'Chocolate com Pimenta' (2003), qual era o nome da protagonista vivida por Mariana Ximenes?",
   ["Ana Francisca", "Jezebel", "Celina", "Bárbara"], "Ana Francisca",
   "Jezebel, a vilã, era interpretada por Elizabeth Savala.",
   "Memória Globo – Chocolate com Pimenta", syn=["aninha"], br=True)
mc(N, "cenários", 4, 16, "Em qual bairro fictício do Rio se passava boa parte de 'Avenida Brasil'?",
   ["Divino", "Tijuca", "Copacabana", "Barra"], "Divino",
   "No Divino ficava a casa de Tufão e o Divino Futebol Clube.",
   "Memória Globo – Avenida Brasil", br=True)

# =========================================================== TELEVISÃO
V = "tv"
mc(V, "desenhos", 1, 6, "Qual desenho mostra um gato e um rato que vivem brigando?",
   ["Tom e Jerry", "Pica-Pau", "Pernalonga", "Frajola e Piu-Piu"], "Tom e Jerry",
   "Tom é o gato e Jerry é o rato; a série estreou em 1940.",
   "Warner Bros. – Tom and Jerry", syn=["tom e jerry"])
mc(V, "desenhos", 1, 6, "Qual é o nome do cachorro medroso que resolve mistérios com sua turma?",
   ["Scooby-Doo", "Snoopy", "Pluto", "Bidu"], "Scooby-Doo",
   "O amigo inseparável dele é o Salsicha.",
   "Warner Bros. – Scooby-Doo", syn=["scooby doo", "scooby"])
mc(V, "desenhos", 1, 6, "Em qual desenho japonês aparece o Pikachu?",
   ["Pokémon", "Dragon Ball", "Digimon", "Naruto"], "Pokémon",
   "Pokémon começou como jogo de videogame em 1996.",
   "The Pokémon Company", syn=["pokemon"])
mc(V, "desenhos", 1, 10, "Qual pai de família amarelo e careca dos desenhos diz 'D'oh!' quando erra?",
   ["Homer Simpson", "Fred Flintstone", "Peter Griffin", "Bob Esponja"], "Homer Simpson",
   "Homer trabalha numa usina nuclear.",
   "FOX – The Simpsons", syn=["homer"])
mc(V, "séries", 2, 12, "Qual série da Netflix se passa na cidade de Hawkins e tem o 'Mundo Invertido'?",
   ["Stranger Things", "Dark", "The Witcher", "Wandinha"], "Stranger Things",
   "A série estreou em 2016 e se passa nos anos 1980.",
   "Netflix – Stranger Things")
mc(V, "séries", 2, 14, "Qual série de fantasia da HBO tem o Trono de Ferro e dragões?",
   ["Game of Thrones", "The Witcher", "Vikings", "Merlin"], "Game of Thrones",
   "É baseada nos livros de George R. R. Martin.",
   "HBO – Game of Thrones", syn=["guerra dos tronos"])
mc(V, "apresentadores", 2, 14, "Qual apresentador jogava bacalhau na plateia e dizia 'Quem não se comunica se trumbica'?",
   ["Chacrinha", "Silvio Santos", "Faustão", "Raul Gil"], "Chacrinha",
   "José Abelardo Barbosa, o Chacrinha, foi um dos maiores comunicadores da TV brasileira.",
   "Memória Globo – Chacrinha", syn=["abelardo barbosa"], br=True)
mc(V, "séries", 2, 16, "Qual série sul-coreana da Netflix, de 2021, mostra competições mortais com brincadeiras infantis?",
   ["Round 6", "Kingdom", "Pousando no Amor", "Sweet Home"], "Round 6",
   "No original, chama-se 'Squid Game'.",
   "Netflix – Round 6", syn=["squid game"])
mc(V, "séries", 2, 16, "Qual série mostra um professor de química que passa a fabricar drogas?",
   ["Breaking Bad", "Narcos", "Ozark", "Better Call Saul"], "Breaking Bad",
   "O personagem principal, Walter White, foi vivido por Bryan Cranston.",
   "AMC – Breaking Bad")
mc(V, "história da TV", 3, 14, "Em que ano começaram as transmissões oficiais de TV em cores no Brasil?",
   ["1972", "1950", "1965", "1985"], "1972",
   "A primeira transmissão oficial foi a Festa da Uva, em Caxias do Sul.",
   "Museu da TV; Ministério das Comunicações", br=True)

# =========================================================== ESPORTES
E = "esp"
mc(E, "ciclismo", 1, 6, "Em qual esporte os atletas competem pedalando?",
   ["Ciclismo", "Natação", "Judô", "Vôlei"], "Ciclismo",
   "O Tour de France é a corrida de ciclismo mais famosa do mundo.",
   "União Ciclística Internacional", syn=["bicicleta"])
mc(E, "olimpíadas", 1, 8, "Quantos anéis tem o símbolo olímpico?",
   ["5", "4", "6", "7"], "5",
   "Os anéis entrelaçados representam a união dos continentes.",
   "Comitê Olímpico Internacional – Olympic rings")
mc(E, "tênis de mesa", 1, 8, "Qual esporte se joga com raquetes e uma bolinha leve sobre uma mesa com rede?",
   ["Tênis de mesa", "Badminton", "Squash", "Golfe"], "Tênis de mesa",
   "O brasileiro Hugo Calderano está entre os melhores do mundo.",
   "ITTF – International Table Tennis Federation", syn=["pingue pongue", "ping pong"])
mc(E, "basquete", 1, 9, "Um time de basquete joga com quantos atletas em quadra ao mesmo tempo?",
   ["5", "6", "7", "11"], "5",
   "O basquete foi inventado em 1891 pelo professor James Naismith.",
   "FIBA – Official Basketball Rules")
mc(E, "copas", 1, 10, "Qual craque argentino foi campeão e eleito melhor jogador da Copa de 2022?",
   ["Lionel Messi", "Diego Maradona", "Ángel Di María", "Julián Álvarez"], "Lionel Messi",
   "Messi recebeu a Bola de Ouro da Copa no Catar.",
   "FIFA – Qatar 2022 Awards", syn=["messi"], ref="Copa de 2022")
mc(E, "tênis", 1, 10, "Em qual esporte se disputa o torneio de Wimbledon?",
   ["Tênis", "Golfe", "Críquete", "Polo"], "Tênis",
   "Wimbledon é jogado na grama, em Londres.",
   "The All England Lawn Tennis Club", syn=["tenis"])
mc(E, "vôlei", 2, 12, "Quantos sets um time precisa vencer para ganhar uma partida de vôlei de quadra?",
   ["3", "2", "4", "5"], "3",
   "As partidas são em melhor de cinco sets.",
   "FIVB – Official Volleyball Rules")
mc(E, "atletismo", 2, 12, "Qual é a distância oficial de uma maratona?",
   ["42,195 km", "21 km", "50 km", "10 km"], "42,195 km",
   "A meia-maratona tem metade: 21,0975 km.",
   "World Athletics – Marathon", syn=["42 km", "42 quilometros"])
mc(E, "futebol feminino", 2, 12, "Qual jogadora brasileira foi eleita seis vezes a melhor do mundo pela FIFA?",
   ["Marta", "Formiga", "Cristiane", "Debinha"], "Marta",
   "Marta também é a maior artilheira da história das Copas, somando homens e mulheres.",
   "FIFA – Marta", br=True)
mc(E, "skate", 2, 12, "Qual skatista brasileira, apelidada de 'Fadinha', ganhou medalha olímpica aos 13 anos?",
   ["Rayssa Leal", "Pâmela Rosa", "Letícia Bufoni", "Dora Varella"], "Rayssa Leal",
   "Rayssa ganhou prata em Tóquio 2020 e bronze em Paris 2024.",
   "Comitê Olímpico do Brasil – Rayssa Leal", syn=["rayssa"], br=True, ref="Até os Jogos de Paris 2024")
mc(E, "automobilismo", 3, 14, "Qual piloto brasileiro foi campeão da Fórmula 1 em 1972 e 1974?",
   ["Emerson Fittipaldi", "Nelson Piquet", "Ayrton Senna", "Felipe Massa"], "Emerson Fittipaldi",
   "Emerson foi o primeiro brasileiro campeão da Fórmula 1.",
   "FIA – Formula One World Championship", syn=["emerson", "fittipaldi"], br=True)
mc(E, "olimpíadas", 3, 14, "Em qual cidade aconteceram os primeiros Jogos Olímpicos da era moderna, em 1896?",
   ["Atenas", "Paris", "Londres", "Roma"], "Atenas",
   "A Grécia foi escolhida por ser o berço dos Jogos da Antiguidade.",
   "Comitê Olímpico Internacional – Athens 1896")
mc(E, "futebol americano", 3, 14, "Quantos pontos vale um touchdown no futebol americano?",
   ["6", "3", "7", "2"], "6",
   "Depois do touchdown, o time ainda pode tentar o ponto extra.",
   "NFL – Rules of the game")

# =========================================================== MARCAS
M = "mar"
mc(M, "personagens", 1, 6, "Qual ratinho de calção vermelho é o personagem mais famoso da Disney?",
   ["Mickey Mouse", "Jerry", "Stuart Little", "Remy"], "Mickey Mouse",
   "Mickey estreou em 1928 no desenho 'Steamboat Willie'.",
   "The Walt Disney Company – Mickey Mouse", syn=["mickey"])
mc(M, "logotipos", 1, 10, "Qual empresa de streaming tem um N vermelho no logotipo?",
   ["Netflix", "Nintendo", "Nike", "Nestlé"], "Netflix",
   "A Netflix começou alugando DVDs pelo correio, em 1997.",
   "Netflix – About")
mc(M, "carros", 2, 10, "Qual marca de carros tem um cavalo empinado no logotipo?",
   ["Ferrari", "Lamborghini", "Porsche", "Jaguar"], "Ferrari",
   "A Lamborghini usa um touro; a Jaguar, um felino.",
   "Ferrari – History")
mc(M, "carros", 2, 12, "Qual marca alemã de carros tem quatro argolas no logotipo?",
   ["Audi", "BMW", "Mercedes-Benz", "Volkswagen"], "Audi",
   "As argolas representam quatro empresas que se uniram em 1932.",
   "Audi – History")
mc(M, "logotipos", 2, 12, "Qual rede de cafeterias tem uma sereia no logotipo?",
   ["Starbucks", "Nespresso", "Café Pilão", "Dunkin'"], "Starbucks",
   "A Starbucks nasceu em Seattle, em 1971.",
   "Starbucks – Company profile")
mc(M, "logotipos", 2, 12, "Qual empresa tem no logotipo uma seta que lembra um sorriso?",
   ["Amazon", "Apple", "Samsung", "Mercado Livre"], "Amazon",
   "A seta vai do 'a' ao 'z', sugerindo que vende de tudo.",
   "Amazon – About")
mc(M, "chocolates", 3, 14, "O chocolate Baton é de qual fabricante?",
   ["Garoto", "Nestlé", "Lacta", "Hershey's"], "Garoto",
   "A Garoto foi fundada em Vila Velha, no Espírito Santo, em 1929.",
   "Chocolates Garoto – história", br=True)
mc(M, "chocolates", 3, 14, "O Kinder Ovo, com surpresa dentro, é de qual empresa?",
   ["Ferrero", "Nestlé", "Lacta", "Mars"], "Ferrero",
   "A Ferrero é italiana e também fabrica a Nutella.",
   "Ferrero – Our brands")

# =========================================================== MÚSICA
S = "mus"
mc(S, "instrumentos", 1, 6, "Qual destes instrumentos tem cordas?",
   ["Harpa", "Tambor", "Apito", "Flauta"], "Harpa",
   "A harpa é um dos instrumentos mais antigos do mundo.",
   "Enciclopédia Britannica – verbete 'harp'")
mc(S, "teoria musical", 2, 10, "Quantas linhas tem uma pauta musical?",
   ["5", "4", "6", "7"], "5",
   "As notas são escritas nas linhas e nos espaços da pauta.",
   "Bohumil Med – Teoria da Música")
mc(S, "instrumentos", 2, 10, "Qual instrumento de cordas é tocado com arco e apoiado no ombro?",
   ["Violino", "Violão", "Contrabaixo", "Cavaquinho"], "Violino",
   "O contrabaixo de orquestra também usa arco, mas é tocado em pé.",
   "Enciclopédia Britannica – verbete 'violin'")
mc(S, "pop", 1, 12, "Qual cantora é conhecida como a 'Rainha do Pop'?",
   ["Madonna", "Beyoncé", "Britney Spears", "Lady Gaga"], "Madonna",
   "Madonna lançou seu primeiro álbum em 1983.",
   "Enciclopédia Britannica – verbete 'Madonna'")
mc(S, "gêneros", 1, 12, "Qual gênero musical nasceu na Jamaica e tem Bob Marley como maior ícone?",
   ["Reggae", "Samba", "Blues", "Tango"], "Reggae",
   "O reggae é Patrimônio Cultural Imaterial da Humanidade desde 2018.",
   "UNESCO – Reggae music of Jamaica (2018)")
mc(S, "MPB", 2, 12, "Quem gravou 'Aquarela' (1983), que começa com 'Numa folha qualquer eu desenho um sol amarelo'?",
   ["Toquinho", "Chico Buarque", "Milton Nascimento", "Djavan"], "Toquinho",
   "A canção é adaptação de uma música italiana feita por Toquinho e Maurizio Fabrizio.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(S, "sertanejo", 2, 12, "Qual dupla sertaneja gravou 'Evidências'?",
   ["Chitãozinho & Xororó", "Zezé Di Camargo & Luciano", "Leandro & Leonardo", "Bruno & Marrone"], "Chitãozinho & Xororó",
   "Gravada em 1990, virou um hino nacional dos karaokês.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["chitaozinho e xororo", "chitaozinho"], br=True)
mc(S, "rock", 2, 14, "Qual banda brasileira dos anos 1980 tinha Renato Russo como vocalista?",
   ["Legião Urbana", "Titãs", "Paralamas do Sucesso", "Barão Vermelho"], "Legião Urbana",
   "A banda surgiu em Brasília, em 1982.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["legiao urbana", "legiao"], br=True)
mc(S, "soul", 3, 16, "Qual cantor gravou 'Do Leme ao Pontal' e 'Gostava Tanto de Você'?",
   ["Tim Maia", "Jorge Ben Jor", "Wilson Simonal", "Cassiano"], "Tim Maia",
   "Tim Maia é considerado o pai do soul brasileiro.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(S, "clássica", 3, 16, "Qual compositor brasileiro escreveu as 'Bachianas Brasileiras'?",
   ["Heitor Villa-Lobos", "Carlos Gomes", "Ernesto Nazareth", "Tom Jobim"], "Heitor Villa-Lobos",
   "Villa-Lobos misturou a música de Bach com ritmos brasileiros.",
   "Museu Villa-Lobos", syn=["villa lobos"], br=True)

# =========================================================== LITERATURA
L = "lit"
mc(L, "contos de fadas", 1, 6, "Qual princesa dormiu por muitos anos depois de espetar o dedo num fuso?",
   ["A Bela Adormecida", "Cinderela", "Branca de Neve", "Rapunzel"], "A Bela Adormecida",
   "Na versão da Disney, a princesa se chama Aurora.",
   "Charles Perrault – A Bela Adormecida (1697)", syn=["bela adormecida", "aurora"])
mc(L, "clássicos infantis", 1, 6, "Qual menino criado por lobos é o protagonista de 'O Livro da Selva'?",
   ["Mogli", "Tarzan", "Peter Pan", "Pinóquio"], "Mogli",
   "O livro é de Rudyard Kipling, de 1894; o urso Balu e a pantera Baguera são amigos dele.",
   "Rudyard Kipling – O Livro da Selva (1894)", syn=["mowgli"])
mc(L, "clássicos infantis", 1, 7, "Em 'Alice no País das Maravilhas', qual animal Alice segue até a toca?",
   ["Um coelho branco", "Um gato listrado", "Um rato cinza", "Uma lagarta azul"], "Um coelho branco",
   "O coelho vive dizendo que está atrasado.",
   "Lewis Carroll – Alice no País das Maravilhas (1865)", syn=["coelho", "coelho branco"])
mc(L, "literatura infantil", 1, 8, "Qual personagem de Monteiro Lobato é um sabugo de milho muito sábio?",
   ["Visconde de Sabugosa", "Pedrinho", "Tio Barnabé", "Marquês de Rabicó"], "Visconde de Sabugosa",
   "O Marquês de Rabicó é o porquinho do Sítio.",
   "Monteiro Lobato – Reinações de Narizinho", syn=["visconde"], br=True)
mc(L, "literatura infantil", 1, 9, "Qual escritor criou o personagem 'Menino Maluquinho'?",
   ["Ziraldo", "Ruth Rocha", "Monteiro Lobato", "Pedro Bandeira"], "Ziraldo",
   "O livro, de 1980, mostra o menino com uma panela na cabeça.",
   "Ziraldo – O Menino Maluquinho (1980)", br=True)
mc(L, "best-sellers", 1, 12, "Qual escritor brasileiro escreveu 'O Alquimista'?",
   ["Paulo Coelho", "Jorge Amado", "Fernando Sabino", "Luis Fernando Verissimo"], "Paulo Coelho",
   "O livro, de 1988, foi traduzido para dezenas de idiomas.",
   "Academia Brasileira de Letras – Paulo Coelho", br=True)
mc(L, "romance", 2, 14, "Quem escreveu 'Memórias Póstumas de Brás Cubas'?",
   ["Machado de Assis", "José de Alencar", "Aluísio Azevedo", "Lima Barreto"], "Machado de Assis",
   "O livro é narrado por um 'defunto autor'.",
   "Academia Brasileira de Letras – Machado de Assis", syn=["machado"], br=True)
mc(L, "distopias", 2, 14, "Quem escreveu '1984', livro que criou o 'Grande Irmão'?",
   ["George Orwell", "Aldous Huxley", "Ray Bradbury", "H. G. Wells"], "George Orwell",
   "Orwell também escreveu 'A Revolução dos Bichos'.",
   "Enciclopédia Britannica – verbete 'George Orwell'", syn=["orwell"])
mc(L, "fantasia", 2, 12, "Quem escreveu 'O Hobbit' (1937)?",
   ["J. R. R. Tolkien", "C. S. Lewis", "J. K. Rowling", "Lewis Carroll"], "J. R. R. Tolkien",
   "Tolkien era professor de línguas antigas em Oxford.",
   "The Tolkien Estate", syn=["tolkien"])
mc(L, "regionalismo", 3, 14, "Quem escreveu 'Vidas Secas' (1938)?",
   ["Graciliano Ramos", "Rachel de Queiroz", "José Lins do Rego", "Jorge Amado"], "Graciliano Ramos",
   "O livro conta a história de uma família de retirantes no sertão.",
   "Academia Brasileira de Letras – Graciliano Ramos", syn=["graciliano"], br=True)
mc(L, "naturalismo", 3, 16, "Quem escreveu 'O Cortiço' (1890)?",
   ["Aluísio Azevedo", "Machado de Assis", "Raul Pompeia", "José de Alencar"], "Aluísio Azevedo",
   "O livro retrata a vida num cortiço do Rio de Janeiro.",
   "Academia Brasileira de Letras – Aluísio Azevedo", syn=["aluisio azevedo"], br=True)
mc(L, "poesia", 3, 16, "Qual poeta escreveu 'Vou-me embora pra Pasárgada'?",
   ["Manuel Bandeira", "Mário de Andrade", "Cecília Meireles", "Olavo Bilac"], "Manuel Bandeira",
   "Pasárgada é um lugar imaginário onde o poeta seria 'amigo do rei'.",
   "Academia Brasileira de Letras – Manuel Bandeira", syn=["bandeira"], br=True)
mc(L, "regionalismo", 4, 16, "Em 'Vidas Secas', qual é o nome da cachorra da família?",
   ["Baleia", "Laika", "Pipoca", "Malhada"], "Baleia",
   "O capítulo sobre a morte da Baleia é um dos mais famosos da literatura brasileira.",
   "Graciliano Ramos – Vidas Secas (1938)", br=True)
mc(L, "pré-modernismo", 4, 16, "Quem escreveu 'Os Sertões', sobre a Guerra de Canudos?",
   ["Euclides da Cunha", "Graciliano Ramos", "Guimarães Rosa", "Lima Barreto"], "Euclides da Cunha",
   "Euclides cobriu o conflito como jornalista; o livro saiu em 1902.",
   "Academia Brasileira de Letras – Euclides da Cunha", syn=["euclides"], br=True)

# =========================================================== NATUREZA
A = "nat"
mc(A, "animais", 1, 6, "Qual inseto produz o mel?",
   ["Abelha", "Formiga", "Mosca", "Joaninha"], "Abelha",
   "As abelhas também polinizam as flores, ajudando as plantas a darem frutos.",
   "Embrapa – Abelhas e polinização")
mc(A, "animais", 1, 6, "Qual destas aves não voa, mas nada muito bem em mares gelados?",
   ["Pinguim", "Gaivota", "Papagaio", "Águia"], "Pinguim",
   "As asas do pinguim funcionam como nadadeiras.",
   "Australian Antarctic Program – Penguins")
mc(A, "animais", 1, 6, "Qual animal é chamado de 'rei da selva', embora viva nas savanas?",
   ["Leão", "Tigre", "Elefante", "Girafa"], "Leão",
   "Os leões vivem em grupos chamados alcateias ou bandos.",
   "Smithsonian's National Zoo – Lion")
mc(A, "animais", 1, 7, "Qual destes é o maior mamífero terrestre?",
   ["Elefante-africano", "Rinoceronte", "Hipopótamo", "Girafa"], "Elefante-africano",
   "Um elefante-africano adulto pode pesar mais de 6 toneladas.",
   "WWF – African Elephant", syn=["elefante", "elefante africano"])
mc(A, "animais", 1, 8, "Qual animal australiano come folhas de eucalipto e dorme quase o dia inteiro?",
   ["Coala", "Canguru", "Ornitorrinco", "Emu"], "Coala",
   "O coala dorme até 20 horas por dia.",
   "Australian Museum – Koala")
mc(A, "animais", 1, 8, "Qual destes animais é um anfíbio?",
   ["Sapo", "Cobra", "Tartaruga", "Jacaré"], "Sapo",
   "Anfíbios vivem parte da vida na água e parte na terra.",
   "Instituto Butantan – Anfíbios")
mc(A, "ecologia", 1, 9, "Como se chama o animal que se alimenta só de plantas?",
   ["Herbívoro", "Carnívoro", "Onívoro", "Predador"], "Herbívoro",
   "Vacas, cavalos e capivaras são herbívoros.",
   "Museu de Zoologia da USP", syn=["herbivoro"])
mc(A, "florestas", 1, 9, "Qual é a maior floresta tropical do mundo?",
   ["Floresta Amazônica", "Mata Atlântica", "Floresta do Congo", "Floresta Negra"], "Floresta Amazônica",
   "A Amazônia se estende por nove países da América do Sul.",
   "WWF – Amazon", syn=["amazonia", "amazonica"], br=True)
mc(A, "animais", 2, 12, "Qual mamífero bota ovos e tem bico parecido com o de um pato?",
   ["Ornitorrinco", "Castor", "Lontra", "Tatu"], "Ornitorrinco",
   "O ornitorrinco vive na Austrália e é um dos poucos mamíferos que põem ovos.",
   "Australian Museum – Platypus")
mc(A, "atmosfera", 2, 12, "Qual camada da atmosfera protege a Terra dos raios ultravioleta do Sol?",
   ["Camada de ozônio", "Camada de nuvens", "Camada de poeira", "Camada de gelo"], "Camada de ozônio",
   "O Protocolo de Montreal, de 1987, ajudou a recuperar a camada de ozônio.",
   "UNEP – Ozone Secretariat", syn=["ozonio", "camada de ozonio"])
mc(A, "animais", 3, 14, "Qual é o maior réptil do mundo?",
   ["Crocodilo-de-água-salgada", "Dragão-de-komodo", "Sucuri", "Tartaruga-gigante"], "Crocodilo-de-água-salgada",
   "Os machos podem passar de 6 metros de comprimento.",
   "Australian Museum – Saltwater Crocodile", syn=["crocodilo", "crocodilo de agua salgada"])
mc(A, "plantas", 3, 14, "Qual árvore é a mais alta do mundo?",
   ["Sequoia-vermelha", "Baobá", "Jequitibá", "Eucalipto"], "Sequoia-vermelha",
   "A sequoia chamada Hyperion, na Califórnia, tem cerca de 116 metros.",
   "National Park Service – Redwood National and State Parks", syn=["sequoia"])

# =========================================================== CULTURA BRASILEIRA
B = "cul"
mc(B, "festas", 1, 6, "Qual festa brasileira, que acontece antes da Quaresma, tem blocos de rua, fantasias e confete?",
   ["Carnaval", "Natal", "Páscoa", "Dia das Crianças"], "Carnaval",
   "O Carnaval acontece em fevereiro ou março, conforme a data da Páscoa.",
   "IPHAN – Carnaval", br=True)
mc(B, "datas", 1, 7, "Em que dia se comemora a Independência do Brasil?",
   ["7 de setembro", "15 de novembro", "21 de abril", "25 de dezembro"], "7 de setembro",
   "15 de novembro é a Proclamação da República e 21 de abril é Tiradentes.",
   "Lei nº 662/1949 – Feriados nacionais", syn=["sete de setembro"], br=True)
mc(B, "doces", 1, 8, "Qual doce amarelinho e brilhante é feito com gema de ovo, açúcar e coco?",
   ["Quindim", "Brigadeiro", "Beijinho", "Pé de moleque"], "Quindim",
   "O quindim tem origem nos doces de ovos portugueses, com o coco brasileiro.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(B, "capoeira", 1, 8, "Qual instrumento de uma corda, com arco e cabaça, comanda a roda de capoeira?",
   ["Berimbau", "Violão", "Pandeiro", "Cuíca"], "Berimbau",
   "O ritmo do berimbau define o jeito do jogo na roda.",
   "IPHAN – Roda de Capoeira", br=True)
mc(B, "símbolos", 1, 9, "Qual hino começa com 'Ouviram do Ipiranga as margens plácidas'?",
   ["Hino Nacional Brasileiro", "Hino da Independência", "Hino à Bandeira", "Hino da Proclamação da República"], "Hino Nacional Brasileiro",
   "A letra é de Joaquim Osório Duque Estrada.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", syn=["hino nacional"], br=True)
mc(B, "cidades", 2, 10, "Qual cidade brasileira é conhecida como 'Terra da Garoa'?",
   ["São Paulo", "Curitiba", "Porto Alegre", "Belo Horizonte"], "São Paulo",
   "O apelido vem da chuva fininha que era comum na cidade.",
   "Prefeitura de São Paulo – História", syn=["sao paulo", "sampa"], br=True)
mc(B, "patrimônio", 2, 12, "Qual cidade histórica mineira, antiga capital do estado, é famosa por suas igrejas barrocas?",
   ["Ouro Preto", "Tiradentes", "Diamantina", "Mariana"], "Ouro Preto",
   "Ouro Preto foi a primeira cidade brasileira declarada Patrimônio Mundial pela UNESCO, em 1980.",
   "UNESCO – Historic Town of Ouro Preto", br=True)
mc(B, "festas", 2, 12, "Qual festa religiosa de Belém reúne milhões de pessoas em outubro?",
   ["Círio de Nazaré", "Festa do Divino", "Lavagem do Bonfim", "Romaria de Aparecida"], "Círio de Nazaré",
   "O Círio é patrimônio cultural imaterial da humanidade (UNESCO, 2013).",
   "UNESCO – Círio de Nazaré (2013)", syn=["cirio de nazare", "cirio"], br=True)
mc(B, "festas", 3, 14, "Em qual cidade acontece a maior Oktoberfest do Brasil?",
   ["Blumenau", "Gramado", "Joinville", "Pomerode"], "Blumenau",
   "A festa começou em 1984, em homenagem à colonização alemã.",
   "Prefeitura de Blumenau – Oktoberfest", br=True)
mc(B, "festas", 3, 14, "Qual cidade da Paraíba disputa com Caruaru o título de 'Maior São João do Mundo'?",
   ["Campina Grande", "João Pessoa", "Patos", "Sousa"], "Campina Grande",
   "As duas cidades recebem milhões de visitantes durante o mês de junho.",
   "Prefeitura de Campina Grande – O Maior São João do Mundo", br=True)
mc(B, "símbolos", 4, 16, "Quem compôs a melodia do hino que começa com 'Ouviram do Ipiranga as margens plácidas'?",
   ["Francisco Manuel da Silva", "Carlos Gomes", "Heitor Villa-Lobos", "Chiquinha Gonzaga"], "Francisco Manuel da Silva",
   "A melodia é de 1831; a letra oficial só foi adotada em 1922.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", br=True)

# =========================================================== CURIOSIDADES
Q = "cur"
mc(Q, "tempo", 1, 6, "Quantas horas tem um dia?",
   ["24", "12", "10", "60"], "24",
   "É o tempo que a Terra leva para girar uma vez em torno de si mesma.",
   "Bureau International des Poids et Mesures – Unidades de tempo")
mc(Q, "calendário", 1, 6, "Quantos meses tem um ano?",
   ["12", "10", "7", "30"], "12",
   "De janeiro a dezembro.",
   "Observatório Nacional – Calendário")
mc(Q, "calendário", 1, 8, "Quantos dias tem o mês de fevereiro num ano comum, que não é bissexto?",
   ["28", "30", "31", "29"], "28",
   "Fevereiro é o mês mais curto do ano.",
   "Observatório Nacional – Calendário")
mc(Q, "animais", 1, 8, "Qual mamífero é famoso por ser muito lento e viver pendurado nas árvores?",
   ["Bicho-preguiça", "Macaco", "Tamanduá", "Gambá"], "Bicho-preguiça",
   "A preguiça desce da árvore mais ou menos uma vez por semana.",
   "Smithsonian's National Zoo – Sloths", syn=["preguica", "bicho preguica"])
mc(Q, "animais", 1, 8, "Quantos braços tem a maioria das estrelas-do-mar?",
   ["5", "3", "8", "10"], "5",
   "Algumas espécies têm muito mais braços, e elas conseguem regenerar os que perdem.",
   "NOAA – Sea Stars")
mc(Q, "línguas", 1, 8, "Qual é o idioma oficial do Japão?",
   ["Japonês", "Chinês", "Coreano", "Inglês"], "Japonês",
   "O japonês usa três tipos de escrita: hiragana, katakana e kanji.",
   "Enciclopédia Britannica – verbete 'Japanese language'", syn=["japones"])
mc(Q, "monumentos", 1, 10, "Qual é o nome do famoso sino do relógio do Parlamento de Londres?",
   ["Big Ben", "Tower Bridge", "London Eye", "Abbey Road"], "Big Ben",
   "Big Ben é o apelido do grande sino; a torre se chama Elizabeth Tower.",
   "UK Parliament – Big Ben")
mc(Q, "continentes", 2, 12, "Qual é o único continente onde não existe nenhum país?",
   ["Antártida", "Oceania", "Ártico", "Groenlândia"], "Antártida",
   "A Antártida é regida pelo Tratado da Antártida, de 1959.",
   "Secretaria do Tratado da Antártida", syn=["antartica", "antartida"])
mc(Q, "palavras", 2, 12, "Como se chama o medo exagerado de aranhas?",
   ["Aracnofobia", "Claustrofobia", "Acrofobia", "Hidrofobia"], "Aracnofobia",
   "Claustrofobia é o medo de lugares fechados; acrofobia, de altura.",
   "Dicionário Houaiss – verbete 'aracnofobia'")
mc(Q, "tradições", 2, 12, "Quantos anos de casamento se comemoram nas bodas de ouro?",
   ["50", "25", "10", "75"], "50",
   "Bodas de prata são 25 anos; de diamante, 60.",
   "Dicionário Houaiss – verbete 'bodas'")
