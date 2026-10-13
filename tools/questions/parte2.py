# Perguntas: Filmes infantis, Novelas, Televisão, Esportes, Marcas e slogans.
from qdsl import mc, op, tf

# =========================================================== FILMES INFANTIS
I = "inf"
mc(I, "Pixar", 1, 6, "Em 'Procurando Nemo', que tipo de animal é o Nemo?",
   ["Peixe-palhaço", "Tubarão", "Tartaruga", "Polvo"], "Peixe-palhaço",
   "Nemo é um peixe-palhaço, que vive entre as anêmonas do mar.",
   "Disney/Pixar – Procurando Nemo (2003)", syn=["peixe", "peixinho", "peixe palhaco"])
mc(I, "Pixar", 1, 6, "Em 'Toy Story', qual é o nome do caubói de brinquedo?",
   ["Woody", "Buzz Lightyear", "Rex", "Slinky"], "Woody",
   "Woody é o brinquedo favorito do menino Andy. Buzz Lightyear é o patrulheiro espacial.",
   "Disney/Pixar – Toy Story (1995)", syn=["xerife woody"])
mc(I, "Disney", 1, 6, "Em 'Frozen', qual é o nome da irmã de Anna que tem poderes de gelo?",
   ["Elsa", "Moana", "Rapunzel", "Ariel"], "Elsa",
   "Elsa é a rainha de Arendelle e canta 'Livre Estou'.",
   "Disney – Frozen (2013)")
mc(I, "Disney", 1, 6, "Qual é o nome do leãozinho protagonista de 'O Rei Leão'?",
   ["Simba", "Mufasa", "Scar", "Nala"], "Simba",
   "Simba é filho do rei Mufasa. Scar é o tio vilão.",
   "Disney – O Rei Leão (1994)")
mc(I, "Disney", 1, 6, "Qual é o nome do boneco de neve falante de 'Frozen'?",
   ["Olaf", "Sven", "Kristoff", "Hans"], "Olaf",
   "Olaf adora abraços quentinhos. Sven é a rena de Kristoff.",
   "Disney – Frozen (2013)")
mc(I, "princesas", 1, 6, "Qual princesa perde um sapatinho de cristal ao sair correndo do baile?",
   ["Cinderela", "Branca de Neve", "Bela", "Aurora"], "Cinderela",
   "À meia-noite o encanto acaba, e o príncipe procura a dona do sapatinho.",
   "Disney – Cinderela (1950)")
mc(I, "princesas", 1, 6, "Em 'A Pequena Sereia', como se chama a sereia protagonista?",
   ["Ariel", "Jasmine", "Mulan", "Pocahontas"], "Ariel",
   "Ariel troca a voz por pernas num acordo com a bruxa Úrsula.",
   "Disney – A Pequena Sereia (1989)")
mc(I, "DreamWorks", 1, 7, "Em 'Shrek', que tipo de criatura é o Shrek?",
   ["Ogro", "Dragão", "Duende", "Gigante"], "Ogro",
   "Shrek é um ogro verde que mora num pântano e vive aventuras com o Burro.",
   "DreamWorks – Shrek (2001)")
mc(I, "Pixar", 1, 7, "Em 'Divertida Mente', qual emoção é a personagem amarela e sempre animada?",
   ["Alegria", "Tristeza", "Raiva", "Medo"], "Alegria",
   "As emoções vivem na mente da menina Riley: Alegria, Tristeza, Raiva, Medo e Nojinho.",
   "Disney/Pixar – Divertida Mente (2015)")
mc(I, "Pixar", 1, 7, "Em 'Carros', qual é o nome do carro de corrida vermelho protagonista?",
   ["Relâmpago McQueen", "Mate", "Doc Hudson", "Sally"], "Relâmpago McQueen",
   "Relâmpago McQueen usa o número 95. Mate é o guincho, seu melhor amigo.",
   "Disney/Pixar – Carros (2006)", syn=["mcqueen", "relampago", "mac queen"])
mc(I, "DreamWorks", 1, 7, "Em 'Madagascar', que animal é o Alex?",
   ["Leão", "Zebra", "Girafa", "Hipopótamo"], "Leão",
   "Alex é o leão; Marty é a zebra, Melman a girafa e Glória a hipopótamo.",
   "DreamWorks – Madagascar (2005)")
mc(I, "Pixar", 2, 8, "Em 'Up – Altas Aventuras', o que faz a casa do senhor Carl voar?",
   ["Balões", "Um foguete", "Asas gigantes", "Um tornado"], "Balões",
   "Carl amarra milhares de balões de gás na casa para viajar até a América do Sul.",
   "Disney/Pixar – Up (2009)", syn=["baloes", "bexigas", "baloes de gas"])
mc(I, "Disney", 2, 9, "Em 'Moana', qual é o nome do semideus que ajuda a heroína?",
   ["Maui", "Hércules", "Tamatoa", "Kakamora"], "Maui",
   "Maui é um semideus que muda de forma graças ao seu anzol mágico.",
   "Disney – Moana (2016)")
mc(I, "Disney", 2, 9, "Em 'Aladdin', como se chama o macaquinho de estimação de Aladdin?",
   ["Abu", "Rajah", "Iago", "Jafar"], "Abu",
   "Rajah é o tigre de Jasmine e Iago é o papagaio do vilão Jafar.",
   "Disney – Aladdin (1992)")
mc(I, "Pixar", 2, 9, "No filme 'Viva – A Vida é uma Festa' (Coco), que instrumento Miguel sonha em tocar?",
   ["Violão", "Piano", "Bateria", "Flauta"], "Violão",
   "Miguel sonha ser músico como seu ídolo, Ernesto de la Cruz.",
   "Disney/Pixar – Viva: A Vida é uma Festa (2017)", syn=["guitarra"])
mc(I, "Pixar", 2, 10, "Qual é o nome do rato cozinheiro de 'Ratatouille'?",
   ["Remy", "Mickey", "Jerry", "Stuart"], "Remy",
   "Remy sonha ser chef em Paris e cozinha escondido no chapéu de Linguini.",
   "Disney/Pixar – Ratatouille (2007)", syn=["remi"])
mc(I, "estúdios", 3, 12, "Qual estúdio produziu 'Toy Story' (1995), o primeiro longa-metragem feito todo em computação gráfica?",
   ["Pixar", "DreamWorks", "Studio Ghibli", "Blue Sky"], "Pixar",
   "A Pixar fez o filme em parceria com a Disney, que o distribuiu.",
   "Pixar Animation Studios – Our story")
mc(I, "anime", 3, 12, "Em qual filme do Studio Ghibli uma menina entra num mundo de espíritos e seus pais viram porcos?",
   ["A Viagem de Chihiro", "Meu Amigo Totoro", "O Castelo Animado", "Ponyo"], "A Viagem de Chihiro",
   "O filme de Hayao Miyazaki venceu o Oscar de Melhor Animação em 2003.",
   "Academy Awards Database – 75º Oscar", syn=["chihiro", "viagem de chihiro"])
mc(I, "Disney", 3, 12, "Em 'Encanto', qual é o sobrenome da família mágica?",
   ["Madrigal", "Rivera", "Flores", "Montoya"], "Madrigal",
   "Cada membro da família Madrigal tem um dom mágico, menos Mirabel.",
   "Disney – Encanto (2021)")
mc(I, "Disney", 4, 14, "Qual foi o primeiro longa-metragem de animação da Disney, lançado em 1937?",
   ["Branca de Neve e os Sete Anões", "Pinóquio", "Fantasia", "Dumbo"], "Branca de Neve e os Sete Anões",
   "O filme estreou em dezembro de 1937; Pinóquio e Fantasia vieram em 1940.",
   "The Walt Disney Company – Disney History", syn=["branca de neve"])

# =========================================================== NOVELAS
N = "nov"
tf(N, "formato", 1, 6, "As novelas brasileiras costumam ser exibidas em capítulos quase todos os dias.", True,
   "As novelas têm capítulos de segunda a sábado e duram vários meses.",
   "Memória Globo – Teledramaturgia", br=True)
mc(N, "infantis", 1, 6, "Qual novela infantil do SBT, de 2012, mostra o dia a dia de uma turma de alunos numa escola?",
   ["Carrossel", "Chiquititas", "Cúmplices de um Resgate", "Poliana"], "Carrossel",
   "Carrossel foi uma adaptação da novela mexicana de mesmo nome, de 1989.",
   "SBT – Carrossel (2012)", br=True)
mc(N, "infantis", 1, 6, "Na novela 'Carrossel', qual é a profissão de Helena?",
   ["Professora", "Médica", "Cozinheira", "Diretora"], "Professora",
   "A doce professora Helena é a querida da turma de alunos da escola.",
   "SBT – Carrossel (2012)", br=True)
mc(N, "infantis", 1, 6, "Qual destes personagens é de uma novela infantil do SBT?",
   ["Cirilo", "Pikachu", "Mickey", "Garfield"], "Cirilo",
   "Cirilo é o menino apaixonado pela Maria Joaquina em 'Carrossel'.",
   "SBT – Carrossel (2012)", br=True)
mc(N, "infantis", 2, 9, "Qual novela infantil do SBT se passa num orfanato e teve versões em 1997 e 2013?",
   ["Chiquititas", "Carrossel", "Cúmplices de um Resgate", "Poliana Moça"], "Chiquititas",
   "As duas versões brasileiras foram adaptadas de uma novela argentina.",
   "SBT – Chiquititas", br=True)
mc(N, "estrangeiras", 1, 10, "Em qual país foi produzida a novela 'Maria do Bairro', exibida várias vezes pelo SBT?",
   ["México", "Argentina", "Colômbia", "Espanha"], "México",
   "A novela da Televisa, de 1995, foi estrelada por Thalía.",
   "Televisa – María la del Barrio (1995)")
mc(N, "juvenis", 1, 10, "Qual novela juvenil da Globo se passava numa escola e teve muitas temporadas a partir de 1995?",
   ["Malhação", "Chiquititas", "Rebelde", "Carrossel"], "Malhação",
   "Malhação estreou em 1995 numa academia e depois passou a se passar em escolas.",
   "Memória Globo – Malhação", br=True)
mc(N, "emissoras", 1, 12, "Qual emissora exibiu a novela 'Avenida Brasil' (2012)?",
   ["TV Globo", "SBT", "Record", "Band"], "TV Globo",
   "Escrita por João Emanuel Carneiro, foi exibida no horário das nove.",
   "Memória Globo – Avenida Brasil", syn=["globo", "rede globo"], br=True)
mc(N, "vilãs", 2, 14, "Em 'Avenida Brasil', qual é o nome da vilã interpretada por Adriana Esteves?",
   ["Carminha", "Nazaré Tedesco", "Odete Roitman", "Flora"], "Carminha",
   "Carminha disputava com Nina (Débora Falabella), que queria vingança.",
   "Memória Globo – Avenida Brasil", br=True)
mc(N, "vilãs", 2, 14, "Qual vilã da novela 'Senhora do Destino' (2004) virou meme na internet?",
   ["Nazaré Tedesco", "Carminha", "Odete Roitman", "Perpétua"], "Nazaré Tedesco",
   "Interpretada por Renata Sorrah, Nazaré virou meme mundial com a cena das contas.",
   "Memória Globo – Senhora do Destino", syn=["nazare"], br=True)
mc(N, "cenários", 2, 14, "A novela 'O Clone' (2001) se passa em parte em qual país do norte da África?",
   ["Marrocos", "Egito", "Tunísia", "Argélia"], "Marrocos",
   "Boa parte da história de Jade e Lucas se passa na cidade de Fez, no Marrocos.",
   "Memória Globo – O Clone", br=True)
mc(N, "autores", 2, 14, "Qual autor de novelas ficou famoso por suas protagonistas chamadas Helena?",
   ["Manoel Carlos", "Walcyr Carrasco", "Benedito Ruy Barbosa", "Janete Clair"], "Manoel Carlos",
   "Maneco escreveu 'Laços de Família' e 'Mulheres Apaixonadas', entre outras.",
   "Memória Globo – Manoel Carlos", syn=["maneco"], br=True)
mc(N, "personagens", 2, 14, "Na novela 'Pantanal', qual personagem tinha fama de virar onça?",
   ["Juma Marruá", "Irma", "Madeleine", "Filó"], "Juma Marruá",
   "Juma foi vivida por Cristiana Oliveira (1990) e por Alanis Guillen (2022).",
   "Memória Globo – Pantanal (2022)", syn=["juma"], br=True)
mc(N, "autores", 3, 16, "Quem escreveu a novela 'O Clone'?",
   ["Glória Perez", "Manoel Carlos", "Gilberto Braga", "Aguinaldo Silva"], "Glória Perez",
   "Glória Perez também escreveu 'Caminho das Índias' e 'A Força do Querer'.",
   "Memória Globo – Glória Perez", br=True)
mc(N, "emissoras", 3, 16, "Em qual emissora foi exibida a primeira versão de 'Pantanal', em 1990?",
   ["Rede Manchete", "TV Globo", "SBT", "TV Tupi"], "Rede Manchete",
   "A novela de Benedito Ruy Barbosa foi um fenômeno da Manchete e ganhou remake na Globo em 2022.",
   "Memória Globo – Pantanal (2022); Teledramaturgia", syn=["manchete"], br=True)
mc(N, "vilãs", 3, 16, "Quem interpretou a vilã Odete Roitman na primeira versão de 'Vale Tudo' (1988)?",
   ["Beatriz Segall", "Fernanda Montenegro", "Regina Duarte", "Glória Menezes"], "Beatriz Segall",
   "O mistério 'Quem matou Odete Roitman?' parou o país em 1989.",
   "Memória Globo – Vale Tudo (1988)", br=True)
mc(N, "clássicas", 3, 16, "Qual novela de 1976, baseada no romance de Bernardo Guimarães, fez sucesso em dezenas de países?",
   ["A Escrava Isaura", "Roque Santeiro", "Dancin' Days", "Gabriela"], "A Escrava Isaura",
   "Estrelada por Lucélia Santos, foi exportada para dezenas de países.",
   "Memória Globo – Escrava Isaura", syn=["escrava isaura", "isaura"], br=True)
mc(N, "personagens", 3, 16, "Em 'Roque Santeiro' (1985), qual era o nome da viúva interpretada por Regina Duarte?",
   ["Porcina", "Tieta", "Odete", "Perpétua"], "Porcina",
   "A Viúva Porcina era 'a que foi sem nunca ter sido'.",
   "Memória Globo – Roque Santeiro", syn=["viuva porcina"], br=True)
mc(N, "vilões", 3, 16, "Em qual novela de Walcyr Carrasco (2013) o vilão Félix, de Mateus Solano, conquistou o público?",
   ["Amor à Vida", "Império", "Fina Estampa", "A Força do Querer"], "Amor à Vida",
   "A novela terminou com o primeiro beijo entre dois homens numa novela da Globo no horário nobre.",
   "Memória Globo – Amor à Vida", br=True)
mc(N, "cenários", 4, 16, "Em que cidade fictícia se passava a novela 'Roque Santeiro'?",
   ["Asa Branca", "Sucupira", "Santana do Agreste", "Bole-Bole"], "Asa Branca",
   "Sucupira é de 'O Bem-Amado', Santana do Agreste de 'Tieta' e Bole-Bole de 'Saramandaia'.",
   "Memória Globo – Roque Santeiro", br=True)

# =========================================================== TELEVISÃO
V = "tv"
mc(V, "infantis", 1, 6, "Qual personagem do 'Sítio do Picapau Amarelo' é uma boneca de pano falante?",
   ["Emília", "Narizinho", "Cuca", "Dona Benta"], "Emília",
   "Emília ganhou a fala depois de tomar uma 'pílula falante'.",
   "Memória Globo – Sítio do Picapau Amarelo", syn=["emilia", "boneca emilia"], br=True)
mc(V, "desenhos", 1, 6, "De que cor é o Bob Esponja?",
   ["Amarelo", "Azul", "Verde", "Rosa"], "Amarelo",
   "Bob Esponja mora num abacaxi no fundo do mar, na Fenda do Biquíni.",
   "Nickelodeon – SpongeBob SquarePants")
mc(V, "desenhos", 1, 6, "No desenho 'Peppa Pig', que animal é a Peppa?",
   ["Porquinha", "Ovelha", "Coelha", "Gata"], "Porquinha",
   "Peppa vive com o Papai Pig, a Mamãe Pig e o irmãozinho George.",
   "Peppa Pig – site oficial", syn=["porca", "porco", "porquinho", "uma porquinha"])
mc(V, "humor", 1, 6, "No seriado 'Chaves', onde o personagem principal costuma se esconder?",
   ["Num barril", "Num armário", "Embaixo da cama", "Numa árvore"], "Num barril",
   "O barril fica no pátio da vila, perto da casa da Dona Florinda.",
   "Televisa – El Chavo del Ocho", syn=["barril", "no barril", "dentro do barril"])
mc(V, "apresentadores", 1, 8, "Qual apresentadora ficou famosa como a 'Rainha dos Baixinhos'?",
   ["Xuxa", "Angélica", "Eliana", "Mara Maravilha"], "Xuxa",
   "O 'Xou da Xuxa' estreou na Globo em 1986.",
   "Memória Globo – Xou da Xuxa", syn=["xuxa meneghel"], br=True)
mc(V, "humor", 2, 9, "No seriado 'Chaves', qual é o nome do professor da turma?",
   ["Professor Girafales", "Seu Madruga", "Seu Barriga", "Nhonho"], "Professor Girafales",
   "Ele é apaixonado pela Dona Florinda e leva sempre um buquê de flores.",
   "Televisa – El Chavo del Ocho", syn=["girafales", "professor linguica"])
mc(V, "humor", 2, 9, "Quem é o dono da vila que vive cobrando o aluguel no seriado 'Chaves'?",
   ["Seu Barriga", "Seu Madruga", "Professor Girafales", "Quico"], "Seu Barriga",
   "Seu Madruga vivia devendo vários meses de aluguel ao Seu Barriga.",
   "Televisa – El Chavo del Ocho", syn=["barriga", "senhor barriga"])
mc(V, "desenhos", 1, 9, "Qual desenho mostra uma família amarela que mora em Springfield?",
   ["Os Simpsons", "Family Guy", "Futurama", "Os Flintstones"], "Os Simpsons",
   "Criado por Matt Groening, estreou como série em 1989.",
   "FOX – The Simpsons", syn=["simpsons"])
mc(V, "infantis", 2, 10, "Em 'Castelo Rá-Tim-Bum', como se chama o aprendiz de feiticeiro de 300 anos?",
   ["Nino", "Zequinha", "Pedro", "Biba"], "Nino",
   "Nino morava no castelo com o tio Victor e a feiticeira Morgana.",
   "TV Cultura – Castelo Rá-Tim-Bum (1994)", br=True)
mc(V, "humor", 1, 10, "Qual grupo de humoristas era formado por Didi, Dedé, Mussum e Zacarias?",
   ["Os Trapalhões", "Casseta & Planeta", "Hermes e Renato", "Porta dos Fundos"], "Os Trapalhões",
   "Os Trapalhões ficaram décadas no ar e fizeram muitos filmes de sucesso.",
   "Memória Globo – Os Trapalhões", syn=["trapalhoes"], br=True)
mc(V, "apresentadores", 1, 10, "Qual apresentador do SBT ficou famoso por perguntar à plateia: 'Quem quer dinheiro?'.",
   ["Silvio Santos", "Faustão", "Gugu", "Chacrinha"], "Silvio Santos",
   "Silvio Santos fundou o SBT em 1981 e jogava aviõezinhos de dinheiro para a plateia.",
   "SBT – Silvio Santos", syn=["silvio"], br=True)
mc(V, "reality shows", 1, 12, "Qual reality show da Globo, no ar desde 2002, confina participantes numa casa vigiada por câmeras?",
   ["Big Brother Brasil", "A Fazenda", "No Limite", "Casa dos Artistas"], "Big Brother Brasil",
   "O BBB é a versão brasileira do formato holandês Big Brother.",
   "Memória Globo – Big Brother Brasil", syn=["bbb", "big brother"], br=True)
mc(V, "emissoras", 2, 12, "Qual emissora pública de São Paulo produziu 'Castelo Rá-Tim-Bum'?",
   ["TV Cultura", "TV Globo", "SBT", "Band"], "TV Cultura",
   "A TV Cultura também produziu 'Rá-Tim-Bum' e 'Cocoricó'.",
   "TV Cultura – Castelo Rá-Tim-Bum", syn=["cultura"], br=True)
mc(V, "programas", 2, 12, "Qual programa dominical da Globo é conhecido como 'o show da vida'?",
   ["Fantástico", "Domingão", "Esporte Espetacular", "Caldeirão"], "Fantástico",
   "O Fantástico está no ar desde 1973.",
   "Memória Globo – Fantástico", br=True)
mc(V, "apresentadores", 2, 12, "Qual apresentador gritava 'Ô loco, meu!' no programa de domingo da Globo?",
   ["Faustão", "Silvio Santos", "Gugu", "Luciano Huck"], "Faustão",
   "Fausto Silva apresentou o 'Domingão do Faustão' de 1989 a 2021.",
   "Memória Globo – Domingão do Faustão", syn=["fausto silva", "fausto"], br=True)
mc(V, "séries", 2, 12, "Qual série americana mostrava seis amigos que frequentavam o café Central Perk?",
   ["Friends", "Seinfeld", "How I Met Your Mother", "The Office"], "Friends",
   "Friends foi ao ar de 1994 a 2004, com dez temporadas.",
   "Warner Bros. Television – Friends")
mc(V, "jornalismo", 2, 14, "Qual telejornal da Globo estreou em 1969 e continua no ar à noite?",
   ["Jornal Nacional", "Fantástico", "Jornal Hoje", "Globo Repórter"], "Jornal Nacional",
   "O Jornal Nacional estreou em 1º de setembro de 1969, apresentado por Cid Moreira.",
   "Memória Globo – Jornal Nacional", syn=["jn"], br=True, ref="Programação de 2026")
mc(V, "humor", 3, 14, "Qual programa de humor da Globo tinha o personagem Caco Antibes, de Miguel Falabella?",
   ["Sai de Baixo", "Zorra Total", "Os Trapalhões", "A Grande Família"], "Sai de Baixo",
   "Sai de Baixo foi exibido de 1996 a 2002, gravado no teatro com plateia.",
   "Memória Globo – Sai de Baixo", br=True)
mc(V, "emissoras", 3, 14, "Qual foi a primeira emissora de televisão do Brasil, inaugurada em 1950?",
   ["TV Tupi", "TV Globo", "TV Record", "TV Excelsior"], "TV Tupi",
   "A TV Tupi de São Paulo foi inaugurada em 18 de setembro de 1950.",
   "Museu da TV; Biblioteca Nacional", syn=["tupi"], br=True)
mc(V, "história da TV", 4, 16, "Qual empresário, dono dos Diários Associados, trouxe a televisão ao Brasil?",
   ["Assis Chateaubriand", "Roberto Marinho", "Silvio Santos", "Adolpho Bloch"], "Assis Chateaubriand",
   "Chatô importou os equipamentos dos Estados Unidos para a primeira transmissão, em 1950.",
   "Biblioteca Nacional – Assis Chateaubriand", syn=["chateaubriand", "chato"], br=True)

# =========================================================== ESPORTES
E = "esp"
mc(E, "futebol", 1, 6, "Qual esporte é jogado com os pés, uma bola e dois gols?",
   ["Futebol", "Basquete", "Natação", "Tênis"], "Futebol",
   "O futebol é o esporte mais popular do Brasil e do mundo.",
   "FIFA – Laws of the Game")
mc(E, "futebol", 1, 6, "Qual jogador brasileiro é conhecido como o 'Rei do Futebol'?",
   ["Pelé", "Ronaldo", "Zico", "Garrincha"], "Pelé",
   "Pelé venceu três Copas do Mundo: 1958, 1962 e 1970.",
   "FIFA – Pelé", syn=["pele", "edson arantes do nascimento"], br=True)
mc(E, "futebol", 1, 6, "Quantos jogadores de cada time ficam em campo numa partida de futebol?",
   ["11", "10", "9", "12"], "11",
   "São 10 jogadores de linha e 1 goleiro em cada time.",
   "IFAB – Regras do Jogo, Regra 3")
tf(E, "futebol", 1, 6, "No futebol, o goleiro pode pegar a bola com as mãos dentro da sua própria grande área.", True,
   "Fora da grande área o goleiro não pode tocar a bola com as mãos.",
   "IFAB – Regras do Jogo, Regra 12")
mc(E, "olimpíadas", 1, 9, "Normalmente, de quantos em quantos anos acontecem os Jogos Olímpicos de Verão?",
   ["4", "2", "5", "3"], "4",
   "Os Jogos de Tóquio foram adiados para 2021 por causa da pandemia, uma exceção.",
   "Comitê Olímpico Internacional")
mc(E, "artes marciais", 1, 9, "Qual luta brasileira mistura dança, música e movimentos de ataque e defesa?",
   ["Capoeira", "Jiu-jítsu", "Judô", "Caratê"], "Capoeira",
   "A roda de capoeira é Patrimônio Cultural Imaterial da Humanidade (UNESCO, 2014).",
   "UNESCO – Capoeira circle (2014)", br=True)
mc(E, "copas", 1, 9, "Até a Copa de 2022, quantas Copas do Mundo de futebol masculino o Brasil havia vencido?",
   ["5", "4", "3", "6"], "5",
   "O Brasil venceu em 1958, 1962, 1970, 1994 e 2002.",
   "FIFA – World Cup history", br=True, ref="Até a Copa do Mundo de 2022")
mc(E, "automobilismo", 1, 10, "Qual piloto brasileiro foi tricampeão mundial de Fórmula 1 e morreu em 1994?",
   ["Ayrton Senna", "Nelson Piquet", "Emerson Fittipaldi", "Rubens Barrichello"], "Ayrton Senna",
   "Senna foi campeão em 1988, 1990 e 1991. Piquet também foi tricampeão.",
   "Instituto Ayrton Senna; FIA", syn=["senna"], br=True)
mc(E, "olimpíadas", 1, 10, "Em que cidade brasileira foram realizados os Jogos Olímpicos de 2016?",
   ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "Rio de Janeiro",
   "Foram os primeiros Jogos Olímpicos realizados na América do Sul.",
   "Comitê Olímpico Internacional – Rio 2016", syn=["rio"], br=True)
mc(E, "copas", 2, 10, "Qual seleção venceu a Copa do Mundo de 2022, no Catar?",
   ["Argentina", "França", "Brasil", "Croácia"], "Argentina",
   "A Argentina venceu a França nos pênaltis, depois de um 3 a 3 na final.",
   "FIFA – Qatar 2022", ref="Copa de 2022")
mc(E, "vôlei", 2, 10, "No vôlei de quadra, quantos jogadores de cada equipe ficam em quadra?",
   ["6", "5", "7", "11"], "6",
   "No vôlei de praia são apenas 2 por equipe.",
   "FIVB – Official Volleyball Rules")
mc(E, "basquete", 2, 10, "No basquete, quantos pontos vale um lance livre convertido?",
   ["1", "2", "3", "4"], "1",
   "Cestas de dentro do garrafão e da área de 2 valem 2 pontos; de trás da linha, 3.",
   "FIBA – Official Basketball Rules")
mc(E, "olimpíadas", 2, 12, "Qual nadador norte-americano é o maior medalhista olímpico da história?",
   ["Michael Phelps", "Mark Spitz", "Ryan Lochte", "Caeleb Dressel"], "Michael Phelps",
   "Phelps ganhou 28 medalhas olímpicas, 23 delas de ouro.",
   "Comitê Olímpico Internacional – Michael Phelps", syn=["phelps"], ref="Até os Jogos de Paris 2024")
mc(E, "atletismo", 2, 12, "Qual atleta jamaicano correu os 100 metros rasos em 9,58 segundos em 2009, estabelecendo o recorde mundial?",
   ["Usain Bolt", "Carl Lewis", "Asafa Powell", "Justin Gatlin"], "Usain Bolt",
   "A marca foi feita no Mundial de Berlim, em 16 de agosto de 2009.",
   "World Athletics – Records", syn=["bolt"], ref="Recorde estabelecido em 2009")
mc(E, "ginástica", 2, 12, "Qual ginasta brasileira ganhou a medalha de ouro no solo nos Jogos de Paris 2024?",
   ["Rebeca Andrade", "Daiane dos Santos", "Flávia Saraiva", "Jade Barbosa"], "Rebeca Andrade",
   "Rebeca superou a americana Simone Biles na final do solo.",
   "Comitê Olímpico do Brasil – Paris 2024", syn=["rebeca"], br=True, ref="Jogos de Paris 2024")
mc(E, "copas", 2, 12, "Em que ano o Brasil sediou uma Copa do Mundo de futebol pela segunda vez?",
   ["2014", "1950", "2010", "2018"], "2014",
   "A primeira Copa no Brasil foi em 1950, com a final no Maracanã.",
   "FIFA – Brazil 2014", br=True)
mc(E, "copas", 2, 12, "Qual foi o placar da derrota do Brasil para a Alemanha na semifinal da Copa de 2014?",
   ["7 a 1", "3 a 0", "2 a 1", "5 a 0"], "7 a 1",
   "O jogo aconteceu no Mineirão, em Belo Horizonte, em 8 de julho de 2014.",
   "FIFA – Brazil 2014, Semi-final", syn=["sete a um", "7 x 1", "7 a um"], br=True)
op(E, "artes marciais", 2, 12, "Em que país surgiu o judô?",
   "Japão", ["japao", "o japao"],
   "O judô foi criado por Jigoro Kano em 1882.",
   "Federação Internacional de Judô – história")
mc(E, "futebol", 3, 12, "No futebol, como se chama o drible em que a bola passa por cima da cabeça do adversário?",
   ["Chapéu", "Caneta", "Elástico", "Pedalada"], "Chapéu",
   "Caneta é quando a bola passa entre as pernas do adversário.",
   "Dicionário Houaiss – verbete 'chapéu' (futebol)", syn=["chapeu", "lencol"], br=True)
mc(E, "tênis", 3, 14, "Em qual esporte o Brasil teve os campeões Gustavo Kuerten e Maria Esther Bueno?",
   ["Tênis", "Vôlei", "Basquete", "Golfe"], "Tênis",
   "Guga foi número 1 do mundo; Maria Esther Bueno venceu Wimbledon em simples três vezes.",
   "ATP Tour; International Tennis Hall of Fame", syn=["tenis"], br=True)
mc(E, "copas", 3, 14, "Qual país sediou a primeira Copa do Mundo de futebol, em 1930?",
   ["Uruguai", "Brasil", "Itália", "França"], "Uruguai",
   "O Uruguai também foi o campeão, vencendo a Argentina na final.",
   "FIFA – Uruguay 1930")
mc(E, "copas", 3, 12, "Em que ano o Brasil ganhou sua primeira Copa do Mundo?",
   ["1958", "1950", "1962", "1970"], "1958",
   "Na Suécia, o Brasil de Pelé e Garrincha venceu a anfitriã por 5 a 2 na final.",
   "FIFA – Sweden 1958", br=True)
mc(E, "copas", 4, 14, "Quem era o técnico da seleção brasileira no título da Copa de 1970?",
   ["Zagallo", "Telê Santana", "Feola", "Parreira"], "Zagallo",
   "Mário Jorge Lobo Zagallo foi campeão como jogador (1958 e 1962) e como técnico (1970).",
   "CBF – Seleção Brasileira; FIFA – Mexico 1970", syn=["mario zagallo", "zagalo"], br=True)

# =========================================================== MARCAS E SLOGANS
M = "mar"
mc(M, "lanchonetes", 1, 6, "Qual rede de lanchonetes tem um palhaço chamado Ronald como mascote?",
   ["McDonald's", "Burger King", "Subway", "Bob's"], "McDonald's",
   "Ronald McDonald é o mascote da rede desde os anos 1960.",
   "McDonald's – história", syn=["mcdonalds", "mc donalds", "mequi"])
mc(M, "brinquedos", 1, 6, "Qual marca dinamarquesa de brinquedos é famosa pelos bloquinhos de montar?",
   ["LEGO", "Estrela", "Hasbro", "Mattel"], "LEGO",
   "O nome vem do dinamarquês 'leg godt', que significa 'brinque bem'.",
   "LEGO Group – Company history")
mc(M, "logotipos", 1, 6, "Qual marca tem uma maçã mordida como logotipo?",
   ["Apple", "Samsung", "Motorola", "Positivo"], "Apple",
   "Apple significa 'maçã' em inglês.",
   "Apple – identidade visual")
mc(M, "logotipos", 1, 6, "Qual cor predomina no logotipo da Coca-Cola?",
   ["Vermelho", "Azul", "Verde", "Amarelo"], "Vermelho",
   "A Coca-Cola usa letras brancas em fundo vermelho.",
   "The Coca-Cola Company – história da marca")
mc(M, "lanchonetes", 1, 8, "Qual rede de fast-food tem um rei como mascote?",
   ["Burger King", "McDonald's", "KFC", "Subway"], "Burger King",
   "O Burger King surgiu nos Estados Unidos nos anos 1950.",
   "Burger King – história")
op(M, "carros", 1, 10, "Qual montadora fabricava o Fusca, um dos carros mais famosos do Brasil?",
   "Volkswagen", ["vw", "volks", "volkswagen do brasil", "fusca volkswagen"],
   "O Fusca foi fabricado no Brasil de 1959 a 1986 e de 1993 a 1996.",
   "Volkswagen do Brasil – história do Fusca", br=True)
mc(M, "logotipos", 1, 10, "Qual marca esportiva tem um logotipo com três listras?",
   ["Adidas", "Nike", "Puma", "Mizuno"], "Adidas",
   "A Adidas foi fundada por Adolf Dassler, na Alemanha.",
   "Adidas Group – história")
mc(M, "videogames", 2, 10, "Qual empresa fabrica o videogame Switch?",
   ["Nintendo", "Sony", "Microsoft", "Sega"], "Nintendo",
   "O Nintendo Switch foi lançado em 2017 e pode ser jogado na TV ou na mão.",
   "Nintendo – Switch")
mc(M, "slogans", 1, 12, "Qual marca de artigos esportivos usa o slogan 'Just do it'?",
   ["Nike", "Adidas", "Puma", "Olympikus"], "Nike",
   "O slogan foi criado em 1988 pela agência Wieden+Kennedy.",
   "Nike – história da marca")
mc(M, "slogans", 2, 12, "Qual refrigerante usou no Brasil o slogan 'Abra a felicidade'?",
   ["Coca-Cola", "Pepsi", "Guaraná Antarctica", "Fanta"], "Coca-Cola",
   "A campanha global 'Open Happiness' começou em 2009.",
   "The Coca-Cola Company – campanhas", syn=["coca", "coca cola"])
mc(M, "slogans", 2, 12, "Qual marca brasileira de sandálias usa o slogan 'Todo mundo usa'?",
   ["Havaianas", "Ipanema", "Rider", "Melissa"], "Havaianas",
   "As Havaianas foram lançadas em 1962 e hoje são vendidas no mundo todo.",
   "Havaianas – história", br=True)
mc(M, "logotipos", 2, 12, "Qual empresa de tecnologia tem um logotipo com quatro quadradinhos coloridos?",
   ["Microsoft", "Google", "Apple", "Samsung"], "Microsoft",
   "Os quadrados são vermelho, verde, azul e amarelo.",
   "Microsoft – identidade visual")
mc(M, "empresas", 2, 12, "O achocolatado Nescau pertence a qual empresa?",
   ["Nestlé", "Unilever", "Kraft", "Danone"], "Nestlé",
   "O Nescau é uma marca da Nestlé vendida no Brasil desde os anos 1930.",
   "Nestlé Brasil – marcas", syn=["nestle"], br=True)
mc(M, "slogans", 2, 14, "Qual marca de esponja de aço ficou famosa pelo slogan '1001 utilidades'?",
   ["Bombril", "Assolan", "Ypê", "Scotch-Brite"], "Bombril",
   "O garoto-propaganda Carlos Moreno fez comerciais da Bombril por décadas.",
   "Bombril – história", br=True)
mc(M, "brinquedos", 2, 14, "Qual fabricante brasileira de brinquedos lançou o jogo 'Banco Imobiliário'?",
   ["Estrela", "Grow", "Mattel", "Hasbro"], "Estrela",
   "A Estrela lança o Banco Imobiliário desde 1944.",
   "Estrela – história", br=True)
mc(M, "slogans", 2, 14, "Qual bebida energética usa o slogan 'te dá asas'?",
   ["Red Bull", "Monster", "TNT", "Burn"], "Red Bull",
   "A Red Bull é austríaca e foi inspirada numa bebida tailandesa.",
   "Red Bull – company")
mc(M, "logotipos", 3, 14, "Qual marca de tênis tem uma estrela no logotipo do modelo 'All Star'?",
   ["Converse", "Vans", "Nike", "Reebok"], "Converse",
   "O Chuck Taylor All Star foi lançado como tênis de basquete no começo do século XX.",
   "Converse – história")
mc(M, "slogans", 3, 14, "Qual marca de sabão em pó usa o slogan 'Se sujar faz bem'?",
   ["Omo", "Ariel", "Tixan", "Brilhante"], "Omo",
   "A campanha 'Dirt is Good' (sujar faz bem) é usada pela marca em vários países.",
   "Unilever – Omo", br=True)
mc(M, "origem", 3, 14, "O guaraná, usado no Guaraná Antarctica, é um fruto originário de qual região brasileira?",
   ["Amazônia", "Pampa", "Caatinga", "Pantanal"], "Amazônia",
   "O guaraná é nativo da Amazônia e foi domesticado pelos indígenas Sateré-Mawé.",
   "Embrapa – Guaraná", syn=["amazonia", "norte"], br=True)
mc(M, "slogans", 4, 16, "Qual iogurte infantil ficou famoso nos anos 1980 com o slogan 'Vale por um bifinho'?",
   ["Danoninho", "Chamyto", "Activia", "Yakult"], "Danoninho",
   "A campanha marcou época na publicidade brasileira e é lembrada até hoje.",
   "Danone Brasil – história do Danoninho", br=True)

# ---- perguntas infantis adicionais (6+)
mc(V, "desenhos", 1, 6, "No desenho 'Patrulha Canina', que animais são os heróis?",
   ["Cachorros", "Gatos", "Coelhos", "Pássaros"], "Cachorros",
   "Os filhotes de cachorro são liderados pelo menino Ryder.",
   "Nickelodeon – Patrulha Canina", syn=["caes", "cachorrinhos", "filhotes", "cachorro"])
mc(E, "natação", 1, 6, "Em qual esporte os atletas competem dentro de uma piscina?",
   ["Natação", "Futebol", "Ciclismo", "Corrida"], "Natação",
   "Na natação há quatro estilos: crawl, costas, peito e borboleta.",
   "World Aquatics – Swimming rules", syn=["natacao", "nadar"])
mc(M, "brinquedos", 1, 6, "Qual destas marcas é de bonecas?",
   ["Barbie", "Nescau", "Havaianas", "Omo"], "Barbie",
   "A Barbie foi lançada pela Mattel em 1959.",
   "Mattel – Barbie")
