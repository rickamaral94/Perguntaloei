# Perguntas novas (parte 6c). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== CINEMA
C = "cin"
mc(C, "clássicos", 1, 8, "Qual gorila gigante dos filmes sobe no alto do Empire State, em Nova York?",
   ["King Kong", "Godzilla", "Shrek", "Hulk"], "King Kong",
   "O primeiro filme de King Kong é de 1933 e virou um clássico do cinema.",
   "IMDb – King Kong (1933)", syn=["king kong", "kong"])
mc(C, "sagas", 1, 10, "Nos filmes de Harry Potter, quem é o diretor de Hogwarts na maior parte da saga?",
   ["Dumbledore", "Snape", "Hagrid", "Voldemort"], "Dumbledore",
   "Na tradução brasileira, o nome completo dele é Alvo Dumbledore.",
   "Warner Bros. – Harry Potter e a Pedra Filosofal (2001)", syn=["alvo dumbledore", "dumbledore"])
tf(C, "super-heróis", 1, 8, "Nos filmes da Marvel, Thor é o deus do trovão.", True,
   "Thor usa um martelo mágico chamado Mjölnir.", "Marvel Studios – Thor (2011)")
mc(C, "sagas", 1, 8, "Em 'Star Wars', qual é o nome do pequeno mestre jedi verde e de orelhas pontudas?",
   ["Yoda", "Chewbacca", "R2-D2", "Obi-Wan"], "Yoda",
   "Yoda fala com a ordem das palavras invertida, um de seus traços mais famosos.",
   "Lucasfilm – O Império Contra-Ataca (1980)")
tf(C, "super-heróis", 1, 8, "O Coringa é o maior inimigo do Superman.", False,
   "O Coringa é o arqui-inimigo do Batman; o grande rival do Superman é Lex Luthor.",
   "DC Comics")
op(C, "sagas", 1, 9, "Em 'Star Wars', qual é o nome do robô dourado que fala milhões de línguas?", "C-3PO",
   ["c-3po", "c3po", "c 3po", "c3 po"],
   "C-3PO costuma andar ao lado do pequeno robô R2-D2.", "Lucasfilm – Star Wars (1977)")
mc(C, "atores", 2, 12, "Qual ator interpretou Forrest Gump no filme de 1994?",
   ["Tom Hanks", "Tom Cruise", "Brad Pitt", "Leonardo DiCaprio"], "Tom Hanks",
   "Tom Hanks ganhou o Oscar de Melhor Ator por esse papel.", "IMDb – Forrest Gump (1994)")
mc(C, "Oscar", 2, 12, "Por qual filme Leonardo DiCaprio ganhou o Oscar de Melhor Ator?",
   ["O Regresso", "Titanic", "O Lobo de Wall Street", "A Origem"], "O Regresso",
   "Ele venceu em 2016, depois de várias indicações sem vitória.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2016")
mc(C, "clássicos", 2, 14, "Em 'O Poderoso Chefão', qual é o sobrenome da família mafiosa?",
   ["Corleone", "Soprano", "Gambino", "Montana"], "Corleone",
   "Marlon Brando interpretou o patriarca Vito Corleone.", "IMDb – O Poderoso Chefão (1972)")
tf(C, "sagas", 2, 12, "O primeiro filme de Harry Potter chegou aos cinemas em 2001.", True,
   "'Harry Potter e a Pedra Filosofal' estreou em novembro de 2001.",
   "Warner Bros. – Harry Potter e a Pedra Filosofal (2001)")
mc(C, "atores", 2, 12, "Qual ator interpretou o agente 007 em 'Cassino Royale', de 2006?",
   ["Daniel Craig", "Pierce Brosnan", "Sean Connery", "Roger Moore"], "Daniel Craig",
   "Daniel Craig viveu James Bond em cinco filmes, de 2006 a 2021.", "IMDb – Cassino Royale (2006)")
op(C, "super-heróis", 2, 12, "Qual é o nome do mordomo de Bruce Wayne, o Batman?", "Alfred",
   ["alfred", "alfred pennyworth"],
   "O sobrenome completo do mordomo é Pennyworth.", "DC Comics")
tf(C, "cinema brasileiro", 2, 12, "Fernanda Torres ganhou o Globo de Ouro de Melhor Atriz por 'Ainda Estou Aqui'.", True,
   "Ela venceu em janeiro de 2025, na categoria de filme dramático.",
   "Globo de Ouro 2025", br=True)
mc(C, "Oscar", 3, 14, "Qual filme de 2003 ganhou 11 Oscars, igualando o recorde de 'Titanic' e 'Ben-Hur'?",
   ["O Senhor dos Anéis: O Retorno do Rei", "Avatar", "O Poderoso Chefão", "Forrest Gump"],
   "O Senhor dos Anéis: O Retorno do Rei",
   "Ele venceu em todas as 11 categorias em que foi indicado.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2004",
   syn=["o retorno do rei", "senhor dos aneis"])
tf(C, "cinema brasileiro", 3, 14, "O filme 'Cidade de Deus' recebeu quatro indicações ao Oscar.", True,
   "Foi indicado a direção, roteiro adaptado, fotografia e montagem, no Oscar de 2004.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2004", br=True)
mc(C, "diretores", 3, 16, "Quem dirigiu o suspense 'Psicose', de 1960?",
   ["Alfred Hitchcock", "Stanley Kubrick", "Orson Welles", "Billy Wilder"], "Alfred Hitchcock",
   "Hitchcock ficou conhecido como o 'mestre do suspense'.", "IMDb – Psicose (1960)",
   syn=["hitchcock"])
mc(C, "Oscar", 4, 16, "Qual filme venceu o primeiro Oscar de Melhor Filme, na cerimônia de 1929?",
   ["Asas", "Casablanca", "...E o Vento Levou", "Cantando na Chuva"], "Asas",
   "'Asas' é um filme mudo sobre pilotos da Primeira Guerra Mundial.",
   "Academia de Artes e Ciências Cinematográficas – 1º Oscar (1929)")
mc(C, "cinema brasileiro", 4, 16, "Qual filme brasileiro de Anselmo Duarte ganhou a Palma de Ouro em Cannes, em 1962?",
   ["O Pagador de Promessas", "Vidas Secas", "Rio 40 Graus", "Macunaíma"], "O Pagador de Promessas",
   "Até hoje é o único filme brasileiro a vencer a Palma de Ouro.",
   "Festival de Cannes – 1962", br=True)

# =========================================================== FILMES INFANTIS
I = "inf"
mc(I, "clássicos", 1, 6, "Quantos anões vivem com a Branca de Neve?",
   ["Sete", "Cinco", "Três", "Dez"], "Sete",
   "Os anões trabalham numa mina de pedras preciosas.",
   "Disney – Branca de Neve e os Sete Anões (1937)", syn=["7", "sete"])
mc(I, "clássicos", 1, 6, "O que acontece com o nariz do Pinóquio quando ele mente?",
   ["Cresce", "Fica vermelho", "Encolhe", "Some"], "Cresce",
   "Pinóquio é um boneco de madeira que sonha em virar um menino de verdade.",
   "Disney – Pinóquio (1940)")
mc(I, "Pixar", 1, 6, "Em 'Toy Story', como se chama o menino dono do Woody e do Buzz?",
   ["Andy", "Sid", "Max", "Lucas"], "Andy",
   "O nome do Andy aparece escrito na sola da bota do Woody.", "Disney/Pixar – Toy Story (1995)")
tf(I, "Disney", 1, 6, "Em 'Frozen', a Elsa tem poderes de fogo.", False,
   "Os poderes da Elsa são de gelo e neve.", "Disney – Frozen: Uma Aventura Congelante (2013)")
mc(I, "Pixar", 1, 6, "Em 'Procurando Nemo', qual peixinha azul tem memória muito curta?",
   ["Dory", "Marlin", "Bruce", "Gill"], "Dory",
   "A Dory ganhou seu próprio filme, 'Procurando Dory', em 2016.",
   "Disney/Pixar – Procurando Nemo (2003)")
mc(I, "Disney", 1, 7, "Em 'Zootopia', que animal é a policial Judy Hopps?",
   ["Coelha", "Raposa", "Gata", "Ovelha"], "Coelha",
   "Judy é a primeira coelha a entrar para a polícia de Zootopia.",
   "Disney – Zootopia: Essa Cidade é o Bicho (2016)")
mc(I, "Disney", 1, 7, "Em 'Aladdin', quantos desejos o Gênio da lâmpada concede?",
   ["Três", "Um", "Cinco", "Sete"], "Três",
   "Aladdin usa seu último desejo para libertar o Gênio.", "Disney – Aladdin (1992)",
   syn=["3", "tres"])
op(I, "Pixar", 1, 7, "Em 'Carros', qual é o nome do guincho enferrujado, melhor amigo do Relâmpago McQueen?", "Mate",
   ["mate", "tom mate"],
   "Mate mora na pequena cidade de Radiator Springs.", "Disney/Pixar – Carros (2006)")
mc(I, "Disney", 2, 8, "Em 'O Rei Leão', qual é o nome do tio malvado de Simba?",
   ["Scar", "Mufasa", "Rafiki", "Zazu"], "Scar",
   "Scar tem uma cicatriz no olho, e 'scar' quer dizer cicatriz em inglês.", "Disney – O Rei Leão (1994)")
mc(I, "Pixar", 2, 8, "Em 'Divertida Mente', qual emoção é representada por uma personagem azul e de óculos?",
   ["Tristeza", "Raiva", "Medo", "Nojinho"], "Tristeza",
   "No fim do filme, a Tristeza se revela muito importante para a menina Riley.",
   "Disney/Pixar – Divertida Mente (2015)")
op(I, "Disney", 2, 8, "Qual princesa da Disney cai num sono profundo depois de espetar o dedo num fuso?", "Aurora",
   ["aurora", "bela adormecida", "a bela adormecida"],
   "A maldição da Aurora foi lançada pela fada Malévola.", "Disney – A Bela Adormecida (1959)")
mc(I, "Disney", 2, 9, "Em 'Enrolados', qual é o bichinho de estimação da Rapunzel?",
   ["Um camaleão", "Um gato", "Um sapo", "Um passarinho"], "Um camaleão",
   "O camaleão se chama Pascal e muda de cor conforme o humor.", "Disney – Enrolados (2010)",
   syn=["camaleão", "camaleao"])
mc(I, "Disney", 2, 9, "Em 'Mulan', qual é o nome do pequeno dragão vermelho que acompanha a heroína?",
   ["Mushu", "Shang", "Cri-Kee", "Khan"], "Mushu",
   "Cri-Kee é o grilo da sorte e Khan é o cavalo da Mulan.", "Disney – Mulan (1998)")
mc(I, "estúdios", 2, 10, "Qual estúdio produziu o filme 'Shrek'?",
   ["DreamWorks", "Pixar", "Disney", "Illumination"], "DreamWorks",
   "A DreamWorks também fez 'Madagascar' e 'Kung Fu Panda'.", "DreamWorks Animation – Shrek (2001)")
mc(I, "animação brasileira", 2, 9, "Em 'Rio', de 2011, de que espécie é a ave Blu?",
   ["Ararinha-azul", "Arara-vermelha", "Tucano", "Papagaio"], "Ararinha-azul",
   "A ararinha-azul é uma ave brasileira que chegou a ser considerada extinta na natureza.",
   "Blue Sky Studios – Rio (2011)", br=True)
tf(I, "Oscar", 3, 12, "'Shrek' ganhou o primeiro Oscar de Melhor Filme de Animação da história.", True,
   "A categoria foi criada no Oscar de 2002, e Shrek venceu 'Monstros S.A.'.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2002")
tf(I, "animação brasileira", 3, 12, "O filme de animação 'Rio' foi dirigido pelo brasileiro Carlos Saldanha.", True,
   "Carlos Saldanha também dirigiu filmes da série 'A Era do Gelo'.",
   "Blue Sky Studios – Rio (2011)", br=True)
mc(I, "estúdios", 3, 12, "Qual estúdio japonês fez o filme 'Meu Amigo Totoro'?",
   ["Studio Ghibli", "Pixar", "DreamWorks", "Illumination"], "Studio Ghibli",
   "O Totoro virou o símbolo do Studio Ghibli.", "Studio Ghibli – Meu Amigo Totoro (1988)",
   syn=["ghibli", "estúdio ghibli"])
mc(I, "Oscar", 4, 14, "Qual foi o primeiro filme da Pixar a ganhar o Oscar de Melhor Filme de Animação?",
   ["Procurando Nemo", "Toy Story", "Monstros S.A.", "Os Incríveis"], "Procurando Nemo",
   "Ele venceu no Oscar de 2004; 'Monstros S.A.' tinha perdido para 'Shrek' em 2002.",
   "Academia de Artes e Ciências Cinematográficas – Oscar 2004")

# =========================================================== MÚSICA
M = "mus"
mc(M, "instrumentos", 1, 7, "Qual instrumento tem fole e é a alma do forró?",
   ["Sanfona", "Violino", "Trompete", "Piano"], "Sanfona",
   "A sanfona também é chamada de acordeão ou gaita, dependendo da região.",
   "Enciclopédia da Música Brasileira", syn=["acordeão", "acordeon", "sanfona"], br=True)
tf(M, "instrumentos", 1, 7, "O violino é um instrumento de sopro.", False,
   "O violino é um instrumento de cordas, tocado com um arco.", "Enciclopédia Britannica – verbete 'Violin'")
mc(M, "instrumentos", 1, 8, "Qual instrumento de sopro dourado, com chaves, é muito usado no jazz?",
   ["Saxofone", "Violão", "Bateria", "Piano"], "Saxofone",
   "O saxofone foi inventado pelo belga Adolphe Sax, por volta de 1840.",
   "Enciclopédia Britannica – verbete 'Saxophone'", syn=["sax"])
tf(M, "bandas", 1, 12, "Freddie Mercury era o vocalista da banda Queen.", True,
   "Freddie Mercury nasceu em Zanzibar, na África, em 1946.", "Enciclopédia Britannica – verbete 'Queen'")
mc(M, "instrumentos", 2, 10, "Qual instrumento de sopro tem uma vara que o músico desliza para mudar as notas?",
   ["Trombone", "Trompete", "Clarinete", "Flauta"], "Trombone",
   "A vara do trombone muda o comprimento do tubo e, assim, o som.",
   "Enciclopédia Britannica – verbete 'Trombone'")
op(M, "instrumentos", 2, 10, "Qual pequeno instrumento de quatro cordas é essencial no samba e no choro?", "Cavaquinho",
   ["cavaquinho", "cavaco"],
   "O cavaquinho chegou ao Brasil trazido pelos portugueses.", "Enciclopédia da Música Brasileira", br=True)
op(M, "teoria", 2, 10, "Como se chama um grupo musical formado por quatro músicos?", "Quarteto",
   ["quarteto"],
   "Grupos de três são trios e de cinco são quintetos.", "Dicionário Grove de Música")
mc(M, "instrumentos", 2, 12, "Quantas teclas tem um piano moderno padrão?",
   ["88", "76", "100", "64"], "88",
   "São 52 teclas brancas e 36 pretas.", "Enciclopédia Britannica – verbete 'Piano'",
   syn=["oitenta e oito"])
mc(M, "música brasileira", 2, 12, "Qual cantora baiana foi vocalista da Banda Eva antes de seguir carreira solo?",
   ["Ivete Sangalo", "Claudia Leitte", "Daniela Mercury", "Margareth Menezes"], "Ivete Sangalo",
   "Ivete deixou a Banda Eva em 1999 para seguir carreira solo.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["ivete"], br=True)
mc(M, "música brasileira", 2, 12, "Qual banda brasileira gravou 'Pelados em Santos'?",
   ["Mamonas Assassinas", "Titãs", "Raimundos", "Paralamas do Sucesso"], "Mamonas Assassinas",
   "O único álbum dos Mamonas, de 1995, vendeu milhões de cópias.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["mamonas"], br=True)
tf(M, "música brasileira", 2, 14, "Caetano Veloso e Gilberto Gil foram líderes do movimento Tropicália.", True,
   "A Tropicália surgiu no fim dos anos 1960, misturando rock, MPB e cultura popular.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(M, "música clássica", 3, 14, "Qual compositor italiano escreveu 'As Quatro Estações'?",
   ["Antonio Vivaldi", "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Frédéric Chopin"], "Antonio Vivaldi",
   "Vivaldi era padre e ficou conhecido como 'o padre ruivo'.",
   "Enciclopédia Britannica – verbete 'Antonio Vivaldi'", syn=["vivaldi"])
mc(M, "música clássica", 3, 14, "Qual compositor polonês ficou famoso por suas peças para piano, como os noturnos?",
   ["Frédéric Chopin", "Antonio Vivaldi", "Johann Sebastian Bach", "Richard Wagner"], "Frédéric Chopin",
   "Chopin nasceu perto de Varsóvia em 1810 e viveu boa parte da vida em Paris.",
   "Enciclopédia Britannica – verbete 'Frédéric Chopin'", syn=["chopin"])
mc(M, "música brasileira", 3, 14, "Qual compositora brasileira criou a marchinha de Carnaval 'Ó Abre Alas', em 1899?",
   ["Chiquinha Gonzaga", "Carmen Miranda", "Dolores Duran", "Dona Ivone Lara"], "Chiquinha Gonzaga",
   "'Ó Abre Alas' é considerada a primeira marchinha de Carnaval.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(M, "música brasileira", 3, 16, "Qual cantor e compositor lançou a canção 'Construção', em 1971?",
   ["Chico Buarque", "Caetano Veloso", "Milton Nascimento", "Gilberto Gil"], "Chico Buarque",
   "Na parte principal de 'Construção', todos os versos terminam com palavras proparoxítonas.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(M, "música brasileira", 4, 14, "Quem compôs a música do Hino Nacional Brasileiro?",
   ["Francisco Manuel da Silva", "Carlos Gomes", "Heitor Villa-Lobos", "Chiquinha Gonzaga"],
   "Francisco Manuel da Silva",
   "A letra atual do hino, de Osório Duque-Estrada, foi oficializada em 1922.",
   "Presidência da República – Símbolos Nacionais", br=True)
mc(M, "música clássica", 4, 16, "Qual compositor brasileiro escreveu a ópera 'O Guarani', estreada em Milão em 1870?",
   ["Carlos Gomes", "Heitor Villa-Lobos", "Ernesto Nazareth", "Pixinguinha"], "Carlos Gomes",
   "A ópera é baseada no romance de José de Alencar.",
   "Enciclopédia Britannica – verbete 'Antônio Carlos Gomes'", br=True)
tf(M, "música clássica", 4, 16, "A ópera 'Carmen' foi composta pelo francês Georges Bizet.", True,
   "Bizet morreu em 1875, poucos meses depois da estreia de 'Carmen'.",
   "Enciclopédia Britannica – verbete 'Carmen'")

# =========================================================== ESPORTES
E = "esp"
mc(E, "futebol", 1, 7, "No futebol, que cor de cartão o juiz mostra para expulsar um jogador?",
   ["Vermelho", "Amarelo", "Verde", "Azul"], "Vermelho",
   "Dois cartões amarelos no mesmo jogo também resultam em cartão vermelho.", "IFAB – Regras do Jogo")
mc(E, "esportes", 1, 7, "Em qual esporte se usa um taco para acertar a bolinha num buraco na grama?",
   ["Golfe", "Beisebol", "Hóquei", "Críquete"], "Golfe",
   "O golfe moderno surgiu na Escócia.", "Enciclopédia Britannica – verbete 'Golf'")
mc(E, "lutas", 1, 7, "Em qual destes esportes os atletas usam quimono e faixas coloridas?",
   ["Judô", "Natação", "Futebol", "Tênis"], "Judô",
   "A cor da faixa mostra o nível do judoca; a preta é das mais altas.",
   "Confederação Brasileira de Judô")
tf(E, "vôlei", 1, 8, "No vôlei, o jogador pode segurar a bola com as duas mãos antes de passá-la.", False,
   "No vôlei a bola deve ser tocada, e não segurada ou conduzida.", "FIVB – Regras Oficiais de Voleibol")
mc(E, "futebol", 1, 8, "Quantos minutos dura cada tempo de uma partida oficial de futebol?",
   ["45", "30", "40", "60"], "45",
   "Os acréscimos repõem o tempo perdido com paradas.", "IFAB – Regras do Jogo",
   syn=["quarenta e cinco"])
mc(E, "futebol", 2, 10, "Qual clube de futebol paulista tem o apelido de 'Timão'?",
   ["Corinthians", "Palmeiras", "São Paulo", "Santos"], "Corinthians",
   "O Corinthians foi fundado em 1910 por operários do bairro do Bom Retiro.",
   "Sport Club Corinthians Paulista", br=True)
op(E, "futebol", 2, 12, "Qual estádio do Rio de Janeiro recebeu o jogo decisivo da Copa de 1950 e a final da Copa de 2014?", "Maracanã",
   ["maracanã", "maracana", "estádio do maracanã"],
   "O nome oficial do Maracanã é Estádio Jornalista Mário Filho.", "FIFA", br=True)
mc(E, "Copa do Mundo", 2, 12, "Qual brasileiro foi o artilheiro da Copa do Mundo de 2002, com oito gols?",
   ["Ronaldo", "Rivaldo", "Ronaldinho", "Romário"], "Ronaldo",
   "Ronaldo marcou os dois gols da final contra a Alemanha.", "FIFA – Copa do Mundo de 2002",
   syn=["ronaldo fenômeno"], br=True)
mc(E, "Copa do Mundo", 2, 14, "Quem era o técnico da seleção brasileira no pentacampeonato, em 2002?",
   ["Luiz Felipe Scolari", "Carlos Alberto Parreira", "Tite", "Vanderlei Luxemburgo"], "Luiz Felipe Scolari",
   "Ele era conhecido pelo apelido de Felipão.", "CBF", syn=["felipão", "felipao", "scolari"], br=True)
tf(E, "Copa do Mundo", 2, 14, "Romário foi eleito o melhor jogador da Copa do Mundo de 1994.", True,
   "Romário fez cinco gols no torneio vencido pelo Brasil nos Estados Unidos.",
   "FIFA – Copa do Mundo de 1994", br=True)
tf(E, "Olimpíadas", 2, 12, "A seleção brasileira masculina de futebol já ganhou medalha de ouro olímpica.", True,
   "O Brasil foi campeão olímpico no Rio 2016 e em Tóquio 2020.", "Comitê Olímpico do Brasil", br=True)
mc(E, "golfe", 3, 12, "Quantos buracos tem um percurso completo de golfe?",
   ["18", "9", "12", "24"], "18",
   "O padrão de 18 buracos vem do tradicional campo de St Andrews, na Escócia.",
   "Enciclopédia Britannica – verbete 'Golf'", syn=["dezoito"])
mc(E, "Olimpíadas", 3, 14, "Em qual esporte coletivo o Brasil ganhou o ouro olímpico masculino em 1992 e 2004?",
   ["Vôlei", "Basquete", "Handebol", "Futebol"], "Vôlei",
   "O primeiro ouro foi em Barcelona e o segundo em Atenas; o terceiro veio no Rio, em 2016.", "Comitê Olímpico do Brasil",
   syn=["voleibol", "volei"], br=True)
mc(E, "Olimpíadas", 3, 14, "Qual brasileira ganhou o ouro no salto em distância nos Jogos de Pequim, em 2008?",
   ["Maurren Maggi", "Daiane dos Santos", "Fabiana Murer", "Rebeca Andrade"], "Maurren Maggi",
   "Foi o primeiro ouro olímpico individual de uma mulher brasileira.",
   "Comitê Olímpico do Brasil", br=True)
mc(E, "Olimpíadas", 3, 14, "Qual brasileiro ganhou o ouro no salto com vara nos Jogos do Rio, em 2016?",
   ["Thiago Braz", "Arthur Zanetti", "Isaquias Queiroz", "Robson Conceição"], "Thiago Braz",
   "Ele saltou 6,03 metros, recorde olímpico na época.", "Comitê Olímpico do Brasil", br=True)
mc(E, "Olimpíadas", 4, 16, "Qual atleta brasileiro foi bicampeão olímpico do salto triplo, em 1952 e 1956?",
   ["Adhemar Ferreira da Silva", "João do Pulo", "Nelson Prudêncio", "Joaquim Cruz"], "Adhemar Ferreira da Silva",
   "Foi o primeiro brasileiro a ganhar duas medalhas de ouro olímpicas.",
   "Comitê Olímpico do Brasil", syn=["adhemar"], br=True)
tf(E, "Olimpíadas", 4, 16, "A primeira medalha de ouro olímpica do Brasil veio no tiro esportivo, em 1920.", True,
   "Guilherme Paraense venceu na pistola, nos Jogos de Antuérpia.", "Comitê Olímpico do Brasil", br=True)

# =========================================================== MARCAS
B = "mar"
mc(B, "brinquedos", 1, 6, "Que tipo de brinquedo a marca Hot Wheels fabrica?",
   ["Carrinhos", "Bonecas", "Bolas", "Pipas"], "Carrinhos",
   "A Hot Wheels foi lançada pela Mattel em 1968.", "Mattel – Hot Wheels")
mc(B, "games", 1, 8, "Qual empresa criou o Mario, o encanador de bigode dos videogames?",
   ["Nintendo", "Sony", "Sega", "Microsoft"], "Nintendo",
   "Mario apareceu pela primeira vez no jogo 'Donkey Kong', de 1981.", "Nintendo")
mc(B, "games", 1, 8, "Qual empresa fabrica o videogame PlayStation?",
   ["Sony", "Nintendo", "Microsoft", "Sega"], "Sony",
   "O primeiro PlayStation foi lançado no Japão em 1994.", "Sony Interactive Entertainment")
mc(B, "alimentos", 1, 8, "Qual biscoito tem duas bolachas pretas de chocolate com recheio branco?",
   ["Oreo", "Passatempo", "Trakinas", "Maizena"], "Oreo",
   "O Oreo foi lançado nos Estados Unidos em 1912.", "Mondelēz International – Oreo")
tf(B, "tecnologia", 1, 10, "O Google começou como uma ferramenta de busca na internet.", True,
   "O Google foi fundado em 1998 por Larry Page e Sergey Brin.", "Google – Nossa história")
op(B, "tecnologia", 1, 10, "Qual empresa fabrica o celular iPhone?", "Apple",
   ["apple"],
   "O primeiro iPhone foi apresentado por Steve Jobs em 2007.", "Apple")
mc(B, "games", 2, 10, "Qual empresa de videogames criou o Sonic, o ouriço azul?",
   ["Sega", "Nintendo", "Sony", "Atari"], "Sega",
   "Sonic estreou em 1991 e virou o mascote da Sega.", "Sega")
mc(B, "carros", 2, 12, "Qual marca de carros tem uma estrela de três pontas no logotipo?",
   ["Mercedes-Benz", "BMW", "Audi", "Volvo"], "Mercedes-Benz",
   "As três pontas representam terra, mar e ar.", "Mercedes-Benz", syn=["mercedes"])
mc(B, "carros", 2, 12, "Qual montadora japonesa tem três elipses no logotipo?",
   ["Toyota", "Honda", "Nissan", "Mitsubishi"], "Toyota",
   "A Toyota é uma das maiores fabricantes de carros do mundo.", "Toyota")
mc(B, "mascotes", 2, 12, "Qual marca de pneus tem como mascote um boneco branco feito de pneus?",
   ["Michelin", "Pirelli", "Goodyear", "Bridgestone"], "Michelin",
   "O boneco se chama Bibendum e foi criado em 1898.", "Michelin")
tf(B, "empresas brasileiras", 2, 12, "A Embraer é uma fabricante brasileira de aviões.", True,
   "A Embraer foi criada em 1969, em São José dos Campos (SP).", "Embraer", br=True)
mc(B, "bebidas", 3, 14, "Qual refrigerante foi criado por um farmacêutico em Atlanta, nos Estados Unidos, em 1886?",
   ["Coca-Cola", "Pepsi", "Fanta", "Sprite"], "Coca-Cola",
   "O criador da Coca-Cola foi o farmacêutico John Pemberton.", "The Coca-Cola Company")
mc(B, "bebidas", 3, 14, "O Guaraná Jesus, refrigerante cor-de-rosa, é tradicional de qual estado?",
   ["Maranhão", "Pará", "Bahia", "Ceará"], "Maranhão",
   "Foi criado em São Luís, em 1920, pelo farmacêutico Jesus Norberto Gomes.",
   "Guaraná Jesus", br=True)
tf(B, "games", 3, 14, "A Nintendo começou, no século XIX, fabricando cartas de baralho.", True,
   "A Nintendo foi fundada em 1889, em Quioto, fazendo cartas hanafuda.", "Nintendo – História")
mc(B, "slogans", 3, 14, "Qual empresa brasileira de cosméticos usa o slogan 'bem estar bem'?",
   ["Natura", "O Boticário", "Avon", "Jequiti"], "Natura",
   "A Natura foi fundada em 1969, em São Paulo.", "Natura", br=True)
mc(B, "slogans", 3, 16, "Qual biscoito ficou famoso pela frase 'vende mais porque é fresquinho ou é fresquinho porque vende mais'?",
   ["Tostines", "Passatempo", "Trakinas", "Bauducco"], "Tostines",
   "A campanha dos anos 1980 virou um ditado popular no Brasil.", "Propaganda brasileira – arquivo do CONAR/ABP",
   br=True)
mc(B, "empresas brasileiras", 4, 16, "Em qual estado brasileiro nasceu a Sadia?",
   ["Santa Catarina", "Rio Grande do Sul", "Paraná", "São Paulo"], "Santa Catarina",
   "A Sadia foi fundada em 1944 na cidade de Concórdia.", "BRF – História da Sadia", br=True)
mc(B, "brinquedos", 4, 14, "O nome LEGO vem de uma expressão dinamarquesa que significa o quê?",
   ["Brinque bem", "Monte rápido", "Bloco forte", "Criança feliz"], "Brinque bem",
   "LEGO vem de 'leg godt', que quer dizer 'brinque bem'.", "The LEGO Group – História")

# =========================================================== CULINÁRIA
F = "gas"
mc(F, "frutas", 1, 6, "Qual fruta tem o mesmo nome de uma cor?",
   ["Laranja", "Maçã", "Banana", "Abacaxi"], "Laranja",
   "A laranja é uma fruta cítrica rica em vitamina C.", "Embrapa")
mc(F, "legumes", 1, 6, "Qual legume laranja os coelhos adoram comer nos desenhos animados?",
   ["Cenoura", "Batata", "Pepino", "Beterraba"], "Cenoura",
   "A cenoura é rica em betacaroteno, que vira vitamina A no corpo.", "Embrapa")
tf(F, "ingredientes", 1, 6, "O queijo é feito de leite.", True,
   "Existem queijos de leite de vaca, cabra, ovelha e até de búfala.", "Embrapa Gado de Leite")
mc(F, "frutas", 1, 6, "Qual fruta é verde por fora e vermelha por dentro, com sementes pretas?",
   ["Melancia", "Melão", "Kiwi", "Abacate"], "Melancia",
   "A melancia tem mais de 90% de água.", "Embrapa")
op(F, "ingredientes", 1, 6, "Qual alimento doce é produzido pelas abelhas?", "Mel",
   ["mel"],
   "As abelhas fazem o mel a partir do néctar das flores.", "Embrapa")
mc(F, "massas", 1, 6, "Qual destes alimentos é um tipo de massa?",
   ["Macarrão", "Arroz", "Feijão", "Alface"], "Macarrão",
   "O macarrão é feito de farinha de trigo e água, às vezes com ovos.",
   "Enciclopédia Britannica – verbete 'Pasta'", syn=["macarrao"])
mc(F, "pratos do mundo", 2, 10, "De qual país é típico o taco, uma tortilha de milho recheada?",
   ["México", "Espanha", "Argentina", "Peru"], "México",
   "A tortilha de milho é feita no México desde antes da chegada dos europeus.",
   "Enciclopédia Britannica – verbete 'Mexican cuisine'", syn=["mexico"])
tf(F, "ingredientes", 2, 12, "Do ponto de vista da botânica, o tomate é um fruto.", True,
   "O tomate se forma a partir da flor e guarda as sementes, como todo fruto.", "Embrapa Hortaliças")
mc(F, "doces", 2, 10, "Qual sobremesa mineira junta goiabada com queijo?",
   ["Romeu e Julieta", "Pé de moleque", "Cocada", "Quindim"], "Romeu e Julieta",
   "O nome brinca com o casal da peça de Shakespeare.", "Enciclopédia da culinária brasileira", br=True)
mc(F, "doces", 2, 12, "O quindim é feito com gema de ovo, açúcar e qual outro ingrediente?",
   ["Coco", "Chocolate", "Morango", "Amendoim"], "Coco",
   "O quindim tem origem nos doces de gema portugueses.", "Enciclopédia da culinária brasileira", br=True)
mc(F, "pratos", 2, 12, "Qual prato baiano leva peixe, leite de coco e azeite de dendê?",
   ["Moqueca", "Feijoada", "Caruru", "Acarajé"], "Moqueca",
   "A moqueca capixaba é uma versão sem dendê e sem leite de coco.",
   "Enciclopédia da culinária brasileira", br=True)
op(F, "bebidas", 1, 8, "Qual bebida quente é feita com grãos torrados e moídos, e muitos adultos tomam de manhã?", "Café",
   ["café", "cafe", "cafezinho"],
   "O café chegou ao Brasil em 1727, trazido para o Pará.", "Embrapa Café", br=True)
mc(F, "pratos do mundo", 3, 14, "Qual é o principal ingrediente do homus, pasta típica do Oriente Médio?",
   ["Grão-de-bico", "Lentilha", "Feijão-branco", "Ervilha"], "Grão-de-bico",
   "O homus também leva tahine, que é uma pasta de gergelim.",
   "Enciclopédia Britannica – verbete 'Hummus'", syn=["grao-de-bico", "grão de bico"])
mc(F, "pratos do mundo", 3, 14, "Qual erva é a base do molho pesto genovês?",
   ["Manjericão", "Salsinha", "Coentro", "Hortelã"], "Manjericão",
   "O pesto também leva pinoli, alho, queijo e azeite.",
   "Enciclopédia Britannica – verbete 'Pesto'", syn=["manjericao"])
mc(F, "doces", 3, 14, "Qual doce português de massa folhada com creme é famoso em Belém, Lisboa?",
   ["Pastel de nata", "Quindim", "Sonho", "Bolinho de chuva"], "Pastel de nata",
   "Também é chamado de pastel de Belém.", "Enciclopédia Britannica – verbete 'Pastel de nata'",
   syn=["pastel de belém"])
mc(F, "pratos", 3, 14, "Qual prato típico do Pará leva pato, tucupi e jambu?",
   ["Pato no tucupi", "Maniçoba", "Vatapá", "Tacacá"], "Pato no tucupi",
   "É o prato tradicional do almoço do Círio de Nazaré, em Belém.",
   "Enciclopédia da culinária brasileira", br=True)
tf(F, "ingredientes", 3, 14, "O chocolate branco é feito com manteiga de cacau.", True,
   "Ele leva manteiga de cacau, açúcar e leite, mas não a massa escura do cacau.",
   "Enciclopédia Britannica – verbete 'Chocolate'")
mc(F, "ingredientes", 4, 16, "De qual planta se extrai o tucupi, caldo amarelo da culinária amazônica?",
   ["Mandioca", "Milho", "Açaí", "Cupuaçu"], "Mandioca",
   "O tucupi vem da mandioca-brava e precisa ser fervido para eliminar o veneno.",
   "Embrapa Amazônia Oriental", br=True)
