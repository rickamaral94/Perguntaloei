# Perguntas novas: marcas. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "mar"

# =========================================================== FÁCEIS
op(T, "brinquedos", 1, 7, "Como se chama o namorado da boneca Barbie?", "Ken", ["ken"],
   "Ken foi lançado pela Mattel em 1961, dois anos depois da Barbie.",
   "Enciclopédia Britannica – verbete 'Barbie'")
mc(T, "doces", 1, 6, "O que são os M&M's?",
   ["Confeitos coloridos de chocolate", "Balas de goma", "Biscoitos recheados", "Pirulitos"],
   "Confeitos coloridos de chocolate",
   "Os M&M's são pastilhas de chocolate cobertas por uma casquinha de açúcar colorida.",
   "Enciclopédia Britannica – verbete 'Mars, Incorporated'")
mc(T, "embalagens", 1, 6, "Em que tipo de embalagem vem a batata Pringles?",
   ["Tubo", "Saquinho plástico", "Garrafa", "Pote de vidro"], "Tubo",
   "As batatas Pringles têm todas o mesmo formato e vêm empilhadas dentro de um tubo.",
   "Enciclopédia Britannica – verbete 'Pringles'", syn=("lata", "tubo cilíndrico"))
mc(T, "bebidas", 1, 6, "O Toddynho é que tipo de bebida?",
   ["Achocolatado", "Suco de uva", "Água de coco", "Refrigerante"], "Achocolatado",
   "O Toddynho é um achocolatado pronto para beber, vendido em caixinha com canudo.",
   "PepsiCo Brasil – marca Toddynho", br=True)
tf(T, "doces", 1, 6, "O creme Nutella é feito com morangos.", False,
   "A Nutella é um creme feito principalmente de avelãs, açúcar e cacau.",
   "Ferrero – história da Nutella")
mc(T, "logotipos", 1, 8, "Que animal verde aparece no logotipo da marca de roupas Lacoste?",
   ["Crocodilo", "Cavalo", "Leão", "Tubarão"], "Crocodilo",
   "O tenista francês René Lacoste tinha o apelido de crocodilo, e o bicho virou o símbolo da marca.",
   "Enciclopédia Britannica – verbete 'René Lacoste'", syn=("jacaré",))
mc(T, "logotipos", 1, 8, "De que cor é o robozinho que é símbolo do sistema Android?",
   ["Verde", "Azul", "Vermelho", "Amarelo"], "Verde",
   "O robô verde do Android foi criado em 2007 e aparece em muitos celulares.",
   "Android – Brand guidelines (Google)")
op(T, "veículos", 1, 8, "Que produto a marca brasileira Caloi é famosa por fabricar?", "Bicicleta",
   ["bicicleta", "bicicletas", "bike", "bikes"],
   "A Caloi nasceu em São Paulo e é uma das fabricantes de bicicletas mais antigas do Brasil.",
   "Caloi – história da empresa", br=True)
mc(T, "logotipos", 1, 8, "Que objeto do mar aparece no logotipo amarelo e vermelho da Shell?",
   ["Concha", "Estrela-do-mar", "Âncora", "Peixe"], "Concha",
   "Shell quer dizer concha em inglês, e a empresa começou vendendo conchas decorativas.",
   "Shell – história da marca")
mc(T, "mascotes", 1, 8, "O Dollynho, mascote que se apresenta como 'seu amiguinho', representa que tipo de bebida?",
   ["Refrigerante", "Leite", "Café", "Iogurte"], "Refrigerante",
   "O Dollynho é uma garrafinha de guaraná falante, mascote dos refrigerantes Dolly.",
   "Dolly Refrigerantes – site oficial", br=True)
mc(T, "mascotes", 1, 8, "O Chester, mascote de óculos escuros do salgadinho Cheetos, é qual animal?",
   ["Guepardo", "Leão", "Cachorro", "Raposa"], "Guepardo",
   "Chester é um guepardo, felino que em inglês se chama cheetah, palavra parecida com o nome do salgadinho.",
   "PepsiCo – marca Cheetos", syn=("chita",))
mc(T, "material escolar", 1, 8, "Qual destes produtos tornou famosa a marca Bic?",
   ["Canetas", "Tênis", "Bonecas", "Biscoitos"], "Canetas",
   "A caneta esferográfica Bic Cristal, lançada na França nos anos 1950, é uma das mais vendidas do mundo.",
   "Enciclopédia Britannica – verbete 'Bic'")
mc(T, "marcas que viraram nome", 1, 9, "Qual produto é vendido com a marca Maizena, que muita gente usa como nome comum?",
   ["Amido de milho", "Farinha de trigo", "Fermento", "Açúcar"], "Amido de milho",
   "Maizena é uma marca de amido de milho, mas no Brasil o nome virou sinônimo do próprio produto.",
   "Unilever Brasil – marca Maizena", br=True)
mc(T, "marcas que viraram nome", 1, 10, "Qual marca americana deu nome aos potes plásticos com tampa para guardar comida?",
   ["Tupperware", "Pyrex", "Tefal", "Tramontina"], "Tupperware",
   "Os potes Tupperware foram criados nos Estados Unidos por Earl Tupper, nos anos 1940.",
   "Enciclopédia Britannica – verbete 'Tupperware'")
op(T, "carros", 1, 10, "Em qual país nasceu a montadora BMW?", "Alemanha", ["alemanha"],
   "BMW é a sigla, em alemão, de Fábrica de Motores da Baviera, e sua sede fica em Munique.",
   "Enciclopédia Britannica – verbete 'BMW'")
tf(T, "carros", 1, 10, "A Volkswagen é uma montadora japonesa.", False,
   "A Volkswagen é alemã e tem sede na cidade de Wolfsburg.",
   "Enciclopédia Britannica – verbete 'Volkswagen Group'")
tf(T, "empresas brasileiras", 1, 10, "A Tramontina, famosa por talheres e panelas, é uma empresa brasileira.", True,
   "A Tramontina foi fundada em 1911 na cidade de Carlos Barbosa, no Rio Grande do Sul.",
   "Tramontina – história da empresa", br=True)
mc(T, "logotipos", 1, 10, "Quais cores formam a bola do logotipo da Pepsi?",
   ["Azul, vermelho e branco", "Verde, amarelo e azul", "Preto e laranja", "Roxo e rosa"],
   "Azul, vermelho e branco",
   "O logotipo da Pepsi é um círculo dividido em faixas vermelha, branca e azul.",
   "PepsiCo – história da marca Pepsi")
mc(T, "bancos", 1, 12, "Qual banco digital brasileiro ficou famoso pelo cartão de cor roxa?",
   ["Nubank", "Inter", "C6 Bank", "PicPay"], "Nubank",
   "O Nubank foi fundado em São Paulo em 2013 e escolheu o roxo como cor da marca.",
   "Nubank – sobre nós", br=True)
mc(T, "doces", 1, 10, "O bombom Sonho de Valsa é de qual marca?",
   ["Lacta", "Garoto", "Nestlé", "Hershey's"], "Lacta",
   "O Sonho de Valsa, com seu papel cor-de-rosa, é fabricado pela Lacta desde os anos 1930.",
   "Lacta – história da marca", br=True)
mc(T, "logotipos", 1, 9, "Qual aplicativo de mensagens tem como logotipo um telefone dentro de um balão verde?",
   ["WhatsApp", "Telegram", "Instagram", "Messenger"], "WhatsApp",
   "O balão verde com um telefone branco é o símbolo do WhatsApp.",
   "WhatsApp – Brand resources")
mc(T, "alimentos", 1, 9, "Que tipo de produto é o Leite Moça?",
   ["Leite condensado", "Leite em pó", "Creme de leite", "Iogurte"], "Leite condensado",
   "O Leite Moça é o leite condensado da Nestlé, muito usado para fazer brigadeiro e pudim.",
   "Nestlé Brasil – marca Moça", br=True)
mc(T, "logotipos", 1, 10, "Qual rede de pizzarias tem um telhado vermelho no logotipo?",
   ["Pizza Hut", "Domino's", "Subway", "Burger King"], "Pizza Hut",
   "Hut quer dizer cabana em inglês, por isso o logotipo da Pizza Hut mostra um telhado.",
   "Enciclopédia Britannica – verbete 'Pizza Hut'")
tf(T, "personagens", 1, 9, "A Hello Kitty foi criada no Japão.", True,
   "A Hello Kitty foi criada em 1974 pela empresa japonesa Sanrio.",
   "Enciclopédia Britannica – verbete 'Hello Kitty'")
mc(T, "carros", 1, 10, "Qual montadora fabricou no Brasil o carro Uno, lançado em 1984?",
   ["Fiat", "Volkswagen", "Ford", "Chevrolet"], "Fiat",
   "O Fiat Uno foi produzido em Betim, Minas Gerais, por quase trinta anos.",
   "Fiat Brasil – história do Uno", br=True)
mc(T, "tecnologia", 1, 9, "O Gmail, serviço de e-mail, pertence a qual empresa?",
   ["Google", "Microsoft", "Apple", "Yahoo"], "Google",
   "O Gmail foi lançado pelo Google em 2004.",
   "Google – história da empresa")
mc(T, "logotipos", 1, 9, "Qual marca esportiva tem um logotipo parecido com um sinal de 'certo', chamado swoosh?",
   ["Nike", "Adidas", "Puma", "Fila"], "Nike",
   "O swoosh foi desenhado em 1971 pela estudante Carolyn Davidson.",
   "Enciclopédia Britannica – verbete 'Nike, Inc.'")

# =========================================================== MÉDIAS
mc(T, "marcas que viraram nome", 2, 12, "Qual marca americana de lâminas de barbear deu origem à palavra que muitos brasileiros usam para qualquer lâmina?",
   ["Gillette", "Bic", "Schick", "Wilkinson"], "Gillette",
   "A Gillette, criada por King Camp Gillette, ficou tão conhecida que 'gilete' virou palavra do dicionário.",
   "Enciclopédia Britannica – verbete 'King Camp Gillette'", syn=("gilete",), br=True)
mc(T, "marcas que viraram nome", 2, 12, "Muita gente chama a fotocópia pelo nome de qual empresa americana?",
   ["Xerox", "Canon", "HP", "Epson"], "Xerox",
   "A Xerox popularizou as copiadoras, e 'xerox' virou sinônimo de cópia em papel.",
   "Enciclopédia Britannica – verbete 'Xerox Corporation'")
mc(T, "marcas que viraram nome", 2, 12, "No Brasil, a fita adesiva transparente é muitas vezes chamada pelo nome de qual marca?",
   ["Durex", "Pritt", "Bic", "Faber-Castell"], "Durex",
   "Durex foi a marca de fita adesiva da 3M no Brasil, e o nome passou a ser usado para qualquer fita.",
   "3M do Brasil – história", br=True)
tf(T, "marcas que viraram nome", 2, 12, "A palavra chiclete veio do nome de uma marca de goma de mascar.", True,
   "Chiclete vem de Chiclets, marca de goma de mascar em pastilhas da empresa americana Adams.",
   "Dicionário Houaiss – verbete 'chiclete'")
tf(T, "marcas que viraram nome", 2, 12, "Cotonete é o nome de uma marca que virou nome comum das hastes com algodão na ponta.", True,
   "Cotonete é marca registrada da Johnson & Johnson, mas o nome passou a ser usado para qualquer haste flexível.",
   "Johnson & Johnson Brasil – marca Cotonetes", br=True)
tf(T, "supermercados", 2, 12, "A rede de supermercados Carrefour é de origem americana.", False,
   "O Carrefour é francês; abriu seu primeiro hipermercado perto de Paris em 1963.",
   "Enciclopédia Britannica – verbete 'Carrefour'")
tf(T, "países de origem", 2, 12, "A Nokia, famosa pelos celulares, é uma empresa japonesa.", False,
   "A Nokia é finlandesa e começou, no século XIX, como uma fábrica de papel.",
   "Enciclopédia Britannica – verbete 'Nokia'")
tf(T, "tecnologia", 2, 12, "O WhatsApp foi comprado pelo Facebook em 2014.", True,
   "O Facebook anunciou a compra do WhatsApp em fevereiro de 2014.",
   "Enciclopédia Britannica – verbete 'WhatsApp'")
op(T, "tecnologia", 2, 12, "A Amazon começou, em 1995, vendendo qual produto pela internet?", "Livros",
   ["livros", "livro"],
   "Jeff Bezos criou a Amazon como uma livraria on-line antes de vender todo tipo de produto.",
   "Enciclopédia Britannica – verbete 'Amazon.com'")
mc(T, "brinquedos", 2, 10, "O Senhor Cabeça de Batata é um brinquedo de qual empresa?",
   ["Hasbro", "LEGO", "Nintendo", "Playmobil"], "Hasbro",
   "Lançado em 1952, o Senhor Cabeça de Batata foi um dos primeiros brinquedos anunciados na televisão.",
   "Hasbro – Mr. Potato Head")
mc(T, "países de origem", 2, 12, "A marca de balas de goma Haribo, famosa pelos ursinhos, é de qual país?",
   ["Alemanha", "Estados Unidos", "Japão", "Brasil"], "Alemanha",
   "O nome Haribo junta as primeiras letras de Hans Riegel, o fundador, e de Bonn, cidade alemã.",
   "Haribo – história da empresa")
mc(T, "países de origem", 2, 12, "A rede de lojas de roupas Zara é de qual país?",
   ["Espanha", "Itália", "França", "Portugal"], "Espanha",
   "A Zara abriu sua primeira loja em 1975 na cidade de La Coruña, na Galícia.",
   "Enciclopédia Britannica – verbete 'Zara'")
mc(T, "logotipos", 2, 12, "Qual montadora tem como logotipo uma figura dourada conhecida como 'gravatinha'?",
   ["Chevrolet", "Ford", "Fiat", "Renault"], "Chevrolet",
   "O símbolo da Chevrolet, em inglês 'bowtie', lembra uma gravata-borboleta.",
   "General Motors – história da Chevrolet")
mc(T, "logotipos", 2, 14, "Qual montadora japonesa tem três losangos vermelhos no logotipo, que lembram o significado do seu nome?",
   ["Mitsubishi", "Honda", "Nissan", "Suzuki"], "Mitsubishi",
   "Em japonês, Mitsubishi junta 'mitsu', que quer dizer três, e 'hishi', o formato de losango.",
   "Mitsubishi – origem do nome e da marca")
mc(T, "eletrodomésticos", 2, 14, "Qual marca de eletrodomésticos ficou tão famosa que virou expressão: 'não é assim uma...'?",
   ["Brastemp", "Electrolux", "Philco", "Arno"], "Brastemp",
   "A frase surgiu numa campanha publicitária dos anos 1990 e passou a indicar algo de qualidade.",
   "Memória da Propaganda – campanha Brastemp", br=True)
mc(T, "mascotes", 2, 12, "Qual animal é o mascote do sistema operacional Linux?",
   ["Pinguim", "Raposa", "Coruja", "Golfinho"], "Pinguim",
   "O pinguim gorducho do Linux se chama Tux e foi desenhado em 1996.",
   "The Linux Foundation – Tux")
mc(T, "alimentos", 2, 10, "Qual marca de cereais tem um galo na caixa de seus flocos de milho?",
   ["Kellogg's", "Nestlé", "Quaker", "Jasmine"], "Kellogg's",
   "O galo Cornelius aparece nas caixas de Corn Flakes da Kellogg's desde os anos 1950.",
   "Kellogg's – história da marca")
mc(T, "logotipos", 2, 14, "Que animais aparecem no logotipo da Hering, marca de roupas de Blumenau?",
   ["Dois peixes", "Dois pássaros", "Dois cavalos", "Duas abelhas"], "Dois peixes",
   "Hering quer dizer arenque, um peixe, em alemão; por isso o logotipo mostra dois peixinhos.",
   "Cia. Hering – história", br=True)
mc(T, "brinquedos", 2, 12, "Em que década a boneca Barbie foi lançada?",
   ["Anos 1950", "Anos 1970", "Anos 1980", "Anos 1990"], "Anos 1950",
   "A Barbie foi apresentada pela Mattel em março de 1959, numa feira de brinquedos em Nova York.",
   "Enciclopédia Britannica – verbete 'Barbie'")
mc(T, "doces", 2, 12, "Qual marca de chocolate usa uma vaca lilás nas embalagens?",
   ["Milka", "Lindt", "Hershey's", "Toblerone"], "Milka",
   "A vaca lilás é o símbolo da Milka desde o começo do século XX.",
   "Mondelez International – marca Milka")
mc(T, "marcas que viraram nome", 2, 12, "Qual empresa lançou o curativo adesivo Band-Aid?",
   ["Johnson & Johnson", "Colgate", "Nestlé", "Bayer"], "Johnson & Johnson",
   "O Band-Aid foi inventado em 1920 por Earle Dickson, funcionário da Johnson & Johnson.",
   "Johnson & Johnson – história do Band-Aid")
mc(T, "países de origem", 2, 12, "Os pneus Pirelli são de uma empresa de qual país?",
   ["Itália", "Alemanha", "França", "Japão"], "Itália",
   "A Pirelli foi fundada em Milão, em 1872.",
   "Enciclopédia Britannica – verbete 'Pirelli & C. SpA'")
mc(T, "veículos", 2, 14, "Qual marca americana de motocicletas foi fundada em Milwaukee, em 1903?",
   ["Harley-Davidson", "Honda", "Yamaha", "Ducati"], "Harley-Davidson",
   "A Harley-Davidson foi criada por William Harley e os irmãos Davidson.",
   "Enciclopédia Britannica – verbete 'Harley-Davidson'")

# =========================================================== DIFÍCEIS
op(T, "origem dos nomes", 3, 12, "O nome Volkswagen, em alemão, quer dizer o quê?", "Carro do povo",
   ["carro do povo", "automóvel do povo", "carro popular"],
   "A Volkswagen foi criada nos anos 1930 para fabricar um carro barato para a população.",
   "Enciclopédia Britannica – verbete 'Volkswagen Group'")
tf(T, "tecnologia", 3, 14, "Um dos criadores do Instagram, Mike Krieger, é brasileiro.", True,
   "Mike Krieger nasceu em São Paulo e fundou o Instagram com Kevin Systrom em 2010.",
   "Enciclopédia Britannica – verbete 'Instagram'", br=True)
tf(T, "empresas brasileiras", 3, 14, "A fábrica de chocolates Garoto nasceu no Espírito Santo.", True,
   "A Garoto foi fundada em 1929 em Vila Velha pelo imigrante alemão Henrique Meyerfreund.",
   "Chocolates Garoto – história", br=True)
tf(T, "países de origem", 3, 14, "O Spotify, aplicativo de músicas, foi criado nos Estados Unidos.", False,
   "O Spotify foi criado na Suécia, em 2006, por Daniel Ek e Martin Lorentzon.",
   "Enciclopédia Britannica – verbete 'Spotify'")
tf(T, "fundadores", 3, 14, "A marca Lacoste foi criada por um famoso jogador de futebol.", False,
   "René Lacoste foi um tenista francês campeão de Roland Garros e Wimbledon.",
   "Enciclopédia Britannica – verbete 'René Lacoste'")
tf(T, "países de origem", 3, 14, "O Mercado Livre foi fundado no Brasil.", False,
   "O Mercado Livre foi fundado na Argentina, em 1999, por Marcos Galperin.",
   "Mercado Livre – relações com investidores", br=True)
mc(T, "calçados", 3, 14, "Qual empresa gaúcha fabrica as sandálias de plástico Melissa?",
   ["Grendene", "Alpargatas", "Azaleia", "Vulcabras"], "Grendene",
   "A Grendene lançou a Melissa em 1979 e tem sede no Ceará e no Rio Grande do Sul.",
   "Grendene – história", br=True)
mc(T, "roupas", 3, 14, "Qual marca de calças jeans leva o nome do seu fundador, um imigrante alemão nos Estados Unidos?",
   ["Levi's", "Wrangler", "Lee", "Diesel"], "Levi's",
   "Levi Strauss e o alfaiate Jacob Davis patentearam em 1873 a calça de brim com rebites.",
   "Enciclopédia Britannica – verbete 'Levi Strauss'")
mc(T, "fundadores", 3, 14, "Qual marca esportiva foi fundada por Rudolf Dassler, irmão do fundador da Adidas?",
   ["Puma", "Nike", "Reebok", "Fila"], "Puma",
   "Os irmãos Dassler se separaram, e cada um criou sua marca na mesma cidade alemã, Herzogenaurach.",
   "Enciclopédia Britannica – verbete 'Adidas'")
mc(T, "origem dos nomes", 3, 14, "O nome da montadora sueca Volvo vem do latim e quer dizer o quê?",
   ["Eu rolo", "Eu corro", "Eu voo", "Eu venço"], "Eu rolo",
   "Volvo foi primeiro uma marca de rolamentos, peças que fazem rodas e eixos girarem.",
   "Volvo Cars – história da marca")
mc(T, "slogans", 3, 14, "Qual analgésico ficou famoso com um slogan que terminava com 'a dor sumiu'?",
   ["Doril", "Melhoral", "Aspirina", "Novalgina"], "Doril",
   "O bordão 'Tomou Doril, a dor sumiu' marcou a propaganda brasileira.",
   "Memória da Propaganda – campanha Doril", br=True)
mc(T, "propaganda", 3, 16, "Qual ator foi, por décadas, o garoto-propaganda da Bombril?",
   ["Carlos Moreno", "Tony Ramos", "Antonio Fagundes", "Marcos Caruso"], "Carlos Moreno",
   "Carlos Moreno estrelou os comerciais da Bombril a partir de 1978 e entrou para o Guinness pela longa parceria.",
   "Guinness World Records", br=True)

# =========================================================== MUITO DIFÍCEIS
op(T, "origem dos nomes", 4, 16, "A sigla Fiat quer dizer 'Fábrica Italiana de Automóveis de...' qual cidade?", "Turim",
   ["turim", "torino"],
   "A Fiat foi fundada em Turim, no norte da Itália, em 1899.",
   "Enciclopédia Britannica – verbete 'Fiat SpA'")
tf(T, "origem dos nomes", 4, 16, "O nome Adidas vem do apelido e do sobrenome do fundador, Adolf Dassler.", True,
   "Adolf Dassler era chamado de Adi; juntando 'Adi' com 'Das' surgiu Adidas.",
   "Enciclopédia Britannica – verbete 'Adidas'")
mc(T, "origem dos nomes", 4, 16, "De onde vem o nome da WEG, fabricante catarinense de motores elétricos?",
   ["Das iniciais dos três fundadores", "De uma palavra alemã que significa motor", "De um rio de Santa Catarina", "De uma sigla em inglês"],
   "Das iniciais dos três fundadores",
   "WEG junta as iniciais de Werner Voigt, Eggon da Silva e Geraldo Werninghaus, que fundaram a empresa em 1961.",
   "WEG – história da empresa", br=True)
mc(T, "alimentos", 4, 16, "Em qual estado brasileiro foi criado o requeijão Catupiry, em 1911?",
   ["Minas Gerais", "São Paulo", "Goiás", "Rio de Janeiro"], "Minas Gerais",
   "O imigrante italiano Mario Silvestrini criou o Catupiry na cidade mineira de Lambari.",
   "Catupiry – história", br=True)
mc(T, "logotipos", 4, 16, "Qual pintor desenhou o logotipo dos pirulitos Chupa Chups, em forma de flor?",
   ["Salvador Dalí", "Pablo Picasso", "Joan Miró", "Andy Warhol"], "Salvador Dalí",
   "Em 1969, o espanhol Salvador Dalí criou a margarida amarela que até hoje enfeita os pirulitos.",
   "Chupa Chups – história da marca")
mc(T, "origem dos nomes", 4, 16, "A palavra Mercedes, no nome da montadora Mercedes-Benz, homenageia quem?",
   ["A filha de um revendedor de carros", "Uma rainha da Espanha", "A esposa de Karl Benz", "Uma santa católica"],
   "A filha de um revendedor de carros",
   "O empresário Emil Jellinek vendia e corria com carros Daimler usando o nome da filha, Mercedes.",
   "Mercedes-Benz – história da marca")
