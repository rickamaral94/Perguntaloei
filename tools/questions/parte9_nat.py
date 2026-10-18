# Perguntas novas: natureza. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "nat"

# =========================================================== FÁCEIS (6–8 anos)
mc(T, "filhotes", 1, 6, "Como se chama o filhote da vaca?",
   ["Bezerro", "Potro", "Cabrito", "Leitão"], "Bezerro",
   "O bezerro mama o leite da vaca nos primeiros meses de vida.",
   "Dicionário Houaiss – verbete 'bezerro'")
mc(T, "filhotes", 1, 6, "Como se chama o filhote da galinha?",
   ["Pintinho", "Patinho", "Leitão", "Cordeiro"], "Pintinho",
   "O pintinho sai do ovo depois de uns 21 dias de choco e já nasce coberto de penugem.",
   "Embrapa – Criação de galinhas caipiras")
op(T, "filhotes", 1, 7, "Como se chama o filhote da ovelha?", "Cordeiro",
   ["cordeiro", "cordeirinho", "cordeira", "borrego", "borrega"],
   "O cordeiro, também chamado de borrego, nasce coberto de lã e mama o leite da ovelha.",
   "Dicionário Houaiss – verbete 'cordeiro'")
mc(T, "filhotes", 1, 7, "Como se chama o filhote do porco?",
   ["Leitão", "Bezerro", "Potro", "Pintinho"], "Leitão",
   "O leitão nasce em ninhadas grandes, muitas vezes com mais de dez irmãos.",
   "Embrapa Suínos e Aves")
mc(T, "sons dos animais", 1, 6, "Qual animal faz 'quá-quá'?",
   ["Pato", "Galinha", "Peru", "Pombo"], "Pato",
   "O 'quá-quá' é o som típico do pato, ave que vive perto da água e tem os pés com membranas para nadar.",
   "Enciclopédia Britannica – verbete 'duck'")
op(T, "sons dos animais", 1, 6, "Qual animal faz 'au-au'?", "Cachorro",
   ["cachorro", "cão", "cao", "cachorrinho", "cadela", "cachorra"],
   "O cachorro late para se comunicar, avisar sobre estranhos ou chamar atenção.",
   "Enciclopédia Britannica – verbete 'dog'")
mc(T, "sons dos animais", 1, 6, "Como se chama o som forte que o leão faz?",
   ["Rugido", "Latido", "Miado", "Relincho"], "Rugido",
   "O rugido do leão pode ser ouvido a vários quilômetros de distância na savana.",
   "Enciclopédia Britannica – verbete 'lion'")
tf(T, "alimentação animal", 1, 6, "O coelho é um animal que come carne.", False,
   "O coelho é herbívoro: come capim, folhas e outras plantas.",
   "Enciclopédia Britannica – verbete 'rabbit'")
mc(T, "habitats", 1, 6, "Onde vive a minhoca?",
   ["Debaixo da terra", "No fundo do mar", "Em ninhos nas árvores", "Em cavernas de gelo"],
   "Debaixo da terra",
   "A minhoca cava túneis no solo, o que ajuda a deixar a terra fofa e boa para as plantas.",
   "Embrapa – Minhocultura")
mc(T, "aves", 1, 6, "O que cobre o corpo de todas as aves?",
   ["Penas", "Pelos", "Escamas", "Espinhos"], "Penas",
   "As aves são os únicos animais atuais que têm penas, que ajudam a voar e a manter o corpo quente.",
   "Enciclopédia Britannica – verbete 'bird'")
mc(T, "plantas", 1, 6, "Qual parte da planta costuma ser colorida e perfumada para atrair as abelhas?",
   ["Flor", "Raiz", "Caule", "Semente"], "Flor",
   "As cores e o perfume das flores atraem abelhas e outros bichos que levam o pólen de uma flor para outra.",
   "Enciclopédia Britannica – verbete 'flower'")
mc(T, "plantas", 1, 7, "O que colocamos na terra para nascer um novo pé de feijão?",
   ["Semente", "Folha seca", "Pedra", "Areia"], "Semente",
   "Dentro da semente de feijão há uma plantinha em miniatura, que brota quando recebe água.",
   "Embrapa Arroz e Feijão")
mc(T, "fenômenos naturais", 1, 6, "Qual é o barulhão que ouvimos no céu logo depois de um relâmpago?",
   ["Trovão", "Granizo", "Arco-íris", "Neblina"], "Trovão",
   "O trovão é o som do ar que esquenta e se expande de repente com a descarga elétrica do raio.",
   "INPE – Grupo de Eletricidade Atmosférica (ELAT)")
tf(T, "répteis", 1, 6, "As cobras têm quatro patas.", False,
   "As cobras não têm patas e se deslocam rastejando, usando os músculos e as escamas da barriga.",
   "Instituto Butantan")
mc(T, "mamíferos", 1, 6, "Qual destes animais dá leite para os filhotes mamarem?",
   ["Cabra", "Galinha", "Tartaruga", "Pata"], "Cabra",
   "A cabra é um mamífero, e as fêmeas dos mamíferos alimentam os filhotes com leite.",
   "Enciclopédia Britannica – verbete 'mammal'")
mc(T, "répteis", 1, 7, "Qual destes animais nasce de um ovo?",
   ["Tartaruga", "Cachorro", "Gato", "Cavalo"], "Tartaruga",
   "As tartarugas botam ovos e os enterram na areia ou na terra; os filhotes cavam para sair.",
   "Projeto Tamar")
mc(T, "habitats", 1, 6, "Qual destes animais vive no gelo do Polo Norte?",
   ["Urso-polar", "Leão", "Camelo", "Macaco"], "Urso-polar",
   "O urso-polar vive no Ártico e caça focas sobre o gelo do mar.",
   "Enciclopédia Britannica – verbete 'polar bear'")
tf(T, "plantas", 1, 6, "As árvores são seres vivos.", True,
   "As árvores nascem, crescem, se alimentam, se reproduzem e morrem, como todo ser vivo.",
   "Enciclopédia Britannica – verbete 'tree'")
mc(T, "alimentação animal", 1, 7, "Qual é o alimento preferido do panda-gigante?",
   ["Bambu", "Peixe", "Banana", "Mel"], "Bambu",
   "O bambu forma quase toda a dieta do panda-gigante, que passa boa parte do dia comendo.",
   "Enciclopédia Britannica – verbete 'giant panda'")
op(T, "mamíferos", 1, 8, "Qual animal de orelhas compridas, parente do cavalo, faz um som chamado zurro?",
   "Burro", ["burro", "jumento", "jumenta", "asno", "jegue", "jerico"],
   "O burro, também chamado de jumento ou jegue, é muito usado no sertão para carregar peso.",
   "Enciclopédia Britannica – verbete 'donkey'")
mc(T, "fenômenos naturais", 1, 8, "Como se chama a montanha que pode soltar lava, cinzas e gases de dentro da Terra?",
   ["Vulcão", "Geleira", "Cânion", "Planalto"], "Vulcão",
   "A lava é a rocha derretida que vem do interior da Terra e sai pela boca do vulcão.",
   "Serviço Geológico do Brasil (SGB)")
tf(T, "aracnídeos", 1, 8, "As aranhas produzem fios de seda para fazer suas teias.", True,
   "A seda sai de glândulas na ponta do abdome da aranha e é muito resistente para o seu tamanho.",
   "Enciclopédia Britannica – verbete 'spider'")
mc(T, "plantas", 1, 8, "Como se chama a parte da planta que sustenta as folhas e as flores e, nas árvores, forma o tronco?",
   ["Caule", "Raiz", "Fruto", "Pétala"], "Caule",
   "O caule sustenta a planta e leva a água e os nutrientes da raiz até as folhas.",
   "Enciclopédia Britannica – verbete 'stem'")
tf(T, "mamíferos", 1, 8, "A baleia respira por um buraco no alto da cabeça.", True,
   "Esse buraco é o espiráculo; quando a baleia solta o ar, forma aquele jato que vemos de longe.",
   "Enciclopédia Britannica – verbete 'whale'")
mc(T, "répteis", 1, 8, "Qual destes animais troca a pele inteira de tempos em tempos e deixa para trás uma pele vazia?",
   ["Cobra", "Coelho", "Tatu", "Lesma"], "Cobra",
   "A cobra troca de pele porque cresce, e a pele velha sai inteira, como uma meia virada do avesso.",
   "Instituto Butantan")
tf(T, "fauna brasileira", 1, 8, "A capivara nada muito bem e vive perto de rios e lagos.", True,
   "A capivara tem membranas entre os dedos e costuma entrar na água para se refrescar e fugir de predadores.",
   "ICMBio", br=True)
mc(T, "peixes", 1, 8, "Qual parte do corpo os peixes usam para respirar dentro da água?",
   ["Brânquias", "Pulmões", "Nadadeiras", "Escamas"], "Brânquias",
   "As brânquias, também chamadas de guelras, retiram da água o oxigênio que o peixe precisa.",
   "Enciclopédia Britannica – verbete 'fish'", syn=("guelras",))
op(T, "peixes", 1, 8, "Qual peixe dos rios brasileiros é famoso pelos dentes afiados e costuma andar em cardumes?",
   "Piranha", ["piranha", "piranhas"],
   "As piranhas vivem em rios da Amazônia, do Pantanal e de outras bacias do Brasil e têm dentes triangulares bem afiados.",
   "Enciclopédia Britannica – verbete 'piranha'", br=True)

# =========================================================== MÉDIAS
mc(T, "fauna brasileira", 2, 9, "Qual animal brasileiro, parente do guaxinim, tem focinho comprido e cauda com anéis, que costuma ficar levantada?",
   ["Quati", "Tamanduá", "Gambá", "Irara"], "Quati",
   "O quati vive em bandos, é ótimo escalador e usa o focinho comprido para fuçar a terra atrás de comida.",
   "ICMBio", br=True)
mc(T, "répteis", 2, 10, "Qual é a maior cobra do Brasil, que vive em rios e pântanos e mata as presas apertando?",
   ["Sucuri", "Jararaca", "Cascavel", "Coral-verdadeira"], "Sucuri",
   "A sucuri não tem veneno: ela se enrola na presa e a aperta até sufocá-la.",
   "Instituto Butantan", br=True)
tf(T, "répteis", 2, 10, "A jiboia é uma cobra venenosa.", False,
   "A jiboia não tem veneno: ela mata as presas apertando-as com o corpo.",
   "Instituto Butantan", br=True)
mc(T, "répteis", 2, 10, "Qual cobra brasileira tem um chocalho na ponta da cauda?",
   ["Cascavel", "Jararaca", "Sucuri", "Jiboia"], "Cascavel",
   "O chocalho da cascavel é formado por anéis duros que fazem barulho quando ela balança a cauda, como um aviso.",
   "Instituto Butantan", br=True)
mc(T, "ecologia", 2, 10, "Como se chama a sequência que mostra quem come quem na natureza, como capim, gafanhoto e sapo?",
   ["Cadeia alimentar", "Ciclo da água", "Fotossíntese", "Migração"], "Cadeia alimentar",
   "Na cadeia alimentar, a energia passa das plantas para os animais que as comem e depois para os predadores.",
   "Enciclopédia Britannica – verbete 'food chain'")
mc(T, "ecologia", 2, 10, "Como se chamam os seres, como fungos e bactérias, que transformam restos de plantas e animais mortos em nutrientes para o solo?",
   ["Decompositores", "Produtores", "Predadores", "Parasitas"], "Decompositores",
   "Os decompositores fazem a reciclagem da natureza, devolvendo ao solo os nutrientes que as plantas vão usar.",
   "Enciclopédia Britannica – verbete 'decomposer'")
mc(T, "ecologia", 2, 10, "Como se chama o transporte do pólen de uma flor para outra, feito por abelhas, borboletas e beija-flores?",
   ["Polinização", "Germinação", "Fotossíntese", "Transpiração"], "Polinização",
   "Sem a polinização, muitas plantas não formariam frutos nem sementes.",
   "Embrapa – Polinizadores")
tf(T, "mamíferos", 2, 10, "Todos os morcegos se alimentam de sangue.", False,
   "Só três espécies de morcego se alimentam de sangue; a maioria come insetos, frutas ou néctar.",
   "Enciclopédia Britannica – verbete 'bat'")
tf(T, "fenômenos naturais", 2, 10, "O Brasil tem vulcões ativos em seu território.", False,
   "O Brasil fica no meio de uma placa tectônica e não tem vulcões ativos; ilhas como Fernando de Noronha são restos de vulcões muito antigos.",
   "Serviço Geológico do Brasil (SGB)", br=True)
mc(T, "fenômenos naturais", 2, 10, "Como se chama o tremor do chão causado pelo movimento das placas que formam a crosta da Terra?",
   ["Terremoto", "Furacão", "Tsunami", "Erupção"], "Terremoto",
   "Os terremotos acontecem principalmente nas bordas das placas tectônicas, quando elas se movem de repente.",
   "Serviço Geológico dos Estados Unidos (USGS)", syn=("sismo", "abalo sísmico"))
mc(T, "ciclo da água", 2, 10, "No ciclo da água, como se chama a queda da água das nuvens em forma de chuva, neve ou granizo?",
   ["Precipitação", "Evaporação", "Condensação", "Infiltração"], "Precipitação",
   "Depois da precipitação, a água corre para rios e mares ou se infiltra no solo, e o ciclo recomeça.",
   "Agência Nacional de Águas (ANA)")
mc(T, "alimentação animal", 2, 9, "Qual destes animais brasileiros se alimenta principalmente de carne?",
   ["Onça-pintada", "Capivara", "Anta", "Bicho-preguiça"], "Onça-pintada",
   "A onça-pintada é carnívora e caça capivaras, jacarés, queixadas e outros animais.",
   "ICMBio", br=True)
mc(T, "fauna brasileira", 2, 10, "Qual macaco brasileiro é famoso pelo ronco fortíssimo, que pode ser ouvido a quilômetros de distância?",
   ["Bugio", "Mico-leão-dourado", "Macaco-prego", "Sagui"], "Bugio",
   "O bugio, também chamado de guariba, tem um osso no pescoço que funciona como uma caixa de som.",
   "Enciclopédia Britannica – verbete 'howler monkey'", syn=("guariba",), br=True)
mc(T, "aracnídeos", 2, 10, "Qual destes animais é um aracnídeo, como a aranha?",
   ["Escorpião", "Formiga", "Besouro", "Centopeia"], "Escorpião",
   "Assim como as aranhas, os escorpiões têm oito patas e pertencem ao grupo dos aracnídeos.",
   "Instituto Butantan")
op(T, "insetos", 2, 10, "Em quantas partes se divide o corpo de um inseto?", "3",
   ["3", "três", "tres"],
   "O corpo dos insetos tem cabeça, tórax e abdome; as patas e as asas ficam presas no tórax.",
   "Enciclopédia Britannica – verbete 'insect'")
mc(T, "biomas", 2, 12, "Qual bioma brasileiro tem árvores de troncos tortos e casca grossa, que ajudam a resistir ao fogo?",
   ["Cerrado", "Pampa", "Pantanal", "Amazônia"], "Cerrado",
   "A casca grossa protege as árvores do Cerrado das queimadas naturais que acontecem na época seca.",
   "Embrapa Cerrados", br=True)
tf(T, "peixes", 2, 12, "O tubarão-baleia caça focas e outros animais grandes.", False,
   "Apesar do tamanho, o tubarão-baleia se alimenta filtrando da água o plâncton e peixes pequenos.",
   "Enciclopédia Britannica – verbete 'whale shark'")
mc(T, "ecologia", 2, 12, "Como se chama o ser vivo que vive à custa de outro e se alimenta dele, como o carrapato?",
   ["Parasita", "Predador", "Decompositor", "Polinizador"], "Parasita",
   "O carrapato se prende à pele de outros animais e suga o sangue deles, prejudicando o hospedeiro.",
   "Enciclopédia Britannica – verbete 'parasitism'")
mc(T, "insetos", 2, 10, "Qual inseto saltador é famoso por formar nuvens enormes que devoram plantações inteiras?",
   ["Gafanhoto", "Cigarra", "Joaninha", "Libélula"], "Gafanhoto",
   "Algumas espécies de gafanhoto se juntam em nuvens com milhões de insetos, que comem tudo por onde passam.",
   "Embrapa")
tf(T, "fauna brasileira", 2, 12, "O lobo-guará também come frutas, como a lobeira, além de pequenos animais.", True,
   "O lobo-guará é onívoro, e a lobeira, fruto do Cerrado, pode ser metade da sua alimentação.",
   "ICMBio", br=True)
tf(T, "peixes", 2, 10, "No cavalo-marinho, é a fêmea que carrega os ovos até os filhotes nascerem.", False,
   "No cavalo-marinho é o macho que guarda os ovos numa bolsa na barriga até os filhotes nascerem.",
   "Enciclopédia Britannica – verbete 'seahorse'")
mc(T, "árvores brasileiras", 2, 10, "Qual árvore brasileira tem tipos com flores amarelas, roxas, rosadas ou brancas e enche as ruas de cor quando floresce?",
   ["Ipê", "Araucária", "Seringueira", "Pau-brasil"], "Ipê",
   "Os ipês costumam perder as folhas antes de florir, e por isso a copa fica toda coberta de flores.",
   "Embrapa Florestas", br=True)
op(T, "plantas", 2, 10, "Como se chama o processo em que as plantas usam a luz do Sol, a água e o ar para fabricar o próprio alimento?",
   "Fotossíntese", ["fotossíntese", "fotossintese"],
   "Na fotossíntese, as plantas produzem açúcar e liberam o oxigênio que os animais respiram.",
   "Enciclopédia Britannica – verbete 'photosynthesis'")

# =========================================================== DIFÍCEIS
mc(T, "fauna brasileira", 3, 12, "Qual macaco brasileiro é conhecido por usar pedras como martelo para quebrar cocos e sementes duras?",
   ["Macaco-prego", "Bugio", "Muriqui", "Sagui"], "Macaco-prego",
   "Na Serra da Capivara, no Piauí, pesquisadores encontraram ferramentas de pedra usadas por macacos-prego há centenas de anos.",
   "Enciclopédia Britannica – verbete 'capuchin monkey'", br=True)
mc(T, "aves", 3, 12, "Qual ave é a mais rápida do mundo quando mergulha para caçar?",
   ["Falcão-peregrino", "Águia-careca", "Andorinha", "Avestruz"], "Falcão-peregrino",
   "No mergulho, o falcão-peregrino passa dos 300 km/h, sendo o animal mais veloz que se conhece.",
   "Enciclopédia Britannica – verbete 'peregrine falcon'")
mc(T, "fauna brasileira", 3, 12, "Qual é o nome brasileiro do ocelote, felino de pelo pintado menor que a onça?",
   ["Jaguatirica", "Suçuarana", "Lince", "Guepardo"], "Jaguatirica",
   "A jaguatirica vive em matas de quase todo o Brasil e caça principalmente à noite.",
   "ICMBio", br=True)
mc(T, "mamíferos", 3, 12, "Qual é a cor da pele do urso-polar, por baixo dos pelos?",
   ["Preta", "Branca", "Rosada", "Amarela"], "Preta",
   "A pele preta absorve o calor do Sol, e os pelos, que são transparentes, apenas parecem brancos.",
   "Enciclopédia Britannica – verbete 'polar bear'")
mc(T, "mamíferos", 3, 12, "Qual baleia vem todos os anos ao litoral da Bahia, na região de Abrolhos, para ter filhotes e é famosa pelos saltos e pelo 'canto'?",
   ["Baleia-jubarte", "Baleia-azul", "Orca", "Cachalote"], "Baleia-jubarte",
   "As jubartes saem das águas geladas da Antártida e chegam ao litoral brasileiro no inverno para se reproduzir.",
   "Instituto Baleia Jubarte", br=True)
mc(T, "anfíbios", 3, 12, "Qual salamandra do México consegue fazer crescer de novo as patas e a cauda perdidas?",
   ["Axolote", "Iguana", "Camaleão", "Lagartixa"], "Axolote",
   "O axolote regenera patas, cauda e até partes do coração e do cérebro, e por isso é muito estudado pela ciência.",
   "Enciclopédia Britannica – verbete 'axolotl'")
mc(T, "plantas", 3, 14, "Como se chama a planta que vive apoiada em outra sem tirar dela o alimento, como muitas orquídeas e bromélias?",
   ["Epífita", "Parasita", "Carnívora", "Trepadeira"], "Epífita",
   "As epífitas usam a árvore só como apoio e retiram água e nutrientes da chuva e do ar.",
   "Jardim Botânico do Rio de Janeiro")
mc(T, "árvores brasileiras", 3, 14, "Qual palmeira do Nordeste, chamada de 'árvore da vida', fornece uma cera usada em polidores e cosméticos?",
   ["Carnaúba", "Babaçu", "Buriti", "Açaí"], "Carnaúba",
   "A cera de carnaúba é tirada do pó que cobre as folhas da palmeira e é exportada pelo Brasil para o mundo todo.",
   "Embrapa", br=True)
tf(T, "mamíferos", 3, 14, "A equidna, assim como o ornitorrinco, é um mamífero que bota ovos.", True,
   "Equidnas e ornitorrincos formam o grupo dos monotremados, os únicos mamíferos que botam ovos.",
   "Enciclopédia Britannica – verbete 'monotreme'")
mc(T, "peixes", 3, 12, "Qual peixe da Amazônia é famoso por dar fortes choques elétricos?",
   ["Poraquê", "Pirarucu", "Tambaqui", "Piranha"], "Poraquê",
   "O poraquê, também chamado de enguia-elétrica, solta descargas de centenas de volts para caçar e se defender.",
   "Enciclopédia Britannica – verbete 'electric eel'", br=True)
tf(T, "fauna brasileira", 3, 12, "O tamanduá-bandeira não tem dentes.", True,
   "O tamanduá-bandeira não tem dentes: ele lambe formigas e cupins com a língua pegajosa e os engole inteiros.",
   "ICMBio", br=True)
op(T, "plantas", 3, 12, "Como se chama o momento em que a semente começa a brotar e dá origem a uma nova planta?",
   "Germinação", ["germinação", "germinacao"],
   "Para germinar, a semente precisa de água, ar e temperatura adequada.",
   "Embrapa")

# =========================================================== MUITO DIFÍCEIS
mc(T, "anfíbios", 4, 14, "A cecília, animal sem patas que parece uma minhoca grande, pertence a qual grupo?",
   ["Anfíbios", "Répteis", "Anelídeos", "Mamíferos"], "Anfíbios",
   "As cecílias são anfíbios, parentes dos sapos e das salamandras, e vivem enterradas no solo úmido.",
   "Enciclopédia Britannica – verbete 'caecilian'")
mc(T, "anfíbios", 4, 14, "Qual é o maior anfíbio do mundo?",
   ["Salamandra-gigante-chinesa", "Rã-golias", "Sapo-cururu", "Axolote"], "Salamandra-gigante-chinesa",
   "As salamandras-gigantes da China podem passar de 1,5 metro de comprimento.",
   "Enciclopédia Britannica – verbete 'giant salamander'")
mc(T, "ecologia", 4, 16, "Como se chama a estratégia de animais venenosos que têm cores fortes para avisar os predadores, como o sapinho-ponta-de-flecha?",
   ["Aposematismo", "Mimetismo", "Camuflagem", "Hibernação"], "Aposematismo",
   "As cores vivas funcionam como um aviso: o predador aprende que aquele animal faz mal e passa a evitá-lo.",
   "Enciclopédia Britannica – verbete 'aposematic coloration'")
mc(T, "plantas", 4, 14, "Como as samambaias se reproduzem, já que não produzem sementes?",
   ["Por esporos", "Por frutos", "Por bulbos", "Por flores"], "Por esporos",
   "Os esporos ficam em pontinhos escuros embaixo das folhas da samambaia e são levados pelo vento.",
   "Enciclopédia Britannica – verbete 'fern'", syn=("esporos",))
mc(T, "árvores brasileiras", 4, 16, "A madeira de qual árvore brasileira ameaçada é considerada a melhor para fazer arcos de violino?",
   ["Pau-brasil", "Mogno", "Jacarandá", "Cedro"], "Pau-brasil",
   "Fora do Brasil, o pau-brasil é conhecido como 'pernambuco', a madeira preferida dos fabricantes de arcos desde o século XVIII.",
   "Enciclopédia Britannica – verbete 'brazilwood'", br=True)
mc(T, "répteis", 4, 16, "Qual destes animais é o parente vivo mais próximo das aves?",
   ["Crocodilo", "Lagarto", "Tartaruga", "Cobra"], "Crocodilo",
   "Aves e crocodilos descendem de um mesmo grupo de répteis antigos, o mesmo que deu origem aos dinossauros.",
   "Enciclopédia Britannica – verbete 'archosaur'")
