# Perguntas: Música, Literatura, Natureza, Cultura brasileira, Curiosidades.
from qdsl import mc, op, tf

# =========================================================== MÚSICA
S = "mus"
mc(S, "instrumentos", 1, 6, "Qual instrumento tem teclas brancas e pretas?",
   ["Piano", "Violão", "Tambor", "Flauta"], "Piano",
   "Um piano comum tem 88 teclas: 52 brancas e 36 pretas.",
   "Enciclopédia Britannica – verbete 'piano'")
mc(S, "instrumentos", 1, 6, "Qual instrumento a gente toca batendo com baquetas?",
   ["Bateria", "Violino", "Flauta", "Harpa"], "Bateria",
   "A bateria é um conjunto de tambores e pratos tocados com baquetas.",
   "Enciclopédia Britannica – verbete 'drum kit'")
mc(S, "instrumentos", 1, 6, "Qual destes é um instrumento de sopro?",
   ["Flauta", "Bateria", "Violino", "Piano"], "Flauta",
   "Nos instrumentos de sopro, o som nasce do ar soprado pelo músico.",
   "Enciclopédia Britannica – verbete 'wind instrument'")
mc(S, "teoria musical", 1, 6, "Quantas notas tem a escala tradicional dó, ré, mi, fá, sol, lá, si?",
   ["7", "5", "8", "12"], "7",
   "São 7 notas naturais; com os sustenidos e bemóis, a escala cromática tem 12 sons.",
   "Bohumil Med – Teoria da Música")
mc(S, "ritmos brasileiros", 1, 8, "Qual ritmo brasileiro é o principal dos desfiles de Carnaval no Sambódromo do Rio?",
   ["Samba", "Frevo", "Forró", "Funk"], "Samba",
   "Cada escola desfila com um samba-enredo e sua bateria.",
   "IPHAN – Matrizes do Samba no Rio de Janeiro", br=True)
mc(S, "instrumentos", 1, 9, "Quantas cordas tem um violão comum?",
   ["6", "4", "5", "12"], "6",
   "O violão de 7 cordas também é muito usado no choro e no samba.",
   "Enciclopédia Britannica – verbete 'guitar'")
mc(S, "rock", 1, 10, "Qual banda britânica era formada por John, Paul, George e Ringo?",
   ["The Beatles", "Rolling Stones", "Queen", "The Who"], "The Beatles",
   "Os Beatles surgiram em Liverpool, na Inglaterra, nos anos 1960.",
   "Enciclopédia Britannica – verbete 'the Beatles'", syn=["beatles", "os beatles"])
mc(S, "MPB", 1, 10, "Qual cantor brasileiro, chamado de 'Rei', gravou 'Detalhes' e 'Emoções'?",
   ["Roberto Carlos", "Erasmo Carlos", "Caetano Veloso", "Tim Maia"], "Roberto Carlos",
   "Roberto Carlos foi um dos líderes da Jovem Guarda nos anos 1960.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["roberto"], br=True)
mc(S, "rock", 1, 10, "Qual cantor norte-americano dos anos 1950 ganhou o apelido de 'Rei do Rock'?",
   ["Elvis Presley", "Chuck Berry", "Little Richard", "Buddy Holly"], "Elvis Presley",
   "Elvis morava em Graceland, em Memphis, que hoje é um museu.",
   "Enciclopédia Britannica – verbete 'Elvis Presley'", syn=["elvis"])
mc(S, "pop", 1, 10, "Quem lançou o álbum 'Thriller', o mais vendido de todos os tempos?",
   ["Michael Jackson", "Prince", "Madonna", "Whitney Houston"], "Michael Jackson",
   "Thriller (1982) é reconhecido pelo Guinness como o álbum mais vendido da história.",
   "Guinness World Records – Best-selling album", syn=["michael"], ref="Guinness World Records, 2025")
mc(S, "MPB", 2, 12, "Qual gênero musical surgiu no fim dos anos 1950 com João Gilberto e Tom Jobim?",
   ["Bossa nova", "Samba-enredo", "Axé", "Sertanejo"], "Bossa nova",
   "O disco 'Chega de Saudade' (1959), de João Gilberto, é o marco da bossa nova.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["bossa"], br=True)
mc(S, "clássica", 2, 12, "Qual compositor alemão continuou compondo mesmo depois de ficar surdo?",
   ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frédéric Chopin"], "Ludwig van Beethoven",
   "Beethoven compôs a 9ª Sinfonia quando já estava praticamente surdo.",
   "Beethoven-Haus Bonn", syn=["beethoven"])
mc(S, "ritmos brasileiros", 2, 12, "Qual estado brasileiro é o berço do frevo?",
   ["Pernambuco", "Bahia", "Ceará", "Maranhão"], "Pernambuco",
   "O frevo nasceu no Recife e é Patrimônio Imaterial da Humanidade (UNESCO, 2012).",
   "UNESCO – Frevo, performing arts of the Carnival of Recife (2012)", br=True)
mc(S, "rock", 2, 12, "Qual banda britânica gravou 'Bohemian Rhapsody'?",
   ["Queen", "The Beatles", "Pink Floyd", "Led Zeppelin"], "Queen",
   "A música de Freddie Mercury foi lançada em 1975.",
   "Queen – site oficial")
mc(S, "MPB", 2, 14, "Qual música de Tom Jobim e Vinicius de Moraes fala de uma moça 'num doce balanço, a caminho do mar'?",
   ["Garota de Ipanema", "Águas de Março", "Chega de Saudade", "Wave"], "Garota de Ipanema",
   "Composta em 1962, é uma das canções mais gravadas do mundo.",
   "Instituto Antonio Carlos Jobim", br=True)
mc(S, "rock", 2, 14, "Qual cantora ficou conhecida como a 'Rainha do Rock brasileiro'?",
   ["Rita Lee", "Pitty", "Elis Regina", "Cássia Eller"], "Rita Lee",
   "Rita Lee começou nos Mutantes e fez sucesso solo com 'Lança Perfume' e 'Ovelha Negra'.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)
mc(S, "forró", 2, 14, "Quem gravou 'Asa Branca' e ficou conhecido como o Rei do Baião?",
   ["Luiz Gonzaga", "Dominguinhos", "Jackson do Pandeiro", "Gilberto Gil"], "Luiz Gonzaga",
   "'Asa Branca' (1947) é de Luiz Gonzaga e Humberto Teixeira.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["gonzagao", "gonzaga"], br=True)
mc(S, "sertanejo", 2, 14, "Qual dupla sertaneja lançou o sucesso 'É o Amor', em 1991?",
   ["Zezé Di Camargo & Luciano", "Chitãozinho & Xororó", "Leandro & Leonardo", "Bruno & Marrone"], "Zezé Di Camargo & Luciano",
   "A música foi composta por Zezé Di Camargo e estava no primeiro disco da dupla.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["zeze di camargo e luciano", "zeze e luciano", "zeze di camargo"], br=True)
mc(S, "clássica", 3, 14, "Qual compositor austríaco escreveu a ópera 'A Flauta Mágica'?",
   ["Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Joseph Haydn", "Franz Schubert"], "Wolfgang Amadeus Mozart",
   "A ópera estreou em Viena em 1791, poucos meses antes da morte de Mozart.",
   "Mozarteum Salzburg", syn=["mozart"])
mc(S, "samba", 3, 14, "Qual instrumento de percussão do samba é pequeno, redondo e tocado com uma baqueta fina?",
   ["Tamborim", "Tuba", "Harpa", "Gaita"], "Tamborim",
   "O tamborim dá o som agudo e marcado da bateria das escolas de samba.",
   "IPHAN – Matrizes do Samba no Rio de Janeiro", br=True)
mc(S, "MPB", 3, 16, "Qual cantora, apelidada de 'Pimentinha', gravou 'Como Nossos Pais'?",
   ["Elis Regina", "Gal Costa", "Maria Bethânia", "Nara Leão"], "Elis Regina",
   "A canção é de Belchior; a gravação de Elis é de 1976.",
   "Dicionário Cravo Albin da Música Popular Brasileira", syn=["elis"], br=True)
mc(S, "samba", 4, 16, "Quem compôs 'Aquarela do Brasil' (1939)?",
   ["Ary Barroso", "Noel Rosa", "Cartola", "Pixinguinha"], "Ary Barroso",
   "A canção ficou famosa no mundo todo como 'Brazil' e é um marco do samba-exaltação.",
   "Dicionário Cravo Albin da Música Popular Brasileira", br=True)

# =========================================================== LITERATURA
L = "lit"
mc(L, "contos de fadas", 1, 6, "Na história da Chapeuzinho Vermelho, quem se disfarça de vovó para enganar a menina?",
   ["O Lobo Mau", "O Caçador", "O Gato", "O Urso"], "O Lobo Mau",
   "Na versão dos Irmãos Grimm, o caçador salva a menina e a avó.",
   "Irmãos Grimm – Contos de Grimm (1812)", syn=["lobo", "lobo mau"])
mc(L, "contos de fadas", 1, 6, "Em 'Os Três Porquinhos', qual casa o lobo não conseguiu derrubar?",
   ["A de tijolos", "A de palha", "A de madeira", "A de papel"], "A de tijolos",
   "A casa de tijolos era a mais trabalhosa de construir, mas a mais forte.",
   "Joseph Jacobs – English Fairy Tales (1890)", syn=["tijolo", "tijolos", "casa de tijolos"])
mc(L, "clássicos infantis", 1, 6, "Qual menino nunca quer crescer e mora na Terra do Nunca?",
   ["Peter Pan", "Pinóquio", "Aladim", "Mogli"], "Peter Pan",
   "Peter Pan foi criado pelo escritor escocês J. M. Barrie.",
   "J. M. Barrie – Peter Pan (1904/1911)", syn=["peter"])
mc(L, "clássicos infantis", 1, 6, "Qual boneco de madeira tem o nariz que cresce quando ele mente?",
   ["Pinóquio", "Peter Pan", "Aladim", "Gepeto"], "Pinóquio",
   "Pinóquio foi criado pelo italiano Carlo Collodi. Gepeto é o carpinteiro que o fez.",
   "Carlo Collodi – As Aventuras de Pinóquio (1883)", syn=["pinoquio"])
mc(L, "literatura infantil", 1, 9, "Quem escreveu as histórias do 'Sítio do Picapau Amarelo'?",
   ["Monteiro Lobato", "Ziraldo", "Ruth Rocha", "Mauricio de Sousa"], "Monteiro Lobato",
   "O primeiro livro, 'A Menina do Narizinho Arrebitado', é de 1920.",
   "Biblioteca Nacional – Monteiro Lobato", syn=["lobato"], br=True)
op(L, "teatro", 1, 10, "Quem escreveu a peça 'Romeu e Julieta'?",
   "William Shakespeare", ["shakespeare", "xequispir"],
   "A tragédia do dramaturgo inglês é do fim do século XVI.",
   "Folger Shakespeare Library")
mc(L, "fantasia", 1, 10, "Qual escritora criou a saga 'Harry Potter'?",
   ["J. K. Rowling", "Agatha Christie", "Suzanne Collins", "Stephenie Meyer"], "J. K. Rowling",
   "O primeiro livro, 'Harry Potter e a Pedra Filosofal', saiu em 1997.",
   "Bloomsbury Publishing – Harry Potter", syn=["rowling", "jk rowling", "j k rowling"])
mc(L, "romance", 2, 12, "Quem escreveu 'Dom Casmurro'?",
   ["Machado de Assis", "José de Alencar", "Jorge Amado", "Graciliano Ramos"], "Machado de Assis",
   "Machado foi o primeiro presidente da Academia Brasileira de Letras.",
   "Academia Brasileira de Letras – Machado de Assis", syn=["machado"], br=True)
mc(L, "clássicos", 2, 12, "Quem escreveu 'O Pequeno Príncipe'?",
   ["Antoine de Saint-Exupéry", "Júlio Verne", "Victor Hugo", "Albert Camus"], "Antoine de Saint-Exupéry",
   "Saint-Exupéry era aviador, e o livro foi publicado em 1943.",
   "Fondation Antoine de Saint-Exupéry", syn=["saint exupery", "exupery"])
mc(L, "clássicos", 2, 12, "Quem escreveu 'Dom Quixote'?",
   ["Miguel de Cervantes", "William Shakespeare", "Luís de Camões", "Dante Alighieri"], "Miguel de Cervantes",
   "A primeira parte do livro foi publicada em 1605, na Espanha.",
   "Instituto Cervantes", syn=["cervantes"])
mc(L, "romance", 2, 14, "Qual escritor baiano escreveu 'Capitães da Areia' e 'Gabriela, Cravo e Canela'?",
   ["Jorge Amado", "João Ubaldo Ribeiro", "Castro Alves", "Graciliano Ramos"], "Jorge Amado",
   "Os livros de Jorge Amado foram traduzidos para dezenas de idiomas.",
   "Fundação Casa de Jorge Amado", syn=["amado"], br=True)
mc(L, "poesia", 2, 14, "Qual poeta mineiro escreveu 'No meio do caminho tinha uma pedra'?",
   ["Carlos Drummond de Andrade", "Manuel Bandeira", "Vinicius de Moraes", "Cecília Meireles"], "Carlos Drummond de Andrade",
   "O poema 'No Meio do Caminho' foi publicado em 1928 e causou polêmica na época.",
   "Instituto Moreira Salles – Drummond", syn=["drummond", "carlos drummond"], br=True)
mc(L, "poesia", 2, 14, "Qual poeta português escreveu 'Os Lusíadas'?",
   ["Luís de Camões", "Fernando Pessoa", "Eça de Queirós", "Bocage"], "Luís de Camões",
   "O poema épico de 1572 narra a viagem de Vasco da Gama à Índia.",
   "Biblioteca Nacional de Portugal", syn=["camoes"])
mc(L, "policial", 3, 14, "Qual escritor britânico criou o detetive Sherlock Holmes?",
   ["Arthur Conan Doyle", "Agatha Christie", "Charles Dickens", "Edgar Allan Poe"], "Arthur Conan Doyle",
   "Sherlock Holmes apareceu pela primeira vez em 'Um Estudo em Vermelho' (1887).",
   "Arthur Conan Doyle Encyclopedia", syn=["conan doyle", "doyle"])
mc(L, "romantismo", 3, 14, "Qual livro de José de Alencar tem como protagonista a 'virgem dos lábios de mel'?",
   ["Iracema", "O Guarani", "Senhora", "Lucíola"], "Iracema",
   "Iracema (1865) é um anagrama de 'América'.",
   "Academia Brasileira de Letras – José de Alencar", br=True)
mc(L, "realismo", 3, 14, "Em 'Dom Casmurro', qual personagem tem 'olhos de ressaca'?",
   ["Capitu", "Iracema", "Gabriela", "Lucíola"], "Capitu",
   "Até hoje os leitores discutem se Capitu traiu ou não Bentinho.",
   "Machado de Assis – Dom Casmurro (1899)", syn=["capitolina"], br=True)
mc(L, "modernismo", 3, 16, "Qual escritora brasileira escreveu 'A Hora da Estrela'?",
   ["Clarice Lispector", "Cecília Meireles", "Rachel de Queiroz", "Lygia Fagundes Telles"], "Clarice Lispector",
   "O livro de 1977 conta a história da nordestina Macabéa.",
   "Instituto Moreira Salles – Clarice Lispector", syn=["clarice"], br=True)
mc(L, "romantismo", 3, 16, "Qual poeta escreveu 'Canção do Exílio' ('Minha terra tem palmeiras onde canta o sabiá')?",
   ["Gonçalves Dias", "Castro Alves", "Olavo Bilac", "Álvares de Azevedo"], "Gonçalves Dias",
   "O poema foi escrito em 1843, quando o autor estudava em Coimbra.",
   "Academia Brasileira de Letras – Gonçalves Dias", br=True)
mc(L, "clássicos", 4, 14, "Em 'O Pequeno Príncipe', de qual asteroide vem o principezinho?",
   ["B 612", "B 52", "X 9", "K 7"], "B 612",
   "O narrador conta que o asteroide B 612 foi visto uma única vez por um astrônomo turco.",
   "Antoine de Saint-Exupéry – O Pequeno Príncipe (1943)", syn=["b612", "be 612", "b seiscentos e doze"])
mc(L, "modernismo", 4, 16, "Quem escreveu 'Grande Sertão: Veredas'?",
   ["João Guimarães Rosa", "Graciliano Ramos", "Euclides da Cunha", "Rachel de Queiroz"], "João Guimarães Rosa",
   "O romance de 1956 é narrado por Riobaldo, um ex-jagunço.",
   "Academia Brasileira de Letras – Guimarães Rosa", syn=["guimaraes rosa"], br=True)

# =========================================================== NATUREZA
A = "nat"
mc(A, "animais", 1, 6, "Quantas patas tem uma aranha?",
   ["8", "6", "4", "10"], "8",
   "Aranhas são aracnídeos, não insetos: têm 8 patas.",
   "Instituto Butantan – Aranhas")
mc(A, "animais", 1, 6, "Qual animal australiano carrega o filhote numa bolsa na barriga?",
   ["Canguru", "Panda", "Elefante", "Zebra"], "Canguru",
   "O canguru é um marsupial: o filhote se desenvolve dentro da bolsa da mãe.",
   "Australian Museum – Kangaroos")
mc(A, "animais", 1, 6, "Depois de sair do casulo, em qual destes insetos a lagarta se transforma?",
   ["Borboleta", "Abelha", "Joaninha", "Formiga"], "Borboleta",
   "Essa transformação se chama metamorfose. A fase do casulo é a pupa (crisálida).",
   "Museu de Zoologia da USP")
mc(A, "animais", 1, 6, "Quantas patas tem um inseto?",
   ["6", "8", "4", "10"], "6",
   "Todos os insetos adultos têm 6 patas e o corpo dividido em cabeça, tórax e abdome.",
   "Museu de Zoologia da USP")
mc(A, "animais", 1, 6, "Qual destes animais é um mamífero que voa?",
   ["Morcego", "Pinguim", "Galinha", "Avestruz"], "Morcego",
   "O morcego é o único mamífero capaz de voar de verdade, batendo as asas.",
   "Enciclopédia Britannica – verbete 'bat'")
tf(A, "animais", 1, 6, "A baleia é um peixe.", False,
   "A baleia é um mamífero: respira ar pelos pulmões e amamenta os filhotes.",
   "Projeto Baleia Jubarte – Instituto Baleia Jubarte")
mc(A, "animais", 1, 6, "Qual animal muda de cor para se camuflar?",
   ["Camaleão", "Hipopótamo", "Cavalo", "Pato"], "Camaleão",
   "O camaleão muda de cor graças a células especiais da pele.",
   "National Geographic – Chameleons")
mc(A, "planeta", 1, 7, "Qual gás precisamos respirar para viver?",
   ["Oxigênio", "Hélio", "Gás carbônico", "Neônio"], "Oxigênio",
   "O oxigênio é levado pelo sangue a todas as células do corpo.",
   "Ministério da Saúde – Biblioteca Virtual em Saúde", syn=["oxigenio"])
mc(A, "animais", 1, 8, "Qual é o maior animal do planeta?",
   ["Baleia-azul", "Elefante-africano", "Tubarão-baleia", "Girafa"], "Baleia-azul",
   "A baleia-azul pode passar de 30 metros e é o maior animal que já existiu.",
   "NOAA Fisheries – Blue Whale", syn=["baleia azul", "baleia"])
op(A, "fauna brasileira", 1, 8, "Qual é o maior roedor do mundo, comum no Brasil?",
   "Capivara", ["a capivara", "capivaras"],
   "A capivara pode pesar mais de 60 kg e vive perto de rios e lagos.",
   "ICMBio – Fauna brasileira", br=True)
op(A, "flora brasileira", 1, 9, "Qual árvore deu nome ao Brasil?",
   "Pau-brasil", ["pau brasil", "o pau brasil"],
   "A madeira vermelha como brasa era usada para tingir tecidos na Europa.",
   "Jardim Botânico do Rio de Janeiro – Pau-brasil", br=True)
mc(A, "animais", 2, 9, "Qual destes animais costuma hibernar no inverno em regiões frias?",
   ["Urso", "Leão", "Camelo", "Papagaio"], "Urso",
   "Muitos ursos passam o inverno em tocas, num sono profundo, gastando a gordura acumulada.",
   "National Park Service – Bear hibernation")
mc(A, "biomas", 2, 10, "Qual bioma ocupa a maior parte do território brasileiro?",
   ["Amazônia", "Cerrado", "Mata Atlântica", "Caatinga"], "Amazônia",
   "A Amazônia ocupa cerca de 49% do território brasileiro.",
   "IBGE – Biomas e Sistema Costeiro-Marinho do Brasil (2019)", syn=["amazonia", "floresta amazonica"], br=True)
mc(A, "animais", 2, 10, "Qual é o animal terrestre mais rápido do mundo?",
   ["Guepardo", "Leão", "Cavalo", "Antílope"], "Guepardo",
   "O guepardo (ou chita) passa de 100 km/h em corridas curtas.",
   "Smithsonian's National Zoo – Cheetah", syn=["chita"])
mc(A, "fauna brasileira", 2, 10, "Qual é o maior felino das Américas?",
   ["Onça-pintada", "Puma", "Jaguatirica", "Lince"], "Onça-pintada",
   "A onça-pintada vive em vários biomas brasileiros e é ótima nadadora.",
   "ICMBio – Plano de Ação Nacional para a Onça-pintada", syn=["onca", "onca pintada"], br=True)
mc(A, "biomas", 2, 12, "Qual bioma brasileiro, típico do sertão nordestino, tem vegetação adaptada à seca?",
   ["Caatinga", "Pampa", "Mata Atlântica", "Pantanal"], "Caatinga",
   "Caatinga significa 'mata branca' em tupi, pela cor da vegetação na seca.",
   "Ministério do Meio Ambiente – Caatinga", br=True)
mc(A, "biomas", 2, 12, "Qual é a maior planície alagável do mundo, que fica no Brasil, na Bolívia e no Paraguai?",
   ["Pantanal", "Amazônia", "Cerrado", "Chaco"], "Pantanal",
   "O Pantanal é Patrimônio Natural da Humanidade e Reserva da Biosfera pela UNESCO.",
   "Ministério do Meio Ambiente – Pantanal", br=True)
mc(A, "fauna brasileira", 2, 12, "Em qual bioma vive o mico-leão-dourado?",
   ["Mata Atlântica", "Pantanal", "Caatinga", "Pampa"], "Mata Atlântica",
   "O mico-leão-dourado vive só em florestas do estado do Rio de Janeiro.",
   "Associação Mico-Leão-Dourado; ICMBio", br=True)
mc(A, "fauna brasileira", 2, 12, "Qual ave símbolo do Pantanal tem pescoço preto e uma faixa vermelha?",
   ["Tuiuiú", "Tucano", "Ema", "Flamingo"], "Tuiuiú",
   "O tuiuiú pode medir cerca de 1,4 metro de altura.",
   "ICMBio – Fauna do Pantanal", syn=["tuiuiu", "jaburu"], br=True)
mc(A, "comportamento", 2, 12, "Como se chama a viagem que muitas aves fazem conforme a estação do ano?",
   ["Migração", "Hibernação", "Metamorfose", "Polinização"], "Migração",
   "Aves migratórias viajam em busca de comida e clima favorável para se reproduzir.",
   "ICMBio – CEMAVE, Aves migratórias", syn=["migracao"])
mc(A, "flora brasileira", 3, 12, "Qual árvore do Sul do Brasil produz o pinhão?",
   ["Araucária", "Ipê-roxo", "Jequitibá", "Pau-brasil"], "Araucária",
   "A araucária, ou pinheiro-do-paraná, está ameaçada de extinção.",
   "Embrapa Florestas – Araucária", syn=["araucaria", "pinheiro do parana"], br=True)
mc(A, "fauna brasileira", 3, 14, "Qual é a maior ave do Brasil?",
   ["Ema", "Tuiuiú", "Arara-azul", "Gavião-real"], "Ema",
   "A ema não voa, mas corre a até 60 km/h.",
   "ICMBio – Fauna brasileira", br=True)
mc(A, "fauna brasileira", 3, 14, "Em qual bioma brasileiro se concentra a maior parte da população de arara-azul-grande?",
   ["Pantanal", "Pampa", "Mata Atlântica", "Caatinga"], "Pantanal",
   "O Projeto Arara Azul ajudou a espécie a se recuperar no Pantanal.",
   "Instituto Arara Azul", br=True)
mc(A, "fauna brasileira", 4, 14, "Qual peixe gigante da Amazônia respira ar e é chamado de 'bacalhau da Amazônia'?",
   ["Pirarucu", "Tambaqui", "Tucunaré", "Piranha"], "Pirarucu",
   "O pirarucu pode passar de 2 metros e precisa subir à superfície para respirar.",
   "Embrapa – Pirarucu", br=True)

# =========================================================== CULTURA BRASILEIRA
B = "cul"
mc(B, "festas", 1, 6, "Qual festa de junho tem quadrilha, fogueira e comidas de milho?",
   ["Festa Junina", "Carnaval", "Réveillon", "Oktoberfest"], "Festa Junina",
   "As festas juninas homenageiam santos como Santo Antônio, São João e São Pedro.",
   "IPHAN – Festas juninas", syn=["festa de sao joao", "sao joao", "junina"], br=True)
mc(B, "folclore", 1, 6, "Qual personagem do folclore tem uma perna só e usa gorro vermelho?",
   ["Saci-Pererê", "Curupira", "Boitatá", "Mula sem cabeça"], "Saci-Pererê",
   "O Saci adora fazer travessuras e aparece em redemoinhos de vento.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=["saci", "saci perere"], br=True)
mc(B, "símbolos", 1, 6, "Quais são as cores da bandeira do Brasil?",
   ["Verde, amarelo, azul e branco", "Verde, vermelho e branco", "Azul, branco e vermelho", "Amarelo, preto e verde"],
   "Verde, amarelo, azul e branco",
   "A bandeira tem um losango amarelo, um círculo azul com estrelas e a faixa branca.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", syn=["verde amarelo azul branco"], br=True)
mc(B, "culinária", 1, 6, "Qual doce de festa é feito de chocolate e coberto com granulado?",
   ["Brigadeiro", "Beijinho", "Cajuzinho", "Quindim"], "Brigadeiro",
   "O beijinho é de coco e o quindim leva gema de ovo e coco.",
   "Dicionário Houaiss – verbete 'brigadeiro'", br=True)
mc(B, "língua", 1, 6, "Qual é a língua oficial do Brasil?",
   ["Português", "Espanhol", "Inglês", "Francês"], "Português",
   "A Constituição define o português como idioma oficial. A Libras também é reconhecida por lei.",
   "Constituição Federal de 1988, art. 13; Lei nº 10.436/2002", syn=["portugues", "lingua portuguesa"], br=True)
mc(B, "folclore", 1, 7, "Qual personagem do folclore tem os pés virados para trás e protege as florestas?",
   ["Curupira", "Saci-Pererê", "Iara", "Cuca"], "Curupira",
   "Com os pés ao contrário, o Curupira deixa pegadas que confundem os caçadores.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(B, "folclore", 1, 8, "Qual é o nome da sereia do folclore brasileiro que vive nos rios?",
   ["Iara", "Cuca", "Mula sem cabeça", "Boitatá"], "Iara",
   "Iara, a Mãe-d'Água, encanta os pescadores com seu canto.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=["yara", "mae d agua"], br=True)
mc(B, "culinária", 1, 8, "Qual prato típico brasileiro é feito com feijão-preto e carnes de porco?",
   ["Feijoada", "Acarajé", "Moqueca", "Vatapá"], "Feijoada",
   "A feijoada costuma ser servida com arroz, couve, farofa e laranja.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(B, "símbolos", 1, 9, "Qual é o lema escrito na bandeira do Brasil?",
   ["Ordem e Progresso", "Paz e Amor", "Liberdade e Igualdade", "Deus e Pátria"], "Ordem e Progresso",
   "O lema foi inspirado no pensamento do filósofo francês Auguste Comte.",
   "Lei nº 5.700/1971 – Símbolos Nacionais", br=True)
mc(B, "carnaval", 1, 10, "Em que cidade fica o Sambódromo da Marquês de Sapucaí?",
   ["Rio de Janeiro", "Salvador", "São Paulo", "Recife"], "Rio de Janeiro",
   "O Sambódromo, projetado por Oscar Niemeyer, foi inaugurado em 1984.",
   "Prefeitura do Rio de Janeiro – Sambódromo", syn=["rio"], br=True)
mc(B, "monumentos", 1, 10, "Qual monumento do Rio de Janeiro foi eleito, em 2007, uma das Novas Sete Maravilhas do Mundo?",
   ["Cristo Redentor", "Pão de Açúcar", "Arcos da Lapa", "Theatro Municipal"], "Cristo Redentor",
   "A estátua, inaugurada em 1931, fica no alto do morro do Corcovado.",
   "New7Wonders Foundation (2007)", syn=["cristo"], br=True)
mc(B, "culinária", 2, 10, "Qual bolinho baiano é feito de massa de feijão-fradinho frita no azeite de dendê?",
   ["Acarajé", "Coxinha", "Pastel", "Bolinho de chuva"], "Acarajé",
   "O ofício das baianas de acarajé é patrimônio imaterial do Brasil (IPHAN, 2004).",
   "IPHAN – Ofício das Baianas de Acarajé", syn=["acaraje"], br=True)
mc(B, "costumes", 2, 10, "Qual bebida quente, tomada numa cuia com bomba, é tradição no Rio Grande do Sul?",
   ["Chimarrão", "Tereré", "Café", "Chocolate quente"], "Chimarrão",
   "O chimarrão é feito com erva-mate. O tereré é a versão gelada, comum no Mato Grosso do Sul.",
   "Embrapa Florestas – Erva-mate", syn=["chimarrao", "mate"], br=True)
mc(B, "festas", 2, 10, "Qual ritmo nordestino é dançado em pares nas festas de São João, ao som da sanfona?",
   ["Forró", "Tango", "Valsa", "Frevo"], "Forró",
   "As matrizes tradicionais do forró são patrimônio cultural do Brasil (IPHAN, 2021).",
   "IPHAN – Matrizes Tradicionais do Forró", syn=["forro"], br=True)
mc(B, "arquitetura", 2, 14, "Qual arquiteto projetou os principais prédios de Brasília, como o Congresso Nacional?",
   ["Oscar Niemeyer", "Lúcio Costa", "Roberto Burle Marx", "Lina Bo Bardi"], "Oscar Niemeyer",
   "Lúcio Costa fez o plano urbanístico (o Plano Piloto); Niemeyer projetou os edifícios.",
   "Fundação Oscar Niemeyer", syn=["niemeyer"], br=True)
mc(B, "festas", 3, 14, "Em qual cidade do Amazonas acontece a disputa entre os bois Garantido e Caprichoso?",
   ["Parintins", "Manaus", "Belém", "Santarém"], "Parintins",
   "O Festival Folclórico de Parintins acontece no fim de junho, no Bumbódromo.",
   "IPHAN – Complexo Cultural do Boi Bumbá do Médio Amazonas e Parintins", br=True)
mc(B, "artes", 3, 14, "Qual pintora modernista brasileira pintou o quadro 'Abaporu' (1928)?",
   ["Tarsila do Amaral", "Anita Malfatti", "Di Cavalcanti", "Candido Portinari"], "Tarsila do Amaral",
   "O Abaporu inspirou o Movimento Antropofágico e hoje está no MALBA, em Buenos Aires.",
   "Tarsila do Amaral – catálogo raisonné; MALBA", syn=["tarsila"], br=True)
mc(B, "artes", 3, 14, "Em que ano aconteceu a Semana de Arte Moderna, em São Paulo?",
   ["1922", "1930", "1889", "1950"], "1922",
   "A Semana ocupou o Theatro Municipal de São Paulo em fevereiro de 1922.",
   "Theatro Municipal de São Paulo; IEB-USP", br=True)
mc(B, "culinária", 4, 16, "Qual prato paraense leva tucupi, jambu, goma de tapioca e camarão seco?",
   ["Tacacá", "Vatapá", "Baião de dois", "Arroz carreteiro"], "Tacacá",
   "O tacacá é servido bem quente numa cuia; o jambu deixa a boca 'tremendo'.",
   "IPHAN – Patrimônio alimentar do Pará", syn=["tacaca"], br=True)
mc(B, "artes", 4, 16, "Como era conhecido Antônio Francisco Lisboa, artista barroco autor dos profetas de Congonhas (MG)?",
   ["Aleijadinho", "Mestre Valentim", "Mestre Ataíde", "Debret"], "Aleijadinho",
   "Os 12 profetas em pedra-sabão ficam no Santuário de Bom Jesus de Matosinhos, Patrimônio Mundial da UNESCO.",
   "UNESCO – Sanctuary of Bom Jesus do Congonhas", br=True)

# =========================================================== CURIOSIDADES
Q = "cur"
mc(Q, "tempo", 1, 6, "Quantos minutos tem uma hora?",
   ["60", "100", "30", "24"], "60",
   "E cada minuto tem 60 segundos.",
   "Bureau International des Poids et Mesures – Unidades de tempo")
mc(Q, "calendário", 1, 6, "Qual dia da semana vem depois do domingo?",
   ["Segunda-feira", "Sábado", "Terça-feira", "Sexta-feira"], "Segunda-feira",
   "Os nomes 'segunda-feira', 'terça-feira' etc. vêm do latim usado na liturgia cristã.",
   "Dicionário Houaiss – verbete 'segunda-feira'", syn=["segunda"])
mc(Q, "números", 1, 6, "Quantas pessoas formam um trio?",
   ["3", "2", "4", "5"], "3",
   "Dupla tem 2, trio tem 3 e quarteto tem 4.",
   "Dicionário Houaiss – verbete 'trio'")
mc(Q, "natureza", 1, 6, "Quantas cores tem o arco-íris na divisão tradicional?",
   ["7", "5", "6", "9"], "7",
   "Vermelho, laranja, amarelo, verde, azul, anil e violeta: divisão popularizada por Isaac Newton.",
   "Enciclopédia Britannica – verbete 'rainbow'")
mc(Q, "matemática", 1, 8, "Quanto é 7 vezes 8?",
   ["56", "54", "64", "48"], "56",
   "Dica: 5, 6, 7, 8 → 56 = 7 × 8.",
   "Tabuada")
mc(Q, "animais", 1, 8, "Qual animal guarda gordura na corcova e aguenta muitos dias sem beber água?",
   ["Camelo", "Cavalo", "Girafa", "Leão"], "Camelo",
   "A corcova guarda gordura, não água, e serve de reserva de energia.",
   "San Diego Zoo – Camel")
mc(Q, "calendário", 1, 9, "Quantos dias tem um ano bissexto?",
   ["366", "365", "364", "360"], "366",
   "No ano bissexto, fevereiro ganha o dia 29.",
   "Observatório Nacional – Calendário")
mc(Q, "geometria", 1, 9, "Quantos lados tem um hexágono?",
   ["6", "5", "8", "7"], "6",
   "Os favos das colmeias têm formato de hexágono.",
   "Dicionário Houaiss – verbete 'hexágono'")
mc(Q, "tempo", 1, 9, "Quantos anos tem um século?",
   ["100", "10", "1000", "50"], "100",
   "Uma década tem 10 anos e um milênio tem 1.000 anos.",
   "Dicionário Houaiss – verbete 'século'")
mc(Q, "números", 2, 9, "Quantos zeros tem o número um milhão?",
   ["6", "5", "7", "9"], "6",
   "Um milhão se escreve 1.000.000.",
   "Sistema de numeração decimal")
mc(Q, "objetos", 2, 9, "O que pesa mais: um quilo de algodão ou um quilo de ferro?",
   ["Os dois pesam o mesmo", "O ferro", "O algodão"], "Os dois pesam o mesmo",
   "Um quilo é um quilo! O algodão só ocupa mais espaço.",
   "Inmetro – Sistema Internacional de Unidades",
   syn=["o mesmo", "iguais", "pesam igual", "os dois", "nenhum", "mesmo peso"])
tf(Q, "animais", 2, 10, "O polvo tem três corações.", True,
   "Dois corações bombeiam sangue para as brânquias e um para o resto do corpo.",
   "Smithsonian Ocean – Octopus")
op(Q, "internet", 2, 10, "Qual é o nome do símbolo @, usado nos endereços de e-mail?",
   "Arroba", ["a arroba"],
   "Arroba também é uma antiga unidade de peso, cerca de 15 kg.",
   "Dicionário Houaiss – verbete 'arroba'")
mc(Q, "monumentos", 2, 12, "Qual país deu a Estátua da Liberdade de presente aos Estados Unidos?",
   ["França", "Inglaterra", "Espanha", "Itália"], "França",
   "A estátua foi inaugurada em Nova York em 1886.",
   "National Park Service – Statue of Liberty")
mc(Q, "jogos", 2, 12, "Quantas casas tem um tabuleiro de xadrez?",
   ["64", "32", "100", "81"], "64",
   "São 8 fileiras com 8 casas cada, alternando claras e escuras.",
   "FIDE – Laws of Chess, artigo 2")
mc(Q, "corpo humano", 2, 12, "Qual é o maior órgão do corpo humano?",
   ["Pele", "Fígado", "Coração", "Intestino"], "Pele",
   "A pele de um adulto cobre cerca de 2 metros quadrados.",
   "Sociedade Brasileira de Dermatologia")
mc(Q, "siglas", 2, 12, "Qual é o nome completo da ONU?",
   ["Organização das Nações Unidas", "Ordem das Nações Unificadas", "Organização Nacional da União", "Ordem Normativa Universal"],
   "Organização das Nações Unidas",
   "A ONU foi criada em 1945, logo depois da Segunda Guerra Mundial.",
   "Nações Unidas – Carta da ONU (1945)", syn=["nacoes unidas"])
mc(Q, "corpo humano", 3, 12, "Qual é o osso mais longo do corpo humano?",
   ["Fêmur", "Tíbia", "Úmero", "Rádio"], "Fêmur",
   "O fêmur fica na coxa e é também um dos ossos mais fortes.",
   "Enciclopédia Britannica – verbete 'femur'", syn=["femur"])
mc(Q, "jogos", 3, 14, "Quantas peças cada jogador tem no início de uma partida de xadrez?",
   ["16", "12", "20", "8"], "16",
   "São 8 peões, 2 torres, 2 cavalos, 2 bispos, 1 dama e 1 rei.",
   "FIDE – Laws of Chess, artigo 2")
mc(Q, "línguas", 3, 14, "Qual é a língua com mais falantes nativos no mundo?",
   ["Mandarim", "Inglês", "Espanhol", "Hindi"], "Mandarim",
   "O inglês tem mais falantes no total (somando quem aprende), mas o mandarim tem mais nativos.",
   "Ethnologue – Most spoken languages (2025)", ref="Ethnologue 2025")
mc(Q, "astronomia", 4, 14, "Em qual planeta um dia dura mais do que um ano?",
   ["Vênus", "Mercúrio", "Marte", "Júpiter"], "Vênus",
   "Vênus leva cerca de 243 dias terrestres para girar em torno de si e 225 para dar a volta no Sol.",
   "NASA – Venus Facts", syn=["venus"])

# ---- perguntas infantis adicionais (6+)
mc(S, "instrumentos", 1, 6, "Qual instrumento redondo, com platinelas, a gente segura numa mão e bate com a outra?",
   ["Pandeiro", "Piano", "Violino", "Trompete"], "Pandeiro",
   "O pandeiro é essencial no samba, no choro e na capoeira.",
   "IPHAN – Matrizes do Samba no Rio de Janeiro", br=True)
mc(L, "contos de fadas", 1, 6, "Na história 'Cachinhos Dourados', quantos ursos moram na casa?",
   ["3", "2", "5", "7"], "3",
   "Papai Urso, Mamãe Ursa e o Ursinho: e cada um tem sua tigela de mingau.",
   "Robert Southey – The Story of the Three Bears (1837)", syn=["tres ursos"])
mc(Q, "calendário", 1, 6, "Quantos dias tem uma semana?",
   ["7", "5", "6", "10"], "7",
   "De domingo a sábado são 7 dias.",
   "Dicionário Houaiss – verbete 'semana'")
