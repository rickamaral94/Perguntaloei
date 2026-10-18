# Perguntas novas: literatura. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "lit"

# ================================================== FÁCEIS
mc(T, "contos de fadas", 1, 6, "Na versão dos Irmãos Grimm de 'Chapeuzinho Vermelho', quem tira a menina e a vovó da barriga do lobo?",
   ["Um caçador", "Um padeiro", "Um rei", "Um pirata"], "Um caçador",
   "Na versão dos Grimm, o caçador abre a barriga do lobo adormecido e salva as duas.",
   "Enciclopédia Britannica – verbete 'Little Red Riding Hood'")
mc(T, "contos de fadas", 1, 6, "Em 'Os Três Porquinhos', de que material era a primeira casa, a mais fraquinha, que o lobo derrubou com um sopro?",
   ["Palha", "Pedra", "Ferro", "Tijolo"], "Palha",
   "Na versão mais conhecida, um porquinho faz a casa de palha, outro de madeira e o terceiro de tijolos.",
   "Enciclopédia Britannica – verbete 'The Three Little Pigs'")
tf(T, "contos de fadas", 1, 7, "Em 'João e Maria', os passarinhos comem as migalhas de pão que João deixou pelo caminho.", True,
   "Sem as migalhas, os irmãos se perdem na floresta e acabam encontrando a casa da bruxa.",
   "Irmãos Grimm – 'Contos para a Infância e o Lar' (1812)")
mc(T, "clássicos infantis", 1, 6, "Qual fadinha é a companheira inseparável de Peter Pan?",
   ["Sininho", "Aurora", "Fiona", "Emília"], "Sininho",
   "Sininho, chamada Tinker Bell em inglês, é uma fada pequena e ciumenta criada por J. M. Barrie.",
   "Enciclopédia Britannica – verbete 'Peter Pan'")
mc(T, "clássicos infantis", 1, 7, "Qual é o nome da menina que voa com Peter Pan até a Terra do Nunca?",
   ["Wendy", "Alice", "Dorothy", "Heidi"], "Wendy",
   "Wendy Darling leva junto seus irmãos, João e Miguel, na viagem à Terra do Nunca.",
   "Enciclopédia Britannica – verbete 'Peter Pan'")
tf(T, "clássicos infantis", 1, 7, "Em 'Alice no País das Maravilhas', Alice fica maior e menor depois de comer e beber coisas mágicas.", True,
   "Ao longo da história, Alice encolhe e cresce várias vezes, o que lhe causa muitas confusões.",
   "Lewis Carroll – 'Alice no País das Maravilhas' (1865)")
mc(T, "clássicos infantis", 1, 7, "Em 'O Pequeno Príncipe', de que flor o principezinho cuida no seu planeta?",
   ["Rosa", "Girassol", "Margarida", "Tulipa"], "Rosa",
   "A rosa é vaidosa, mas o principezinho a protege do vento com uma redoma de vidro.",
   "Antoine de Saint-Exupéry – 'O Pequeno Príncipe' (1943)")
tf(T, "clássicos infantis", 1, 8, "O Pequeno Príncipe mora num planeta enorme, cheio de cidades e pessoas.", False,
   "O planeta dele é tão pequeno que bastava arrastar a cadeira alguns passos para ver de novo o pôr do sol.",
   "Antoine de Saint-Exupéry – 'O Pequeno Príncipe' (1943)")
mc(T, "literatura infantil brasileira", 1, 6, "No Sítio do Picapau Amarelo, a Emília é uma boneca feita de quê?",
   ["Pano", "Porcelana", "Madeira", "Plástico"], "Pano",
   "Emília é uma boneca de pano costurada por Tia Nastácia, que começa a falar depois de tomar uma pílula.",
   "Monteiro Lobato – 'Reinações de Narizinho' (1931)", br=True)
mc(T, "literatura infantil brasileira", 1, 7, "Em 'Menina Bonita do Laço de Fita', qual animal branquinho quer ficar pretinho igual à menina?",
   ["Coelho", "Gato", "Cachorro", "Pato"], "Coelho",
   "O coelho tenta de tudo para escurecer o pelo, até descobrir que a cor vem dos pais e avós.",
   "Ana Maria Machado – 'Menina Bonita do Laço de Fita' (1986)", br=True)
mc(T, "literatura infantil brasileira", 1, 7, "O que o Menino Maluquinho, de Ziraldo, usa na cabeça?",
   ["Uma panela", "Um boné", "Uma coroa", "Um capacete"], "Uma panela",
   "A panela na cabeça virou a marca do personagem desde o livro de 1980.",
   "Ziraldo – 'O Menino Maluquinho' (1980)", br=True)
mc(T, "fábulas", 1, 7, "Na fábula 'A Raposa e as Uvas', o que a raposa diz das uvas que não consegue alcançar?",
   ["Que estão verdes", "Que estão salgadas", "Que são de plástico", "Que estão quentes"], "Que estão verdes",
   "A fábula mostra quem despreza aquilo que não consegue ter.",
   "Esopo – 'Fábulas'")
op(T, "fábulas", 1, 7, "Na fábula do pastorzinho mentiroso, que animal ele fingia estar atacando as ovelhas?", "Lobo",
   ["lobo", "o lobo", "um lobo", "lobos"],
   "De tanto mentir, quando o lobo apareceu de verdade, ninguém acreditou nele.",
   "Esopo – 'Fábulas'")
mc(T, "gêneros literários", 1, 8, "Como se chama a lição ensinada no final de uma fábula?",
   ["Moral da história", "Refrão", "Prefácio", "Rima"], "Moral da história",
   "As fábulas usam animais que falam para ensinar uma moral, como 'devagar se vai ao longe'.",
   "Enciclopédia Britannica – verbete 'Fable'")
mc(T, "livros", 1, 7, "Como se chama a pessoa que faz os desenhos de um livro?",
   ["Ilustrador", "Tradutor", "Revisor", "Editor"], "Ilustrador",
   "O ilustrador cria as imagens; muitos livros infantis têm autor e ilustrador na capa.",
   "Dicionário Houaiss – verbete 'ilustrador'")
tf(T, "fábulas", 1, 8, "Na fábula 'A Galinha dos Ovos de Ouro', o dono mata a galinha achando que havia muito ouro dentro dela.", True,
   "Por ganância, ele fica sem a galinha e sem os ovos de ouro que ganhava todo dia.",
   "Esopo – 'Fábulas'")
mc(T, "clássicos infantis", 1, 9, "Em 'Pinóquio', de Carlo Collodi, em que animal o boneco começa a se transformar no País dos Brinquedos?",
   ["Burro", "Gato", "Cachorro", "Coelho"], "Burro",
   "Os meninos que só querem brincar ganham orelhas e rabo de burro no País dos Brinquedos.",
   "Carlo Collodi – 'As Aventuras de Pinóquio' (1883)")
mc(T, "clássicos infantis", 1, 8, "Em 'Alice no País das Maravilhas', qual gato sorridente aparece e desaparece no ar?",
   ["Gato de Cheshire", "Gato de Botas", "Gato Félix", "Garfield"], "Gato de Cheshire",
   "Às vezes o Gato de Cheshire some aos poucos e só o sorriso fica no ar.",
   "Enciclopédia Britannica – verbete 'Cheshire Cat'")
tf(T, "literatura infantil brasileira", 1, 9, "Monteiro Lobato é o autor de 'O Menino Maluquinho'.", False,
   "'O Menino Maluquinho' foi escrito e desenhado por Ziraldo, em 1980.",
   "Ziraldo – 'O Menino Maluquinho' (1980)", br=True)
op(T, "gêneros literários", 1, 9, "Como se chama cada linha de um poema?", "Verso",
   ["verso", "versos", "um verso"],
   "Um grupo de versos forma uma estrofe.",
   "Dicionário Houaiss – verbete 'verso'")
mc(T, "gêneros literários", 1, 10, "Como se chama o livro que conta a história da vida de uma pessoa, escrito por outra?",
   ["Biografia", "Dicionário", "Atlas", "Enciclopédia"], "Biografia",
   "Quando a própria pessoa conta a sua vida, o livro se chama autobiografia.",
   "Dicionário Houaiss – verbete 'biografia'")
tf(T, "personagens célebres", 1, 10, "O detetive Sherlock Holmes foi criado pela escritora Agatha Christie.", False,
   "Sherlock Holmes foi criado por Arthur Conan Doyle; Agatha Christie criou Hercule Poirot e Miss Marple.",
   "Enciclopédia Britannica – verbete 'Sherlock Holmes'")
mc(T, "clássicos infantis", 1, 9, "Em 'Alice no País das Maravilhas', quem oferece um chá maluco junto com a Lebre de Março?",
   ["Chapeleiro Maluco", "Rainha de Copas", "Coelho Branco", "Lagarta Azul"], "Chapeleiro Maluco",
   "No chá maluco é sempre seis da tarde, por isso a mesa nunca é tirada.",
   "Enciclopédia Britannica – verbete 'Mad Hatter'")
mc(T, "personagens célebres", 1, 10, "Em 'Dom Quixote', contra o que o cavaleiro luta achando que são gigantes?",
   ["Moinhos de vento", "Árvores", "Ovelhas", "Castelos"], "Moinhos de vento",
   "A luta contra os moinhos de vento é a cena mais famosa do livro de Cervantes.",
   "Enciclopédia Britannica – verbete 'Don Quixote'")
mc(T, "personagens célebres", 1, 10, "Qual é o nome do médico amigo e ajudante de Sherlock Holmes?",
   ["Dr. Watson", "Dr. Jekyll", "Dr. Frankenstein", "Dr. Moriarty"], "Dr. Watson",
   "John Watson é quem narra a maior parte das aventuras de Sherlock Holmes.",
   "Enciclopédia Britannica – verbete 'Dr. Watson'")
mc(T, "contos de fadas", 1, 10, "Os Irmãos Grimm, que recolheram contos como 'Branca de Neve' e 'Rapunzel', eram de qual país?",
   ["Alemanha", "França", "Dinamarca", "Itália"], "Alemanha",
   "Jacob e Wilhelm Grimm eram alemães e estudavam a língua e as tradições do seu povo.",
   "Enciclopédia Britannica – verbete 'Brothers Grimm'")
op(T, "clássicos mundiais", 1, 9, "Em 'Ali Babá e os Quarenta Ladrões', qual é a frase mágica que abre a caverna do tesouro?", "Abre-te, Sésamo",
   ["abre-te sésamo", "abre-te, sésamo", "abre te sesamo", "abre-te sesamo", "abra-te sésamo"],
   "Sésamo é outro nome do gergelim.",
   "Enciclopédia Britannica – verbete 'Ali Baba'")

# ================================================== MÉDIAS
mc(T, "clássicos infantis", 2, 10, "Em 'O Pequeno Príncipe', qual animal ensina que 'o essencial é invisível aos olhos'?",
   ["Raposa", "Serpente", "Ovelha", "Coruja"], "Raposa",
   "A raposa pede para ser cativada e, na despedida, conta esse segredo ao principezinho.",
   "Antoine de Saint-Exupéry – 'O Pequeno Príncipe' (1943)")
op(T, "personagens célebres", 2, 12, "Em 'Robinson Crusoé', que nome o náufrago dá ao amigo que salva na ilha?", "Sexta-Feira",
   ["sexta-feira", "sexta feira", "sexta"],
   "Ele recebe esse nome porque foi salvo numa sexta-feira.",
   "Daniel Defoe – 'Robinson Crusoé' (1719)")
mc(T, "literatura infantil brasileira", 2, 10, "No Sítio do Picapau Amarelo, que animal é o Quindim, que vai morar no sítio?",
   ["Rinoceronte", "Elefante", "Hipopótamo", "Jacaré"], "Rinoceronte",
   "O rinoceronte Quindim aparece em 'Caçadas de Pedrinho' e vira amigo da turma.",
   "Monteiro Lobato – 'Caçadas de Pedrinho' (1933)", br=True)
tf(T, "literatura infantil brasileira", 2, 12, "No livro 'Flicts', de Ziraldo, o personagem principal é uma cor.", True,
   "Flicts é uma cor que não encontra lugar no mundo até descobrir que é a cor da Lua.",
   "Ziraldo – 'Flicts' (1969)", br=True)
mc(T, "literatura juvenil brasileira", 2, 12, "Qual escritor brasileiro criou a turma dos Karas, no livro 'A Droga da Obediência'?",
   ["Pedro Bandeira", "Ziraldo", "Monteiro Lobato", "Marcos Rey"], "Pedro Bandeira",
   "Lançado em 1984, o livro virou série e é muito lido nas escolas.",
   "Pedro Bandeira – 'A Droga da Obediência' (1984)", br=True)
mc(T, "autores brasileiros", 2, 12, "Em qual cidade nasceu Machado de Assis?",
   ["Rio de Janeiro", "Salvador", "São Paulo", "Recife"], "Rio de Janeiro",
   "Machado nasceu em 1839, no Morro do Livramento, e viveu a vida toda no Rio de Janeiro.",
   "Academia Brasileira de Letras – Machado de Assis, biografia", br=True)
mc(T, "autores brasileiros", 2, 14, "Em 'Capitães da Areia', de Jorge Amado, os meninos vivem nas ruas de qual cidade?",
   ["Salvador", "Recife", "Fortaleza", "Rio de Janeiro"], "Salvador",
   "O livro, de 1937, acompanha um grupo de meninos abandonados que vive num trapiche do porto de Salvador.",
   "Academia Brasileira de Letras – Jorge Amado, biografia", br=True)
mc(T, "poesia brasileira", 2, 14, "Qual poeta escreveu o poema que repete a pergunta 'E agora, José?'?",
   ["Carlos Drummond de Andrade", "Manuel Bandeira", "Vinicius de Moraes", "Mario Quintana"], "Carlos Drummond de Andrade",
   "O poema 'José' foi publicado em 1942 e a pergunta virou expressão popular.",
   "Enciclopédia Itaú Cultural – verbete 'Carlos Drummond de Andrade'", br=True)
mc(T, "poesia brasileira", 2, 12, "Qual poeta escreveu 'Trem de Ferro', que imita o barulho do trem com 'Café com pão, café com pão'?",
   ["Manuel Bandeira", "Cecília Meireles", "Castro Alves", "Olavo Bilac"], "Manuel Bandeira",
   "O ritmo dos versos lembra o som das rodas do trem andando nos trilhos.",
   "Enciclopédia Itaú Cultural – verbete 'Manuel Bandeira'", br=True)
mc(T, "poesia brasileira", 2, 14, "Qual poeta gaúcho escreveu 'Todos esses que aí estão atravancando meu caminho, eles passarão... eu passarinho!'?",
   ["Mario Quintana", "Carlos Drummond de Andrade", "Paulo Leminski", "Ferreira Gullar"], "Mario Quintana",
   "Os versos são do 'Poeminha do Contra', um dos mais conhecidos do poeta de Alegrete.",
   "Enciclopédia Itaú Cultural – verbete 'Mario Quintana'", br=True)
mc(T, "teatro brasileiro", 2, 12, "Em 'O Auto da Compadecida', como se chama o amigo medroso e contador de lorotas de João Grilo?",
   ["Chicó", "Severino", "Fabiano", "Riobaldo"], "Chicó",
   "Chicó sempre termina suas histórias inventadas com 'não sei, só sei que foi assim'.",
   "Ariano Suassuna – 'Auto da Compadecida' (1955)", br=True)
tf(T, "literatura portuguesa", 2, 14, "O poeta Luís de Camões era cego de um olho.", True,
   "Camões perdeu um olho lutando em Ceuta, no norte da África.",
   "Enciclopédia Britannica – verbete 'Luís de Camões'")
mc(T, "clássicos mundiais", 2, 12, "Qual escritor francês escreveu 'Os Três Mosqueteiros'?",
   ["Alexandre Dumas", "Victor Hugo", "Júlio Verne", "Molière"], "Alexandre Dumas",
   "O livro, de 1844, conta as aventuras de D'Artagnan com Athos, Porthos e Aramis.",
   "Enciclopédia Britannica – verbete 'The Three Musketeers'")
mc(T, "clássicos mundiais", 2, 12, "Histórias como 'Aladim' e 'Simbad, o Marujo' fazem parte de qual famosa coletânea?",
   ["As Mil e Uma Noites", "Fábulas de Esopo", "Contos de Grimm", "Ilíada"], "As Mil e Uma Noites",
   "A coletânea reúne contos do Oriente Médio, da Índia e da Pérsia, contados noite após noite.",
   "Enciclopédia Britannica – verbete 'The Thousand and One Nights'")
mc(T, "clássicos infantis", 2, 12, "Qual escritor escocês criou o personagem Peter Pan?",
   ["J. M. Barrie", "Lewis Carroll", "Roald Dahl", "Charles Dickens"], "J. M. Barrie",
   "Peter Pan apareceu numa peça de teatro de 1904 e depois virou livro.",
   "Enciclopédia Britannica – verbete 'J. M. Barrie'")
op(T, "gêneros literários", 2, 12, "Quantos versos tem um soneto?", "14",
   ["14", "catorze", "quatorze"],
   "O soneto tem duas estrofes de quatro versos e duas de três.",
   "Enciclopédia Britannica – verbete 'Sonnet'")
mc(T, "gêneros literários", 2, 12, "Qual gênero de texto curto, comum em jornais e revistas, comenta com leveza fatos do dia a dia?",
   ["Crônica", "Epopeia", "Tragédia", "Soneto"], "Crônica",
   "A crônica é muito forte no Brasil, com autores como Rubem Braga e Fernando Sabino.",
   "Dicionário Houaiss – verbete 'crônica'", br=True)
op(T, "prêmios literários", 2, 12, "Qual animal dá nome ao mais tradicional prêmio literário do Brasil, criado em 1959?", "Jabuti",
   ["jabuti", "o jabuti", "prêmio jabuti"],
   "O Prêmio Jabuti é entregue pela Câmara Brasileira do Livro.",
   "Câmara Brasileira do Livro – Prêmio Jabuti", br=True)
op(T, "academia brasileira de letras", 2, 14, "Quantas cadeiras tem a Academia Brasileira de Letras?", "40",
   ["40", "quarenta"],
   "Cada cadeira tem um patrono, e um novo membro só é eleito quando outro morre.",
   "Academia Brasileira de Letras", br=True)
tf(T, "autores brasileiros", 2, 12, "A poeta Cecília Meireles nasceu em Portugal.", False,
   "Cecília Meireles nasceu no Rio de Janeiro, em 1901.",
   "Academia Brasileira de Letras – Cecília Meireles, biografia", br=True)
tf(T, "crônica", 2, 14, "O cronista Luis Fernando Verissimo é filho do escritor Erico Verissimo.", True,
   "Luis Fernando, criador do 'Analista de Bagé', é filho do autor de 'O Tempo e o Vento'.",
   "Enciclopédia Itaú Cultural – verbete 'Luis Fernando Verissimo'", br=True)
tf(T, "clássicos mundiais", 2, 12, "O livro 'Dom Quixote' foi escrito originalmente em italiano.", False,
   "Miguel de Cervantes escreveu 'Dom Quixote' em espanhol; a primeira parte saiu em 1605.",
   "Enciclopédia Britannica – verbete 'Don Quixote'")
tf(T, "contos de fadas", 2, 12, "Hans Christian Andersen é o autor de 'Chapeuzinho Vermelho'.", False,
   "As versões mais famosas de 'Chapeuzinho Vermelho' são de Charles Perrault e dos Irmãos Grimm.",
   "Enciclopédia Britannica – verbete 'Little Red Riding Hood'")

# ================================================== DIFÍCEIS
mc(T, "clássicos infantis", 3, 12, "Em 'O Pequeno Príncipe', que árvores o principezinho arranca enquanto pequenas, para não destruírem seu planeta?",
   ["Baobás", "Palmeiras", "Pinheiros", "Ipês"], "Baobás",
   "Se crescessem, as raízes dos baobás poderiam rachar o pequeno planeta.",
   "Antoine de Saint-Exupéry – 'O Pequeno Príncipe' (1943)")
mc(T, "personagens célebres", 3, 14, "Como se chama o cavalo magro de Dom Quixote?",
   ["Rocinante", "Bucéfalo", "Pégaso", "Tornado"], "Rocinante",
   "Cervantes escolheu o nome porque o cavalo tinha sido um 'rocim', um pangaré.",
   "Enciclopédia Britannica – verbete 'Don Quixote'")
mc(T, "personagens célebres", 3, 14, "Em 'Romeu e Julieta', a qual família pertence Julieta?",
   ["Capuleto", "Montéquio", "Médici", "Bórgia"], "Capuleto",
   "Romeu é um Montéquio, e as duas famílias de Verona são inimigas.",
   "Enciclopédia Britannica – verbete 'Romeo and Juliet'")
mc(T, "literatura infantil brasileira", 3, 12, "No Sítio do Picapau Amarelo, qual é o nome verdadeiro da menina chamada de Narizinho?",
   ["Lúcia", "Maria", "Clara", "Beatriz"], "Lúcia",
   "Lobato a apresenta como 'Lúcia, a menina do narizinho arrebitado'.",
   "Monteiro Lobato – 'Reinações de Narizinho' (1931)", br=True)
mc(T, "autores brasileiros", 3, 16, "Em 'Vidas Secas', de Graciliano Ramos, como se chama o vaqueiro, pai da família?",
   ["Fabiano", "Paulo Honório", "Riobaldo", "Policarpo"], "Fabiano",
   "Fabiano foge da seca com a mulher, Sinha Vitória, os dois filhos e a cachorra Baleia.",
   "Enciclopédia Itaú Cultural – verbete 'Graciliano Ramos'", br=True)
tf(T, "autores brasileiros", 3, 16, "Antes de virar diplomata, o escritor Guimarães Rosa trabalhou como médico.", True,
   "Formado em medicina em Belo Horizonte, ele atendeu no interior de Minas Gerais, onde ouviu muitas histórias do sertão.",
   "Academia Brasileira de Letras – Guimarães Rosa, biografia", br=True)
mc(T, "autores brasileiros", 3, 16, "Qual escritora mineira criou o termo 'escrevivência', para a escrita que nasce da vida das mulheres negras?",
   ["Conceição Evaristo", "Carolina Maria de Jesus", "Clarice Lispector", "Adélia Prado"], "Conceição Evaristo",
   "Conceição Evaristo é autora de 'Ponciá Vicêncio' e 'Olhos d'Água'.",
   "Enciclopédia Itaú Cultural – verbete 'Conceição Evaristo'", br=True)
mc(T, "clássicos mundiais", 3, 16, "Em 'A Metamorfose', de Franz Kafka, em que Gregor Samsa acorda transformado?",
   ["Num inseto", "Num lobo", "Num pássaro", "Num peixe"], "Num inseto",
   "Gregor acorda transformado num enorme inseto e não consegue mais trabalhar.",
   "Enciclopédia Britannica – verbete 'The Metamorphosis'")
tf(T, "cordel", 3, 14, "A literatura de cordel foi reconhecida pelo Iphan como Patrimônio Cultural do Brasil.", True,
   "O registro como patrimônio imaterial foi aprovado em 2018.",
   "Iphan – Literatura de Cordel", br=True)
tf(T, "academia brasileira de letras", 3, 16, "Rachel de Queiroz foi a primeira mulher eleita para a Academia Brasileira de Letras.", True,
   "Ela foi eleita em 1977, quase oitenta anos depois da fundação da Academia.",
   "Academia Brasileira de Letras – Rachel de Queiroz, biografia", br=True)
mc(T, "poesia brasileira", 3, 16, "Qual poeta pernambucano escreveu 'Morte e Vida Severina'?",
   ["João Cabral de Melo Neto", "Manuel Bandeira", "Augusto dos Anjos", "Ferreira Gullar"], "João Cabral de Melo Neto",
   "O poema acompanha o retirante Severino em sua caminhada do sertão até o Recife.",
   "Academia Brasileira de Letras – João Cabral de Melo Neto, biografia", br=True)
mc(T, "contos de fadas", 3, 14, "Qual escritor francês publicou em 1697 contos como 'O Gato de Botas' e 'O Barba Azul'?",
   ["Charles Perrault", "Júlio Verne", "Victor Hugo", "Alexandre Dumas"], "Charles Perrault",
   "O livro de Perrault também trazia versões de 'Cinderela' e 'A Bela Adormecida'.",
   "Enciclopédia Britannica – verbete 'Charles Perrault'")

# ================================================== MUITO DIFÍCEIS
mc(T, "autores brasileiros", 4, 14, "Em qual cidade paulista nasceu Monteiro Lobato?",
   ["Taubaté", "Campinas", "Santos", "Sorocaba"], "Taubaté",
   "Lobato nasceu em 1882, e o sítio da sua infância em Taubaté hoje é um museu.",
   "Academia Brasileira de Letras – Monteiro Lobato, biografia", br=True)
mc(T, "clássicos mundiais", 4, 14, "Em 'As Mil e Uma Noites', como se chama a jovem que conta histórias ao sultão para salvar a própria vida?",
   ["Sherazade", "Jasmine", "Cleópatra", "Nefertiti"], "Sherazade",
   "Ela deixa cada história sem final ao amanhecer, e o sultão adia sua morte para ouvir o resto.",
   "Enciclopédia Britannica – verbete 'Scheherazade'")
mc(T, "prêmios literários", 4, 16, "Qual escritora brasileira ganhou em 2000 o Prêmio Hans Christian Andersen, o mais importante da literatura infantil?",
   ["Ana Maria Machado", "Ruth Rocha", "Cecília Meireles", "Clarice Lispector"], "Ana Maria Machado",
   "Ela foi a segunda brasileira a receber o prêmio, depois de Lygia Bojunga, em 1982.",
   "IBBY – Hans Christian Andersen Awards", br=True)
mc(T, "prêmios literários", 4, 16, "Qual escritor português foi o primeiro vencedor do Prêmio Camões, em 1989?",
   ["Miguel Torga", "José Saramago", "Jorge Amado", "João Cabral de Melo Neto"], "Miguel Torga",
   "No ano seguinte, o prêmio foi para o brasileiro João Cabral de Melo Neto.",
   "Biblioteca Nacional – Prêmio Camões")
mc(T, "autores brasileiros", 4, 16, "Quem é o narrador, um ex-jagunço, de 'Grande Sertão: Veredas'?",
   ["Riobaldo", "Diadorim", "Fabiano", "Macunaíma"], "Riobaldo",
   "Riobaldo conta sua vida a um visitante e fala muito do amigo Diadorim.",
   "Enciclopédia Itaú Cultural – verbete 'Guimarães Rosa'", br=True)
mc(T, "autores brasileiros", 4, 16, "Em 'O Alienista', de Machado de Assis, como se chama o hospício criado pelo doutor Simão Bacamarte?",
   ["Casa Verde", "Casa Amarela", "Solar das Flores", "Palácio Azul"], "Casa Verde",
   "Na história, o médico vai internando quase toda a cidade de Itaguaí na Casa Verde.",
   "Machado de Assis – 'O Alienista' (1882)", br=True)
