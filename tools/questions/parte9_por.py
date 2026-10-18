# Perguntas novas: português. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "por"

GRAM = "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo"
BECH = "Evanildo Bechara – Moderna Gramática Portuguesa"
HOU = "Dicionário Houaiss da Língua Portuguesa"
VOLP = "Academia Brasileira de Letras – Vocabulário Ortográfico da Língua Portuguesa (VOLP)"

# =========================================================== FÁCEIS
mc(T, "onomatopeias", 1, 6, "Qual animal faz 'oinc-oinc'?",
   ["Porco", "Gato", "Pato", "Vaca"], "Porco",
   "'Oinc-oinc' é a palavra que imita o grunhido do porco, um exemplo de onomatopeia.",
   HOU)
mc(T, "onomatopeias", 1, 7, "Quando alguém diz 'atchim!', está imitando o som de quê?",
   ["Um espirro", "Uma risada", "Um choro", "Um assobio"], "Um espirro",
   "'Atchim' é a onomatopeia usada no Brasil para o barulho do espirro.",
   HOU)
mc(T, "rimas", 1, 6, "Qual destas palavras rima com 'janela'?",
   ["Panela", "Cadeira", "Sapato", "Mesa"], "Panela",
   "'Janela' e 'panela' terminam com o mesmo som, '-ela', por isso rimam.",
   GRAM)
tf(T, "rimas", 1, 6, "As palavras 'gato' e 'pato' rimam.", True,
   "As duas terminam com o mesmo som, '-ato', e por isso formam uma rima.",
   GRAM)
mc(T, "antônimos", 1, 6, "Qual é o contrário de 'alto'?",
   ["Baixo", "Gordo", "Forte", "Longe"], "Baixo",
   "'Alto' e 'baixo' são antônimos, palavras de sentido oposto.",
   HOU)
op(T, "antônimos", 1, 7, "Qual é o contrário de 'cheio'?", "Vazio", ["vazio", "vazia"],
   "Um copo cheio tem tudo ocupado; um copo vazio não tem nada dentro.",
   HOU)
op(T, "antônimos", 1, 6, "Qual é o contrário de 'subir'?", "Descer", ["descer", "desce"],
   "Subimos e descemos a escada: 'subir' e 'descer' são verbos de sentido oposto.",
   HOU)
mc(T, "masculino e feminino", 1, 7, "Qual é o feminino de 'leão'?",
   ["Leoa", "Leona", "Leãozinha", "Leonesa"], "Leoa",
   "A fêmea do leão é a leoa, que é quem mais caça no bando.",
   GRAM)
mc(T, "diminutivo", 1, 7, "Qual é o diminutivo de 'bola'?",
   ["Bolinha", "Bolão", "Bolada", "Boleiro"], "Bolinha",
   "O final '-inha' indica tamanho pequeno: bola pequena é bolinha.",
   GRAM)
tf(T, "antônimos", 1, 7, "As palavras 'bonito' e 'feio' têm sentidos contrários.", True,
   "'Bonito' e 'feio' são antônimos, palavras de significado oposto.",
   HOU)
mc(T, "ordem alfabética", 1, 8, "Em ordem alfabética, qual destas frutas vem primeiro?",
   ["Banana", "Laranja", "Maçã", "Uva"], "Banana",
   "Banana começa com B, que vem antes de L, M e U no alfabeto.",
   GRAM)
op(T, "alfabeto", 1, 7, "Qual é a última letra do alfabeto?", "Z", ["z", "zê", "ze", "letra z"],
   "O alfabeto da língua portuguesa vai do A ao Z.",
   VOLP)
mc(T, "expressões populares", 1, 9, "O que quer dizer a expressão 'pagar mico'?",
   ["Passar vergonha", "Pagar uma dívida", "Comprar um animal", "Ganhar um presente"], "Passar vergonha",
   "'Pagar mico' é uma expressão bem brasileira para quem passa por uma situação constrangedora.",
   HOU, br=True)
mc(T, "coletivos", 1, 9, "Como se chama um grupo de aves que voam juntas?",
   ["Bando", "Cardume", "Manada", "Enxame"], "Bando",
   "Um grupo de aves é chamado de bando; cardume é de peixes e enxame é de abelhas.",
   GRAM)
mc(T, "classes de palavras", 1, 9, "Qual destas palavras é um adjetivo?",
   ["Cheiroso", "Correr", "Mesa", "Ontem"], "Cheiroso",
   "Adjetivo indica uma característica: 'cheiroso' diz como algo é, como em 'bolo cheiroso'.",
   BECH)
tf(T, "classes de palavras", 1, 8, "A palavra 'mesa' é um verbo.", False,
   "'Mesa' é um substantivo, pois dá nome a um objeto; verbos indicam ações, como 'comer'.",
   BECH)
mc(T, "plural", 1, 8, "Qual é o plural de 'cão'?",
   ["Cães", "Cãos", "Cões", "Cãis"], "Cães",
   "Palavras terminadas em '-ão' têm plurais diferentes; o de 'cão' é 'cães', como o de 'pão' é 'pães'.",
   VOLP)
mc(T, "gentílicos", 1, 6, "Quem nasce no Brasil é chamado de quê?",
   ["Brasileiro", "Argentino", "Português", "Americano"], "Brasileiro",
   "O adjetivo pátrio de quem nasce no Brasil é 'brasileiro'.",
   "IBGE", br=True)
mc(T, "ditados", 1, 9, "Qual é o final do ditado 'Quem ri por último'?",
   ["Ri melhor", "Chora mais", "Fica sozinho", "Ganha o prêmio"], "Ri melhor",
   "O ditado ensina que não se deve comemorar antes da hora: quem ri por último ri melhor.",
   "Câmara Cascudo – Locuções Tradicionais no Brasil")
mc(T, "sinônimos", 1, 8, "Qual palavra quer dizer o mesmo que 'bonito'?",
   ["Belo", "Feio", "Baixo", "Triste"], "Belo",
   "'Bonito' e 'belo' são sinônimos, palavras com sentido parecido.",
   HOU)
mc(T, "alfabeto", 1, 6, "Qual destes bichos tem o nome começando pela vogal O?",
   ["Onça", "Gato", "Rato", "Leão"], "Onça",
   "'Onça' começa com O, uma das cinco vogais: A, E, I, O e U.",
   GRAM)
mc(T, "classes de palavras", 1, 9, "Na frase 'O menino chutou a bola', qual é a classe da palavra 'bola'?",
   ["Substantivo", "Verbo", "Adjetivo", "Advérbio"], "Substantivo",
   "'Bola' dá nome a um objeto, por isso é um substantivo; 'chutou' é o verbo da frase.",
   BECH)
tf(T, "classes de palavras", 1, 9, "Na frase 'Ana come maçã', a palavra 'come' é um verbo.", True,
   "'Come' indica a ação que Ana realiza; é uma forma do verbo 'comer'.",
   BECH)
mc(T, "sílabas", 1, 8, "Qual destas palavras tem três sílabas?",
   ["Macaco", "Sol", "Casa", "Hipopótamo"], "Macaco",
   "Ma-ca-co tem três sílabas; sol tem uma, casa tem duas e hipopótamo tem cinco.",
   GRAM)
mc(T, "masculino e feminino", 1, 8, "Qual é o feminino de 'carneiro'?",
   ["Ovelha", "Cabra", "Égua", "Vaca"], "Ovelha",
   "O carneiro é o macho e a ovelha é a fêmea; o feminino tem uma palavra totalmente diferente.",
   GRAM)
tf(T, "alfabeto", 1, 6, "A palavra 'elefante' começa com a mesma letra que 'janela'.", False,
   "'Elefante' começa com a vogal E, e 'janela' começa com a consoante J.",
   GRAM)
mc(T, "gentílicos", 1, 9, "Quem nasce em Minas Gerais é chamado de quê?",
   ["Mineiro", "Paulista", "Goiano", "Baiano"], "Mineiro",
   "O gentílico de Minas Gerais é 'mineiro'; paulista, goiano e baiano são de outros estados.",
   "IBGE", br=True)

# =========================================================== MÉDIAS
mc(T, "expressões populares", 2, 12, "O que quer dizer a expressão 'chover no molhado'?",
   ["Repetir o que já se sabe, sem adiantar nada", "Ficar muito triste",
    "Perder todo o dinheiro", "Chegar atrasado"], "Repetir o que já se sabe, sem adiantar nada",
   "Chover onde já está molhado não muda nada: a expressão indica insistir em algo óbvio ou inútil.",
   HOU)
mc(T, "expressões populares", 2, 12, "O que quer dizer a expressão 'enfiar o pé na jaca'?",
   ["Exagerar", "Tropeçar", "Desistir", "Fugir"], "Exagerar",
   "A expressão popular brasileira significa passar dos limites, principalmente ao comer ou beber.",
   HOU, br=True)
mc(T, "expressões populares", 2, 10, "Quando alguém 'pisa na bola', o que essa pessoa fez?",
   ["Cometeu um erro", "Fez um gol", "Ganhou um jogo", "Ficou cansada"], "Cometeu um erro",
   "'Pisar na bola' é uma expressão brasileira que significa errar ou decepcionar alguém.",
   HOU, br=True)
mc(T, "ditados", 2, 10, "Qual é o final do ditado 'Mais vale um pássaro na mão'?",
   ["Do que dois voando", "Do que nenhum no ninho", "Do que três na gaiola", "Do que um bando no céu"],
   "Do que dois voando",
   "O ditado ensina que é melhor garantir o que já se tem do que arriscar por algo incerto.",
   "Câmara Cascudo – Locuções Tradicionais no Brasil")
mc(T, "palavras de origem indígena", 2, 10, "Qual destes animais tem nome de origem tupi?",
   ["Capivara", "Cavalo", "Leão", "Elefante"], "Capivara",
   "'Capivara' vem do tupi e quer dizer algo como 'comedor de capim'.",
   HOU, br=True)
mc(T, "gentílicos", 2, 12, "Paulista é quem nasce no estado de São Paulo; e quem nasce na cidade de São Paulo é chamado de quê?",
   ["Paulistano", "Paulense", "Sampaulino", "Paulistense"], "Paulistano",
   "Quem nasce na capital paulista é paulistano, e quem nasce em qualquer parte do estado é paulista.",
   "IBGE", br=True)
mc(T, "gentílicos", 2, 12, "Quem nasce no estado do Acre é chamado de quê?",
   ["Acriano", "Amapaense", "Rondoniense", "Roraimense"], "Acriano",
   "O gentílico do Acre é 'acriano'; amapaense, rondoniense e roraimense são de outros estados do Norte.",
   VOLP, br=True)
mc(T, "aumentativo", 2, 10, "Qual é o aumentativo de 'nariz'?",
   ["Narigão", "Narizinho", "Narinas", "Nasal"], "Narigão",
   "Um nariz bem grande é um narigão; 'narizinho' é o diminutivo.",
   GRAM)
op(T, "coletivos", 2, 10, "Como se chama um grupo de bois?", "Boiada", ["boiada", "a boiada"],
   "'Boiada' é o coletivo de bois, palavra muito usada pelos vaqueiros e boiadeiros.",
   GRAM)
mc(T, "coletivos", 2, 10, "Como se chama um conjunto de chaves presas numa mesma argola?",
   ["Molho", "Cacho", "Feixe", "Penca"], "Molho",
   "Um conjunto de chaves é chamado de molho de chaves.",
   GRAM)
tf(T, "antônimos", 2, 10, "As palavras 'antigo' e 'moderno' são antônimos.", True,
   "'Antigo' é o que é de muito tempo atrás, e 'moderno' é o que é atual: sentidos opostos.",
   HOU)
tf(T, "sinônimos", 2, 12, "A palavra 'ligeiro' é sinônimo de 'lento'.", False,
   "'Ligeiro' quer dizer rápido; é justamente o contrário de lento.",
   HOU)
tf(T, "português pelo mundo", 2, 12, "Em Portugal, o café da manhã é chamado de 'pequeno-almoço'.", True,
   "Muitas palavras do dia a dia mudam entre o Brasil e Portugal, e o café da manhã é uma delas.",
   "Dicionário Priberam da Língua Portuguesa", br=True)
mc(T, "português pelo mundo", 2, 12, "Em Portugal, como se chama o ônibus?",
   ["Autocarro", "Comboio", "Elétrico", "Bonde"], "Autocarro",
   "Em Portugal o ônibus é o autocarro; 'comboio' é o trem e 'elétrico' é o bonde.",
   "Dicionário Priberam da Língua Portuguesa", br=True)
mc(T, "tempos verbais", 2, 10, "Na frase 'Amanhã eu viajarei', o verbo está em qual tempo?",
   ["Futuro", "Passado", "Presente", "Gerúndio"], "Futuro",
   "'Viajarei' indica algo que ainda vai acontecer, por isso está no futuro.",
   BECH)
mc(T, "classes de palavras", 2, 12, "Qual classe de palavras vem antes do substantivo, como 'o', 'um' e 'uma'?",
   ["Artigo", "Verbo", "Advérbio", "Interjeição"], "Artigo",
   "Os artigos acompanham o substantivo: 'o' e 'a' são definidos, 'um' e 'uma' são indefinidos.",
   BECH)
op(T, "classes de palavras", 2, 12, "Qual classe de palavras expressa emoções, como 'Oba!' e 'Ai!'?",
   "Interjeição", ["interjeição", "interjeicao", "interjeições", "interjeicoes"],
   "As interjeições exprimem sentimentos de forma rápida, como alegria, dor ou susto.",
   BECH)
mc(T, "palavras de origem estrangeira", 2, 10, "Qual destas palavras veio do inglês?",
   ["Futebol", "Bola", "Rede", "Torcida"], "Futebol",
   "'Futebol' é a adaptação do inglês 'football', o nome do esporte criado na Inglaterra.",
   HOU)
mc(T, "palavras de origem africana", 2, 12, "Qual destas palavras chegou ao português do Brasil vinda de uma língua africana?",
   ["Cafuné", "Janela", "Escola", "Cadeira"], "Cafuné",
   "'Cafuné', o carinho na cabeça, vem do quimbundo, língua falada em Angola.",
   HOU, br=True)
op(T, "palavras de origem estrangeira", 2, 12, "De qual língua vieram palavras como 'abajur', 'bufê' e 'garçom'?",
   "Francês", ["francês", "frances", "língua francesa", "lingua francesa", "da frança"],
   "As três vieram do francês: 'abat-jour', 'buffet' e 'garçon'.",
   HOU)
mc(T, "países de língua portuguesa", 2, 10, "Em qual destes países a língua oficial é o português?",
   ["Moçambique", "México", "Marrocos", "Peru"], "Moçambique",
   "Moçambique, no sudeste da África, é um dos países membros da CPLP.",
   "CPLP – Comunidade dos Países de Língua Portuguesa")
tf(T, "concordância", 2, 12, "Na frase 'Os meninos correm', o verbo está no singular.", False,
   "'Correm' está no plural, concordando com 'os meninos'; no singular seria 'o menino corre'.",
   BECH)
tf(T, "expressões populares", 2, 12, "A expressão 'ficar a ver navios' quer dizer ficar muito feliz.", False,
   "'Ficar a ver navios' significa ficar sem aquilo que se esperava, decepcionado.",
   HOU)

# =========================================================== DIFÍCEIS
mc(T, "gentílicos", 3, 14, "Quem nasce no estado do Rio Grande do Norte é chamado de quê?",
   ["Potiguar", "Capixaba", "Paraibano", "Cearense"], "Potiguar",
   "'Potiguar' vem do nome de um povo indígena da região e é o gentílico do Rio Grande do Norte.",
   "IBGE", br=True)
mc(T, "aumentativo", 3, 14, "Qual é o aumentativo de 'cão'?",
   ["Canzarrão", "Canil", "Canino", "Canícula"], "Canzarrão",
   "As gramáticas registram 'canzarrão' como aumentativo de 'cão'.",
   GRAM)
tf(T, "palavras de origem africana", 3, 14, "A palavra 'caçula', usada para o filho mais novo, tem origem em línguas africanas.", True,
   "'Caçula' vem do quimbundo, língua de Angola trazida ao Brasil por africanos escravizados.",
   HOU, br=True)
tf(T, "países de língua portuguesa", 3, 14, "O português é uma das línguas oficiais de Timor-Leste, na Ásia.", True,
   "Timor-Leste tem duas línguas oficiais, o português e o tétum, e faz parte da CPLP.",
   "CPLP – Comunidade dos Países de Língua Portuguesa")
tf(T, "palavras de origem estrangeira", 3, 14, "A palavra 'chocolate' chegou ao português vinda do árabe.", False,
   "'Chocolate' vem do náuatle, língua dos astecas, e chegou ao português pelo espanhol.",
   HOU)
tf(T, "acordo ortográfico", 3, 14, "O Acordo Ortográfico de 1990 mudou a forma como as palavras são pronunciadas.", False,
   "O acordo trata só da escrita; a pronúncia de cada país continua a mesma.",
   "Decreto nº 6.583/2008 – Acordo Ortográfico da Língua Portuguesa")
mc(T, "figuras de linguagem", 3, 14, "Qual figura de linguagem repete uma ideia para reforçá-la, como em 'Vi com meus próprios olhos'?",
   ["Pleonasmo", "Hipérbole", "Metáfora", "Ironia"], "Pleonasmo",
   "Só se vê com os olhos; repetir isso de propósito, para dar ênfase, é um pleonasmo.",
   BECH)
mc(T, "figuras de linguagem", 3, 14, "Qual figura de linguagem repete o mesmo som de consoante, como em 'O rato roeu a roupa do rei de Roma'?",
   ["Aliteração", "Eufemismo", "Antítese", "Pleonasmo"], "Aliteração",
   "A aliteração repete sons de consoantes, recurso comum em trava-línguas e poemas.",
   BECH)
mc(T, "palavras de origem indígena", 3, 14, "Em nomes de origem tupi, como Itaquera e Itapuã, o pedaço 'ita' quer dizer o quê?",
   ["Pedra", "Água", "Pássaro", "Fogo"], "Pedra",
   "'Itá' significa pedra em tupi e aparece em muitos nomes de lugares do Brasil.",
   "Eduardo de Almeida Navarro – Dicionário de Tupi Antigo", br=True)
mc(T, "coletivos", 3, 14, "Qual é o coletivo de porcos?",
   ["Vara", "Matilha", "Cáfila", "Récua"], "Vara",
   "Um grupo de porcos é uma vara; matilha é de cães, cáfila de camelos e récua de animais de carga.",
   GRAM)
mc(T, "palavras de origem estrangeira", 3, 14, "De qual língua veio a despedida 'tchau', tão usada no Brasil?",
   ["Italiano", "Francês", "Inglês", "Alemão"], "Italiano",
   "'Tchau' vem do italiano 'ciao' e se popularizou no Brasil com os imigrantes italianos.",
   HOU, br=True)
op(T, "estudo das palavras", 3, 14, "Como se chama o estudo da origem das palavras?", "Etimologia",
   ["etimologia", "a etimologia"],
   "A etimologia investiga de onde vem cada palavra e como seu sentido mudou com o tempo.",
   HOU)

# =========================================================== MUITO DIFÍCEIS
mc(T, "plural", 4, 16, "Qual é o plural de 'caráter'?",
   ["Caracteres", "Caráteres", "Caráters", "Caratéis"], "Caracteres",
   "O plural de 'caráter' é 'caracteres', com a sílaba mais forte deslocada para '-te-'.",
   VOLP)
mc(T, "gentílicos", 4, 16, "Quem nasce em Madagascar é chamado de quê?",
   ["Malgaxe", "Maltês", "Malaio", "Malinês"], "Malgaxe",
   "'Malgaxe' é o gentílico de Madagascar e também o nome da língua falada na ilha.",
   "Enciclopédia Britannica – verbete 'Madagascar'")
mc(T, "gentílicos", 4, 16, "Quem nasce na cidade de Belém, no Pará, é chamado de quê?",
   ["Belenense", "Manauara", "Macapaense", "Santareno"], "Belenense",
   "O gentílico de Belém é 'belenense'; manauara é de Manaus, macapaense de Macapá e santareno de Santarém.",
   "IBGE", br=True)
mc(T, "história da língua", 4, 16, "Como se chamava a língua de base tupi, usada por jesuítas e colonos, que foi muito falada no Brasil nos primeiros séculos?",
   ["Língua geral", "Latim vulgar", "Guarani paraguaio", "Crioulo cabo-verdiano"], "Língua geral",
   "A língua geral, baseada no tupi, foi a mais falada em várias regiões do Brasil colonial, e dela descende o nheengatu.",
   "Museu da Língua Portuguesa", br=True)
mc(T, "figuras de linguagem", 4, 16, "Qual figura de linguagem mistura sentidos diferentes, como em 'voz doce' ou 'cor gritante'?",
   ["Sinestesia", "Metonímia", "Pleonasmo", "Eufemismo"], "Sinestesia",
   "Na sinestesia, uma sensação é descrita com palavras de outro sentido, como o paladar para falar da audição.",
   BECH)
mc(T, "masculino e feminino", 4, 16, "Qual é o feminino de 'abade', o superior de um mosteiro?",
   ["Abadessa", "Abadia", "Abada", "Freira"], "Abadessa",
   "A abadessa dirige um mosteiro feminino; 'abadia' é o nome do próprio mosteiro.",
   GRAM)
