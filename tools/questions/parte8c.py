# Perguntas novas (parte 8c). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== CINEMA
C = "cin"
mc(C, "clássicos", 1, 6, "Em 'O Mágico de Oz', qual personagem queria ganhar um cérebro?",
   ["Espantalho", "Homem de Lata", "Leão Covarde", "Totó"], "Espantalho",
   "O Homem de Lata queria um coração, e o Leão, coragem.",
   "IMDb – O Mágico de Oz (1939)")
mc(C, "aventura", 1, 8, "Em 'Jurassic Park', qual dinossauro gigante faz a água do copo tremer quando se aproxima?",
   ["Tiranossauro rex", "Braquiossauro", "Tricerátops", "Estegossauro"], "Tiranossauro rex",
   "A água tremendo no copo anuncia os passos pesados do tiranossauro.",
   "IMDb – Jurassic Park: O Parque dos Dinossauros (1993)")
mc(C, "comédia", 1, 8, "Na comédia de 1992, o cachorro São Bernardo tem o nome de qual compositor famoso?",
   ["Beethoven", "Mozart", "Bach", "Chopin"], "Beethoven",
   "O filme 'Beethoven – O Magnífico' fez tanto sucesso que ganhou várias continuações.",
   "IMDb – Beethoven – O Magnífico (1992)")
op(C, "Hollywood", 1, 10, "Em qual bairro de Los Angeles fica o famoso letreiro branco no morro, símbolo do cinema americano?",
   "Hollywood", ["hollywood"],
   "Hollywood virou sinônimo da indústria de cinema dos Estados Unidos.",
   "Hollywood Sign Trust")
mc(C, "elenco", 1, 10, "Qual ator interpretou Harry Potter nos oito filmes da saga?",
   ["Daniel Radcliffe", "Rupert Grint", "Tom Felton", "Robert Pattinson"], "Daniel Radcliffe",
   "Rupert Grint fez o Rony, e Tom Felton, o Draco Malfoy.",
   "IMDb – Harry Potter e a Pedra Filosofal (2001)")
tf(C, "clássicos", 2, 10, "Em 'Karatê Kid', o senhor Miyagi treina o jovem Daniel mandando-o encerar carros.", True,
   "O 'passe a cera, tire a cera' ensinava, sem ele perceber, movimentos de defesa.",
   "IMDb – Karatê Kid: A Hora da Verdade (1984)")
mc(C, "elenco", 2, 12, "Qual cantora estrelou 'O Guarda-Costas', de 1992, ao lado de Kevin Costner?",
   ["Whitney Houston", "Madonna", "Mariah Carey", "Celine Dion"], "Whitney Houston",
   "A trilha do filme tem 'I Will Always Love You', grande sucesso na voz dela.",
   "IMDb – O Guarda-Costas (1992)")
mc(C, "elenco", 2, 12, "Qual atriz interpretou Rose no filme 'Titanic', de 1997?",
   ["Kate Winslet", "Nicole Kidman", "Gwyneth Paltrow", "Julia Roberts"], "Kate Winslet",
   "Ela contracenou com Leonardo DiCaprio, que viveu Jack.",
   "IMDb – Titanic (1997)")
mc(C, "clássicos", 2, 14, "Qual filme de 1939 tem Scarlett O'Hara como protagonista?",
   ["E o Vento Levou", "Casablanca", "Cidadão Kane", "Ben-Hur"], "E o Vento Levou",
   "Vivien Leigh ganhou o Oscar de Melhor Atriz pelo papel de Scarlett.",
   "IMDb – E o Vento Levou (1939)")
mc(C, "trilhas sonoras", 2, 14, "Qual compositor criou as trilhas de 'Star Wars', 'Tubarão' e 'Superman'?",
   ["John Williams", "Hans Zimmer", "Ennio Morricone", "Danny Elfman"], "John Williams",
   "Ele também compôs o tema dos primeiros filmes de Harry Potter.",
   "IMDb – John Williams")
mc(C, "trilhas sonoras", 3, 14, "Qual compositor alemão fez as trilhas de 'Interestelar' e 'Duna'?",
   ["Hans Zimmer", "John Williams", "Howard Shore", "James Horner"], "Hans Zimmer",
   "Ele ganhou o Oscar de Melhor Trilha Sonora por 'Duna', de 2021.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2022")
mc(C, "trilhas sonoras", 3, 16, "Qual compositor italiano fez as trilhas de 'Cinema Paradiso' e dos faroestes de Sergio Leone?",
   ["Ennio Morricone", "Nino Rota", "Hans Zimmer", "John Williams"], "Ennio Morricone",
   "Morricone ganhou o Oscar de trilha sonora por 'Os Oito Odiados', de 2015.",
   "IMDb – Ennio Morricone")
tf(C, "clássicos", 3, 14, "Orson Welles dirigiu e também estrelou o filme 'Cidadão Kane', de 1941.", True,
   "Welles tinha só 25 anos quando fez o filme, considerado um dos maiores da história.",
   "IMDb – Cidadão Kane (1941)")
mc(C, "cinema europeu", 3, 16, "Qual diretor italiano fez 'A Doce Vida', vencedor da Palma de Ouro em 1960?",
   ["Federico Fellini", "Sergio Leone", "Roberto Rossellini", "Bernardo Bertolucci"], "Federico Fellini",
   "O filme tem a famosa cena de Anita Ekberg na Fontana di Trevi, em Roma.",
   "Festival de Cannes – A Doce Vida (1960)")
mc(C, "cinema latino-americano", 4, 16, "Qual filme argentino ganhou o Oscar de Melhor Filme Estrangeiro na cerimônia de 2010?",
   ["O Segredo dos Seus Olhos", "Relatos Selvagens", "Nove Rainhas", "O Filho da Noiva"], "O Segredo dos Seus Olhos",
   "O filme foi dirigido por Juan José Campanella e estrelado por Ricardo Darín.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2010")
mc(C, "cinema brasileiro", 3, 16, "Qual filme de Kleber Mendonça Filho e Juliano Dornelles ganhou o Prêmio do Júri em Cannes, em 2019?",
   ["Bacurau", "Aquarius", "O Som ao Redor", "Que Horas Ela Volta?"], "Bacurau",
   "O filme se passa num pequeno povoado fictício do sertão nordestino.",
   "Festival de Cannes – Bacurau (2019)", br=True)
op(C, "cinema brasileiro", 3, 14, "Qual cantora e atriz, chamada de 'Pequena Notável', fez sucesso em Hollywood com turbantes enfeitados de frutas?",
   "Carmen Miranda", ["carmen miranda", "carmem miranda"],
   "Ela nasceu em Portugal, cresceu no Rio de Janeiro e virou estrela nos Estados Unidos nos anos 1940.",
   "Dicionário Cravo Albin da MPB – Carmen Miranda", br=True)

# =========================================================== FILMES INFANTIS
I = "inf"
mc(I, "desenhos clássicos", 1, 6, "Qual é o nome da namorada do Mickey?",
   ["Minnie", "Margarida", "Clarabela", "Sininho"], "Minnie",
   "Minnie usa um laço de bolinhas na cabeça e é companheira do Mickey desde 1928.",
   "Disney – O Vapor Willie (1928)")
mc(I, "desenhos clássicos", 1, 6, "Qual pato de roupa de marinheiro é um dos melhores amigos do Mickey?",
   ["Pato Donald", "Patolino", "Tio Patinhas", "Zé Carioca"], "Pato Donald",
   "Donald é conhecido pela roupa de marinheiro e pelo jeito nervoso de falar.",
   "Disney – A Galinha Sábia (1934)")
mc(I, "animação", 1, 6, "Em 'Toy Story', qual é o nome do dinossauro verde de brinquedo?",
   ["Rex", "Slinky", "Bala no Alvo", "Sr. Cabeça de Batata"], "Rex",
   "Rex é um tiranossauro de plástico, grande mas muito medroso.",
   "Disney/Pixar – Toy Story (1995)")
mc(I, "animação", 1, 6, "Em 'A Era do Gelo', que animal é o Manny?",
   ["Mamute", "Elefante", "Rinoceronte", "Urso"], "Mamute",
   "Manny é um mamute peludo que viaja com a preguiça Sid e o tigre-dentes-de-sabre Diego.",
   "Blue Sky Studios – A Era do Gelo (2002)")
mc(I, "animação", 1, 7, "Em 'Shrek 2', qual personagem de chapéu e botas vira amigo do ogro?",
   ["Gato de Botas", "Pinóquio", "Biscoito", "Príncipe Encantado"], "Gato de Botas",
   "O Gato de Botas fez tanto sucesso que ganhou filmes próprios.",
   "DreamWorks – Shrek 2 (2004)")
mc(I, "animação", 1, 7, "Em 'Aladdin', qual é o nome da princesa que tem um tigre de estimação?",
   ["Jasmine", "Ariel", "Pocahontas", "Mulan"], "Jasmine",
   "O tigre da princesa Jasmine se chama Rajá.",
   "Disney – Aladdin (1992)")
tf(I, "animação", 1, 8, "Em 'Monstros S.A.', os monstros usam os gritos das crianças para gerar energia.", True,
   "Por isso a empresa mandava os monstros assustarem crianças durante a noite.",
   "Disney/Pixar – Monstros S.A. (2001)")
mc(I, "desenhos clássicos", 2, 8, "Qual é o nome do passarinho amarelo que o gato Frajola vive tentando pegar?",
   ["Piu-Piu", "Pica-Pau", "Papa-Léguas", "Patolino"], "Piu-Piu",
   "Piu-Piu e Frajola são personagens dos desenhos Looney Tunes, da Warner.",
   "Warner Bros. – Looney Tunes")
mc(I, "animação", 2, 8, "Em 'Divertida Mente', qual emoção é vermelha e solta fogo pela cabeça?",
   ["Raiva", "Medo", "Nojinho", "Tristeza"], "Raiva",
   "Quando fica furiosa, a Raiva solta labaredas pelo topo da cabeça.",
   "Disney/Pixar – Divertida Mente (2015)")
mc(I, "animação", 2, 8, "Em 'Valente', qual princesa ruiva é ótima no arco e flecha?",
   ["Merida", "Anna", "Rapunzel", "Aurora"], "Merida",
   "A história de Merida se passa nas montanhas da Escócia.",
   "Disney/Pixar – Valente (2012)")
mc(I, "animação", 2, 10, "Em 'Up – Altas Aventuras', qual é o nome do pequeno escoteiro que viaja com o senhor Carl?",
   ["Russell", "Kevin", "Dug", "Charles"], "Russell",
   "Kevin é a ave colorida e Dug, o cachorro falante do filme.",
   "Disney/Pixar – Up – Altas Aventuras (2009)")
mc(I, "animação", 2, 10, "Em 'Como Treinar o Seu Dragão', qual é o nome do dragão preto que vira amigo de Soluço?",
   ["Banguela", "Smaug", "Mushu", "Malévola"], "Banguela",
   "O apelido vem dos dentes que ele esconde quando quer.",
   "DreamWorks – Como Treinar o Seu Dragão (2010)")
tf(I, "estúdios", 2, 10, "O filme 'Kung Fu Panda' foi produzido pela DreamWorks.", True,
   "O filme de 2008 foi um dos maiores sucessos do estúdio, depois de 'Shrek'.",
   "DreamWorks – Kung Fu Panda (2008)")
op(I, "animação", 2, 10, "Em 'Ratatouille', qual é o nome do jovem ajudante de cozinha que o rato Remy controla puxando o cabelo?",
   "Linguini", ["linguini", "alfredo linguini"],
   "Escondido no chapéu de Linguini, Remy comanda as receitas do restaurante.",
   "Disney/Pixar – Ratatouille (2007)")
mc(I, "Ghibli", 3, 12, "Qual diretor japonês, um dos fundadores do Studio Ghibli, dirigiu 'A Viagem de Chihiro'?",
   ["Hayao Miyazaki", "Akira Kurosawa", "Isao Takahata", "Makoto Shinkai"], "Hayao Miyazaki",
   "Com esse filme, Miyazaki ganhou o Oscar de Melhor Filme de Animação em 2003.",
   "Studio Ghibli – A Viagem de Chihiro (2001)")
mc(I, "Ghibli", 3, 12, "Em 'O Serviço de Entregas da Kiki', qual é o nome do gato preto da bruxinha?",
   ["Jiji", "Totoro", "Luna", "Calcifer"], "Jiji",
   "Kiki voa numa vassoura entregando encomendas, sempre com o gatinho Jiji.",
   "Studio Ghibli – O Serviço de Entregas da Kiki (1989)")
tf(I, "animação brasileira", 3, 12, "A animação brasileira 'O Menino e o Mundo', de Alê Abreu, foi indicada ao Oscar de Melhor Filme de Animação.", True,
   "A indicação veio na cerimônia de 2016, a primeira de um longa animado brasileiro.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2016", br=True)
mc(I, "estúdios", 4, 14, "Qual foi o primeiro longa-metragem de animação da DreamWorks, lançado em 1998?",
   ["FormiguinhaZ", "Shrek", "O Príncipe do Egito", "A Fuga das Galinhas"], "FormiguinhaZ",
   "O filme conta a história da formiga operária Z e saiu meses antes de 'O Príncipe do Egito'.",
   "DreamWorks – FormiguinhaZ (1998)")

# =========================================================== MÚSICA
M = "mus"
mc(M, "instrumentos", 1, 6, "Qual instrumento a gente toca chacoalhando, porque tem sementes ou bolinhas dentro?",
   ["Chocalho", "Violão", "Flauta", "Piano"], "Chocalho",
   "O chocalho é um instrumento de percussão que faz barulho quando é sacudido.",
   "Dicionário Cravo Albin da MPB – instrumentos de percussão")
mc(M, "notas musicais", 1, 6, "Qual nota musical vem logo depois do dó?",
   ["Ré", "Mi", "Fá", "Si"], "Ré",
   "A sequência das notas é dó, ré, mi, fá, sol, lá, si.",
   "Teoria musical – escala de dó maior")
mc(M, "cantigas", 1, 6, "Na cantiga de roda, o cravo brigou com quem?",
   ["A rosa", "O lírio", "A margarida", "O girassol"], "A rosa",
   "Na cantiga, o cravo saiu ferido e a rosa, despedaçada.",
   "Cancioneiro popular brasileiro – O Cravo e a Rosa", br=True)
mc(M, "instrumentos", 1, 8, "Qual pequeno instrumento de sopro cabe no bolso e é tocado soprando e puxando o ar pelos furinhos?",
   ["Gaita", "Trompete", "Tuba", "Clarinete"], "Gaita",
   "A gaita de boca, ou harmônica, é muito usada no blues e no folk.",
   "Enciclopédia Britannica – Harmonica")
tf(M, "instrumentos", 1, 10, "O violoncelo é tocado com o músico sentado, apoiando o instrumento no chão, entre as pernas.", True,
   "Ele é maior e tem o som mais grave que o violino e a viola.",
   "Enciclopédia Britannica – Cello")
mc(M, "instrumentos", 2, 10, "Qual instrumento é o maior e o mais grave da família dos metais?",
   ["Tuba", "Trompete", "Trompa", "Flauta"], "Tuba",
   "A tuba é tocada com o instrumento apoiado no colo ou preso ao corpo.",
   "Enciclopédia Britannica – Tuba")
mc(M, "instrumentos", 2, 10, "Qual tambor grande, de som grave, marca o ritmo de uma bateria de escola de samba?",
   ["Surdo", "Tamborim", "Cuíca", "Agogô"], "Surdo",
   "O surdo é o coração da bateria e segura o andamento do samba.",
   "Dicionário Cravo Albin da MPB – surdo", br=True)
mc(M, "pop internacional", 2, 12, "Qual cantora britânica lançou o álbum '21', com o sucesso 'Rolling in the Deep'?",
   ["Adele", "Amy Winehouse", "Dua Lipa", "Lady Gaga"], "Adele",
   "O álbum '21', de 2011, ganhou o Grammy de Álbum do Ano.",
   "Recording Academy – Grammy 2012")
mc(M, "sertanejo", 2, 12, "Qual cantora sertaneja, chamada de 'Rainha da Sofrência', morreu num acidente aéreo em 2021?",
   ["Marília Mendonça", "Paula Fernandes", "Maiara", "Naiara Azevedo"], "Marília Mendonça",
   "Ela fez enorme sucesso com músicas como 'Infiel' e 'Supera'.",
   "Dicionário Cravo Albin da MPB – Marília Mendonça", br=True)
mc(M, "rock nacional", 2, 14, "Qual banda de rock brasileiro teve Cazuza como vocalista no começo dos anos 1980?",
   ["Barão Vermelho", "Titãs", "Ultraje a Rigor", "Kid Abelha"], "Barão Vermelho",
   "Cazuza deixou o Barão Vermelho em 1985 para seguir carreira solo.",
   "Dicionário Cravo Albin da MPB – Barão Vermelho", br=True)
mc(M, "rock nacional", 2, 14, "Qual banda tem Herbert Vianna como vocalista e guitarrista?",
   ["Os Paralamas do Sucesso", "Capital Inicial", "Skank", "Biquíni Cavadão"], "Os Paralamas do Sucesso",
   "O trio é formado por Herbert Vianna, Bi Ribeiro e João Barone.",
   "Dicionário Cravo Albin da MPB – Os Paralamas do Sucesso", br=True)
mc(M, "MPB", 2, 14, "Qual cantora baiana é irmã de Caetano Veloso?",
   ["Maria Bethânia", "Gal Costa", "Daniela Mercury", "Margareth Menezes"], "Maria Bethânia",
   "Os dois nasceram em Santo Amaro da Purificação, no Recôncavo Baiano.",
   "Dicionário Cravo Albin da MPB – Maria Bethânia", br=True)
mc(M, "MPB", 2, 14, "Qual cantor, criado em Minas Gerais, gravou 'Travessia' e 'Maria, Maria'?",
   ["Milton Nascimento", "Lô Borges", "Beto Guedes", "Djavan"], "Milton Nascimento",
   "Milton é um dos nomes centrais do Clube da Esquina.",
   "Dicionário Cravo Albin da MPB – Milton Nascimento", br=True)
mc(M, "rock nacional", 3, 14, "Qual banda gaúcha, liderada por Humberto Gessinger, gravou 'Infinita Highway'?",
   ["Engenheiros do Hawaii", "Nenhum de Nós", "Os Replicantes", "Cachorro Grande"], "Engenheiros do Hawaii",
   "A banda surgiu em Porto Alegre, em meados dos anos 1980.",
   "Dicionário Cravo Albin da MPB – Engenheiros do Hawaii", br=True)
tf(M, "rock nacional", 3, 14, "Arnaldo Antunes foi um dos integrantes da banda Titãs.", True,
   "Ele deixou os Titãs em 1992 e depois formou os Tribalistas com Marisa Monte e Carlinhos Brown.",
   "Dicionário Cravo Albin da MPB – Arnaldo Antunes", br=True)
mc(M, "sertanejo", 3, 14, "Qual canção de Almir Sater e Renato Teixeira começa com 'Ando devagar porque já tive pressa'?",
   ["Tocando em Frente", "Romaria", "Chalana", "Menino da Porteira"], "Tocando em Frente",
   "A música ficou famosa também na voz de Maria Bethânia.",
   "Dicionário Cravo Albin da MPB – Tocando em Frente", br=True)
op(M, "choro", 3, 16, "Qual músico carioca compôs 'Carinhoso', um dos choros mais famosos do Brasil?",
   "Pixinguinha", ["pixinguinha", "alfredo da rocha viana filho", "alfredo da rocha vianna filho"],
   "A melodia é de Pixinguinha, e a letra foi feita depois por João de Barro, o Braguinha.",
   "Dicionário Cravo Albin da MPB – Carinhoso", br=True)
mc(M, "choro", 4, 16, "Qual cavaquinista compôs o choro 'Brasileirinho', de 1949?",
   ["Waldir Azevedo", "Jacob do Bandolim", "Ernesto Nazareth", "Pixinguinha"], "Waldir Azevedo",
   "'Brasileirinho' é um dos choros mais tocados no cavaquinho até hoje.",
   "Dicionário Cravo Albin da MPB – Waldir Azevedo", br=True)

# =========================================================== ESPORTES
E = "esp"
mc(E, "lutas", 1, 6, "Em qual esporte os atletas usam luvas grandes e lutam dentro de um ringue?",
   ["Boxe", "Judô", "Esgrima", "Natação"], "Boxe",
   "No boxe, os golpes só podem ser dados com as mãos fechadas, usando luvas.",
   "World Boxing – regras do boxe olímpico")
mc(E, "basquete", 1, 6, "No basquete, onde o jogador tem de colocar a bola para marcar pontos?",
   ["Na cesta", "No gol", "No buraco", "Na rede do meio"], "Na cesta",
   "A cesta é um aro com uma rede, preso a uma tabela.",
   "FIBA – Regras oficiais do basquete")
mc(E, "vôlei", 1, 8, "Qual esporte olímpico é disputado na areia, com dois jogadores de cada lado da rede?",
   ["Vôlei de praia", "Handebol", "Basquete", "Polo aquático"], "Vôlei de praia",
   "O vôlei de praia entrou nos Jogos Olímpicos em Atlanta 1996.",
   "Comitê Olímpico Internacional – Vôlei de praia")
mc(E, "atletismo", 1, 8, "Na corrida de revezamento, o que um corredor entrega para o outro?",
   ["Bastão", "Bandeira", "Bola", "Tocha"], "Bastão",
   "O bastão precisa ser passado dentro de uma zona marcada na pista.",
   "World Athletics – Regras de revezamento")
mc(E, "Fórmula 1", 1, 10, "Qual equipe italiana de Fórmula 1 é famosa por seus carros vermelhos?",
   ["Ferrari", "McLaren", "Williams", "Red Bull"], "Ferrari",
   "A Ferrari é a equipe mais antiga ainda em atividade na Fórmula 1.",
   "Fórmula 1 – Scuderia Ferrari")
mc(E, "vôlei", 1, 10, "No vôlei, como se chama o golpe em que o jogador bate forte na bola para baixo, no campo adversário?",
   ["Cortada", "Saque", "Manchete", "Toque"], "Cortada",
   "A cortada é o principal golpe de ataque do vôlei.",
   "FIVB – Regras oficiais do voleibol")
tf(E, "tênis", 2, 10, "No tênis, os pontos de um game são contados como 15, 30 e 40.", True,
   "Quem tem 40 e vence mais um ponto ganha o game, a não ser que haja empate em 40.",
   "ITF – Regras do tênis")
mc(E, "tênis", 2, 12, "Qual tenista espanhol venceu o torneio de Roland Garros 14 vezes?",
   ["Rafael Nadal", "Carlos Alcaraz", "Novak Djokovic", "Roger Federer"], "Rafael Nadal",
   "Nadal é o maior campeão da história de Roland Garros, disputado no saibro de Paris.",
   "Roland Garros – lista de campeões")
mc(E, "tênis", 2, 14, "Gustavo Kuerten, o Guga, foi três vezes campeão de qual torneio de tênis?",
   ["Roland Garros", "Wimbledon", "US Open", "Australian Open"], "Roland Garros",
   "Guga venceu o torneio francês em 1997, 2000 e 2001.",
   "Roland Garros – lista de campeões", br=True)
mc(E, "Fórmula 1", 2, 12, "Qual autódromo de São Paulo recebe a corrida brasileira da Fórmula 1?",
   ["Interlagos", "Jacarepaguá", "Tarumã", "Velopark"], "Interlagos",
   "O nome oficial do circuito é Autódromo José Carlos Pace.",
   "Fórmula 1 – Grande Prêmio de São Paulo", br=True)
mc(E, "esportes paralímpicos", 2, 14, "Qual nadador é o maior medalhista paralímpico do Brasil?",
   ["Daniel Dias", "Clodoaldo Silva", "Gabriel Araújo", "André Brasil"], "Daniel Dias",
   "Daniel Dias conquistou 27 medalhas paralímpicas, sendo 14 de ouro.",
   "Comitê Paralímpico Brasileiro", br=True, ref="2026-10-13")
mc(E, "atletismo", 2, 12, "Qual prova do atletismo tem barreiras pesadas e um fosso com água no caminho?",
   ["3.000 metros com obstáculos", "110 metros com barreiras", "Revezamento 4x100", "Maratona"], "3.000 metros com obstáculos",
   "Os corredores pulam o fosso com água uma vez a cada volta.",
   "World Athletics – 3000 metres steeplechase")
tf(E, "Fórmula 1", 3, 14, "Ayrton Senna venceu o Grande Prêmio do Brasil pela primeira vez em 1991.", True,
   "Ele ganhou em Interlagos com o câmbio preso na sexta marcha nas voltas finais.",
   "Fórmula 1 – GP do Brasil de 1991", br=True)
mc(E, "esportes paralímpicos", 3, 14, "Qual esporte paralímpico, criado para atletas cegos, é jogado com as mãos e uma bola com guizo?",
   ["Goalball", "Bocha", "Futebol de 5", "Vôlei sentado"], "Goalball",
   "Os jogadores usam vendas e se guiam pelo som do guizo dentro da bola.",
   "Comitê Paralímpico Brasileiro – Goalball")
tf(E, "esportes paralímpicos", 3, 16, "A seleção brasileira de futebol de 5, para cegos, ganhou o ouro em todas as Paralimpíadas de 2004 a 2020.", True,
   "Foram cinco ouros seguidos: Atenas, Pequim, Londres, Rio e Tóquio.",
   "Comitê Paralímpico Brasileiro – Futebol de 5", br=True)
mc(E, "vôlei", 3, 14, "Em quais Jogos Olímpicos a seleção feminina de vôlei de quadra do Brasil ganhou seu primeiro ouro?",
   ["Pequim 2008", "Atenas 2004", "Londres 2012", "Sydney 2000"], "Pequim 2008",
   "A seleção feminina voltou a ganhar o ouro quatro anos depois, em Londres 2012.",
   "Comitê Olímpico do Brasil", br=True)
op(E, "canoagem", 3, 14, "Qual canoísta baiano ganhou a medalha de ouro no C1 1000 metros nos Jogos de Tóquio?",
   "Isaquias Queiroz", ["isaquias queiroz", "isaquias queiroz dos santos"],
   "Isaquias é o brasileiro com mais medalhas olímpicas na canoagem de velocidade.",
   "Comitê Olímpico do Brasil", br=True)
mc(E, "basquete", 4, 16, "Em que ano a seleção brasileira masculina de basquete ganhou seu primeiro título mundial?",
   ["1959", "1963", "1970", "1978"], "1959",
   "O primeiro título veio no Chile, e o segundo em 1963, no Rio de Janeiro.",
   "FIBA – Copa do Mundo de Basquete 1959", br=True)

# =========================================================== MARCAS
A = "mar"
mc(A, "mascotes", 1, 6, "Que animal é o mascote do achocolatado Nesquik?",
   ["Coelho", "Tigre", "Urso", "Cachorro"], "Coelho",
   "O coelhinho do Nesquik aparece nas embalagens desde os anos 1970.",
   "Nestlé – Nesquik")
mc(A, "logotipos", 1, 6, "De que cor é o grande 'M' do logotipo do McDonald's?",
   ["Amarelo", "Azul", "Verde", "Roxo"], "Amarelo",
   "O 'M' é formado pelos chamados arcos dourados.",
   "McDonald's – história da marca")
mc(A, "logotipos", 1, 6, "Qual é a cor principal da lata do Guaraná Antarctica?",
   ["Verde", "Rosa", "Roxo", "Preto"], "Verde",
   "O verde é a cor tradicional do refrigerante, lançado em 1921.",
   "Ambev – Guaraná Antarctica", br=True)
mc(A, "produtos", 1, 8, "Qual chocolate suíço é famoso pelo formato de triângulos, como montanhas?",
   ["Toblerone", "Kit Kat", "Twix", "Bis"], "Toblerone",
   "O formato é associado ao monte Matterhorn, nos Alpes suíços.",
   "Mondelēz – Toblerone")
mc(A, "origem dos produtos", 2, 10, "Qual massinha de modelar foi criada, nos Estados Unidos, como um produto para limpar papel de parede?",
   ["Play-Doh", "Lego", "Slime", "Durepoxi"], "Play-Doh",
   "A massa limpadora virou brinquedo nos anos 1950, quando a empresa percebeu que as crianças gostavam de modelá-la.",
   "Hasbro – história da Play-Doh")
mc(A, "lanchonetes", 2, 10, "Qual rede brasileira de lanchonetes, fundada em São Paulo em 1988, tem a esfiha como carro-chefe?",
   ["Habib's", "Bob's", "Giraffas", "Spoleto"], "Habib's",
   "A rede foi fundada pelo empresário Alberto Saraiva.",
   "Habib's – história da empresa", br=True)
mc(A, "origem das marcas", 2, 12, "A Nestlé foi fundada em qual país?",
   ["Suíça", "França", "Alemanha", "Estados Unidos"], "Suíça",
   "A sede da empresa fica em Vevey, às margens do lago Léman.",
   "Nestlé – história da empresa")
mc(A, "origem das marcas", 2, 12, "Qual empresa fabrica o refrigerante Guaraná Antarctica?",
   ["Ambev", "Coca-Cola", "Nestlé", "Pepsico"], "Ambev",
   "A Ambev nasceu em 1999 da união da Antarctica com a Brahma.",
   "Ambev – nossas marcas", br=True, ref="2026-10-13")
tf(A, "origem das marcas", 2, 12, "A fabricante de lápis Faber-Castell é uma empresa de origem alemã.", True,
   "A empresa nasceu em 1761, perto da cidade de Nuremberg, na Alemanha.",
   "Faber-Castell – história da empresa")
mc(A, "slogans", 2, 12, "Qual chocolate ficou famoso no mundo com o slogan 'Have a break'?",
   ["Kit Kat", "Twix", "Snickers", "Toblerone"], "Kit Kat",
   "O slogan completo é 'Have a break, have a Kit Kat'.",
   "Nestlé – Kit Kat")
mc(A, "mascotes", 2, 12, "Qual personagem de cabelo branco e gravata-borboleta aparece no logotipo do KFC?",
   ["Coronel Sanders", "Ronald McDonald", "Tio Sam", "Capitão Iglo"], "Coronel Sanders",
   "Harland Sanders foi quem criou a receita do frango frito da rede.",
   "KFC – história da marca")
mc(A, "marcas brasileiras", 2, 14, "Qual marca brasileira de perfumes e cosméticos nasceu como uma pequena farmácia em Curitiba, em 1977?",
   ["O Boticário", "Natura", "Avon", "Jequiti"], "O Boticário",
   "A empresa foi fundada pelo farmacêutico Miguel Krigsner.",
   "Grupo Boticário – história", br=True)
mc(A, "produtos", 2, 14, "Qual marca ficou famosa pelas câmeras que imprimem a foto na hora?",
   ["Polaroid", "Canon", "Nikon", "GoPro"], "Polaroid",
   "A primeira câmera instantânea da Polaroid foi lançada nos Estados Unidos em 1948.",
   "Polaroid – história da marca")
op(A, "tecnologia", 2, 12, "Como se chama a empresa dona do Facebook, do Instagram e do WhatsApp?",
   "Meta", ["meta", "meta platforms"],
   "O Facebook Inc. mudou o nome para Meta em 2021.",
   "Meta – comunicado de 28/10/2021", ref="2026-10-13")
tf(A, "origem dos produtos", 3, 14, "O refrigerante Fanta foi criado na Alemanha durante a Segunda Guerra Mundial.", True,
   "A filial alemã da Coca-Cola criou a Fanta em 1940, quando faltava xarope de Coca-Cola no país.",
   "The Coca-Cola Company – história da Fanta")
mc(A, "slogans", 3, 14, "Qual empresa usou o slogan 'Think different', que quer dizer 'pense diferente', a partir de 1997?",
   ["Apple", "Microsoft", "IBM", "Google"], "Apple",
   "A campanha mostrava personalidades como Einstein e Gandhi.",
   "Apple – campanha Think Different (1997)")
mc(A, "marcas brasileiras", 3, 16, "Qual empresa lançou o Kichute, tênis com travas de borracha muito usado para jogar bola nos anos 1970?",
   ["Alpargatas", "Rainha", "Topper", "Penalty"], "Alpargatas",
   "O Kichute, preto e com cadarço comprido, virou febre entre os meninos dos anos 1970.",
   "Alpargatas – história da empresa", br=True)
tf(A, "origem das marcas", 4, 16, "A marca de sorvetes Häagen-Dazs foi criada nos Estados Unidos, apesar do nome que parece escandinavo.", True,
   "O nome foi inventado por Reuben Mattus, em Nova York, em 1960.",
   "Häagen-Dazs – história da marca")

# =========================================================== CULINÁRIA
G = "gas"
mc(G, "frutas", 1, 6, "Qual fruta azedinha é usada para fazer limonada?",
   ["Limão", "Banana", "Uva", "Manga"], "Limão",
   "A limonada mistura suco de limão, água e açúcar.",
   "Embrapa – Limão")
mc(G, "alimentos", 1, 6, "De qual animal vem a maioria dos ovos que comemos?",
   ["Galinha", "Vaca", "Porco", "Cabra"], "Galinha",
   "Também se comem ovos de codorna e de pata, mas os de galinha são os mais comuns.",
   "Embrapa – Avicultura")
mc(G, "verduras e legumes", 1, 6, "Qual destes alimentos é verde e parece uma arvorezinha?",
   ["Brócolis", "Cenoura", "Beterraba", "Abóbora"], "Brócolis",
   "O brócolis é formado por pequenos botões de flor ainda fechados.",
   "Embrapa Hortaliças – Brócolis")
mc(G, "salgados", 1, 8, "Qual salgado frito, de massa fina e recheado, é o par famoso do caldo de cana nas feiras?",
   ["Pastel", "Pudim", "Brigadeiro", "Pão de queijo"], "Pastel",
   "O pastel de feira é um clássico das feiras livres de São Paulo.",
   "Prefeitura de São Paulo – feiras livres", br=True)
tf(G, "ingredientes", 1, 8, "A mandioca também é chamada de aipim e de macaxeira, dependendo da região do Brasil.", True,
   "Aipim é comum no Rio e no Sul, e macaxeira, no Norte e no Nordeste.",
   "Embrapa Mandioca e Fruticultura", br=True)
mc(G, "frutas brasileiras", 1, 8, "Qual fruta tem a castanha pendurada do lado de fora?",
   ["Caju", "Manga", "Goiaba", "Pitanga"], "Caju",
   "A castanha é o verdadeiro fruto do cajueiro; a parte suculenta é o pedúnculo.",
   "Embrapa Agroindústria Tropical – Caju", br=True)
mc(G, "temperos", 2, 10, "No Sudeste, o cheiro-verde junta cebolinha com qual outro tempero?",
   ["Salsinha", "Orégano", "Cominho", "Pimenta-do-reino"], "Salsinha",
   "No Nordeste, o cheiro-verde costuma levar coentro no lugar da salsinha.",
   "Embrapa Hortaliças – Salsa e cebolinha", br=True)
mc(G, "temperos", 2, 10, "Qual especiaria, que parece um preguinho, vai no quentão das festas juninas?",
   ["Cravo-da-índia", "Noz-moscada", "Pimenta-do-reino", "Orégano"], "Cravo-da-índia",
   "O cravo-da-índia é o botão seco da flor de uma árvore originária da Indonésia.",
   "Embrapa – Especiarias", br=True)
mc(G, "frutas", 2, 10, "Qual destas frutas pequenas e vermelhas é famosa por ter muita vitamina C?",
   ["Acerola", "Banana", "Pera", "Melão"], "Acerola",
   "A acerola tem muito mais vitamina C que a laranja.",
   "Embrapa – Acerola")
mc(G, "doces", 2, 10, "Qual doce cremoso e marrom é feito cozinhando leite com açúcar por muito tempo?",
   ["Doce de leite", "Goiabada", "Marmelada", "Cocada"], "Doce de leite",
   "O doce de leite é muito popular no Brasil, na Argentina e no Uruguai.",
   "Embrapa Gado de Leite – Doce de leite")
op(G, "frutas brasileiras", 2, 10, "Qual castanha da Amazônia, vendida no mundo todo, tem o nome de um estado brasileiro?",
   "Castanha-do-pará", ["castanha-do-pará", "castanha do pará", "castanha-do-brasil", "castanha do brasil"],
   "Ela também é chamada de castanha-do-brasil e vem de uma árvore enorme da floresta.",
   "Embrapa Amazônia Oriental – Castanha-do-brasil", br=True)
mc(G, "culinária do mundo", 2, 12, "Qual prato italiano é um arroz cozido aos poucos até ficar bem cremoso?",
   ["Risoto", "Nhoque", "Lasanha", "Polenta"], "Risoto",
   "O risoto é feito com arroz de grão curto, como o arbóreo, e caldo quente.",
   "Accademia Italiana della Cucina – Risotto")
mc(G, "culinária do mundo", 3, 14, "Qual bolinho frito do Oriente Médio é feito de grão-de-bico moído com temperos?",
   ["Falafel", "Quibe", "Esfiha", "Charuto"], "Falafel",
   "O falafel é servido no pão sírio, com salada e molho de tahine.",
   "Enciclopédia Britannica – Falafel")
mc(G, "frutas brasileiras", 3, 14, "Qual fruta pequena e azedinha é chamada de taperebá na Amazônia?",
   ["Cajá", "Pitanga", "Graviola", "Jambo"], "Cajá",
   "O cajá é muito usado em sucos e sorvetes no Norte e no Nordeste.",
   "Embrapa – Cajá", br=True)
mc(G, "frutas brasileiras", 3, 14, "O umbu é uma fruta típica de qual bioma brasileiro?",
   ["Caatinga", "Pampa", "Pantanal", "Mata Atlântica"], "Caatinga",
   "O umbuzeiro guarda água nas raízes e aguenta longos períodos de seca.",
   "Embrapa Semiárido – Umbuzeiro", br=True)
tf(G, "doces regionais", 3, 14, "A cidade gaúcha de Pelotas é famosa pelos seus doces de tradição portuguesa.", True,
   "Os doces de Pelotas, como o quindim e o camafeu, têm Indicação Geográfica reconhecida.",
   "INPI – Indicação Geográfica Pelotas (doces)", br=True)
tf(G, "pratos regionais", 3, 14, "A sopa paraguaia, comum no Mato Grosso do Sul, é na verdade uma torta salgada de milho.", True,
   "Apesar do nome, ela é assada no forno e servida em pedaços.",
   "Governo de Mato Grosso do Sul – culinária sul-mato-grossense", br=True)
op(G, "ingredientes", 3, 14, "Como se chama o trigo partido e pré-cozido usado no quibe e no tabule?",
   "Triguilho", ["triguilho", "trigo para quibe", "trigo para kibe", "bulgur", "trigo bulgur"],
   "Esse trigo é muito usado na culinária árabe, que chegou ao Brasil com imigrantes sírios e libaneses.",
   "Enciclopédia Britannica – Bulgur")
mc(G, "frutas brasileiras", 4, 16, "Qual fruto de palmeira da Amazônia é cozido em água e sal e comido com café?",
   ["Pupunha", "Cupuaçu", "Bacuri", "Graviola"], "Pupunha",
   "Da mesma palmeira também se tira um palmito muito apreciado.",
   "Embrapa Amazônia Ocidental – Pupunha", br=True)
