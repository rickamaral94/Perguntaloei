# Perguntas novas: culinária. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "gas"

# =========================================================== FÁCEIS
mc(T, "frutas", 1, 6, "Qual fruta pequena e roxa cresce em cachos e vira suco e geleia?",
   ["Uva", "Manga", "Pera", "Melão"], "Uva",
   "A uva nasce em cachos na videira e pode ser verde, roxa ou vermelha.",
   "Embrapa Uva e Vinho")
mc(T, "ingredientes", 1, 6, "Qual alimento vermelho e redondo é a base do molho do macarrão?",
   ["Tomate", "Pepino", "Alface", "Cebola"], "Tomate",
   "O molho de tomate é cozido com tempero e é um dos mais usados em massas.",
   "Enciclopédia Britannica – verbete 'Tomato'")
mc(T, "utensílios", 1, 6, "Qual talher usamos para tomar sopa?",
   ["Colher", "Garfo", "Faca", "Espeto"], "Colher",
   "A colher tem uma parte côncava que segura líquidos, como a sopa.",
   "Enciclopédia Britannica – verbete 'Spoon'")
mc(T, "doces de festa", 1, 7, "Qual doce de festa é branquinho, feito com leite condensado e coco, e muitas vezes leva um cravo em cima?",
   ["Beijinho", "Cajuzinho", "Bem-casado", "Olho de sogra"], "Beijinho",
   "O beijinho é o 'irmão' de coco do brigadeiro e costuma ser enrolado no açúcar.",
   "Dicionário Houaiss da Língua Portuguesa – verbete 'beijinho'", br=True)
mc(T, "laticínios", 1, 7, "Qual alimento feito de leite é azedinho e cremoso e costuma vir em potinhos?",
   ["Iogurte", "Gelatina", "Pudim", "Mingau"], "Iogurte",
   "O iogurte fica azedinho porque bactérias do bem transformam o açúcar do leite em ácido.",
   "Enciclopédia Britannica – verbete 'Yogurt'")
op(T, "ovos", 1, 6, "Qual é a cor da gema do ovo?",
   "Amarela", ["amarela", "amarelo", "amarelinha", "amarelada"],
   "A gema é a parte amarela ou alaranjada do ovo, rodeada pela clara.",
   "Embrapa Suínos e Aves")
mc(T, "utensílios", 1, 7, "Qual utensílio de cozinha é usado para transformar queijo e cenoura em fiapos?",
   ["Ralador", "Peneira", "Concha", "Rolo de massa"], "Ralador",
   "O ralador tem furinhos com bordas cortantes que soltam fiapos do alimento.",
   "Enciclopédia Britannica – verbete 'Grater'")
mc(T, "doces juninos", 1, 8, "Qual doce junino é feito de amendoim inteiro grudado numa calda dura de rapadura ou açúcar?",
   ["Pé de moleque", "Canjica", "Curau", "Quentão"], "Pé de moleque",
   "O pé de moleque é um doce duro e crocante, comum nas festas de São João.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "Japão", 1, 9, "Como se chamam os dois palitinhos usados para comer no Japão?",
   ["Hashi", "Espeto", "Pinça", "Palito de dente"], "Hashi",
   "Os hashis são usados há séculos em vários países da Ásia, como Japão, China e Coreia.",
   "Enciclopédia Britannica – verbete 'Chopsticks'")
tf(T, "conservação", 1, 9, "O mel estraga em poucos dias se ficar fora da geladeira.", False,
   "Por ter pouca água e muito açúcar, o mel bem fechado dura muito tempo fora da geladeira.",
   "Embrapa Meio-Norte – Sistema de Produção de Mel")
mc(T, "utensílios", 1, 9, "Qual panela cozinha o feijão bem rápido prendendo o vapor dentro dela?",
   ["Panela de pressão", "Frigideira", "Assadeira", "Chaleira"], "Panela de pressão",
   "Com o vapor preso, a pressão aumenta e a água ferve a uma temperatura mais alta, cozinhando mais rápido.",
   "Enciclopédia Britannica – verbete 'Pressure cooker'")
op(T, "legumes", 1, 8, "Qual raiz roxa, usada em saladas e sucos, deixa as mãos manchadas?",
   "Beterraba", ["beterraba", "beterrabas"],
   "A cor forte da beterraba vem de pigmentos chamados betalaínas.",
   "Embrapa Hortaliças")
mc(T, "nutrição", 1, 6, "Qual destas bebidas é a melhor para matar a sede?",
   ["Água", "Refrigerante", "Suco de caixinha", "Achocolatado"], "Água",
   "O Guia Alimentar do Ministério da Saúde recomenda a água como a principal bebida do dia a dia.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
mc(T, "padaria", 1, 8, "Qual doce de padaria, frito e recheado de creme, tem nome de algo que acontece quando a gente dorme?",
   ["Sonho", "Bomba", "Carolina", "Rosca"], "Sonho",
   "O sonho é uma bola de massa frita, recheada de creme e polvilhada com açúcar.",
   "Dicionário Houaiss da Língua Portuguesa – verbete 'sonho'", br=True)
mc(T, "técnicas", 1, 7, "Para fritar a batata, ela é mergulhada em que líquido bem quente?",
   ["Óleo", "Água", "Leite", "Vinagre"], "Óleo",
   "O óleo de fritura costuma passar de 160 °C, por isso a batata fica dourada e crocante por fora.",
   "Enciclopédia Britannica – verbete 'Frying'")
mc(T, "temperos", 1, 6, "O que existe na água do mar e também colocamos no feijão para dar gosto?",
   ["Sal", "Açúcar", "Fermento", "Vinagre"], "Sal",
   "Boa parte do sal de cozinha do Brasil vem das salinas, onde a água do mar evapora.",
   "Enciclopédia Britannica – verbete 'Salt'")
mc(T, "verduras", 1, 6, "Qual destas é uma verdura de folhas usada na salada?",
   ["Alface", "Cenoura", "Beterraba", "Batata"], "Alface",
   "Comemos as folhas da alface; já a cenoura, a beterraba e a batata crescem debaixo da terra.",
   "Embrapa Hortaliças")
mc(T, "frutas", 1, 7, "Qual fruta tem um caroço grande e cheio de fiapos e deixa o queixo melado quando a gente chupa?",
   ["Manga", "Uva", "Morango", "Pera"], "Manga",
   "A manga veio da Ásia e se adaptou tão bem que hoje é uma das frutas mais populares do Brasil.",
   "Embrapa Mandioca e Fruticultura")
mc(T, "nutrição", 1, 6, "O que é importante fazer depois de comer doces?",
   ["Escovar os dentes", "Dormir", "Tomar refrigerante", "Comer mais bala"], "Escovar os dentes",
   "O açúcar alimenta as bactérias que causam cárie, por isso escovar os dentes protege o sorriso.",
   "Ministério da Saúde – Saúde Bucal")
mc(T, "queijos", 1, 9, "Qual queijo é assado no espeto e vendido nas praias, principalmente no Nordeste?",
   ["Queijo coalho", "Gorgonzola", "Parmesão", "Brie"], "Queijo coalho",
   "O queijo coalho é firme e não derrete fácil, por isso pode ir direto à brasa.",
   "MAPA – Instrução Normativa nº 30/2001, Regulamento Técnico de Identidade e Qualidade do Queijo de Coalho", br=True)
op(T, "ingredientes", 1, 9, "De qual grão é feito o fubá?",
   "Milho", ["milho", "do milho", "grão de milho"],
   "O fubá é o milho moído bem fininho, usado em bolos, angu e polenta.",
   "Embrapa Milho e Sorgo", br=True)
tf(T, "bebidas", 1, 8, "A água de coco é tirada do coco verde.", True,
   "O coco verde, mais novo, tem bastante água; o coco seco tem mais polpa e pouca água.",
   "Embrapa Tabuleiros Costeiros")
tf(T, "grãos", 1, 8, "O milho de pipoca é o mesmo milho verde usado na pamonha.", False,
   "O milho de pipoca é uma variedade diferente, de casca dura, que estoura quando a água de dentro vira vapor.",
   "Embrapa Milho e Sorgo")
tf(T, "frutas", 1, 8, "O abacaxi nasce no galho de uma árvore alta.", False,
   "O abacaxi cresce no meio de uma planta baixa, de folhas pontudas, rente ao chão.",
   "Embrapa Mandioca e Fruticultura")
mc(T, "utensílios", 1, 7, "Qual utensílio parece uma colher grande e funda e serve para pôr feijão e sopa no prato?",
   ["Concha", "Espátula", "Peneira", "Batedor"], "Concha",
   "A concha tem cabo longo e uma cuba funda, ideal para servir líquidos.",
   "Enciclopédia Britannica – verbete 'Ladle'")
mc(T, "ovos", 1, 7, "Qual prato é feito batendo ovos e cozinhando na frigideira, às vezes com queijo e presunto?",
   ["Omelete", "Pudim", "Mingau", "Gelatina"], "Omelete",
   "A omelete é feita com ovos batidos e pode ser dobrada ao meio com recheio dentro.",
   "Enciclopédia Britannica – verbete 'Omelet'")
mc(T, "frutas", 1, 8, "Qual fruta amarela, quando cortada em fatias, fica com formato de estrela?",
   ["Carambola", "Pera", "Ameixa", "Goiaba"], "Carambola",
   "A carambola tem cinco gomos salientes, que formam uma estrela no corte.",
   "Embrapa Mandioca e Fruticultura")

# =========================================================== MÉDIAS
mc(T, "pães do mundo", 2, 10, "Qual pão francês é comprido e fininho, com casca bem crocante?",
   ["Baguete", "Ciabatta", "Pão sírio", "Broa de milho"], "Baguete",
   "A baguete é um símbolo da França, e sua tradição artesanal virou Patrimônio da UNESCO em 2022.",
   "UNESCO – Saber artesanal e cultura do pão baguete (Patrimônio Imaterial, 2022)")
mc(T, "salgados", 2, 10, "Qual salgado de origem árabe é feito de trigo partido com carne moída e tem formato oval e pontudo?",
   ["Quibe", "Esfirra", "Empada", "Coxinha"], "Quibe",
   "O quibe chegou ao Brasil com imigrantes sírios e libaneses e virou salgado de festa.",
   "Enciclopédia Britannica – verbete 'Kibbeh'")
mc(T, "pratos típicos", 2, 12, "Qual sanduíche, criado em São Paulo, leva rosbife, queijo derretido, tomate e pepino no pão francês?",
   ["Bauru", "Misto-quente", "Beirute", "Cachorro-quente"], "Bauru",
   "O sanduíche surgiu nos anos 1930 no restaurante Ponto Chic e ganhou o apelido do estudante que o pediu, nascido em Bauru.",
   "Prefeitura Municipal de Bauru", br=True)
mc(T, "pratos típicos", 2, 12, "Qual prato gaúcho é feito de arroz cozido junto com charque picado?",
   ["Arroz carreteiro", "Galinhada", "Risoto", "Arroz de forno"], "Arroz carreteiro",
   "O nome vem dos carreteiros, que viajavam em carretas de boi e levavam charque, que não estragava.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(T, "origem dos alimentos", 2, 12, "Em qual região da América do Sul a batata foi cultivada pela primeira vez?",
   ["Cordilheira dos Andes", "Floresta Amazônica", "Pantanal", "Caribe"], "Cordilheira dos Andes",
   "Povos andinos, nas terras altas do Peru e da Bolívia, cultivam a batata há milhares de anos.",
   "Enciclopédia Britannica – verbete 'Potato'")
tf(T, "origem dos alimentos", 2, 12, "Antes de virar doce, o cacau era consumido por maias e astecas principalmente como bebida.", True,
   "Os povos da Mesoamérica preparavam uma bebida espumante de cacau, muitas vezes amarga e temperada.",
   "Enciclopédia Britannica – verbete 'Chocolate'")
tf(T, "origem dos alimentos", 2, 12, "O tomate é uma planta originária da Itália.", False,
   "O tomate é das Américas e só chegou à Europa depois das viagens dos espanhóis, no século XVI.",
   "Enciclopédia Britannica – verbete 'Tomato'")
mc(T, "técnicas", 2, 10, "Como se chama a técnica de cozinhar o pudim com a forma dentro de outra panela com água quente?",
   ["Banho-maria", "Fritura", "Grelhado", "Defumação"], "Banho-maria",
   "No banho-maria o calor chega devagar e por igual, e o pudim fica liso, sem furinhos.",
   "Enciclopédia Britannica – verbete 'Bain-marie'")
mc(T, "técnicas", 2, 12, "Como se chama a técnica de dourar alho e cebola em pouca gordura, mexendo sempre, antes de juntar outros ingredientes?",
   ["Refogar", "Gratinar", "Escaldar", "Marinar"], "Refogar",
   "O refogado é a base do feijão e do arroz em muitas casas brasileiras.",
   "Dicionário Houaiss da Língua Portuguesa – verbete 'refogar'")
mc(T, "queijos", 2, 10, "Qual queijo italiano, bem duro, é ralado por cima do macarrão e amadurece por pelo menos um ano?",
   ["Parmesão", "Muçarela", "Ricota", "Mascarpone"], "Parmesão",
   "O Parmigiano Reggiano original precisa maturar pelo menos 12 meses.",
   "Consorzio del Formaggio Parmigiano Reggiano")
mc(T, "Índia", 2, 12, "Como se chama a mistura de especiarias amarelada, com cúrcuma, que lembra a culinária indiana?",
   ["Curry", "Wasabi", "Shoyu", "Chimichurri"], "Curry",
   "O curry em pó junta cúrcuma, cominho, coentro e outras especiarias, inspirado em pratos da Índia.",
   "Enciclopédia Britannica – verbete 'Curry'", syn=("caril",))
mc(T, "Japão", 2, 10, "Qual pasta verde e muito ardida acompanha o sushi?",
   ["Wasabi", "Shoyu", "Missô", "Tahine"], "Wasabi",
   "O wasabi verdadeiro vem de uma raiz japonesa, mas muitos restaurantes servem uma imitação feita com raiz-forte.",
   "Enciclopédia Britannica – verbete 'Wasabi'")
mc(T, "Itália", 2, 12, "Qual sobremesa italiana leva biscoito molhado no café e creme de queijo mascarpone?",
   ["Tiramisù", "Panetone", "Cannoli", "Gelato"], "Tiramisù",
   "O nome tiramisù quer dizer 'me levanta' em italiano, por causa do café.",
   "Enciclopédia Britannica – verbete 'Tiramisu'", syn=("tiramisu",))
mc(T, "Portugal", 2, 10, "Qual peixe salgado e seco é o ingrediente mais famoso da cozinha portuguesa?",
   ["Bacalhau", "Salmão", "Atum", "Tilápia"], "Bacalhau",
   "Os portugueses dizem ter uma receita de bacalhau para cada dia do ano, embora o peixe venha de mares frios do norte.",
   "Enciclopédia Britannica – verbete 'Cod'")
mc(T, "pães do mundo", 2, 10, "Qual pão achatado e redondo, que forma um bolso por dentro, é típico do Oriente Médio?",
   ["Pão sírio", "Brioche", "Ciabatta", "Pão de forma"], "Pão sírio",
   "Ao assar em forno bem quente, o vapor estufa a massa e cria o bolso do pão sírio, também chamado pita.",
   "Enciclopédia Britannica – verbete 'Pita'", syn=("pita",))
mc(T, "pratos típicos", 2, 10, "Qual carne levemente salgada e seca ao ar, típica do Nordeste, é servida com macaxeira e manteiga de garrafa?",
   ["Carne de sol", "Picanha", "Cupim", "Rosbife"], "Carne de sol",
   "A carne de sol leva pouco sal e seca por pouco tempo, ficando mais macia que o charque.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(T, "doces", 2, 12, "Qual doce de origem portuguesa, feito de gemas cozidas em calda de açúcar, forma fios amarelos que enfeitam bolos?",
   ["Fios de ovos", "Glacê", "Chantilly", "Marzipã"], "Fios de ovos",
   "Os fios de ovos vêm da doçaria dos conventos portugueses, que usavam muitas gemas.",
   "Câmara Cascudo – História da Alimentação no Brasil", syn=("fios de ovo",))
op(T, "ingredientes", 2, 10, "Como se chama a uva desidratada que muita gente coloca no arroz de Natal?",
   "Uva-passa", ["uva-passa", "uva passa", "passa", "passas", "uvas-passas", "uvas passas"],
   "A uva-passa é a uva seca ao sol ou em secadores, que fica doce e enrugada.",
   "Embrapa Uva e Vinho", br=True)
mc(T, "nutrição", 2, 10, "Qual nutriente, presente no arroz, no pão e no macarrão, é a principal fonte de energia do corpo?",
   ["Carboidrato", "Proteína", "Vitamina", "Sal mineral"], "Carboidrato",
   "No corpo, os carboidratos viram glicose, o principal combustível das células.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
tf(T, "nutrição", 2, 12, "O Guia Alimentar para a População Brasileira recomenda evitar alimentos ultraprocessados.", True,
   "A regra de ouro do guia é preferir alimentos naturais ou pouco processados aos ultraprocessados.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira (2014)", br=True, ref="2026-10-13")
tf(T, "nomes regionais", 2, 10, "No Rio Grande do Sul, a tangerina é popularmente chamada de bergamota.", True,
   "A mesma fruta é chamada de tangerina, mexerica, mimosa ou bergamota, conforme a região do Brasil.",
   "Embrapa Mandioca e Fruticultura", br=True)
tf(T, "bebidas", 2, 12, "A cajuína, bebida típica do Piauí, é feita com suco de caju e não tem álcool.", True,
   "A cajuína é o suco de caju clarificado e cozido, e sua produção tradicional é patrimônio cultural registrado pelo IPHAN.",
   "IPHAN – Produção tradicional da cajuína no Piauí", br=True)
tf(T, "lanches", 2, 12, "O 'X' do X-salada vem da pronúncia da palavra inglesa 'cheese', que quer dizer queijo.", True,
   "'Cheese' soa parecido com 'xis', e o nome pegou nas lanchonetes brasileiras.",
   "Dicionário Houaiss da Língua Portuguesa", br=True)

# =========================================================== DIFÍCEIS
mc(T, "origem dos alimentos", 3, 13, "O café é originário de qual continente?",
   ["África", "América do Sul", "Ásia", "Europa"], "África",
   "O cafeeiro arábica é nativo das terras altas da Etiópia, no leste africano.",
   "Enciclopédia Britannica – verbete 'Coffee'")
mc(T, "utensílios", 3, 14, "Em qual estado ficam as paneleiras de Goiabeiras, que fazem as panelas de barro usadas na moqueca?",
   ["Espírito Santo", "Bahia", "Pernambuco", "Santa Catarina"], "Espírito Santo",
   "O ofício das paneleiras de Goiabeiras, em Vitória, foi o primeiro bem registrado no Livro dos Saberes do IPHAN, em 2002.",
   "IPHAN – Ofício das Paneleiras de Goiabeiras", br=True)
mc(T, "pratos típicos", 3, 14, "Qual prato do litoral do Paraná é cozido por horas numa panela de barro lacrada com massa de farinha?",
   ["Barreado", "Sarapatel", "Galinhada", "Buchada"], "Barreado",
   "A tampa é 'barreada' com uma massa de farinha e água, que impede o vapor de escapar.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(T, "época dos alimentos", 3, 13, "Em quais estações o pinhão, semente da araucária, é colhido e vendido no Sul do Brasil?",
   ["Outono e inverno", "Primavera e verão", "Só no verão", "O ano inteiro"], "Outono e inverno",
   "A colheita do pinhão começa em abril, e ele é a estrela das festas de inverno da região Sul.",
   "Embrapa Florestas", br=True)
mc(T, "África", 3, 14, "Qual prato do norte da África é feito com grãozinhos de sêmola de trigo cozidos no vapor?",
   ["Cuscuz marroquino", "Paella", "Homus", "Polenta"], "Cuscuz marroquino",
   "Os saberes ligados ao cuscuz de Marrocos, Argélia, Tunísia e Mauritânia são patrimônio da UNESCO desde 2020.",
   "UNESCO – Saberes e práticas ligados ao cuscuz (Patrimônio Imaterial, 2020)")
mc(T, "Índia", 3, 14, "Qual pão achatado indiano é assado grudado nas paredes de um forno de barro chamado tandoor?",
   ["Naan", "Bagel", "Brioche", "Focaccia"], "Naan",
   "No tandoor, a massa fica presa à parede quente e assa em poucos minutos.",
   "Enciclopédia Britannica – verbete 'Naan'")
mc(T, "Itália", 3, 13, "Em qual cidade italiana surgiu a pizza como a conhecemos hoje?",
   ["Nápoles", "Roma", "Milão", "Veneza"], "Nápoles",
   "A arte dos pizzaiolos napolitanos foi reconhecida como patrimônio da UNESCO em 2017.",
   "UNESCO – A arte do pizzaiolo napolitano (Patrimônio Imaterial, 2017)")
tf(T, "padaria", 3, 14, "O fermento químico em pó funciona com seres vivos, assim como o fermento biológico.", False,
   "O fermento biológico tem leveduras vivas; o químico solta gás por uma reação entre substâncias, sem seres vivos.",
   "Enciclopédia Britannica – verbete 'Baking powder'")
tf(T, "legumes", 3, 13, "A berinjela é uma raiz, assim como a cenoura.", False,
   "A berinjela é o fruto da planta e cresce pendurado nos galhos, como o tomate, seu parente.",
   "Embrapa Hortaliças")
mc(T, "pratos típicos", 3, 13, "Qual prato mineiro é uma massa firme de fubá cozido na água e acompanha o frango com quiabo?",
   ["Angu", "Tutu", "Torresmo", "Feijão tropeiro"], "Angu",
   "O angu é feito só de fubá, água e sal, mexido até virar uma massa firme.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
tf(T, "pratos típicos", 3, 14, "No Nordeste, a paçoca também pode ser um prato salgado, de carne de sol pilada com farinha de mandioca.", True,
   "A paçoca de pilão é comida de viagem dos sertanejos, porque dura muitos dias sem estragar.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "medidas", 3, 14, "Quantas colheres de chá cabem em uma colher de sopa?",
   "3", ["3", "três", "tres", "3 colheres", "três colheres"],
   "Na medida padrão de receitas, a colher de sopa tem 15 ml e a de chá, 5 ml.",
   "Senac – Técnicas de Cozinha")

# =========================================================== MUITO DIFÍCEIS
mc(T, "queijos", 4, 16, "Qual queijo francês redondo e cremoso, de casca branca, leva o nome de uma vila da Normandia?",
   ["Camembert", "Gouda", "Cheddar", "Roquefort"], "Camembert",
   "O camembert é parente do brie e tem casca branca formada por fungos.",
   "Enciclopédia Britannica – verbete 'Camembert cheese'")
mc(T, "México", 4, 16, "Qual molho mexicano escuro é feito com várias pimentas e chocolate?",
   ["Mole", "Guacamole", "Pesto", "Chimichurri"], "Mole",
   "O mole poblano, de Puebla, mistura dezenas de ingredientes, entre eles pimentas secas e cacau.",
   "Enciclopédia Britannica – verbete 'Mole'")
mc(T, "técnicas", 4, 16, "Como se chama a técnica de mergulhar legumes rapidamente em água fervente e depois em água com gelo?",
   ["Branqueamento", "Flambagem", "Empanamento", "Defumação"], "Branqueamento",
   "O choque térmico interrompe o cozimento e mantém a cor viva dos legumes.",
   "Embrapa Hortaliças")
mc(T, "pratos típicos", 4, 16, "Qual arroz típico do Maranhão leva uma folha azedinha chamada vinagreira?",
   ["Arroz de cuxá", "Arroz-doce", "Arroz de forno", "Arroz à grega"], "Arroz de cuxá",
   "O cuxá mistura vinagreira, gergelim, farinha e camarão seco, e é marca da cozinha de São Luís.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(T, "pratos típicos", 4, 16, "Qual torta salgada do Centro-Oeste leva frango, linguiça, queijo e guariroba, um palmito amargo?",
   ["Empadão goiano", "Torta capixaba", "Quiche", "Barreado"], "Empadão goiano",
   "A guariroba dá ao empadão um amargor característico da culinária de Goiás.",
   "Embrapa Cerrados", br=True)
op(T, "técnicas", 4, 16, "Qual técnica francesa cozinha alimentos embalados a vácuo em água com temperatura controlada?",
   "Sous-vide", ["sous-vide", "sous vide", "suvide", "su vide"],
   "Sous-vide quer dizer 'sob vácuo' em francês, e o alimento cozinha por igual em temperatura baixa e precisa.",
   "Enciclopédia Britannica – verbete 'Sous vide'")
