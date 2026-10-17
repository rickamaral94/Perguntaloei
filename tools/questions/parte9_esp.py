# Perguntas novas: esportes. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "esp"

# =========================================================== FÁCEIS
mc(T, "equipamentos", 1, 6, "O que o goleiro de futebol costuma usar nas mãos para agarrar melhor a bola?",
   ["Luvas", "Raquete", "Capacete", "Taco"], "Luvas",
   "As luvas de goleiro têm palmas emborrachadas que ajudam a segurar a bola e protegem os dedos.",
   "FIFA – Regras do Jogo (IFAB), Regra 4: Equipamento dos jogadores")
mc(T, "equipamentos", 1, 6, "No tênis, o que o jogador usa para bater na bola?",
   ["Raquete", "Taco", "Luva", "Bastão"], "Raquete",
   "A raquete de tênis tem uma armação com cordas bem esticadas que lançam a bola para o outro lado da rede.",
   "Federação Internacional de Tênis (ITF) – Regras do Tênis")
mc(T, "equipamentos", 1, 6, "Que equipamento o nadador usa para proteger os olhos dentro da água?",
   ["Óculos de natação", "Capacete", "Joelheira", "Caneleira"], "Óculos de natação",
   "Os óculos de natação vedam os olhos, evitando a irritação causada pelo cloro e ajudando o atleta a enxergar.",
   "Enciclopédia Britannica – verbete 'Swimming'")
mc(T, "modalidades", 1, 6, "Em qual esporte se usa uma prancha com quatro rodinhas para fazer manobras?",
   ["Skate", "Surfe", "Patinação", "Ciclismo"], "Skate",
   "O skate estreou nos Jogos Olímpicos em Tóquio 2020, com provas de rua e de parque.",
   "Comitê Olímpico Internacional – verbete 'Skateboarding'")
mc(T, "esportes de inverno", 1, 8, "Qual esporte de inverno se pratica descendo montanhas nevadas com duas pranchas compridas presas aos pés?",
   ["Esqui", "Snowboard", "Curling", "Hóquei no gelo"], "Esqui",
   "No esqui o atleta usa duas pranchas e bastões; no snowboard, uma prancha só.",
   "Enciclopédia Britannica – verbete 'Skiing'")
mc(T, "ginástica", 1, 7, "Em qual esporte as atletas fazem movimentos com fitas, arcos e bolas ao som de música?",
   ["Ginástica rítmica", "Nado artístico", "Patinação artística", "Ginástica artística"], "Ginástica rítmica",
   "Na ginástica rítmica, os aparelhos são a corda, o arco, a bola, as maças e a fita.",
   "Comitê Olímpico Internacional – verbete 'Rhythmic Gymnastics'")
mc(T, "esportes de inverno", 1, 7, "Em qual esporte os atletas deslizam sobre o gelo com lâminas nos pés, fazendo giros e saltos com música?",
   ["Patinação artística", "Ginástica rítmica", "Esqui", "Skate"], "Patinação artística",
   "A patinação artística é uma das modalidades mais antigas dos Jogos Olímpicos de Inverno.",
   "Comitê Olímpico Internacional – verbete 'Figure Skating'")
mc(T, "olimpíadas", 1, 7, "Que medalha recebe quem fica em segundo lugar numa prova dos Jogos Olímpicos?",
   ["Prata", "Ouro", "Bronze", "Cobre"], "Prata",
   "Nos Jogos Olímpicos, o primeiro lugar ganha ouro, o segundo prata e o terceiro bronze.",
   "Comitê Olímpico Internacional – Carta Olímpica")
mc(T, "natação", 1, 8, "Qual estilo da natação é nadado de barriga para cima?",
   ["Costas", "Peito", "Borboleta", "Crawl"], "Costas",
   "O nado costas é o único dos quatro estilos olímpicos em que o atleta larga dentro da água.",
   "World Aquatics – Regras de Natação")
mc(T, "regras", 1, 8, "No futebol, qual cor de cartão serve de advertência, sendo que dois deles no mesmo jogo resultam em expulsão?",
   ["Amarelo", "Vermelho", "Verde", "Azul"], "Amarelo",
   "Quem recebe o segundo cartão amarelo na mesma partida também recebe o vermelho e deixa o campo.",
   "FIFA – Regras do Jogo (IFAB), Regra 12: Faltas e conduta antidesportiva")
mc(T, "modalidades", 1, 9, "Qual esporte coletivo se joga com as mãos, arremessando a bola para dentro de um gol?",
   ["Handebol", "Polo aquático", "Futsal", "Basquete"], "Handebol",
   "O handebol é disputado em quadra, e os jogadores podem dar no máximo três passos segurando a bola.",
   "Federação Internacional de Handebol (IHF) – Regras do Jogo")
mc(T, "lutas", 1, 9, "Qual luta japonesa tem lutadores muito pesados que tentam empurrar o adversário para fora de um círculo?",
   ["Sumô", "Caratê", "Judô", "Kung fu"], "Sumô",
   "No sumô, perde quem sair do círculo ou tocar o chão com qualquer parte do corpo além da sola dos pés.",
   "Enciclopédia Britannica – verbete 'Sumo'")
mc(T, "lutas", 1, 9, "Em qual esporte olímpico os atletas usam roupa branca, máscara e armas como o florete e o sabre?",
   ["Esgrima", "Tiro com arco", "Caratê", "Pentatlo"], "Esgrima",
   "A esgrima tem três armas: florete, espada e sabre, e os toques são registrados por sensores elétricos.",
   "Comitê Olímpico Internacional – verbete 'Fencing'")
mc(T, "estádios", 1, 10, "Em qual cidade fica o estádio do Pacaembu?",
   ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Santos"], "São Paulo",
   "O Pacaembu foi inaugurado em 1940 e recebeu jogos da Copa do Mundo de 1950.",
   "Prefeitura de São Paulo – Estádio do Pacaembu", br=True)
mc(T, "jogadores", 1, 10, "Diego Maradona, campeão da Copa de 1986, era de qual país?",
   ["Argentina", "Uruguai", "Itália", "Espanha"], "Argentina",
   "Maradona foi o capitão da Argentina no título mundial de 1986, no México.",
   "FIFA – verbete 'Diego Maradona'")
mc(T, "clubes", 1, 9, "Qual clube carioca tem o apelido de 'Mengão'?",
   ["Flamengo", "Fluminense", "Vasco", "Botafogo"], "Flamengo",
   "O Clube de Regatas do Flamengo veste vermelho e preto e é um dos clubes mais populares do Brasil.",
   "Clube de Regatas do Flamengo – História", br=True)
mc(T, "basquete", 1, 10, "Qual é a sigla da principal liga de basquete dos Estados Unidos?",
   ["NBA", "NFL", "MLB", "NHL"], "NBA",
   "NFL é a liga de futebol americano, MLB a de beisebol e NHL a de hóquei no gelo.",
   "Enciclopédia Britannica – verbete 'National Basketball Association'")
tf(T, "vôlei", 1, 6, "No vôlei, há uma rede alta separando os dois times.", True,
   "A rede do vôlei masculino adulto fica a 2,43 metros de altura, e a do feminino a 2,24 metros.",
   "Federação Internacional de Vôlei (FIVB) – Regras Oficiais")
tf(T, "atletismo", 1, 6, "Numa corrida, vence quem chega por último à linha de chegada.", False,
   "Vence quem cruza primeiro a linha de chegada, ou seja, quem faz o percurso em menos tempo.",
   "World Athletics – Regras de Competição")
tf(T, "regras", 1, 8, "Uma partida oficial de futebol é dividida em quatro tempos.", False,
   "A partida tem dois tempos de 45 minutos, com um intervalo entre eles.",
   "FIFA – Regras do Jogo (IFAB), Regra 7: Duração da partida")
tf(T, "futsal", 1, 8, "O futsal é jogado num campo de grama.", False,
   "O futsal é disputado em quadra, com piso liso de madeira ou material sintético.",
   "FIFA – Regras do Jogo de Futsal")
tf(T, "tênis", 1, 9, "No tênis, a bola pode quicar duas vezes antes de o jogador devolvê-la.", False,
   "No tênis, a bola só pode quicar uma vez no chão antes de ser rebatida; se quicar duas, o ponto é perdido.",
   "Federação Internacional de Tênis (ITF) – Regras do Tênis")
tf(T, "paralímpicos", 1, 9, "Os Jogos Paralímpicos reúnem atletas com deficiência.", True,
   "Os Jogos Paralímpicos acontecem logo depois dos Olímpicos, na mesma cidade-sede.",
   "Comitê Paralímpico Internacional")
tf(T, "olimpíadas", 1, 10, "A chama olímpica é acesa na Grécia, com a luz do sol, antes dos Jogos.", True,
   "A chama é acesa em Olímpia com um espelho que concentra os raios do sol e depois viaja numa tocha até a cidade-sede.",
   "Comitê Olímpico Internacional – 'The Olympic flame'")
tf(T, "jogadores", 1, 10, "Pelé ganhou três Copas do Mundo como jogador da seleção brasileira.", True,
   "Pelé foi campeão em 1958, 1962 e 1970, e é o único jogador com três títulos mundiais.",
   "FIFA – verbete 'Pelé'", br=True)
op(T, "regras", 1, 6, "No futebol, que palavra o narrador grita quando a bola entra na rede do adversário?", "Gol",
   ["gol", "golo", "goool"],
   "O gol vale um ponto, e vence a partida o time que marcar mais gols.",
   "FIFA – Regras do Jogo (IFAB), Regra 10")
op(T, "xadrez", 1, 7, "Qual jogo de tabuleiro tem peças chamadas rei, rainha, torre, bispo e cavalo?", "Xadrez",
   ["xadrez", "jogo de xadrez"],
   "O xadrez é reconhecido como esporte pelo Comitê Olímpico Internacional e tem campeonatos mundiais.",
   "Federação Internacional de Xadrez (FIDE) – Leis do Xadrez")
op(T, "regras", 1, 9, "No futebol, como se chama a cobrança feita da marca a 11 metros do gol?", "Pênalti",
   ["pênalti", "penalti", "penálti", "penalty", "tiro penal"],
   "O pênalti é marcado quando há falta dentro da grande área, e só o goleiro pode tentar defender.",
   "FIFA – Regras do Jogo (IFAB), Regra 14: O tiro penal")

# =========================================================== MÉDIAS
mc(T, "jogadores", 2, 12, "Qual é o apelido do ex-jogador Arthur Antunes Coimbra, grande ídolo do Flamengo?",
   ["Zico", "Zizinho", "Careca", "Dinamite"], "Zico",
   "Zico é o maior artilheiro da história do Flamengo e foi chamado de 'Galinho de Quintino'.",
   "Clube de Regatas do Flamengo – Ídolos", br=True)
mc(T, "jogadores", 2, 10, "Oscar Schmidt, apelidado de 'Mão Santa', foi um craque de qual esporte?",
   ["Basquete", "Vôlei", "Handebol", "Futebol"], "Basquete",
   "Oscar disputou cinco Olimpíadas e é um dos maiores pontuadores da história do basquete.",
   "FIBA – Hall da Fama, verbete 'Oscar Schmidt'", br=True)
mc(T, "ginástica", 2, 14, "Qual ginasta brasileira foi a primeira do país campeã mundial, no solo, em 2003?",
   ["Daiane dos Santos", "Rebeca Andrade", "Jade Barbosa", "Flávia Saraiva"], "Daiane dos Santos",
   "Daiane venceu o Mundial de Anaheim, nos Estados Unidos, e tem um salto com seu nome no código da ginástica.",
   "Confederação Brasileira de Ginástica", br=True)
mc(T, "copas do mundo", 2, 12, "Em qual país foi disputada a Copa do Mundo de 1970, a do tricampeonato brasileiro?",
   ["México", "Argentina", "Inglaterra", "Alemanha"], "México",
   "Na final, o Brasil venceu a Itália por 4 a 1, no Estádio Azteca, na Cidade do México.",
   "FIFA – Copa do Mundo de 1970", br=True)
mc(T, "copas do mundo", 2, 12, "Contra qual seleção o Brasil venceu a final da Copa do Mundo de 2002?",
   ["Alemanha", "França", "Itália", "Argentina"], "Alemanha",
   "O Brasil venceu por 2 a 0, com dois gols de Ronaldo, em Yokohama, no Japão.",
   "FIFA – Copa do Mundo de 2002", br=True)
mc(T, "copas do mundo", 2, 12, "Qual país sediou a Copa do Mundo de 2010, a primeira no continente africano?",
   ["África do Sul", "Egito", "Nigéria", "Marrocos"], "África do Sul",
   "A Copa de 2010 ficou marcada pelo som das vuvuzelas nos estádios.",
   "FIFA – Copa do Mundo de 2010")
mc(T, "copas do mundo", 2, 12, "Qual seleção conquistou a Copa do Mundo de 2010, seu primeiro título mundial?",
   ["Espanha", "Holanda", "Alemanha", "Itália"], "Espanha",
   "A Espanha venceu a Holanda por 1 a 0 na prorrogação, com gol de Andrés Iniesta.",
   "FIFA – Copa do Mundo de 2010")
mc(T, "futsal", 2, 10, "Quantos jogadores de cada time ficam em quadra numa partida de futsal, contando o goleiro?",
   ["5", "6", "7", "11"], "5",
   "No futsal cada equipe tem um goleiro e quatro jogadores de linha em quadra.",
   "FIFA – Regras do Jogo de Futsal, Regra 3", syn=("cinco",))
mc(T, "olimpíadas", 2, 10, "Qual cidade sediou os Jogos Olímpicos de 2024?",
   ["Paris", "Tóquio", "Los Angeles", "Londres"], "Paris",
   "Paris recebeu os Jogos pela terceira vez, cem anos depois da edição de 1924.",
   "Comitê Olímpico Internacional – Paris 2024")
mc(T, "mascotes", 2, 12, "Qual era o nome do mascote dos Jogos Olímpicos Rio 2016, inspirado na fauna brasileira?",
   ["Vinicius", "Tom", "Fuleco", "Zé Carioca"], "Vinicius",
   "O nome homenageia o poeta Vinicius de Moraes; o mascote paralímpico, Tom, homenageia Tom Jobim.",
   "Comitê Olímpico Internacional – Rio 2016", br=True)
mc(T, "mascotes", 2, 10, "Como se chamava o tatu-bola mascote da Copa do Mundo de 2014, no Brasil?",
   ["Fuleco", "Vinicius", "Tom", "Canarinho"], "Fuleco",
   "O nome Fuleco mistura as palavras 'futebol' e 'ecologia'.",
   "FIFA – Copa do Mundo de 2014", br=True)
mc(T, "atletismo", 2, 12, "Qual prova do atletismo consiste em arremessar uma bola de metal pesada o mais longe possível?",
   ["Arremesso de peso", "Lançamento de dardo", "Lançamento de disco", "Salto em altura"], "Arremesso de peso",
   "No arremesso de peso o atleta empurra a bola a partir do ombro; a bola masculina pesa 7,26 kg.",
   "World Athletics – Regras de Competição")
mc(T, "tênis", 2, 12, "No tênis, como se chama o saque que o adversário nem consegue tocar com a raquete?",
   ["Ace", "Smash", "Lob", "Voleio"], "Ace",
   "Um ace dá o ponto direto ao sacador, sem que o adversário consiga encostar na bola.",
   "Federação Internacional de Tênis (ITF) – Glossário")
mc(T, "basquete", 2, 12, "Em qual país o basquete foi inventado, em 1891?",
   ["Estados Unidos", "Canadá", "Inglaterra", "França"], "Estados Unidos",
   "O professor James Naismith criou o jogo em Springfield, Massachusetts, usando cestos de pêssego como alvo.",
   "Enciclopédia Britannica – verbete 'Basketball'")
mc(T, "jogadores", 2, 12, "Qual craque brasileiro, campeão das Copas de 1958 e 1962, ficou famoso pelas pernas tortas e pelos dribles?",
   ["Garrincha", "Didi", "Vavá", "Nilton Santos"], "Garrincha",
   "Mané Garrincha foi eleito o melhor jogador da Copa de 1962, no Chile.",
   "FIFA – verbete 'Garrincha'", br=True)
mc(T, "clubes", 2, 10, "Por qual clube brasileiro Pelé jogou quase toda a sua carreira?",
   ["Santos", "Palmeiras", "Corinthians", "São Paulo"], "Santos",
   "Pelé defendeu o Santos de 1956 a 1974 e marcou mais de mil gols na carreira.",
   "Santos Futebol Clube – História", br=True)
mc(T, "natação", 2, 12, "Qual é o comprimento oficial de uma piscina olímpica?",
   ["50 metros", "25 metros", "100 metros", "75 metros"], "50 metros",
   "A piscina olímpica tem 50 metros de comprimento e dez raias.",
   "World Aquatics – Regras de Instalações", syn=("50", "cinquenta metros"))
tf(T, "natação", 2, 10, "O nado peito é o mais rápido dos quatro estilos da natação.", False,
   "O nado peito é o mais lento; o mais rápido é o crawl, usado pelos nadadores nas provas de estilo livre.",
   "World Aquatics – Regras de Natação")
tf(T, "copas do mundo", 2, 12, "O Brasil venceu a final da Copa de 1994 nos pênaltis, contra a Itália.", True,
   "A final, nos Estados Unidos, terminou 0 a 0, e o Brasil venceu por 3 a 2 nos pênaltis.",
   "FIFA – Copa do Mundo de 1994", br=True)
tf(T, "vôlei", 2, 10, "O vôlei foi inventado no Brasil.", False,
   "O vôlei foi criado em 1895 nos Estados Unidos por William Morgan, professor de educação física.",
   "Enciclopédia Britannica – verbete 'Volleyball'")
op(T, "xadrez", 2, 10, "No xadrez, como se chama o lance que ataca o rei sem que ele tenha como escapar, terminando a partida?",
   "Xeque-mate", ["xeque-mate", "xeque mate", "xequemate", "mate", "cheque-mate", "cheque mate"],
   "A expressão vem do persa 'shah mat', que quer dizer 'o rei está indefeso'.",
   "Federação Internacional de Xadrez (FIDE) – Leis do Xadrez")
op(T, "handebol", 2, 12, "Quantos jogadores de cada time ficam em quadra no handebol, contando o goleiro?", "7",
   ["7", "sete"],
   "Cada equipe de handebol tem seis jogadores de linha e um goleiro em quadra.",
   "Federação Internacional de Handebol (IHF) – Regras do Jogo")
op(T, "tênis", 2, 12, "Em qual país fica o torneio de tênis de Wimbledon?", "Inglaterra",
   ["inglaterra", "reino unido", "grã-bretanha", "gra-bretanha"],
   "Wimbledon, disputado em quadras de grama em Londres, é o torneio de tênis mais antigo do mundo.",
   "All England Lawn Tennis Club – História")

# =========================================================== DIFÍCEIS
mc(T, "basquete", 3, 14, "Qual jogadora brasileira, campeã mundial de basquete em 1994, ficou conhecida como 'Rainha do Basquete'?",
   ["Hortência", "Magic Paula", "Daiane dos Santos", "Marta"], "Hortência",
   "Hortência liderou a seleção no título mundial de 1994, na Austrália, e está no Hall da Fama da FIBA.",
   "FIBA – Hall da Fama, verbete 'Hortência Marcari'", br=True)
mc(T, "olimpíadas", 3, 14, "Qual francês é considerado o criador dos Jogos Olímpicos modernos?",
   ["Pierre de Coubertin", "Napoleão Bonaparte", "Louis Pasteur", "Júlio Verne"], "Pierre de Coubertin",
   "O barão Pierre de Coubertin fundou o Comitê Olímpico Internacional em 1894.",
   "Comitê Olímpico Internacional – verbete 'Pierre de Coubertin'")
mc(T, "xadrez", 3, 14, "No xadrez, como se chama a jogada em que o rei e uma torre se movem ao mesmo tempo?",
   ["Roque", "Xeque", "En passant", "Promoção"], "Roque",
   "No roque, o rei anda duas casas em direção à torre, e a torre pula para o outro lado dele.",
   "Federação Internacional de Xadrez (FIDE) – Leis do Xadrez")
mc(T, "paralímpicos", 3, 14, "Em qual esporte paralímpico o brasileiro Clodoaldo Silva se tornou um grande campeão?",
   ["Natação", "Atletismo", "Judô", "Bocha"], "Natação",
   "Clodoaldo, apelidado de 'Tubarão', ganhou seis medalhas de ouro nos Jogos Paralímpicos de Atenas 2004.",
   "Comitê Paralímpico Brasileiro", br=True)
mc(T, "olimpíadas", 3, 14, "Em qual edição dos Jogos a seleção brasileira masculina de futebol ganhou seu primeiro ouro olímpico?",
   ["Rio 2016", "Londres 2012", "Pequim 2008", "Atenas 2004"], "Rio 2016",
   "Na final, no Maracanã, o Brasil empatou com a Alemanha e venceu nos pênaltis.",
   "Comitê Olímpico do Brasil", br=True)
mc(T, "ginástica", 3, 14, "Qual destes aparelhos da ginástica artística é usado só pelas mulheres?",
   ["Trave", "Argolas", "Cavalo com alças", "Barra fixa"], "Trave",
   "A trave de equilíbrio tem apenas 10 centímetros de largura; argolas, cavalo com alças e barra fixa são provas masculinas.",
   "Federação Internacional de Ginástica (FIG) – Código de Pontuação")
mc(T, "copas do mundo", 3, 14, "Em qual país o Brasil conquistou sua primeira Copa do Mundo?",
   ["Suécia", "Suíça", "Chile", "Inglaterra"], "Suécia",
   "Em 1958, o Brasil venceu a Suécia, dona da casa, por 5 a 2 na final, em Estocolmo.",
   "FIFA – Copa do Mundo de 1958", br=True)
op(T, "paralímpicos", 3, 14, "Qual esporte paralímpico consiste em lançar bolas tentando deixá-las o mais perto possível de uma bolinha branca?",
   "Bocha", ["bocha", "bocha paralímpica", "boccia"],
   "A bocha paralímpica é disputada por atletas com deficiências severas, e o Brasil já ganhou ouro na modalidade.",
   "Comitê Paralímpico Brasileiro")
tf(T, "esportes de inverno", 3, 14, "Os Jogos Olímpicos de Inverno já foram realizados na América do Sul.", False,
   "Todas as edições dos Jogos de Inverno foram disputadas no Hemisfério Norte.",
   "Comitê Olímpico Internacional – Jogos Olímpicos de Inverno")
tf(T, "vôlei", 3, 16, "A seleção brasileira masculina de vôlei conquistou seu primeiro título mundial em 2002.", True,
   "O título veio na Argentina, com vitória sobre a Rússia na final; depois o Brasil foi campeão também em 2006 e 2010.",
   "Federação Internacional de Vôlei (FIVB) – Campeonato Mundial", br=True)
tf(T, "automobilismo", 3, 14, "Ayrton Senna conquistou seus três títulos de Fórmula 1 pela equipe McLaren.", True,
   "Senna foi campeão pela McLaren em 1988, 1990 e 1991.",
   "Fórmula 1 – verbete 'Ayrton Senna'", br=True)

# =========================================================== MUITO DIFÍCEIS
mc(T, "copas do mundo", 4, 16, "Qual atacante brasileiro marcou gols em todos os jogos da seleção na Copa de 1970?",
   ["Jairzinho", "Tostão", "Rivellino", "Gérson"], "Jairzinho",
   "Jairzinho, o 'Furacão da Copa', marcou sete gols nas seis partidas do Brasil no México.",
   "FIFA – Copa do Mundo de 1970", br=True)
mc(T, "copas do mundo", 4, 16, "Qual atacante francês marcou 13 gols numa única Copa do Mundo, a de 1958?",
   ["Just Fontaine", "Michel Platini", "Thierry Henry", "Zinedine Zidane"], "Just Fontaine",
   "Os 13 gols de Just Fontaine em 1958 são o recorde de gols de um jogador numa só edição da Copa.",
   "FIFA – verbete 'Just Fontaine'")
mc(T, "esportes de inverno", 4, 16, "Em qual país foram realizados os primeiros Jogos Olímpicos de Inverno, em 1924?",
   ["França", "Suíça", "Noruega", "Áustria"], "França",
   "A primeira edição aconteceu em Chamonix, ao pé do Monte Branco, nos Alpes franceses.",
   "Comitê Olímpico Internacional – Chamonix 1924")
mc(T, "futebol feminino", 4, 16, "Qual seleção venceu a primeira Copa do Mundo de futebol feminino da FIFA, em 1991?",
   ["Estados Unidos", "Noruega", "Alemanha", "China"], "Estados Unidos",
   "O torneio foi disputado na China, e os Estados Unidos venceram a Noruega por 2 a 1 na final.",
   "FIFA – Copa do Mundo Feminina de 1991")
mc(T, "tênis", 4, 16, "Quantas vezes a brasileira Maria Esther Bueno venceu o torneio de simples de Wimbledon?",
   ["3", "1", "5", "7"], "3",
   "Maria Esther venceu Wimbledon em simples em 1959, 1960 e 1964.",
   "International Tennis Hall of Fame – verbete 'Maria Bueno'", syn=("três",), br=True)
mc(T, "copas do mundo", 4, 16, "A Copa do Mundo de 1962, do bicampeonato brasileiro, foi disputada em qual país sul-americano?",
   ["Chile", "Uruguai", "Argentina", "Peru"], "Chile",
   "Na final, em Santiago, o Brasil venceu a Tchecoslováquia por 3 a 1.",
   "FIFA – Copa do Mundo de 1962", br=True)
