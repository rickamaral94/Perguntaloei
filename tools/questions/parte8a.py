# Perguntas novas (parte 8a): geografia, história, política, cultura brasileira, novelas e televisão.
from qdsl import mc, op, tf

# =========================================================== GEOGRAFIA
G = "geo"
mc(G, "relevo", 1, 6, "Como se chama a parte mais alta de uma montanha?",
   ["Cume", "Vale", "Foz", "Margem"], "Cume",
   "O cume, também chamado de topo, é o ponto mais alto de uma montanha.",
   "IBGE – Atlas Geográfico Escolar")
tf(G, "planeta", 1, 7, "A maior parte da superfície da Terra é coberta por água.", True,
   "Cerca de 71% da superfície do planeta é coberta por água, principalmente pelos oceanos.",
   "Enciclopédia Britannica – verbete 'Ocean'")
mc(G, "cidades do mundo", 1, 8, "Em qual país fica a cidade de Sydney, famosa por sua casa de ópera?",
   ["Austrália", "Nova Zelândia", "Canadá", "Inglaterra"], "Austrália",
   "A Ópera de Sydney, com seu teto em forma de velas, é um símbolo da Austrália.",
   "Enciclopédia Britannica – verbete 'Sydney'")
mc(G, "capitais", 1, 9, "Qual é a capital da Rússia?",
   ["Moscou", "São Petersburgo", "Minsk", "Varsóvia"], "Moscou",
   "Em Moscou ficam o Kremlin e a Praça Vermelha.",
   "Enciclopédia Britannica – verbete 'Moscow'")
mc(G, "desertos", 1, 9, "Qual é o maior deserto quente do mundo, no norte da África?",
   ["Saara", "Atacama", "Gobi", "Kalahari"], "Saara",
   "O Saara ocupa boa parte do norte da África, de um lado ao outro do continente.",
   "Enciclopédia Britannica – verbete 'Sahara'")
mc(G, "estados", 2, 10, "Qual é a capital do Rio Grande do Norte?",
   ["Natal", "João Pessoa", "Mossoró", "Maceió"], "Natal",
   "Natal é conhecida pelas dunas e pelo Forte dos Reis Magos.",
   "IBGE – Cidades", br=True)
op(G, "estados", 2, 10, "Qual é a capital do Mato Grosso?", "Cuiabá", ["cuiabá", "cuiaba"],
   "Cuiabá fica no centro da América do Sul e é conhecida pelo calor intenso.",
   "IBGE – Cidades", br=True)
mc(G, "capitais", 2, 12, "Qual é a capital da China?",
   ["Pequim", "Xangai", "Hong Kong", "Tóquio"], "Pequim",
   "Em Pequim fica a Cidade Proibida, antigo palácio dos imperadores chineses.",
   "Enciclopédia Britannica – verbete 'Beijing'", syn=("beijing",))
mc(G, "rios", 2, 12, "Qual rio atravessa a cidade de Paris?",
   ["Sena", "Tâmisa", "Reno", "Danúbio"], "Sena",
   "O rio Sena corta Paris e deságua no canal da Mancha.",
   "Enciclopédia Britannica – verbete 'Seine River'")
tf(G, "estados", 2, 12, "Rio Branco é a capital do Acre.", True,
   "O Acre fica no extremo oeste do Brasil, e sua capital é Rio Branco.",
   "IBGE – Cidades", br=True)
mc(G, "fronteiras", 2, 12, "Qual é o único estado brasileiro que faz fronteira com o Uruguai?",
   ["Rio Grande do Sul", "Santa Catarina", "Paraná", "Mato Grosso do Sul"], "Rio Grande do Sul",
   "Cidades como Santana do Livramento e Rivera ficam coladas na fronteira entre os dois países.",
   "IBGE – Atlas Geográfico Escolar", br=True)
mc(G, "montanhas", 2, 12, "Qual é a montanha mais alta do Japão, um vulcão de topo nevado?",
   ["Monte Fuji", "Monte Everest", "Monte Kilimanjaro", "Monte Branco"], "Monte Fuji",
   "O Monte Fuji tem cerca de 3.776 metros e é um símbolo do Japão.",
   "Enciclopédia Britannica – verbete 'Mount Fuji'")
mc(G, "montanhas", 3, 14, "Em qual país africano fica o monte Kilimanjaro, o ponto mais alto da África?",
   ["Tanzânia", "Quênia", "Etiópia", "Uganda"], "Tanzânia",
   "O Kilimanjaro fica no nordeste da Tanzânia, perto da fronteira com o Quênia.",
   "Enciclopédia Britannica – verbete 'Kilimanjaro'")
mc(G, "capitais", 3, 14, "Qual é a capital da Índia?",
   ["Nova Délhi", "Mumbai", "Calcutá", "Bangalore"], "Nova Délhi",
   "Mumbai é a maior cidade, mas a capital do país é Nova Délhi.",
   "Enciclopédia Britannica – verbete 'New Delhi'")
tf(G, "rios", 3, 14, "O rio Nilo deságua no mar Mediterrâneo.", True,
   "O Nilo corre para o norte e forma um grande delta no Egito antes de chegar ao Mediterrâneo.",
   "Enciclopédia Britannica – verbete 'Nile River'")
mc(G, "montanhas", 3, 14, "Em qual cordilheira asiática fica o Monte Everest?",
   ["Himalaia", "Andes", "Alpes", "Urais"], "Himalaia",
   "O Himalaia reúne as montanhas mais altas do planeta.",
   "Enciclopédia Britannica – verbete 'Himalayas'")
mc(G, "países", 3, 14, "Qual é o maior país da África em área?",
   ["Argélia", "Egito", "Nigéria", "África do Sul"], "Argélia",
   "A Argélia passou a ser o maior país africano depois da divisão do Sudão, em 2011.",
   "Enciclopédia Britannica – verbete 'Algeria'", ref="2026-10-13")
mc(G, "fronteiras", 3, 14, "O Monte Roraima marca a fronteira entre o Brasil, a Venezuela e qual outro país?",
   ["Guiana", "Suriname", "Colômbia", "Guiana Francesa"], "Guiana",
   "O topo achatado do Monte Roraima é dividido entre Brasil, Venezuela e Guiana.",
   "Enciclopédia Britannica – verbete 'Mount Roraima'", br=True)
mc(G, "capitais", 4, 16, "Qual é a capital da Mongólia?",
   ["Ulan Bator", "Astana", "Bishkek", "Tashkent"], "Ulan Bator",
   "Ulan Bator concentra quase metade da população da Mongólia.",
   "Enciclopédia Britannica – verbete 'Ulaanbaatar'", syn=("ulaanbaatar", "ulan bator"))
mc(G, "capitais", 4, 16, "Port Moresby é a capital de qual país da Oceania?",
   ["Papua-Nova Guiné", "Fiji", "Samoa", "Tonga"], "Papua-Nova Guiné",
   "Papua-Nova Guiné ocupa a metade leste da ilha de Nova Guiné.",
   "Enciclopédia Britannica – verbete 'Port Moresby'")

# =========================================================== HISTÓRIA
H = "his"
mc(H, "reis e rainhas", 1, 6, "O que os reis e as rainhas usavam na cabeça como símbolo de poder?",
   ["Coroa", "Boné", "Chapéu de palha", "Touca de natação"], "Coroa",
   "A coroa, muitas vezes de ouro e pedras preciosas, mostrava a autoridade do monarca.",
   "Enciclopédia Britannica – verbete 'Crown'")
mc(H, "vida antiga", 1, 7, "Antes da luz elétrica, o que as pessoas acendiam para iluminar a casa à noite?",
   ["Velas", "Lâmpadas de LED", "Lanternas de celular", "Televisões"], "Velas",
   "Velas e lampiões a óleo ou querosene eram a principal iluminação das casas.",
   "Enciclopédia Britannica – verbete 'Candle'")
tf(H, "Antiguidade", 1, 8, "Os antigos egípcios escreviam usando desenhos chamados hieróglifos.", True,
   "Os hieróglifos misturavam figuras que representavam ideias e sons.",
   "Enciclopédia Britannica – verbete 'Hieroglyph'")
mc(H, "Brasil Colônia", 1, 9, "O Brasil já foi colônia de qual país europeu?",
   ["Portugal", "Espanha", "França", "Inglaterra"], "Portugal",
   "O Brasil foi colônia portuguesa até a independência, em 1822.",
   "Enciclopédia Britannica – verbete 'Brazil'", br=True)
mc(H, "Segunda Guerra Mundial", 1, 10, "Qual país foi governado por Adolf Hitler durante a Segunda Guerra Mundial?",
   ["Alemanha", "Itália", "Japão", "Espanha"], "Alemanha",
   "Hitler governou a Alemanha nazista de 1933 a 1945.",
   "Enciclopédia Britannica – verbete 'Adolf Hitler'")
mc(H, "Antiguidade", 2, 12, "Em qual cidade da Grécia Antiga nasceu a democracia?",
   ["Atenas", "Esparta", "Roma", "Troia"], "Atenas",
   "Em Atenas, os cidadãos votavam diretamente nas assembleias.",
   "Enciclopédia Britannica – verbete 'Democracy'")
mc(H, "Idade Média", 2, 12, "Qual epidemia matou uma enorme parte da população da Europa no século XIV?",
   ["Peste Negra", "Gripe Espanhola", "Covid-19", "Febre amarela"], "Peste Negra",
   "A Peste Negra, uma epidemia de peste bubônica, devastou a Europa a partir de 1347.",
   "Enciclopédia Britannica – verbete 'Black Death'")
mc(H, "Segunda Guerra Mundial", 2, 12, "Qual país atacou a base americana de Pearl Harbor, em 1941?",
   ["Japão", "Alemanha", "Itália", "União Soviética"], "Japão",
   "O ataque japonês levou os Estados Unidos a entrar na Segunda Guerra Mundial.",
   "Enciclopédia Britannica – verbete 'Pearl Harbor attack'")
tf(H, "Primeira Guerra Mundial", 2, 12, "A Primeira Guerra Mundial terminou em 1918.", True,
   "O armistício que encerrou os combates foi assinado em 11 de novembro de 1918.",
   "Enciclopédia Britannica – verbete 'World War I'")
mc(H, "personalidades", 2, 12, "Qual líder indiano ficou famoso por lutar pela independência da Índia sem usar violência?",
   ["Mahatma Gandhi", "Nelson Mandela", "Martin Luther King", "Dalai Lama"], "Mahatma Gandhi",
   "Gandhi liderou protestos pacíficos contra o domínio britânico, e a Índia ficou independente em 1947.",
   "Enciclopédia Britannica – verbete 'Mahatma Gandhi'", syn=("gandhi",))
mc(H, "Brasil Império", 2, 12, "Às margens de qual riacho Dom Pedro I proclamou a independência do Brasil?",
   ["Ipiranga", "Tietê", "Carioca", "Anhangabaú"], "Ipiranga",
   "O riacho do Ipiranga fica na cidade de São Paulo.",
   "Enciclopédia Britannica – verbete 'Brazil'", br=True)
mc(H, "Brasil Colônia", 3, 14, "Como eram chamados os exploradores que saíam de São Paulo rumo ao interior em busca de ouro e de indígenas?",
   ["Bandeirantes", "Jesuítas", "Cangaceiros", "Imperadores"], "Bandeirantes",
   "As bandeiras ampliaram o território da colônia muito além da linha de Tordesilhas.",
   "Enciclopédia Britannica – verbete 'Bandeira'", br=True)
mc(H, "Brasil Império", 3, 14, "Qual nome recebeu o governo de Dom Pedro II, que foi de 1840 a 1889?",
   ["Segundo Reinado", "Primeiro Reinado", "Período Regencial", "República Velha"], "Segundo Reinado",
   "O Segundo Reinado começou com o Golpe da Maioridade e terminou com a Proclamação da República.",
   "Enciclopédia Britannica – verbete 'Pedro II'", br=True)
mc(H, "Brasil Império", 3, 14, "Em qual cidade a família real portuguesa desembarcou primeiro ao chegar ao Brasil, em 1808?",
   ["Salvador", "Rio de Janeiro", "Recife", "São Luís"], "Salvador",
   "A corte desembarcou em Salvador em janeiro de 1808 e seguiu para o Rio de Janeiro em março.",
   "Enciclopédia Britannica – verbete 'John VI'", br=True)
tf(H, "Idade Média", 3, 14, "Os mongóis, liderados por Gengis Khan, formaram um dos maiores impérios da história.", True,
   "O Império Mongol chegou a se estender da Coreia até o leste da Europa.",
   "Enciclopédia Britannica – verbete 'Mongol empire'")
op(H, "Idade Média", 3, 14, "Qual jovem camponesa francesa liderou tropas na Guerra dos Cem Anos e foi queimada em 1431?",
   "Joana d'Arc", ["joana d'arc", "joana darc", "joana d arc", "santa joana d'arc"],
   "Joana d'Arc foi declarada santa pela Igreja Católica em 1920.",
   "Enciclopédia Britannica – verbete 'Saint Joan of Arc'")
mc(H, "Antiguidade", 3, 16, "Quem foi o primeiro imperador de Roma?",
   ["Augusto", "Júlio César", "Nero", "Constantino"], "Augusto",
   "Júlio César nunca foi imperador; seu herdeiro Otávio recebeu o título de Augusto em 27 a.C.",
   "Enciclopédia Britannica – verbete 'Augustus'")
mc(H, "Idade Média", 4, 16, "Qual documento, assinado em 1215 pelo rei João da Inglaterra, limitou o poder do monarca?",
   ["Magna Carta", "Bill of Rights", "Édito de Nantes", "Tratado de Versalhes"], "Magna Carta",
   "A Magna Carta estabeleceu que nem o rei estava acima da lei.",
   "Enciclopédia Britannica – verbete 'Magna Carta'")
op(H, "Antiguidade", 4, 16, "Qual rei da Babilônia ficou famoso por um dos mais antigos códigos de leis escritas?",
   "Hamurábi", ["hamurábi", "hamurabi", "hammurabi"],
   "O código, gravado numa grande pedra, ficou conhecido pela regra do 'olho por olho'.",
   "Enciclopédia Britannica – verbete 'Code of Hammurabi'")

# =========================================================== POLÍTICA
P = "pol"
mc(P, "cidadania", 1, 6, "Quem apaga incêndios e resgata pessoas em perigo?",
   ["Os bombeiros", "Os carteiros", "Os padeiros", "Os pintores"], "Os bombeiros",
   "O Corpo de Bombeiros atende incêndios, salvamentos e acidentes.",
   "Corpo de Bombeiros Militar – institucional", br=True)
tf(P, "eleições", 1, 7, "No Brasil, o presidente da República é escolhido pelo voto dos eleitores.", True,
   "A eleição para presidente é direta: cada eleitor vota no seu candidato.",
   "Tribunal Superior Eleitoral", br=True)
mc(P, "eleições", 1, 8, "Na urna eletrônica, qual tecla o eleitor aperta para confirmar o voto?",
   ["Confirma", "Corrige", "Branco", "Desliga"], "Confirma",
   "A tecla verde 'Confirma' registra o voto; a laranja 'Corrige' apaga o número digitado.",
   "Tribunal Superior Eleitoral", br=True)
mc(P, "economia", 1, 8, "Qual é o nome do dinheiro usado no Brasil?",
   ["Real", "Peso", "Dólar", "Euro"], "Real",
   "O real é a moeda brasileira desde 1994.",
   "Banco Central do Brasil", br=True)
mc(P, "eleições", 1, 10, "Qual documento a pessoa recebe ao se cadastrar como eleitor?",
   ["Título de eleitor", "Certidão de nascimento", "Carteira de trabalho", "Passaporte"], "Título de eleitor",
   "O título de eleitor indica a zona e a seção onde a pessoa vota.",
   "Tribunal Superior Eleitoral", br=True)
mc(P, "siglas", 2, 12, "O que significa a sigla SUS?",
   ["Sistema Único de Saúde", "Serviço Universal de Segurança", "Sistema Unificado de Seguros", "Setor Único Social"],
   "Sistema Único de Saúde",
   "O SUS foi criado pela Constituição de 1988 e oferece atendimento de saúde gratuito.",
   "Ministério da Saúde", br=True)
mc(P, "organizações internacionais", 2, 12, "Qual agência da ONU trabalha pelos direitos das crianças no mundo?",
   ["UNICEF", "FMI", "OTAN", "OPEP"], "UNICEF",
   "O UNICEF é o Fundo das Nações Unidas para a Infância, criado em 1946.",
   "UNICEF – institucional")
mc(P, "organizações internacionais", 2, 12, "Qual é a sigla da Organização Mundial da Saúde?",
   ["OMS", "OEA", "OMC", "OIT"], "OMS",
   "A OMS foi criada em 1948 e tem sede em Genebra, na Suíça.",
   "Organização Mundial da Saúde – institucional")
op(P, "relações internacionais", 2, 12, "Como se chama o representante oficial que um país envia para outro país?",
   "Embaixador", ["embaixador", "embaixadora"],
   "O embaixador chefia a embaixada e representa seu país no exterior.",
   "Ministério das Relações Exteriores – Itamaraty")
tf(P, "poderes", 2, 12, "Os vereadores fazem parte do Poder Judiciário.", False,
   "Os vereadores integram o Poder Legislativo do município, na Câmara Municipal.",
   "Câmara dos Deputados – Constituição Federal", br=True)
mc(P, "siglas", 2, 14, "O que significa a sigla CLT, criada em 1943 no governo de Getúlio Vargas?",
   ["Consolidação das Leis do Trabalho", "Código Legal do Trabalhador", "Conselho de Leis Trabalhistas", "Cadastro Livre de Trabalho"],
   "Consolidação das Leis do Trabalho",
   "A CLT reuniu numa só lei as regras sobre emprego, férias e jornada de trabalho.",
   "Planalto – legislação (Decreto-Lei 5.452/1943)", br=True)
mc(P, "organizações internacionais", 3, 14, "Qual órgão da ONU cuida de educação, ciência e cultura e declara os Patrimônios da Humanidade?",
   ["UNESCO", "UNICEF", "OMS", "OIT"], "UNESCO",
   "A UNESCO mantém a lista do Patrimônio Mundial, que inclui lugares como Ouro Preto e Brasília.",
   "UNESCO – institucional")
mc(P, "história política", 3, 14, "Em que ano foi outorgada a primeira Constituição do Brasil, por Dom Pedro I?",
   ["1824", "1822", "1889", "1891"], "1824",
   "A Constituição de 1824 foi a que vigorou por mais tempo no país, até 1891.",
   "Planalto – legislação (Constituição de 1824)", br=True)
mc(P, "organizações internacionais", 3, 14, "Qual destes países é membro permanente do Conselho de Segurança da ONU?",
   ["França", "Brasil", "Alemanha", "Japão"], "França",
   "Os membros permanentes são Estados Unidos, Rússia, China, Reino Unido e França.",
   "ONU – Carta das Nações Unidas")
tf(P, "Congresso Nacional", 3, 14, "No prédio do Congresso Nacional, a cúpula virada para cima é a da Câmara dos Deputados.", True,
   "A cúpula côncava é da Câmara, e a convexa, virada para baixo, é do Senado.",
   "Câmara dos Deputados – institucional", br=True)
mc(P, "Legislativo", 4, 16, "Como se chama o órgão legislativo do Distrito Federal, onde trabalham os deputados distritais?",
   ["Câmara Legislativa", "Assembleia Legislativa", "Câmara Municipal", "Conselho Distrital"], "Câmara Legislativa",
   "O Distrito Federal não tem municípios nem vereadores; suas leis são feitas pela Câmara Legislativa.",
   "Planalto – Constituição Federal, art. 32", br=True)
mc(P, "eleições", 4, 16, "Por qual sistema são eleitos os deputados federais no Brasil, com vagas divididas conforme os votos de cada partido?",
   ["Proporcional", "Majoritário", "Distrital", "Indireto"], "Proporcional",
   "No sistema proporcional, as vagas são distribuídas entre os partidos pelo quociente eleitoral.",
   "Tribunal Superior Eleitoral", br=True)
op(P, "organizações internacionais", 4, 16, "Qual é o principal tribunal da ONU, com sede em Haia, que julga disputas entre países?",
   "Corte Internacional de Justiça",
   ["corte internacional de justiça", "corte internacional de justica", "tribunal internacional de justiça", "cij"],
   "A Corte Internacional de Justiça funciona no Palácio da Paz, na Holanda.",
   "ONU – Carta das Nações Unidas")

# =========================================================== CULTURA BRASILEIRA
C = "cul"
mc(C, "brincadeiras", 1, 6, "Qual brinquedo de madeira gira no chão depois de ser lançado com um barbante?",
   ["Pião", "Pipa", "Bambolê", "Bola de gude"], "Pião",
   "O pião é uma brincadeira tradicional em todo o Brasil.",
   "IPHAN – brinquedos populares", br=True)
mc(C, "festas", 1, 6, "Quais enfeites de papel colorido, pendurados em fios, decoram as festas juninas?",
   ["Bandeirinhas", "Bolas de Natal", "Ovos de Páscoa", "Abóboras"], "Bandeirinhas",
   "As bandeirinhas coloridas são o enfeite mais tradicional do arraial.",
   "IPHAN – festas juninas", br=True)
mc(C, "símbolos nacionais", 1, 7, "Qual é a cor do losango da bandeira do Brasil?",
   ["Amarelo", "Azul", "Branco", "Vermelho"], "Amarelo",
   "A bandeira tem um retângulo verde, um losango amarelo e um círculo azul.",
   "Planalto – legislação (Lei 5.700/1971)", br=True)
mc(C, "datas comemorativas", 1, 9, "Em que dia se comemora a Proclamação da República?",
   ["15 de novembro", "7 de setembro", "21 de abril", "1º de maio"], "15 de novembro",
   "A República foi proclamada em 15 de novembro de 1889.",
   "Planalto – legislação (feriados nacionais)", br=True)
tf(C, "datas comemorativas", 1, 9, "O Dia de Tiradentes, em 21 de abril, é feriado nacional.", True,
   "A data lembra a execução de Tiradentes, em 1792.",
   "Planalto – legislação (feriados nacionais)", br=True)
tf(C, "folclore", 2, 10, "O Dia do Folclore é comemorado em 22 de agosto.", True,
   "A data foi oficializada em 1965 para valorizar lendas, festas e tradições populares.",
   "Planalto – legislação (Decreto 56.747/1965)", br=True)
mc(C, "símbolos nacionais", 2, 12, "Quantos são os símbolos nacionais do Brasil, segundo a Constituição?",
   ["4", "2", "3", "5"], "4",
   "São a bandeira, o hino, as armas e o selo nacionais.",
   "Planalto – Constituição Federal, art. 13", br=True)
mc(C, "símbolos nacionais", 2, 12, "O que representam as estrelas da bandeira do Brasil?",
   ["Os estados e o Distrito Federal", "Os presidentes do país", "Os rios brasileiros", "Os santos padroeiros"],
   "Os estados e o Distrito Federal",
   "Cada estrela representa um estado ou o Distrito Federal.",
   "Planalto – legislação (Lei 5.700/1971)", br=True)
mc(C, "festas religiosas", 2, 12, "Em qual festa católica muitas cidades enfeitam as ruas com tapetes de serragem colorida?",
   ["Corpus Christi", "Natal", "Carnaval", "Festa Junina"], "Corpus Christi",
   "Os tapetes são feitos para a procissão de Corpus Christi passar por cima.",
   "IPHAN – festas religiosas", br=True)
mc(C, "artesanato", 3, 14, "Em qual cidade pernambucana viveu Mestre Vitalino, famoso pelos bonecos de barro?",
   ["Caruaru", "Olinda", "Petrolina", "Garanhuns"], "Caruaru",
   "O Alto do Moura, em Caruaru, é um dos maiores centros de arte figurativa em barro das Américas.",
   "IPHAN – Mestre Vitalino", br=True)
mc(C, "artesanato", 3, 14, "O artesanato de capim dourado é típico de qual estado?",
   ["Tocantins", "Bahia", "Piauí", "Goiás"], "Tocantins",
   "O capim dourado é colhido na região do Jalapão, no Tocantins.",
   "IPHAN – artesanato do Tocantins", br=True)
mc(C, "dança", 3, 14, "Qual cidade catarinense recebe um dos maiores festivais de dança do mundo e uma escola do Balé Bolshoi?",
   ["Joinville", "Blumenau", "Florianópolis", "Chapecó"], "Joinville",
   "A Escola do Teatro Bolshoi no Brasil é a única filial da escola russa fora da Rússia.",
   "Prefeitura de Joinville – institucional", br=True)
tf(C, "patrimônio", 3, 14, "O ofício das baianas de acarajé é registrado pelo IPHAN como patrimônio imaterial do Brasil.", True,
   "O registro foi feito em 2005, no Livro dos Saberes.",
   "IPHAN – Ofício das Baianas de Acarajé", br=True)
op(C, "tradições regionais", 3, 14, "Como se chama a entidade onde os gaúchos se reúnem para cultivar danças, trajes e costumes do Sul?",
   "Centro de Tradições Gaúchas", ["centro de tradições gaúchas", "centro de tradicoes gauchas", "ctg"],
   "Os CTGs existem no Rio Grande do Sul e em muitas outras partes do Brasil.",
   "Movimento Tradicionalista Gaúcho – institucional", br=True)
mc(C, "festas religiosas", 4, 16, "Qual cidade baiana do Recôncavo é famosa pela Festa da Boa Morte, de uma irmandade de mulheres negras?",
   ["Cachoeira", "Ilhéus", "Porto Seguro", "Juazeiro"], "Cachoeira",
   "A Irmandade da Boa Morte reúne mulheres negras devotas desde o século XIX.",
   "IPHAN – Cachoeira (BA)", br=True)
mc(C, "povos indígenas", 4, 16, "O Kuarup, ritual dos povos do Alto Xingu, é uma cerimônia em homenagem a quem?",
   ["Aos mortos", "Aos recém-nascidos", "À colheita do milho", "Aos visitantes"], "Aos mortos",
   "No Kuarup, troncos de madeira enfeitados representam pessoas importantes que morreram.",
   "Instituto Socioambiental – Povos Indígenas no Brasil", br=True)
mc(C, "símbolos nacionais", 4, 16, "Qual estrela aparece sozinha acima da faixa branca da bandeira do Brasil?",
   ["Espiga", "Sirius", "Canopus", "Antares"], "Espiga",
   "A Espiga, da constelação de Virgem, representa o estado do Pará.",
   "Planalto – legislação (Lei 5.700/1971)", br=True)

# =========================================================== NOVELAS
N = "nov"
mc(N, "bastidores", 1, 6, "Em que lugar fechado, com cenários montados, muitas cenas de novela são gravadas?",
   ["Estúdio", "Hospital", "Escola", "Supermercado"], "Estúdio",
   "Nos estúdios são montados cenários como casas, bares e escritórios.",
   "Memória Globo")
tf(N, "bastidores", 1, 6, "Os atores de novela precisam decorar as falas dos seus personagens.", True,
   "Os atores estudam o texto de cada capítulo antes das gravações.",
   "Memória Globo")
mc(N, "bastidores", 1, 8, "Como se chama o texto com as falas e as cenas que os atores recebem para gravar?",
   ["Roteiro", "Cardápio", "Bula", "Recibo"], "Roteiro",
   "O roteiro é escrito pelo autor e sua equipe, capítulo por capítulo.",
   "Memória Globo")
mc(N, "novelas infantis", 2, 9, "Na novela 'Carrossel', do SBT, por qual colega o menino Cirilo é apaixonado?",
   ["Maria Joaquina", "Valéria", "Laura", "Alícia"], "Maria Joaquina",
   "Maria Joaquina costuma esnobar Cirilo, mas ele nunca desiste.",
   "SBT – Carrossel", br=True)
mc(N, "novelas dos anos 2010", 1, 12, "Em 'Cheias de Charme' (2012), qual era a profissão das três protagonistas no começo da história?",
   ["Empregadas domésticas", "Professoras", "Enfermeiras", "Policiais"], "Empregadas domésticas",
   "Penha, Rosário e Cida trabalhavam como domésticas antes da fama.",
   "Memória Globo – Cheias de Charme", br=True)
mc(N, "novelas dos anos 2010", 2, 14, "Qual nome ganhou o grupo musical formado pelas três domésticas de 'Cheias de Charme'?",
   ["Empreguetes", "Chiquititas", "Rouge", "Frenéticas"], "Empreguetes",
   "O clipe das Empreguetes vazou na história e virou fenômeno também fora da novela.",
   "Memória Globo – Cheias de Charme", br=True)
mc(N, "novelas dos anos 2010", 2, 12, "Qual personagem bíblico protagoniza 'Os Dez Mandamentos', novela da Record que estreou em 2015?",
   ["Moisés", "Noé", "Davi", "Abraão"], "Moisés",
   "A novela conta a história de Moisés, que guiou os hebreus para fora do Egito.",
   "Record TV – Os Dez Mandamentos", br=True)
mc(N, "novelas dos anos 2010", 2, 14, "Qual país foi um dos principais cenários de 'Salve Jorge', novela que estreou em 2012?",
   ["Turquia", "Índia", "Marrocos", "Grécia"], "Turquia",
   "Parte da trama foi gravada na Capadócia e em Istambul.",
   "Memória Globo – Salve Jorge", br=True)
mc(N, "novelas dos anos 2000", 2, 14, "Em 'Páginas da Vida', novela que estreou em 2006, a menina Clara nasceu com qual condição?",
   ["Síndrome de Down", "Daltonismo", "Surdez", "Miopia"], "Síndrome de Down",
   "Clara foi criada por Helena, personagem de Regina Duarte.",
   "Memória Globo – Páginas da Vida", br=True)
mc(N, "novelas dos anos 2000", 2, 14, "Em 'Caminho das Índias' (2009), como se chamava a protagonista indiana vivida por Juliana Paes?",
   ["Maya", "Jade", "Bibi", "Serena"], "Maya",
   "Maya vivia dividida entre o casamento arranjado e o amor por Bahuan.",
   "Memória Globo – Caminho das Índias", br=True)
mc(N, "novelas dos anos 2000", 3, 16, "A novela 'O Cravo e a Rosa', que estreou em 2000, foi inspirada em qual peça de Shakespeare?",
   ["A Megera Domada", "Romeu e Julieta", "Hamlet", "Otelo"], "A Megera Domada",
   "Catarina e Petruchio repetem o casal brigão da comédia de Shakespeare.",
   "Memória Globo – O Cravo e a Rosa", br=True)
mc(N, "novelas dos anos 2010", 3, 16, "Em 'Fina Estampa', qual era o apelido de Griselda, a faz-tudo vivida por Lilia Cabral?",
   ["Pereirão", "Pé de Chinelo", "Mulher-Maravilha", "Dona Encrenca"], "Pereirão",
   "Griselda consertava de tudo e ganhou uma fortuna na loteria.",
   "Memória Globo – Fina Estampa", br=True)
mc(N, "novelas dos anos 2000", 3, 16, "Em 'Da Cor do Pecado' (2004), qual era o nome da protagonista vivida por Taís Araújo?",
   ["Preta", "Rosa", "Clara", "Dora"], "Preta",
   "Preta era uma feirante de São Luís que se apaixona por Paco, de Reynaldo Gianecchini.",
   "Memória Globo – Da Cor do Pecado", br=True)
mc(N, "novelas dos anos 2000", 3, 16, "Em 'Viver a Vida' (2009), qual atriz interpretou Helena, a primeira protagonista negra de Manoel Carlos?",
   ["Taís Araújo", "Camila Pitanga", "Juliana Paes", "Alinne Moraes"], "Taís Araújo",
   "Helena era uma modelo famosa que se casava com Marcos, personagem de José Mayer.",
   "Memória Globo – Viver a Vida", br=True)
mc(N, "novelas dos anos 2000", 3, 16, "Em 'América' (2005), qual era a profissão de Tião, personagem de Murilo Benício?",
   ["Peão de rodeio", "Médico", "Taxista", "Pescador"], "Peão de rodeio",
   "Tião sonhava em vencer o rodeio de Barretos e montar o touro Bandido.",
   "Memória Globo – América", br=True)
tf(N, "novelas dos anos 2000", 3, 16, "A Record exibiu uma nova versão de 'A Escrava Isaura' em 2004, com Bianca Rinaldi como protagonista.", True,
   "O remake foi um dos maiores sucessos de audiência da emissora naquela década.",
   "Record TV – A Escrava Isaura", br=True)
mc(N, "novelas dos anos 2010", 4, 16, "Qual era o nome da cidade nordestina fictícia de 'Cordel Encantado' (2011)?",
   ["Brogodó", "Asa Branca", "Sucupira", "Santana do Agreste"], "Brogodó",
   "Em Brogodó, a camponesa Açucena descobre ser a princesa do reino de Seráfia.",
   "Memória Globo – Cordel Encantado", br=True)
op(N, "novelas dos anos 2000", 4, 16, "Em 'Duas Caras', que estreou em 2007, qual era o nome da comunidade comandada por Juvenal Antena?",
   "Portelinha", ["portelinha", "favela da portelinha"],
   "Juvenal Antena, vivido por Antônio Fagundes, era o líder da Portelinha.",
   "Memória Globo – Duas Caras", br=True)

# =========================================================== TELEVISÃO
T = "tv"
mc(T, "programas infantis", 1, 6, "Quantos são os Teletubbies?",
   ["4", "3", "5", "2"], "4",
   "Os Teletubbies são Tinky Winky, Dipsy, Laa-Laa e Po.",
   "BBC – Teletubbies")
mc(T, "telejornais", 1, 7, "Como se chama a pessoa que lê as notícias num telejornal?",
   ["Apresentador", "Cozinheiro", "Goleiro", "Maestro"], "Apresentador",
   "O apresentador, também chamado de âncora, conduz o telejornal.",
   "Memória Globo")
mc(T, "programas infantis", 1, 8, "Qual programa infantil da TV Cultura se passa numa fazenda, com o menino Júlio e a galinha Lilica?",
   ["Cocoricó", "Castelo Rá-Tim-Bum", "Vila Sésamo", "X-Tudo"], "Cocoricó",
   "O 'Cocoricó' é feito com bonecos e estreou nos anos 1990.",
   "TV Cultura – Cocoricó", br=True)
tf(T, "telejornais", 1, 10, "O 'Bom Dia Brasil', da TV Globo, é um telejornal exibido pela manhã.", True,
   "Como o nome sugere, o 'Bom Dia Brasil' vai ao ar no começo do dia.",
   "Memória Globo – Bom Dia Brasil", br=True)
op(T, "programas infantis", 1, 10, "Qual palhaço famoso teve um programa infantil no SBT nos anos 1980?",
   "Bozo", ["bozo", "palhaço bozo"],
   "O personagem americano ganhou versão brasileira no SBT e marcou uma geração.",
   "SBT – memória", br=True)
mc(T, "programas infantis", 2, 10, "No programa 'TV Colosso', da Globo, os personagens eram bonecos de quais animais?",
   ["Cachorros", "Gatos", "Coelhos", "Ursos"], "Cachorros",
   "Na 'TV Colosso', uma emissora de TV era comandada por cães, como a apresentadora Priscila.",
   "Memória Globo – TV Colosso", br=True)
mc(T, "programas de entrevista", 2, 12, "Qual humorista e apresentador comandou um famoso talk show de fim de noite na Globo, de 2000 a 2016?",
   ["Jô Soares", "Chico Anysio", "Renato Aragão", "Fausto Silva"], "Jô Soares",
   "Antes da Globo, Jô Soares já fazia um programa de entrevistas no SBT.",
   "Memória Globo – Programa do Jô", br=True)
mc(T, "programas de auditório", 2, 12, "Qual programa de perguntas, apresentado por Silvio Santos a partir de 1999, dava até um milhão de reais ao vencedor?",
   ["Show do Milhão", "Qual é a Música?", "Passa ou Repassa", "Porta da Esperança"], "Show do Milhão",
   "Os participantes podiam pedir ajuda às cartas, aos universitários e às placas.",
   "SBT – memória", br=True)
mc(T, "humorísticos", 2, 12, "Qual humorístico do SBT tem como cenário principal um banco de praça?",
   ["A Praça é Nossa", "Zorra Total", "Escolinha do Professor Raimundo", "Sai de Baixo"], "A Praça é Nossa",
   "No programa, os humoristas vão se sentando no banco ao lado do apresentador.",
   "SBT – A Praça é Nossa", br=True)
mc(T, "programas de auditório", 2, 12, "Qual apresentador comandou por muitos anos o 'Domingo Legal', no SBT?",
   ["Gugu Liberato", "Faustão", "Luciano Huck", "Raul Gil"], "Gugu Liberato",
   "Gugu disputava a audiência das tardes de domingo com o 'Domingão do Faustão'.",
   "SBT – memória", br=True)
mc(T, "programas jornalísticos", 2, 12, "Qual programa da Globo é dedicado à agricultura e à vida no campo?",
   ["Globo Rural", "Globo Repórter", "Esporte Espetacular", "Mais Você"], "Globo Rural",
   "O 'Globo Rural' vai ao ar nas manhãs de domingo.",
   "Memória Globo – Globo Rural", br=True)
mc(T, "programas de auditório", 2, 14, "Qual apresentadora ficou famosa por dar selinhos nos convidados e chamar as pessoas de 'gracinha'?",
   ["Hebe Camargo", "Xuxa", "Angélica", "Eliana"], "Hebe Camargo",
   "Hebe foi uma das pioneiras da televisão brasileira, desde os anos 1950.",
   "Enciclopédia Itaú Cultural – verbete 'Hebe Camargo'", br=True)
mc(T, "telejornais", 3, 14, "Qual jornalista apresentou o 'Jornal Nacional' de 1969 a 1996 e ficou famoso pela voz grave?",
   ["Cid Moreira", "William Bonner", "Boris Casoy", "Galvão Bueno"], "Cid Moreira",
   "Cid Moreira apresentou a primeira edição do 'Jornal Nacional', em 1969.",
   "Memória Globo – Cid Moreira", br=True)
mc(T, "humorísticos", 3, 14, "Qual humorístico da Band tinha repórteres de terno preto e óculos escuros?",
   ["CQC", "Pânico na TV", "Zorra Total", "Casseta & Planeta"], "CQC",
   "O 'CQC – Custe o Que Custar' misturava humor e jornalismo.",
   "Band – CQC", br=True)
mc(T, "programas infantis", 3, 14, "Na série 'Mundo da Lua', da TV Cultura, o que o menino Lucas usava para narrar suas aventuras imaginárias?",
   ["Um gravador", "Um telescópio", "Um telefone", "Uma máquina de escrever"], "Um gravador",
   "Lucas Silva e Silva narrava suas fantasias num gravador, falando com o 'planeta Terra'.",
   "TV Cultura – Mundo da Lua", br=True)
tf(T, "programas de entrevista", 3, 14, "No 'Roda Viva', da TV Cultura, o entrevistado fica no centro de uma roda de jornalistas.", True,
   "O programa de entrevistas estreou em 1986 e ficou conhecido pelo cenário em forma de arena.",
   "TV Cultura – Roda Viva", br=True)
mc(T, "humorísticos", 4, 16, "Qual humorístico da Globo, de 1988, reunia Regina Casé e Marco Nanini em sátiras da própria televisão?",
   ["TV Pirata", "Viva o Gordo", "Os Trapalhões", "Zorra Total"], "TV Pirata",
   "O 'TV Pirata' parodiava novelas, telejornais e comerciais.",
   "Memória Globo – TV Pirata", br=True)
mc(T, "telejornais", 4, 16, "Qual telejornal da TV Tupi tinha o bordão 'testemunha ocular da história'?",
   ["Repórter Esso", "Jornal Nacional", "Jornal da Globo", "Aqui Agora"], "Repórter Esso",
   "O 'Repórter Esso' começou no rádio e depois ganhou versão na TV Tupi.",
   "Enciclopédia Itaú Cultural – verbete 'Repórter Esso'", br=True)
