# Perguntas novas (parte 8d). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== LITERATURA
L = "lit"
mc(L, "contos de fadas", 1, 6, "Na história 'João e o Pé de Feijão', o que João recebe em troca da vaca da família?",
   ["Feijões mágicos", "Um saco de moedas", "Um cavalo", "Um cesto de pães"], "Feijões mágicos",
   "Dos feijões nasce um pé enorme que leva João até o castelo de um gigante.",
   "Enciclopédia Britannica – verbete 'Jack and the Beanstalk'")
mc(L, "fábulas", 1, 6, "Na fábula de Esopo, qual animal pequeno rói a rede e liberta o leão preso?",
   ["Rato", "Coelho", "Passarinho", "Esquilo"], "Rato",
   "O leão tinha poupado o ratinho, que depois retribuiu o favor roendo as cordas da rede.",
   "Enciclopédia Britannica – verbete 'Aesop'")
mc(L, "clássicos infantis", 1, 7, "Qual é o nome do velho carpinteiro que constrói o boneco Pinóquio?",
   ["Gepeto", "Estrômboli", "Fagundes", "Tobias"], "Gepeto",
   "No livro de Carlo Collodi, Gepeto esculpe o boneco num pedaço de madeira que fala.",
   "Carlo Collodi – As Aventuras de Pinóquio")
tf(L, "contos de fadas", 1, 7, "No conto de Hans Christian Andersen, o soldadinho de chumbo tem uma perna só.", True,
   "O último soldadinho feito da colher de chumbo ficou com uma perna só porque o metal acabou.",
   "Hans Christian Andersen – O Soldadinho de Chumbo")
tf(L, "contos de fadas", 1, 8, "No conto 'Os Músicos de Bremen', dos Irmãos Grimm, os animais que viajam juntos são um burro, um cachorro, um gato e um galo.", True,
   "Os quatro animais, rejeitados pelos donos, partem para Bremen para virar músicos.",
   "Irmãos Grimm – Contos da Infância e do Lar")
tf(L, "autores estrangeiros", 1, 10, "O livro 'A Volta ao Mundo em 80 Dias' foi escrito por Júlio Verne.", True,
   "No romance, Phileas Fogg aposta que consegue dar a volta ao mundo em 80 dias.",
   "Enciclopédia Britannica – verbete 'Around the World in Eighty Days'")
mc(L, "literatura popular", 2, 10, "Como se chama a poesia popular nordestina vendida em folhetos pendurados em barbantes nas feiras?",
   ["Literatura de cordel", "Haicai", "Crônica", "Soneto"], "Literatura de cordel",
   "O nome vem dos cordões em que os folhetos ficavam expostos para venda.",
   "IPHAN – Literatura de Cordel, Patrimônio Cultural do Brasil", br=True)
mc(L, "literatura infantil", 2, 10, "Qual escritora brasileira escreveu 'Marcelo, Marmelo, Martelo'?",
   ["Ruth Rocha", "Ana Maria Machado", "Cecília Meireles", "Tatiana Belinky"], "Ruth Rocha",
   "O livro conta a história de um menino que resolve inventar novos nomes para as coisas.",
   "Enciclopédia Itaú Cultural – verbete 'Ruth Rocha'", br=True)
mc(L, "literatura infantil", 2, 10, "Qual escritora brasileira escreveu 'Menina Bonita do Laço de Fita'?",
   ["Ana Maria Machado", "Ruth Rocha", "Lygia Bojunga", "Sylvia Orthof"], "Ana Maria Machado",
   "Ana Maria Machado é membro da Academia Brasileira de Letras e uma das maiores autoras infantis do país.",
   "Academia Brasileira de Letras", br=True)
mc(L, "poesia", 2, 12, "Qual poeta brasileira escreveu o livro infantil de poemas 'Ou Isto ou Aquilo'?",
   ["Cecília Meireles", "Cora Coralina", "Adélia Prado", "Rachel de Queiroz"], "Cecília Meireles",
   "O livro reúne poemas para crianças com brincadeiras de sons e palavras.",
   "Enciclopédia Itaú Cultural – verbete 'Cecília Meireles'", br=True)
mc(L, "clássicos mundiais", 2, 12, "Quem escreveu 'Robinson Crusoé', sobre um náufrago que vive anos numa ilha?",
   ["Daniel Defoe", "Jonathan Swift", "Charles Dickens", "Walter Scott"], "Daniel Defoe",
   "O romance do escritor inglês foi publicado em 1719.",
   "Enciclopédia Britannica – verbete 'Daniel Defoe'")
mc(L, "clássicos mundiais", 2, 12, "Qual escritor irlandês escreveu o romance 'Drácula', sobre o famoso conde vampiro?",
   ["Bram Stoker", "Edgar Allan Poe", "Mary Shelley", "Oscar Wilde"], "Bram Stoker",
   "O livro, escrito em forma de cartas e diários, foi publicado em 1897.",
   "Enciclopédia Britannica – verbete 'Bram Stoker'")
mc(L, "clássicos mundiais", 2, 12, "Qual escritor escocês escreveu 'A Ilha do Tesouro', com o pirata Long John Silver?",
   ["Robert Louis Stevenson", "Rudyard Kipling", "Jack London", "Herman Melville"], "Robert Louis Stevenson",
   "Stevenson também escreveu 'O Médico e o Monstro'.",
   "Enciclopédia Britannica – verbete 'Robert Louis Stevenson'")
mc(L, "clássicos mundiais", 2, 12, "Em 'As Viagens de Gulliver', como se chama o país onde as pessoas são minúsculas?",
   ["Lilipute", "Brobdingnag", "Terra do Nunca", "Nárnia"], "Lilipute",
   "No livro de Jonathan Swift, os liliputianos têm poucos centímetros de altura.",
   "Enciclopédia Britannica – verbete 'Gulliver's Travels'")
mc(L, "clássicos mundiais", 2, 12, "Qual poema épico atribuído a Homero conta episódios da Guerra de Troia e a fúria de Aquiles?",
   ["Ilíada", "Odisseia", "Eneida", "Teogonia"], "Ilíada",
   "O nome vem de Ílion, outro nome da cidade de Troia.",
   "Enciclopédia Britannica – verbete 'Iliad'")
mc(L, "autores brasileiros", 2, 12, "Qual escritor cearense escreveu o romance 'O Guarani', com o herói indígena Peri?",
   ["José de Alencar", "Gonçalves Dias", "Machado de Assis", "Bernardo Guimarães"], "José de Alencar",
   "O romance de 1857 é um dos marcos do indianismo romântico brasileiro.",
   "Academia Brasileira de Letras", br=True)
tf(L, "prêmios literários", 2, 14, "O Prêmio Camões, criado por Brasil e Portugal, homenageia autores de língua portuguesa.", True,
   "Criado em 1988, é considerado o prêmio literário mais importante da língua portuguesa.",
   "Fundação Biblioteca Nacional – Prêmio Camões")
mc(L, "literatura popular", 3, 14, "Qual técnica de gravura, feita com uma matriz de madeira entalhada, ilustra muitas capas de folhetos de cordel?",
   ["Xilogravura", "Litogravura", "Serigrafia", "Aquarela"], "Xilogravura",
   "O artista entalha o desenho na madeira, passa tinta e carimba o papel.",
   "IPHAN – Literatura de Cordel, Patrimônio Cultural do Brasil", br=True)
op(L, "literatura popular", 3, 14, "Qual poeta popular cearense, autor de 'A Triste Partida', ficou conhecido pelo nome de um passarinho?",
   "Patativa do Assaré", ["patativa do assare", "patativa do assaré", "patativa", "antonio goncalves da silva", "antônio gonçalves da silva"],
   "Antônio Gonçalves da Silva ganhou o apelido comparado ao canto da ave patativa.",
   "Enciclopédia Itaú Cultural – verbete 'Patativa do Assaré'", br=True)
op(L, "autores brasileiros", 3, 14, "Qual escritora mineira contou sua vida na favela do Canindé, em São Paulo, no livro 'Quarto de Despejo'?",
   "Carolina Maria de Jesus", ["carolina maria de jesus", "carolina de jesus"],
   "O diário, publicado em 1960, foi traduzido para muitos idiomas.",
   "Enciclopédia Itaú Cultural – verbete 'Carolina Maria de Jesus'", br=True)
tf(L, "clássicos mundiais", 3, 14, "No livro de Mary Shelley, Frankenstein é o nome do cientista, e não da criatura que ele cria.", True,
   "Victor Frankenstein é o cientista; a criatura não recebe nome no romance.",
   "Enciclopédia Britannica – verbete 'Frankenstein'")
mc(L, "clássicos mundiais", 3, 14, "Qual poeta italiano escreveu 'A Divina Comédia', uma viagem pelo Inferno, Purgatório e Paraíso?",
   ["Dante Alighieri", "Giovanni Boccaccio", "Francesco Petrarca", "Nicolau Maquiavel"], "Dante Alighieri",
   "O poema, escrito no século XIV, é um dos marcos da língua italiana.",
   "Enciclopédia Britannica – verbete 'Divine Comedy'")
mc(L, "autores africanos", 3, 16, "Qual escritor moçambicano escreveu o romance 'Terra Sonâmbula'?",
   ["Mia Couto", "Pepetela", "José Eduardo Agualusa", "Paulina Chiziane"], "Mia Couto",
   "O romance de 1992 se passa durante a guerra civil de Moçambique.",
   "Enciclopédia Britannica – verbete 'Mia Couto'")
mc(L, "autores africanos", 4, 16, "Qual escritor angolano, autor de 'Mayombe', recebeu o Prêmio Camões em 1997?",
   ["Pepetela", "Mia Couto", "Luandino Vieira", "Ondjaki"], "Pepetela",
   "Pepetela é o nome de guerra de Artur Pestana, que lutou pela independência de Angola.",
   "Fundação Biblioteca Nacional – Prêmio Camões")
mc(L, "clássicos mundiais", 4, 16, "Em 'A Divina Comédia', qual poeta romano guia Dante pelo Inferno e pelo Purgatório?",
   ["Virgílio", "Homero", "Ovídio", "Horácio"], "Virgílio",
   "Dante escolheu como guia o autor da 'Eneida', que admirava muito.",
   "Enciclopédia Britannica – verbete 'Divine Comedy'")

# =========================================================== PORTUGUÊS
P = "por"
mc(P, "antônimos", 1, 6, "Qual é a palavra de sentido oposto a 'abrir'?",
   ["Fechar", "Pular", "Comer", "Correr"], "Fechar",
   "Abrimos e fechamos portas, janelas e caixas.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "alfabeto", 1, 6, "No alfabeto, qual letra vem logo depois do A?",
   ["B", "C", "D", "E"], "B",
   "O alfabeto começa com A, B, C, D, E.", "Academia Brasileira de Letras – VOLP")
mc(P, "diminutivo", 1, 6, "Um gato bem pequenininho é chamado de quê?",
   ["Gatinho", "Gatão", "Gataria", "Gatuno"], "Gatinho",
   "O sufixo '-inho' forma o diminutivo, que indica tamanho pequeno.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "gênero", 1, 7, "O homem que atua em novelas e filmes é o ator; e a mulher, como se chama?",
   ["Atriz", "Atora", "Atoriz", "Atrice"], "Atriz",
   "Ator e atriz formam um par de masculino e feminino com terminações diferentes.", "Dicionário Houaiss da Língua Portuguesa")
tf(P, "sinônimos", 1, 8, "A palavra 'garoto' quer dizer o mesmo que 'menino'.", True,
   "Garoto e menino são sinônimos: palavras com sentido parecido.", "Dicionário Houaiss da Língua Portuguesa")
op(P, "ortografia", 1, 9, "Como se chama o sinal gráfico que aparece sobre o A nas palavras 'mãe' e 'pão'?", "Til",
   ["til"],
   "O til indica que a vogal tem som nasal.", "Academia Brasileira de Letras – VOLP")
op(P, "coletivos", 2, 10, "Como se chama um grupo de cães?", "Matilha",
   ["matilha", "cainçalha", "caincalha"],
   "Matilha é o coletivo de cães, especialmente os de caça; cainçalha também é aceito.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "antônimos", 2, 10, "Qual palavra tem sentido contrário a 'aceitar'?",
   ["Recusar", "Receber", "Aprovar", "Concordar"], "Recusar",
   "Quem recusa não aceita algo que foi oferecido.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "ditados", 2, 10, "Qual é o final do ditado 'Em boca fechada'?",
   ["Não entra mosca", "Não cabe comida", "Ninguém escuta", "Não sai palavra"], "Não entra mosca",
   "O ditado aconselha a ficar calado para evitar problemas.", "Câmara Cascudo – Locuções Tradicionais no Brasil")
mc(P, "expressões idiomáticas", 2, 12, "O que significa a expressão 'chutar o balde'?",
   ["Desistir de tudo", "Ter muita sorte", "Fazer faxina", "Mudar de casa"], "Desistir de tudo",
   "Chutar o balde é largar tudo, geralmente por perder a paciência.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "expressões idiomáticas", 2, 12, "Quando se diz que algo custou os olhos da cara, o que isso quer dizer?",
   ["Que foi muito caro", "Que foi muito feio", "Que foi muito rápido", "Que foi de graça"], "Que foi muito caro",
   "A expressão compara o preço a algo tão valioso quanto os próprios olhos.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "sinônimos", 2, 12, "Qual é um sinônimo de 'gélido'?",
   ["Gelado", "Quente", "Molhado", "Escuro"], "Gelado",
   "Gélido é aquilo que está muito frio, como gelo.", "Dicionário Houaiss da Língua Portuguesa")
mc(P, "classes de palavras", 2, 12, "Na frase 'Ela correu rapidamente', qual é a classe da palavra 'rapidamente'?",
   ["Advérbio", "Adjetivo", "Verbo", "Substantivo"], "Advérbio",
   "O advérbio modifica o verbo, indicando aqui o modo como ela correu.", "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "classes de palavras", 2, 12, "Na frase 'Nós fomos à praia', a palavra 'nós' pertence a qual classe?",
   ["Pronome", "Verbo", "Advérbio", "Substantivo"], "Pronome",
   "'Nós' é pronome pessoal da primeira pessoa do plural.", "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "sintaxe", 2, 12, "Como se chama o termo da oração sobre o qual se declara algo, como 'O cachorro' em 'O cachorro latiu'?",
   ["Sujeito", "Predicado", "Objeto direto", "Vocativo"], "Sujeito",
   "O sujeito é o termo de que se fala; o predicado é o que se diz dele.", "Evanildo Bechara – Moderna Gramática Portuguesa")
mc(P, "regência", 3, 14, "Pela norma-padrão, qual palavra completa a frase 'Prefiro suco ___ refrigerante'?",
   ["a", "do que", "que", "mais que"], "a",
   "Na norma-padrão, quem prefere, prefere uma coisa a outra.", "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "regência", 3, 14, "Pela norma-padrão, no sentido de ver, como se completa a frase 'Ontem eu assisti ___ jogo'?",
   ["ao", "o", "no", "com o"], "ao",
   "No sentido de ver, a norma-padrão pede 'assistir a': assisti ao jogo.", "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "antônimos", 3, 14, "Qual é o antônimo de 'escasso'?",
   ["Abundante", "Raro", "Pequeno", "Pouco"], "Abundante",
   "Escasso é o que existe em pouca quantidade; abundante, o que existe em grande quantidade.", "Dicionário Houaiss da Língua Portuguesa")
tf(P, "acentuação", 3, 14, "Pelo Acordo Ortográfico de 1990, a palavra 'voo', do avião, continua com acento circunflexo.", False,
   "O acordo tirou o circunflexo das palavras terminadas em 'oo', como voo e enjoo.", "Academia Brasileira de Letras – VOLP")
tf(P, "acentuação", 3, 14, "A palavra 'paralelepípedo' é proparoxítona, com a sílaba mais forte na antepenúltima posição.", True,
   "A sílaba tônica é 'pí' (pa-ra-le-le-pí-pe-do), por isso a palavra leva acento.", "Academia Brasileira de Letras – VOLP")
op(P, "gentílicos", 4, 16, "Como se chama quem nasce na cidade de Salvador, na Bahia?", "Soteropolitano",
   ["soteropolitano", "soteropolitana", "soteropolitanos"],
   "O nome vem do grego 'Soterópolis', cidade do Salvador.", "Dicionário Houaiss da Língua Portuguesa", br=True)
mc(P, "parônimos", 4, 16, "Qual verbo significa 'corrigir', como quando se corrige um documento com erro?",
   ["Retificar", "Ratificar", "Ratear", "Relatar"], "Retificar",
   "Retificar é corrigir; ratificar, com A, é confirmar.", "Dicionário Houaiss da Língua Portuguesa")

# =========================================================== ARTES
A = "art"
mc(A, "fotografia", 1, 6, "Como se chama a pessoa que tira fotografias como profissão?",
   ["Fotógrafo", "Pintor", "Escultor", "Desenhista"], "Fotógrafo",
   "O fotógrafo registra imagens com a câmera.", "Dicionário Houaiss da Língua Portuguesa")
mc(A, "teatro", 1, 6, "Como se chama o lugar do teatro onde os atores se apresentam para o público?",
   ["Palco", "Plateia", "Bilheteria", "Camarim"], "Palco",
   "O público fica na plateia e assiste aos atores no palco.", "Dicionário Houaiss da Língua Portuguesa")
mc(A, "arte de rua", 1, 7, "Como se chama a arte de rua feita com tinta spray em muros da cidade?",
   ["Grafite", "Aquarela", "Mosaico", "Origami"], "Grafite",
   "O grafite transforma muros e paredes em grandes painéis coloridos.", "Enciclopédia Itaú Cultural – verbete 'Grafite'")
tf(A, "teatro", 1, 8, "Os mímicos se apresentam usando gestos e expressões do rosto, sem falar.", True,
   "A mímica conta histórias apenas com o corpo, sem palavras.", "Enciclopédia Britannica – verbete 'Mime and pantomime'")
mc(A, "teatro", 1, 8, "Como se chama o boneco de teatro movido por fios presos a uma cruz de madeira?",
   ["Marionete", "Fantoche", "Espantalho", "Manequim"], "Marionete",
   "A marionete é movida de cima, por fios; o fantoche é vestido na mão.", "Enciclopédia Britannica – verbete 'Puppetry'")
mc(A, "arte rupestre", 1, 9, "Como se chamam as pinturas feitas pelos povos pré-históricos em paredes de cavernas e rochas?",
   ["Arte rupestre", "Arte barroca", "Arte gótica", "Arte digital"], "Arte rupestre",
   "Rupestre vem do latim 'rupes', que quer dizer rocha.", "Enciclopédia Britannica – verbete 'Rock art'")
op(A, "desenho", 2, 10, "Como se chama o desenho de uma pessoa com traços exagerados de propósito, para fazer graça?", "Caricatura",
   ["caricatura", "caricaturas"],
   "A caricatura exagera nariz, orelhas e outros traços marcantes da pessoa.", "Enciclopédia Britannica – verbete 'Caricature'")
mc(A, "dança", 2, 10, "O flamenco, dança com palmas, sapateado e violão, é típico de qual país?",
   ["Espanha", "Itália", "México", "Argentina"], "Espanha",
   "O flamenco nasceu na Andaluzia, no sul da Espanha.", "UNESCO – Patrimônio Cultural Imaterial: Flamenco")
mc(A, "Renascimento", 2, 12, "Qual cidade italiana, governada pela família Médici, é considerada o berço do Renascimento?",
   ["Florença", "Veneza", "Roma", "Milão"], "Florença",
   "Os Médici patrocinaram artistas como Botticelli e Michelangelo em Florença.", "Enciclopédia Britannica – verbete 'Renaissance'")
mc(A, "teatro", 2, 12, "Quais eram os dois principais gêneros do teatro na Grécia antiga?",
   ["Tragédia e comédia", "Ópera e balé", "Novela e musical", "Circo e mágica"], "Tragédia e comédia",
   "As máscaras que choram e que riem, símbolo do teatro, representam esses dois gêneros.", "Enciclopédia Britannica – verbete 'Greek theatre'")
tf(A, "fotografia", 2, 12, "Em grego, a palavra 'fotografia' quer dizer algo como 'desenhar com a luz'.", True,
   "Vem de 'phos', luz, e 'graphein', escrever ou desenhar.", "Dicionário Houaiss da Língua Portuguesa")
op(A, "técnicas", 2, 12, "Como se chama a pintura feita com tinta diluída em água, de cores transparentes, geralmente sobre papel?", "Aquarela",
   ["aquarela", "aguarela", "aquarelas"],
   "Na aquarela, o branco do papel aparece através das camadas leves de tinta.", "Enciclopédia Britannica – verbete 'Watercolour'")
tf(A, "Impressionismo", 3, 14, "Os pintores impressionistas costumavam pintar ao ar livre para captar os efeitos da luz natural.", True,
   "Monet, Renoir e outros pintavam fora do ateliê para registrar a luz de cada momento.", "Enciclopédia Britannica – verbete 'Impressionism'")
mc(A, "arte rupestre", 3, 14, "Qual parque nacional do Piauí guarda milhares de pinturas rupestres e é Patrimônio Mundial da Unesco?",
   ["Serra da Capivara", "Chapada Diamantina", "Lençóis Maranhenses", "Serra dos Órgãos"], "Serra da Capivara",
   "O parque reúne uma das maiores concentrações de sítios pré-históricos das Américas.", "UNESCO – Serra da Capivara National Park", br=True)
mc(A, "arte rupestre", 3, 14, "Em qual país fica a caverna de Lascaux, famosa por pinturas pré-históricas de animais?",
   ["França", "Espanha", "Itália", "Portugal"], "França",
   "A caverna fica no sudoeste da França e foi descoberta por jovens em 1940.", "Enciclopédia Britannica – verbete 'Lascaux'")
mc(A, "arte brasileira", 3, 14, "Qual pintor brasileiro ficou conhecido por quadros com bandeirinhas de festa junina?",
   ["Alfredo Volpi", "Candido Portinari", "Di Cavalcanti", "Ismael Nery"], "Alfredo Volpi",
   "Volpi pintava com têmpera e transformou as bandeirinhas em formas geométricas.", "Enciclopédia Itaú Cultural – verbete 'Alfredo Volpi'", br=True)
mc(A, "fotografia", 3, 14, "Qual fotógrafo brasileiro ficou famoso pelas imagens em preto e branco do garimpo de Serra Pelada?",
   ["Sebastião Salgado", "Vik Muniz", "Pierre Verger", "Marc Ferrez"], "Sebastião Salgado",
   "As fotos dos garimpeiros, feitas nos anos 1980, correram o mundo.", "Enciclopédia Itaú Cultural – verbete 'Sebastião Salgado'", br=True)
mc(A, "teatro", 3, 14, "Como se chama o tradicional teatro de bonecos popular de Pernambuco?",
   ["Mamulengo", "Maracatu", "Bumba meu boi", "Reisado"], "Mamulengo",
   "O mamulengo é registrado como Patrimônio Cultural do Brasil pelo IPHAN.", "IPHAN – Teatro de Bonecos Popular do Nordeste", br=True)
mc(A, "arte oriental", 3, 14, "Como se chama a arte japonesa de fazer arranjos com flores?",
   ["Ikebana", "Origami", "Bonsai", "Haicai"], "Ikebana",
   "A ikebana valoriza a harmonia, as linhas e o espaço vazio do arranjo.", "Enciclopédia Britannica – verbete 'Ikebana'")
mc(A, "Impressionismo", 3, 16, "Qual pintor impressionista francês pintou 'Baile no Moulin de la Galette'?",
   ["Pierre-Auguste Renoir", "Édouard Manet", "Camille Pissarro", "Paul Cézanne"], "Pierre-Auguste Renoir",
   "O quadro de 1876 mostra um baile ao ar livre em Montmartre e está no Museu d'Orsay.", "Musée d'Orsay – 'Bal du moulin de la Galette'")
mc(A, "arte brasileira contemporânea", 3, 16, "Qual artista brasileiro criou os 'Parangolés', capas coloridas para vestir e dançar?",
   ["Hélio Oiticica", "Lygia Clark", "Cildo Meireles", "Di Cavalcanti"], "Hélio Oiticica",
   "Os Parangolés só se completam quando alguém os veste e se movimenta.", "Enciclopédia Itaú Cultural – verbete 'Hélio Oiticica'", br=True)
mc(A, "arte brasileira contemporânea", 4, 16, "Qual artista brasileira criou os 'Bichos', esculturas de metal com dobradiças que o público pode manipular?",
   ["Lygia Clark", "Lygia Pape", "Tomie Ohtake", "Anita Malfatti"], "Lygia Clark",
   "Os Bichos, do início dos anos 1960, convidam o espectador a mudar a forma da obra.", "Enciclopédia Itaú Cultural – verbete 'Lygia Clark'", br=True)

# =========================================================== MITOLOGIA
M = "mit"
mc(M, "seres mágicos", 1, 6, "Qual personagem das histórias usa chapéu pontudo, voa numa vassoura e mexe um caldeirão?",
   ["Bruxa", "Fada", "Sereia", "Princesa"], "Bruxa",
   "A bruxa dos contos costuma preparar poções no caldeirão.", "Câmara Cascudo – Dicionário do Folclore Brasileiro")
mc(M, "criaturas lendárias", 1, 8, "Qual criatura lendária tem corpo de leão e cabeça e asas de águia?",
   ["Grifo", "Esfinge", "Pégaso", "Quimera"], "Grifo",
   "O grifo aparece em lendas e brasões como guardião de tesouros.", "Enciclopédia Britannica – verbete 'Griffin'")
mc(M, "lendas europeias", 1, 8, "Qual herói das lendas inglesas roubava dos ricos para dar aos pobres?",
   ["Robin Hood", "Rei Artur", "Zorro", "Guilherme Tell"], "Robin Hood",
   "Robin Hood vivia com seu bando na floresta de Sherwood.", "Enciclopédia Britannica – verbete 'Robin Hood'")
tf(M, "lendas", 1, 8, "Em muitas lendas e filmes, o lobisomem se transforma em noites de lua cheia.", True,
   "Em muitas histórias, o homem vira lobo na lua cheia; no folclore brasileiro, fala-se também das noites de sexta-feira.", "Câmara Cascudo – Dicionário do Folclore Brasileiro")
mc(M, "mitologia chinesa", 1, 9, "Quantos animais formam o zodíaco chinês?",
   ["12", "7", "10", "9"], "12",
   "Cada ano do ciclo chinês é representado por um dos 12 animais.", "Enciclopédia Britannica – verbete 'Chinese zodiac'")
mc(M, "lendas europeias", 1, 10, "Nas lendas do rei Artur, qual é o nome da espada mágica do rei?",
   ["Excalibur", "Durindana", "Tizona", "Mjölnir"], "Excalibur",
   "Em algumas versões, Artur recebe Excalibur da Dama do Lago.", "Enciclopédia Britannica – verbete 'Excalibur'")
mc(M, "mitologia chinesa", 2, 12, "Segundo a lenda do zodíaco chinês, qual animal ganhou a grande corrida, chegando em primeiro?",
   ["Rato", "Boi", "Tigre", "Dragão"], "Rato",
   "Na lenda, o rato pega carona nas costas do boi e salta na frente na chegada.", "Enciclopédia Britannica – verbete 'Chinese zodiac'")
mc(M, "mitologia hindu", 2, 12, "Qual deus hindu tem cabeça de elefante?",
   ["Ganesha", "Shiva", "Krishna", "Hanuman"], "Ganesha",
   "Ganesha é invocado para remover obstáculos e trazer bons começos.", "Enciclopédia Britannica – verbete 'Ganesha'")
mc(M, "mitologia romana", 2, 12, "Segundo a lenda da fundação de Roma, quais irmãos gêmeos foram amamentados por uma loba?",
   ["Rômulo e Remo", "Castor e Pólux", "Apolo e Ártemis", "Caim e Abel"], "Rômulo e Remo",
   "Rômulo deu nome à cidade de Roma, segundo a tradição.", "Enciclopédia Britannica – verbete 'Romulus and Remus'")
mc(M, "mitologia indígena", 2, 12, "Na mitologia tupi, qual é o nome do ser ligado ao trovão?",
   ["Tupã", "Jaci", "Guaraci", "Anhangá"], "Tupã",
   "Os jesuítas usaram o nome Tupã para traduzir a ideia de Deus aos indígenas.", "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
tf(M, "mitologia indígena", 2, 12, "Nas lendas tupis, Jaci é o nome da Lua.", True,
   "Jaci é a Lua e Guaraci é o Sol nas tradições de origem tupi.", "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia nórdica", 2, 12, "Na mitologia nórdica, como se chamam as guerreiras que escolhem os mortos em batalha e os levam ao Valhala?",
   ["Valquírias", "Amazonas", "Nornas", "Fúrias"], "Valquírias",
   "As valquírias serviam a Odin e conduziam os heróis ao seu salão.", "Enciclopédia Britannica – verbete 'Valkyrie'")
mc(M, "mitologia hindu", 3, 14, "Na trindade hindu, Brahma é o criador e Vishnu o preservador; qual deus é o destruidor?",
   ["Shiva", "Ganesha", "Indra", "Krishna"], "Shiva",
   "Shiva destrói para permitir que o universo se renove.", "Enciclopédia Britannica – verbete 'Shiva'")
mc(M, "mitologia japonesa", 3, 14, "Na mitologia japonesa, qual é a deusa do Sol?",
   ["Amaterasu", "Izanami", "Susanoo", "Inari"], "Amaterasu",
   "Segundo a tradição, a família imperial japonesa descende de Amaterasu.", "Enciclopédia Britannica – verbete 'Amaterasu'")
mc(M, "mitologia japonesa", 3, 14, "Qual criatura do folclore japonês é uma raposa mágica que pode ter várias caudas?",
   ["Kitsune", "Tanuki", "Kappa", "Oni"], "Kitsune",
   "Quanto mais velha e sábia a kitsune, mais caudas ela tem, até nove.", "Enciclopédia Britannica – verbete 'Kitsune'")
mc(M, "mitologia romana", 3, 14, "Qual deus romano de duas faces, uma olhando para o passado e outra para o futuro, deu nome ao mês de janeiro?",
   ["Jano", "Saturno", "Mercúrio", "Vulcano"], "Jano",
   "Jano era o deus das portas, das passagens e dos começos.", "Enciclopédia Britannica – verbete 'Janus'")
mc(M, "mitologia grega", 3, 14, "Na mitologia grega, quantas eram as musas, filhas de Zeus que inspiravam as artes?",
   ["9", "3", "7", "12"], "9",
   "Cada uma das nove musas protegia uma arte, como a poesia, a dança e a história.", "Enciclopédia Britannica – verbete 'Muse'")
mc(M, "mitologia grega", 3, 14, "Qual deusa grega da agricultura e das colheitas é mãe de Perséfone?",
   ["Deméter", "Hera", "Héstia", "Atena"], "Deméter",
   "Na lenda, a tristeza de Deméter pela filha explica a chegada do inverno.", "Enciclopédia Britannica – verbete 'Demeter'")
mc(M, "mitologia grega", 3, 14, "Qual personagem grego decifrou o enigma da Esfinge de Tebas?",
   ["Édipo", "Teseu", "Perseu", "Jasão"], "Édipo",
   "A resposta ao enigma era o ser humano, que engatinha, anda e depois usa bengala.", "Enciclopédia Britannica – verbete 'Oedipus'")
op(M, "mitologia grega", 3, 14, "Na mitologia grega, como se chama o alimento dos deuses do Olimpo?", "Ambrosia",
   ["ambrosia", "ambrósia"],
   "A ambrosia, junto com o néctar, garantia a imortalidade dos deuses.", "Enciclopédia Britannica – verbete 'Ambrosia'")
mc(M, "folclore brasileiro", 3, 14, "Qual criatura do folclore amazônico é um gigante peludo que, em muitas versões, tem uma boca na barriga?",
   ["Mapinguari", "Curupira", "Caipora", "Boitatá"], "Mapinguari",
   "O mapinguari assusta caçadores e seringueiros nas matas da Amazônia.", "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(M, "mitologia chinesa", 4, 16, "Qual é o nome do Rei Macaco, herói do clássico chinês 'Jornada ao Oeste'?",
   ["Sun Wukong", "Nezha", "Pangu", "Fu Xi"], "Sun Wukong",
   "O macaco, cheio de poderes, acompanha um monge numa viagem em busca de textos sagrados.", "Enciclopédia Britannica – verbete 'Journey to the West'")
op(M, "folclore brasileiro", 4, 16, "Qual lenda do Piauí fala de um pescador amaldiçoado, de cabeça enorme, que vive no rio Parnaíba?", "Cabeça de Cuia",
   ["cabeca de cuia", "cabeça de cuia", "cabeça-de-cuia", "crispim"],
   "Segundo a lenda, Crispim foi amaldiçoado pela mãe e vive assombrando o encontro dos rios em Teresina.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)

# =========================================================== CURIOSIDADES
C = "cur"
mc(C, "calendário", 1, 6, "Em qual mês do ano se comemora o Natal?",
   ["Dezembro", "Janeiro", "Junho", "Outubro"], "Dezembro",
   "O Natal é comemorado no dia 25 de dezembro.", "Enciclopédia Britannica – verbete 'Christmas'")
mc(C, "calendário", 1, 6, "Em qual dia comemoramos a chegada do Ano-Novo?",
   ["1º de janeiro", "25 de dezembro", "7 de setembro", "12 de outubro"], "1º de janeiro",
   "A virada do ano acontece na passagem de 31 de dezembro para 1º de janeiro.", "Enciclopédia Britannica – verbete 'New Year's Day'")
mc(C, "calendário", 1, 7, "Qual estação do ano é conhecida como a época em que as folhas das árvores caem?",
   ["Outono", "Verão", "Primavera", "Inverno"], "Outono",
   "Em inglês americano, o outono é até chamado de 'fall', que quer dizer queda.", "Enciclopédia Britannica – verbete 'Autumn'")
mc(C, "bandeiras", 1, 8, "Qual é a cor do círculo no centro da bandeira do Japão?",
   ["Vermelho", "Azul", "Amarelo", "Preto"], "Vermelho",
   "O círculo vermelho sobre fundo branco representa o Sol.", "Enciclopédia Britannica – verbete 'Flag of Japan'")
mc(C, "calendário", 1, 9, "Em geral, de quantos em quantos anos acontece um ano bissexto?",
   ["4", "2", "5", "10"], "4",
   "A cada quatro anos, em geral, fevereiro ganha o dia 29.", "Observatório Nacional")
mc(C, "bandeiras", 2, 10, "Quantas estrelas tem a bandeira dos Estados Unidos?",
   ["50", "13", "48", "52"], "50",
   "Cada estrela representa um estado; as 13 listras lembram as colônias originais.", "Enciclopédia Britannica – verbete 'Flag of the United States'")
mc(C, "costumes", 2, 10, "As bodas de prata comemoram quantos anos de casamento?",
   ["25", "10", "15", "30"], "25",
   "Depois das bodas de prata, aos 25 anos, vêm as de ouro, aos 50.", "Dicionário Houaiss da Língua Portuguesa")
mc(C, "origem dos objetos", 2, 10, "Qual relógio antigo marca as horas pela sombra de uma haste?",
   ["Relógio de sol", "Ampulheta", "Clepsidra", "Relógio cuco"], "Relógio de sol",
   "Conforme o Sol se move no céu, a sombra da haste aponta para horas diferentes.", "Enciclopédia Britannica – verbete 'Sundial'")
mc(C, "calendário", 2, 10, "Em qual mês começa a primavera no Brasil?",
   ["Setembro", "Março", "Junho", "Dezembro"], "Setembro",
   "No Hemisfério Sul, a primavera começa no equinócio de setembro.", "Observatório Nacional", br=True)
mc(C, "calendário", 2, 10, "Um período de mil anos recebe qual nome?",
   ["Milênio", "Século", "Década", "Era"], "Milênio",
   "Um milênio tem dez séculos.", "Dicionário Houaiss da Língua Portuguesa")
tf(C, "mitos populares", 2, 10, "Os flamingos já nascem com as penas cor-de-rosa.", False,
   "Os filhotes nascem acinzentados; a cor rosa vem de pigmentos da alimentação.", "Enciclopédia Britannica – verbete 'Flamingo'")
tf(C, "mitos populares", 2, 10, "Um chiclete engolido fica grudado no estômago por sete anos.", False,
   "O chiclete não é digerido, mas passa pelo intestino e sai do corpo em poucos dias.", "Mayo Clinic")
mc(C, "bandeiras", 2, 12, "Qual folha aparece no centro da bandeira do Canadá?",
   ["Bordo", "Carvalho", "Palmeira", "Oliveira"], "Bordo",
   "A folha de bordo vermelha é o grande símbolo do Canadá.", "Enciclopédia Britannica – verbete 'Flag of Canada'")
mc(C, "calendário", 2, 12, "Qual mês recebeu esse nome em homenagem ao líder romano Júlio César?",
   ["Julho", "Agosto", "Março", "Junho"], "Julho",
   "Agosto, por sua vez, homenageia o imperador Augusto.", "Enciclopédia Britannica – verbete 'July'")
mc(C, "origem dos objetos", 2, 12, "Em qual país foram inventados os fogos de artifício?",
   ["China", "Índia", "Itália", "Egito"], "China",
   "Os fogos surgiram na China, depois da invenção da pólvora.", "Enciclopédia Britannica – verbete 'Fireworks'")
tf(C, "origem dos costumes", 2, 12, "O nome 'sanduíche' vem de um nobre inglês, o Conde de Sandwich.", True,
   "O nome homenageia John Montagu, 4º Conde de Sandwich, no século XVIII.", "Enciclopédia Britannica – verbete 'Sandwich'")
tf(C, "mitos populares", 3, 12, "Gêmeos idênticos têm impressões digitais iguais.", False,
   "As digitais se formam no útero e sofrem pequenas variações, por isso são diferentes até entre gêmeos.", "Enciclopédia Britannica – verbete 'Fingerprint'")
mc(C, "bandeiras", 3, 14, "Qual país tem uma bandeira que não é retangular, formada por dois triângulos?",
   ["Nepal", "Butão", "Índia", "Tailândia"], "Nepal",
   "A bandeira do Nepal tem a forma de duas flâmulas triangulares sobrepostas.", "Enciclopédia Britannica – verbete 'Flag of Nepal'")
tf(C, "calendário", 3, 14, "O nome 'setembro' vem do número sete em latim, porque era o sétimo mês do antigo calendário romano.", True,
   "O antigo ano romano começava em março; por isso setembro era o sétimo mês.", "Enciclopédia Britannica – verbete 'September'")
op(C, "coleções", 3, 14, "Como se chama a pessoa que coleciona e estuda moedas e cédulas?", "Numismata",
   ["numismata", "numismatico", "numismático"],
   "A numismática é o estudo das moedas e do dinheiro.", "Dicionário Houaiss da Língua Portuguesa")
mc(C, "calendário", 4, 16, "Qual papa deu nome ao calendário usado hoje na maior parte do mundo?",
   ["Gregório XIII", "João Paulo II", "Pio IX", "Leão X"], "Gregório XIII",
   "O calendário gregoriano foi instituído em 1582 para corrigir o calendário juliano.", "Enciclopédia Britannica – verbete 'Gregorian calendar'")
mc(C, "palavras curiosas", 4, 16, "Como se chama o medo exagerado do número 13?",
   ["Triscaidecafobia", "Claustrofobia", "Agorafobia", "Nictofobia"], "Triscaidecafobia",
   "Por causa dela, alguns prédios pulam o 13º andar na numeração.", "Dicionário Houaiss da Língua Portuguesa")
