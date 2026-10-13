# Perguntas novas (parte 6d). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== LITERATURA
L = "lit"
mc(L, "contos de fadas", 1, 6, "Qual personagem dos contos de fadas perdeu um sapatinho de cristal no baile?",
   ["Cinderela", "Branca de Neve", "Rapunzel", "Bela Adormecida"], "Cinderela",
   "A versão mais conhecida do conto foi publicada por Charles Perrault em 1697.",
   "Enciclopédia Britannica – verbete 'Cinderella'")
mc(L, "contos de fadas", 1, 6, "Em 'Branca de Neve', quantos anões moram na casinha da floresta?",
   ["5", "6", "7", "8"], "7",
   "O conto foi registrado pelos Irmãos Grimm no início do século XIX.",
   "Enciclopédia Britannica – verbete 'Snow White'")
tf(L, "contos de fadas", 1, 7, "Na história 'João e Maria', os irmãos encontram uma casa feita de doces.", True,
   "A casa de doces é a armadilha da bruxa no conto recolhido pelos Irmãos Grimm.",
   "Enciclopédia Britannica – verbete 'Hansel and Gretel'")
op(L, "literatura infantil", 1, 7, "No Sítio do Picapau Amarelo, como se chama o porquinho guloso que ganhou título de marquês?", "Rabicó",
   ["rabico", "marques de rabico", "o rabico"],
   "Rabicó só pensa em comer e foge de qualquer perigo.",
   "Monteiro Lobato – Reinações de Narizinho", br=True)
mc(L, "contos de fadas", 1, 7, "No conto 'O Patinho Feio', em que ave o patinho se transforma ao crescer?",
   ["Cisne", "Ganso", "Galinha", "Pato"], "Cisne",
   "O conto foi publicado pelo dinamarquês Hans Christian Andersen em 1843.",
   "Enciclopédia Britannica – verbete 'The Ugly Duckling'")
mc(L, "autores estrangeiros", 1, 10, "Qual escritor dinamarquês escreveu 'A Pequena Sereia' e 'A Roupa Nova do Imperador'?",
   ["Hans Christian Andersen", "Charles Perrault", "Irmãos Grimm", "Lewis Carroll"], "Hans Christian Andersen",
   "Uma estátua da Pequena Sereia é um dos símbolos de Copenhague.",
   "Enciclopédia Britannica – verbete 'Hans Christian Andersen'")
mc(L, "personagens", 1, 9, "Na saga 'Harry Potter', qual é o nome da coruja branca de Harry?",
   ["Edwiges", "Bichento", "Perebas", "Fawkes"], "Edwiges",
   "Harry ganhou a coruja de presente de aniversário de Hagrid.",
   "J. K. Rowling – Harry Potter e a Pedra Filosofal")
mc(L, "autores estrangeiros", 2, 12, "Quem escreveu 'Os Miseráveis'?",
   ["Victor Hugo", "Alexandre Dumas", "Júlio Verne", "Charles Dickens"], "Victor Hugo",
   "O romance de 1862 acompanha o ex-prisioneiro Jean Valjean.",
   "Enciclopédia Britannica – verbete 'Les Misérables'")
tf(L, "personagens", 2, 12, "O detetive Hercule Poirot foi criado pela escritora Agatha Christie.", True,
   "Poirot é um detetive belga que estreou em 1920.",
   "Enciclopédia Britannica – verbete 'Hercule Poirot'")
mc(L, "autores brasileiros", 2, 12, "Qual escritor paraibano escreveu o 'Auto da Compadecida'?",
   ["Ariano Suassuna", "Jorge Amado", "Graciliano Ramos", "José Lins do Rego"], "Ariano Suassuna",
   "A peça de 1955 traz os amigos João Grilo e Chicó.",
   "Academia Brasileira de Letras", br=True)
mc(L, "autores brasileiros", 2, 14, "Quem escreveu o romance 'A Moreninha' (1844)?",
   ["Joaquim Manuel de Macedo", "José de Alencar", "Álvares de Azevedo", "Castro Alves"], "Joaquim Manuel de Macedo",
   "É considerado um dos primeiros romances do romantismo brasileiro.",
   "Academia Brasileira de Letras", br=True)
op(L, "personagens", 2, 12, "Em 'O Mágico de Oz', qual é o nome da menina levada por um ciclone até a terra de Oz?", "Dorothy",
   ["dorothy", "doroti", "dorothy gale"],
   "O livro de L. Frank Baum foi publicado em 1900.",
   "Enciclopédia Britannica – verbete 'The Wonderful Wizard of Oz'")
mc(L, "autores brasileiros", 2, 14, "Quem escreveu 'Macunaíma, o herói sem nenhum caráter'?",
   ["Mário de Andrade", "Oswald de Andrade", "Monteiro Lobato", "Manuel Bandeira"], "Mário de Andrade",
   "O livro de 1928 é um dos marcos do modernismo brasileiro.",
   "Enciclopédia Britannica – verbete 'Mário de Andrade'", br=True)
tf(L, "autores brasileiros", 2, 12, "O livro 'Meu Pé de Laranja Lima' foi escrito por José Mauro de Vasconcelos.", True,
   "Publicado em 1968, o livro conta a infância do menino Zezé.",
   "Enciclopédia Britannica – verbete 'José Mauro de Vasconcelos'", br=True)
mc(L, "autores brasileiros", 3, 14, "Qual poetisa goiana publicou seu primeiro livro aos 75 anos de idade?",
   ["Cora Coralina", "Cecília Meireles", "Rachel de Queiroz", "Adélia Prado"], "Cora Coralina",
   "Ela era doceira na cidade de Goiás e virou símbolo de poesia simples e forte.",
   "Museu Casa de Cora Coralina", br=True)
mc(L, "prêmios", 3, 16, "Qual escritor português ganhou o Prêmio Nobel de Literatura em 1998?",
   ["José Saramago", "Fernando Pessoa", "Eça de Queirós", "António Lobo Antunes"], "José Saramago",
   "Até hoje é o único autor de língua portuguesa premiado com o Nobel de Literatura.",
   "Fundação Nobel – nobelprize.org")
tf(L, "autores brasileiros", 3, 16, "Machado de Assis foi o primeiro presidente da Academia Brasileira de Letras.", True,
   "A Academia foi fundada em 1897, e por isso é chamada de Casa de Machado de Assis.",
   "Academia Brasileira de Letras", br=True)
mc(L, "personagens", 4, 16, "Qual é o nome e sobrenome do narrador de 'Dom Casmurro'?",
   ["Bento Santiago", "Brás Cubas", "Quincas Borba", "Pedro Rubião"], "Bento Santiago",
   "O apelido 'Dom Casmurro' foi dado a Bentinho por um vizinho.",
   "Machado de Assis – Dom Casmurro (1899)", br=True)
mc(L, "personagens", 3, 16, "Em 'Moby Dick', qual é o nome do capitão obcecado pela baleia branca?",
   ["Ahab", "Nemo", "Gancho", "Flint"], "Ahab",
   "O romance de Herman Melville foi publicado em 1851.",
   "Enciclopédia Britannica – verbete 'Moby Dick'")

# =========================================================== PORTUGUÊS
P = "por"
op(P, "antônimos", 1, 6, "Qual palavra significa o oposto de 'quente'?", "Frio",
   ["frio", "gelado"],
   "Palavras de sentido oposto são chamadas de antônimos.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "plural", 1, 7, "Uma flor, duas... Como se diz o plural de 'flor'?",
   ["Flores", "Flors", "Floris", "Florões"], "Flores",
   "Palavras terminadas em R fazem o plural com -es, como mar e mares.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "gênero", 1, 7, "Como se chama a fêmea do boi, que dá leite?",
   ["Vaca", "Boia", "Cabra", "Ovelha"], "Vaca",
   "Boi e vaca são palavras diferentes para o macho e a fêmea, os chamados heterônimos.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
tf(P, "sílabas", 1, 6, "A palavra 'sol' tem só uma sílaba.", True,
   "Palavras de uma só sílaba são chamadas de monossílabas.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "coletivos", 1, 8, "Qual é o coletivo de abelhas?",
   ["Enxame", "Cardume", "Matilha", "Manada"], "Enxame",
   "Enxame também é usado para muitos insetos voando juntos.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
op(P, "coletivos", 1, 8, "Como se chama um grupo de ovelhas?", "Rebanho",
   ["rebanho", "um rebanho", "grei"],
   "Rebanho serve para grupos de gado em geral, como ovelhas e bois.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "plural", 1, 9, "Qual é o plural de 'animal'?",
   ["Animais", "Animals", "Animales", "Animaus"], "Animais",
   "Palavras terminadas em -al trocam o L por -is no plural.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "coletivos", 2, 10, "Que nome se dá a uma grande coleção de livros organizada num só lugar?",
   ["Biblioteca", "Pinacoteca", "Constelação", "Fauna"], "Biblioteca",
   "Pinacoteca, por sua vez, é o coletivo de quadros.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "coletivos", 2, 10, "Como se chama um conjunto de ilhas próximas umas das outras?",
   ["Arquipélago", "Continente", "Península", "Cordilheira"], "Arquipélago",
   "Fernando de Noronha é um arquipélago brasileiro.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
tf(P, "sinônimos", 2, 10, "As palavras 'rápido' e 'veloz' são sinônimos.", True,
   "Sinônimos são palavras com significado igual ou parecido.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "plural", 2, 10, "Temos uma mão direita e uma esquerda; como se diz no plural?",
   ["Mãos", "Mães", "Mões", "Mãoses"], "Mãos",
   "Palavras em -ão podem fazer plural em -ãos, -ães ou -ões, e só o dicionário resolve.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "acentuação", 2, 12, "Em qual destas palavras a sílaba mais forte é a penúltima?",
   ["Mesa", "Café", "Lâmpada", "Jacaré"], "Mesa",
   "Paroxítonas têm a sílaba mais forte na penúltima posição e são as mais comuns no português.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "antônimos", 2, 12, "Qual é o antônimo de 'generoso'?",
   ["Avarento", "Bondoso", "Gentil", "Educado"], "Avarento",
   "Avarento é quem se apega ao dinheiro e não gosta de gastar nem de dividir.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "gentílicos", 2, 12, "Como é chamado quem nasce no estado do Espírito Santo?",
   ["Capixaba", "Potiguar", "Fluminense", "Candango"], "Capixaba",
   "Potiguar é quem nasce no Rio Grande do Norte, e fluminense, no estado do Rio de Janeiro.",
   "IBGE – gentílicos dos estados brasileiros", br=True)
mc(P, "significado", 2, 14, "O que significa a palavra 'efêmero'?",
   ["Passageiro", "Eterno", "Pesado", "Brilhante"], "Passageiro",
   "Vem do grego e indicava algo que dura um só dia.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem aparece em 'Ele bebeu dois copos', querendo dizer o líquido dentro deles?",
   ["Metonímia", "Metáfora", "Hipérbole", "Ironia"], "Metonímia",
   "Na metonímia, uma palavra é usada no lugar de outra com que tem relação, como o recipiente pelo conteúdo.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem imita sons, como o 'tique-taque' do relógio?",
   ["Onomatopeia", "Antítese", "Eufemismo", "Pleonasmo"], "Onomatopeia",
   "Histórias em quadrinhos usam muitas onomatopeias, como 'pow' e 'crash'.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
tf(P, "acordo ortográfico", 3, 14, "Depois do Acordo Ortográfico de 1990, a palavra 'ideia' deixou de ter acento agudo.", True,
   "Os ditongos abertos 'ei' e 'oi' das paroxítonas perderam o acento, como em 'ideia' e 'jiboia'.",
   "Vocabulário Ortográfico da Língua Portuguesa (ABL)", br=True)
tf(P, "acordo ortográfico", 3, 14, "Pelo Acordo Ortográfico de 1990, palavras como 'linguiça' e 'frequente' não levam mais trema.", True,
   "O trema só continua em nomes estrangeiros e seus derivados, como Müller e mülleriano.",
   "Vocabulário Ortográfico da Língua Portuguesa (ABL)", br=True)
mc(P, "superlativo", 3, 14, "Qual é o superlativo absoluto sintético de 'feliz'?",
   ["Felicíssimo", "Felizão", "Felizinho", "Felizmente"], "Felicíssimo",
   "O superlativo sintético usa o radical latino, felix, felicis.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)
mc(P, "plural", 4, 16, "Qual é o plural de 'qualquer'?",
   ["Quaisquer", "Qualqueres", "Quaisqueres", "Qualquers"], "Quaisquer",
   "É um caso raro: qualquer vem de qual + quer, e só o qual vai para o plural.",
   "Evanildo Bechara – Moderna Gramática Portuguesa", br=True)

# =========================================================== ARTES
A = "art"
mc(A, "materiais", 1, 6, "Qual objeto usamos para apagar o traço feito com lápis?",
   ["Borracha", "Régua", "Apontador", "Tesoura"], "Borracha",
   "Antes da borracha, as pessoas apagavam o lápis com miolo de pão.",
   "Enciclopédia Britannica – verbete 'eraser'")
tf(A, "materiais", 1, 6, "O giz de cera é um material usado para desenhar e colorir.", True,
   "O giz de cera é feito de cera misturada com pigmentos coloridos.",
   "Enciclopédia Britannica – verbete 'crayon'")
mc(A, "quadrinhos", 1, 7, "Qual personagem da Turma da Mônica é comilona e adora melancia?",
   ["Magali", "Mônica", "Marina", "Rosinha"], "Magali",
   "Magali foi inspirada em uma das filhas de Mauricio de Sousa.",
   "Mauricio de Sousa Produções", br=True)
op(A, "quadrinhos", 1, 8, "Qual é o nome do cachorro verde do Cebolinha?", "Floquinho",
   ["floquinho"],
   "Floquinho tem tanto pelo que é difícil saber onde fica a cabeça e onde fica o rabo.",
   "Mauricio de Sousa Produções", br=True)
mc(A, "pintura", 1, 9, "Como se chama o quadro em que o artista pinta a si mesmo?",
   ["Autorretrato", "Paisagem", "Natureza-morta", "Caricatura"], "Autorretrato",
   "Van Gogh pintou mais de 30 autorretratos.",
   "Enciclopédia Britannica – verbete 'self-portrait'")
tf(A, "dança", 1, 9, "No balé clássico, as bailarinas costumam dançar na ponta dos pés com sapatilhas especiais.", True,
   "As sapatilhas de ponta têm a frente reforçada para sustentar o peso da bailarina.",
   "Enciclopédia Britannica – verbete 'ballet'")
mc(A, "escultura", 2, 12, "Qual estátua de Michelangelo representa o jovem que venceu o gigante Golias?",
   ["Davi", "Moisés", "Pietà", "O Pensador"], "Davi",
   "A estátua de mármore, com mais de 5 metros, fica em Florença.",
   "Galleria dell'Accademia di Firenze")
mc(A, "pintura", 2, 12, "Quem pintou 'O Nascimento de Vênus'?",
   ["Sandro Botticelli", "Rafael", "Caravaggio", "Ticiano"], "Sandro Botticelli",
   "O quadro mostra a deusa chegando à praia sobre uma concha.",
   "Galleria degli Uffizi")
mc(A, "escultura", 2, 12, "Qual famosa estátua grega sem braços está exposta no Museu do Louvre?",
   ["Vênus de Milo", "Discóbolo", "Davi", "Pietà"], "Vênus de Milo",
   "Ela foi encontrada em 1820 na ilha grega de Milos.",
   "Museu do Louvre")
mc(A, "pintura", 2, 12, "Qual artista ficou famoso por pintar latas de sopa Campbell's?",
   ["Andy Warhol", "Roy Lichtenstein", "Jackson Pollock", "Keith Haring"], "Andy Warhol",
   "Warhol foi um dos principais nomes da pop art.",
   "Museum of Modern Art (MoMA)")
tf(A, "monumentos", 2, 12, "O Cristo Redentor, no Rio de Janeiro, foi inaugurado em 1931.", True,
   "A estátua tem 30 metros de altura, sem contar o pedestal.",
   "Santuário Cristo Redentor", br=True)
mc(A, "escultura", 2, 14, "Qual escultor mineiro do século XVIII esculpiu os Doze Profetas de Congonhas?",
   ["Aleijadinho", "Mestre Valentim", "Victor Brecheret", "Bruno Giorgi"], "Aleijadinho",
   "Antônio Francisco Lisboa é o maior nome do barroco mineiro.",
   "IPHAN – Santuário do Bom Jesus de Matosinhos", br=True)
op(A, "técnicas", 3, 14, "Como se chama a pintura feita sobre reboco ainda úmido, técnica do teto da Capela Sistina?", "Afresco",
   ["afresco", "fresco", "pintura a fresco"],
   "A tinta é absorvida pela parede enquanto ela seca, por isso a pintura dura séculos.",
   "Enciclopédia Britannica – verbete 'fresco painting'")
mc(A, "pintura", 3, 14, "Qual pintor holandês pintou 'Moça com Brinco de Pérola'?",
   ["Johannes Vermeer", "Rembrandt", "Vincent van Gogh", "Piet Mondrian"], "Johannes Vermeer",
   "O quadro fica no museu Mauritshuis, em Haia.",
   "Mauritshuis")
mc(A, "pintura", 3, 14, "Qual pintor francês é famoso pelos quadros de bailarinas?",
   ["Edgar Degas", "Paul Cézanne", "Henri Matisse", "Paul Gauguin"], "Edgar Degas",
   "Degas também fez a escultura 'Pequena Bailarina de Catorze Anos'.",
   "Musée d'Orsay")
mc(A, "arte brasileira", 3, 14, "Qual pintora brasileira teve sua exposição de 1917 duramente criticada por Monteiro Lobato?",
   ["Anita Malfatti", "Tarsila do Amaral", "Djanira", "Tomie Ohtake"], "Anita Malfatti",
   "A polêmica do artigo 'Paranoia ou Mistificação' ajudou a preparar a Semana de 1922.",
   "Enciclopédia Itaú Cultural – verbete 'Anita Malfatti'", br=True)
tf(A, "pintura", 3, 14, "'A Ronda Noturna' é uma obra famosa do pintor holandês Rembrandt.", True,
   "O enorme quadro de 1642 está no Rijksmuseum, em Amsterdã.",
   "Rijksmuseum")
tf(A, "pintura", 3, 14, "Vincent van Gogh vendeu centenas de quadros enquanto estava vivo.", False,
   "Van Gogh vendeu pouquíssimos quadros em vida e só ficou famoso depois de morrer.",
   "Museu Van Gogh – Amsterdã")
mc(A, "movimentos", 3, 16, "Qual movimento artístico ganhou nome por causa de um quadro de Monet que mostra o nascer do sol?",
   ["Impressionismo", "Expressionismo", "Surrealismo", "Realismo"], "Impressionismo",
   "Um crítico usou o título 'Impressão, Nascer do Sol' para zombar dos pintores, e o nome pegou.",
   "Musée Marmottan Monet")
mc(A, "museus", 4, 16, "Em qual museu de Madri está exposta a 'Guernica', de Picasso?",
   ["Museu Reina Sofia", "Museu do Prado", "Museu Thyssen-Bornemisza", "Museu Guggenheim"], "Museu Reina Sofia",
   "O quadro só chegou à Espanha em 1981, depois do fim da ditadura de Franco.",
   "Museo Nacional Centro de Arte Reina Sofía")

# =========================================================== MITOLOGIA
M = "mit"
mc(M, "lendas", 1, 6, "Qual criatura das lendas é um homem que vira lobo?",
   ["Lobisomem", "Vampiro", "Centauro", "Duende"], "Lobisomem",
   "A lenda do lobisomem existe em vários países e chegou ao Brasil com os portugueses.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(M, "folclore", 1, 7, "Qual bruxa com cabeça de jacaré é vilã no Sítio do Picapau Amarelo?", "Cuca",
   ["cuca", "a cuca"],
   "A Cuca também aparece na cantiga de ninar 'Nana, nenê, que a Cuca vem pegar'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia grega", 1, 10, "Na mitologia grega, quem é a deusa do amor e da beleza?",
   ["Afrodite", "Atena", "Ártemis", "Deméter"], "Afrodite",
   "Os romanos a chamavam de Vênus.",
   "Enciclopédia Britannica – verbete 'Aphrodite'")
mc(M, "mitologia grega", 2, 12, "Qual herói grego cortou a cabeça da Medusa?",
   ["Perseu", "Teseu", "Jasão", "Hércules"], "Perseu",
   "Perseu olhou a Medusa pelo reflexo do escudo para não virar pedra.",
   "Enciclopédia Britannica – verbete 'Perseus'")
mc(M, "mitologia romana", 2, 12, "Qual deus romano corresponde a Ares, o deus grego da guerra?",
   ["Marte", "Mercúrio", "Saturno", "Vulcano"], "Marte",
   "O mês de março recebeu esse nome em homenagem a Marte.",
   "Enciclopédia Britannica – verbete 'Mars'")
mc(M, "folclore", 2, 10, "Qual lenda indígena conta que uma fruta nasceu dos olhos de um menino?",
   ["Guaraná", "Açaí", "Cupuaçu", "Mandioca"], "Guaraná",
   "Segundo a lenda dos Sateré-Mawé, a fruta parece um olho por causa disso.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(M, "folclore", 2, 12, "Segundo a lenda indígena, a vitória-régia era uma moça que se apaixonou pela Lua.", True,
   "A moça, chamada Naiá, se afogou ao tentar alcançar o reflexo da Lua no rio.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "folclore", 2, 12, "Qual lenda gaúcha fala de um menino escravizado que, depois de morrer, ajuda a achar objetos perdidos?",
   ["Negrinho do Pastoreio", "Saci-Pererê", "Boto cor-de-rosa", "Curupira"], "Negrinho do Pastoreio",
   "Quem perde algo acende uma vela para o Negrinho pedindo ajuda.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia grega", 2, 12, "Qual deus grego é o mensageiro dos deuses e usa sandálias com asas?",
   ["Hermes", "Apolo", "Dionísio", "Hefesto"], "Hermes",
   "Os romanos o chamavam de Mercúrio.",
   "Enciclopédia Britannica – verbete 'Hermes'")
op(M, "mitologia romana", 2, 12, "Qual é o nome romano de Poseidon, o deus grego dos mares?", "Netuno",
   ["netuno"],
   "O planeta Netuno, descoberto em 1846, também recebeu o nome desse deus.",
   "Enciclopédia Britannica – verbete 'Neptune'")
mc(M, "mitologia grega", 2, 12, "Na mitologia grega, quem é a deusa da caça, irmã gêmea de Apolo?",
   ["Ártemis", "Atena", "Deméter", "Héstia"], "Ártemis",
   "Os romanos a chamavam de Diana.",
   "Enciclopédia Britannica – verbete 'Artemis'")
mc(M, "mitologia grega", 2, 12, "Qual deusa grega é esposa de Zeus e rainha dos deuses?",
   ["Hera", "Afrodite", "Perséfone", "Gaia"], "Hera",
   "Hera era a protetora do casamento.",
   "Enciclopédia Britannica – verbete 'Hera'")
tf(M, "mitologia grega", 2, 12, "Na mitologia grega, Narciso se apaixonou pelo próprio reflexo na água.", True,
   "Do mito vem a palavra 'narcisista', para quem é apaixonado por si mesmo.",
   "Enciclopédia Britannica – verbete 'Narcissus'")
op(M, "mitologia grega", 2, 12, "Qual cão de três cabeças guarda a entrada do mundo dos mortos na mitologia grega?", "Cérbero",
   ["cerbero", "cérbero"],
   "Capturar o cão foi o último dos doze trabalhos de Hércules.",
   "Enciclopédia Britannica – verbete 'Cerberus'")
tf(M, "mitologia grega", 2, 12, "Na mitologia grega, Zeus e Hades são irmãos.", True,
   "Os dois são filhos do titã Cronos, assim como Poseidon.",
   "Enciclopédia Britannica – verbete 'Hades'")
mc(M, "folclore", 3, 14, "Qual protetora das matas do folclore brasileiro anda montada num porco-do-mato?",
   ["Caipora", "Iara", "Cuca", "Mula sem cabeça"], "Caipora",
   "Os caçadores deixavam fumo para a Caipora para ter sorte na caça.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia egípcia", 3, 14, "Na mitologia egípcia, qual deus com cabeça de falcão é filho de Ísis e Osíris?",
   ["Hórus", "Anúbis", "Seth", "Tot"], "Hórus",
   "O 'olho de Hórus' era um amuleto de proteção no Egito antigo.",
   "Enciclopédia Britannica – verbete 'Horus'")
mc(M, "mitologia grega", 3, 14, "Na mitologia grega, qual barqueiro leva as almas pelo rio dos mortos?",
   ["Caronte", "Ícaro", "Orfeu", "Tântalo"], "Caronte",
   "Os gregos punham uma moeda com o morto para pagar a travessia.",
   "Enciclopédia Britannica – verbete 'Charon'")
mc(M, "mitologia grega", 3, 14, "Qual ciclope prende Ulisses e seus homens numa caverna na 'Odisseia'?",
   ["Polifemo", "Argos", "Tifão", "Talos"], "Polifemo",
   "Ulisses disse que se chamava 'Ninguém' para enganar o ciclope.",
   "Homero – Odisseia, canto IX")
mc(M, "mitologia nórdica", 4, 16, "Na mitologia nórdica, qual é o nome da árvore gigante que liga os nove mundos?",
   ["Yggdrasil", "Bifrost", "Asgard", "Midgard"], "Yggdrasil",
   "Bifrost, por sua vez, é a ponte de arco-íris que leva a Asgard.",
   "Enciclopédia Britannica – verbete 'Yggdrasill'")

# =========================================================== CURIOSIDADES
C = "cur"
mc(C, "números", 1, 6, "Quantos dedos temos somando as duas mãos?",
   ["8", "10", "12", "20"], "10",
   "Muitos acreditam que contamos de dez em dez justamente por causa dos dedos.",
   "Enciclopédia Britannica – verbete 'decimal number system'")
mc(C, "estações", 1, 6, "Qual estação do ano é a mais fria?",
   ["Inverno", "Verão", "Primavera", "Outono"], "Inverno",
   "No Brasil, o inverno começa em junho.",
   "Observatório Nacional", br=True)
mc(C, "números", 1, 6, "Quantas rodas tem um triciclo?",
   ["3", "2", "4", "5"], "3",
   "O prefixo 'tri' significa três, como em triângulo.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "números", 1, 6, "Quantas rodas tem uma bicicleta?",
   ["2", "3", "4", "1"], "2",
   "O prefixo 'bi' significa dois.",
   "Enciclopédia Britannica – verbete 'bicycle'")
tf(C, "números", 1, 7, "Uma dúzia tem 12 unidades.", True,
   "Meia dúzia, portanto, são 6 unidades.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "países", 1, 9, "Qual país europeu tem o formato de uma bota no mapa?",
   ["Itália", "Espanha", "Portugal", "Grécia"], "Itália",
   "A ilha da Sicília parece a bola que a bota está chutando.",
   "Enciclopédia Britannica – verbete 'Italy'")
tf(C, "mitos", 2, 10, "O avestruz enterra a cabeça na areia quando sente medo.", False,
   "É um mito: o ninho é um buraco raso no chão, e o avestruz abaixa a cabeça para virar os ovos com o bico.",
   "National Geographic – verbete 'ostrich'")
mc(C, "aviação", 2, 12, "Qual é a cor da 'caixa-preta' dos aviões?",
   ["Laranja", "Preta", "Azul", "Branca"], "Laranja",
   "A cor forte ajuda as equipes a encontrá-la depois de um acidente.",
   "Enciclopédia Britannica – verbete 'flight recorder'")
tf(C, "mitos", 2, 12, "A Grande Muralha da China pode ser vista a olho nu da Lua.", False,
   "Da Lua, nenhuma construção humana é visível a olho nu.",
   "NASA – 'China's Wall Less Great in View from Space'")
mc(C, "comunicação", 2, 12, "Qual é o famoso pedido de socorro em código Morse?",
   ["SOS", "SAS", "OSO", "SSS"], "SOS",
   "Em Morse ele é três pontos, três traços e três pontos.",
   "Enciclopédia Britannica – verbete 'SOS'")
op(C, "moedas", 2, 12, "Qual é o nome da moeda do Japão?", "Iene",
   ["iene", "yen", "iene japonês"],
   "O símbolo do iene é ¥.",
   "Banco do Japão")
mc(C, "medos", 2, 12, "Qual palavra indica o medo exagerado de lugares altos?",
   ["Acrofobia", "Claustrofobia", "Hidrofobia", "Agorafobia"], "Acrofobia",
   "Vem do grego 'akros', que quer dizer alto.",
   "Dicionário Houaiss da Língua Portuguesa")
tf(C, "geografia", 2, 12, "O Monte Everest é a montanha mais alta do mundo medida a partir do nível do mar.", True,
   "Ele tem cerca de 8.849 metros de altitude.",
   "Enciclopédia Britannica – verbete 'Mount Everest'")
mc(C, "símbolos", 3, 14, "Como se chama o sinal que parece um e enrolado, usado em nomes de empresas no lugar da palavra e?",
   ["E comercial", "Cerquilha", "Asterisco", "Til"], "E comercial",
   "O sinal nasceu da junção das letras 'e' e 't' da palavra latina 'et'.",
   "Dicionário Houaiss da Língua Portuguesa")
op(C, "símbolos", 3, 14, "Qual é o nome registrado nos dicionários para o sinal chamado popularmente de jogo da velha?", "Cerquilha",
   ["cerquilha", "cardinal"],
   "Nas redes sociais, o sinal ficou famoso como 'hashtag'.",
   "Dicionário Houaiss da Língua Portuguesa")
mc(C, "invenções", 3, 14, "Segundo a tradição, em qual país o papel foi inventado, por volta do ano 105?",
   ["China", "Egito", "Grécia", "Índia"], "China",
   "A invenção é atribuída ao funcionário da corte chinesa Cai Lun.",
   "Enciclopédia Britannica – verbete 'paper'")
mc(C, "números", 4, 16, "Como se chama o número 1 seguido de 100 zeros?",
   ["Googol", "Googolplex", "Quintilhão", "Infinito"], "Googol",
   "O nome do Google foi inspirado nessa palavra.",
   "Enciclopédia Britannica – verbete 'googol'")
