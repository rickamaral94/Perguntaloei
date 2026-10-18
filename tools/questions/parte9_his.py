# Perguntas novas: história. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "his"

# =========================================================== FÁCEIS
tf(T, "pré-história", 1, 6, "Os homens das cavernas caçavam dinossauros.", False,
   "Os grandes dinossauros desapareceram há cerca de 66 milhões de anos, muito antes de existirem seres humanos.",
   "Enciclopédia Britannica – verbete 'Dinosaur'")
mc(T, "pré-história", 1, 6, "O que os povos pré-históricos aprenderam a controlar para se aquecer, cozinhar e espantar animais?",
   ["Fogo", "Gelo", "Vento", "Chuva"], "Fogo",
   "Dominar o fogo foi uma das descobertas mais importantes dos nossos antepassados.",
   "Enciclopédia Britannica – verbete 'Stone Age'")
mc(T, "pré-história", 1, 6, "Em que tipo de abrigo natural muitos povos pré-históricos se protegiam da chuva e do frio?",
   ["Cavernas", "Prédios", "Navios", "Castelos"], "Cavernas",
   "Cavernas e grutas serviam de abrigo, e em algumas delas ficaram pinturas feitas por esses povos.",
   "Enciclopédia Britannica – verbete 'Stone Age'")
mc(T, "vida antiga", 1, 6, "Antes de existir o fogão a gás, em que muitas famílias cozinhavam?",
   ["Fogão a lenha", "Micro-ondas", "Forno elétrico", "Air fryer"], "Fogão a lenha",
   "O fogão a lenha queima pedaços de madeira e ainda é usado em muitas casas do interior.",
   "Museu Paulista da USP – acervo de objetos domésticos")
mc(T, "vida antiga", 1, 6, "Antes de existir o avião, como as pessoas atravessavam o oceano?",
   ["De navio", "De ônibus", "De bicicleta", "De trem"], "De navio",
   "Por séculos, a única forma de cruzar o oceano era de barco, e a viagem podia levar semanas ou meses.",
   "Enciclopédia Britannica – verbete 'Ship'")
mc(T, "invenções antigas", 1, 6, "Qual invenção antiga, redonda, facilitou muito carregar coisas pesadas em carroças?",
   ["Roda", "Asa", "Vela", "Hélice"], "Roda",
   "A roda foi inventada há mais de 5 mil anos e mudou para sempre o transporte.",
   "Enciclopédia Britannica – verbete 'Wheel'")
tf(T, "pré-história", 1, 8, "Os povos pré-históricos já sabiam ler e escrever.", False,
   "A pré-história é justamente o período anterior à invenção da escrita.",
   "Enciclopédia Britannica – verbete 'Prehistoric'")
tf(T, "vida antiga", 1, 7, "Antigamente, muitas pessoas escreviam com penas de aves molhadas em tinta.", True,
   "As penas de ganso eram cortadas na ponta e usadas como caneta durante séculos.",
   "Enciclopédia Britannica – verbete 'Quill'")
tf(T, "idade média", 1, 7, "Os castelos medievais costumavam ter torres altas para vigiar quem se aproximava.", True,
   "Do alto das torres, os guardas viam os inimigos chegando de longe.",
   "Enciclopédia Britannica – verbete 'Castle'")
mc(T, "antiguidade", 1, 8, "Qual animal de estimação era tão respeitado no antigo Egito que alguns chegavam a ser mumificados?",
   ["Gato", "Coelho", "Hamster", "Papagaio"], "Gato",
   "Os egípcios ligavam os gatos à deusa Bastet, e arqueólogos já encontraram muitos gatos mumificados.",
   "Smithsonian Institution – Museu Nacional de História Natural")
mc(T, "idade média", 1, 8, "Como se chamava o artista que divertia o rei com piadas e palhaçadas na corte?",
   ["Bobo da corte", "Escudeiro", "Mordomo", "Ferreiro"], "Bobo da corte",
   "O bobo da corte usava roupas coloridas e chapéu com guizos para fazer a corte rir.",
   "Enciclopédia Britannica – verbete 'Fool'")
mc(T, "idade média", 1, 8, "Como se chama o buraco cheio de água que cercava muitos castelos para dificultar ataques?",
   ["Fosso", "Poço", "Lagoa", "Piscina"], "Fosso",
   "Para atravessar o fosso era preciso usar uma ponte levadiça, que podia ser erguida.",
   "Enciclopédia Britannica – verbete 'Moat'")
mc(T, "idade média", 1, 8, "De qual material eram feitas as espadas dos cavaleiros medievais?",
   ["Metal", "Plástico", "Papelão", "Vidro"], "Metal",
   "As espadas eram forjadas por ferreiros, principalmente com ferro e aço.",
   "Enciclopédia Britannica – verbete 'Sword'")
op(T, "antiguidade", 1, 9, "Qual rio, o mais famoso da África, era essencial para a vida no antigo Egito?", "Nilo",
   ["nilo", "rio nilo", "o nilo"],
   "As cheias do Nilo deixavam a terra fértil, e por isso o Egito foi chamado de 'dádiva do Nilo'.",
   "Enciclopédia Britannica – verbete 'Nile River'")
mc(T, "invenções antigas", 1, 9, "Qual destes itens foi inventado na China antiga?",
   ["Papel", "Avião", "Telefone", "Lâmpada"], "Papel",
   "Os chineses fabricavam papel com fibras vegetais há cerca de 2 mil anos.",
   "Enciclopédia Britannica – verbete 'Paper'")
op(T, "brasil império", 1, 9, "Segundo a tradição, qual frase Dom Pedro I gritou ao proclamar a independência do Brasil?",
   "Independência ou Morte",
   ["independência ou morte", "independencia ou morte", "independência ou morte!"],
   "O grito, às margens do Ipiranga, foi eternizado no quadro de Pedro Américo.",
   "Museu Paulista da USP – 'Independência ou Morte', de Pedro Américo", br=True)
mc(T, "antiguidade", 1, 9, "Em qual país atual fica a cidade de Roma, centro do antigo Império Romano?",
   ["Itália", "Grécia", "Egito", "Espanha"], "Itália",
   "Roma é hoje a capital da Itália e ainda guarda ruínas como o Fórum Romano.",
   "Enciclopédia Britannica – verbete 'Rome'")
mc(T, "antiguidade", 1, 10, "Qual arte, com tragédias e comédias encenadas ao ar livre, foi muito importante na Grécia Antiga?",
   ["Teatro", "Cinema", "Televisão", "Videogame"], "Teatro",
   "Os gregos construíam grandes teatros de pedra em forma de semicírculo.",
   "Enciclopédia Britannica – verbete 'Greek theatre'")
mc(T, "grandes navegações", 1, 10, "Além de Portugal, qual país europeu colonizou a maior parte da América do Sul?",
   ["Espanha", "Inglaterra", "Alemanha", "Itália"], "Espanha",
   "Por isso o espanhol é a língua mais falada nos países vizinhos do Brasil.",
   "Enciclopédia Britannica – verbete 'Latin America'")
op(T, "brasil colônia", 1, 10, "Como se chamavam as comunidades formadas por pessoas escravizadas que fugiam em busca de liberdade?",
   "Quilombos", ["quilombos", "quilombo", "mocambos", "mocambo"],
   "Muitas comunidades quilombolas existem até hoje e têm direito às suas terras pela Constituição.",
   "Fundação Cultural Palmares", br=True)
mc(T, "mundo moderno", 1, 10, "Qual máquina, movida pela força do vapor de água fervente, foi a grande invenção da Revolução Industrial?",
   ["Máquina a vapor", "Computador", "Motor elétrico", "Painel solar"], "Máquina a vapor",
   "As máquinas a vapor movimentavam fábricas, trens e navios no século XIX.",
   "Enciclopédia Britannica – verbete 'Steam engine'")
op(T, "brasil império", 1, 10, "Quem era o pai da Princesa Isabel?", "Dom Pedro II",
   ["dom pedro ii", "dom pedro 2", "dom pedro segundo", "pedro ii", "pedro segundo", "d. pedro ii"],
   "Isabel era a herdeira do trono e governou como regente nas viagens do pai.",
   "Museu Imperial de Petrópolis", br=True)
mc(T, "brasil colônia", 1, 10, "Por que Joaquim José da Silva Xavier ganhou o apelido de Tiradentes?",
   ["Porque também trabalhava arrancando dentes", "Porque perdeu todos os dentes",
    "Porque mordeu um soldado", "Porque vendia escovas de dente"],
   "Porque também trabalhava arrancando dentes",
   "Além de militar, ele exercia ofícios de dentista prático, comuns na época.",
   "Enciclopédia Britannica – verbete 'Tiradentes'", br=True)
mc(T, "brasil colônia", 1, 10, "Qual produto, feito da cana nos engenhos do Nordeste, foi a principal riqueza do Brasil nos seus primeiros séculos de colonização?",
   ["Açúcar", "Café", "Borracha", "Algodão"], "Açúcar",
   "O açúcar brasileiro era vendido para a Europa, onde valia muito.",
   "Enciclopédia Britannica – verbete 'Brazil: Colonial period'", br=True)
tf(T, "brasil império", 1, 10, "A Proclamação da República aconteceu antes da abolição da escravidão no Brasil.", False,
   "A Lei Áurea é de maio de 1888, e a República foi proclamada em novembro de 1889.",
   "Arquivo Nacional", br=True)
mc(T, "brasil colônia", 1, 10, "De qual continente vieram os milhões de pessoas trazidas à força para serem escravizadas no Brasil?",
   ["África", "Ásia", "Europa", "Oceania"], "África",
   "O Brasil foi o país que mais recebeu africanos escravizados nas Américas.",
   "IBGE – Brasil: 500 anos de povoamento", br=True)
tf(T, "brasil colônia", 1, 10, "Uma missa foi rezada pelos portugueses poucos dias depois da chegada da frota de Cabral ao Brasil.", True,
   "A primeira missa foi celebrada em 26 de abril de 1500, no litoral sul da Bahia.",
   "Carta de Pero Vaz de Caminha – Biblioteca Nacional", br=True)

# =========================================================== MÉDIAS
tf(T, "pré-história", 2, 12, "A invenção da agricultura permitiu que muitos grupos humanos deixassem de mudar de lugar o tempo todo.", True,
   "Plantando e criando animais, os grupos puderam fixar moradia e formar as primeiras aldeias.",
   "Enciclopédia Britannica – verbete 'Neolithic'")
mc(T, "antiguidade", 2, 12, "A antiga Mesopotâmia ficava entre quais dois rios?",
   ["Tigre e Eufrates", "Nilo e Jordão", "Reno e Danúbio", "Amazonas e Negro"], "Tigre e Eufrates",
   "O nome Mesopotâmia vem do grego e quer dizer 'terra entre rios'.",
   "Enciclopédia Britannica – verbete 'Mesopotamia'")
mc(T, "antiguidade", 2, 10, "Em que material, feito de uma planta das margens do Nilo, os antigos egípcios escreviam?",
   ["Papiro", "Seda", "Couro", "Argila"], "Papiro",
   "O papiro era feito de tiras do caule da planta, prensadas e secas ao sol.",
   "Enciclopédia Britannica – verbete 'Papyrus'")
mc(T, "antiguidade", 2, 12, "Qual rei da Macedônia conquistou um enorme império e fundou a cidade de Alexandria, no Egito?",
   ["Alexandre, o Grande", "Júlio César", "Ramsés II", "Dario I"], "Alexandre, o Grande",
   "Alexandre teve como professor o filósofo Aristóteles e morreu com apenas 32 anos.",
   "Enciclopédia Britannica – verbete 'Alexander the Great'")
mc(T, "antiguidade", 2, 12, "Qual cidade da Grécia Antiga era famosa por seus guerreiros e pela educação militar rígida?",
   ["Esparta", "Atenas", "Cartago", "Troia"], "Esparta",
   "Em Esparta, os meninos começavam o treinamento militar por volta dos 7 anos.",
   "Enciclopédia Britannica – verbete 'Sparta'")
mc(T, "antiguidade", 2, 12, "Como se chamava a antiga rede de caminhos comerciais que ligava a China ao Mediterrâneo?",
   ["Rota da Seda", "Estrada Real", "Rota do Sal", "Caminho de Santiago"], "Rota da Seda",
   "Por ela viajavam seda, especiarias, ideias e até religiões entre o Oriente e o Ocidente.",
   "UNESCO – Silk Roads Programme")
mc(T, "idade média", 2, 10, "Como se chamava o jovem que servia um cavaleiro e treinava para um dia virar cavaleiro também?",
   ["Escudeiro", "Bobo", "Monge", "Mensageiro"], "Escudeiro",
   "O escudeiro cuidava das armas e do cavalo do seu senhor.",
   "Enciclopédia Britannica – verbete 'Squire'")
mc(T, "idade média", 2, 12, "Como se chamavam os camponeses que trabalhavam nas terras do senhor feudal e não podiam deixá-las?",
   ["Servos", "Nobres", "Burgueses", "Cavaleiros"], "Servos",
   "Os servos entregavam ao senhor parte do que produziam em troca de proteção.",
   "Enciclopédia Britannica – verbete 'Serfdom'")
tf(T, "idade média", 2, 14, "A Peste Negra foi causada por um vírus.", False,
   "A peste é causada por uma bactéria, a Yersinia pestis, transmitida principalmente por pulgas.",
   "Organização Mundial da Saúde – Plague")
mc(T, "idade média", 2, 12, "Qual mercador de Veneza ficou famoso pelo relato de sua longa viagem até a China, no século XIII?",
   ["Marco Polo", "Vasco da Gama", "Américo Vespúcio", "Fernão de Magalhães"], "Marco Polo",
   "O livro com suas aventuras despertou na Europa a curiosidade pelo Oriente.",
   "Enciclopédia Britannica – verbete 'Marco Polo'")
mc(T, "grandes navegações", 2, 12, "Quem escreveu a carta ao rei de Portugal contando a chegada da frota de Cabral ao Brasil?",
   ["Pero Vaz de Caminha", "Padre Anchieta", "Pedro Álvares Cabral", "Américo Vespúcio"], "Pero Vaz de Caminha",
   "A carta, de 1500, é considerada a 'certidão de nascimento' do Brasil.",
   "Biblioteca Nacional – Carta de Pero Vaz de Caminha", br=True)
op(T, "grandes navegações", 2, 12, "Quantos navios Cristóvão Colombo levou na sua primeira viagem à América, em 1492?", "3",
   ["3", "três", "tres", "três navios"],
   "Eram a Santa María, a Pinta e a Niña.",
   "Enciclopédia Britannica – verbete 'Christopher Columbus'")
tf(T, "grandes navegações", 2, 12, "Cristóvão Colombo nasceu em Portugal.", False,
   "Segundo a maioria dos historiadores, Colombo nasceu em Gênova, na atual Itália.",
   "Enciclopédia Britannica – verbete 'Christopher Columbus'")
mc(T, "brasil colônia", 2, 12, "Como se chamavam as grandes faixas de terra em que o rei de Portugal dividiu o Brasil a partir de 1534?",
   ["Capitanias hereditárias", "Províncias", "Comarcas", "Regiões metropolitanas"], "Capitanias hereditárias",
   "Eram 'hereditárias' porque passavam de pai para filho entre os donatários.",
   "Arquivo Nacional – O Arquivo Nacional e a História Luso-Brasileira", br=True)
mc(T, "brasil colônia", 2, 12, "Qual cidade brasileira nasceu em 1554, a partir de um colégio fundado por padres jesuítas?",
   ["São Paulo", "Salvador", "Recife", "Belo Horizonte"], "São Paulo",
   "O colégio foi fundado em 25 de janeiro, data em que até hoje se comemora o aniversário da cidade.",
   "Prefeitura de São Paulo – História da cidade", br=True)
tf(T, "brasil império", 2, 12, "Dom Pedro II era apaixonado por ciência e foi um dos primeiros brasileiros a ter uma máquina fotográfica.", True,
   "Em 1840, ainda adolescente, ele comprou um daguerreótipo, um dos primeiros aparelhos de fotografia.",
   "Biblioteca Nacional – Coleção D. Thereza Christina Maria", br=True)
tf(T, "brasil república", 2, 12, "A família imperial continuou morando no Brasil depois da Proclamação da República.", False,
   "Poucos dias depois de 15 de novembro de 1889, a família imperial partiu para o exílio na Europa.",
   "Museu Imperial de Petrópolis", br=True)
tf(T, "brasil república", 2, 12, "Brasília foi inaugurada em 21 de abril, o mesmo dia em que se lembra Tiradentes.", True,
   "A inauguração foi em 21 de abril de 1960, data escolhida em homenagem ao herói da Inconfidência.",
   "Arquivo Público do Distrito Federal", br=True)
mc(T, "brasil república", 2, 12, "Qual empresa estatal de petróleo foi criada em 1953, no governo de Getúlio Vargas?",
   ["Petrobras", "Eletrobras", "Vale do Rio Doce", "Embraer"], "Petrobras",
   "A criação veio depois da campanha popular 'O petróleo é nosso'.",
   "Petrobras – Nossa história", br=True)
mc(T, "mundo moderno", 2, 12, "Como se chamavam as valas cavadas no chão onde os soldados se abrigavam na Primeira Guerra Mundial?",
   ["Trincheiras", "Bunkers", "Túneis do metrô", "Fossos de castelo"], "Trincheiras",
   "As trincheiras se estendiam por centenas de quilômetros e eram lamacentas e perigosas.",
   "Imperial War Museums – First World War")
mc(T, "mundo moderno", 2, 12, "Qual menina judia escreveu um famoso diário enquanto vivia escondida em Amsterdã durante a Segunda Guerra?",
   ["Anne Frank", "Malala Yousafzai", "Helen Keller", "Marie Curie"], "Anne Frank",
   "O diário foi publicado pelo pai dela, Otto, o único da família que sobreviveu.",
   "Casa de Anne Frank – Amsterdã")
mc(T, "mundo moderno", 2, 12, "Qual líder norte-americano fez o famoso discurso 'Eu tenho um sonho', em 1963?",
   ["Martin Luther King", "Abraham Lincoln", "John Kennedy", "Malcolm X"], "Martin Luther King",
   "O discurso, em Washington, pedia direitos iguais para negros e brancos nos Estados Unidos.",
   "The King Center – Atlanta")
mc(T, "mundo moderno", 2, 12, "Quais países eram os grandes rivais durante a Guerra Fria?",
   ["Estados Unidos e União Soviética", "Brasil e Argentina", "França e Inglaterra", "Japão e China"],
   "Estados Unidos e União Soviética",
   "Os dois disputaram poder e influência sem se enfrentar diretamente numa guerra.",
   "Enciclopédia Britannica – verbete 'Cold War'")

# =========================================================== DIFÍCEIS
op(T, "pré-história", 3, 14, "Qual apelido recebeu o crânio humano de cerca de 11 mil anos encontrado em Minas Gerais, um dos mais antigos das Américas?",
   "Luzia", ["luzia"],
   "O fóssil estava no Museu Nacional, no Rio, e foi recuperado em pedaços depois do incêndio de 2018.",
   "Museu Nacional – UFRJ", br=True)
mc(T, "pré-história", 3, 14, "Como se chamam os montes de conchas deixados por povos antigos no litoral brasileiro?",
   ["Sambaquis", "Quilombos", "Malocas", "Tabas"], "Sambaquis",
   "Alguns sambaquis têm milhares de anos e chegam a dezenas de metros de altura.",
   "IPHAN – Sítios arqueológicos", br=True)
mc(T, "antiguidade", 3, 14, "Como se chama a escrita da Mesopotâmia, feita com marcas em forma de cunha em placas de barro?",
   ["Cuneiforme", "Hieróglifo", "Rúnica", "Braille"], "Cuneiforme",
   "É um dos sistemas de escrita mais antigos que se conhecem, criado pelos sumérios.",
   "Museu Britânico – Writing in Mesopotamia")
mc(T, "antiguidade", 3, 14, "O que foi encontrado em 1974 perto do túmulo do primeiro imperador da China?",
   ["Milhares de estátuas de soldados de barro", "Um navio de ouro", "Uma biblioteca de papiros", "O esqueleto de um dragão"],
   "Milhares de estátuas de soldados de barro",
   "O chamado Exército de Terracota foi descoberto por agricultores que cavavam um poço.",
   "UNESCO – Mausoléu do primeiro imperador Qin")
tf(T, "antiguidade", 3, 14, "Os maias já usavam um símbolo para representar o número zero.", True,
   "O zero maia aparecia em seus calendários e era desenhado muitas vezes como uma concha.",
   "Enciclopédia Britannica – verbete 'Maya'")
mc(T, "brasil colônia", 3, 14, "Quem foi o primeiro governador-geral do Brasil, que fundou Salvador em 1549?",
   ["Tomé de Sousa", "Mem de Sá", "Martim Afonso de Sousa", "Duarte da Costa"], "Tomé de Sousa",
   "Ele chegou com os primeiros jesuítas, entre eles o padre Manuel da Nóbrega.",
   "Arquivo Nacional – Governo-Geral", br=True)
mc(T, "brasil colônia", 3, 14, "Qual governante holandês administrou o Nordeste brasileiro a partir do Recife, no século XVII?",
   ["Maurício de Nassau", "Pieter Heyn", "Guilherme de Orange", "Rembrandt"], "Maurício de Nassau",
   "Ele trouxe artistas e cientistas e mandou construir pontes e palácios no Recife.",
   "Instituto Ricardo Brennand – Coleção Brasil Holandês", br=True)
mc(T, "brasil império", 3, 14, "Como ficou conhecido o dia de 1822 em que Dom Pedro decidiu permanecer no Brasil em vez de voltar a Portugal?",
   ["Dia do Fico", "Dia da Partida", "Dia do Grito", "Dia da Coroação"], "Dia do Fico",
   "Em 9 de janeiro de 1822, ele disse que ficava 'para o bem de todos e felicidade geral da nação'.",
   "Arquivo Nacional", br=True)
mc(T, "brasil império", 3, 14, "Qual lei de 1871 declarou livres os filhos de mulheres escravizadas nascidos a partir dali?",
   ["Lei do Ventre Livre", "Lei Áurea", "Lei dos Sexagenários", "Lei Eusébio de Queirós"], "Lei do Ventre Livre",
   "Também chamada de Lei Rio Branco, foi um dos passos rumo à abolição.",
   "Câmara dos Deputados – Lei nº 2.040, de 1871", br=True)
mc(T, "brasil república", 3, 14, "Como eram chamados os trabalhadores, vindos de várias partes do país, que construíram Brasília?",
   ["Candangos", "Bandeirantes", "Tropeiros", "Retirantes"], "Candangos",
   "Uma escultura na Praça dos Três Poderes, 'Os Guerreiros', é conhecida como homenagem a eles.",
   "Arquivo Público do Distrito Federal", br=True)
mc(T, "brasil república", 3, 14, "Qual líder religioso comandava o arraial de Canudos, no sertão da Bahia, destruído em 1897?",
   ["Antônio Conselheiro", "Padre Cícero", "Lampião", "Frei Caneca"], "Antônio Conselheiro",
   "A Guerra de Canudos foi contada por Euclides da Cunha no livro 'Os Sertões'.",
   "Enciclopédia Britannica – verbete 'Canudos'", br=True)
mc(T, "mundo moderno", 3, 14, "Qual mulher negra foi presa em 1955 por se recusar a ceder o lugar no ônibus a um passageiro branco, nos Estados Unidos?",
   ["Rosa Parks", "Michelle Obama", "Harriet Tubman", "Oprah Winfrey"], "Rosa Parks",
   "Sua prisão, em Montgomery, deu início a um boicote aos ônibus que durou mais de um ano.",
   "Biblioteca do Congresso dos EUA – Rosa Parks Papers")

# =========================================================== MUITO DIFÍCEIS
op(T, "pré-história", 4, 16, "Qual apelido recebeu o famoso esqueleto de ancestral humano, com cerca de 3,2 milhões de anos, achado na Etiópia em 1974?",
   "Lucy", ["lucy", "luci"],
   "O nome veio da música 'Lucy in the Sky with Diamonds', dos Beatles, que tocava no acampamento.",
   "Museu de História Natural de Cleveland")
mc(T, "antiguidade", 4, 16, "Como se chamava o sistema de cordas com nós que os incas usavam para registrar números?",
   ["Quipu", "Ábaco", "Papiro", "Tear"], "Quipu",
   "A cor, a posição e o tipo de cada nó indicavam quantidades, como colheitas e tributos.",
   "Enciclopédia Britannica – verbete 'Quipu'")
mc(T, "grandes navegações", 4, 16, "Qual navegador português foi o primeiro europeu a contornar o sul da África, em 1488?",
   ["Bartolomeu Dias", "Gil Eanes", "Diogo Cão", "Nicolau Coelho"], "Bartolomeu Dias",
   "Ele abriu o caminho que Vasco da Gama seguiu dez anos depois até a Índia.",
   "Enciclopédia Britannica – verbete 'Bartolomeu Dias'")
tf(T, "grandes navegações", 4, 16, "Fernão de Magalhães completou pessoalmente a primeira volta ao mundo.", False,
   "Magalhães morreu nas Filipinas em 1521, e a viagem foi concluída em 1522 sob o comando de Juan Sebastián Elcano.",
   "Enciclopédia Britannica – verbete 'Ferdinand Magellan'")
mc(T, "brasil república", 4, 16, "Qual navio trouxe os primeiros imigrantes japoneses ao Brasil, em 1908?",
   ["Kasato Maru", "Titanic", "Mayflower", "Santa María"], "Kasato Maru",
   "O navio chegou ao porto de Santos em 18 de junho, data do Dia da Imigração Japonesa.",
   "Museu Histórico da Imigração Japonesa no Brasil", br=True)
mc(T, "brasil colônia", 4, 16, "Qual capitão português fundou a cidade do Rio de Janeiro, em 1565?",
   ["Estácio de Sá", "Tomé de Sousa", "Duarte Coelho", "Martim Afonso de Sousa"], "Estácio de Sá",
   "A cidade foi fundada em 1º de março de 1565, entre o Pão de Açúcar e o morro Cara de Cão.",
   "Prefeitura do Rio de Janeiro – História do Rio", br=True)
