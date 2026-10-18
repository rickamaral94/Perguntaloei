# Perguntas novas: matemática. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "mat"

# ============================================================ FÁCEIS
mc(T, "contagem", 1, 6, "Um cachorro tem quatro patas. Quantas patas têm, ao todo, dois cachorros?",
   ["8", "6", "4", "10"], "8",
   "Quatro patas mais quatro patas dão oito patas.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "contagem", 1, 6, "Contando os dedos das mãos e dos pés, quantos dedos uma pessoa tem ao todo?",
   ["20", "10", "15", "25"], "20",
   "São dez dedos nas mãos e dez nos pés, somando vinte.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "subtração", 1, 6, "Num prato havia sete morangos e Lucas comeu dois. Quantos morangos sobraram?",
   ["5", "4", "6", "9"], "5",
   "Sete menos dois é igual a cinco.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "adição", 1, 6, "Num ninho há três ovos azuis e dois ovos brancos. Quantos ovos há no ninho?",
   ["5", "4", "6", "3"], "5",
   "Três mais dois é igual a cinco.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "formas geométricas", 1, 6, "Quantos cantos tem um quadrado?",
   ["4", "3", "5", "6"], "4",
   "O quadrado tem quatro lados e quatro cantos, que na matemática se chamam vértices.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
op(T, "números", 1, 6, "Na contagem, qual número fica entre o seis e o oito?", "7",
   ["7", "sete"],
   "Contando seis, sete, oito, o sete fica no meio.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
tf(T, "formas geométricas", 1, 7, "Um triângulo tem quatro vértices.", False,
   "O triângulo tem três lados e três vértices, que são as pontas onde os lados se encontram.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
mc(T, "dobro e metade", 1, 7, "Marina tem três bonecas e sua prima tem o dobro. Quantas bonecas tem a prima?",
   ["6", "5", "9", "4"], "6",
   "O dobro de três é três mais três, que dá seis.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
mc(T, "par e ímpar", 1, 7, "Qual destes números é ímpar?",
   ["7", "4", "10", "12"], "7",
   "O sete não pode ser dividido em dois grupos iguais, por isso é ímpar.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
mc(T, "adição", 1, 7, "Uma bicicleta tem duas rodas e um triciclo tem três. Quantas rodas há nos dois juntos?",
   ["5", "4", "6", "7"], "5",
   "Duas rodas mais três rodas dão cinco rodas.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "sólidos geométricos", 1, 7, "Qual destes objetos tem a forma de um cone?",
   ["Casquinha de sorvete", "Bola de futebol", "Caixa de sapato", "Lata de milho"], "Casquinha de sorvete",
   "O cone tem uma base redonda e termina em uma ponta, como a casquinha de sorvete.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
op(T, "contagem", 1, 7, "Quantas rodas tem um carro comum de passeio, sem contar o estepe?", "4",
   ["4", "quatro"],
   "Um carro de passeio anda sobre quatro rodas; o estepe é a roda de reserva.",
   "Base Nacional Comum Curricular – Matemática, 1º ano")
mc(T, "sólidos geométricos", 1, 8, "Um dado de jogo tem o formato de qual sólido geométrico?",
   ["Cubo", "Esfera", "Cilindro", "Cone"], "Cubo",
   "O dado comum é um cubo, com seis faces quadradas numeradas de um a seis.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
mc(T, "sólidos geométricos", 1, 8, "Uma lata de refrigerante lembra qual sólido geométrico?",
   ["Cilindro", "Cubo", "Pirâmide", "Esfera"], "Cilindro",
   "O cilindro tem duas bases redondas e uma lateral curva, como uma lata.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
mc(T, "medidas", 1, 8, "Qual unidade de medida usamos para dizer quanto leite cabe numa caixinha?",
   ["Litro", "Metro", "Quilo", "Hora"], "Litro",
   "O litro mede capacidade, ou seja, quanto de líquido cabe num recipiente.",
   "Inmetro – Sistema Internacional de Unidades")
mc(T, "dinheiro", 1, 8, "Bia tem uma moeda de um real e uma moeda de cinquenta centavos. Quanto dinheiro ela tem?",
   ["Um real e cinquenta centavos", "Cinquenta e um centavos", "Dois reais", "Um real e cinco centavos"],
   "Um real e cinquenta centavos",
   "Um real mais cinquenta centavos dá um real e cinquenta centavos.",
   "Banco Central do Brasil – Moedas do Real", br=True)
mc(T, "dinheiro", 1, 8, "Quem tem duas notas de dez reais e uma nota de cinco reais tem quanto dinheiro?",
   ["25 reais", "20 reais", "15 reais", "30 reais"], "25 reais",
   "Dez mais dez dá vinte, e mais cinco dá vinte e cinco reais.",
   "Banco Central do Brasil – Cédulas do Real", br=True)
mc(T, "dinheiro", 1, 8, "Quantas moedas de vinte e cinco centavos são necessárias para formar um real?",
   ["4", "2", "5", "10"], "4",
   "Quatro vezes vinte e cinco centavos dá cem centavos, que é um real.",
   "Banco Central do Brasil – Moedas do Real", br=True)
mc(T, "frações", 1, 8, "Uma pizza foi cortada em quatro pedaços iguais. Cada pedaço é que parte da pizza?",
   ["Um quarto", "Um meio", "Um terço", "Um oitavo"], "Um quarto",
   "Quando o inteiro é dividido em quatro partes iguais, cada parte é um quarto.",
   "Base Nacional Comum Curricular – Matemática, 3º ano")
tf(T, "medidas de tempo", 1, 8, "Um minuto tem cem segundos.", False,
   "Um minuto tem sessenta segundos, e uma hora tem sessenta minutos.",
   "Inmetro – Sistema Internacional de Unidades")
mc(T, "dobro e metade", 1, 9, "Dois irmãos dividiram igualmente dezoito figurinhas. Com quantas figurinhas ficou cada um?",
   ["9", "8", "6", "10"], "9",
   "Dividir dezoito em duas partes iguais dá nove para cada um.",
   "Base Nacional Comum Curricular – Matemática, 3º ano")
mc(T, "adição", 1, 9, "Num ônibus havia nove passageiros e subiram mais seis. Quantos passageiros há agora?",
   ["15", "14", "16", "13"], "15",
   "Nove mais seis é igual a quinze.",
   "Base Nacional Comum Curricular – Matemática, 2º ano")
op(T, "números romanos", 1, 9, "Na numeração romana, que número se forma com três letras I seguidas?", "3",
   ["3", "três", "tres"],
   "Na numeração romana, cada letra I vale um, e três delas juntas valem três.",
   "Enciclopédia Britannica – verbete 'Roman numeral'")
tf(T, "formas geométricas", 1, 9, "Um retângulo tem quatro vértices.", True,
   "O retângulo tem quatro lados e quatro vértices, todos com ângulos retos.",
   "Base Nacional Comum Curricular – Matemática, 3º ano")
mc(T, "medidas de tempo", 1, 9, "Quantas horas há em dois dias inteiros?",
   ["48", "24", "36", "60"], "48",
   "Cada dia tem vinte e quatro horas, e duas vezes vinte e quatro dá quarenta e oito.",
   "Observatório Nacional – Hora Legal Brasileira")
mc(T, "medidas de tempo", 1, 9, "Quantas semanas completas cabem em vinte e oito dias?",
   ["4", "3", "5", "7"], "4",
   "Cada semana tem sete dias, e quatro vezes sete dá vinte e oito.",
   "Base Nacional Comum Curricular – Matemática, 3º ano")
tf(T, "medidas", 1, 9, "Um metro é maior que um quilômetro.", False,
   "Um quilômetro tem mil metros, então é muito maior que um metro.",
   "Inmetro – Sistema Internacional de Unidades")

# ============================================================ MÉDIAS
mc(T, "sólidos geométricos", 2, 10, "Quantos vértices tem uma pirâmide de base quadrada?",
   ["5", "4", "6", "8"], "5",
   "São quatro vértices na base quadrada e mais um na ponta de cima.",
   "Base Nacional Comum Curricular – Matemática, 5º ano")
mc(T, "formas geométricas", 2, 10, "Como se chama o polígono que tem cinco lados?",
   ["Pentágono", "Hexágono", "Heptágono", "Octógono"], "Pentágono",
   "O prefixo grego 'penta' significa cinco, como em pentacampeão.",
   "Enciclopédia Britannica – verbete 'Pentagon'")
mc(T, "dinheiro", 2, 10, "Carla comprou um lanche de doze reais e um suco de sete reais e pagou com uma nota de vinte. Quanto recebeu de troco?",
   ["1 real", "2 reais", "3 reais", "8 reais"], "1 real",
   "Doze mais sete dá dezenove reais, e vinte menos dezenove deixa um real de troco.",
   "Base Nacional Comum Curricular – Matemática, 4º ano", syn=("um real",), br=True)
mc(T, "dinheiro", 2, 9, "Qual destes valores NÃO existe como moeda do real?",
   ["30 centavos", "5 centavos", "10 centavos", "50 centavos"], "30 centavos",
   "As moedas do real são de um, cinco, dez, vinte e cinco e cinquenta centavos, além da de um real.",
   "Banco Central do Brasil – Moedas do Real", br=True)
tf(T, "dinheiro", 2, 10, "Uma nota de cem reais vale o mesmo que cinco notas de vinte reais.", True,
   "Cinco vezes vinte reais dá exatamente cem reais.",
   "Banco Central do Brasil – Cédulas do Real", br=True)
tf(T, "medidas", 2, 10, "Um quilograma equivale a mil gramas.", True,
   "O prefixo 'quilo' significa mil, por isso um quilograma tem mil gramas.",
   "Inmetro – Sistema Internacional de Unidades")
mc(T, "frações", 2, 10, "Uma barra de chocolate tem doze quadradinhos. Quantos quadradinhos há em um terço da barra?",
   ["4", "3", "6", "9"], "4",
   "Um terço de doze é doze dividido por três, que dá quatro.",
   "Base Nacional Comum Curricular – Matemática, 4º ano")
mc(T, "multiplicação", 2, 10, "Uma caixa tem seis fileiras com nove bombons em cada uma. Quantos bombons há na caixa?",
   ["54", "45", "56", "63"], "54",
   "Seis vezes nove é igual a cinquenta e quatro.",
   "Base Nacional Comum Curricular – Matemática, 4º ano")
mc(T, "medidas de tempo", 2, 10, "Que horas serão quinze minutos depois das dez e cinquenta?",
   ["Onze e cinco", "Dez e cinco", "Onze e quinze", "Onze e meia"], "Onze e cinco",
   "Dez minutos levam às onze horas, e os cinco que faltam levam às onze e cinco.",
   "Base Nacional Comum Curricular – Matemática, 4º ano")
op(T, "multiplicação", 2, 10, "Uma aranha tem oito patas. Quantas patas têm, juntas, três aranhas?", "24",
   ["24", "vinte e quatro"],
   "Três vezes oito é igual a vinte e quatro.",
   "Base Nacional Comum Curricular – Matemática, 3º ano")
tf(T, "sólidos geométricos", 2, 10, "Uma esfera tem vértices e arestas.", False,
   "A esfera é totalmente arredondada e não tem nenhuma aresta nem vértice.",
   "Base Nacional Comum Curricular – Matemática, 5º ano")
mc(T, "multiplicação", 2, 9, "Num estacionamento há três carros e cinco motos. Quantas rodas há ao todo?",
   ["22", "16", "20", "32"], "22",
   "Os carros somam doze rodas e as motos somam dez, num total de vinte e duas.",
   "Base Nacional Comum Curricular – Matemática, 4º ano")
mc(T, "problemas de tempo", 2, 10, "A Copa do Mundo de futebol acontece de quatro em quatro anos. Se houve Copa em 2014, em qual destes anos também houve?",
   ["2022", "2020", "2021", "2016"], "2022",
   "Somando quatro anos a 2014 chega-se a 2018 e, depois, a 2022.",
   "FIFA – FIFA World Cup", br=True)
mc(T, "médias", 2, 12, "Um time fez dois gols no primeiro jogo, quatro no segundo e nenhum no terceiro. Qual foi a média de gols por jogo?",
   ["2", "3", "4", "6"], "2",
   "O total é seis gols em três jogos, e seis dividido por três dá dois.",
   "Base Nacional Comum Curricular – Matemática, 6º ano")
mc(T, "perímetro", 2, 12, "Qual é o perímetro de um quadrado com sete centímetros de lado?",
   ["28 centímetros", "14 centímetros", "21 centímetros", "49 centímetros"], "28 centímetros",
   "O perímetro soma os quatro lados: quatro vezes sete dá vinte e oito.",
   "Base Nacional Comum Curricular – Matemática, 5º ano")
mc(T, "ângulos", 2, 12, "Como se chama o ângulo que mede menos de noventa graus?",
   ["Agudo", "Obtuso", "Reto", "Raso"], "Agudo",
   "Ângulos menores que o reto são agudos; os maiores que o reto e menores que o raso são obtusos.",
   "Base Nacional Comum Curricular – Matemática, 6º ano")
mc(T, "porcentagem", 2, 12, "Num grupo de cinquenta crianças, vinte por cento gostam de jiló. Quantas crianças são?",
   ["10", "20", "5", "25"], "10",
   "Dez por cento de cinquenta é cinco, então vinte por cento é dez.",
   "Base Nacional Comum Curricular – Matemática, 6º ano")
mc(T, "problemas de idade", 2, 12, "Lucas tem oito anos e sua mãe tem o quádruplo da idade dele. Quantos anos tem a mãe?",
   ["32", "24", "36", "40"], "32",
   "O quádruplo é quatro vezes: quatro vezes oito dá trinta e dois.",
   "Base Nacional Comum Curricular – Matemática, 5º ano")
mc(T, "formas geométricas", 2, 12, "Como se chama o ponto onde dois lados de um polígono se encontram?",
   ["Vértice", "Aresta", "Diagonal", "Raio"], "Vértice",
   "Os vértices são os 'cantos' do polígono, onde um lado termina e outro começa.",
   "Base Nacional Comum Curricular – Matemática, 6º ano")
mc(T, "números romanos", 2, 12, "Na numeração romana, qual letra vale mil?",
   ["M", "D", "C", "L"], "M",
   "Na numeração romana, M vale mil, D vale quinhentos, C vale cem e L vale cinquenta.",
   "Enciclopédia Britannica – verbete 'Roman numeral'")
tf(T, "números romanos", 2, 12, "A numeração romana não tem um símbolo para o zero.", True,
   "Os romanos não tinham um algarismo para o zero; ele chegou à Europa com os algarismos indo-arábicos.",
   "Enciclopédia Britannica – verbete 'Roman numeral'")
tf(T, "matemáticos famosos", 2, 12, "Pitágoras foi um matemático da Roma Antiga.", False,
   "Pitágoras era grego, nascido na ilha de Samos, no século VI antes de Cristo.",
   "Enciclopédia Britannica – verbete 'Pythagoras'")

# ============================================================ DIFÍCEIS
mc(T, "matemáticos famosos", 3, 12, "Qual livro famoso foi escrito pelo professor brasileiro Malba Tahan?",
   ["O Homem que Calculava", "O Pequeno Príncipe", "Alice no País das Maravilhas", "O Menino Maluquinho"],
   "O Homem que Calculava",
   "O livro, de 1938, conta as aventuras de Beremiz Samir, que resolve problemas com a matemática.",
   "Enciclopédia Itaú Cultural – verbete 'Malba Tahan'", br=True)
mc(T, "matemáticos famosos", 3, 14, "O Dia Nacional da Matemática, em 6 de maio, homenageia o nascimento de qual escritor brasileiro?",
   ["Malba Tahan", "Monteiro Lobato", "Machado de Assis", "Ziraldo"], "Malba Tahan",
   "A Lei 12.835, de 2013, escolheu o dia em que nasceu Júlio César de Mello e Souza, o Malba Tahan.",
   "Lei nº 12.835/2013", br=True)
mc(T, "matemáticos famosos", 3, 14, "Qual matemático brasileiro ganhou a Medalha Fields, o maior prêmio da matemática, em 2014?",
   ["Artur Avila", "César Lattes", "Oswaldo Cruz", "Carlos Chagas"], "Artur Avila",
   "Artur Avila foi o primeiro latino-americano a receber a Medalha Fields.",
   "União Matemática Internacional – Fields Medal 2014", br=True)
mc(T, "matemática no Brasil", 3, 16, "O que significa a sigla IMPA, instituto de pesquisa em matemática no Rio de Janeiro?",
   ["Instituto de Matemática Pura e Aplicada", "Instituto Municipal de Probabilidade Avançada",
    "Instituto de Medidas e Padrões Aritméticos", "Instituto Moderno de Problemas Algébricos"],
   "Instituto de Matemática Pura e Aplicada",
   "O IMPA foi criado em 1952 e é referência internacional em pesquisa matemática.",
   "IMPA – Instituto de Matemática Pura e Aplicada", br=True)
mc(T, "problemas de tempo", 3, 12, "A Independência do Brasil foi em 1822 e a Proclamação da República, em 1889. Quantos anos se passaram entre as duas?",
   ["67", "57", "77", "63"], "67",
   "Mil oitocentos e oitenta e nove menos mil oitocentos e vinte e dois dá sessenta e sete.",
   "Arquivo Nacional", br=True)
mc(T, "dinheiro", 2, 9, "Qual é a cédula de maior valor do real?",
   ["200 reais", "100 reais", "500 reais", "1.000 reais"], "200 reais",
   "A nota de duzentos reais, com o lobo-guará, foi lançada em 2020.",
   "Banco Central do Brasil – Cédulas do Real", br=True, ref="2026-10-13")
op(T, "sequências", 3, 14, "Qual matemático italiano dá nome à sequência um, um, dois, três, cinco, oito, treze?", "Fibonacci",
   ["fibonacci", "leonardo fibonacci", "leonardo de pisa"],
   "Leonardo de Pisa, o Fibonacci, apresentou essa sequência em seu livro 'Liber Abaci', de 1202.",
   "Enciclopédia Britannica – verbete 'Fibonacci'")
tf(T, "matemáticos famosos", 3, 14, "Hipátia de Alexandria foi uma matemática e filósofa da Antiguidade.", True,
   "Hipátia ensinou matemática e filosofia em Alexandria, no Egito, por volta do ano 400.",
   "Enciclopédia Britannica – verbete 'Hypatia'")
mc(T, "matemáticos famosos", 3, 14, "Qual sábio grego calculou uma boa aproximação do número pi usando polígonos dentro e fora de um círculo?",
   ["Arquimedes", "Euclides", "Pitágoras", "Tales"], "Arquimedes",
   "Arquimedes mostrou que pi fica entre três inteiros e dez setenta e um avos e três inteiros e um sétimo.",
   "Enciclopédia Britannica – verbete 'Archimedes'")
tf(T, "par e ímpar", 3, 12, "Zero é um número par.", True,
   "Zero dividido por dois dá zero, sem resto, por isso ele é par.",
   "Enciclopédia Britannica – verbete 'parity'")
mc(T, "problemas de idade", 3, 12, "Uma mãe tem trinta anos e o filho tem seis. Daqui a quantos anos a mãe terá o triplo da idade do filho?",
   ["6", "4", "8", "12"], "6",
   "Daqui a seis anos a mãe terá trinta e seis e o filho doze, e trinta e seis é o triplo de doze.",
   "Base Nacional Comum Curricular – Matemática, 7º ano")
op(T, "medidas de tempo", 3, 12, "Quantos minutos há em um dia inteiro?", "1.440",
   ["1440", "1.440", "mil quatrocentos e quarenta"],
   "Vinte e quatro horas vezes sessenta minutos dá mil quatrocentos e quarenta minutos.",
   "Observatório Nacional – Hora Legal Brasileira")
tf(T, "ângulos", 3, 12, "Um ângulo raso mede noventa graus.", False,
   "O ângulo raso mede cento e oitenta graus, como uma linha reta; o de noventa é o reto.",
   "Base Nacional Comum Curricular – Matemática, 6º ano")

# ============================================================ MUITO DIFÍCEIS
mc(T, "matemáticos famosos", 4, 14, "Segundo uma história famosa, o menino Gauss somou rapidamente todos os números de um a cem. Qual é o resultado?",
   ["5.050", "5.000", "10.100", "4.950"], "5.050",
   "Juntando um com cem, dois com noventa e nove e assim por diante, formam-se cinquenta pares de cento e um.",
   "Enciclopédia Britannica – verbete 'Carl Friedrich Gauss'", syn=("5050",))
mc(T, "raciocínio lógico", 4, 14, "Cinco pessoas se cumprimentam e cada uma aperta a mão de todas as outras uma única vez. Quantos apertos de mão acontecem?",
   ["10", "20", "25", "15"], "10",
   "Cada pessoa aperta quatro mãos, o que daria vinte, mas cada aperto envolve duas pessoas, então são dez.",
   "Base Nacional Comum Curricular – Matemática, 8º ano")
tf(T, "números primos", 4, 16, "Existem infinitos números primos.", True,
   "Euclides demonstrou, há mais de dois mil anos, que a lista dos números primos nunca termina.",
   "Enciclopédia Britannica – verbete 'prime'")
mc(T, "raciocínio lógico", 4, 14, "Um caracol sobe três metros de um poço durante o dia e escorrega dois à noite. Se o poço tem dez metros, em quantos dias ele chega à borda?",
   ["8", "10", "7", "9"], "8",
   "Em sete dias ele avança sete metros e, no oitavo dia, sobe os três que faltam e chega à borda.",
   "Base Nacional Comum Curricular – Matemática, 7º ano")
op(T, "potências", 4, 14, "Qualquer número diferente de zero elevado a zero dá qual resultado?", "1",
   ["1", "um"],
   "Por definição, todo número diferente de zero elevado a zero é igual a um.",
   "Enciclopédia Britannica – verbete 'exponent'")
mc(T, "raciocínio lógico", 4, 14, "Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?",
   ["2 quilos", "1 quilo e meio", "1 quilo", "3 quilos"], "2 quilos",
   "Se meio tijolo mais um quilo é o tijolo todo, então a outra metade pesa um quilo, e o tijolo pesa dois.",
   "Base Nacional Comum Curricular – Matemática, 7º ano", syn=("dois quilos",))
