# Perguntas novas: curiosidades. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "cur"

# =========================================================== FÁCEIS
mc(T, "objetos do dia a dia", 1, 7, "Qual fecho de roupa tem duas fileiras de dentinhos que se encaixam quando puxamos um cursor?",
   ["Zíper", "Botão", "Velcro", "Colchete"], "Zíper",
   "O zíper moderno foi aperfeiçoado em 1913 pelo engenheiro Gideon Sundback e hoje fecha roupas, bolsas e mochilas.",
   "Enciclopédia Britannica – verbete 'Zipper'")
mc(T, "brinquedos", 1, 6, "Qual brinquedo em forma de argola a gente gira na cintura sem deixar cair?",
   ["Bambolê", "Pião", "Ioiô", "Peteca"], "Bambolê",
   "O bambolê de plástico virou febre no mundo inteiro em 1958.",
   "Enciclopédia Britannica – verbete 'Hula hoop'")
op(T, "brinquedos", 1, 6, "Qual brinquedo sobe e desce preso a um barbante enrolado no dedo?",
   "Ioiô", ["ioiô", "ioio", "io-io", "iô-iô"],
   "O ioiô é um dos brinquedos mais antigos do mundo: já aparecia em vasos da Grécia Antiga.",
   "Enciclopédia Britannica – verbete 'Yo-yo'")
mc(T, "brinquedos", 1, 6, "Como se chama o jogo de juntar pecinhas recortadas até formar uma figura inteira?",
   ["Quebra-cabeça", "Dominó", "Damas", "Bingo"], "Quebra-cabeça",
   "Os primeiros quebra-cabeças foram feitos na Inglaterra, por volta de 1760, com mapas colados em madeira para ensinar geografia.",
   "Enciclopédia Britannica – verbete 'Jigsaw puzzle'")
mc(T, "datas comemorativas", 1, 6, "Na tradição da Páscoa, qual animal entrega ovos de chocolate para as crianças?",
   ["Coelho", "Cachorro", "Gato", "Pato"], "Coelho",
   "O coelho, que tem muitos filhotes, é símbolo de vida nova e virou o mensageiro dos ovos de Páscoa.",
   "Enciclopédia Britannica – verbete 'Easter Bunny'")
mc(T, "datas comemorativas", 1, 6, "Quais animais puxam o trenó do Papai Noel?",
   ["Renas", "Cavalos", "Cachorros", "Bois"], "Renas",
   "Renas são parentes dos cervos e vivem em lugares muito frios, como a Lapônia, no norte da Europa.",
   "Enciclopédia Britannica – verbete 'Santa Claus'")
tf(T, "datas comemorativas", 1, 6, "Na festa de aniversário, é tradição o aniversariante assoprar as velinhas do bolo.", True,
   "Depois do 'Parabéns', o aniversariante apaga as velinhas com um sopro, e muita gente faz um pedido em silêncio.",
   "Enciclopédia Britannica – verbete 'Birthday'")
op(T, "profissões", 1, 6, "Qual profissional entrega cartas e encomendas nas casas das pessoas?",
   "Carteiro", ["carteiro", "carteira", "o carteiro", "a carteira"],
   "No Brasil, as cartas são entregues pelos carteiros dos Correios.",
   "Correios")
mc(T, "comidas", 1, 6, "Qual sobremesa gelada costuma ser servida numa casquinha crocante?",
   ["Sorvete", "Pudim", "Gelatina", "Brigadeiro"], "Sorvete",
   "A casquinha é feita de massa de biscoito e pode ser comida junto com o sorvete.",
   "Enciclopédia Britannica – verbete 'Ice cream'")
mc(T, "datas comemorativas", 1, 6, "Qual árvore costuma ser enfeitada com bolas e luzinhas no Natal?",
   ["Pinheiro", "Coqueiro", "Bananeira", "Mangueira"], "Pinheiro",
   "O pinheiro continua verde mesmo no inverno europeu e, por isso, virou símbolo de vida no Natal.",
   "Enciclopédia Britannica – verbete 'Christmas tree'")
tf(T, "datas comemorativas", 1, 7, "Segundo a tradição, o Papai Noel mora no Polo Sul.", False,
   "Pela tradição, o Papai Noel mora no Polo Norte, de onde sai com seu trenó na noite de Natal.",
   "Enciclopédia Britannica – verbete 'Santa Claus'")
mc(T, "calendário", 1, 7, "Qual é o mês mais curto do ano?",
   ["Fevereiro", "Abril", "Junho", "Novembro"], "Fevereiro",
   "Fevereiro tem 28 dias, ou 29 nos anos bissextos; abril, junho e novembro têm 30.",
   "Observatório Nacional – Calendário")
op(T, "números e contagens", 1, 7, "Quantas unidades tem meia dúzia?",
   "6", ["6", "seis"],
   "Uma dúzia tem doze unidades, então meia dúzia tem seis, como meia dúzia de ovos.",
   "Dicionário Michaelis – verbete 'dúzia'")
mc(T, "profissões", 1, 7, "Qual profissional cuida da saúde dos animais?",
   ["Veterinário", "Dentista", "Pediatra", "Farmacêutico"], "Veterinário",
   "O veterinário cuida de bichos de estimação, de animais de fazenda e até de animais de zoológico.",
   "Conselho Federal de Medicina Veterinária (CFMV)")
mc(T, "objetos do dia a dia", 1, 8, "Qual objeto de vidro mede o tempo com areia escorrendo de um lado para o outro?",
   ["Ampulheta", "Bússola", "Termômetro", "Luneta"], "Ampulheta",
   "A areia leva sempre o mesmo tempo para passar pelo gargalo estreito, por isso a ampulheta marca um intervalo certo.",
   "Enciclopédia Britannica – verbete 'Hourglass'")
mc(T, "datas comemorativas", 1, 8, "Em qual mês se comemora o Dia das Mães no Brasil?",
   ["Maio", "Março", "Agosto", "Dezembro"], "Maio",
   "Desde 1932, o Dia das Mães no Brasil é comemorado no segundo domingo de maio.",
   "Decreto nº 21.366, de 5 de maio de 1932", br=True)
mc(T, "datas comemorativas", 1, 8, "Em qual dia o Brasil comemora o Dia das Crianças?",
   ["12 de outubro", "1º de junho", "20 de novembro", "25 de dezembro"], "12 de outubro",
   "A data foi oficializada por decreto em 1924 e coincide com o feriado de Nossa Senhora Aparecida.",
   "Decreto nº 4.867, de 1924", br=True)
mc(T, "costumes", 1, 8, "No Brasil, qual cor de roupa muita gente veste na noite de Ano-Novo, pedindo paz?",
   ["Branco", "Preto", "Roxo", "Marrom"], "Branco",
   "O branco simboliza a paz, e vestir essa cor na virada é um dos costumes de Ano-Novo mais populares do Brasil.",
   "Agência Brasil – tradições de Réveillon", br=True)
mc(T, "jogos", 1, 8, "Quantas casas tem o tabuleiro do jogo da velha?",
   ["9", "6", "12", "16"], "9",
   "O jogo da velha tem três linhas e três colunas, e vence quem completa uma fileira primeiro.",
   "Enciclopédia Britannica – verbete 'Tic-tac-toe'")
mc(T, "datas comemorativas", 1, 8, "Qual festa de 31 de outubro, muito comemorada nos Estados Unidos, tem fantasias e abóboras com rostos iluminados?",
   ["Halloween", "Carnaval", "Festa Junina", "Páscoa"], "Halloween",
   "No Halloween, também chamado de Dia das Bruxas, as crianças se fantasiam e pedem doces de porta em porta.",
   "Enciclopédia Britannica – verbete 'Halloween'", syn=["dia das bruxas"])
op(T, "calendário", 1, 8, "Quantos dias tem o mês de dezembro?",
   "31", ["31", "trinta e um"],
   "Dezembro, o último mês do ano, tem 31 dias, e o seu dia 31 é a véspera de Ano-Novo.",
   "Observatório Nacional – Calendário")
mc(T, "profissões", 1, 8, "Como se chama o profissional que conserta relógios?",
   ["Relojoeiro", "Sapateiro", "Encanador", "Marceneiro"], "Relojoeiro",
   "O relojoeiro trabalha com peças minúsculas, usando pinças e uma lupa presa ao olho.",
   "Classificação Brasileira de Ocupações (CBO)")
mc(T, "jogos", 1, 8, "Qual jogo tem peças retangulares marcadas com pontinhos, encaixadas pelas pontas que têm o mesmo número?",
   ["Dominó", "Xadrez", "Damas", "Baralho"], "Dominó",
   "No dominó, cada peça tem duas metades com pontinhos, e o jogador encaixa números iguais lado a lado.",
   "Enciclopédia Britannica – verbete 'Dominoes'")
tf(T, "mitos populares", 1, 9, "Pegar num sapo faz nascer verruga na mão.", False,
   "As verrugas são causadas por um vírus, o HPV, que passa de pessoa para pessoa; os sapos não transmitem verrugas.",
   "Sociedade Brasileira de Dermatologia – Verrugas")
mc(T, "calendário", 1, 9, "Quantos meses tem um semestre?",
   ["6", "3", "4", "12"], "6",
   "Semestre é um período de seis meses; por isso o ano tem dois semestres.",
   "Dicionário Michaelis – verbete 'semestre'")
tf(T, "datas comemorativas", 1, 9, "No Brasil, o Dia dos Pais é comemorado no segundo domingo de agosto.", True,
   "A data começou a ser comemorada no Brasil em 1953 e se fixou no segundo domingo de agosto.",
   "Memória O Globo – Dia dos Pais", br=True)
tf(T, "idiomas", 1, 9, "O Brasil é o único país da América do Sul que tem o português como língua oficial.", True,
   "Os vizinhos falam principalmente espanhol; a Guiana tem o inglês e o Suriname, o holandês.",
   "CIA World Factbook", br=True)

# =========================================================== MÉDIAS
mc(T, "invenções", 2, 12, "O velcro foi inventado por um engenheiro suíço que se inspirou em quê?",
   ["Carrapichos presos no pelo do seu cachorro", "Patas de lagartixa", "Teias de aranha", "Escamas de peixe"],
   "Carrapichos presos no pelo do seu cachorro",
   "George de Mestral viu no microscópio os ganchinhos dos carrapichos presos no pelo do cachorro e copiou a ideia.",
   "Lemelson-MIT – inventor George de Mestral")
mc(T, "calendário", 2, 10, "Quantos meses do ano têm 31 dias?",
   ["7", "6", "5", "8"], "7",
   "Têm 31 dias janeiro, março, maio, julho, agosto, outubro e dezembro.",
   "Observatório Nacional – Calendário")
op(T, "calendário", 2, 10, "Em qual dia e mês nasceu quem só tem aniversário 'de verdade' de quatro em quatro anos?",
   "29 de fevereiro", ["29 de fevereiro", "vinte e nove de fevereiro", "29/02", "dia 29 de fevereiro"],
   "O dia 29 de fevereiro só existe nos anos bissextos, por isso quem nasce nele comemora em 28 de fevereiro ou 1º de março nos outros anos.",
   "Observatório Nacional – Ano bissexto")
mc(T, "costumes", 2, 10, "Na virada do ano, muita gente na praia pula quantas ondas para dar sorte?",
   ["7", "3", "10", "12"], "7",
   "Pular sete ondas é uma simpatia de Réveillon muito popular no litoral brasileiro, com um pedido a cada onda.",
   "Agência Brasil – tradições de Réveillon", br=True)
mc(T, "maravilhas do mundo", 2, 12, "Qual das sete maravilhas do mundo antigo é a única que ainda existe?",
   ["Grande Pirâmide de Gizé", "Farol de Alexandria", "Colosso de Rodes", "Jardins Suspensos da Babilônia"],
   "Grande Pirâmide de Gizé",
   "Construída há cerca de 4.500 anos no Egito, a Grande Pirâmide é a mais antiga das sete maravilhas e a única que resistiu.",
   "Enciclopédia Britannica – verbete 'Seven Wonders of the World'")
mc(T, "bandeiras", 2, 10, "Qual figura aparece no centro da bandeira da Argentina?",
   ["Sol", "Estrela", "Lua", "Águia"], "Sol",
   "O desenho é o Sol de Maio, com rosto humano, entre duas faixas azul-claras e uma branca.",
   "Enciclopédia Britannica – verbete 'Flag of Argentina'")
tf(T, "bandeiras", 2, 12, "As cores principais da bandeira de Portugal são o verde e o vermelho.", True,
   "A bandeira portuguesa é verde e vermelha, com a esfera armilar e o escudo de Portugal no meio.",
   "Presidência da República Portuguesa – Símbolos Nacionais")
tf(T, "mitos populares", 2, 12, "O touro ataca a capa do toureiro porque fica furioso com a cor vermelha.", False,
   "Os touros não distinguem bem o vermelho; o que provoca o ataque é o movimento da capa.",
   "Discovery Channel – MythBusters, episódio 'Red Rag to a Bull'")
tf(T, "objetos do dia a dia", 2, 10, "A ponta do lápis é feita de chumbo.", False,
   "A ponta é de grafite misturado com argila; o nome 'chumbo' vem de uma confusão antiga entre os dois materiais.",
   "Enciclopédia Britannica – verbete 'Pencil'")
mc(T, "números e contagens", 2, 12, "Quantas horas tem uma semana inteira?",
   ["168", "144", "120", "186"], "168",
   "São sete dias de 24 horas cada: sete vezes vinte e quatro dá cento e sessenta e oito.",
   "Observatório Nacional – Hora Legal Brasileira")
mc(T, "datas comemorativas", 2, 12, "Em qual país a tradição da árvore de Natal enfeitada ganhou força antes de se espalhar pelo mundo?",
   ["Alemanha", "Brasil", "Egito", "México"], "Alemanha",
   "O costume de enfeitar pinheiros no Natal surgiu na região da atual Alemanha e se espalhou a partir do século 19.",
   "Enciclopédia Britannica – verbete 'Christmas tree'")
op(T, "calendário", 2, 9, "Como se chama um período de quinze dias?",
   "Quinzena", ["quinzena", "uma quinzena"],
   "Quinzena vem de 'quinze', e um mês tem mais ou menos duas quinzenas.",
   "Dicionário Michaelis – verbete 'quinzena'")
tf(T, "mitos populares", 2, 12, "Os vikings usavam capacetes com chifres nas batalhas.", False,
   "Não há prova de capacetes com chifres em batalha; essa imagem ficou famosa com figurinos de óperas do século 19.",
   "Enciclopédia Britannica – verbete 'Viking'")
mc(T, "dinheiro", 2, 10, "Qual animal aparece na nota de dois reais?",
   ["Tartaruga-marinha", "Garça", "Arara", "Mico-leão-dourado"], "Tartaruga-marinha",
   "Cada cédula do real traz um animal da fauna brasileira, e a de dois reais mostra a tartaruga-marinha.",
   "Banco Central do Brasil – Cédulas do real", br=True)
tf(T, "monumentos", 2, 12, "A Estátua da Liberdade é verde porque foi pintada dessa cor.", False,
   "Ela é revestida de cobre, que tinha cor de moeda nova e ficou verde com o tempo por causa da oxidação, a chamada pátina.",
   "National Park Service – Statue of Liberty")
mc(T, "comidas", 2, 10, "De qual país é originário o panetone, pão doce muito comido no Natal?",
   ["Itália", "Portugal", "França", "Alemanha"], "Itália",
   "O panetone nasceu em Milão, no norte da Itália, e chegou ao Brasil com os imigrantes italianos.",
   "Enciclopédia Britannica – verbete 'Panettone'")
mc(T, "museus", 2, 12, "Em qual cidade fica o Museu do Amanhã, que trata de ciência e do futuro do planeta?",
   ["Rio de Janeiro", "São Paulo", "Curitiba", "Salvador"], "Rio de Janeiro",
   "O Museu do Amanhã foi inaugurado em 2015, na Praça Mauá, na zona portuária do Rio de Janeiro.",
   "Museu do Amanhã", br=True)
tf(T, "idiomas", 2, 10, "A Libras, língua de sinais usada por pessoas surdas no Brasil, é reconhecida por uma lei federal.", True,
   "A Lei nº 10.436, de 2002, reconhece a Língua Brasileira de Sinais como meio legal de comunicação e expressão.",
   "Planalto – Lei nº 10.436/2002", br=True)
mc(T, "idiomas", 2, 12, "Qual língua foi criada no século 19 para ser um idioma internacional fácil de aprender?",
   ["Esperanto", "Latim", "Sânscrito", "Tupi"], "Esperanto",
   "O esperanto foi lançado em 1887 pelo médico polonês Ludwik Zamenhof.",
   "Enciclopédia Britannica – verbete 'Esperanto'")
mc(T, "ilhas famosas", 2, 12, "A qual país pertence a Ilha de Páscoa, famosa pelas enormes estátuas de pedra chamadas moais?",
   ["Chile", "Peru", "México", "Nova Zelândia"], "Chile",
   "A ilha ganhou esse nome porque o navegador holandês Jacob Roggeveen chegou lá num domingo de Páscoa, em 1722.",
   "Enciclopédia Britannica – verbete 'Easter Island'")
mc(T, "datas comemorativas", 2, 12, "A melodia do 'Parabéns a você' veio de uma canção americana feita originalmente para quê?",
   ["Dar bom-dia aos alunos na escola", "Ninar bebês", "Comemorar o Ano-Novo", "Animar jogos de beisebol"],
   "Dar bom-dia aos alunos na escola",
   "A melodia é de 'Good Morning to All', canção escolar publicada em 1893 pelas irmãs Mildred e Patty Hill.",
   "Enciclopédia Britannica – verbete 'Happy Birthday to You'")
mc(T, "profissões", 2, 12, "Como se chama o profissional que desenha mapas?",
   ["Cartógrafo", "Calígrafo", "Geólogo", "Arquiteto"], "Cartógrafo",
   "A cartografia é a ciência de fazer mapas, e no Brasil o IBGE produz os mapas oficiais do país.",
   "IBGE – Cartografia")
mc(T, "documentos", 2, 12, "Quantos algarismos tem o número do CPF, contando os dois dígitos finais de verificação?",
   ["11", "8", "9", "13"], "11",
   "O CPF tem nove algarismos de base e mais dois dígitos verificadores, que ajudam a detectar erros de digitação.",
   "Receita Federal", br=True)

# =========================================================== DIFÍCEIS
mc(T, "objetos do dia a dia", 3, 12, "Na China antiga, as primeiras escovas de dentes com cerdas usavam pelos de qual animal?",
   ["Porco", "Cavalo", "Coelho", "Ovelha"], "Porco",
   "Por volta de 1498, os chineses prendiam pelos duros do pescoço de porcos num cabo de osso ou bambu.",
   "Biblioteca do Congresso dos EUA – Everyday Mysteries: 'Who invented the toothbrush?'")
mc(T, "objetos do dia a dia", 3, 12, "Antes da borracha de apagar, o que as pessoas costumavam usar para apagar traços de lápis?",
   ["Miolo de pão", "Folha de alface", "Casca de banana", "Sabão"], "Miolo de pão",
   "Até o século 18 usava-se miolo de pão; por volta de 1770 se descobriu que a borracha apagava melhor o grafite.",
   "Enciclopédia Britannica – verbete 'Rubber'")
mc(T, "museus", 3, 12, "Qual pedra antiga, exposta no Museu Britânico, ajudou a decifrar os hieróglifos egípcios?",
   ["Pedra de Roseta", "Pedra do Sol", "Pedra Filosofal", "Pedra do Ingá"], "Pedra de Roseta",
   "Ela traz o mesmo texto em hieróglifos, em demótico e em grego, o que permitiu a Champollion decifrar a escrita egípcia em 1822.",
   "Museu Britânico – Rosetta Stone")
mc(T, "brinquedos", 3, 14, "O cubo mágico foi inventado em 1974 por um professor de qual país?",
   ["Hungria", "Japão", "Alemanha", "Estados Unidos"], "Hungria",
   "Ernő Rubik, professor de design em Budapeste, criou o cubo para ajudar seus alunos a entender o movimento no espaço.",
   "Enciclopédia Britannica – verbete 'Rubik's Cube'")
mc(T, "bandeiras", 3, 14, "Qual árvore aparece no centro da bandeira do Líbano?",
   ["Cedro", "Palmeira", "Oliveira", "Carvalho"], "Cedro",
   "O cedro-do-líbano, verde entre duas faixas vermelhas, é símbolo do país desde a Antiguidade.",
   "CIA World Factbook – Lebanon")
mc(T, "museus", 3, 14, "Como é mais conhecido o Museu Paulista, construído em São Paulo perto do local onde foi proclamada a Independência?",
   ["Museu do Ipiranga", "Museu Imperial", "Museu Nacional", "Museu do Amanhã"], "Museu do Ipiranga",
   "O prédio foi inaugurado em 1895 e reaberto em 2022, depois de uma grande reforma para o Bicentenário da Independência.",
   "Museu Paulista da USP", br=True)
mc(T, "museus", 3, 14, "Qual cidade tem o Museu Oscar Niemeyer, apelidado de 'Museu do Olho' por causa do formato de um de seus prédios?",
   ["Curitiba", "Brasília", "Belo Horizonte", "Niterói"], "Curitiba",
   "O Museu Oscar Niemeyer fica na capital do Paraná, e seu prédio mais famoso lembra um grande olho suspenso.",
   "Museu Oscar Niemeyer (MON)", br=True)
mc(T, "documentos", 3, 12, "Quantos algarismos tem o CEP usado nos endereços do Brasil?",
   ["8", "5", "6", "10"], "8",
   "Os cinco primeiros algarismos indicam região e cidade, e os três últimos apontam ruas ou locais específicos.",
   "Correios – Código de Endereçamento Postal", br=True)
mc(T, "museus", 3, 12, "Em qual cidade fica o Museu da Língua Portuguesa, instalado numa antiga estação de trem?",
   ["São Paulo", "Rio de Janeiro", "Salvador", "Brasília"], "São Paulo",
   "O museu fica na Estação da Luz e foi reaberto em 2021, depois de um incêndio em 2015.",
   "Museu da Língua Portuguesa", br=True)
mc(T, "datas comemorativas", 3, 12, "O Dia Nacional do Livro Infantil, em 18 de abril, homenageia o nascimento de qual escritor?",
   ["Monteiro Lobato", "Ziraldo", "Ruth Rocha", "Cecília Meireles"], "Monteiro Lobato",
   "Monteiro Lobato, criador do Sítio do Picapau Amarelo, nasceu em 18 de abril de 1882, em Taubaté.",
   "Planalto – Lei nº 10.402/2002", br=True)
tf(T, "museus", 3, 14, "O Museu Nacional, no Rio de Janeiro, funciona num palácio onde morou a família imperial brasileira.", True,
   "O museu ocupa o Paço de São Cristóvão, na Quinta da Boa Vista, que foi residência de Dom Pedro I e Dom Pedro II.",
   "Museu Nacional/UFRJ", br=True)
op(T, "telefone", 3, 12, "Como se chama o código de dois algarismos discado antes do número para ligar para outra cidade do Brasil?",
   "DDD", ["ddd", "código ddd", "código de área", "discagem direta a distância"],
   "DDD quer dizer Discagem Direta a Distância; o de São Paulo capital, por exemplo, é 11.",
   "Anatel – Códigos Nacionais", br=True)

# =========================================================== MUITO DIFÍCEIS
mc(T, "objetos do dia a dia", 4, 14, "O chicle, goma usada nos primeiros chicletes, é a seiva de qual árvore da América Central?",
   ["Sapotizeiro", "Seringueira", "Mogno", "Cacaueiro"], "Sapotizeiro",
   "O chicle vem do sapotizeiro, a mesma árvore que dá o sapoti, e era mascado pelos maias muito antes da goma industrial.",
   "Enciclopédia Britannica – verbete 'Chicle'")
mc(T, "bandeiras", 4, 14, "Segundo o Guinness, qual país tem a bandeira nacional mais antiga em uso contínuo, com uma cruz branca sobre fundo vermelho?",
   ["Dinamarca", "Suécia", "Noruega", "Finlândia"], "Dinamarca",
   "A bandeira dinamarquesa, chamada Dannebrog, é usada há séculos e inspirou as cruzes das bandeiras nórdicas vizinhas.",
   "Guinness World Records – Oldest national flag", ref="2026-10-13")
mc(T, "idiomas", 4, 16, "Qual bispo do século 6 é lembrado por dar aos dias da semana em português nomes como 'segunda-feira' e 'terça-feira'?",
   ["Martinho de Dume", "Santo Agostinho", "Padre Antônio Vieira", "José de Anchieta"], "Martinho de Dume",
   "Ele propôs trocar os nomes ligados a deuses pagãos por 'feiras' numeradas, e por isso o português conta os dias da semana.",
   "Ciberdúvidas da Língua Portuguesa – origem dos nomes dos dias da semana")
tf(T, "calendário", 4, 14, "O ano de 1900 foi bissexto.", False,
   "Anos terminados em 00 só são bissextos se forem divisíveis por 400; por isso 2000 foi bissexto, mas 1900 não.",
   "Observatório Nacional – Ano bissexto")
mc(T, "objetos curiosos", 4, 16, "Como ficou conhecido o primeiro selo postal do Brasil, lançado em 1843?",
   ["Olho-de-boi", "Olho-de-cabra", "Olho-de-gato", "Olho-de-peixe"], "Olho-de-boi",
   "O apelido veio do desenho dos números grandes e arredondados dentro de uma moldura oval, que lembravam olhos de boi.",
   "Correios – Museu Correios: selo Olho-de-boi", br=True)
tf(T, "hinos", 4, 14, "O hino nacional da Espanha, a 'Marcha Real', não tem letra oficial.", True,
   "A 'Marcha Real' é só instrumental, por isso os espanhóis não cantam o hino nas cerimônias oficiais.",
   "La Moncloa (Governo da Espanha) – Himno Nacional")
