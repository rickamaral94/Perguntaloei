# Perguntas novas (parte 7d). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== LITERATURA
L = "lit"
mc(L, "fábulas", 1, 6, "Na fábula de Esopo, qual animal lento vence a corrida contra a lebre?",
   ["Tartaruga", "Caracol", "Bicho-preguiça", "Lesma"], "Tartaruga",
   "A lebre, confiante demais, para para descansar e a tartaruga vence devagar e sempre.",
   "Enciclopédia Britannica – verbete 'Aesop'")
mc(L, "fábulas", 1, 7, "Na famosa fábula, qual inseto passa o verão cantando enquanto a formiga trabalha?",
   ["Cigarra", "Grilo", "Abelha", "Borboleta"], "Cigarra",
   "Quando chega o inverno, a cigarra não tem comida guardada e pede ajuda à formiga.",
   "La Fontaine – Fábulas")
tf(L, "contos de fadas", 1, 7, "No conto dos Irmãos Grimm, Rapunzel joga seus longos cabelos pela janela da torre para que alguém suba.", True,
   "A bruxa e depois o príncipe sobem na torre segurando as tranças de Rapunzel.",
   "Enciclopédia Britannica – verbete 'Rapunzel'")
mc(L, "literatura infantil", 1, 8, "No Sítio do Picapau Amarelo, qual é o nome da cozinheira famosa pelos seus bolinhos?",
   ["Tia Nastácia", "Dona Benta", "Narizinho", "Emília"], "Tia Nastácia",
   "Foi Tia Nastácia quem costurou a boneca Emília.",
   "Monteiro Lobato – Reinações de Narizinho", br=True)
op(L, "literatura infantil", 1, 9, "No Sítio do Picapau Amarelo, como se chama a avó de Narizinho e Pedrinho, dona do sítio?", "Dona Benta",
   ["dona benta", "benta", "vovo benta", "vovó benta", "dona benta encerrabodes de oliveira"],
   "Dona Benta adora contar histórias aos netos na varanda do sítio.",
   "Monteiro Lobato – Reinações de Narizinho", br=True)
mc(L, "autores estrangeiros", 1, 9, "Quem escreveu 'Alice no País das Maravilhas'?",
   ["Lewis Carroll", "J. M. Barrie", "Charles Dickens", "Mark Twain"], "Lewis Carroll",
   "O livro foi publicado em 1865 pelo matemático inglês que usava esse pseudônimo.",
   "Enciclopédia Britannica – verbete 'Lewis Carroll'")
mc(L, "autores estrangeiros", 2, 10, "Qual escritor norte-americano criou os personagens Tom Sawyer e Huckleberry Finn?",
   ["Mark Twain", "Jack London", "Herman Melville", "Edgar Allan Poe"], "Mark Twain",
   "As aventuras se passam às margens do rio Mississippi.",
   "Enciclopédia Britannica – verbete 'Mark Twain'")
mc(L, "autores estrangeiros", 2, 12, "Qual escritor francês escreveu 'Vinte Mil Léguas Submarinas', com o capitão Nemo?",
   ["Júlio Verne", "Victor Hugo", "Alexandre Dumas", "Gustave Flaubert"], "Júlio Verne",
   "Verne é um dos pais da ficção científica e também escreveu 'A Volta ao Mundo em 80 Dias'.",
   "Enciclopédia Britannica – verbete 'Jules Verne'")
mc(L, "autores estrangeiros", 2, 12, "Qual escritor criou 'As Crônicas de Nárnia', com o leão Aslam?",
   ["C. S. Lewis", "J. R. R. Tolkien", "Roald Dahl", "Lewis Carroll"], "C. S. Lewis",
   "C. S. Lewis era amigo de Tolkien e professor em Oxford.",
   "Enciclopédia Britannica – verbete 'C.S. Lewis'")
mc(L, "personagens", 2, 12, "Em 'Dom Quixote', como se chama o fiel escudeiro do cavaleiro?",
   ["Sancho Pança", "Rocinante", "Dulcineia", "Sansão Carrasco"], "Sancho Pança",
   "Rocinante é o cavalo de Dom Quixote, e Dulcineia é sua amada imaginária.",
   "Miguel de Cervantes – Dom Quixote")
tf(L, "autores brasileiros", 2, 12, "Erico Verissimo, autor de 'O Tempo e o Vento', nasceu no Rio Grande do Sul.", True,
   "Ele nasceu em Cruz Alta, em 1905, e sua grande obra conta a formação do povo gaúcho.",
   "Enciclopédia Britannica – verbete 'Erico Verissimo'", br=True)
mc(L, "autores brasileiros", 2, 12, "Qual escritora cearense escreveu 'O Quinze', sobre a grande seca de 1915?",
   ["Rachel de Queiroz", "Cecília Meireles", "Clarice Lispector", "Lygia Fagundes Telles"], "Rachel de Queiroz",
   "Em 1977, ela se tornou a primeira mulher eleita para a Academia Brasileira de Letras.",
   "Academia Brasileira de Letras", br=True)
mc(L, "poesia", 2, 14, "Qual poeta baiano escreveu 'O Navio Negreiro' e ficou conhecido como o 'poeta dos escravos'?",
   ["Castro Alves", "Gonçalves Dias", "Álvares de Azevedo", "Olavo Bilac"], "Castro Alves",
   "O poema de 1869 denuncia o horror do tráfico de pessoas escravizadas.",
   "Academia Brasileira de Letras", br=True)
mc(L, "teatro", 2, 14, "Em qual peça de Shakespeare aparece a frase 'Ser ou não ser, eis a questão'?",
   ["Hamlet", "Macbeth", "Otelo", "Rei Lear"], "Hamlet",
   "A frase abre o monólogo do príncipe da Dinamarca no terceiro ato.",
   "Enciclopédia Britannica – verbete 'Hamlet'")
mc(L, "autores brasileiros", 3, 14, "Quem escreveu 'Triste Fim de Policarpo Quaresma'?",
   ["Lima Barreto", "Aluísio Azevedo", "Raul Pompeia", "Graça Aranha"], "Lima Barreto",
   "O romance de 1915 conta a história de um major patriota e ingênuo.",
   "Academia Brasileira de Letras", br=True)
mc(L, "poesia", 3, 14, "Qual poeta escreveu o 'Soneto de Fidelidade', que termina com 'que seja infinito enquanto dure'?",
   ["Vinicius de Moraes", "Manuel Bandeira", "Mario Quintana", "Cecília Meireles"], "Vinicius de Moraes",
   "Além de poeta, Vinicius foi um dos criadores da bossa nova.",
   "Academia Brasileira de Letras", br=True)
mc(L, "autores estrangeiros", 3, 16, "Qual escritor colombiano escreveu 'Cem Anos de Solidão'?",
   ["Gabriel García Márquez", "Jorge Luis Borges", "Mario Vargas Llosa", "Julio Cortázar"], "Gabriel García Márquez",
   "O romance se passa na cidade fictícia de Macondo; o autor ganhou o Nobel em 1982.",
   "Enciclopédia Britannica – verbete 'Gabriel García Márquez'")
tf(L, "autores brasileiros", 3, 16, "A escritora Clarice Lispector nasceu na Ucrânia e veio para o Brasil ainda bebê.", True,
   "Ela nasceu em 1920 e chegou com a família ao Brasil por volta de 1922.",
   "Enciclopédia Britannica – verbete 'Clarice Lispector'", br=True)
mc(L, "autores estrangeiros", 3, 16, "Qual escritor russo escreveu 'Crime e Castigo'?",
   ["Fiódor Dostoiévski", "Liev Tolstói", "Anton Tchekhov", "Aleksandr Púchkin"], "Fiódor Dostoiévski",
   "O romance de 1866 acompanha o estudante Raskólnikov depois de um assassinato.",
   "Enciclopédia Britannica – verbete 'Crime and Punishment'")
mc(L, "autores portugueses", 3, 16, "Qual escritor português escreveu 'O Primo Basílio' e 'Os Maias'?",
   ["Eça de Queirós", "Camilo Castelo Branco", "Almeida Garrett", "José Saramago"], "Eça de Queirós",
   "Eça de Queirós é o grande nome do realismo em Portugal.",
   "Enciclopédia Britannica – verbete 'José Maria de Eça de Queirós'")
mc(L, "poesia", 4, 16, "Qual poeta português criou heterônimos como Alberto Caeiro, Ricardo Reis e Álvaro de Campos?",
   ["Fernando Pessoa", "Luís de Camões", "Florbela Espanca", "Bocage"], "Fernando Pessoa",
   "Cada heterônimo tinha biografia e estilo próprios.",
   "Enciclopédia Britannica – verbete 'Fernando Pessoa'")
op(L, "poesia", 4, 16, "Qual poeta paraibano publicou um único livro, chamado 'Eu', com versos sombrios como os de 'Versos Íntimos'?", "Augusto dos Anjos",
   ["augusto dos anjos", "augusto"],
   "O livro saiu em 1912, e o poeta morreu dois anos depois.",
   "Academia Brasileira de Letras", br=True)

# =========================================================== PORTUGUÊS
P = "por"
tf(P, "alfabeto", 1, 6, "A palavra 'abelha' começa com uma vogal.", True,
   "A letra A é uma das cinco vogais do alfabeto.",
   "Academia Brasileira de Letras – VOLP")
mc(P, "gênero", 1, 7, "Como chamamos a fêmea do galo?",
   ["Galinha", "Gansa", "Pata", "Perua"], "Galinha",
   "O galo canta de manhã, e a galinha bota ovos.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(P, "gênero", 1, 8, "Se a mulher do rei é a rainha, a filha do rei é a...?",
   ["Princesa", "Duquesa", "Condessa", "Baronesa"], "Princesa",
   "Princesa é o feminino de príncipe, o filho do rei.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(P, "classes de palavras", 1, 8, "Qual destas palavras é um verbo?",
   ["Correr", "Mesa", "Azul", "Feliz"], "Correr",
   "Verbos indicam ações; mesa é substantivo, azul e feliz são adjetivos.",
   "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "ditados", 1, 9, "Qual é o final do ditado 'Água mole em pedra dura'?",
   ["Tanto bate até que fura", "Nunca se desgasta", "Logo vira areia", "Só faz barulho"], "Tanto bate até que fura",
   "O ditado ensina que a persistência vence as dificuldades.",
   "Câmara Cascudo – Locuções Tradicionais no Brasil")
mc(P, "plural", 2, 10, "Qual destas formas é o plural correto de 'limão'?",
   ["Limões", "Limãos", "Limães"], "Limões",
   "Palavras terminadas em -ão podem fazer plural em -ões, -ãos ou -ães; limão faz limões.",
   "Academia Brasileira de Letras – VOLP")
mc(P, "sinônimos", 2, 10, "Qual palavra tem o mesmo sentido de 'começar'?",
   ["Iniciar", "Terminar", "Parar", "Desistir"], "Iniciar",
   "Sinônimos são palavras de significado parecido.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(P, "antônimos", 2, 12, "Quem não tem coragem é chamado de quê?",
   ["Covarde", "Valente", "Ousado", "Destemido"], "Covarde",
   "Covarde é o antônimo de corajoso; as outras opções são sinônimos de corajoso.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(P, "gentílicos", 2, 12, "Quem nasce na cidade do Rio é carioca; e quem nasce no estado do Rio de Janeiro é chamado de quê?",
   ["Fluminense", "Capixaba", "Potiguar", "Paulista"], "Fluminense",
   "Fluminense vem do latim 'flumen', que quer dizer rio.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "expressões", 2, 12, "O que significa a expressão 'pagar o pato'?",
   ["Levar a culpa no lugar de outro", "Pagar caro por uma comida", "Perder um jogo", "Ficar devendo dinheiro"],
   "Levar a culpa no lugar de outro",
   "A expressão é usada quando alguém sofre as consequências de algo que não fez.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "ditados", 2, 12, "Qual é o final do ditado 'Quem não tem cão'?",
   ["Caça com gato", "Caça sozinho", "Não caça nada"], "Caça com gato",
   "O ditado significa que, na falta do ideal, a gente se vira com o que tem.",
   "Câmara Cascudo – Locuções Tradicionais no Brasil")
tf(P, "classes de palavras", 2, 12, "A palavra 'saudade' é um substantivo.", True,
   "Saudade dá nome a um sentimento, por isso é um substantivo abstrato.",
   "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "figuras de linguagem", 2, 12, "Qual figura de linguagem aparece em 'Minha casa é um forno', comparando sem usar a palavra 'como'?",
   ["Metáfora", "Onomatopeia", "Eufemismo", "Ironia"], "Metáfora",
   "A metáfora faz uma comparação implícita: a casa é muito quente, como um forno.",
   "Evanildo Bechara – Moderna Gramática Portuguesa")
tf(P, "ortografia", 2, 12, "As palavras 'mal' e 'mau' têm o mesmo significado.", False,
   "'Mau' é adjetivo, contrário de bom; 'mal' é advérbio ou substantivo, contrário de bem.",
   "Academia Brasileira de Letras")
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem suaviza uma ideia triste, como dizer 'ele partiu' em vez de 'ele morreu'?",
   ["Eufemismo", "Hipérbole", "Metáfora", "Onomatopeia"], "Eufemismo",
   "O eufemismo troca uma expressão dura por outra mais delicada.",
   "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem diz o contrário do que se pensa, como elogiar 'Que belo trabalho!' algo malfeito?",
   ["Ironia", "Eufemismo", "Comparação", "Personificação"], "Ironia",
   "Na ironia, o sentido verdadeiro é o oposto do que as palavras dizem.",
   "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "origem das palavras", 3, 14, "De qual língua indígena vêm palavras como 'abacaxi', 'pipoca' e 'jabuticaba'?",
   ["Tupi", "Quíchua", "Guarani", "Nheengatu"], "Tupi",
   "O tupi deixou milhares de palavras no português do Brasil, sobretudo nomes de plantas, animais e lugares.",
   "Dicionário Houaiss da Língua Portuguesa – etimologias", br=True)
mc(P, "origem das palavras", 3, 14, "Palavras como 'almofada', 'alface' e 'açúcar' chegaram ao português vindas de qual língua?",
   ["Árabe", "Grego", "Francês", "Alemão"], "Árabe",
   "Os árabes ocuparam a Península Ibérica por séculos e deixaram muitas palavras começadas por 'al-'.",
   "Dicionário Houaiss da Língua Portuguesa – etimologias")
mc(P, "vocabulário", 3, 14, "Qual é o significado do verbo 'procrastinar'?",
   ["Adiar", "Apressar", "Esquecer", "Repetir"], "Adiar",
   "Procrastinar é deixar para depois o que se deveria fazer agora.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(P, "plural", 3, 14, "Como se escreve o plural de 'guarda-chuva'?",
   ["Guarda-chuvas", "Guardas-chuvas", "Guardas-chuva"], "Guarda-chuvas",
   "Em compostos de verbo mais substantivo, só o substantivo vai para o plural.",
   "Academia Brasileira de Letras – VOLP")
mc(P, "coletivos", 3, 14, "Como se chama um grupo de camelos que viajam juntos?",
   ["Cáfila", "Alcateia", "Cardume", "Enxame"], "Cáfila",
   "Cáfila é o coletivo de camelos, comum nas caravanas do deserto.",
   "Dicionário Houaiss da Língua Portuguesa")
op(P, "vocabulário", 4, 16, "Como se chama a palavra ou frase que se lê igual de trás para frente, como 'ovo' e 'radar'?", "Palíndromo",
   ["palindromo", "palíndromo", "palindromos", "palíndromos"],
   "A palavra vem do grego e quer dizer 'que corre de volta'.",
   "Dicionário Houaiss da Língua Portuguesa")

# =========================================================== ARTES
A = "art"
mc(A, "cores", 1, 6, "Se misturarmos tinta azul com tinta vermelha, qual cor vamos obter?",
   ["Roxo", "Verde", "Laranja", "Marrom"], "Roxo",
   "Azul e vermelho são cores primárias que, juntas, formam o roxo.",
   "Enciclopédia Britannica – verbete 'color'")
mc(A, "escultura", 1, 7, "Como se chama a arte de criar figuras moldando argila ou esculpindo pedra e madeira?",
   ["Escultura", "Pintura", "Fotografia", "Gravura"], "Escultura",
   "A escultura é uma arte em três dimensões.",
   "Enciclopédia Britannica – verbete 'sculpture'")
tf(A, "música erudita", 1, 7, "A pessoa que rege uma orquestra é chamada de maestro.", True,
   "O maestro usa uma batuta para indicar o ritmo e as entradas dos músicos.",
   "Enciclopédia Britannica – verbete 'conducting'")
mc(A, "técnicas", 1, 8, "Como se chama a imagem feita juntando pedacinhos de pedra, vidro ou cerâmica?",
   ["Mosaico", "Aquarela", "Colagem", "Xilogravura"], "Mosaico",
   "Romanos e bizantinos decoravam pisos e paredes com mosaicos.",
   "Enciclopédia Britannica – verbete 'mosaic'")
mc(A, "técnicas", 1, 8, "Como se chama o suporte, geralmente de madeira com três pés, que segura a tela do pintor?",
   ["Cavalete", "Paleta", "Moldura", "Pincel"], "Cavalete",
   "Na paleta o pintor mistura as tintas; no cavalete ele apoia a tela.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(A, "gêneros de pintura", 2, 10, "Como se chama a pintura que mostra frutas, flores e objetos parados sobre uma mesa?",
   ["Natureza-morta", "Paisagem", "Retrato", "Marinha"], "Natureza-morta",
   "O gênero foi muito popular entre os pintores holandeses do século XVII.",
   "Enciclopédia Britannica – verbete 'still-life painting'")
mc(A, "música erudita", 2, 12, "Qual compositor russo criou o balé 'O Quebra-Nozes'?",
   ["Piotr Tchaikovsky", "Igor Stravinsky", "Serguei Rachmaninov", "Nikolai Rimsky-Korsakov"], "Piotr Tchaikovsky",
   "O balé estreou em 1892 e virou tradição de Natal no mundo todo.",
   "Enciclopédia Britannica – verbete 'The Nutcracker'")
mc(A, "museus", 2, 12, "Em qual cidade fica o Museu do Prado, com obras de Velázquez e Goya?",
   ["Madri", "Barcelona", "Lisboa", "Roma"], "Madri",
   "O Prado, aberto em 1819, é um dos maiores museus de pintura do mundo.",
   "Enciclopédia Britannica – verbete 'Prado Museum'")
tf(A, "arquitetura", 2, 12, "O Taj Mahal, na Índia, foi construído como túmulo para uma esposa do imperador Shah Jahan.", True,
   "O mausoléu de mármore branco homenageia Mumtaz Mahal, morta em 1631.",
   "Enciclopédia Britannica – verbete 'Taj Mahal'")
mc(A, "arquitetura", 3, 14, "Qual arquiteto catalão projetou a basílica da Sagrada Família, em Barcelona?",
   ["Antoni Gaudí", "Le Corbusier", "Frank Lloyd Wright", "Santiago Calatrava"], "Antoni Gaudí",
   "A obra começou no século XIX e continua em construção.",
   "Enciclopédia Britannica – verbete 'Antoni Gaudí'")
mc(A, "pintores", 3, 14, "Qual pintor holandês ficou famoso por quadros com linhas pretas e retângulos vermelhos, azuis e amarelos?",
   ["Piet Mondrian", "Wassily Kandinsky", "Paul Klee", "Joan Miró"], "Piet Mondrian",
   "Mondrian foi um dos líderes do movimento De Stijl, de arte abstrata geométrica.",
   "Enciclopédia Britannica – verbete 'Piet Mondrian'")
mc(A, "pintores", 3, 14, "Qual pintor espanhol pintou 'As Meninas' (1656)?",
   ["Diego Velázquez", "Francisco de Goya", "El Greco", "Bartolomé Murillo"], "Diego Velázquez",
   "No quadro, o próprio pintor aparece trabalhando diante de uma grande tela.",
   "Enciclopédia Britannica – verbete 'Las Meninas'")
mc(A, "pintores", 3, 14, "Qual pintor do Renascimento italiano pintou 'A Escola de Atenas', no Vaticano?",
   ["Rafael", "Michelangelo", "Leonardo da Vinci", "Ticiano"], "Rafael",
   "O afresco reúne filósofos gregos, como Platão e Aristóteles, no centro.",
   "Enciclopédia Britannica – verbete 'School of Athens'")
mc(A, "técnicas", 3, 14, "Como se chama a técnica de pintar com pequenos pontos de cor, usada por Georges Seurat?",
   ["Pontilhismo", "Cubismo", "Afresco", "Sfumato"], "Pontilhismo",
   "De longe, os pontos se misturam aos olhos de quem vê o quadro.",
   "Enciclopédia Britannica – verbete 'pointillism'")
mc(A, "pintores", 3, 14, "Qual pintor francês foi morar no Taiti e pintou cenas com as mulheres da ilha?",
   ["Paul Gauguin", "Paul Cézanne", "Henri Matisse", "Pierre-Auguste Renoir"], "Paul Gauguin",
   "Gauguin chegou ao Taiti em 1891 em busca de uma vida longe da Europa.",
   "Enciclopédia Britannica – verbete 'Paul Gauguin'")
tf(A, "pintores", 3, 14, "A cena 'A Criação de Adão', no teto da Capela Sistina, foi pintada por Leonardo da Vinci.", False,
   "O teto da Capela Sistina, incluindo 'A Criação de Adão', foi pintado por Michelangelo.",
   "Enciclopédia Britannica – verbete 'Sistine Chapel'")
mc(A, "música erudita", 3, 14, "Qual compositor austríaco, conhecido como 'Rei da Valsa', compôs 'O Danúbio Azul'?",
   ["Johann Strauss II", "Franz Schubert", "Joseph Haydn", "Gustav Mahler"], "Johann Strauss II",
   "A valsa de 1867 é tocada todo ano no Concerto de Ano-Novo de Viena.",
   "Enciclopédia Britannica – verbete 'Johann Strauss the Younger'")
mc(A, "arte contemporânea", 3, 14, "Qual artista brasileiro ficou famoso por retratos feitos com lixo no aterro de Gramacho, mostrados no documentário 'Lixo Extraordinário'?",
   ["Vik Muniz", "Romero Britto", "Os Gêmeos", "Hélio Oiticica"], "Vik Muniz",
   "O documentário de 2010 foi indicado ao Oscar.",
   "Enciclopédia Britannica – verbete 'Vik Muniz'", br=True)
mc(A, "escultura", 4, 16, "Qual escultor italiano do Barroco fez 'O Êxtase de Santa Teresa', em Roma?",
   ["Gian Lorenzo Bernini", "Donatello", "Antonio Canova", "Benvenuto Cellini"], "Gian Lorenzo Bernini",
   "Bernini também projetou a colunata da Praça de São Pedro.",
   "Enciclopédia Britannica – verbete 'Gian Lorenzo Bernini'")
mc(A, "escultura", 4, 16, "Qual artista criou 'Maman', escultura gigante de uma aranha de metal?",
   ["Louise Bourgeois", "Yayoi Kusama", "Georgia O'Keeffe", "Frida Kahlo"], "Louise Bourgeois",
   "A aranha homenageia a mãe da artista, que trabalhava restaurando tapeçarias.",
   "Enciclopédia Britannica – verbete 'Louise Bourgeois'")
op(A, "escultura", 4, 16, "Qual era o nome de batismo do escultor mineiro conhecido como Aleijadinho?", "Antônio Francisco Lisboa",
   ["antonio francisco lisboa", "antônio francisco lisboa", "francisco lisboa"],
   "Filho de um arquiteto português, ele é o maior nome do Barroco mineiro.",
   "Enciclopédia Britannica – verbete 'Aleijadinho'", br=True)

# =========================================================== MITOLOGIA
M = "mit"
mc(M, "mitologia grega", 1, 6, "Como se chama o gigante da mitologia grega que tem um olho só no meio da testa?",
   ["Ciclope", "Centauro", "Titã", "Minotauro"], "Ciclope",
   "Na 'Odisseia', Ulisses engana o ciclope Polifemo para fugir da caverna.",
   "Enciclopédia Britannica – verbete 'Cyclops'")
tf(M, "mitologia grega", 1, 7, "Na mitologia grega, os centauros têm corpo metade humano e metade cavalo.", True,
   "O centauro Quíron foi professor de heróis como Aquiles.",
   "Enciclopédia Britannica – verbete 'centaur'")
mc(M, "lendas europeias", 1, 8, "Qual criatura do folclore irlandês é um homenzinho que esconde um pote de ouro no fim do arco-íris?",
   ["Leprechaun", "Troll", "Gnomo", "Elfo"], "Leprechaun",
   "O leprechaun é um sapateiro encantado e é símbolo do Dia de São Patrício.",
   "Enciclopédia Britannica – verbete 'leprechaun'")
mc(M, "mitologia nórdica", 1, 8, "Qual criatura das lendas da Escandinávia vive nas montanhas e, em alguns contos, vira pedra com a luz do sol?",
   ["Troll", "Fada", "Sereia", "Fênix"], "Troll",
   "Nos contos noruegueses, os trolls são grandes, brutos e evitam a luz do dia.",
   "Enciclopédia Britannica – verbete 'troll'")
mc(M, "lendas indígenas", 2, 10, "Segundo a lenda indígena, qual alimento nasceu no lugar onde foi enterrada a menina Mani?",
   ["Mandioca", "Milho", "Guaraná", "Açaí"], "Mandioca",
   "O nome viria de 'Mani' mais 'oca', a casa onde a menina foi enterrada.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "lendas europeias", 2, 10, "Nas lendas do rei Artur, qual mago era seu conselheiro?",
   ["Merlin", "Gandalf", "Morgana", "Lancelot"], "Merlin",
   "Merlin aparece nas histórias medievais sobre Artur e Camelot.",
   "Enciclopédia Britannica – verbete 'Merlin'")
mc(M, "religiões afro-brasileiras", 2, 10, "Qual orixá é a rainha do mar, homenageada com flores na praia na virada do ano?",
   ["Iemanjá", "Oxum", "Iansã", "Nanã"], "Iemanjá",
   "Em Salvador, a grande festa de Iemanjá acontece em 2 de fevereiro.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia grega", 2, 10, "Qual rei da mitologia grega transformava em ouro tudo o que tocava?",
   ["Midas", "Minos", "Príamo", "Creso"], "Midas",
   "O dom virou maldição quando até a comida dele virava ouro.",
   "Enciclopédia Britannica – verbete 'Midas'")
mc(M, "mitologia egípcia", 2, 10, "Qual criatura com corpo de leão e cabeça humana tem uma estátua gigante em Gizé, no Egito?",
   ["Esfinge", "Grifo", "Quimera", "Mantícora"], "Esfinge",
   "A Grande Esfinge fica perto das pirâmides e tem mais de 4.500 anos.",
   "Enciclopédia Britannica – verbete 'Great Sphinx'")
mc(M, "mitologia grega", 2, 12, "Qual deus grego do vinho e das festas os romanos chamavam de Baco?",
   ["Dionísio", "Apolo", "Hermes", "Hefesto"], "Dionísio",
   "Em sua honra surgiram as festas que deram origem ao teatro grego.",
   "Enciclopédia Britannica – verbete 'Dionysus'")
mc(M, "mitologia grega", 2, 12, "Qual deus grego do fogo e dos ferreiros forjava armas para os deuses?",
   ["Hefesto", "Ares", "Apolo", "Hermes"], "Hefesto",
   "Os romanos o chamavam de Vulcano.",
   "Enciclopédia Britannica – verbete 'Hephaestus'")
mc(M, "mitologia nórdica", 2, 12, "Qual deus nórdico, pai de Thor, deu um de seus olhos em troca de sabedoria?",
   ["Odin", "Loki", "Tyr", "Balder"], "Odin",
   "Odin bebeu da fonte de Mímir depois de entregar um olho.",
   "Enciclopédia Britannica – verbete 'Odin'")
tf(M, "mitologia grega", 2, 12, "Na mitologia grega, Ícaro caiu no mar porque voou perto demais do Sol e a cera das suas asas derreteu.", True,
   "As asas de penas e cera foram feitas por seu pai, Dédalo, para fugir de Creta.",
   "Enciclopédia Britannica – verbete 'Icarus'")
mc(M, "mitologia grega", 3, 14, "Qual herói grego liderou os argonautas em busca do Velocino de Ouro?",
   ["Jasão", "Perseu", "Teseu", "Aquiles"], "Jasão",
   "Ele navegou no barco Argo e teve a ajuda da feiticeira Medeia.",
   "Enciclopédia Britannica – verbete 'Jason'")
mc(M, "mitologia egípcia", 3, 14, "Na mitologia egípcia, qual deus, marido de Ísis, governa o mundo dos mortos?",
   ["Osíris", "Rá", "Set", "Thot"], "Osíris",
   "Osíris foi morto pelo irmão Set e depois virou o juiz dos mortos.",
   "Enciclopédia Britannica – verbete 'Osiris'")
mc(M, "mitologia egípcia", 3, 14, "Qual deusa egípcia era representada como uma gata ou como uma mulher com cabeça de gata?",
   ["Bastet", "Ísis", "Hator", "Sekhmet"], "Bastet",
   "Seu principal templo ficava na cidade de Bubástis, onde gatos eram mumificados.",
   "Enciclopédia Britannica – verbete 'Bastet'")
mc(M, "mitologia nórdica", 3, 14, "Na mitologia nórdica, como se chama a grande batalha final que marca o fim do mundo dos deuses?",
   ["Ragnarök", "Valhala", "Midgard", "Asgard"], "Ragnarök",
   "No Ragnarök, Odin enfrenta o lobo Fenrir e Thor enfrenta a serpente do mundo.",
   "Enciclopédia Britannica – verbete 'Ragnarök'")
mc(M, "lendas europeias", 3, 14, "Nas lendas do rei Artur, qual cavaleiro se apaixonou pela rainha Guinevere?",
   ["Lancelot", "Galahad", "Percival", "Gawain"], "Lancelot",
   "O romance entre os dois ajudou a provocar a queda de Camelot.",
   "Enciclopédia Britannica – verbete 'Lancelot'")
mc(M, "religiões afro-brasileiras", 3, 14, "Qual orixá é o senhor dos raios, do trovão e da justiça, com um machado de duas lâminas?",
   ["Xangô", "Ogum", "Oxóssi", "Exu"], "Xangô",
   "O machado duplo de Xangô se chama oxê.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia grega", 3, 14, "Na mitologia grega, quem foi condenado a empurrar para sempre uma pedra morro acima, que sempre rola de volta?",
   ["Sísifo", "Tântalo", "Prometeu", "Atlas"], "Sísifo",
   "Por isso, um trabalho sem fim e inútil é chamado de 'trabalho de Sísifo'.",
   "Enciclopédia Britannica – verbete 'Sisyphus'")
mc(M, "mitologia asteca", 4, 16, "Na mitologia asteca, qual deus era a 'serpente emplumada'?",
   ["Quetzalcóatl", "Huitzilopochtli", "Tlaloc", "Tezcatlipoca"], "Quetzalcóatl",
   "Ele era ligado ao vento, à sabedoria e ao planeta Vênus.",
   "Enciclopédia Britannica – verbete 'Quetzalcóatl'")
op(M, "mitologia nórdica", 4, 16, "Na mitologia nórdica, como se chama o reino dos deuses, ligado ao mundo dos humanos por uma ponte de arco-íris?", "Asgard",
   ["asgard", "asgardh", "asgardr", "ásgard"],
   "A ponte de arco-íris se chama Bifrost e é vigiada pelo deus Heimdall.",
   "Enciclopédia Britannica – verbete 'Asgard'")

# =========================================================== CURIOSIDADES
C = "cur"
mc(C, "calendário", 1, 6, "Qual é o primeiro mês do ano?",
   ["Janeiro", "Fevereiro", "Março", "Dezembro"], "Janeiro",
   "O ano começa em 1º de janeiro e termina em 31 de dezembro.",
   "Observatório Nacional – Divisão Serviço da Hora", br=True)
mc(C, "calendário", 1, 6, "Quantas estações tem o ano?",
   ["4", "2", "3", "6"], "4",
   "As estações são primavera, verão, outono e inverno.",
   "Observatório Nacional")
mc(C, "objetos", 1, 7, "Qual objeto usamos para medir a temperatura do corpo quando estamos com febre?",
   ["Termômetro", "Relógio", "Balança", "Régua"], "Termômetro",
   "A temperatura normal do corpo fica por volta de 36 a 37 graus Celsius.",
   "Ministério da Saúde", br=True)
mc(C, "objetos", 1, 9, "Qual instrumento tem uma agulha que aponta para o norte e ajuda a não se perder?",
   ["Bússola", "Lupa", "Telescópio", "Cronômetro"], "Bússola",
   "A agulha imantada da bússola se alinha com o campo magnético da Terra.",
   "Enciclopédia Britannica – verbete 'compass'")
mc(C, "medidas de tempo", 1, 9, "Como se chama um período de dez anos?",
   ["Década", "Século", "Milênio", "Semestre"], "Década",
   "Dez anos formam uma década; cem anos, um século.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "jogos", 1, 9, "Quantos quadradinhos coloridos tem cada face de um cubo mágico tradicional?",
   ["9", "6", "12", "16"], "9",
   "O cubo tradicional é 3 por 3, e cada face tem nove quadradinhos.",
   "Enciclopédia Britannica – verbete 'Rubik's Cube'")
mc(C, "dinheiro", 1, 8, "Quantos centavos formam um real?",
   ["100", "10", "50", "1000"], "100",
   "O real, moeda brasileira desde 1994, é dividido em cem centavos.",
   "Banco Central do Brasil", br=True)
mc(C, "jogos", 2, 10, "Quantas cartas tem um baralho comum, sem contar os curingas?",
   ["52", "48", "54", "40"], "52",
   "São quatro naipes com 13 cartas cada.",
   "Enciclopédia Britannica – verbete 'playing card'")
mc(C, "jogos", 2, 10, "Somando os pontos de todas as faces de um dado comum de seis lados, qual é o total?",
   ["21", "18", "24", "36"], "21",
   "1 + 2 + 3 + 4 + 5 + 6 dá 21; e as faces opostas sempre somam 7.",
   "Enciclopédia Britannica – verbete 'dice'")
tf(C, "mitos populares", 2, 10, "Os morcegos são cegos.", False,
   "Morcegos enxergam; muitos também usam a ecolocalização para caçar no escuro.",
   "Enciclopédia Britannica – verbete 'bat'")
tf(C, "calendário", 2, 12, "Um ano comum tem exatamente 52 semanas, sem sobrar nenhum dia.", False,
   "52 semanas dão 364 dias, então sobra um dia num ano comum e dois num ano bissexto.",
   "Observatório Nacional")
tf(C, "mitos populares", 2, 12, "Um raio nunca cai duas vezes no mesmo lugar.", False,
   "Prédios altos, como o Empire State Building, são atingidos por raios várias vezes por ano.",
   "INPE – Grupo de Eletricidade Atmosférica (ELAT)")
tf(C, "mitos populares", 2, 12, "O peixinho-dourado tem memória de apenas três segundos.", False,
   "Experimentos mostram que esses peixes conseguem aprender e lembrar tarefas por meses.",
   "BBC Science Focus – 'Do goldfish really have a 3-second memory?'")
mc(C, "objetos", 2, 12, "O bolsinho pequeno da calça jeans foi criado originalmente para guardar o quê?",
   ["Relógio de bolso", "Moedas", "Chaves", "Fósforos"], "Relógio de bolso",
   "Segundo a Levi Strauss & Co., o bolso servia para o relógio de bolso dos trabalhadores no século XIX.",
   "Levi Strauss & Co. – história do jeans 501")
mc(C, "objetos", 2, 12, "Quantos quilates tem o ouro puro?",
   ["24", "18", "12", "30"], "24",
   "O ouro 18 quilates tem 18 partes de ouro em 24, ou seja, 75%.",
   "Enciclopédia Britannica – verbete 'karat'")
mc(C, "objetos", 2, 12, "Qual aparelho mede a pressão atmosférica e ajuda na previsão do tempo?",
   ["Barômetro", "Termômetro", "Higrômetro", "Anemômetro"], "Barômetro",
   "O higrômetro mede a umidade e o anemômetro mede a velocidade do vento.",
   "Instituto Nacional de Meteorologia (INMET)", br=True)
mc(C, "transportes", 3, 14, "Qual cidade inaugurou o primeiro metrô do mundo, em 1863?",
   ["Londres", "Paris", "Nova York", "Berlim"], "Londres",
   "A primeira linha, a Metropolitan Railway, usava locomotivas a vapor.",
   "Enciclopédia Britannica – verbete 'London Underground'")
tf(C, "monumentos", 3, 14, "A Torre Eiffel foi construída para a Exposição Universal de 1889, em Paris.", True,
   "A exposição celebrava o centenário da Revolução Francesa.",
   "Enciclopédia Britannica – verbete 'Eiffel Tower'")
op(C, "coleções", 3, 14, "Como se chama a pessoa que coleciona selos?", "Filatelista",
   ["filatelista", "filatelistas", "filatélico"],
   "A filatelia é o hobby de colecionar e estudar selos postais.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "objetos", 4, 16, "Como se chama a ponteira de plástico ou metal na ponta do cadarço?",
   ["Agulheta", "Ilhós", "Presilha", "Fivela"], "Agulheta",
   "O ilhós é o aro do furo por onde passa o cadarço; a agulheta é a ponteira que facilita enfiá-lo.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "fusos horários", 4, 16, "Contando seus territórios espalhados pelo mundo, qual país tem o maior número de fusos horários?",
   ["França", "Rússia", "Estados Unidos", "Reino Unido"], "França",
   "Com territórios ultramarinos em vários oceanos, a França usa 12 fusos horários.",
   "Enciclopédia Britannica – verbete 'time zone'")
