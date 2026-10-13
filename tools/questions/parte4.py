# Temas novos: Língua portuguesa, Matemática, Política e cidadania, Artes,
# Mitologia e lendas, Astronomia e espaço, Corpo humano e saúde, Culinária.
from qdsl import mc, op, tf

# =========================================================== LÍNGUA PORTUGUESA
P = "por"
mc(P, "alfabeto", 1, 6, "Qual destas palavras começa com a letra A?",
   ["Abacaxi", "Banana", "Uva", "Morango"], "Abacaxi",
   "Abacaxi começa com A. Banana com B, Uva com U e Morango com M.",
   "Ministério da Educação – Base Nacional Comum Curricular (alfabetização)")
mc(P, "antônimos", 1, 6, "Qual é o contrário de 'grande'?",
   ["Pequeno", "Alto", "Largo", "Gigante"], "Pequeno",
   "Palavras de sentido contrário se chamam antônimos.",
   "Dicionário Houaiss – verbete 'pequeno'")
mc(P, "vogais", 1, 6, "Quantas vogais tem o nosso alfabeto?",
   ["5", "3", "7", "10"], "5",
   "As vogais são A, E, I, O e U.",
   "Academia Brasileira de Letras – Vocabulário Ortográfico (VOLP)")
mc(P, "vocabulário", 1, 6, "Qual destas palavras é o nome de um animal?",
   ["Gato", "Mesa", "Azul", "Correr"], "Gato",
   "Mesa é um objeto, azul é uma cor e correr é uma ação.",
   "Dicionário Houaiss – verbete 'gato'")
mc(P, "antônimos", 1, 6, "Qual é o contrário de 'dia'?",
   ["Noite", "Sol", "Manhã", "Semana"], "Noite",
   "Dia e noite são antônimos.",
   "Dicionário Houaiss – verbete 'noite'")
op(P, "antônimos", 1, 7, "Qual palavra significa o contrário de 'alegre'?",
   "Triste", ["tristonho", "infeliz"],
   "Alegre e triste são antônimos; 'infeliz' também serve.",
   "Dicionário Houaiss – verbete 'triste'")
mc(P, "plural", 1, 7, "Qual é o plural de 'pão'?",
   ["Pães", "Pãos", "Pãoes", "Pãs"], "Pães",
   "Palavras terminadas em -ão podem fazer plural em -ães, -ões ou -ãos; 'pão' vira 'pães'.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "diminutivo", 1, 7, "Qual é o diminutivo de 'pé'?",
   ["Pezinho", "Pezão", "Pedal", "Pequeno"], "Pezinho",
   "O sufixo -zinho forma o diminutivo; -ão forma o aumentativo.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "alfabeto", 1, 8, "Quantas letras tem o alfabeto da língua portuguesa?",
   ["26", "23", "24", "30"], "26",
   "Com o Acordo Ortográfico, K, W e Y voltaram oficialmente ao alfabeto, que passou a ter 26 letras.",
   "Acordo Ortográfico da Língua Portuguesa (1990), Base I", br=True, ref="Acordo Ortográfico, em vigor no Brasil desde 2009")
mc(P, "coletivos", 1, 8, "Qual é o coletivo de peixes?",
   ["Cardume", "Alcateia", "Bando", "Constelação"], "Cardume",
   "Cardume é um grupo de peixes. Alcateia é de lobos e bando, de aves.",
   "Dicionário Houaiss – verbete 'cardume'")
mc(P, "sinônimos", 1, 8, "Qual destas palavras é sinônimo de 'feliz'?",
   ["Contente", "Triste", "Bravo", "Cansado"], "Contente",
   "Sinônimos são palavras de sentido parecido.",
   "Dicionário Houaiss – verbete 'contente'")
mc(P, "gênero", 1, 8, "Qual é o feminino de 'cavalo'?",
   ["Égua", "Cavala", "Vaca", "Cabra"], "Égua",
   "Alguns femininos são palavras diferentes: cavalo/égua, boi/vaca, bode/cabra.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "plural", 1, 9, "Qual é o plural de 'pastel'?",
   ["Pastéis", "Pastels", "Pasteles", "Pastelos"], "Pastéis",
   "Palavras terminadas em -el fazem plural em -éis: papel/papéis, anel/anéis.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "classes de palavras", 1, 9, "Qual classe de palavra indica uma ação, como 'pular' e 'cantar'?",
   ["Verbo", "Substantivo", "Adjetivo", "Artigo"], "Verbo",
   "Verbos indicam ação, estado ou fenômeno da natureza.",
   "Base Nacional Comum Curricular – Língua Portuguesa")
mc(P, "sílabas", 1, 9, "Quantas sílabas tem a palavra 'borboleta'?",
   ["4", "3", "5", "2"], "4",
   "Bor-bo-le-ta: quatro sílabas.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "aumentativo", 1, 9, "Qual é o aumentativo de 'casa'?",
   ["Casarão", "Casinha", "Caseiro", "Casal"], "Casarão",
   "Casarão é uma casa grande; casinha é o diminutivo.",
   "Dicionário Houaiss – verbete 'casarão'")
mc(P, "acentuação", 1, 9, "Qual destas palavras tem acento circunflexo?",
   ["Você", "Café", "Sofá", "Avó"], "Você",
   "O circunflexo (^) fecha o som da vogal: você, avô, ônibus.",
   "Acordo Ortográfico da Língua Portuguesa (1990)")
mc(P, "plural", 2, 10, "Qual é o plural de 'cidadão'?",
   ["Cidadãos", "Cidadões", "Cidadães", "Cidadãoes"], "Cidadãos",
   "Cidadão, irmão e mão fazem plural em -ãos.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "ortografia", 2, 10, "Qual destas palavras está escrita corretamente?",
   ["Exceção", "Excessão", "Esceção", "Exseção"], "Exceção",
   "Exceção se escreve com X, C e Ç.",
   "Academia Brasileira de Letras – VOLP")
mc(P, "coletivos", 2, 10, "Qual é o coletivo de lobos?",
   ["Alcateia", "Cardume", "Enxame", "Rebanho"], "Alcateia",
   "Alcateia é um grupo de lobos; enxame é de abelhas e rebanho, de gado.",
   "Dicionário Houaiss – verbete 'alcateia'")
mc(P, "coletivos", 2, 10, "Qual é o coletivo de estrelas?",
   ["Constelação", "Arquipélago", "Galeria", "Biblioteca"], "Constelação",
   "Arquipélago é de ilhas, galeria de quadros e biblioteca de livros.",
   "Dicionário Houaiss – verbete 'constelação'")
mc(P, "classes de palavras", 2, 10, "Qual classe de palavra dá nome a seres e coisas, como 'casa' e 'cachorro'?",
   ["Substantivo", "Verbo", "Advérbio", "Preposição"], "Substantivo",
   "Substantivos nomeiam seres, objetos, lugares e sentimentos.",
   "Base Nacional Comum Curricular – Língua Portuguesa")
mc(P, "classes de palavras", 2, 10, "Qual classe de palavra indica uma característica, como 'bonito' e 'alto'?",
   ["Adjetivo", "Verbo", "Pronome", "Numeral"], "Adjetivo",
   "Adjetivos qualificam o substantivo: casa bonita, menino alto.",
   "Base Nacional Comum Curricular – Língua Portuguesa")
mc(P, "gênero", 2, 10, "Qual é o feminino de 'bode'?",
   ["Cabra", "Boda", "Ovelha", "Vaca"], "Cabra",
   "O feminino de bode é cabra; o de carneiro é ovelha.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "classes de palavras", 2, 10, "Qual destas palavras é um substantivo próprio?",
   ["Brasil", "cidade", "país", "rio"], "Brasil",
   "Substantivos próprios nomeiam um ser específico e começam com letra maiúscula.",
   "Base Nacional Comum Curricular – Língua Portuguesa")
mc(P, "mau ou mal", 2, 10, "A palavra 'mau' é o contrário de qual palavra?",
   ["Bom", "Bem", "Mal", "Ótimo"], "Bom",
   "Mau é o contrário de bom; mal é o contrário de bem.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "língua no mundo", 1, 10, "Qual destes países NÃO faz parte do grupo de países lusófonos?",
   ["Espanha", "Angola", "Moçambique", "Cabo Verde"], "Espanha",
   "Lusófonos são os países de língua portuguesa. Na Espanha a língua oficial é o espanhol.",
   "Comunidade dos Países de Língua Portuguesa (CPLP)")
mc(P, "acentuação", 2, 12, "Qual destas palavras é oxítona (tem a sílaba mais forte no final)?",
   ["Café", "Mesa", "Lâmpada", "Livro"], "Café",
   "Oxítonas têm a última sílaba tônica: ca-FÉ. Mesa e livro são paroxítonas; lâmpada é proparoxítona.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "acentuação", 2, 12, "Qual destas palavras é proparoxítona?",
   ["Lâmpada", "Café", "Cadeira", "Jacaré"], "Lâmpada",
   "Proparoxítonas têm a antepenúltima sílaba tônica e sempre levam acento: LÂM-pa-da.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "mas ou mais", 2, 12, "Qual palavra completa a frase: 'Eu queria ir, ___ choveu'?",
   ["mas", "mais", "mau"], "mas",
   "'Mas' indica oposição (porém); 'mais' indica quantidade; 'mau' é o contrário de bom.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo",
   syn=["porem"])
mc(P, "siglas", 2, 12, "Qual é o nome completo do CEP, o código usado nos endereços?",
   ["Código de Endereçamento Postal", "Cadastro Estadual de Pessoas", "Central de Entregas Postais", "Controle de Endereços Públicos"],
   "Código de Endereçamento Postal",
   "O CEP foi criado pelos Correios em 1971 para organizar a entrega de correspondências.",
   "Correios – O que é o CEP", br=True)
mc(P, "dicionários", 2, 14, "Qual dicionário brasileiro ficou tão famoso que seu nome virou apelido para 'dicionário'?",
   ["Aurélio", "Michaelis", "Houaiss", "Caldas Aulete"], "Aurélio",
   "O 'Novo Dicionário da Língua Portuguesa', de Aurélio Buarque de Holanda, foi lançado em 1975.",
   "Academia Brasileira de Letras – Aurélio Buarque de Holanda", br=True)
mc(P, "acordo ortográfico", 3, 14, "Em que ano o Novo Acordo Ortográfico começou a valer no Brasil?",
   ["2009", "1990", "2002", "2016"], "2009",
   "O acordo foi assinado em 1990, entrou em vigor no Brasil em 2009 e se tornou obrigatório em 2016.",
   "Decreto nº 6.583/2008", br=True)
mc(P, "crase", 3, 14, "Qual destas frases usa a crase corretamente?",
   ["Vou à escola.", "Vou à pé.", "Ele começou à cantar.", "Fiz tudo à você."], "Vou à escola.",
   "Crase é a fusão da preposição 'a' com o artigo 'a'; não se usa antes de palavras masculinas, verbos ou pronomes como 'você'.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "concordância", 3, 14, "Qual destas frases está correta?",
   ["Faz dois anos que me mudei.", "Fazem dois anos que me mudei.", "Fazem dois anos que mudei-me."], "Faz dois anos que me mudei.",
   "Quando indica tempo decorrido, o verbo 'fazer' é impessoal e fica no singular.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo")
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem é um exagero, como em 'Chorei rios de lágrimas'?",
   ["Hipérbole", "Metáfora", "Ironia", "Eufemismo"], "Hipérbole",
   "Hipérbole exagera a ideia para dar ênfase.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo", syn=["hiperbole"])
mc(P, "figuras de linguagem", 3, 14, "Qual figura de linguagem aparece em 'Ela é forte como um touro'?",
   ["Comparação", "Hipérbole", "Ironia", "Onomatopeia"], "Comparação",
   "A comparação (ou símile) aproxima dois elementos usando um conectivo como 'como'.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo", syn=["simile", "comparacao"])
mc(P, "língua no mundo", 3, 14, "Quantos países fazem parte da CPLP, a Comunidade dos Países de Língua Portuguesa?",
   ["9", "5", "7", "12"], "9",
   "Brasil, Portugal, Angola, Moçambique, Cabo Verde, Guiné-Bissau, São Tomé e Príncipe, Timor-Leste e Guiné Equatorial.",
   "CPLP – Estados-membros", ref="Composição desde 2014")
mc(P, "figuras de linguagem", 4, 16, "Qual figura de linguagem dá características humanas a coisas, como em 'O vento cantava'?",
   ["Personificação", "Hipérbole", "Antítese", "Eufemismo"], "Personificação",
   "Também chamada de prosopopeia: atribui ações humanas a seres inanimados.",
   "Celso Cunha e Lindley Cintra – Nova Gramática do Português Contemporâneo", syn=["prosopopeia", "personificacao"])

# =========================================================== MATEMÁTICA
M = "mat"
mc(M, "adição", 1, 6, "Quanto é 2 + 3?",
   ["5", "4", "6", "7"], "5",
   "Dois mais três é igual a cinco.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 1, 6, "Quantos lados tem um triângulo?",
   ["3", "4", "5", "6"], "3",
   "Tri quer dizer três: o triângulo tem 3 lados e 3 ângulos.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "subtração", 1, 6, "Quanto é 10 menos 4?",
   ["6", "5", "7", "14"], "6",
   "Dez menos quatro é igual a seis.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "sequências", 1, 6, "Qual número vem logo depois do 19?",
   ["20", "18", "21", "29"], "20",
   "Depois do 19 vem o 20.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "problemas", 1, 6, "Quantas rodas têm duas bicicletas juntas?",
   ["4", "2", "6", "8"], "4",
   "Cada bicicleta tem 2 rodas: 2 + 2 = 4.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 1, 6, "Qual destas figuras é redonda?",
   ["Círculo", "Quadrado", "Triângulo", "Retângulo"], "Círculo",
   "O círculo não tem cantos; as outras figuras têm lados retos.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "frações", 1, 7, "Quanto é a metade de 10?",
   ["5", "2", "20", "8"], "5",
   "Metade é dividir em duas partes iguais: 10 ÷ 2 = 5.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "frações", 1, 8, "Qual fração representa a metade?",
   ["1/2", "1/3", "2/3", "1/4"], "1/2",
   "Um meio: uma parte de duas partes iguais.",
   "Base Nacional Comum Curricular – Matemática", syn=["um meio", "meio"])
mc(M, "multiplicação", 1, 8, "Qual é o dobro de 15?",
   ["30", "25", "45", "60"], "30",
   "Dobro é multiplicar por 2: 15 × 2 = 30.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "multiplicação", 1, 9, "Qual é o resultado de 9 multiplicado por 9?",
   ["81", "72", "99", "18"], "81",
   "9 × 9 = 81.",
   "Tabuada")
mc(M, "divisão", 1, 9, "Quanto é 100 dividido por 4?",
   ["25", "20", "40", "24"], "25",
   "100 ÷ 4 = 25, como quatro moedas de 25 centavos formam 1 real.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "medidas", 1, 9, "Quantos centímetros tem 1 metro?",
   ["100", "10", "1000", "50"], "100",
   "Centi quer dizer centésimo: 1 metro tem 100 centímetros.",
   "Inmetro – Sistema Internacional de Unidades")
mc(M, "medidas", 1, 9, "Quantos metros tem 1 quilômetro?",
   ["1000", "100", "10000", "10"], "1000",
   "Quilo quer dizer mil: 1 km = 1.000 m.",
   "Inmetro – Sistema Internacional de Unidades")
mc(M, "multiplicação", 1, 9, "Qualquer número multiplicado por zero dá quanto?",
   ["0", "1", "O próprio número", "10"], "0",
   "Zero vezes qualquer coisa é zero.",
   "Base Nacional Comum Curricular – Matemática", syn=["zero"])
mc(M, "problemas", 1, 9, "Se um pacote tem 6 ovos, quantos ovos há em 4 pacotes?",
   ["24", "10", "18", "30"], "24",
   "4 × 6 = 24 ovos.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 1, 10, "Quantos graus tem um ângulo reto?",
   ["90", "45", "180", "360"], "90",
   "O ângulo reto forma um 'canto' de quadrado, com 90 graus.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "números romanos", 1, 10, "Em números romanos, qual valor representa a letra X?",
   ["10", "5", "50", "100"], "10",
   "I = 1, V = 5, X = 10, L = 50, C = 100.",
   "Enciclopédia Britannica – verbete 'Roman numeral'")
mc(M, "multiplicação", 1, 10, "Qual número, multiplicado por ele mesmo, dá 49?",
   ["7", "8", "6", "9"], "7",
   "7 × 7 = 49: a raiz quadrada de 49 é 7.",
   "Tabuada")
mc(M, "tempo", 2, 10, "Quantos minutos há em duas horas e meia?",
   ["150", "130", "250", "120"], "150",
   "Duas horas são 120 minutos, mais 30 da meia hora: 150.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 2, 10, "Como se chama um polígono de 8 lados?",
   ["Octógono", "Hexágono", "Pentágono", "Decágono"], "Octógono",
   "O sinal de 'PARE' no trânsito tem formato de octógono.",
   "Dicionário Houaiss – verbete 'octógono'", syn=["octogono"])
mc(M, "geometria", 2, 10, "Quantas faces tem um cubo?",
   ["6", "4", "8", "12"], "6",
   "Um dado é um cubo: 6 faces quadradas.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "números", 2, 10, "Qual é o menor número par positivo?",
   ["2", "0", "1", "4"], "2",
   "O zero é par, mas não é positivo; o 1 é ímpar.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "sequências", 2, 10, "Qual número continua a sequência 2, 4, 8, 16...?",
   ["32", "18", "24", "20"], "32",
   "Cada número é o dobro do anterior: 16 × 2 = 32.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "tempo", 2, 10, "Uma hora tem quantos segundos?",
   ["3600", "60", "600", "1000"], "3600",
   "60 minutos × 60 segundos = 3.600 segundos.",
   "Bureau International des Poids et Mesures – Unidades de tempo")
mc(M, "porcentagem", 2, 12, "Quanto é 15% de 200?",
   ["30", "15", "20", "35"], "30",
   "10% de 200 é 20 e 5% é 10: somando, 30.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "porcentagem", 2, 12, "Quanto é 25% de 80?",
   ["20", "25", "40", "16"], "20",
   "25% é um quarto: 80 ÷ 4 = 20.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "potências e raízes", 2, 12, "Qual é a raiz quadrada de 144?",
   ["12", "14", "16", "72"], "12",
   "12 × 12 = 144.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "números primos", 2, 12, "Qual é o próximo número primo depois do 7?",
   ["11", "9", "8", "13"], "11",
   "O 9 é divisível por 3 e o 8 por 2; o 11 só é divisível por 1 e por ele mesmo.",
   "Base Nacional Comum Curricular – Matemática")
tf(M, "números primos", 2, 12, "O número 1 é um número primo.", False,
   "Primos têm exatamente dois divisores; o 1 tem só um. O menor primo é o 2.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 2, 12, "Quanto dá a soma dos ângulos internos de um triângulo?",
   ["180 graus", "90 graus", "360 graus", "270 graus"], "180 graus",
   "Em qualquer triângulo plano, os três ângulos somam 180°.",
   "Euclides – Os Elementos, Livro I", syn=["180"])
mc(M, "frações", 2, 12, "Quanto é 3/4 de 100?",
   ["75", "34", "25", "70"], "75",
   "Um quarto de 100 é 25; três quartos são 75.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 2, 12, "Qual é a área de um quadrado com 5 cm de lado?",
   ["25 cm²", "20 cm²", "10 cm²", "50 cm²"], "25 cm²",
   "Área do quadrado = lado × lado = 5 × 5 = 25 cm².",
   "Base Nacional Comum Curricular – Matemática", syn=["25"])
mc(M, "geometria", 2, 12, "Qual é o perímetro de um retângulo de 3 m por 5 m?",
   ["16 m", "15 m", "8 m", "30 m"], "16 m",
   "Perímetro é a soma dos lados: 3 + 5 + 3 + 5 = 16 m.",
   "Base Nacional Comum Curricular – Matemática", syn=["16"])
mc(M, "números decimais", 2, 12, "Quanto é 0,5 + 0,25?",
   ["0,75", "0,30", "0,7", "1,25"], "0,75",
   "Meio mais um quarto dá três quartos: 0,75.",
   "Base Nacional Comum Curricular – Matemática", syn=["0 75", "3 quartos"])
mc(M, "números romanos", 2, 12, "Em números romanos, como se escreve 50?",
   ["L", "C", "V", "D"], "L",
   "L = 50, C = 100, D = 500 e M = 1.000.",
   "Enciclopédia Britannica – verbete 'Roman numeral'")
mc(M, "constantes", 2, 12, "Qual é o valor aproximado do número pi?",
   ["3,14", "2,71", "1,61", "9,81"], "3,14",
   "Pi é a razão entre o comprimento e o diâmetro de qualquer círculo.",
   "Enciclopédia Britannica – verbete 'pi'", syn=["3 14", "3 virgula 14"])
mc(M, "expressões", 3, 12, "Respeitando a ordem das operações, quanto é 7 + 8 × 2?",
   ["23", "30", "22", "46"], "23",
   "Primeiro a multiplicação (8 × 2 = 16), depois a soma: 7 + 16 = 23.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "somas", 3, 12, "Qual é o resultado de 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10?",
   ["55", "50", "45", "60"], "55",
   "Diz a lenda que o jovem Gauss somou pares: (1+10) + (2+9)... = 5 × 11 = 55.",
   "Enciclopédia Britannica – verbete 'Carl Friedrich Gauss'")
mc(M, "números primos", 3, 12, "Qual é o único número par que é primo?",
   ["2", "4", "0", "6"], "2",
   "Todo outro número par é divisível por 2, então tem mais de dois divisores.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "potências e raízes", 3, 14, "Quanto é 2 elevado a 10?",
   ["1024", "20", "100", "512"], "1024",
   "2¹⁰ = 1.024 — por isso 1 kilobyte já foi definido como 1.024 bytes.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "geometria", 3, 14, "Quantas arestas tem um cubo?",
   ["12", "6", "8", "24"], "12",
   "4 arestas em cima, 4 embaixo e 4 nas laterais.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "história da matemática", 3, 14, "Quem é conhecido como o 'pai da geometria' e escreveu 'Os Elementos'?",
   ["Euclides", "Pitágoras", "Arquimedes", "Tales"], "Euclides",
   "Euclides de Alexandria viveu por volta de 300 a.C.",
   "Enciclopédia Britannica – verbete 'Euclid'")
mc(M, "geometria", 2, 14, "Qual teorema diz que, num triângulo retângulo, o quadrado da hipotenusa é igual à soma dos quadrados dos catetos?",
   ["Teorema de Pitágoras", "Teorema de Tales", "Fórmula de Bhaskara", "Teorema de Euclides"], "Teorema de Pitágoras",
   "a² = b² + c²: o exemplo clássico é o triângulo 3, 4, 5.",
   "Enciclopédia Britannica – verbete 'Pythagorean theorem'", syn=["pitagoras"])
mc(M, "números primos", 4, 14, "Quantos números primos existem entre 1 e 20?",
   ["8", "7", "9", "10"], "8",
   "São eles: 2, 3, 5, 7, 11, 13, 17 e 19.",
   "Base Nacional Comum Curricular – Matemática")
mc(M, "fatorial", 4, 16, "Quanto é 5 fatorial (5!)?",
   ["120", "25", "60", "720"], "120",
   "5! = 5 × 4 × 3 × 2 × 1 = 120.",
   "Enciclopédia Britannica – verbete 'factorial'")
mc(M, "logaritmos", 4, 16, "Qual é o logaritmo de 1000 na base 10?",
   ["3", "10", "100", "4"], "3",
   "10³ = 1.000, então log₁₀ 1.000 = 3.",
   "Enciclopédia Britannica – verbete 'logarithm'")

# =========================================================== POLÍTICA E CIDADANIA
G = "pol"
mc(G, "municípios", 1, 6, "Quem é a pessoa eleita para governar uma cidade?",
   ["O prefeito", "O governador", "O senador", "O juiz"], "O prefeito",
   "Os prefeitos são eleitos a cada 4 anos e governam os municípios.",
   "Constituição Federal de 1988, art. 29", syn=["prefeito", "a prefeita"], br=True)
mc(G, "trânsito", 1, 6, "Qual é a atitude certa antes de atravessar a rua?",
   ["Olhar para os dois lados", "Correr sem olhar", "Atravessar no sinal vermelho para pedestres", "Brincar no meio da rua"],
   "Olhar para os dois lados",
   "E de preferência atravessar na faixa de pedestres, quando o sinal estiver verde para quem anda a pé.",
   "Código de Trânsito Brasileiro, art. 69", br=True)
mc(G, "trânsito", 1, 6, "No semáforo, qual cor indica que os carros devem parar?",
   ["Vermelho", "Verde", "Azul", "Branco"], "Vermelho",
   "Vermelho: pare. Amarelo: atenção. Verde: siga.",
   "Código de Trânsito Brasileiro – Anexo II")
mc(G, "meio ambiente", 1, 6, "Onde devemos jogar o lixo?",
   ["Na lixeira", "No chão", "No rio", "Na rua"], "Na lixeira",
   "Lixo jogado na rua entope bueiros e polui rios e mares.",
   "Ministério do Meio Ambiente – Política Nacional de Resíduos Sólidos")
mc(G, "emergências", 1, 8, "Qual é o número de telefone do SAMU no Brasil?",
   ["192", "190", "193", "100"], "192",
   "SAMU: 192. Polícia Militar: 190. Bombeiros: 193.",
   "Ministério da Saúde – SAMU 192", br=True)
mc(G, "emergências", 1, 8, "Qual número chamamos para falar com a Polícia Militar no Brasil?",
   ["190", "192", "193", "181"], "190",
   "O 190 funciona em todo o país, de graça, inclusive de celular sem crédito.",
   "Anatel – Serviços de utilidade pública", br=True)
mc(G, "emergências", 1, 8, "Qual número chamamos para falar com os Bombeiros no Brasil?",
   ["193", "190", "192", "199"], "193",
   "Os Bombeiros atendem incêndios, resgates e salvamentos.",
   "Anatel – Serviços de utilidade pública", br=True)
mc(G, "estados", 1, 9, "Quem governa um estado brasileiro?",
   ["O governador", "O prefeito", "O vereador", "O presidente do Senado"], "O governador",
   "Governadores são eleitos a cada 4 anos, junto com o presidente.",
   "Constituição Federal de 1988, art. 28", syn=["governador", "a governadora"], br=True)
mc(G, "poderes", 1, 10, "Quais são os três Poderes da República no Brasil?",
   ["Executivo, Legislativo e Judiciário", "Federal, Estadual e Municipal", "Militar, Civil e Religioso", "Presidente, Governador e Prefeito"],
   "Executivo, Legislativo e Judiciário",
   "Os três Poderes são independentes e harmônicos entre si.",
   "Constituição Federal de 1988, art. 2º", br=True)
mc(G, "poderes", 1, 10, "Qual Poder é responsável principalmente por fazer as leis?",
   ["Legislativo", "Executivo", "Judiciário", "Moderador"], "Legislativo",
   "No âmbito federal, o Legislativo é o Congresso Nacional: Câmara dos Deputados e Senado.",
   "Constituição Federal de 1988, art. 44", br=True)
mc(G, "constituição", 1, 10, "Como se chama a lei máxima de um país, acima de todas as outras?",
   ["Constituição", "Decreto", "Portaria", "Estatuto"], "Constituição",
   "Nenhuma lei pode contrariar a Constituição.",
   "Constituição Federal de 1988", br=True)
mc(G, "eleições", 1, 10, "A partir de qual idade o voto é obrigatório no Brasil?",
   ["18 anos", "16 anos", "21 anos", "17 anos"], "18 anos",
   "O voto é obrigatório dos 18 aos 70 anos e facultativo para quem tem 16 ou 17 anos ou mais de 70.",
   "Constituição Federal de 1988, art. 14", syn=["18"], br=True)
mc(G, "municípios", 1, 10, "Como se chamam os representantes eleitos para a Câmara Municipal?",
   ["Vereadores", "Deputados", "Senadores", "Prefeitos"], "Vereadores",
   "Vereadores fazem as leis da cidade e fiscalizam o prefeito.",
   "Constituição Federal de 1988, art. 29", br=True)
mc(G, "governo federal", 1, 10, "Quem é o chefe de Estado e de governo no Brasil?",
   ["O presidente da República", "O presidente do Senado", "O ministro da Justiça", "O presidente do STF"],
   "O presidente da República",
   "No presidencialismo, o presidente acumula as duas funções.",
   "Constituição Federal de 1988, art. 76", syn=["presidente", "a presidente"], br=True)
mc(G, "eleições", 2, 12, "A partir de qual idade o brasileiro já pode votar, de forma facultativa?",
   ["16 anos", "14 anos", "18 anos", "15 anos"], "16 anos",
   "Aos 16 anos já é possível tirar o título de eleitor e votar.",
   "Constituição Federal de 1988, art. 14", syn=["16"], br=True)
mc(G, "eleições", 2, 12, "A partir de qual idade o voto passa a ser facultativo para os idosos?",
   ["70 anos", "60 anos", "65 anos", "80 anos"], "70 anos",
   "Acima de 70 anos, votar é opcional.",
   "Constituição Federal de 1988, art. 14", syn=["70"], br=True)
mc(G, "senado", 2, 12, "Quantos senadores cada estado brasileiro elege?",
   ["3", "2", "4", "5"], "3",
   "Cada estado e o Distrito Federal têm 3 senadores, somando 81.",
   "Constituição Federal de 1988, art. 46", br=True)
mc(G, "senado", 2, 12, "Qual é a duração do mandato de um senador no Brasil?",
   ["8 anos", "4 anos", "6 anos", "5 anos"], "8 anos",
   "As eleições para o Senado renovam alternadamente um terço e dois terços das vagas a cada 4 anos.",
   "Constituição Federal de 1988, art. 46", syn=["8", "oito anos"], br=True)
mc(G, "governo federal", 2, 10, "Qual é a duração do mandato do presidente da República no Brasil?",
   ["4 anos", "5 anos", "6 anos", "8 anos"], "4 anos",
   "O mandato é de 4 anos, com direito a uma reeleição consecutiva.",
   "Constituição Federal de 1988, art. 82", syn=["4", "quatro anos"], br=True)
mc(G, "justiça", 2, 12, "Qual é o mais alto tribunal do Brasil, guardião da Constituição?",
   ["Supremo Tribunal Federal", "Superior Tribunal de Justiça", "Tribunal Superior Eleitoral", "Tribunal de Contas da União"],
   "Supremo Tribunal Federal",
   "O STF tem 11 ministros.",
   "Constituição Federal de 1988, art. 101 e 102", syn=["stf", "supremo"], br=True)
mc(G, "eleições", 2, 12, "Qual órgão organiza as eleições no Brasil?",
   ["Tribunal Superior Eleitoral", "Polícia Federal", "Banco Central", "Ministério da Educação"],
   "Tribunal Superior Eleitoral",
   "O TSE comanda a Justiça Eleitoral em todo o país.",
   "Constituição Federal de 1988, art. 118", syn=["tse", "justica eleitoral"], br=True)
mc(G, "direitos", 2, 12, "Qual lei reúne os direitos das crianças e adolescentes no Brasil?",
   ["Estatuto da Criança e do Adolescente", "Código Civil", "Consolidação das Leis do Trabalho", "Código de Trânsito"],
   "Estatuto da Criança e do Adolescente",
   "O ECA é a Lei nº 8.069, de 1990.",
   "Lei nº 8.069/1990", syn=["eca"], br=True)
mc(G, "documentos", 2, 12, "O CPF, documento da Receita Federal, é a sigla de quê?",
   ["Cadastro de Pessoas Físicas", "Controle Pessoal de Finanças", "Cartão de Pagamento Federal", "Certificado de Pessoa Física"],
   "Cadastro de Pessoas Físicas",
   "O CPF é emitido pela Receita Federal e identifica cada contribuinte.",
   "Receita Federal – CPF", br=True)
mc(G, "governo federal", 2, 12, "Em qual palácio fica o gabinete de trabalho do presidente da República?",
   ["Palácio do Planalto", "Palácio da Alvorada", "Palácio do Itamaraty", "Palácio do Jaburu"], "Palácio do Planalto",
   "O Planalto é a sede do Executivo; o Alvorada é a residência oficial.",
   "Presidência da República – Palácio do Planalto", syn=["planalto"], br=True)
mc(G, "governo federal", 2, 12, "Qual é o sistema de governo do Brasil, confirmado pelo plebiscito de 1993?",
   ["Presidencialismo", "Parlamentarismo", "Monarquia", "Semipresidencialismo"], "Presidencialismo",
   "Em 1993 os eleitores escolheram república e presidencialismo.",
   "TSE – Plebiscito de 1993", br=True)
mc(G, "governo federal", 3, 14, "Qual palácio é a residência oficial do presidente do Brasil?",
   ["Palácio da Alvorada", "Palácio do Planalto", "Palácio Guanabara", "Palácio do Catete"], "Palácio da Alvorada",
   "Projetado por Oscar Niemeyer, foi inaugurado em 1958.",
   "Presidência da República – Palácio da Alvorada", syn=["alvorada"], br=True)
mc(G, "eleições", 3, 14, "Em que ano a urna eletrônica foi usada pela primeira vez nas eleições brasileiras?",
   ["1996", "1989", "2002", "1985"], "1996",
   "Em 1996 ela foi usada nas eleições municipais de parte das cidades; em 2000 chegou a todo o país.",
   "TSE – História da urna eletrônica", br=True)
mc(G, "eleições", 3, 14, "Em que ano as mulheres conquistaram o direito de votar no Brasil?",
   ["1932", "1889", "1946", "1964"], "1932",
   "O Código Eleitoral de 1932 garantiu o voto feminino.",
   "Decreto nº 21.076/1932 – TSE", br=True)
mc(G, "democracia", 3, 14, "O que é um plebiscito?",
   ["Uma consulta ao povo antes de uma decisão", "Um tipo de imposto", "Uma lei municipal", "Um cargo político"],
   "Uma consulta ao povo antes de uma decisão",
   "No referendo, ao contrário, o povo aprova ou rejeita algo já decidido.",
   "Lei nº 9.709/1998", br=True)
mc(G, "organizações internacionais", 3, 14, "Em que ano foi criada a Organização das Nações Unidas?",
   ["1945", "1919", "1950", "1939"], "1945",
   "A Carta da ONU entrou em vigor em 24 de outubro de 1945.",
   "Nações Unidas – História")
mc(G, "organizações internacionais", 3, 14, "Quantos países são membros da ONU?",
   ["193", "150", "200", "177"], "193",
   "O Sudão do Sul foi o último a entrar, em 2011.",
   "Nações Unidas – Estados-membros", ref="Composição desde 2011")
mc(G, "direitos", 3, 14, "Qual documento a ONU proclamou em 1948 com 30 artigos sobre direitos de todas as pessoas?",
   ["Declaração Universal dos Direitos Humanos", "Carta Magna", "Convenção de Genebra", "Tratado de Versalhes"],
   "Declaração Universal dos Direitos Humanos",
   "Foi adotada em 10 de dezembro de 1948, em Paris.",
   "Nações Unidas – Declaração Universal dos Direitos Humanos", syn=["declaracao universal"])
mc(G, "organizações internacionais", 3, 14, "Em qual cidade fica a sede da Comissão Europeia?",
   ["Bruxelas", "Paris", "Berlim", "Estrasburgo"], "Bruxelas",
   "Bruxelas, na Bélgica, é a principal sede das instituições da União Europeia.",
   "União Europeia – Instituições")
mc(G, "eleições", 4, 16, "Qual foi o primeiro país a garantir o voto feminino em eleições nacionais, em 1893?",
   ["Nova Zelândia", "Estados Unidos", "Reino Unido", "França"], "Nova Zelândia",
   "As neozelandesas votaram pela primeira vez em novembro de 1893.",
   "New Zealand History – Women and the vote")

# =========================================================== ARTES
A = "art"
mc(A, "cores", 1, 6, "Que cor obtemos ao misturar azul e amarelo?",
   ["Verde", "Roxo", "Laranja", "Marrom"], "Verde",
   "Azul e amarelo são primárias; juntas formam o verde.",
   "Base Nacional Comum Curricular – Arte")
mc(A, "cores", 1, 6, "Que cor obtemos ao misturar vermelho e branco?",
   ["Rosa", "Verde", "Azul", "Preto"], "Rosa",
   "O branco clareia as cores: vermelho + branco = rosa.",
   "Base Nacional Comum Curricular – Arte")
mc(A, "cores", 1, 6, "Misturando tinta vermelha com tinta amarela, que cor aparece?",
   ["Laranja", "Roxo", "Verde", "Cinza"], "Laranja",
   "Vermelho e amarelo formam o laranja, uma cor secundária.",
   "Base Nacional Comum Curricular – Arte")
mc(A, "materiais", 1, 6, "Qual objeto usamos para pintar um quadro, junto com a tinta?",
   ["Pincel", "Martelo", "Tesoura", "Régua"], "Pincel",
   "Os pincéis podem ter pelos naturais ou sintéticos.",
   "Base Nacional Comum Curricular – Arte")
mc(A, "quadrinhos", 1, 6, "Nos gibis brasileiros, qual menina baixinha e dentuça carrega um coelhinho azul chamado Sansão?",
   ["Mônica", "Magali", "Marina", "Rosinha"], "Mônica",
   "Mônica foi criada por Mauricio de Sousa em 1963.",
   "Mauricio de Sousa Produções – Turma da Mônica", syn=["monica"], br=True)
mc(A, "quadrinhos", 1, 6, "Qual personagem dos gibis brasileiros vive sujo e foge da água?",
   ["Cascão", "Cebolinha", "Chico Bento", "Franjinha"], "Cascão",
   "Cascão tem pavor de água e é o melhor amigo do Cebolinha.",
   "Mauricio de Sousa Produções – Turma da Mônica", syn=["cascao"], br=True)
mc(A, "quadrinhos", 1, 7, "Qual personagem dos gibis brasileiros troca o R pelo L quando fala?",
   ["Cebolinha", "Cascão", "Magali", "Anjinho"], "Cebolinha",
   "Os 'planos infalíveis' do Cebolinha contra a Mônica nunca dão certo.",
   "Mauricio de Sousa Produções – Turma da Mônica", br=True)
mc(A, "escultura", 1, 7, "Qual destes materiais um escultor costuma usar?",
   ["Mármore", "Algodão-doce", "Gelatina", "Sabão em pó"], "Mármore",
   "Esculturas também são feitas em bronze, madeira, argila e pedra-sabão.",
   "Enciclopédia Britannica – verbete 'sculpture'")
mc(A, "quadrinhos", 1, 8, "Qual artista brasileiro criou a 'Turma da Mônica'?",
   ["Mauricio de Sousa", "Ziraldo", "Monteiro Lobato", "Henfil"], "Mauricio de Sousa",
   "Os gibis da turma são publicados desde os anos 1960.",
   "Mauricio de Sousa Produções", syn=["mauricio"], br=True)
mc(A, "cores", 1, 8, "Quais são as três cores primárias tradicionais na pintura?",
   ["Vermelho, amarelo e azul", "Verde, laranja e roxo", "Preto, branco e cinza", "Rosa, marrom e verde"],
   "Vermelho, amarelo e azul",
   "Misturando as primárias obtemos as secundárias: verde, laranja e roxo.",
   "Base Nacional Comum Curricular – Arte")
mc(A, "técnicas", 1, 8, "Como se chama a arte japonesa de dobrar papel?",
   ["Origami", "Ikebana", "Mangá", "Caligrafia"], "Origami",
   "Ikebana é a arte de arranjos florais; mangá são os quadrinhos japoneses.",
   "Enciclopédia Britannica – verbete 'origami'")
mc(A, "pintura", 1, 10, "Quem pintou a 'Mona Lisa'?",
   ["Leonardo da Vinci", "Michelangelo", "Vincent van Gogh", "Pablo Picasso"], "Leonardo da Vinci",
   "Leonardo pintou o quadro no início do século XVI.",
   "Museu do Louvre – La Joconde", syn=["da vinci", "leonardo"])
mc(A, "arquitetura", 1, 10, "Em qual cidade italiana fica a famosa torre inclinada?",
   ["Pisa", "Roma", "Veneza", "Milão"], "Pisa",
   "A torre começou a inclinar ainda durante a construção, no século XII.",
   "UNESCO – Piazza del Duomo, Pisa")
mc(A, "técnicas", 2, 10, "Como se chama a arte de escrever com letras bonitas e decorativas?",
   ["Caligrafia", "Ortografia", "Tipografia", "Xilogravura"], "Caligrafia",
   "Caligrafia vem do grego: 'bela escrita'.",
   "Dicionário Houaiss – verbete 'caligrafia'")
mc(A, "pintura", 2, 12, "Qual pintor holandês pintou 'A Noite Estrelada'?",
   ["Vincent van Gogh", "Rembrandt", "Claude Monet", "Salvador Dalí"], "Vincent van Gogh",
   "Van Gogh pintou o quadro em 1889, vendo a paisagem da janela de um asilo na França.",
   "MoMA – The Starry Night", syn=["van gogh"])
mc(A, "museus", 2, 12, "Em qual museu de Paris está exposta a 'Mona Lisa'?",
   ["Museu do Louvre", "Museu d'Orsay", "Centro Pompidou", "Museu Rodin"], "Museu do Louvre",
   "O Louvre é o museu mais visitado do mundo.",
   "Museu do Louvre", syn=["louvre"])
mc(A, "pintura", 2, 12, "Quem pintou o teto da Capela Sistina, no Vaticano?",
   ["Michelangelo", "Rafael", "Leonardo da Vinci", "Botticelli"], "Michelangelo",
   "O trabalho levou cerca de quatro anos, de 1508 a 1512.",
   "Museus do Vaticano – Capela Sistina")
mc(A, "escultura", 2, 12, "Qual escultura de Auguste Rodin mostra um homem sentado com a mão no queixo?",
   ["O Pensador", "O Beijo", "Davi", "Vênus de Milo"], "O Pensador",
   "O Pensador foi criado como parte da obra 'A Porta do Inferno'.",
   "Museu Rodin (Paris) – Le Penseur")
mc(A, "dança", 2, 12, "Qual balé de Tchaikovsky conta a história de uma princesa transformada em cisne?",
   ["O Lago dos Cisnes", "O Quebra-Nozes", "A Bela Adormecida", "Giselle"], "O Lago dos Cisnes",
   "Estreou em Moscou em 1877.",
   "Enciclopédia Britannica – verbete 'Swan Lake'", syn=["lago dos cisnes"])
mc(A, "pintura", 2, 12, "Qual pintora mexicana ficou famosa por seus autorretratos com flores no cabelo?",
   ["Frida Kahlo", "Tarsila do Amaral", "Georgia O'Keeffe", "Anita Malfatti"], "Frida Kahlo",
   "A Casa Azul, onde Frida viveu, na Cidade do México, hoje é um museu.",
   "Museo Frida Kahlo", syn=["frida"])
mc(A, "pintura", 3, 14, "Qual artista espanhol pintou 'Guernica', sobre o bombardeio de uma cidade na Guerra Civil Espanhola?",
   ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Francisco Goya"], "Pablo Picasso",
   "O painel de 1937 está no Museu Reina Sofía, em Madri.",
   "Museo Reina Sofía – Guernica", syn=["picasso"])
mc(A, "movimentos", 3, 14, "Qual movimento artístico do início do século XX usava formas geométricas e vários pontos de vista ao mesmo tempo?",
   ["Cubismo", "Impressionismo", "Barroco", "Renascimento"], "Cubismo",
   "Picasso e Georges Braque são os principais nomes do cubismo.",
   "Enciclopédia Britannica – verbete 'Cubism'")
mc(A, "pintura", 3, 14, "Qual pintor surrealista ficou famoso pelos relógios derretidos de 'A Persistência da Memória'?",
   ["Salvador Dalí", "René Magritte", "Pablo Picasso", "Joan Miró"], "Salvador Dalí",
   "O quadro de 1931 está no MoMA, em Nova York.",
   "MoMA – The Persistence of Memory", syn=["dali"])
mc(A, "pintura", 3, 14, "Qual pintor brasileiro fez os painéis 'Guerra e Paz', na sede da ONU em Nova York?",
   ["Candido Portinari", "Di Cavalcanti", "Tarsila do Amaral", "Anita Malfatti"], "Candido Portinari",
   "Os painéis foram entregues em 1956 e estão no saguão da Assembleia Geral.",
   "Projeto Portinari", syn=["portinari"], br=True)
mc(A, "pintura", 3, 14, "Qual pintor impressionista francês pintou a série 'Ninfeias'?",
   ["Claude Monet", "Edgar Degas", "Paul Cézanne", "Auguste Renoir"], "Claude Monet",
   "Monet pintou as ninfeias do lago do seu jardim em Giverny.",
   "Musée de l'Orangerie – Les Nymphéas", syn=["monet"])
mc(A, "pintura", 3, 14, "O quadro 'O Grito' é de qual artista norueguês?",
   ["Edvard Munch", "Gustav Klimt", "Edgar Degas", "Paul Gauguin"], "Edvard Munch",
   "Munch fez várias versões da obra a partir de 1893.",
   "Museu Munch (Oslo)", syn=["munch"])
mc(A, "pintura", 3, 14, "Qual pintura renascentista, num convento de Milão, mostra Jesus e os apóstolos à mesa?",
   ["A Última Ceia", "A Criação de Adão", "O Nascimento de Vênus", "A Escola de Atenas"], "A Última Ceia",
   "Leonardo da Vinci a pintou na parede do refeitório de Santa Maria delle Grazie.",
   "UNESCO – Santa Maria delle Grazie with 'The Last Supper'", syn=["ultima ceia", "santa ceia"])
mc(A, "arte urbana", 3, 14, "Qual artista de rua britânico mantém sua identidade em segredo?",
   ["Banksy", "Keith Haring", "Andy Warhol", "Jean-Michel Basquiat"], "Banksy",
   "Uma obra de Banksy se autodestruiu parcialmente logo após ser leiloada, em 2018.",
   "Enciclopédia Britannica – verbete 'Banksy'")
mc(A, "arquitetura", 4, 16, "Qual arquiteta projetou o MASP, com seu famoso vão livre na Avenida Paulista?",
   ["Lina Bo Bardi", "Tomie Ohtake", "Zaha Hadid", "Lygia Clark"], "Lina Bo Bardi",
   "O prédio do MASP foi inaugurado em 1968.",
   "MASP – Edifício", syn=["lina"], br=True)

# =========================================================== MITOLOGIA E LENDAS
Y = "mit"
mc(Y, "criaturas", 1, 6, "Qual criatura lendária parece um cavalo e tem um chifre na testa?",
   ["Unicórnio", "Dragão", "Grifo", "Sereia"], "Unicórnio",
   "O unicórnio aparece em lendas da Europa e da Ásia há milhares de anos.",
   "Enciclopédia Britannica – verbete 'unicorn'", syn=["unicornio"])
mc(Y, "criaturas", 1, 6, "Qual criatura lendária tem asas e cospe fogo?",
   ["Dragão", "Unicórnio", "Fada", "Duende"], "Dragão",
   "Dragões aparecem em lendas de muitos povos, da China à Europa.",
   "Enciclopédia Britannica – verbete 'dragon'", syn=["dragao"])
mc(Y, "criaturas", 1, 6, "Qual ser mágico das histórias tem asas pequenas e uma varinha de condão?",
   ["Fada", "Bruxa", "Gigante", "Ogro"], "Fada",
   "Uma fada famosa é a Sininho, de 'Peter Pan'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro")
mc(Y, "criaturas", 1, 6, "Qual ser lendário vive no mar e tem metade do corpo de peixe?",
   ["Sereia", "Centauro", "Fênix", "Grifo"], "Sereia",
   "O centauro é metade cavalo; o grifo mistura águia e leão.",
   "Enciclopédia Britannica – verbete 'mermaid'")
mc(Y, "lendas brasileiras", 1, 8, "Qual lenda brasileira fala de uma mulher transformada em mula que solta fogo pelo pescoço?",
   ["Mula sem cabeça", "Cuca", "Iara", "Boitatá"], "Mula sem cabeça",
   "A lenda é contada em várias regiões do Brasil.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", br=True)
mc(Y, "mitologia grega", 1, 9, "Qual é o nome do cavalo alado da mitologia grega?",
   ["Pégaso", "Cérbero", "Quimera", "Minotauro"], "Pégaso",
   "Pégaso ajudou o herói Belerofonte a vencer a Quimera.",
   "Enciclopédia Britannica – verbete 'Pegasus'", syn=["pegaso"])
mc(Y, "mitologia grega", 1, 9, "Qual herói grego realizou os famosos 12 trabalhos?",
   ["Hércules", "Aquiles", "Perseu", "Ulisses"], "Hércules",
   "Os gregos o chamavam de Héracles; Hércules é o nome romano.",
   "Enciclopédia Britannica – verbete 'Heracles'", syn=["heracles", "hercules"])
mc(Y, "criaturas", 1, 9, "Qual ave mitológica renasce das próprias cinzas?",
   ["Fênix", "Grifo", "Harpia", "Pégaso"], "Fênix",
   "A fênix é símbolo de renascimento e esperança.",
   "Enciclopédia Britannica – verbete 'phoenix'", syn=["fenix"])
mc(Y, "mitologia grega", 1, 10, "Na mitologia grega, quem é o rei dos deuses, senhor dos raios?",
   ["Zeus", "Hades", "Apolo", "Ares"], "Zeus",
   "Zeus governava o Olimpo; seus irmãos Poseidon e Hades reinavam nos mares e no submundo.",
   "Enciclopédia Britannica – verbete 'Zeus'")
mc(Y, "mitologia grega", 1, 10, "Qual deus grego dos mares carrega um tridente?",
   ["Poseidon", "Zeus", "Hermes", "Dionísio"], "Poseidon",
   "Para os romanos, ele era Netuno.",
   "Enciclopédia Britannica – verbete 'Poseidon'", syn=["posseidon", "netuno"])
mc(Y, "mitologia nórdica", 1, 10, "Na mitologia nórdica, qual deus empunha o martelo Mjölnir?",
   ["Thor", "Odin", "Loki", "Freyr"], "Thor",
   "Thor é o deus do trovão; a quinta-feira em inglês, 'Thursday', vem do nome dele.",
   "Enciclopédia Britannica – verbete 'Thor'")
mc(Y, "mitologia grega", 1, 10, "Qual criatura grega tinha serpentes no lugar dos cabelos e transformava em pedra quem a olhasse?",
   ["Medusa", "Hidra", "Esfinge", "Harpia"], "Medusa",
   "O herói Perseu a venceu olhando seu reflexo num escudo.",
   "Enciclopédia Britannica – verbete 'Medusa'")
mc(Y, "Guerra de Troia", 1, 10, "Que truque os gregos usaram para entrar na cidade de Troia?",
   ["Um cavalo de madeira", "Um túnel subterrâneo", "Uma ponte de cordas", "Um disfarce de pastores"],
   "Um cavalo de madeira",
   "Soldados escondidos dentro do cavalo abriram os portões à noite.",
   "Virgílio – Eneida, Livro II", syn=["cavalo de troia", "cavalo"])
mc(Y, "mitologia grega", 1, 10, "Em qual monte viviam os deuses gregos?",
   ["Olimpo", "Everest", "Vesúvio", "Sinai"], "Olimpo",
   "O Monte Olimpo é a montanha mais alta da Grécia, com cerca de 2.900 metros.",
   "Enciclopédia Britannica – verbete 'Mount Olympus'", syn=["monte olimpo"])
mc(Y, "lendas", 2, 10, "Qual monstro lendário viveria num lago da Escócia?",
   ["Nessie", "Pé-Grande", "Chupa-cabra", "Iéti"], "Nessie",
   "Nessie é o apelido do suposto Monstro do Lago Ness; nunca houve prova da sua existência.",
   "Enciclopédia Britannica – verbete 'Loch Ness monster'", syn=["monstro do lago ness", "lago ness"])
mc(Y, "lendas brasileiras", 2, 10, "Qual personagem do folclore amazônico vira um rapaz bonito nas festas para encantar as moças?",
   ["Boto cor-de-rosa", "Curupira", "Saci-Pererê", "Mapinguari"], "Boto cor-de-rosa",
   "Na lenda, o boto usa chapéu para esconder o furinho de respirar na cabeça.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=["boto", "boto rosa"], br=True)
mc(Y, "lendas brasileiras", 2, 10, "Qual criatura do folclore brasileiro é uma cobra de fogo que protege os campos?",
   ["Boitatá", "Iara", "Cuca", "Lobisomem"], "Boitatá",
   "O nome vem do tupi: 'cobra de fogo'.",
   "Câmara Cascudo – Dicionário do Folclore Brasileiro", syn=["boitata"], br=True)
mc(Y, "mitologia grega", 2, 12, "Qual é o nome da deusa grega da sabedoria?",
   ["Atena", "Afrodite", "Hera", "Ártemis"], "Atena",
   "A cidade de Atenas leva o nome dela, e a coruja é seu símbolo.",
   "Enciclopédia Britannica – verbete 'Athena'", syn=["athena"])
mc(Y, "mitologia grega", 2, 12, "Qual herói grego era invulnerável, exceto no calcanhar?",
   ["Aquiles", "Hércules", "Teseu", "Jasão"], "Aquiles",
   "Daí vem a expressão 'calcanhar de Aquiles' para um ponto fraco.",
   "Enciclopédia Britannica – verbete 'Achilles'")
mc(Y, "mitologia grega", 2, 12, "Qual criatura, metade homem e metade touro, vivia no labirinto de Creta?",
   ["Minotauro", "Centauro", "Ciclope", "Sátiro"], "Minotauro",
   "O labirinto teria sido construído por Dédalo para o rei Minos.",
   "Enciclopédia Britannica – verbete 'Minotaur'")
mc(Y, "mitologia romana", 2, 12, "Quem era o rei dos deuses na mitologia romana?",
   ["Júpiter", "Marte", "Mercúrio", "Saturno"], "Júpiter",
   "Os romanos adaptaram muitos deuses gregos: Júpiter equivale a Zeus.",
   "Enciclopédia Britannica – verbete 'Jupiter (Roman god)'", syn=["jupiter"])
mc(Y, "mitologia grega", 2, 12, "Na mitologia grega, quem é o deus do mundo dos mortos?",
   ["Hades", "Ares", "Apolo", "Hermes"], "Hades",
   "Hades era guardado pelo cão de três cabeças, Cérbero.",
   "Enciclopédia Britannica – verbete 'Hades'")
mc(Y, "mitologia grega", 2, 12, "O que Pandora abriu, liberando os males do mundo?",
   ["Uma caixa", "Uma porta", "Um livro", "Uma janela"], "Uma caixa",
   "No mito original era um jarro; só a esperança ficou lá dentro.",
   "Hesíodo – Os Trabalhos e os Dias", syn=["caixa", "jarro", "a caixa de pandora"])
mc(Y, "mitologia nórdica", 2, 12, "Qual deus nórdico é famoso por ser trapaceiro e mudar de forma?",
   ["Loki", "Thor", "Odin", "Balder"], "Loki",
   "Loki causa confusão entre os deuses de Asgard.",
   "Enciclopédia Britannica – verbete 'Loki'")
mc(Y, "mitologia egípcia", 2, 12, "Qual deus egípcio do Sol era um dos mais importantes do Egito antigo?",
   ["Rá", "Osíris", "Seth", "Anúbis"], "Rá",
   "Rá atravessaria o céu num barco durante o dia.",
   "Enciclopédia Britannica – verbete 'Re'", syn=["ra"])
mc(Y, "lendas", 3, 12, "Como se chama o gigante peludo lendário das montanhas do Himalaia?",
   ["Iéti", "Pé-Grande", "Nessie", "Kraken"], "Iéti",
   "Também chamado de 'abominável homem das neves'.",
   "Enciclopédia Britannica – verbete 'Yeti'", syn=["yeti", "abominavel homem das neves"])
mc(Y, "mitologia grega", 3, 14, "Qual titã grego foi castigado a segurar o céu nos ombros?",
   ["Atlas", "Cronos", "Prometeu", "Oceano"], "Atlas",
   "Por isso coleções de mapas são chamadas de 'atlas'.",
   "Enciclopédia Britannica – verbete 'Atlas'")
mc(Y, "mitologia grega", 3, 14, "Qual titã roubou o fogo dos deuses para dar aos humanos?",
   ["Prometeu", "Atlas", "Cronos", "Hipérion"], "Prometeu",
   "Como castigo, foi acorrentado a uma rocha, onde uma águia comia seu fígado.",
   "Hesíodo – Teogonia")
mc(Y, "mitologia egípcia", 3, 14, "Na mitologia egípcia, qual deus tem cabeça de chacal e protege os mortos?",
   ["Anúbis", "Hórus", "Rá", "Osíris"], "Anúbis",
   "Anúbis era associado à mumificação.",
   "Enciclopédia Britannica – verbete 'Anubis'", syn=["anubis"])
mc(Y, "mitologia nórdica", 3, 14, "Na mitologia nórdica, como se chama o salão que recebe os guerreiros mortos em batalha?",
   ["Valhala", "Olimpo", "Asgard", "Tártaro"], "Valhala",
   "Valhala fica em Asgard e é governado por Odin.",
   "Enciclopédia Britannica – verbete 'Valhalla'", syn=["valhalla"])
mc(Y, "mitologia grega", 3, 14, "Qual herói grego usou um novelo de linha, dado por Ariadne, para sair do labirinto de Creta?",
   ["Teseu", "Perseu", "Jasão", "Aquiles"], "Teseu",
   "Teseu enfrentou a criatura do labirinto e voltou seguindo o fio.",
   "Plutarco – Vida de Teseu")
mc(Y, "Guerra de Troia", 3, 14, "Qual herói grego leva dez anos para voltar para casa na 'Odisseia', de Homero?",
   ["Ulisses", "Aquiles", "Heitor", "Páris"], "Ulisses",
   "Em grego, ele se chama Odisseu, e sua esposa Penélope o espera em Ítaca.",
   "Homero – Odisseia", syn=["odisseu"])
mc(Y, "mitologia grega", 3, 14, "Qual deus grego do amor era representado com arco e flechas (o Cupido dos romanos)?",
   ["Eros", "Apolo", "Hermes", "Dionísio"], "Eros",
   "As flechas de Eros faziam as pessoas se apaixonarem.",
   "Enciclopédia Britannica – verbete 'Eros'")
