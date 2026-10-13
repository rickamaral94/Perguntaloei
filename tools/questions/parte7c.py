# Perguntas novas (parte 7c). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== CINEMA
C = "cin"
mc(C, "super-heróis", 1, 6, "Qual super-herói da Marvel usa um escudo redondo com uma estrela no meio?",
   ["Capitão América", "Thor", "Homem de Ferro", "Pantera Negra"], "Capitão América",
   "O escudo do Capitão América tem as cores vermelha, branca e azul.",
   "Marvel Studios – Capitão América: O Primeiro Vingador (2011)")
mc(C, "clássicos", 1, 8, "Em 'E.T. – O Extraterrestre', em que o menino Elliott voa pelo céu levando o E.T.?",
   ["Bicicleta", "Skate", "Carro", "Patinete"], "Bicicleta",
   "A cena da bicicleta passando na frente da lua virou o símbolo do filme.",
   "IMDb – E.T. – O Extraterrestre (1982)")
mc(C, "clássicos", 1, 8, "Qual babá mágica do cinema voa segurando um guarda-chuva?",
   ["Mary Poppins", "Matilda", "Dorothy", "Alice"], "Mary Poppins",
   "Julie Andrews ganhou o Oscar de Melhor Atriz pelo papel de Mary Poppins.",
   "Disney – Mary Poppins (1964)")
mc(C, "aventura", 1, 10, "Qual arqueólogo aventureiro do cinema usa chapéu e chicote?",
   ["Indiana Jones", "James Bond", "Jack Sparrow", "Rocky Balboa"], "Indiana Jones",
   "Harrison Ford interpretou Indiana Jones a partir de 'Os Caçadores da Arca Perdida' (1981).",
   "Lucasfilm – Os Caçadores da Arca Perdida (1981)")
mc(C, "comédia", 1, 10, "Em 'Esqueceram de Mim', o menino Kevin fica sozinho em casa às vésperas de qual festa?",
   ["Natal", "Páscoa", "Carnaval", "Halloween"], "Natal",
   "A família de Kevin viaja para Paris no Natal e o esquece em casa.",
   "IMDb – Esqueceram de Mim (1990)")
tf(C, "ação", 1, 10, "O agente secreto James Bond é conhecido pelo código 007.", True,
   "O código 007 indica que Bond tem permissão para matar em serviço.", "IMDb – 007 contra o Satânico Dr. No (1962)")
tf(C, "ação", 1, 12, "Arnold Schwarzenegger interpretou o robô de 'O Exterminador do Futuro'.", True,
   "Ele viveu o Exterminador no filme de 1984, dirigido por James Cameron.",
   "IMDb – O Exterminador do Futuro (1984)")
mc(C, "atores", 2, 12, "Qual personagem boxeador foi criado e interpretado por Sylvester Stallone?",
   ["Rocky Balboa", "Rambo", "Indiana Jones", "John McClane"], "Rocky Balboa",
   "'Rocky – Um Lutador' ganhou o Oscar de Melhor Filme.", "IMDb – Rocky – Um Lutador (1976)")
mc(C, "atores", 2, 12, "Qual ator interpretou Wolverine nos filmes dos X-Men?",
   ["Hugh Jackman", "Chris Hemsworth", "Ryan Reynolds", "Chris Evans"], "Hugh Jackman",
   "Hugh Jackman viveu Wolverine pela primeira vez em 'X-Men – O Filme' (2000).",
   "IMDb – X-Men – O Filme (2000)")
op(C, "super-heróis", 2, 12, "Qual é o nome do país africano fictício governado pelo Pantera Negra?", "Wakanda",
   ["wakanda", "uacanda"],
   "Wakanda é uma nação escondida e muito avançada graças ao metal vibranium.",
   "Marvel Studios – Pantera Negra (2018)")
mc(C, "cinema brasileiro", 2, 12, "Qual ator criou e interpretou Dona Hermínia em 'Minha Mãe é uma Peça'?",
   ["Paulo Gustavo", "Marcelo Adnet", "Leandro Hassum", "Fábio Porchat"], "Paulo Gustavo",
   "Paulo Gustavo se inspirou na própria mãe para criar a personagem.",
   "IMDb – Minha Mãe é uma Peça (2013)", br=True)
tf(C, "Oscar", 2, 14, "Keanu Reeves interpretou o Coringa em 'Batman – O Cavaleiro das Trevas'.", False,
   "O Coringa do filme de 2008 foi Heath Ledger, que ganhou o Oscar de Ator Coadjuvante.",
   "IMDb – Batman – O Cavaleiro das Trevas (2008)")
op(C, "terror", 2, 14, "Qual é o nome do boneco assassino da série de filmes 'Brinquedo Assassino'?", "Chucky",
   ["chucky", "chuck", "boneco chucky"],
   "Chucky é um boneco possuído pelo espírito de um criminoso.", "IMDb – Brinquedo Assassino (1988)")
mc(C, "suspense", 3, 16, "Qual personagem Anthony Hopkins interpretou em 'O Silêncio dos Inocentes'?",
   ["Hannibal Lecter", "Norman Bates", "Freddy Krueger", "Jack Torrance"], "Hannibal Lecter",
   "O papel deu a Anthony Hopkins o Oscar de Melhor Ator.", "IMDb – O Silêncio dos Inocentes (1991)")
mc(C, "cinema brasileiro", 3, 16, "Qual filme de Hector Babenco, de 2003, se passa num grande presídio de São Paulo?",
   ["Carandiru", "Cidade de Deus", "Central do Brasil", "Bicho de Sete Cabeças"], "Carandiru",
   "O filme foi baseado no livro 'Estação Carandiru', do médico Drauzio Varella.",
   "IMDb – Carandiru (2003)", br=True)
mc(C, "cinema brasileiro", 3, 14, "Qual ator ficou famoso por interpretar caipiras no cinema, como no filme 'Jeca Tatu', de 1959?",
   ["Mazzaropi", "Oscarito", "Grande Otelo", "Renato Aragão"], "Mazzaropi",
   "Amácio Mazzaropi também produzia os próprios filmes, que lotavam os cinemas do interior.",
   "Cinemateca Brasileira", br=True)
mc(C, "clássicos", 3, 14, "O clássico de 1942 com Humphrey Bogart e Ingrid Bergman tem o nome de qual cidade do Marrocos?",
   ["Casablanca", "Marrakech", "Tânger", "Rabat"], "Casablanca",
   "'Casablanca' ganhou o Oscar de Melhor Filme.", "IMDb – Casablanca (1942)")
mc(C, "musicais", 4, 16, "Qual ator dança e canta com um guarda-chuva na cena mais famosa de 'Cantando na Chuva'?",
   ["Gene Kelly", "Fred Astaire", "Frank Sinatra", "Elvis Presley"], "Gene Kelly",
   "Gene Kelly também foi um dos diretores do filme.", "IMDb – Cantando na Chuva (1952)")

# =========================================================== FILMES INFANTIS
I = "inf"
mc(I, "Disney", 1, 6, "Que animal é o Bambi?",
   ["Cervo", "Coelho", "Raposa", "Cavalo"], "Cervo",
   "Bambi é um filhote de cervo, e seu amigo Tambor é um coelho.", "Disney – Bambi (1942)")
mc(I, "Disney", 1, 6, "Qual fadinha acompanha o Peter Pan nas aventuras?",
   ["Sininho", "Fada Madrinha", "Ariel", "Aurora"], "Sininho",
   "Sininho espalha um pozinho mágico que faz as pessoas voarem.", "Disney – Peter Pan (1953)")
tf(I, "Pixar", 1, 6, "Em 'Toy Story', os brinquedos ganham vida quando os humanos não estão olhando.", True,
   "Quando alguém chega perto, os brinquedos ficam paradinhos de novo.", "Disney/Pixar – Toy Story (1995)")
op(I, "desenhos", 1, 6, "Qual é o nome do cachorro de estimação do Mickey?", "Pluto",
   ["pluto", "o pluto"],
   "Pluto é o cachorro de estimação do Mickey e não fala, ao contrário do Pateta.", "Disney")
mc(I, "Disney", 1, 7, "Qual vilã quer fazer um casaco com a pele dos filhotes de dálmata?",
   ["Cruella", "Úrsula", "Malévola", "Rainha Má"], "Cruella",
   "Cruella de Vil é a vilã de '101 Dálmatas'.", "Disney – 101 Dálmatas (1961)")
mc(I, "Disney", 1, 7, "Em 'Pinóquio', que bichinho faz o papel de consciência do boneco?",
   ["Grilo", "Abelha", "Formiga", "Joaninha"], "Grilo",
   "O Grilo Falante aconselha Pinóquio a sempre falar a verdade.", "Disney – Pinóquio (1940)")
mc(I, "DreamWorks", 1, 7, "Em 'Shrek', qual princesa se casa com o ogro?",
   ["Fiona", "Aurora", "Bela", "Jasmine"], "Fiona",
   "Fiona vira ogra ao pôr do sol por causa de um feitiço.", "DreamWorks – Shrek (2001)")
op(I, "animação", 1, 7, "Em 'Meu Malvado Favorito', qual é o nome do vilão que adota três meninas?", "Gru",
   ["gru", "o gru"],
   "Gru adota Margo, Edith e Agnes e acaba deixando a vilania.", "Illumination – Meu Malvado Favorito (2010)")
mc(I, "Pixar", 1, 8, "Em qual cidade se passa o filme 'Ratatouille'?",
   ["Paris", "Roma", "Londres", "Nova York"], "Paris",
   "O ratinho Remy sonha em ser chef num famoso restaurante de Paris.", "Disney/Pixar – Ratatouille (2007)")
mc(I, "Disney", 2, 8, "Em 'O Rei Leão', qual é o nome do pai de Simba?",
   ["Mufasa", "Scar", "Rafiki", "Zazu"], "Mufasa",
   "Mufasa é o rei das Terras do Reino no começo do filme.", "Disney – O Rei Leão (1994)")
mc(I, "Disney", 2, 8, "Em 'Mogli – O Menino Lobo', qual urso é o grande amigo de Mogli?",
   ["Balu", "Bagheera", "Shere Khan", "Kaa"], "Balu",
   "Bagheera é a pantera, Shere Khan é o tigre e Kaa é a cobra.", "Disney – Mogli – O Menino Lobo (1967)")
mc(I, "Pixar", 2, 8, "Em 'Monstros S.A.', como se chama a menininha que entra no mundo dos monstros?",
   ["Boo", "Dory", "Agnes", "Lilo"], "Boo",
   "Boo chama o monstro Sulley de 'gatinho'.", "Disney/Pixar – Monstros S.A. (2001)")
tf(I, "Disney", 2, 8, "Em 'Zootopia', o malandro Nick Wilde é um lobo.", False,
   "Nick Wilde é uma raposa e vira parceiro da coelha Judy Hopps.", "Disney – Zootopia (2016)")
mc(I, "Disney", 2, 10, "Em 'Frozen', qual é o título em português da canção que Elsa canta ao construir seu castelo de gelo?",
   ["Livre Estou", "Saber Quem Sou", "Hakuna Matata", "Aqui no Mar"], "Livre Estou",
   "No original em inglês, a canção se chama 'Let It Go' e ganhou o Oscar de Melhor Canção.",
   "Disney – Frozen: Uma Aventura Congelante (2013)")
mc(I, "Pixar", 2, 10, "Em 'Divertida Mente 2', qual nova emoção laranja chega à cabeça de Riley?",
   ["Ansiedade", "Raiva", "Nojinho", "Medo"], "Ansiedade",
   "Raiva, Nojinho e Medo já estavam no primeiro filme; Ansiedade chega com a adolescência.",
   "Disney/Pixar – Divertida Mente 2 (2024)")
mc(I, "Pixar", 3, 10, "Em 'Procurando Nemo', em qual cidade fica o consultório do dentista que leva Nemo?",
   ["Sydney", "Melbourne", "Honolulu", "Auckland"], "Sydney",
   "Marlin e Dory atravessam o oceano até o endereço P. Sherman, 42, Wallaby Way, Sydney.",
   "Disney/Pixar – Procurando Nemo (2003)")
tf(I, "Oscar", 3, 12, "'A Bela e a Fera', de 1991, foi a primeira animação indicada ao Oscar de Melhor Filme.", True,
   "Ele foi indicado na cerimônia de 1992, quando ainda não existia a categoria de Melhor Animação.",
   "Academia de Artes e Ciências Cinematográficas")
mc(I, "Disney", 4, 14, "Em qual filme da Disney, de 1942, o papagaio Zé Carioca apareceu pela primeira vez?",
   ["Alô, Amigos", "Você Já Foi à Bahia?", "Fantasia", "Dumbo"], "Alô, Amigos",
   "Em 'Alô, Amigos', Zé Carioca mostra o Rio de Janeiro ao Pato Donald; ele voltou em 'Você Já Foi à Bahia?' (1944).",
   "Disney – Alô, Amigos (1942)", br=True)

# =========================================================== MÚSICA
M = "mus"
mc(M, "personagens", 1, 6, "Qual personagem azul de bolinhas brancas canta músicas infantis em vídeos famosos?",
   ["Galinha Pintadinha", "Peppa Pig", "Patati Patatá", "Mundo Bita"], "Galinha Pintadinha",
   "A Galinha Pintadinha surgiu na internet em 2006 cantando cantigas populares.",
   "Galinha Pintadinha – site oficial", br=True)
mc(M, "instrumentos", 1, 7, "Que tipo de instrumento é o tambor?",
   ["De percussão", "De cordas", "De sopro", "De teclas"], "De percussão",
   "Instrumentos de percussão fazem som quando são batidos, sacudidos ou raspados.",
   "Dicionário Grove de Música")
op(M, "instrumentos", 1, 7, "Qual instrumento de metal, com três lados, é tocado com uma varinha no forró?", "Triângulo",
   ["triângulo", "triangulo", "o triângulo"],
   "Sanfona, zabumba e triângulo formam o trio tradicional do forró pé de serra.",
   "Museu Cais do Sertão", br=True)
tf(M, "instrumentos", 1, 9, "O cavaquinho tem mais cordas que o violão.", False,
   "O cavaquinho tem quatro cordas, e o violão comum tem seis.", "Dicionário Grove de Música")
op(M, "conceitos", 1, 9, "Como se chama o grande conjunto de músicos com cordas, sopros e percussão, regido por um maestro?", "Orquestra",
   ["orquestra", "orquestra sinfônica", "orquestra sinfonica", "sinfônica", "sinfonica", "filarmônica", "filarmonica", "orquestra filarmônica"],
   "Numa orquestra sinfônica, os violinos costumam ser o grupo mais numeroso.", "Dicionário Grove de Música")
mc(M, "pop", 1, 10, "Qual cantora americana gravou 'Shake It Off' e 'Love Story'?",
   ["Taylor Swift", "Beyoncé", "Lady Gaga", "Katy Perry"], "Taylor Swift",
   "Taylor Swift começou a carreira na música country antes de migrar para o pop.", "Billboard")
mc(M, "rock", 2, 12, "Qual banda inglesa, liderada por Mick Jagger, gravou '(I Can't Get No) Satisfaction'?",
   ["The Rolling Stones", "The Beatles", "Queen", "Pink Floyd"], "The Rolling Stones",
   "A banda foi formada em Londres em 1962.", "Rock and Roll Hall of Fame")
mc(M, "gêneros", 2, 12, "Qual gênero musical nasceu em Nova Orleans e tem Louis Armstrong como um de seus maiores nomes?",
   ["Jazz", "Reggae", "Tango", "Samba"], "Jazz",
   "O jazz surgiu no começo do século XX entre músicos negros do sul dos Estados Unidos.",
   "Smithsonian – National Museum of American History")
tf(M, "gêneros", 2, 12, "O axé music surgiu na Bahia.", True,
   "O axé se popularizou em Salvador nos anos 1980, embalando o Carnaval dos trios elétricos.",
   "Enciclopédia da Música Brasileira", br=True)
mc(M, "MPB", 2, 14, "Qual gênero musical instrumental brasileiro tem Pixinguinha como um de seus maiores mestres?",
   ["Choro", "Axé", "Sertanejo", "Funk"], "Choro",
   "Pixinguinha compôs clássicos do choro como 'Carinhoso'.", "Instituto Moreira Salles", br=True)
mc(M, "MPB", 2, 14, "Quem compôs 'País Tropical', que diz 'Moro num país tropical, abençoado por Deus'?",
   ["Jorge Ben Jor", "Tim Maia", "Djavan", "Gilberto Gil"], "Jorge Ben Jor",
   "A música foi lançada em 1969 e ficou famosa também na voz de Wilson Simonal.",
   "Dicionário Cravo Albin da MPB", br=True)
mc(M, "MPB", 2, 14, "Qual cantor baiano gravou 'Aquele Abraço' e 'Andar com Fé'?",
   ["Gilberto Gil", "Caetano Veloso", "Djavan", "Milton Nascimento"], "Gilberto Gil",
   "Gilberto Gil também foi ministro da Cultura entre 2003 e 2008.",
   "Dicionário Cravo Albin da MPB", br=True)
mc(M, "rock", 2, 14, "Qual banda irlandesa tem Bono como vocalista?",
   ["U2", "Coldplay", "Oasis", "Radiohead"], "U2",
   "O U2 foi formado em Dublin em 1976.", "Rock and Roll Hall of Fame")
mc(M, "clássica", 3, 14, "Qual compositor russo escreveu o balé 'O Quebra-Nozes'?",
   ["Piotr Tchaikovsky", "Igor Stravinsky", "Sergei Rachmaninoff", "Modest Mussorgsky"], "Piotr Tchaikovsky",
   "O balé estreou em São Petersburgo em 1892 e virou tradição de Natal.", "Encyclopaedia Britannica")
mc(M, "clássica", 3, 16, "Qual compositor alemão do período barroco escreveu a 'Paixão segundo São Mateus'?",
   ["Johann Sebastian Bach", "Ludwig van Beethoven", "Johannes Brahms", "Richard Wagner"], "Johann Sebastian Bach",
   "Bach viveu de 1685 a 1750 e é um dos maiores nomes da música barroca.", "Encyclopaedia Britannica")
mc(M, "samba", 3, 16, "Qual sambista da Mangueira compôs 'As Rosas Não Falam'?",
   ["Cartola", "Noel Rosa", "Adoniran Barbosa", "Paulinho da Viola"], "Cartola",
   "Cartola foi um dos fundadores da escola de samba Estação Primeira de Mangueira.",
   "Dicionário Cravo Albin da MPB", br=True)
mc(M, "samba", 3, 16, "Qual compositor paulista criou os sambas 'Trem das Onze' e 'Saudosa Maloca'?",
   ["Adoniran Barbosa", "Cartola", "Noel Rosa", "Paulo Vanzolini"], "Adoniran Barbosa",
   "Os dois sambas ficaram famosos na gravação do grupo Demônios da Garoa.",
   "Dicionário Cravo Albin da MPB", br=True)
mc(M, "samba", 4, 16, "Qual sambista de Vila Isabel compôs 'Com Que Roupa?' e morreu em 1937, aos 26 anos?",
   ["Noel Rosa", "Cartola", "Pixinguinha", "Ary Barroso"], "Noel Rosa",
   "Mesmo vivendo pouco, Noel Rosa deixou centenas de canções.",
   "Dicionário Cravo Albin da MPB", br=True)

# =========================================================== ESPORTES
E = "esp"
mc(E, "esportes aquáticos", 1, 6, "Em qual esporte o atleta desliza nas ondas em pé sobre uma prancha?",
   ["Surfe", "Remo", "Natação", "Polo aquático"], "Surfe",
   "O surfe estreou nos Jogos Olímpicos em Tóquio 2020.", "Comitê Olímpico Internacional")
mc(E, "outros esportes", 1, 8, "Em qual esporte os jogadores usam patins e tacos para levar um disco até o gol, sobre o gelo?",
   ["Hóquei", "Golfe", "Beisebol", "Críquete"], "Hóquei",
   "O disco do hóquei no gelo se chama puck.", "Federação Internacional de Hóquei no Gelo")
mc(E, "outros esportes", 1, 8, "Em qual esporte se faz um 'strike' ao derrubar todos os pinos de uma vez?",
   ["Boliche", "Bocha", "Beisebol", "Golfe"], "Boliche",
   "No boliche, a bola é lançada numa pista para derrubar dez pinos.", "World Bowling")
tf(E, "natação", 1, 8, "O nado borboleta é um dos estilos oficiais da natação.", True,
   "Os quatro estilos oficiais são crawl (livre), costas, peito e borboleta.", "World Aquatics")
mc(E, "outros esportes", 1, 10, "Qual jogo usa tacos, bolas coloridas e uma mesa com seis caçapas?",
   ["Sinuca", "Boliche", "Golfe", "Tênis de mesa"], "Sinuca",
   "Na sinuca, o jogador usa a bola branca para encaçapar as outras.", "World Snooker")
mc(E, "olimpíadas", 1, 10, "Em qual esporte olímpico o cavaleiro e o cavalo saltam obstáculos?",
   ["Hipismo", "Esgrima", "Remo", "Atletismo"], "Hipismo",
   "Nas provas de salto, a dupla perde pontos ao derrubar obstáculos.",
   "Comitê Olímpico Internacional")
mc(E, "outros esportes", 2, 10, "Qual esporte olímpico é jogado com raquetes leves e uma peteca?",
   ["Badminton", "Tênis", "Squash", "Tênis de mesa"], "Badminton",
   "A peteca do badminton é feita de penas ou de material sintético.", "Badminton World Federation")
tf(E, "basquete", 2, 10, "No basquete oficial, a cesta fica a pouco mais de 3 metros do chão.", True,
   "O aro fica a 3,05 metros de altura.", "FIBA – Regras Oficiais do Basquete")
tf(E, "basquete", 2, 12, "Uma partida da NBA é dividida em dois tempos de 24 minutos.", False,
   "O jogo da NBA tem quatro quartos de 12 minutos cada.", "NBA – Official Rules")
op(E, "vôlei", 2, 12, "No vôlei, como se chama o jogador de camisa de cor diferente que só atua na defesa?", "Líbero",
   ["líbero", "libero", "o líbero"],
   "O líbero não pode sacar, bloquear nem atacar acima da altura da rede.", "FIVB – Regras Oficiais do Voleibol")
op(E, "olimpíadas", 2, 12, "Qual esporte olímpico junta natação, ciclismo e corrida numa só prova?", "Triatlo",
   ["triatlo", "triatlon", "triathlon", "triátlon"],
   "Na prova olímpica, os atletas nadam 1,5 km, pedalam 40 km e correm 10 km.", "World Triathlon")
mc(E, "olimpíadas", 2, 12, "Qual surfista brasileiro ganhou a primeira medalha de ouro olímpica do surfe, em Tóquio 2020?",
   ["Ítalo Ferreira", "Gabriel Medina", "Filipe Toledo", "Adriano de Souza"], "Ítalo Ferreira",
   "Ítalo Ferreira, do Rio Grande do Norte, venceu a final no Japão em 2021.",
   "Comitê Olímpico do Brasil", br=True)
mc(E, "natação", 2, 14, "Qual nadador brasileiro foi campeão olímpico dos 50 metros livre em Pequim 2008?",
   ["César Cielo", "Gustavo Borges", "Thiago Pereira", "Bruno Fratus"], "César Cielo",
   "Foi a primeira medalha de ouro olímpica da natação brasileira.", "Comitê Olímpico do Brasil", br=True)
mc(E, "automobilismo", 2, 14, "Qual piloto brasileiro foi campeão mundial de Fórmula 1 em 1981, 1983 e 1987?",
   ["Nelson Piquet", "Ayrton Senna", "Emerson Fittipaldi", "Rubens Barrichello"], "Nelson Piquet",
   "Piquet foi o primeiro brasileiro tricampeão da Fórmula 1.", "FIA – Fórmula 1", br=True)
mc(E, "olimpíadas", 3, 14, "Qual judoca foi a primeira brasileira a ganhar ouro olímpico no judô, em Londres 2012?",
   ["Sarah Menezes", "Rafaela Silva", "Mayra Aguiar", "Ketleyn Quadros"], "Sarah Menezes",
   "A piauiense Sarah Menezes venceu na categoria até 48 kg.", "Comitê Olímpico do Brasil", br=True)
mc(E, "olimpíadas", 3, 14, "Em qual esporte o Brasil ganhou suas primeiras medalhas de ouro olímpicas femininas, em Atlanta 1996?",
   ["Vôlei de praia", "Futebol", "Judô", "Natação"], "Vôlei de praia",
   "Jacqueline e Sandra venceram a final contra a dupla brasileira Adriana e Mônica.",
   "Comitê Olímpico do Brasil", br=True)
tf(E, "basquete", 3, 14, "A seleção brasileira masculina de basquete já foi campeã mundial.", True,
   "O Brasil venceu os Mundiais de 1959, no Chile, e de 1963, no Rio de Janeiro.", "FIBA", br=True)
mc(E, "olimpíadas", 4, 16, "Qual velejador brasileiro ganhou o ouro olímpico na classe Laser em 1996 e 2004?",
   ["Robert Scheidt", "Lars Grael", "Bruno Prada", "Torben Grael"], "Robert Scheidt",
   "Scheidt ganhou cinco medalhas olímpicas, duas delas de ouro.", "Comitê Olímpico do Brasil", br=True)

# =========================================================== MARCAS
K = "mar"
mc(K, "produtos", 1, 6, "A Colgate é famosa por fabricar qual produto?",
   ["Creme dental", "Sorvete", "Tênis", "Brinquedos"], "Creme dental",
   "A Colgate foi fundada em Nova York em 1806.", "Colgate-Palmolive – site oficial")
mc(K, "mascotes", 1, 8, "Qual cereal matinal tem como mascote o tigre Tony?",
   ["Sucrilhos", "Froot Loops", "Nescau Cereal", "Snow Flakes"], "Sucrilhos",
   "Sucrilhos é fabricado pela Kellogg's, e o Tony é seu mascote há décadas.", "Kellogg's – site oficial", br=True)
mc(K, "produtos", 1, 10, "Qual rede de lanchonetes vende o sanduíche Whopper?",
   ["Burger King", "McDonald's", "Subway", "Bob's"], "Burger King",
   "O Whopper foi criado pelo Burger King em 1957.", "Burger King – site oficial")
mc(K, "origens", 1, 10, "A Samsung é uma empresa de qual país?",
   ["Coreia do Sul", "Japão", "China", "Estados Unidos"], "Coreia do Sul",
   "A Samsung foi fundada em 1938, na Coreia.", "Samsung – site oficial")
mc(K, "brinquedos", 2, 10, "Qual empresa americana fabrica a boneca Barbie?",
   ["Mattel", "Hasbro", "Estrela", "LEGO"], "Mattel",
   "A Barbie foi lançada pela Mattel em 1959.", "Mattel – site oficial")
mc(K, "logotipos", 2, 10, "Qual marca italiana de carros esportivos tem um touro no logotipo?",
   ["Lamborghini", "Ferrari", "Maserati", "Alfa Romeo"], "Lamborghini",
   "O fundador, Ferruccio Lamborghini, era do signo de Touro.", "Lamborghini – site oficial")
mc(K, "logotipos", 2, 12, "Qual montadora francesa tem um leão no logotipo?",
   ["Peugeot", "Renault", "Citroën", "Fiat"], "Peugeot",
   "O leão representa a marca Peugeot desde o século XIX.", "Peugeot – site oficial")
mc(K, "origens", 2, 12, "Em qual país foi fundada a IKEA, loja famosa por móveis para montar em casa?",
   ["Suécia", "Noruega", "Dinamarca", "Finlândia"], "Suécia",
   "A IKEA foi fundada por Ingvar Kamprad em 1943.", "IKEA – site oficial")
tf(K, "origens", 2, 12, "O nome da marca Nike vem da deusa grega da vitória.", True,
   "Na mitologia grega, Nike é a deusa que personifica a vitória.", "Nike – site oficial")
mc(K, "slogans", 2, 12, "Qual rede de lanchonetes usa no Brasil o slogan 'Amo muito tudo isso'?",
   ["McDonald's", "Burger King", "Subway", "Habib's"], "McDonald's",
   "É a versão brasileira do slogan mundial 'I'm lovin' it', lançado em 2003.", "McDonald's – site oficial", br=True)
mc(K, "logotipos", 2, 12, "Qual marca de sorvetes tem um coração no logotipo?",
   ["Kibon", "Nestlé", "Garoto", "Danone"], "Kibon",
   "O coração é o símbolo dos sorvetes da Unilever, dona da Kibon.", "Kibon – site oficial", br=True)
mc(K, "slogans", 2, 14, "Qual cartão usa o slogan 'Existem coisas que o dinheiro não compra'?",
   ["Mastercard", "Visa", "American Express", "Elo"], "Mastercard",
   "A frase completa termina com 'para todas as outras, existe Mastercard'.", "Mastercard – site oficial")
mc(K, "slogans", 2, 14, "Qual marca de cosméticos usa o slogan 'Porque você vale muito'?",
   ["L'Oréal", "Natura", "O Boticário", "Avon"], "L'Oréal",
   "É a versão brasileira do slogan 'Because you're worth it'.", "L'Oréal – site oficial")
mc(K, "slogans", 3, 14, "Qual rede de lojas usa o slogan 'Dedicação total a você'?",
   ["Casas Bahia", "Magazine Luiza", "Ponto Frio", "Lojas Americanas"], "Casas Bahia",
   "A Casas Bahia foi fundada por Samuel Klein em São Caetano do Sul, São Paulo.",
   "Casas Bahia – site oficial", br=True)
tf(K, "origens", 3, 14, "As sandálias Havaianas foram inspiradas nas zori, sandálias japonesas.", True,
   "Por isso a sola das Havaianas tem uma textura que lembra grãos de arroz.", "Havaianas – site oficial", br=True)
mc(K, "origens", 4, 16, "Qual empresa lançou as sandálias Havaianas, em 1962?",
   ["Alpargatas", "Grendene", "Azaleia", "Vulcabras"], "Alpargatas",
   "As Havaianas foram criadas pela São Paulo Alpargatas.", "Alpargatas – site oficial", br=True)
mc(K, "slogans", 4, 16, "Qual remédio para dor ficou famoso com o slogan 'é melhor e não faz mal'?",
   ["Melhoral", "Aspirina", "Doril", "Engov"], "Melhoral",
   "O jingle 'Melhoral, Melhoral, é melhor e não faz mal' marcou o rádio e a TV no Brasil.",
   "Propagandas Históricas", br=True)

# =========================================================== CULINÁRIA
G = "gas"
mc(G, "frutas", 1, 6, "Qual fruta tem casca cheia de escamas e uma coroa de folhas no topo?",
   ["Abacaxi", "Banana", "Manga", "Limão"], "Abacaxi",
   "O abacaxi é uma fruta nativa da América do Sul.", "Embrapa")
mc(G, "frutas", 1, 6, "Qual fruta tem casca marrom e peluda e polpa verde com sementinhas pretas?",
   ["Kiwi", "Maçã", "Laranja", "Banana"], "Kiwi",
   "O kiwi ficou famoso no mundo graças aos produtores da Nova Zelândia.", "Embrapa")
tf(G, "alimentos", 1, 6, "A batata cresce debaixo da terra.", True,
   "A batata é um tubérculo, uma parte da planta que cresce sob o solo.", "Embrapa")
op(G, "frutas", 1, 6, "Qual fruta vermelha a bruxa usa para enfeitiçar a Branca de Neve?", "Maçã",
   ["maçã", "maca", "maçã vermelha", "uma maçã"],
   "A Branca de Neve dá uma mordida na maçã envenenada e cai num sono profundo.",
   "Disney – Branca de Neve e os Sete Anões (1937)")
mc(G, "doces", 1, 8, "Além do chocolate em pó, qual ingrediente é a base da massa do brigadeiro?",
   ["Leite condensado", "Farinha de trigo", "Fermento", "Maionese"], "Leite condensado",
   "O brigadeiro é feito com leite condensado, chocolate e manteiga, mexidos no fogo.",
   "Museu da Gastronomia Brasileira", br=True)
mc(G, "frutas", 1, 8, "Qual fruta roxa e redondinha cresce grudada no tronco da árvore?",
   ["Jabuticaba", "Uva", "Ameixa", "Amora"], "Jabuticaba",
   "A jabuticabeira é uma árvore nativa do Brasil.", "Embrapa", br=True)
mc(G, "ingredientes", 2, 10, "Qual especiaria é feita da casca de uma árvore e vai no arroz-doce?",
   ["Canela", "Cravo", "Noz-moscada", "Pimenta-do-reino"], "Canela",
   "A canela é a casca seca da caneleira; o cravo é um botão de flor.", "Embrapa")
mc(G, "ingredientes", 2, 10, "Qual alimento é feito batendo o creme do leite até virar uma pasta amarelada?",
   ["Manteiga", "Requeijão", "Iogurte", "Maionese"], "Manteiga",
   "Ao bater o creme, a gordura se separa do soro e forma a manteiga.", "Embrapa Gado de Leite")
mc(G, "pratos brasileiros", 2, 12, "Qual prato nordestino mistura arroz, feijão-de-corda e queijo coalho?",
   ["Baião de dois", "Arroz carreteiro", "Feijão tropeiro", "Risoto"], "Baião de dois",
   "O baião de dois é especialmente tradicional no Ceará.", "Museu da Gastronomia Brasileira", br=True)
mc(G, "pratos brasileiros", 2, 12, "Qual prato baiano é um creme feito de pão, camarão seco, amendoim e azeite de dendê?",
   ["Vatapá", "Moqueca", "Feijoada", "Galinhada"], "Vatapá",
   "O vatapá também acompanha o acarajé.", "Museu da Gastronomia Baiana", br=True)
op(G, "pratos brasileiros", 2, 12, "Qual legume verde e de baba acompanha o frango num prato típico de Minas Gerais?", "Quiabo",
   ["quiabo", "o quiabo"],
   "O frango com quiabo costuma ser servido com angu.", "Museu da Gastronomia Brasileira", br=True)
tf(G, "pratos brasileiros", 2, 12, "O cuscuz nordestino é feito principalmente com farinha de trigo.", False,
   "O cuscuz nordestino é feito com flocos de milho cozidos no vapor.", "Embrapa", br=True)
mc(G, "pratos do mundo", 2, 12, "De qual país vem o estrogonofe, prato de carne com molho cremoso?",
   ["Rússia", "França", "Alemanha", "Itália"], "Rússia",
   "O nome vem da família Stroganov, da nobreza russa.", "Encyclopaedia Britannica")
mc(G, "pratos do mundo", 2, 14, "De qual país vem o kimchi, conserva picante de vegetais fermentados?",
   ["Coreia", "Japão", "China", "Tailândia"], "Coreia",
   "O preparo do kimchi é reconhecido pela UNESCO como patrimônio cultural da Coreia.", "UNESCO")
mc(G, "ingredientes", 3, 12, "Qual fruta amazônica, parente do cacau, é muito usada em sucos e cremes?",
   ["Cupuaçu", "Pequi", "Caju", "Pitanga"], "Cupuaçu",
   "Cupuaçu e cacau pertencem ao mesmo gênero de plantas, Theobroma.", "Embrapa Amazônia Oriental", br=True)
mc(G, "ingredientes", 3, 14, "Qual fruto do Cerrado, de cheiro forte e com espinhos no caroço, é marca da culinária goiana?",
   ["Pequi", "Cupuaçu", "Caju", "Pitanga"], "Pequi",
   "Não se deve morder o caroço do pequi, por causa dos espinhos.", "Embrapa Cerrados", br=True)
mc(G, "doces", 3, 14, "Qual doce pernambucano é um bolo de camadas finas enroladas com goiabada?",
   ["Bolo de rolo", "Bolo Souza Leão", "Cocada", "Pé de moleque"], "Bolo de rolo",
   "O bolo de rolo é Patrimônio Cultural Imaterial de Pernambuco.", "Governo de Pernambuco", br=True)
mc(G, "técnicas", 4, 16, "Qual molho clássico francês é feito com gema de ovo, manteiga e suco de limão?",
   ["Holandês", "Bechamel", "Vinagrete", "Pesto"], "Holandês",
   "O molho holandês é base dos ovos Benedict.", "Le Cordon Bleu")
