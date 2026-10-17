# Perguntas novas: novelas. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "nov"

# ============================================================ FÁCEIS
mc(T, "bastidores", 1, 6, "Como se chama a pausa com propagandas no meio de um capítulo de novela?",
   ["Intervalo comercial", "Abertura", "Elenco", "Roteiro"], "Intervalo comercial",
   "Durante o intervalo comercial a emissora exibe anúncios, que ajudam a pagar a produção da novela.",
   "Enciclopédia Britannica – verbete 'Television advertising'")
tf(T, "personagens", 1, 6, "Quem faz o papel de vilão numa novela também é uma pessoa má na vida real.", False,
   "O ator apenas interpreta o personagem; fora das gravações ele é uma pessoa comum, que pode ser muito gentil.",
   "Memória Globo – verbete 'Vilões'")
mc(T, "bastidores", 1, 8, "Como se chama o episódio em que a história da novela termina?",
   ["Último capítulo", "Primeiro capítulo", "Intervalo", "Abertura"], "Último capítulo",
   "O último capítulo costuma revelar os grandes segredos da trama e reunir muita gente diante da TV.",
   "Memória Globo")
op(T, "bastidores", 1, 8, "Como se chama a parte do começo da novela, com uma música e os nomes dos atores?",
   "Abertura", ["abertura", "a abertura", "vinheta de abertura"],
   "A abertura apresenta a novela com imagens, música-tema e os créditos do elenco.",
   "Memória Globo – verbete 'Aberturas de novelas'")
mc(T, "bastidores", 1, 8, "Quem comanda as gravações de uma novela e orienta os atores em cada cena?",
   ["Diretor", "Figurante", "Maquiador", "Dublador"], "Diretor",
   "O diretor decide como cada cena será gravada e orienta a interpretação dos atores.",
   "Enciclopédia Britannica – verbete 'Director'")
mc(T, "bastidores", 1, 8, "Como se chamam as casas e ruas de mentira construídas para gravar uma novela?",
   ["Cenários", "Figurinos", "Roteiros", "Capítulos"], "Cenários",
   "Os cenários são construídos por cenógrafos para parecer lugares reais, como casas, bares e até cidades inteiras.",
   "Memória Globo – verbete 'Cenografia'")
tf(T, "trilha sonora", 1, 8, "Nas novelas, personagens importantes costumam ter uma música própria, chamada de tema.", True,
   "A música-tema toca nas cenas do personagem ou do casal e ajuda o público a reconhecê-los.",
   "Memória Globo – verbete 'Trilhas sonoras'", br=True)
mc(T, "novelas infantis", 1, 8, "Qual destas é uma novela infantil?",
   ["Carinha de Anjo", "Avenida Brasil", "Vale Tudo", "O Clone"], "Carinha de Anjo",
   "'Carinha de Anjo', exibida pelo SBT a partir de 2016, tem uma menina como protagonista.",
   "SBT – página oficial de 'Carinha de Anjo'", br=True)
mc(T, "novelas infantis", 1, 8, "Na novela 'Carrossel', do SBT, qual aluno é conhecido por viver comendo?",
   ["Jaime", "Cirilo", "Davi", "Paulo"], "Jaime",
   "Jaime Palillo é o comilão da turma da professora Helena e está sempre pensando em comida.",
   "SBT – página oficial de 'Carrossel'", br=True)
tf(T, "novelas infantis", 1, 7, "Na novela 'Chiquititas', as crianças cantam e dançam muitas músicas.", True,
   "As canções de 'Chiquititas' fizeram tanto sucesso que viraram discos e shows do elenco.",
   "SBT – página oficial de 'Chiquititas'", br=True)
tf(T, "novelas infantis", 1, 8, "Na novela 'Carrossel', a professora Helena é brava e malvada com os alunos.", False,
   "Helena é uma professora carinhosa e paciente, muito querida pela turma.",
   "SBT – página oficial de 'Carrossel'", br=True)
mc(T, "bastidores", 1, 9, "Como se chamam as roupas e os acessórios que os personagens usam numa novela?",
   ["Figurino", "Cenário", "Roteiro", "Elenco"], "Figurino",
   "O figurino é criado pelos figurinistas para combinar com a época e o jeito de cada personagem.",
   "Memória Globo – verbete 'Figurino'")
mc(T, "bastidores", 1, 10, "Como se chamam as pessoas que aparecem no fundo das cenas, sem falas importantes?",
   ["Figurantes", "Protagonistas", "Vilões", "Dubladores"], "Figurantes",
   "Os figurantes enchem as cenas de restaurantes, ruas e festas para que pareçam lugares de verdade.",
   "Enciclopédia Britannica – verbete 'Extra (acting)'")
op(T, "emissoras", 1, 10, "Em qual cidade ficam os Estúdios Globo, onde são gravadas as novelas da emissora?",
   "Rio de Janeiro", ["rio de janeiro", "rio", "no rio de janeiro", "rio de janeiro rj"],
   "Os Estúdios Globo ficam em Jacarepaguá, na Zona Oeste do Rio de Janeiro.",
   "Memória Globo – verbete 'Estúdios Globo'", br=True)
tf(T, "novelas estrangeiras", 1, 10, "As novelas mexicanas exibidas no Brasil costumam ser dubladas em português.", True,
   "Novelas como 'Maria do Bairro' e 'A Usurpadora' chegaram ao público brasileiro com dublagem em português.",
   "SBT – página oficial de novelas mexicanas", br=True)
tf(T, "novelas infantis", 1, 9, "A novela 'Cúmplices de um Resgate' foi exibida pela TV Globo.", False,
   "'Cúmplices de um Resgate' foi produzida e exibida pelo SBT, entre 2015 e 2016.",
   "SBT – página oficial de 'Cúmplices de um Resgate'", br=True)
tf(T, "novelas juvenis", 1, 10, "A série juvenil 'Malhação' ficou no ar por apenas uma temporada.", False,
   "'Malhação' estreou em 1995 e teve temporadas inéditas por cerca de 25 anos.",
   "Memória Globo – verbete 'Malhação'", br=True)
mc(T, "faixas de horário", 1, 10, "Qual faixa da TV Globo exibe à tarde reprises de novelas que já fizeram sucesso?",
   ["Vale a Pena Ver de Novo", "Sessão da Tarde", "Tela Quente", "Fantástico"], "Vale a Pena Ver de Novo",
   "O 'Vale a Pena Ver de Novo' está no ar desde 1980 e reexibe novelas antigas da emissora.",
   "Memória Globo – verbete 'Vale a Pena Ver de Novo'", br=True, ref="2026-10-13")
mc(T, "bastidores", 1, 10, "Quando a TV exibe de novo uma novela antiga, como se chama essa nova exibição?",
   ["Reprise", "Estreia", "Bastidores", "Making of"], "Reprise",
   "Na reprise, a mesma gravação é exibida outra vez, com os atores originais.",
   "Dicionário Houaiss – verbete 'reprise'")
mc(T, "novelas infantis", 1, 10, "Qual atriz mirim interpretou Dulce Maria na novela 'Carinha de Anjo', do SBT?",
   ["Lorena Queiroz", "Sophia Valverde", "Larissa Manoela", "Maisa Silva"], "Lorena Queiroz",
   "Lorena Queiroz ainda era bem pequena quando estreou como a protagonista Dulce Maria, em 2016.",
   "SBT – página oficial de 'Carinha de Anjo'", br=True)
tf(T, "faixas de horário", 1, 12, "A principal novela da Globo, antes chamada de 'novela das oito', hoje é conhecida como 'novela das nove'.", True,
   "O horário da faixa nobre passou a começar por volta das 21h, e o apelido mudou junto.",
   "Memória Globo – verbete 'Faixas de novelas'", br=True, ref="2026-10-13")
mc(T, "novelas infantis", 1, 10, "Qual atriz interpretou as gêmeas da novela 'Cúmplices de um Resgate'?",
   ["Larissa Manoela", "Sophia Valverde", "Lorena Queiroz", "Maisa Silva"], "Larissa Manoela",
   "Larissa Manoela, que antes viveu Maria Joaquina em 'Carrossel', fez os dois papéis principais.",
   "SBT – página oficial de 'Cúmplices de um Resgate'", br=True)
op(T, "bastidores", 1, 10, "Como se chama o conjunto de todos os atores de uma novela?",
   "Elenco", ["elenco", "o elenco"],
   "O elenco reúne protagonistas, coadjuvantes e participações especiais de uma produção.",
   "Dicionário Houaiss – verbete 'elenco'")
mc(T, "cenários", 1, 12, "Em qual região do Brasil fica o bioma que dá nome à novela 'Pantanal'?",
   ["Centro-Oeste", "Nordeste", "Sul", "Norte"], "Centro-Oeste",
   "O Pantanal brasileiro fica em Mato Grosso e Mato Grosso do Sul, estados do Centro-Oeste.",
   "IBGE – Biomas brasileiros", br=True)
mc(T, "novelas infantis", 1, 10, "Em 'Carrossel', do SBT, como se chamava o grupo de alunos que se unia para ajudar as pessoas?",
   ["Patrulha Salvadora", "Liga da Justiça", "Turma da Mônica", "Patrulha Canina"], "Patrulha Salvadora",
   "A Patrulha Salvadora fez tanto sucesso que ganhou uma série própria no SBT, em 2014.",
   "SBT – página oficial de 'Patrulha Salvadora'", br=True)
tf(T, "novelas infantis", 1, 10, "A novela 'Carinha de Anjo', do SBT, é uma versão brasileira de uma novela mexicana.", True,
   "Ela foi adaptada de 'Carita de Ángel', novela mexicana do ano 2000.",
   "SBT – página oficial de 'Carinha de Anjo'", br=True)
mc(T, "temas", 1, 12, "Em 'O Clone', qual religião é seguida pela protagonista Jade e sua família?",
   ["Islamismo", "Budismo", "Hinduísmo", "Judaísmo"], "Islamismo",
   "A novela mostrou costumes de famílias muçulmanas do Marrocos e do Rio de Janeiro.",
   "Memória Globo – verbete 'O Clone'", br=True)

# ============================================================ MÉDIAS
mc(T, "novelas infantis", 2, 9, "Qual atriz interpretou a protagonista de 'As Aventuras de Poliana', do SBT?",
   ["Sophia Valverde", "Larissa Manoela", "Lorena Queiroz", "Maisa Silva"], "Sophia Valverde",
   "Sophia Valverde viveu Poliana na novela de 2018 e na continuação 'Poliana Moça'.",
   "SBT – página oficial de 'As Aventuras de Poliana'", br=True)
mc(T, "bastidores", 2, 12, "Como se chama a nova versão de uma novela antiga, gravada outra vez com outro elenco?",
   ["Remake", "Reprise", "Making of", "Trailer"], "Remake",
   "No remake a história é regravada; na reprise, a gravação antiga só é exibida de novo.",
   "Enciclopédia Britannica – verbete 'Remake'")
mc(T, "novelas juvenis", 2, 12, "Quando estreou, em 1995, a série 'Malhação' se passava em que tipo de lugar?",
   ["Academia de ginástica", "Hospital", "Fazenda", "Navio"], "Academia de ginástica",
   "O nome vem de 'malhar'; só depois a trama passou a se concentrar numa escola.",
   "Memória Globo – verbete 'Malhação'", br=True)
mc(T, "novelas infantis", 2, 12, "A versão brasileira de 'Carrossel' (2012) foi inspirada numa novela de 1989 de qual país?",
   ["México", "Argentina", "Colômbia", "Portugal"], "México",
   "O SBT já tinha exibido a mexicana 'Carrusel', da Televisa, nos anos 1990.",
   "SBT – página oficial de 'Carrossel'", br=True)
mc(T, "novelas estrangeiras", 2, 12, "Qual atriz e cantora mexicana estrelou as novelas 'Maria do Bairro' e 'Marimar'?",
   ["Thalía", "Lucero", "Shakira", "Jennifer Lopez"], "Thalía",
   "Thalía protagonizou a chamada 'trilogia das Marias': 'Maria Mercedes', 'Marimar' e 'Maria do Bairro'.",
   "Enciclopédia Britannica – verbete 'Thalía'")
op(T, "história", 2, 12, "Antes de chegar à televisão, em qual meio de comunicação as novelas já faziam sucesso no Brasil?",
   "Rádio", ["rádio", "radio", "o rádio", "no rádio", "radionovela"],
   "As radionovelas reuniam famílias inteiras em volta do aparelho nos anos 1940 e 1950.",
   "Enciclopédia Itaú Cultural – verbete 'Radionovela'", br=True)
mc(T, "emissoras", 2, 12, "Qual emissora exibiu a novela juvenil 'Floribella', em 2005?",
   ["Band", "TV Globo", "SBT", "Record"], "Band",
   "'Floribella', com Juliana Silveira, foi adaptada da argentina 'Floricienta'.",
   "Band – página oficial de 'Floribella'", br=True)
mc(T, "autores", 2, 14, "Em qual bairro do Rio de Janeiro se passam muitas novelas de Manoel Carlos?",
   ["Leblon", "Madureira", "Copacabana", "Méier"], "Leblon",
   "Novelas como 'Laços de Família' e 'Mulheres Apaixonadas' mostram o cotidiano de moradores do Leblon.",
   "Memória Globo – verbete 'Manoel Carlos'", br=True)
op(T, "cenários", 2, 14, "A novela 'Renascer' se passa numa região da Bahia famosa pelo cultivo de qual fruto?",
   "Cacau", ["cacau", "o cacau"],
   "A história de José Inocêncio se passa na zona cacaueira do sul da Bahia, em 1993 e no remake de 2024.",
   "Memória Globo – verbete 'Renascer'", br=True, ref="2026-10-13")
mc(T, "faixas de horário", 2, 14, "Na Globo, qual faixa de horário é conhecida por exibir muitas novelas de época?",
   ["Novela das seis", "Novela das sete", "Novela das nove", "Novela das onze"], "Novela das seis",
   "Tramas históricas como 'Novo Mundo' e 'Orgulho e Paixão' foram exibidas no fim da tarde.",
   "Memória Globo – verbete 'Faixas de novelas'", br=True)
mc(T, "personagens", 2, 14, "Em 'O Bem-Amado', qual obra o prefeito Odorico Paraguaçu queria muito inaugurar?",
   ["Cemitério", "Estádio", "Hospital", "Ponte"], "Cemitério",
   "A graça da história é que ninguém morria na cidade, e o cemitério não podia ser inaugurado.",
   "Memória Globo – verbete 'O Bem-Amado'", br=True)
mc(T, "bordões", 2, 14, "Em 'O Clone', qual personagem, dona de um bar no subúrbio, repetia 'Não é brinquedo, não!'?",
   ["Dona Jura", "Dona Beija", "Dona Lurdes", "Dona Benta"], "Dona Jura",
   "Dona Jura, vivida por Solange Couto, transformou o bordão numa febre em 2001.",
   "Memória Globo – verbete 'O Clone'", br=True)
mc(T, "bordões", 2, 14, "Qual expressão virou bordão na novela 'Caminho das Índias' (2009)?",
   ["Are baba", "Inshallah", "Hasta la vista", "Arigatô"], "Are baba",
   "A exclamação indiana era repetida por vários personagens e caiu na boca do público.",
   "Memória Globo – verbete 'Caminho das Índias'", br=True)
mc(T, "personagens", 2, 14, "Em 'Mulheres de Areia' (1993), o que o personagem Tonho da Lua fazia na praia?",
   ["Esculturas de areia", "Castelos de cartas", "Pipas coloridas", "Redes de pesca"], "Esculturas de areia",
   "Tonho da Lua, vivido por Marcos Frota, esculpia figuras na areia da praia.",
   "Memória Globo – verbete 'Mulheres de Areia'", br=True)
mc(T, "personagens", 2, 14, "Em 'Ti Ti Ti', Jacques Leclair e Victor Valentim eram rivais em qual profissão?",
   ["Estilistas", "Chefs de cozinha", "Cabeleireiros", "Jogadores de futebol"], "Estilistas",
   "A disputa entre os dois costureiros movimentou a versão de 1985 e o remake de 2010.",
   "Memória Globo – verbete 'Ti Ti Ti'", br=True)
mc(T, "personagens", 2, 14, "Qual novela de 1991 tinha uma cantora vampira chamada Natasha?",
   ["Vamp", "Saramandaia", "Que Rei Sou Eu?", "Tieta"], "Vamp",
   "Natasha, vivida por Cláudia Ohana, chegava à cidade de Armação dos Anjos com outros vampiros.",
   "Memória Globo – verbete 'Vamp'", br=True)
mc(T, "novelas bíblicas", 2, 14, "Qual personagem bíblico lidera o povo hebreu em 'A Terra Prometida', novela da Record de 2016?",
   ["Josué", "Abraão", "Davi", "Salomão"], "Josué",
   "A novela continua a história de 'Os Dez Mandamentos', com a conquista de Canaã sob o comando de Josué.",
   "Record – página oficial de 'A Terra Prometida'", br=True)
mc(T, "adaptações", 2, 14, "A novela 'Orgulho e Paixão' (2018) foi inspirada em obras de qual escritora inglesa?",
   ["Jane Austen", "Agatha Christie", "Virginia Woolf", "Emily Brontë"], "Jane Austen",
   "O título lembra 'Orgulho e Preconceito', e a trama mistura personagens de vários livros de Jane Austen.",
   "Memória Globo – verbete 'Orgulho e Paixão'", br=True)
mc(T, "remakes", 2, 14, "Qual atriz interpretou a protagonista no remake de 'Gabriela', exibido pela Globo em 2012?",
   ["Juliana Paes", "Sônia Braga", "Taís Araújo", "Camila Pitanga"], "Juliana Paes",
   "Sônia Braga fez a versão de 1975; o remake de 2012, adaptado por Walcyr Carrasco, teve Juliana Paes.",
   "Memória Globo – verbete 'Gabriela (2012)'", br=True)
mc(T, "personagens", 2, 14, "Em 'Êta Mundo Bom!' (2016), qual era o nome do caipira ingênuo vivido por Sérgio Guizé?",
   ["Candinho", "Tião", "Chicó", "Juvenal"], "Candinho",
   "Walcyr Carrasco se inspirou no Cândido, do filósofo Voltaire, para criar o otimista Candinho.",
   "Memória Globo – verbete 'Êta Mundo Bom!'", br=True)
mc(T, "bordões", 2, 16, "Qual bordão era repetido por Sinhozinho Malta em 'Roque Santeiro'?",
   ["Tô certo ou tô errado?", "Ô loco, meu!", "Haja coração!", "Cala a boca, Magda!"], "Tô certo ou tô errado?",
   "Lima Duarte balançava as pulseiras e repetia a pergunta, que virou expressão popular.",
   "Memória Globo – verbete 'Roque Santeiro'", br=True)
mc(T, "vilões", 2, 16, "Em 'Vale Tudo' (1988), qual era o nome da filha ambiciosa de Raquel, vivida por Glória Pires?",
   ["Maria de Fátima", "Maria do Carmo", "Maria Clara", "Maria Joaquina"], "Maria de Fátima",
   "Maria de Fátima vende a casa da mãe e foge para tentar a vida no Rio de Janeiro.",
   "Memória Globo – verbete 'Vale Tudo'", br=True)
tf(T, "remakes", 2, 14, "A TV Globo exibiu um remake da novela 'Vale Tudo' em 2025.", True,
   "A nova versão, escrita por Manuela Dias, teve Débora Bloch como Odete Roitman.",
   "Memória Globo – verbete 'Vale Tudo (2025)'", br=True, ref="2026-10-13")
op(T, "personagens", 2, 16, "Em 'Império' (2014), qual era o apelido de José Alfredo, vivido por Alexandre Nero?",
   "Comendador", ["comendador", "o comendador", "comendador josé alfredo"],
   "O Comendador comandava um império de joias, e a novela ganhou o Emmy Internacional em 2015.",
   "Memória Globo – verbete 'Império'", br=True)

# ============================================================ DIFÍCEIS
mc(T, "trilha sonora", 3, 16, "Quem compôs e cantou 'Pecado Capital', música de abertura da novela de 1975?",
   ["Paulinho da Viola", "Chico Buarque", "Martinho da Vila", "Cartola"], "Paulinho da Viola",
   "A canção, que diz 'dinheiro na mão é vento', abria a novela de Janete Clair.",
   "Memória Globo – verbete 'Pecado Capital'", br=True)
mc(T, "trilha sonora", 3, 16, "Qual grupo cantava a música de abertura da novela 'Dancin' Days', de 1978?",
   ["As Frenéticas", "Rouge", "Blitz", "Os Paralamas do Sucesso"], "As Frenéticas",
   "A novela de Gilberto Braga levou a febre das discotecas para todo o país.",
   "Memória Globo – verbete 'Dancin' Days'", br=True)
mc(T, "vilões", 3, 16, "Em 'Celebridade' (2003), qual era o nome da vilã de Cláudia Abreu, que invejava Maria Clara Diniz?",
   ["Laura", "Flora", "Carminha", "Nazaré"], "Laura",
   "Laura tentava destruir a vida da empresária vivida por Malu Mader na novela de Gilberto Braga.",
   "Memória Globo – verbete 'Celebridade'", br=True)
mc(T, "tramas", 3, 16, "Em 'Por Amor' (1997), o que Helena faz com o bebê da filha, que morre ao nascer?",
   ["Troca pelo próprio bebê", "Leva para o exterior", "Entrega para adoção", "Esconde num convento"], "Troca pelo próprio bebê",
   "Helena, vivida por Regina Duarte, troca os recém-nascidos para poupar a filha Maria Eduarda do sofrimento.",
   "Memória Globo – verbete 'Por Amor'", br=True)
mc(T, "personagens", 3, 16, "Em 'O Rei do Gado' (1996), qual família de origem italiana era inimiga dos Mezenga?",
   ["Berdinazzi", "Tedesco", "Roitman", "Paraguaçu"], "Berdinazzi",
   "A briga entre as duas famílias de imigrantes começou na primeira fase e atravessou gerações.",
   "Memória Globo – verbete 'O Rei do Gado'", br=True)
op(T, "emissoras", 3, 16, "Qual era o antigo nome dos Estúdios Globo, em Jacarepaguá?",
   "Projac", ["projac", "pro jac", "projeto jacarepaguá", "projeto jacarepagua"],
   "O nome era a abreviação de 'Projeto Jacarepaguá', bairro da Zona Oeste do Rio.",
   "Memória Globo – verbete 'Estúdios Globo'", br=True)
tf(T, "remakes", 3, 16, "O remake de 'Pantanal', exibido em 2022, foi escrito por Bruno Luperi, neto de Benedito Ruy Barbosa.", True,
   "Bruno Luperi adaptou a história criada pelo avô para a Rede Manchete em 1990.",
   "Memória Globo – verbete 'Pantanal (2022)'", br=True)
mc(T, "cenas famosas", 3, 16, "Em qual novela de 1983 Fernanda Montenegro e Paulo Autran fizeram uma famosa guerra de comida no café da manhã?",
   ["Guerra dos Sexos", "Vale Tudo", "Roque Santeiro", "Ti Ti Ti"], "Guerra dos Sexos",
   "Na cena da novela de Silvio de Abreu, os primos Charlô e Otávio atiram comida um no outro.",
   "Memória Globo – verbete 'Guerra dos Sexos'", br=True)
mc(T, "tramas", 3, 16, "Em 'Torre de Babel' (1998), que tipo de lugar explode no meio da novela?",
   ["Shopping center", "Hospital", "Estádio de futebol", "Aeroporto"], "Shopping center",
   "A explosão do shopping, na novela de Silvio de Abreu, criou um mistério sobre quem era o culpado.",
   "Memória Globo – verbete 'Torre de Babel'", br=True)
mc(T, "aberturas", 3, 16, "Qual designer austríaco criou o logotipo da Globo e muitas aberturas de novelas?",
   ["Hans Donner", "Oscar Niemeyer", "Romero Britto", "Ziraldo"], "Hans Donner",
   "Hans Donner chegou à emissora nos anos 1970 e marcou a identidade visual da TV brasileira.",
   "Memória Globo – verbete 'Hans Donner'", br=True)
tf(T, "emissoras", 3, 16, "A novela 'Xica da Silva', de 1996, com Taís Araújo, foi exibida pela TV Globo.", False,
   "'Xica da Silva' foi um sucesso da Rede Manchete e lançou Taís Araújo como protagonista.",
   "Enciclopédia Itaú Cultural – verbete 'Xica da Silva (telenovela)'", br=True)
tf(T, "remakes", 3, 16, "A novela 'Mulheres de Areia', de 1993, foi a primeira versão dessa história na TV.", False,
   "Ivani Ribeiro já tinha escrito 'Mulheres de Areia' para a TV Tupi, em 1973.",
   "Memória Globo – verbete 'Mulheres de Areia'", br=True)

# ============================================================ MUITO DIFÍCEIS
tf(T, "emissoras", 4, 16, "A novela 'Os Imigrantes', de Benedito Ruy Barbosa, foi exibida pela TV Tupi em 1981.", False,
   "'Os Imigrantes' foi produzida pela Band; a Tupi já tinha saído do ar em 1980.",
   "Band – história da emissora", br=True)
mc(T, "história", 4, 16, "A novela 'O Direito de Nascer', sucesso da TV Tupi nos anos 1960, veio de uma radionovela de qual país?",
   ["Cuba", "Argentina", "México", "Venezuela"], "Cuba",
   "A história foi criada pelo cubano Félix B. Caignet e virou um fenômeno em toda a América Latina.",
   "Enciclopédia Itaú Cultural – verbete 'O Direito de Nascer'", br=True)
mc(T, "cidades fictícias", 4, 16, "Em qual cidade fictícia, cheia de manias inglesas, se passava a novela 'A Indomada' (1997)?",
   ["Greenville", "Asa Branca", "Sucupira", "Santana do Agreste"], "Greenville",
   "A cidade nordestina inventada por Aguinaldo Silva e Ricardo Linhares misturava sotaque local e palavras em inglês.",
   "Memória Globo – verbete 'A Indomada'", br=True)
mc(T, "cidades fictícias", 4, 16, "Como se chamava o reino fictício onde se passava a novela 'Que Rei Sou Eu?' (1989)?",
   ["Avilan", "Arendelle", "Nárnia", "Genóvia"], "Avilan",
   "A novela de Cassiano Gabus Mendes satirizava a política usando um reino europeu do século 18.",
   "Memória Globo – verbete 'Que Rei Sou Eu?'", br=True)
mc(T, "adaptações", 4, 16, "A novela 'Éramos Seis' foi adaptada do livro de qual escritora?",
   ["Maria José Dupré", "Rachel de Queiroz", "Lygia Fagundes Telles", "Cecília Meireles"], "Maria José Dupré",
   "O romance de 1943 sobre Dona Lola e seus filhos ganhou várias versões na TV, a mais recente na Globo em 2019.",
   "Enciclopédia Itaú Cultural – verbete 'Maria José Dupré'", br=True, ref="2026-10-13")
