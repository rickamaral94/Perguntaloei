# Perguntas novas (parte 6b). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== CIÊNCIA
C = "cie"
mc(C, "física", 1, 6, "O que acontece com um cubo de gelo deixado fora da geladeira num dia quente?",
   ["Derrete", "Fica mais duro", "Vira pedra", "Fica maior"], "Derrete",
   "Com o calor, o gelo passa do estado sólido para o líquido, o que se chama fusão.",
   "Enciclopédia Britannica – verbete 'Melting'")
tf(C, "química", 1, 6, "A água do mar é salgada.", True,
   "A água do mar tem em média cerca de 3,5% de sais dissolvidos, principalmente cloreto de sódio.",
   "NOAA – National Ocean Service")
mc(C, "física", 1, 7, "Qual destes objetos flutua na água?",
   ["Rolha de cortiça", "Moeda", "Prego", "Pedra"], "Rolha de cortiça",
   "A cortiça é bem menos densa que a água, por isso boia.",
   "Enciclopédia Britannica – verbete 'Buoyancy'")
mc(C, "física", 1, 7, "De que cor vemos o céu num dia limpo e ensolarado?",
   ["Azul", "Verde", "Vermelho", "Roxo"], "Azul",
   "O ar espalha mais a luz azul do Sol do que as outras cores, e por isso o céu parece azul.",
   "NASA – Space Place")
tf(C, "química", 2, 10, "O vidro comum é feito principalmente a partir de areia.", True,
   "A areia é rica em sílica, que derretida em altíssima temperatura vira vidro.",
   "Enciclopédia Britannica – verbete 'Glass'")
mc(C, "física", 2, 10, "Qual fenômeno forma as gotinhas de água do lado de fora de um copo bem gelado?",
   ["Condensação", "Evaporação", "Fusão", "Solidificação"], "Condensação",
   "O vapor de água do ar esfria ao tocar o copo e volta a ser líquido.",
   "Enciclopédia Britannica – verbete 'Condensation'")
mc(C, "química", 2, 10, "Qual elemento químico tem o símbolo Fe?",
   ["Ferro", "Flúor", "Fósforo", "Frâncio"], "Ferro",
   "O símbolo Fe vem do nome em latim do ferro, ferrum.",
   "IUPAC – Tabela Periódica")
mc(C, "química", 3, 12, "O sal de cozinha é formado por cloro e por qual outro elemento químico?",
   ["Sódio", "Potássio", "Cálcio", "Magnésio"], "Sódio",
   "O sal de cozinha é o cloreto de sódio; o símbolo do sódio, Na, vem do latim natrium.",
   "IUPAC – Tabela Periódica")
mc(C, "química", 2, 12, "Qual metal fica líquido na temperatura ambiente e era usado nos termômetros antigos?",
   ["Mercúrio", "Chumbo", "Alumínio", "Estanho"], "Mercúrio",
   "O mercúrio é o único metal líquido em temperatura ambiente; por ser tóxico, saiu dos termômetros.",
   "Enciclopédia Britannica – verbete 'Mercury (chemical element)'", syn=["mercurio"])
mc(C, "física", 2, 12, "Qual unidade do Sistema Internacional mede a força?",
   ["Newton", "Joule", "Watt", "Pascal"], "Newton",
   "A unidade de força homenageia o físico inglês Isaac Newton.",
   "BIPM – Sistema Internacional de Unidades")
tf(C, "física", 3, 12, "No vácuo, uma pena e um martelo soltos juntos chegam ao chão ao mesmo tempo.", True,
   "Sem o ar para frear, tudo cai igual; um astronauta da Apollo 15 mostrou isso na Lua em 1971.",
   "NASA – Apollo 15")
mc(C, "química", 3, 14, "Qual liga metálica é feita de cobre e estanho?",
   ["Bronze", "Aço", "Latão", "Ouro branco"], "Bronze",
   "O bronze foi tão importante que deu nome a um período da Pré-História, a Idade do Bronze.",
   "Enciclopédia Britannica – verbete 'Bronze'")
mc(C, "química", 2, 12, "Qual partícula do átomo tem carga elétrica negativa?",
   ["Elétron", "Próton", "Nêutron"], "Elétron",
   "Os elétrons ficam em volta do núcleo, onde estão os prótons e os nêutrons.",
   "Enciclopédia Britannica – verbete 'Electron'", syn=["eletron"])
op(C, "química", 3, 14, "Qual gás nobre brilha em vermelho-alaranjado nos letreiros luminosos?", "Neônio",
   ["neônio", "neonio", "neon", "néon"],
   "Os letreiros de neon ganham cor quando a eletricidade atravessa o gás dentro dos tubos.",
   "Enciclopédia Britannica – verbete 'Neon'")
mc(C, "química", 4, 16, "Qual cientista russo organizou a tabela periódica dos elementos, em 1869?",
   ["Dmitri Mendeleiev", "Antoine Lavoisier", "John Dalton", "Niels Bohr"], "Dmitri Mendeleiev",
   "Mendeleiev deixou espaços vazios na tabela e previu elementos que ainda seriam descobertos.",
   "Enciclopédia Britannica – verbete 'Dmitri Mendeleev'", syn=["mendeleiev", "mendeleev"])
mc(C, "química", 3, 14, "Qual cientista francês ficou famoso pela ideia de que na natureza nada se cria, nada se perde, tudo se transforma?",
   ["Antoine Lavoisier", "Louis Pasteur", "Blaise Pascal", "René Descartes"], "Antoine Lavoisier",
   "Lavoisier é considerado o pai da química moderna e formulou a lei da conservação da massa.",
   "Enciclopédia Britannica – verbete 'Antoine Lavoisier'", syn=["lavoisier"])
op(C, "energia", 2, 10, "Em que tipo de energia um painel solar transforma a luz do sol?", "Energia elétrica",
   ["energia elétrica", "energia eletrica", "eletricidade", "elétrica", "eletrica"],
   "As células fotovoltaicas do painel geram corrente elétrica quando recebem luz.",
   "Ministério de Minas e Energia")
tf(C, "física", 2, 10, "O ar quente tende a subir, e o ar frio tende a descer.", True,
   "O ar quente é menos denso; é por isso que os balões de ar quente sobem.",
   "Enciclopédia Britannica – verbete 'Convection'")

# =========================================================== NATUREZA
N = "nat"
mc(N, "animais", 1, 6, "Qual animal é famoso por ter o pescoço muito comprido?",
   ["Girafa", "Zebra", "Hipopótamo", "Rinoceronte"], "Girafa",
   "A girafa é o animal mais alto do mundo e alcança folhas no alto das árvores.",
   "Enciclopédia Britannica – verbete 'Giraffe'")
mc(N, "animais", 1, 6, "Qual destes animais carrega uma concha nas costas e anda bem devagar?",
   ["Caracol", "Formiga", "Grilo", "Minhoca"], "Caracol",
   "O caracol se esconde dentro da concha para se proteger e não ressecar.",
   "Enciclopédia Britannica – verbete 'Snail'")
tf(N, "animais", 1, 6, "Os sapos nascem como girinos, que vivem na água.", True,
   "Os girinos respiram por brânquias e, com a metamorfose, ganham patas e pulmões.",
   "Enciclopédia Britannica – verbete 'Frog'")
mc(N, "animais", 1, 8, "O que as abelhas recolhem das flores para fazer o mel?",
   ["Néctar", "Folhas", "Raízes", "Sementes"], "Néctar",
   "As abelhas transformam o néctar das flores em mel dentro da colmeia.",
   "Embrapa", syn=["nectar"])
mc(N, "animais", 1, 8, "O jacaré pertence a qual grupo de animais?",
   ["Répteis", "Anfíbios", "Mamíferos", "Peixes"], "Répteis",
   "Os répteis têm a pele coberta de escamas e botam ovos com casca.",
   "Enciclopédia Britannica – verbete 'Reptile'", syn=["repteis", "réptil", "reptil"])
mc(N, "animais", 1, 8, "Como se chama o filhote do cavalo?",
   ["Potro", "Bezerro", "Cabrito", "Leitão"], "Potro",
   "O potro consegue ficar em pé poucas horas depois de nascer.",
   "Enciclopédia Britannica – verbete 'Horse'")
mc(N, "fauna brasileira", 1, 8, "Qual animal brasileiro tem uma língua comprida e se alimenta de formigas e cupins?",
   ["Tamanduá-bandeira", "Anta", "Quati", "Bicho-preguiça"], "Tamanduá-bandeira",
   "A língua do tamanduá-bandeira pode passar de 60 centímetros.",
   "ICMBio", syn=["tamandua bandeira", "tamanduá"], br=True)
mc(N, "fauna brasileira", 1, 7, "Qual animal brasileiro vive pendurado nas árvores e se move muito devagar?",
   ["Bicho-preguiça", "Tamanduá", "Anta", "Capivara"], "Bicho-preguiça",
   "A preguiça desce da árvore só cerca de uma vez por semana para fazer as necessidades.",
   "ICMBio", syn=["preguiça", "preguica", "bicho preguica"], br=True)
mc(N, "fauna brasileira", 2, 12, "Qual é o maior mamífero terrestre do Brasil?",
   ["Anta", "Onça-pintada", "Capivara", "Lobo-guará"], "Anta",
   "A anta pode passar de 250 quilos e é chamada de 'jardineira da floresta' por espalhar sementes.",
   "ICMBio", br=True)
mc(N, "fauna brasileira", 2, 10, "Qual animal do Cerrado, de pernas longas e pelo alaranjado, aparece na nota de duzentos reais?",
   ["Lobo-guará", "Raposa-do-campo", "Onça-parda", "Veado-campeiro"], "Lobo-guará",
   "O lobo-guará é o maior canídeo da América do Sul e come muitos frutos, como a lobeira.",
   "Banco Central do Brasil", syn=["lobo guara"], br=True)
tf(N, "fauna brasileira", 2, 9, "O boto-cor-de-rosa vive nos rios da Amazônia.", True,
   "O boto-cor-de-rosa é o maior golfinho de água doce do mundo.",
   "ICMBio", br=True)
mc(N, "animais", 2, 10, "Como se chama a transformação pela qual a lagarta vira borboleta?",
   ["Metamorfose", "Migração", "Hibernação", "Fotossíntese"], "Metamorfose",
   "Dentro da crisálida, o corpo da lagarta se reorganiza completamente até virar borboleta.",
   "Enciclopédia Britannica – verbete 'Metamorphosis'")
tf(N, "animais", 2, 9, "As aranhas são insetos.", False,
   "Aranhas são aracnídeos: têm oito patas, enquanto os insetos têm seis.",
   "Enciclopédia Britannica – verbete 'Spider'")
tf(N, "animais", 2, 8, "O tubarão é um peixe.", True,
   "O tubarão é um peixe cartilaginoso: seu esqueleto é feito de cartilagem, e não de ossos.",
   "Enciclopédia Britannica – verbete 'Shark'")
mc(N, "biomas", 3, 12, "Depois da Amazônia, qual é o segundo maior bioma brasileiro?",
   ["Cerrado", "Mata Atlântica", "Caatinga", "Pampa"], "Cerrado",
   "O Cerrado ocupa cerca de um quarto do território brasileiro e é chamado de 'berço das águas'.",
   "IBGE – Biomas do Brasil", br=True)
mc(N, "animais", 2, 10, "Qual ave consegue voar para trás?",
   ["Beija-flor", "Andorinha", "Pardal", "Gavião"], "Beija-flor",
   "O beija-flor bate as asas dezenas de vezes por segundo e consegue até ficar parado no ar.",
   "Enciclopédia Britannica – verbete 'Hummingbird'", syn=["beija flor"])
mc(N, "plantas", 3, 12, "Qual planta carnívora fecha as folhas como uma armadilha para prender insetos?",
   ["Dioneia", "Vitória-régia", "Samambaia", "Bromélia"], "Dioneia",
   "A dioneia fecha a armadilha em menos de um segundo quando o inseto toca seus pelinhos.",
   "Enciclopédia Britannica – verbete 'Venus flytrap'", syn=["dionéia"])
op(N, "flora brasileira", 3, 10, "Qual planta aquática da Amazônia tem folhas redondas gigantes que flutuam nos rios?", "Vitória-régia",
   ["vitória-régia", "vitoria regia", "vitória régia", "vitoria-regia"],
   "As folhas da vitória-régia podem passar de dois metros de diâmetro.",
   "Embrapa", br=True)
mc(N, "animais", 4, 12, "Quantos corações tem um polvo?",
   ["Um", "Dois", "Três", "Quatro"], "Três",
   "Dois corações levam sangue às brânquias e um ao resto do corpo; e o sangue do polvo é azul.",
   "Enciclopédia Britannica – verbete 'Octopus'", syn=["3", "tres"])

# =========================================================== ASTRONOMIA
A = "ast"
tf(A, "estrelas", 1, 6, "O Sol é uma estrela.", True,
   "O Sol é a estrela mais próxima de nós; as outras parecem pontinhos porque estão muito mais longe.",
   "NASA")
mc(A, "planetas", 1, 6, "Em qual planeta nós vivemos?",
   ["Terra", "Marte", "Vênus", "Júpiter"], "Terra",
   "A Terra é o terceiro planeta a partir do Sol e o único conhecido com vida.",
   "NASA")
mc(A, "Lua", 1, 7, "Como se chama a fase em que vemos a Lua toda iluminada, bem redonda?",
   ["Lua cheia", "Lua nova", "Quarto crescente", "Quarto minguante"], "Lua cheia",
   "Na lua cheia, a Terra fica entre o Sol e a Lua, e vemos toda a face iluminada.",
   "NASA – Moon Phases")
mc(A, "observação", 1, 7, "Qual instrumento usamos para ver estrelas e planetas mais de perto?",
   ["Telescópio", "Microscópio", "Estetoscópio", "Periscópio"], "Telescópio",
   "Galileu Galilei foi um dos primeiros a apontar um telescópio para o céu, em 1609.",
   "Enciclopédia Britannica – verbete 'Telescope'", syn=["telescopio"])
tf(A, "Lua", 2, 8, "A Lua realmente muda de formato ao longo do mês.", False,
   "A Lua é sempre redonda; o que muda é a parte iluminada pelo Sol que conseguimos ver.",
   "NASA – Moon Phases")
mc(A, "planetas", 2, 12, "Qual é o planeta mais quente do Sistema Solar?",
   ["Vênus", "Mercúrio", "Marte", "Júpiter"], "Vênus",
   "A atmosfera grossa de gás carbônico de Vênus prende o calor, e a superfície passa de 400 °C.",
   "NASA", syn=["venus"])
mc(A, "planetas", 3, 12, "Qual planeta é chamado popularmente de 'Estrela d'Alva', por brilhar forte ao amanhecer?",
   ["Vênus", "Marte", "Saturno", "Mercúrio"], "Vênus",
   "Depois da Lua, Vênus é o objeto mais brilhante do céu noturno.",
   "NASA", syn=["venus"])
mc(A, "planetas", 2, 10, "Entre os oito planetas, qual tem o menor tamanho?",
   ["Mercúrio", "Marte", "Vênus", "Terra"], "Mercúrio",
   "Mercúrio é menor até que Ganimedes, uma lua de Júpiter.",
   "NASA", syn=["mercurio"])
mc(A, "Sol", 3, 12, "Quanto tempo, aproximadamente, a luz do Sol leva para chegar à Terra?",
   ["8 segundos", "8 minutos", "8 horas", "8 dias"], "8 minutos",
   "A luz percorre os cerca de 150 milhões de quilômetros entre o Sol e a Terra em uns 8 minutos.",
   "NASA", syn=["oito minutos"])
mc(A, "Lua", 2, 10, "Quanto tempo dura, aproximadamente, o ciclo completo das fases da Lua?",
   ["Cerca de um mês", "Cerca de uma semana", "Cerca de um ano", "Cerca de um dia"], "Cerca de um mês",
   "O ciclo de fases leva cerca de 29 dias e meio, e deu origem à ideia de 'mês'.",
   "NASA – Moon Phases")
tf(A, "planetas", 2, 10, "Júpiter é um planeta formado principalmente por gases.", True,
   "Júpiter é feito sobretudo de hidrogênio e hélio e não tem uma superfície sólida como a da Terra.",
   "NASA")
mc(A, "buracos negros", 4, 16, "Como se chama o limite em volta de um buraco negro de onde nem a luz consegue escapar?",
   ["Horizonte de eventos", "Coroa", "Cinturão de radiação", "Órbita"], "Horizonte de eventos",
   "Em 2019, uma rede de radiotelescópios fez a primeira imagem da sombra de um buraco negro.",
   "NASA – Black Holes")
mc(A, "satélites", 4, 14, "Qual é o maior satélite natural do Sistema Solar?",
   ["Ganimedes", "Titã", "Lua", "Europa"], "Ganimedes",
   "Ganimedes, lua de Júpiter, é maior até que o planeta Mercúrio.",
   "NASA")
mc(A, "satélites", 4, 16, "Qual lua de Saturno tem uma atmosfera densa e lagos de metano líquido?",
   ["Titã", "Ganimedes", "Io", "Fobos"], "Titã",
   "Titã é o único satélite do Sistema Solar com atmosfera densa.",
   "NASA – Titan", syn=["tita"])
mc(A, "Sistema Solar", 3, 14, "Entre quais planetas fica o principal cinturão de asteroides?",
   ["Marte e Júpiter", "Terra e Marte", "Júpiter e Saturno", "Vênus e Terra"], "Marte e Júpiter",
   "Ceres, o maior objeto do cinturão de asteroides, é classificado como planeta anão.",
   "NASA")
tf(A, "exploração espacial", 3, 12, "Os astronautas flutuam na estação espacial porque lá não existe nenhuma gravidade.", False,
   "A gravidade lá ainda é forte; eles flutuam porque a estação e eles estão em queda livre contínua em volta da Terra.",
   "NASA")
op(A, "exploração espacial", 3, 12, "Qual era o nome da cadela soviética que foi o primeiro animal a orbitar a Terra, em 1957?", "Laika",
   ["laika", "laica"],
   "Laika viajou a bordo do Sputnik 2, um mês depois do lançamento do primeiro satélite.",
   "NASA")

# =========================================================== CORPO HUMANO
H = "cor"
op(H, "anatomia", 1, 6, "Quantos dedos temos em uma mão?", "5", ["5", "cinco"],
   "Cada mão tem cinco dedos, e o polegar é o que nos permite segurar objetos com firmeza.",
   "Enciclopédia Britannica – verbete 'Hand'")
mc(H, "sentidos", 1, 6, "Qual órgão do corpo usamos para escutar os sons?",
   ["Ouvido", "Nariz", "Olho", "Língua"], "Ouvido",
   "O ouvido também ajuda a manter o equilíbrio do corpo.",
   "Enciclopédia Britannica – verbete 'Ear'", syn=["orelha", "ouvidos"])
tf(H, "dentes", 1, 6, "O dente de leite cai para dar lugar ao dente permanente.", True,
   "A troca dos dentes de leite costuma começar por volta dos seis anos.",
   "Ministério da Saúde")
mc(H, "anatomia", 1, 8, "Qual parte do esqueleto protege o cérebro?",
   ["Crânio", "Costelas", "Coluna", "Bacia"], "Crânio",
   "O crânio é formado por vários ossos que se unem durante a infância.",
   "Enciclopédia Britannica – verbete 'Skull'", syn=["cranio"])
mc(H, "fisiologia", 1, 8, "O que a pele libera para ajudar a esfriar o corpo quando sentimos calor?",
   ["Suor", "Saliva", "Lágrima", "Sangue"], "Suor",
   "Quando o suor evapora, ele leva calor embora e refresca a pele.",
   "Enciclopédia Britannica – verbete 'Sweat gland'")
tf(H, "anatomia", 1, 8, "O coração é um músculo.", True,
   "O coração é feito de músculo cardíaco, que trabalha sem parar a vida inteira.",
   "Enciclopédia Britannica – verbete 'Heart'")
mc(H, "anatomia", 2, 12, "Qual osso da coxa é o maior e o mais longo do corpo?",
   ["Fêmur", "Tíbia", "Úmero", "Rádio"], "Fêmur",
   "O fêmur liga o quadril ao joelho e aguenta grande parte do peso do corpo.",
   "Enciclopédia Britannica – verbete 'Femur'", syn=["femur"])
mc(H, "digestão", 2, 10, "Logo depois de passar pelo esôfago, a comida chega a qual órgão?",
   ["Estômago", "Intestino grosso", "Pâncreas", "Bexiga"], "Estômago",
   "No estômago, a comida é misturada com um suco ácido que ajuda a digeri-la.",
   "Enciclopédia Britannica – verbete 'Stomach'", syn=["estomago"])
tf(H, "circulação", 3, 12, "O sangue sai do coração pelas veias e volta para ele pelas artérias.", False,
   "É o contrário: as artérias levam o sangue para fora do coração, e as veias o trazem de volta.",
   "Enciclopédia Britannica – verbete 'Artery'")
mc(H, "sangue", 2, 12, "Quais células do sangue defendem o corpo contra infecções?",
   ["Glóbulos brancos", "Glóbulos vermelhos", "Plaquetas"], "Glóbulos brancos",
   "Os glóbulos brancos, ou leucócitos, atacam vírus e bactérias.",
   "Enciclopédia Britannica – verbete 'White blood cell'", syn=["leucócitos", "leucocitos"])
mc(H, "sangue", 2, 12, "Quais partes do sangue ajudam a formar a casquinha que fecha um machucado?",
   ["Plaquetas", "Glóbulos brancos", "Glóbulos vermelhos", "Anticorpos"], "Plaquetas",
   "As plaquetas se juntam no local do corte e ajudam o sangue a coagular.",
   "Enciclopédia Britannica – verbete 'Platelet'")
tf(H, "anatomia", 2, 10, "Os ossos são vivos: crescem e conseguem se regenerar depois de uma fratura.", True,
   "Os ossos têm células e vasos sanguíneos e se renovam ao longo da vida.",
   "Enciclopédia Britannica – verbete 'Bone'")
mc(H, "visão", 3, 14, "Qual parte do olho funciona como uma lente e fica opaca na catarata?",
   ["Cristalino", "Retina", "Córnea", "Pupila"], "Cristalino",
   "Na cirurgia de catarata, o cristalino opaco é trocado por uma lente artificial.",
   "Ministério da Saúde")
op(H, "anatomia", 2, 10, "Qual é o nome do órgão em forma de bolsa que guarda a urina antes de sairmos para o banheiro?", "Bexiga",
   ["bexiga"],
   "A bexiga de um adulto costuma guardar algo entre 400 e 600 mililitros.",
   "Enciclopédia Britannica – verbete 'Urinary bladder'")
mc(H, "sistema nervoso", 3, 14, "Qual é o maior nervo do corpo humano, que desce pela parte de trás da perna?",
   ["Nervo ciático", "Nervo óptico", "Nervo vago", "Nervo facial"], "Nervo ciático",
   "A inflamação desse nervo causa a dor conhecida como ciática.",
   "Enciclopédia Britannica – verbete 'Sciatic nerve'", syn=["ciatico", "ciático"])
mc(H, "sistema nervoso", 3, 14, "Qual parte do encéfalo é a principal responsável pelo equilíbrio e pela coordenação dos movimentos?",
   ["Cerebelo", "Hipotálamo", "Bulbo", "Hipocampo"], "Cerebelo",
   "O cerebelo fica na parte de trás da cabeça, embaixo do cérebro.",
   "Enciclopédia Britannica – verbete 'Cerebellum'")
mc(H, "pele", 3, 12, "Qual pigmento dá cor à pele, aos cabelos e aos olhos?",
   ["Melanina", "Clorofila", "Hemoglobina", "Queratina"], "Melanina",
   "A melanina também ajuda a proteger a pele dos raios ultravioleta do Sol.",
   "Enciclopédia Britannica – verbete 'Melanin'")
op(H, "saúde", 2, 12, "Como se chama a doença em que o corpo não produz insulina suficiente ou não consegue usá-la bem, deixando o açúcar alto no sangue?", "Diabetes",
   ["diabetes", "diabete"],
   "O controle da diabetes envolve alimentação, atividade física e, em muitos casos, remédios ou insulina.",
   "Ministério da Saúde")
mc(H, "digestão", 3, 14, "Qual é a principal função do intestino delgado?",
   ["Absorver os nutrientes", "Produzir a bile", "Armazenar as fezes", "Produzir a insulina"], "Absorver os nutrientes",
   "O intestino delgado de um adulto mede vários metros e tem milhões de dobrinhas que aumentam a absorção.",
   "Enciclopédia Britannica – verbete 'Small intestine'")

# =========================================================== TECNOLOGIA
T = "tec"
mc(T, "eletrodomésticos", 1, 6, "Qual aparelho da cozinha mantém os alimentos gelados?",
   ["Geladeira", "Fogão", "Liquidificador", "Batedeira"], "Geladeira",
   "A geladeira tira o calor do lado de dentro e o solta pela parte de trás.",
   "Enciclopédia Britannica – verbete 'Refrigerator'")
mc(T, "computadores", 1, 6, "Qual parte do computador usamos para digitar letras?",
   ["Teclado", "Monitor", "Caixa de som", "Impressora"], "Teclado",
   "A ordem das letras QWERTY no teclado vem das antigas máquinas de escrever.",
   "Enciclopédia Britannica – verbete 'Keyboard'")
tf(T, "computadores", 1, 7, "A impressora serve para passar para o papel o que está no computador.", True,
   "Existem até impressoras 3D, que criam objetos em vez de folhas impressas.",
   "Enciclopédia Britannica – verbete 'Printer'")
mc(T, "eletrodomésticos", 1, 8, "Qual aparelho esquenta a comida usando ondas invisíveis?",
   ["Micro-ondas", "Geladeira", "Liquidificador", "Torradeira"], "Micro-ondas",
   "As micro-ondas fazem as moléculas de água do alimento se agitarem e esquentarem.",
   "Enciclopédia Britannica – verbete 'Microwave oven'", syn=["microondas", "forno de micro-ondas"])
mc(T, "internet", 1, 9, "O que é um e-mail?",
   ["Uma mensagem enviada pela internet", "Um tipo de vírus", "Um jogo de computador", "Um cabo de energia"],
   "Uma mensagem enviada pela internet",
   "O nome vem do inglês 'electronic mail', ou correio eletrônico.",
   "Enciclopédia Britannica – verbete 'E-mail'")
mc(T, "videogames", 2, 9, "Qual empresa japonesa criou o personagem Mario?",
   ["Nintendo", "Sega", "Sony", "Microsoft"], "Nintendo",
   "Mario apareceu pela primeira vez em 1981, no jogo Donkey Kong.",
   "Enciclopédia Britannica – verbete 'Nintendo'")
mc(T, "videogames", 2, 10, "Qual empresa fabrica o console Xbox?",
   ["Microsoft", "Nintendo", "Sony", "Sega"], "Microsoft",
   "O primeiro Xbox foi lançado em 2001.",
   "Enciclopédia Britannica – verbete 'Xbox'")
mc(T, "computadores", 2, 12, "Qual destas unidades de armazenamento é a maior?",
   ["Terabyte", "Gigabyte", "Megabyte", "Kilobyte"], "Terabyte",
   "Um terabyte equivale a cerca de mil gigabytes.",
   "IEC 80000-13 – Unidades de informação")
tf(T, "segurança", 1, 10, "Um vírus de computador é um programa feito para causar problemas.", True,
   "Os vírus de computador se espalham copiando a si mesmos para outros arquivos e aparelhos.",
   "Enciclopédia Britannica – verbete 'Computer virus'")
mc(T, "comunicação", 2, 10, "Qual sistema usa sinais de satélites para mostrar a nossa localização no mapa do celular?",
   ["GPS", "Bluetooth", "Wi-Fi", "QR Code"], "GPS",
   "O GPS calcula a nossa posição com sinais de vários satélites ao mesmo tempo.",
   "Enciclopédia Britannica – verbete 'GPS'")
mc(T, "comunicação", 1, 9, "Qual tecnologia sem fio de curto alcance liga fones de ouvido ao celular?",
   ["Bluetooth", "GPS", "Cabo USB", "Rádio AM"], "Bluetooth",
   "O nome homenageia Harald Bluetooth, um antigo rei da Dinamarca.",
   "Enciclopédia Britannica – verbete 'Bluetooth'")
mc(T, "empresas", 2, 12, "Quem fundou a Apple ao lado de Steve Wozniak, em 1976?",
   ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk"], "Steve Jobs",
   "A Apple começou na garagem da casa da família de Steve Jobs, na Califórnia.",
   "Enciclopédia Britannica – verbete 'Apple Inc.'", syn=["jobs"])
mc(T, "comunicação", 1, 9, "Qual código quadrado, cheio de pontinhos, é lido pela câmera do celular?",
   ["QR Code", "Código Morse", "Braille", "CEP"], "QR Code",
   "O QR Code foi criado no Japão em 1994 para rastrear peças de carros.",
   "Enciclopédia Britannica – verbete 'QR code'", syn=["qr", "qrcode"])
tf(T, "história", 2, 10, "Os primeiros computadores eletrônicos eram tão grandes que ocupavam salas inteiras.", True,
   "O ENIAC, de 1946, pesava cerca de 27 toneladas.",
   "Enciclopédia Britannica – verbete 'ENIAC'")
op(T, "Brasil", 1, 10, "Qual sistema de pagamento instantâneo foi criado pelo Banco Central do Brasil em 2020?", "Pix",
   ["pix"],
   "Com ele dá para transferir dinheiro a qualquer hora, inclusive em fins de semana e feriados.",
   "Banco Central do Brasil", br=True)
mc(T, "história", 4, 14, "Quem é considerada a primeira programadora da história, por um algoritmo escrito no século XIX?",
   ["Ada Lovelace", "Marie Curie", "Grace Hopper", "Hedy Lamarr"], "Ada Lovelace",
   "Ada Lovelace escreveu instruções para a máquina analítica imaginada por Charles Babbage.",
   "Enciclopédia Britannica – verbete 'Ada Lovelace'", syn=["lovelace"])
mc(T, "história", 4, 16, "Qual cofundador da Intel previu, em 1965, que o número de transistores nos chips dobraria em intervalos regulares?",
   ["Gordon Moore", "Steve Jobs", "Bill Gates", "Linus Torvalds"], "Gordon Moore",
   "A previsão ficou conhecida como Lei de Moore.",
   "Enciclopédia Britannica – verbete 'Moore's law'", syn=["moore"])
op(T, "software", 3, 14, "Qual sistema operacional de código aberto foi criado pelo finlandês Linus Torvalds em 1991?", "Linux",
   ["linux"],
   "O mascote do Linux é um pinguim chamado Tux.",
   "Enciclopédia Britannica – verbete 'Linux'")

# =========================================================== MATEMÁTICA
M = "mat"
mc(M, "aritmética", 1, 7, "Quanto é três mais três mais três?",
   ["6", "8", "9", "12"], "9",
   "Somar três vezes o número três é o mesmo que fazer três vezes três, que dá nove.",
   "Aritmética básica", syn=["nove"])
mc(M, "geometria", 1, 7, "Como se chama a figura que tem quatro lados iguais e quatro cantos retos?",
   ["Quadrado", "Triângulo", "Círculo", "Pentágono"], "Quadrado",
   "Todo quadrado é também um retângulo, porque tem quatro ângulos retos.",
   "Geometria básica")
mc(M, "problemas", 1, 6, "Ana tinha oito balas e deu três para o irmão. Com quantas balas ela ficou?",
   ["4", "5", "6", "11"], "5",
   "Oito menos três é igual a cinco.",
   "Aritmética básica", syn=["cinco"])
tf(M, "contagem", 1, 7, "Meia dúzia de ovos são seis ovos.", True,
   "Uma dúzia tem doze unidades, e a metade de doze é seis.",
   "Aritmética básica")
op(M, "aritmética", 1, 8, "Quanto é mil menos um?", "999",
   ["999", "novecentos e noventa e nove"],
   "Mil menos um é o maior número de três algarismos.",
   "Aritmética básica")
mc(M, "tabuada", 2, 9, "Quanto é sete vezes oito?",
   ["48", "54", "56", "63"], "56",
   "Uma dica para lembrar: cinco, seis, sete, oito — cinquenta e seis é sete vezes oito.",
   "Aritmética básica", syn=["cinquenta e seis"])
mc(M, "medidas", 1, 9, "Quantos minutos tem um quarto de hora?",
   ["10", "15", "20", "25"], "15",
   "Uma hora tem sessenta minutos, e a quarta parte de sessenta é quinze.",
   "Aritmética básica", syn=["quinze"])
mc(M, "porcentagem", 2, 12, "Um produto custava cem reais e ganhou dez por cento de desconto. Quanto passou a custar?",
   ["80 reais", "90 reais", "95 reais", "110 reais"], "90 reais",
   "Dez por cento de cem é dez, e cem menos dez dá noventa.",
   "Aritmética básica", syn=["90", "noventa reais"])
mc(M, "frações", 3, 12, "Quanto é a metade de um quarto?",
   ["Um oitavo", "Um sexto", "Um meio", "Dois quartos"], "Um oitavo",
   "Dividir um quarto em duas partes iguais dá um oitavo.",
   "Aritmética básica")
op(M, "raciocínio", 3, 10, "Se hoje é segunda-feira, que dia da semana será daqui a dez dias?", "Quinta-feira",
   ["quinta-feira", "quinta feira", "quinta"],
   "Em sete dias volta a ser segunda; mais três dias, chega a quinta-feira.",
   "Raciocínio lógico")
tf(M, "divisibilidade", 2, 10, "Todo número que termina em zero pode ser dividido por cinco sem deixar resto.", True,
   "Um número é divisível por cinco quando termina em zero ou em cinco.",
   "Aritmética básica")
mc(M, "geometria", 2, 10, "Um hexágono é um polígono com quantos lados?",
   ["5", "6", "7", "8"], "6",
   "Os alvéolos das colmeias das abelhas têm a forma de hexágonos.",
   "Geometria básica", syn=["seis"])
mc(M, "números primos", 3, 12, "Qual destes números é primo?",
   ["21", "27", "29", "33"], "29",
   "Vinte e nove só pode ser dividido por um e por ele mesmo.",
   "Aritmética básica", syn=["vinte e nove"])
op(M, "estatística", 2, 12, "Qual é a média de três, cinco e sete?", "5",
   ["5", "cinco"],
   "Três mais cinco mais sete dá quinze, e quinze dividido por três é cinco.",
   "Aritmética básica")
mc(M, "problemas", 3, 12, "Um trem anda a sessenta quilômetros por hora. Quantos quilômetros ele percorre em duas horas e meia?",
   ["120", "150", "160", "180"], "150",
   "Sessenta vezes dois é cento e vinte, mais trinta da meia hora, dá cento e cinquenta.",
   "Aritmética básica", syn=["cento e cinquenta"])
mc(M, "geometria", 2, 12, "Qual é a área de um retângulo de quatro metros por seis metros?",
   ["10 metros quadrados", "20 metros quadrados", "24 metros quadrados", "48 metros quadrados"], "24 metros quadrados",
   "A área do retângulo é o comprimento vezes a largura: quatro vezes seis.",
   "Geometria básica", syn=["24", "vinte e quatro"])
mc(M, "problemas", 2, 10, "Se três canetas custam doze reais, quanto custam cinco canetas iguais?",
   ["15 reais", "20 reais", "24 reais", "60 reais"], "20 reais",
   "Cada caneta custa quatro reais, e cinco vezes quatro dá vinte.",
   "Aritmética básica", syn=["20", "vinte reais"])
mc(M, "potências", 3, 12, "Quanto é três elevado ao cubo?",
   ["6", "9", "27", "81"], "27",
   "Três elevado ao cubo é três vezes três vezes três.",
   "Aritmética básica", syn=["vinte e sete"])
tf(M, "geometria", 3, 12, "Um ângulo de cento e vinte graus é um ângulo obtuso.", True,
   "Ângulo obtuso é aquele maior que noventa e menor que cento e oitenta graus.",
   "Geometria básica")
mc(M, "sequências", 3, 12, "Qual é o próximo número da sequência um, um, dois, três, cinco, oito?",
   ["11", "12", "13", "16"], "13",
   "É a sequência de Fibonacci: cada número é a soma dos dois anteriores.",
   "Enciclopédia Britannica – verbete 'Fibonacci sequence'", syn=["treze"])
mc(M, "números", 3, 12, "Quantos zeros tem o número um bilhão, escrito com algarismos?",
   ["6", "9", "10", "12"], "9",
   "Um bilhão é mil vezes um milhão: o número um seguido de nove zeros.",
   "Aritmética básica", syn=["nove"])
mc(M, "geometria", 4, 14, "Quantas diagonais tem um pentágono?",
   ["3", "5", "6", "10"], "5",
   "De cada um dos cinco vértices saem duas diagonais, e cada diagonal é contada duas vezes.",
   "Geometria básica", syn=["cinco"])
mc(M, "geometria", 4, 14, "Quantos graus somam os quatro ângulos internos de qualquer quadrilátero?",
   ["180 graus", "270 graus", "360 graus", "540 graus"], "360 graus",
   "Uma diagonal divide o quadrilátero em dois triângulos, de cento e oitenta graus cada.",
   "Geometria básica", syn=["360", "trezentos e sessenta"])
