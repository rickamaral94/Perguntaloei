# Perguntas novas: música. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "mus"

# ================================================== FÁCEIS
mc(T, "músicas infantis", 1, 6, "Na música 'A Dona Aranha', o que derrubou a aranha quando ela subia pela parede?",
   ["A chuva", "O vento", "O gato", "A vassoura"], "A chuva",
   "A letra diz: 'A Dona Aranha subiu pela parede, veio a chuva forte e a derrubou'. É a versão brasileira da cantiga inglesa 'Itsy Bitsy Spider'.",
   "Cancioneiro infantil tradicional (domínio público)")
mc(T, "músicas infantis", 1, 6, "Na música 'Meu pintinho amarelinho', onde o pintinho cabe?",
   ["Na minha mão", "No meu bolso", "No meu chapéu", "Na caixinha"], "Na minha mão",
   "A canção diz: 'Meu pintinho amarelinho cabe aqui na minha mão'.",
   "Cancioneiro infantil tradicional (domínio público)", br=True)
mc(T, "músicas infantis", 1, 6, "Na música 'Seu Lobato', o que Seu Lobato tinha, cheio de bichos?",
   ["Um sítio", "Um circo", "Um barco", "Um zoológico"], "Um sítio",
   "A canção diz 'Seu Lobato tinha um sítio, ia, ia, ô' e vai apresentando os animais do lugar. É a versão brasileira de 'Old MacDonald Had a Farm'.",
   "Cancioneiro infantil tradicional (domínio público)")
mc(T, "canções famosas", 1, 6, "Na música de aniversário, depois de 'Parabéns a você, nesta data querida', o que se canta?",
   ["Muitas felicidades, muitos anos de vida", "Muitos presentes e doces na mesa",
    "Vamos todos cantar com alegria", "Um bolo bem grande para a festa"],
   "Muitas felicidades, muitos anos de vida",
   "A melodia é a mesma de 'Happy Birthday to You', mas a letra brasileira é própria: foi escrita por Bertha Celeste Homem de Mello e venceu um concurso da Rádio Tupi, em 1942.",
   "Enciclopédia Britannica – verbete 'Happy Birthday to You'; Rádio Tupi", br=True)
op(T, "canções", 1, 6, "Como se chama a música cantada baixinho para fazer o bebê dormir?", "Canção de ninar",
   ["canção de ninar", "cancao de ninar", "cantiga de ninar", "música de ninar", "musica de ninar", "acalanto",
    "cantiga de embalar"],
   "As canções de ninar, como 'Nana, neném', também são chamadas de acalantos.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro")
mc(T, "cantigas de roda", 1, 7, "Na cantiga 'Pai Francisco', o que Pai Francisco vinha tocando ao entrar na roda?",
   ["Violão", "Pandeiro", "Sanfona", "Flauta"], "Violão",
   "Os versos dizem: 'Pai Francisco entrou na roda tocando seu violão'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cantigas de roda", 1, 7, "Na cantiga 'Alecrim dourado', onde o alecrim nasceu sem ser semeado?",
   ["No campo", "No jardim", "Na horta", "No quintal"], "No campo",
   "A cantiga diz: 'Alecrim, alecrim dourado, que nasceu no campo sem ser semeado'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cantigas de roda", 1, 7, "Na cantiga 'Ciranda, cirandinha', o anel que tu me deste era de quê?",
   ["Vidro", "Ouro", "Prata", "Lata"], "Vidro",
   "Os versos dizem: 'O anel que tu me deste era vidro e se quebrou'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "cantigas de roda", 1, 7, "Na cantiga 'A barata diz que tem', a barata diz que tem sete saias de quê?",
   ["Filó", "Seda", "Renda", "Chita"], "Filó",
   "A brincadeira da letra é que a barata diz que tem sete saias de filó, mas 'tem é uma só'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "instrumentos", 1, 7, "Qual destes é um instrumento de percussão, tocado com baquetas?",
   ["Xilofone", "Clarinete", "Trompete", "Violino"], "Xilofone",
   "O xilofone tem plaquinhas de madeira de tamanhos diferentes, e cada uma dá uma nota quando recebe a batida.",
   "Enciclopédia Britannica – verbete 'Xylophone'")
mc(T, "instrumentos", 1, 7, "Qual instrumento de cordas costuma ser ligado a um amplificador e é a estrela das bandas de rock?",
   ["Guitarra", "Harpa", "Violoncelo", "Violino"], "Guitarra",
   "A guitarra elétrica capta a vibração das cordas e manda o som para o amplificador.",
   "Enciclopédia Britannica – verbete 'Electric guitar'")
op(T, "notas musicais", 1, 7, "Na sequência dó, ré, mi, fá, sol, lá, qual nota vem em seguida?", "Si", ["si"],
   "Depois do si, a escala recomeça no dó, só que mais agudo.",
   "Enciclopédia Britannica – verbete 'Solmization'")
tf(T, "instrumentos", 1, 7, "O trompete é um instrumento de cordas.", False,
   "O trompete é um instrumento de sopro da família dos metais; o som nasce da vibração dos lábios no bocal.",
   "Enciclopédia Britannica – verbete 'Trumpet'")
tf(T, "conceitos musicais", 1, 7, "Um som agudo é um som 'fininho', como o piado de um passarinho.", True,
   "Sons agudos têm frequência alta; os graves, como o de um trovão, são 'grossos'.",
   "Enciclopédia Britannica – verbete 'Pitch'")
mc(T, "instrumentos brasileiros", 1, 8, "Qual instrumento do samba tem uma varinha presa dentro e solta um som parecido com um ronco?",
   ["Cuíca", "Agogô", "Ganzá", "Caixa"], "Cuíca",
   "O músico esfrega a varinha com um pano úmido, e a pele do instrumento faz o som de 'ronco' ou 'gemido'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "instrumentos", 1, 8, "Qual instrumento faz barulho quando a gente raspa uma varinha nos seus risquinhos?",
   ["Reco-reco", "Pandeiro", "Chocalho", "Tamborim"], "Reco-reco",
   "O reco-reco tem ranhuras, e o som surge ao raspar uma vareta sobre elas.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "conceitos musicais", 1, 8, "Como se chamam as palavras que a gente canta numa música?", "Letra",
   ["letra", "a letra", "letra da música", "letra da musica"],
   "Quem escreve a letra é o letrista; quem cria a melodia é o compositor, e às vezes é a mesma pessoa.",
   "Enciclopédia Britannica – verbete 'Lyric'")
mc(T, "instrumentos", 1, 9, "Qual flauta, muitas vezes de plástico, é a mais usada para aprender música na escola?",
   ["Flauta doce", "Flauta transversal", "Flauta de Pã", "Ocarina"], "Flauta doce",
   "A flauta doce é tocada na vertical e é barata e simples de aprender.",
   "Enciclopédia Britannica – verbete 'Recorder'")
op(T, "conceitos musicais", 1, 9, "Como se chama a parte de uma canção que se repete várias vezes e todo mundo canta junto?",
   "Refrão", ["refrão", "refrao", "estribilho", "o refrão"],
   "O refrão costuma ser a parte mais fácil de lembrar de uma música.",
   "Enciclopédia Britannica – verbete 'Refrain'")
tf(T, "carnaval", 1, 9, "O samba-enredo é a música que a escola de samba canta no desfile para contar o seu tema.", True,
   "Cada escola escolhe um enredo, e o samba-enredo conta essa história durante o desfile.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "música internacional", 1, 9, "Qual cantor ficou famoso pelo passo 'moonwalk', em que parece deslizar para trás?",
   ["Michael Jackson", "Elvis Presley", "Bruno Mars", "Justin Bieber"], "Michael Jackson",
   "Ele apresentou o passo na TV em 1983, cantando 'Billie Jean'.",
   "Enciclopédia Britannica – verbete 'Michael Jackson'")
mc(T, "música infantil", 1, 9, "Qual cantora e apresentadora gravou 'Lua de Cristal' e 'Ilariê'?",
   ["Xuxa", "Eliana", "Angélica", "Mara Maravilha"], "Xuxa",
   "'Ilariê' foi lançada em 1988, e 'Lua de Cristal' foi tema do filme de mesmo nome, de 1990.",
   "Memória Globo", br=True)
mc(T, "festivais", 1, 10, "Qual festival de música começou no Rio de Janeiro em 1985 e depois ganhou edições em Lisboa e Las Vegas?",
   ["Rock in Rio", "Lollapalooza", "Woodstock", "Coachella"], "Rock in Rio",
   "A primeira edição, em janeiro de 1985, reuniu bandas como Queen e Iron Maiden.",
   "Memória Globo", br=True)
op(T, "gêneros", 1, 10, "O que quer dizer a sigla MPB?", "Música Popular Brasileira",
   ["música popular brasileira", "musica popular brasileira"],
   "O nome se firmou nos anos 1960 para a música de artistas como Chico Buarque, Elis Regina e Milton Nascimento.",
   "Enciclopédia Itaú Cultural – verbete 'MPB'", br=True)
tf(T, "música internacional", 1, 10, "Os Beatles eram uma banda dos Estados Unidos.", False,
   "Os Beatles eram ingleses, de Liverpool, e fizeram sucesso no mundo todo nos anos 1960.",
   "Enciclopédia Britannica – verbete 'the Beatles'")
tf(T, "música erudita", 1, 10, "Mozart começou a compor música quando ainda era criança.", True,
   "Wolfgang Amadeus Mozart escreveu suas primeiras peças por volta dos 5 anos de idade.",
   "Enciclopédia Britannica – verbete 'Wolfgang Amadeus Mozart'")
mc(T, "música infantil", 1, 10, "Qual dupla de música infantil, formada por Sandra Peres e Paulo Tatit, gravou a canção 'Sopa'?",
   ["Palavra Cantada", "Patati Patatá", "Trem da Alegria", "Turma do Balão Mágico"], "Palavra Cantada",
   "Na canção, a pergunta é 'o que é que tem na sopa do neném?', e a resposta vira uma lista de ingredientes.",
   "Palavra Cantada – site oficial", br=True)

# ================================================== MÉDIAS
mc(T, "instrumentos brasileiros", 2, 10, "Qual tambor do forró é tocado com uma baqueta grossa de um lado e uma varinha fina do outro?",
   ["Zabumba", "Atabaque", "Tamborim", "Cuíca"], "Zabumba",
   "Com a sanfona e o triângulo, a zabumba forma o trio clássico do forró.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
op(T, "instrumentos", 2, 10, "Quantas cordas tem um violino?", "4", ["4", "quatro"],
   "As quatro cordas do violino são afinadas nas notas sol, ré, lá e mi.",
   "Enciclopédia Britannica – verbete 'Violin'")
mc(T, "teoria musical", 2, 10, "Como se chama o sinal da partitura que indica um momento de silêncio?",
   ["Pausa", "Clave", "Bemol", "Sustenido"], "Pausa",
   "Cada pausa tem uma figura que diz por quanto tempo o músico fica em silêncio.",
   "Enciclopédia Britannica – verbete 'Rest'")
mc(T, "teoria musical", 2, 12, "Como se chama o conjunto de três ou mais notas tocadas ao mesmo tempo?",
   ["Acorde", "Escala", "Melodia", "Ritmo"], "Acorde",
   "No violão, por exemplo, a mão esquerda forma os acordes enquanto a direita toca as cordas.",
   "Enciclopédia Britannica – verbete 'Chord'")
mc(T, "teoria musical", 2, 12, "Qual aparelho faz um 'tique-taque' regular para ajudar o músico a manter a velocidade da música?",
   ["Metrônomo", "Diapasão", "Afinador", "Amplificador"], "Metrônomo",
   "O metrônomo pode ser ajustado para bater mais rápido ou mais devagar, conforme o andamento.",
   "Enciclopédia Britannica – verbete 'Metronome'")
tf(T, "instrumentos", 2, 12, "Entre os instrumentos de cordas tocados com arco na orquestra, o contrabaixo é o mais agudo.", False,
   "É o contrário: o contrabaixo é o maior e o mais grave desse grupo; o violino é o mais agudo.",
   "Enciclopédia Britannica – verbete 'Double bass'")
tf(T, "instrumentos", 2, 12, "O ukulele, pequeno instrumento de quatro cordas, surgiu no Japão.", False,
   "O ukulele surgiu no Havaí, a partir de um instrumento levado por imigrantes da Ilha da Madeira, parente do cavaquinho.",
   "Enciclopédia Britannica – verbete 'Ukulele'")
mc(T, "instrumentos brasileiros", 2, 12, "Qual instrumento de percussão tem duas campânulas de metal e é tocado com uma baqueta?",
   ["Agogô", "Ganzá", "Caxixi", "Pandeiro"], "Agogô",
   "O agogô veio da África e aparece no samba, no maracatu e na capoeira.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "instrumentos brasileiros", 2, 12, "Qual instrumento de dez cordas, arrumadas em cinco pares, é a marca da música caipira de raiz?",
   ["Viola caipira", "Cavaquinho", "Bandolim", "Violino"], "Viola caipira",
   "A viola caipira acompanha modas de viola, catiras e Folias de Reis no interior do Brasil.",
   "Enciclopédia Itaú Cultural – verbete 'Viola caipira'", br=True)
mc(T, "artistas brasileiros", 2, 12, "Qual compositor brasileiro dá nome ao aeroporto internacional do Galeão, no Rio de Janeiro?",
   ["Tom Jobim", "Vinicius de Moraes", "Pixinguinha", "Cartola"], "Tom Jobim",
   "O aeroporto se chama oficialmente Aeroporto Internacional do Rio de Janeiro/Galeão – Antonio Carlos Jobim.",
   "Lei nº 9.778/1999", br=True)
op(T, "música internacional", 2, 12, "De qual cidade inglesa eram os Beatles?", "Liverpool", ["liverpool"],
   "Liverpool é uma cidade portuária no noroeste da Inglaterra, onde a banda tocava no Cavern Club.",
   "Enciclopédia Britannica – verbete 'the Beatles'")
tf(T, "música internacional", 2, 12, "O grupo ABBA, de 'Dancing Queen' e 'Mamma Mia', era da Suécia.", True,
   "O ABBA ficou famoso no mundo todo ao vencer o concurso Eurovisão de 1974 com 'Waterloo'.",
   "Enciclopédia Britannica – verbete 'ABBA'")
tf(T, "música erudita", 2, 12, "A peça para piano 'Para Elisa' foi composta por Mozart.", False,
   "'Para Elisa' é de Ludwig van Beethoven e só foi publicada décadas depois da morte dele.",
   "Enciclopédia Britannica – verbete 'Für Elise'")
mc(T, "artistas brasileiros", 2, 14, "Qual música de Tom Jobim diz 'É pau, é pedra, é o fim do caminho'?",
   ["Águas de Março", "Wave", "Corcovado", "Chega de Saudade"], "Águas de Março",
   "Lançada em 1972, ficou ainda mais famosa no dueto de Tom Jobim com Elis Regina, em 1974.",
   "Instituto Antonio Carlos Jobim", br=True)
mc(T, "movimentos musicais", 2, 14, "Como se chamou o movimento dos anos 1960 liderado por Roberto Carlos, Erasmo Carlos e Wanderléa?",
   ["Jovem Guarda", "Tropicália", "Bossa Nova", "Clube da Esquina"], "Jovem Guarda",
   "O nome veio do programa de TV 'Jovem Guarda', da TV Record, que estreou em 1965.",
   "Enciclopédia Itaú Cultural – verbete 'Jovem Guarda'", br=True)
mc(T, "artistas brasileiros", 2, 14, "Qual cantor e compositor gravou 'Exagerado' e 'O Tempo Não Para'?",
   ["Cazuza", "Renato Russo", "Lobão", "Frejat"], "Cazuza",
   "Depois de sair do Barão Vermelho, Cazuza fez sucesso na carreira solo até morrer, em 1990.",
   "Enciclopédia Itaú Cultural – verbete 'Cazuza'", br=True)
mc(T, "artistas brasileiros", 2, 14, "Qual cantora formou o trio Tribalistas com Arnaldo Antunes e Carlinhos Brown?",
   ["Marisa Monte", "Ivete Sangalo", "Daniela Mercury", "Adriana Calcanhotto"], "Marisa Monte",
   "O primeiro disco dos Tribalistas, de 2002, trouxe o sucesso 'Já Sei Namorar'.",
   "Enciclopédia Itaú Cultural – verbete 'Marisa Monte'", br=True)
mc(T, "artistas brasileiros", 2, 14, "Qual cantor baiano, um dos pioneiros do rock no Brasil, gravou 'Maluco Beleza' e 'Metamorfose Ambulante'?",
   ["Raul Seixas", "Erasmo Carlos", "Lulu Santos", "Ney Matogrosso"], "Raul Seixas",
   "Raul Seixas nasceu em Salvador e é lembrado até hoje pelo grito 'Toca Raul!' nos shows.",
   "Enciclopédia Itaú Cultural – verbete 'Raul Seixas'", br=True)
tf(T, "artistas brasileiros", 2, 14, "Gonzaguinha, autor de 'O Que É, O Que É?', era filho de Luiz Gonzaga.", True,
   "Luiz Gonzaga Júnior, o Gonzaguinha, seguiu um caminho diferente do pai, mais ligado à MPB.",
   "Enciclopédia Itaú Cultural – verbete 'Gonzaguinha'", br=True)
mc(T, "artistas brasileiros", 2, 14, "Qual sambista carioca gravou o sucesso 'Deixa a Vida Me Levar', em 2002?",
   ["Zeca Pagodinho", "Arlindo Cruz", "Martinho da Vila", "Jorge Aragão"], "Zeca Pagodinho",
   "A canção, de Serginho Meriti e Eri do Cais, virou uma das marcas de Zeca Pagodinho.",
   "Enciclopédia Itaú Cultural – verbete 'Zeca Pagodinho'", br=True)
tf(T, "vozes", 2, 14, "Soprano é o nome da voz feminina mais aguda.", True,
   "As vozes femininas vão do soprano, a mais aguda, ao contralto, a mais grave.",
   "Enciclopédia Britannica – verbete 'Soprano'")
mc(T, "gêneros", 2, 14, "Qual gênero musical afro-americano, de letras melancólicas, nasceu no sul dos Estados Unidos e tem B.B. King como grande nome?",
   ["Blues", "Reggae", "Country", "Tango"], "Blues",
   "O blues surgiu no fim do século 19 e influenciou o jazz, o rock e muitos outros gêneros.",
   "Enciclopédia Britannica – verbete 'Blues'")
mc(T, "artistas brasileiros", 2, 14, "Qual poeta e compositor, parceiro de Tom Jobim, era chamado carinhosamente de 'Poetinha'?",
   ["Vinicius de Moraes", "Carlos Drummond de Andrade", "Cartola", "Noel Rosa"], "Vinicius de Moraes",
   "Vinicius escreveu letras como 'Chega de Saudade' e 'A Felicidade' e também foi diplomata.",
   "Enciclopédia Itaú Cultural – verbete 'Vinicius de Moraes'", br=True)

# ================================================== DIFÍCEIS
mc(T, "instrumentos brasileiros", 3, 14, "Qual instrumento popular do Nordeste, parente rústico do violino, é tocado com arco nas festas e no cavalo-marinho?",
   ["Rabeca", "Cavaquinho", "Bandolim", "Viola caipira"], "Rabeca",
   "A rabeca costuma ser feita à mão por artesãos, e cada uma tem um som um pouco diferente.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(T, "instrumentos", 3, 14, "Qual instrumento de sopro, geralmente de madeira escura, tem uma palheta simples presa ao bocal?",
   ["Clarinete", "Trompete", "Trombone", "Tuba"], "Clarinete",
   "A palheta vibra contra o bocal e produz o som; trompete, trombone e tuba usam a vibração dos lábios.",
   "Enciclopédia Britannica – verbete 'Clarinet'")
mc(T, "instrumentos", 3, 14, "Qual grande tambor da orquestra, em forma de bacia de cobre, pode ser afinado em notas diferentes?",
   ["Tímpano", "Surdo", "Bumbo", "Caixa"], "Tímpano",
   "O timpanista muda a afinação com pedais que esticam ou afrouxam a pele.",
   "Enciclopédia Britannica – verbete 'Timpani'")
mc(T, "teoria musical", 3, 14, "Qual objeto de metal em forma de garfo vibra sempre na mesma nota e serve para afinar instrumentos?",
   ["Diapasão", "Metrônomo", "Batuta", "Partitura"], "Diapasão",
   "O diapasão mais comum dá a nota lá, usada como referência pelas orquestras.",
   "Enciclopédia Britannica – verbete 'Tuning fork'")
mc(T, "artistas brasileiros", 3, 16, "Qual cantora baiana, uma das vozes da Tropicália, gravou 'Baby' e 'Divino, Maravilhoso'?",
   ["Gal Costa", "Maria Bethânia", "Nara Leão", "Elza Soares"], "Gal Costa",
   "'Divino, Maravilhoso', de Caetano Veloso e Gilberto Gil, foi apresentada por ela num festival de 1968.",
   "Enciclopédia Itaú Cultural – verbete 'Gal Costa'", br=True)
mc(T, "gêneros", 3, 16, "Qual canção, gravada por João Gilberto em 1958, é considerada o marco inicial da bossa nova?",
   ["Chega de Saudade", "Garota de Ipanema", "Wave", "Águas de Março"], "Chega de Saudade",
   "A música é de Tom Jobim e Vinicius de Moraes, e a batida do violão de João Gilberto marcou época.",
   "Enciclopédia Itaú Cultural – verbete 'Bossa nova'", br=True)
mc(T, "artistas brasileiros", 3, 16, "Antes da carreira solo, Rita Lee fez parte de qual banda, com os irmãos Arnaldo e Sérgio Dias Baptista?",
   ["Os Mutantes", "Secos & Molhados", "Novos Baianos", "Titãs"], "Os Mutantes",
   "Os Mutantes acompanharam Gilberto Gil em 'Domingo no Parque', no festival da Record de 1967.",
   "Enciclopédia Itaú Cultural – verbete 'Os Mutantes'", br=True)
mc(T, "música internacional", 3, 16, "Qual guitarrista canhoto tocou uma versão marcante do hino dos Estados Unidos no festival de Woodstock, em 1969?",
   ["Jimi Hendrix", "Eric Clapton", "Chuck Berry", "Jimmy Page"], "Jimi Hendrix",
   "Hendrix tocava uma guitarra de destro virada de cabeça para baixo, com as cordas invertidas.",
   "Enciclopédia Britannica – verbete 'Jimi Hendrix'")
mc(T, "música erudita", 3, 16, "Qual compositor nascido na Alemanha, que viveu em Londres, escreveu 'O Messias', com o famoso coro 'Aleluia'?",
   ["Georg Friedrich Händel", "Johann Sebastian Bach", "Joseph Haydn", "Wolfgang Amadeus Mozart"],
   "Georg Friedrich Händel",
   "O oratório estreou em Dublin, em 1742, e até hoje é cantado em muitos países no Natal.",
   "Enciclopédia Britannica – verbete 'Messiah'", syn=("handel", "händel", "haendel"))
tf(T, "artistas brasileiros", 3, 16, "Luiz Gonzaga nasceu em Exu, no sertão de Pernambuco.", True,
   "O Rei do Baião nasceu em 1912 em Exu, e lá hoje funciona um museu dedicado a ele.",
   "Enciclopédia Itaú Cultural – verbete 'Luiz Gonzaga'", br=True)
tf(T, "artistas brasileiros", 3, 16, "A cantora Elis Regina era baiana.", False,
   "Elis Regina nasceu em Porto Alegre, no Rio Grande do Sul, em 1945.",
   "Enciclopédia Itaú Cultural – verbete 'Elis Regina'", br=True)
mc(T, "instrumentos brasileiros", 3, 16, "Qual instrumento de oito cordas, em quatro pares, deu apelido a Jacob, um dos mestres do choro?",
   ["Bandolim", "Cavaquinho", "Violão", "Viola caipira"], "Bandolim",
   "Jacob do Bandolim compôs choros como 'Doce de Coco' e 'Noites Cariocas'.",
   "Enciclopédia Itaú Cultural – verbete 'Jacob do Bandolim'", br=True)

# ================================================== MUITO DIFÍCEIS
mc(T, "samba", 4, 16, "Qual canção, registrada por Donga em 1916, é considerada o primeiro samba gravado?",
   ["Pelo Telefone", "Aquarela do Brasil", "Com Que Roupa?", "Carinhoso"], "Pelo Telefone",
   "Registrada em nome de Donga e Mauro de Almeida, a música nasceu nas rodas da casa de Tia Ciata; a gravação saiu em 1917 e ajudou a espalhar o nome 'samba' pelo país.",
   "Enciclopédia Itaú Cultural – verbete 'Donga'", br=True)
mc(T, "festivais", 4, 16, "Qual canção de Chico Buarque dividiu o primeiro lugar do festival da TV Record de 1966 com 'Disparada'?",
   ["A Banda", "Construção", "Roda Viva", "Apesar de Você"], "A Banda",
   "'A Banda' foi cantada por Chico e Nara Leão, e 'Disparada', de Geraldo Vandré e Théo de Barros, por Jair Rodrigues.",
   "Enciclopédia Itaú Cultural – verbete 'Festivais de MPB'", br=True)
mc(T, "hinos", 4, 16, "Qual poeta escreveu a letra do Hino à Bandeira Nacional?",
   ["Olavo Bilac", "Joaquim Osório Duque Estrada", "Castro Alves", "Machado de Assis"], "Olavo Bilac",
   "A música do hino, que começa com 'Salve, lindo pendão da esperança', é de Francisco Braga.",
   "Presidência da República – Símbolos Nacionais", br=True)
tf(T, "instrumentos", 4, 16, "O saxofone tem esse nome por causa do seu inventor, o belga Adolphe Sax.", True,
   "Adolphe Sax patenteou o instrumento em Paris, em 1846.",
   "Enciclopédia Britannica – verbete 'Saxophone'")
mc(T, "artistas brasileiros", 4, 16, "Qual músico alagoano, apelidado de 'Bruxo', ficou famoso por tirar música de chaleiras e até de sons de bichos?",
   ["Hermeto Pascoal", "Egberto Gismonti", "Sivuca", "Dominguinhos"], "Hermeto Pascoal",
   "Hermeto tocava dezenas de instrumentos e transformava objetos do dia a dia em instrumentos musicais.",
   "Enciclopédia Itaú Cultural – verbete 'Hermeto Pascoal'", br=True)
mc(T, "música erudita", 4, 16, "Qual compositor alemão criou, em 1868, a 'Canção de Ninar' mais famosa da música erudita?",
   ["Johannes Brahms", "Richard Wagner", "Felix Mendelssohn", "Gustav Mahler"], "Johannes Brahms",
   "A 'Wiegenlied' de Brahms é tocada até hoje em caixinhas de música e brinquedos de bebê.",
   "Enciclopédia Britannica – verbete 'Johannes Brahms'")
