# Perguntas novas: filmes infantis. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "inf"

# =========================================================== FÁCEIS (6–8 anos)
op(T, "personagens", 1, 6, "De que cor é a pele do ogro Shrek?", "Verde", ["verde"],
   "Shrek é um ogro verde que vive sozinho em seu pântano até ter a paz interrompida.",
   "DreamWorks Animation – 'Shrek' (2001)")
op(T, "objetos mágicos", 1, 6, "Em 'Cinderela', no que a Fada Madrinha transforma uma abóbora?", "Carruagem",
   ["carruagem", "uma carruagem", "a carruagem", "coche"],
   "Com sua varinha, a Fada Madrinha transforma a abóbora em carruagem para Cinderela ir ao baile.",
   "Disney – 'Cinderela' (1950)")
op(T, "animação brasileira", 1, 6, "Em 'Rio', o que a ararinha-azul Blu não sabe fazer no começo do filme?", "Voar",
   ["voar", "não sabe voar"],
   "Criado como bicho de estimação nos Estados Unidos, Blu nunca aprendeu a voar.",
   "Blue Sky Studios – 'Rio' (2011)", br=True)
op(T, "personagens", 1, 6, "Em 'Monstros S.A.', quantos olhos tem o monstrinho verde Mike Wazowski?", "Um",
   ["1", "um", "só um", "apenas um", "um olho", "1 olho"],
   "Mike Wazowski é uma bolinha verde com um único olho grande no meio do corpo.",
   "Pixar Animation Studios – 'Monstros S.A.' (2001)")
op(T, "objetos mágicos", 1, 7, "Em 'A Bela e a Fera', qual flor encantada mostra quanto tempo falta para o feitiço não ter mais volta?", "Rosa",
   ["rosa", "uma rosa", "a rosa", "rosa encantada"],
   "Quando a última pétala da rosa encantada cair, a Fera ficará para sempre como monstro.",
   "Disney – 'A Bela e a Fera' (1991)")
mc(T, "animais dos filmes", 1, 6, "Em 'O Rei Leão', que animal é o Pumba, amigo de Timão?",
   ["Javali", "Suricato", "Hiena", "Zebra"], "Javali",
   "Pumba é um javali-africano, também chamado facócero, e Timão é um suricato.",
   "Disney – 'O Rei Leão' (1994)")
mc(T, "personagens", 1, 6, "De que cor é o Stitch, o alienígena de 'Lilo & Stitch'?",
   ["Azul", "Verde", "Vermelho", "Amarelo"], "Azul",
   "Stitch é um bichinho azul de orelhas grandes, criado em laboratório por um cientista alienígena.",
   "Disney – 'Lilo & Stitch' (2002)")
mc(T, "amigos dos protagonistas", 1, 7, "Em 'A Pequena Sereia', qual é o nome do peixinho amarelo e azul, melhor amigo de Ariel?",
   ["Linguado", "Sebastião", "Sabidão", "Tritão"], "Linguado",
   "Linguado acompanha Ariel em todas as aventuras no fundo do mar.",
   "Disney – 'A Pequena Sereia' (1989)")
mc(T, "animais dos filmes", 1, 6, "Em 'A Pequena Sereia', que animal é o Sebastião, conselheiro do rei Tritão?",
   ["Caranguejo", "Polvo", "Tartaruga", "Cavalo-marinho"], "Caranguejo",
   "Sebastião é um caranguejo vermelho encarregado de vigiar Ariel.",
   "Disney – 'A Pequena Sereia' (1989)")
mc(T, "animais dos filmes", 1, 6, "Em 'Madagascar', que animal é o Marty, melhor amigo do leão Alex?",
   ["Zebra", "Cavalo", "Girafa", "Hipopótamo"], "Zebra",
   "Marty é uma zebra que sonha em conhecer a natureza fora do zoológico de Nova York.",
   "DreamWorks Animation – 'Madagascar' (2005)")
mc(T, "Minions", 1, 6, "Qual fruta os Minions adoram?",
   ["Banana", "Maçã", "Uva", "Melancia"], "Banana",
   "Os Minions são loucos por banana e até cantam uma música chamada 'Banana'.",
   "Illumination – 'Meu Malvado Favorito' (2010)")
mc(T, "brinquedos", 1, 6, "Em 'Toy Story', qual brinquedo tem olhos, nariz e boca que podem ser tirados e trocados de lugar?",
   ["Senhor Cabeça de Batata", "Rex", "Slinky", "Porquinho"], "Senhor Cabeça de Batata",
   "O Senhor Cabeça de Batata é um brinquedo rabugento cujas peças se encaixam no corpo.",
   "Pixar Animation Studios – 'Toy Story' (1995)")
mc(T, "personagens", 1, 6, "Em 'Trolls', de que cor é a princesa Poppy?",
   ["Rosa", "Azul", "Verde", "Laranja"], "Rosa",
   "Poppy é uma trolzinha cor-de-rosa, alegre e cantora, que vive abraçando todo mundo.",
   "DreamWorks Animation – 'Trolls' (2016)")
mc(T, "animais dos filmes", 1, 6, "Em '101 Dálmatas', como são os pelos dos cachorros?",
   ["Brancos com manchas pretas", "Marrons com manchas brancas", "Cinza com listras pretas", "Amarelos com manchas marrons"],
   "Brancos com manchas pretas",
   "Os dálmatas são cães brancos cobertos de pintas pretas, que aparecem conforme crescem.",
   "Disney – '101 Dálmatas' (1961)")
mc(T, "vilões", 1, 7, "Em 'Mogli – O Menino Lobo', que animal é o vilão Shere Khan?",
   ["Tigre", "Leão", "Lobo", "Cobra"], "Tigre",
   "Shere Khan é um tigre que odeia os humanos e quer pegar Mogli.",
   "Disney – 'Mogli – O Menino Lobo' (1967)")
mc(T, "animais dos filmes", 1, 7, "Em 'Kung Fu Panda', que animal é o sábio Mestre Oogway?",
   ["Tartaruga", "Macaco", "Garça", "Cobra"], "Tartaruga",
   "Mestre Oogway é uma tartaruga muito velha e sábia que escolhe Po como Dragão Guerreiro.",
   "DreamWorks Animation – 'Kung Fu Panda' (2008)")
mc(T, "animais dos filmes", 1, 7, "Em 'Madagascar', quais aves agem como um grupo de agentes secretos?",
   ["Pinguins", "Flamingos", "Papagaios", "Corujas"], "Pinguins",
   "Os quatro pinguins de Madagascar fazem fugas e missões como se fossem um comando secreto.",
   "DreamWorks Animation – 'Madagascar' (2005)")
mc(T, "animais dos filmes", 1, 7, "Em 'Zootopia', que animal é o Flash, funcionário que faz tudo muito devagar?",
   ["Bicho-preguiça", "Tartaruga", "Caracol", "Coala"], "Bicho-preguiça",
   "Flash é um bicho-preguiça que trabalha no departamento de trânsito e demora uma eternidade para atender.",
   "Disney – 'Zootopia' (2016)")
mc(T, "brinquedos", 1, 7, "Em 'Toy Story 2', como se chama a boneca vaqueira de trança ruiva?",
   ["Jessie", "Molly", "Gabby", "Bonnie"], "Jessie",
   "Jessie faz parte da coleção de brinquedos do antigo programa de TV do Woody.",
   "Pixar Animation Studios – 'Toy Story 2' (1999)")
mc(T, "vilões", 1, 7, "Em 'Peter Pan', que animal vive perseguindo o Capitão Gancho?",
   ["Crocodilo", "Tubarão", "Leão", "Polvo"], "Crocodilo",
   "O crocodilo engoliu um relógio, e o tique-taque avisa o Capitão Gancho quando ele se aproxima.",
   "Disney – 'Peter Pan' (1953)")
mc(T, "personagens", 1, 7, "Em 'Divertida Mente', qual emoção é verde?",
   ["Nojinho", "Medo", "Raiva", "Tristeza"], "Nojinho",
   "Nojinho é verde e protege Riley de coisas nojentas, como brócolis.",
   "Pixar Animation Studios – 'Divertida Mente' (2015)")
mc(T, "personagens", 1, 7, "Em 'Super Mario Bros. – O Filme', de 2023, qual princesa governa o Reino dos Cogumelos?",
   ["Peach", "Daisy", "Zelda", "Elsa"], "Peach",
   "A princesa Peach lidera o Reino dos Cogumelos e ensina Mario a enfrentar os desafios.",
   "Illumination – 'Super Mario Bros. – O Filme' (2023)")
mc(T, "animação brasileira", 1, 8, "Em 'Rio 2', a família da ararinha Blu viaja para qual floresta brasileira?",
   ["Amazônia", "Mata Atlântica", "Caatinga", "Pantanal"], "Amazônia",
   "Em 'Rio 2', Blu, Jade e os filhos deixam o Rio de Janeiro e vão para a Floresta Amazônica.",
   "Blue Sky Studios – 'Rio 2' (2014)", br=True)
mc(T, "Turma da Mônica", 1, 8, "No filme 'Turma da Mônica: Laços', a turma sai em busca de qual cachorro desaparecido?",
   ["Floquinho", "Bidu", "Mingau", "Sansão"], "Floquinho",
   "Mônica, Cebolinha, Cascão e Magali partem numa aventura para encontrar o cachorro do Cebolinha.",
   "AdoroCinema – 'Turma da Mônica: Laços' (2019)", br=True)
tf(T, "lugares", 1, 6, "O Shrek mora num castelo.", False,
   "Shrek mora num pântano e adora ficar sozinho por lá.",
   "DreamWorks Animation – 'Shrek' (2001)")
tf(T, "personagens", 1, 7, "Em 'Up – Altas Aventuras', o senhor Carl viaja sozinho do começo ao fim da aventura.", False,
   "Sem querer, Carl leva junto o pequeno escoteiro Russell, que estava na varanda quando a casa decolou.",
   "Pixar Animation Studios – 'Up – Altas Aventuras' (2009)")
tf(T, "objetos mágicos", 1, 7, "Em 'Up – Altas Aventuras', o cachorro Dug consegue falar graças a uma coleira especial.", True,
   "A coleira de Dug transforma os pensamentos dele em palavras.",
   "Pixar Animation Studios – 'Up – Altas Aventuras' (2009)")

# =========================================================== MÉDIAS
mc(T, "animais dos filmes", 2, 8, "Em 'Toy Story 2', que animal é o Bala no Alvo, companheiro de Woody e Jessie?",
   ["Cavalo", "Cachorro", "Vaca", "Burro"], "Cavalo",
   "Bala no Alvo é o cavalo de brinquedo do Woody, rápido e muito carinhoso.",
   "Pixar Animation Studios – 'Toy Story 2' (1999)")
mc(T, "animais dos filmes", 2, 8, "Em 'Mogli – O Menino Lobo', que animal é Bagheera, que tenta levar o menino para a aldeia dos homens?",
   ["Pantera-negra", "Tigre", "Lobo", "Urso"], "Pantera-negra",
   "Bagheera é uma pantera-negra que encontrou Mogli bebê e cuida dele.",
   "Disney – 'Mogli – O Menino Lobo' (1967)")
mc(T, "vilões", 2, 8, "Em 'Meu Malvado Favorito', qual é o grande plano de Gru para virar o maior vilão do mundo?",
   ["Roubar a Lua", "Roubar o Sol", "Apagar as estrelas", "Congelar o oceano"], "Roubar a Lua",
   "Gru usa um raio encolhedor para deixar a Lua pequenininha e roubá-la.",
   "Illumination – 'Meu Malvado Favorito' (2010)")
mc(T, "lugares", 2, 9, "Em 'Frozen', qual é o nome do reino de Anna e Elsa?",
   ["Arendelle", "Corona", "Agrabah", "Tão Tão Distante"], "Arendelle",
   "Arendelle é um reino nórdico cercado por montanhas e por um fiorde.",
   "Disney – 'Frozen – Uma Aventura Congelante' (2013)")
mc(T, "personagens", 2, 9, "Em 'Encanto', qual é o nome da menina de óculos que não recebeu um dom mágico?",
   ["Mirabel", "Isabela", "Luisa", "Dolores"], "Mirabel",
   "Mirabel é a única da nova geração dos Madrigal sem dom, mas é ela quem salva a família.",
   "Disney – 'Encanto' (2021)")
mc(T, "animais dos filmes", 2, 9, "Em 'Up – Altas Aventuras', como se chama a ave gigante e colorida que Russell encontra?",
   ["Kevin", "Dug", "Zazu", "Blu"], "Kevin",
   "Russell dá o nome de Kevin à ave, mas depois descobre que ela é fêmea e mãe de filhotes.",
   "Pixar Animation Studios – 'Up – Altas Aventuras' (2009)")
mc(T, "personagens", 2, 8, "Em 'WALL-E', qual é o nome da robô branca por quem WALL-E se apaixona?",
   ["EVA", "MO", "AUTO", "Baymax"], "EVA",
   "EVA é uma robô exploradora enviada à Terra para procurar sinais de vida vegetal.",
   "Pixar Animation Studios – 'WALL-E' (2008)")
tf(T, "bichos de estimação", 2, 8, "Em 'WALL-E', o robozinho tem uma barata como bichinho de estimação.", True,
   "A baratinha é a única companheira de WALL-E na Terra coberta de lixo.",
   "Pixar Animation Studios – 'WALL-E' (2008)")
tf(T, "personagens", 2, 8, "Em 'Shrek', a princesa Fiona se transforma em ogra quando o sol se põe.", True,
   "Fiona foi enfeitiçada: de dia é humana e, ao anoitecer, vira ogra.",
   "DreamWorks Animation – 'Shrek' (2001)")
tf(T, "personagens", 2, 8, "Em 'Procurando Nemo', o Nemo tem as duas nadadeiras do mesmo tamanho.", False,
   "Nemo tem uma nadadeira menor que a outra, que o pai chama de 'nadadeira da sorte'.",
   "Pixar Animation Studios – 'Procurando Nemo' (2003)")
tf(T, "vilões", 2, 8, "Em 'A Pequena Sereia', a bruxa Úrsula é metade mulher e metade tubarão.", False,
   "Úrsula tem a parte de baixo do corpo com tentáculos, como um polvo.",
   "Disney – 'A Pequena Sereia' (1989)")
tf(T, "lugares", 2, 9, "A história de 'Kung Fu Panda' se passa no Japão.", False,
   "O filme se passa no Vale da Paz, numa China antiga e imaginária.",
   "DreamWorks Animation – 'Kung Fu Panda' (2008)")
op(T, "roupas de personagens", 2, 10, "Em 'Os Incríveis', que peça de roupa a estilista Edna Moda proíbe nos uniformes de super-herói?", "Capa",
   ["capa", "capas", "a capa"],
   "Edna repete 'nada de capas!' e lembra heróis que se deram mal porque a capa ficou presa.",
   "Pixar Animation Studios – 'Os Incríveis' (2004)")
op(T, "personagens", 2, 9, "Em 'Carros', qual é o número pintado no Relâmpago McQueen?", "95",
   ["95", "noventa e cinco", "número 95"],
   "O número 95 aparece nas laterais do carro vermelho e lembra 1995, ano de lançamento de 'Toy Story'.",
   "Pixar Animation Studios – 'Carros' (2006)")
mc(T, "personagens", 2, 10, "Em 'Kung Fu Panda', como se chama o grupo de cinco mestres que treina com Po?",
   ["Cinco Furiosos", "Cinco Dragões", "Cinco Tigres", "Cinco Guerreiros"], "Cinco Furiosos",
   "Os Cinco Furiosos são Tigresa, Macaco, Louva-a-Deus, Víbora e Garça.",
   "DreamWorks Animation – 'Kung Fu Panda' (2008)")
mc(T, "animais dos filmes", 2, 10, "Em 'Kung Fu Panda', que animal é o Mestre Shifu?",
   ["Panda-vermelho", "Guaxinim", "Raposa", "Macaco"], "Panda-vermelho",
   "Mestre Shifu é um panda-vermelho pequeno e exigente que treina o grande Po.",
   "DreamWorks Animation – 'Kung Fu Panda' (2008)")
mc(T, "lugares", 2, 10, "Em 'Shrek 2', qual é o nome do reino dos pais de Fiona?",
   ["Tão Tão Distante", "Arendelle", "Agrabah", "Corona"], "Tão Tão Distante",
   "O reino de Tão Tão Distante imita Hollywood, com até um letreiro no morro.",
   "DreamWorks Animation – 'Shrek 2' (2004)")
mc(T, "músicas dos filmes", 2, 10, "Em 'Encanto', qual é o título em português da canção sobre o tio de quem a família evita falar?",
   ["Não Falamos do Bruno", "Livre Estou", "Saber Quem Sou", "Ciclo sem Fim"], "Não Falamos do Bruno",
   "A canção virou um enorme sucesso e chegou ao topo das paradas nos Estados Unidos.",
   "Disney – 'Encanto' (2021)")
mc(T, "lugares", 2, 10, "Em 'Viva – A Vida É uma Festa', a história acontece durante qual celebração mexicana?",
   ["Dia dos Mortos", "Carnaval", "Natal", "Ano-Novo"], "Dia dos Mortos",
   "No Dia dos Mortos, as famílias mexicanas enfeitam altares com fotos e flores para lembrar quem já morreu.",
   "Pixar Animation Studios – 'Viva – A Vida É uma Festa' (2017)")
mc(T, "animação brasileira", 2, 10, "Em 'Rio', como se chama a ararinha-azul fêmea por quem Blu se apaixona?",
   ["Jade", "Linda", "Eva", "Bia"], "Jade",
   "Jade é uma ararinha livre e corajosa que ensina Blu a se virar no Rio de Janeiro.",
   "Blue Sky Studios – 'Rio' (2011)", br=True)
mc(T, "animação brasileira", 2, 10, "Em 'Rio', qual é o nome da cacatua malvada que ajuda os contrabandistas de aves?",
   ["Nigel", "Pedro", "Nico", "Rafael"], "Nigel",
   "Nigel é uma cacatua rancorosa que persegue Blu e Jade pela cidade.",
   "Blue Sky Studios – 'Rio' (2011)", br=True)
tf(T, "Turma da Mônica", 2, 9, "'Turma da Mônica: Laços' foi feito com atores de verdade, e não como desenho animado.", True,
   "Lançado em 2019, o filme trouxe crianças atores nos papéis de Mônica, Cebolinha, Cascão e Magali.",
   "AdoroCinema – 'Turma da Mônica: Laços' (2019)", br=True)
mc(T, "Turma da Mônica", 2, 9, "Qual árvore frutífera aparece no título do filme do Chico Bento com atores, lançado em 2025?",
   ["Goiabeira", "Mangueira", "Jabuticabeira", "Laranjeira"], "Goiabeira",
   "O filme se chama 'Chico Bento e a Goiabeira Maravilhosa', e goiaba é a fruta preferida do caipira.",
   "AdoroCinema – 'Chico Bento e a Goiabeira Maravilhosa' (2025)", br=True)

# =========================================================== DIFÍCEIS
tf(T, "sequências", 3, 12, "'Moana 2' foi lançado antes de 'Frozen II'.", False,
   "'Frozen II' estreou em 2019 e 'Moana 2' só chegou aos cinemas em 2024.",
   "Disney – lançamentos de 2019 e 2024")
tf(T, "clássicos da Disney", 3, 12, "'O Rei Leão', de 1994, foi feito todo em computação gráfica.", False,
   "O filme de 1994 é uma animação desenhada à mão; a versão de 2019 é que foi toda feita em computador.",
   "Enciclopédia Britannica – verbete 'The Lion King'")
mc(T, "músicas dos filmes", 3, 12, "Em 'O Rei Leão', qual é o título em português da canção de abertura, quando Simba é apresentado aos animais?",
   ["Ciclo sem Fim", "Hakuna Matata", "Aqui no Mar", "Um Mundo Ideal"], "Ciclo sem Fim",
   "'Ciclo sem Fim' é a versão brasileira de 'Circle of Life', de Elton John e Tim Rice.",
   "Disney – 'O Rei Leão' (1994)")
mc(T, "personagens", 3, 12, "Em 'A Bela e a Fera', qual personagem encantada é um bule de chá?",
   ["Madame Samovar", "Lumière", "Zip", "Gaston"], "Madame Samovar",
   "Madame Samovar é a bule bondosa, mãe da xicarazinha Zip.",
   "Disney – 'A Bela e a Fera' (1991)")
mc(T, "lugares", 3, 12, "Em 'Como Treinar o Seu Dragão', qual é o nome da ilha viking onde Soluço vive?",
   ["Berk", "Asgard", "Valhala", "Midgard"], "Berk",
   "Berk é uma ilha gelada onde vikings e dragões viviam em guerra até Soluço fazer amizade com Banguela.",
   "DreamWorks Animation – 'Como Treinar o Seu Dragão' (2010)")
mc(T, "Studio Ghibli", 3, 12, "Em 'Meu Amigo Totoro', um gato gigante e mágico serve de qual meio de transporte?",
   ["Ônibus", "Trem", "Barco", "Avião"], "Ônibus",
   "O Gato-ônibus corre pelos campos com seus muitos pés e tem janelas no corpo.",
   "Studio Ghibli – 'Meu Amigo Totoro' (1988)")
mc(T, "Studio Ghibli", 3, 12, "No filme 'Ponyo – Uma Amizade que Veio do Mar', o que é Ponyo antes de virar menina?",
   ["Peixe", "Pássaro", "Gato", "Sapo"], "Peixe",
   "Ponyo é uma peixinha que foge do mar, conhece o menino Sosuke e decide virar humana.",
   "Studio Ghibli – 'Ponyo' (2008)")
mc(T, "Studio Ghibli", 3, 13, "Em 'O Castelo Animado', do Studio Ghibli, que tipo de criatura é Calcifer, que faz o castelo andar?",
   ["Um demônio do fogo", "Um dragão", "Um espantalho", "Um gato"], "Um demônio do fogo",
   "Calcifer é um demônio do fogo preso à lareira por um pacto com o mago Howl.",
   "Studio Ghibli – 'O Castelo Animado' (2004)")
tf(T, "Studio Ghibli", 3, 13, "'A Viagem de Chihiro' ganhou o Oscar de Melhor Filme de Animação.", True,
   "O filme de Hayao Miyazaki venceu o prêmio na cerimônia de 2003.",
   "Academia de Artes e Ciências Cinematográficas – 75º Oscar")
mc(T, "animação brasileira", 3, 12, "Qual animação dirigida pelo brasileiro Carlos Saldanha conta a história de um touro que prefere cheirar flores a lutar?",
   ["O Touro Ferdinando", "Rio 2", "A Era do Gelo 2", "Robôs"], "O Touro Ferdinando",
   "Lançado em 2017, o filme foi indicado ao Oscar de Melhor Filme de Animação.",
   "Blue Sky Studios – 'O Touro Ferdinando' (2017)", br=True)
mc(T, "dublagem e vozes", 3, 14, "Qual ator brasileiro deu voz ao ornitólogo Túlio em 'Rio', inclusive na versão original em inglês?",
   ["Rodrigo Santoro", "Wagner Moura", "Lázaro Ramos", "Selton Mello"], "Rodrigo Santoro",
   "Rodrigo Santoro dublou Túlio em inglês e em português.",
   "Blue Sky Studios – 'Rio' (2011)", br=True)
mc(T, "dublagem e vozes", 3, 14, "Qual humorista do 'Casseta & Planeta' dublou o Shrek no Brasil nos primeiros filmes?",
   ["Bussunda", "Hélio de la Peña", "Marcelo Madureira", "Cláudio Manoel"], "Bussunda",
   "Bussunda deu voz ao ogro em 'Shrek' (2001) e 'Shrek 2' (2004).",
   "Memória Globo – verbete 'Bussunda'", br=True)

# =========================================================== MUITO DIFÍCEIS
mc(T, "clássicos da Disney", 4, 14, "Em 'Você Já Foi à Bahia?', da Disney, que animal é Panchito, amigo mexicano de Zé Carioca e do Pato Donald?",
   ["Galo", "Papagaio", "Pato", "Tucano"], "Galo",
   "Panchito Pistoles é um galo mexicano que forma com Donald e Zé Carioca o trio do filme de 1944.",
   "Disney – 'Você Já Foi à Bahia?' (1944)", br=True)
tf(T, "músicas dos filmes", 4, 16, "A canção 'Real in Rio', do filme 'Rio', foi indicada ao Oscar de Melhor Canção Original.", True,
   "A música, de Sergio Mendes, Carlinhos Brown e Siedah Garrett, concorreu ao Oscar em 2012.",
   "Academia de Artes e Ciências Cinematográficas – 84º Oscar", br=True)
tf(T, "estúdios", 4, 14, "O estúdio Blue Sky, de 'A Era do Gelo' e 'Rio', foi fechado em 2021.", True,
   "A Disney, que havia comprado a Fox, encerrou as atividades do Blue Sky em abril de 2021.",
   "Enciclopédia Britannica – verbete 'Blue Sky Studios'")
mc(T, "Turma da Mônica", 4, 14, "O filme 'Turma da Mônica: Laços' foi baseado na graphic novel de quais irmãos quadrinistas?",
   ["Vitor e Lu Cafaggi", "Fábio Moon e Gabriel Bá", "Chico e Paulo Caruso", "Mauricio e Mônica de Sousa"], "Vitor e Lu Cafaggi",
   "A graphic novel 'Laços', de 2013, faz parte do selo Graphic MSP, de Mauricio de Sousa Produções.",
   "Mauricio de Sousa Produções – Graphic MSP", br=True)
mc(T, "estúdios", 4, 14, "Quem dirigiu 'Toy Story', de 1995?",
   ["John Lasseter", "Steven Spielberg", "Brad Bird", "Pete Docter"], "John Lasseter",
   "John Lasseter foi um dos fundadores criativos da Pixar e dirigiu o primeiro longa do estúdio.",
   "Enciclopédia Britannica – verbete 'Toy Story'")
mc(T, "clássicos da Disney", 4, 14, "Em qual desenho de 1928, com som sincronizado, o Mickey ficou famoso pilotando um barco?",
   ["O Vapor Willie", "Fantasia", "O Aprendiz de Feiticeiro", "Plane Crazy"], "O Vapor Willie",
   "'O Vapor Willie' foi um dos primeiros desenhos com som sincronizado e lançou o Mickey ao sucesso.",
   "Enciclopédia Britannica – verbete 'Steamboat Willie'")
