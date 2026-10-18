# Perguntas novas: tecnologia. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "tec"

# =========================================================== FÁCEIS
mc(T, "transportes", 1, 6, "Qual meio de transporte anda sobre trilhos e puxa vários vagões?",
   ["Trem", "Ônibus", "Navio", "Helicóptero"], "Trem",
   "O trem é formado por uma locomotiva que puxa vagões de passageiros ou de carga sobre trilhos de ferro.",
   "Enciclopédia Britannica – verbete 'Railroad'")
mc(T, "transportes", 1, 6, "Qual veículo voa com uma grande hélice girando no teto?",
   ["Helicóptero", "Avião a jato", "Foguete", "Planador"], "Helicóptero",
   "A hélice de cima do helicóptero, chamada de rotor, permite subir em linha reta e até ficar parado no ar.",
   "Enciclopédia Britannica – verbete 'Helicopter'")
tf(T, "aparelhos de casa", 1, 6, "O ferro de passar fica quente para desamassar as roupas.", True,
   "O calor do ferro, às vezes junto com vapor, amolece as fibras do tecido e tira os amassados.",
   "Enciclopédia Britannica – verbete 'Iron (household appliance)'")
mc(T, "aparelhos de casa", 1, 6, "Qual aparelho usamos para tostar fatias de pão?",
   ["Torradeira", "Liquidificador", "Batedeira", "Geladeira"], "Torradeira",
   "A torradeira tem fios que ficam muito quentes e deixam o pão dourado e crocante.",
   "Enciclopédia Britannica – verbete 'Toaster'")
tf(T, "transportes", 1, 6, "Uma bicicleta comum anda com a força das pernas de quem pedala.", True,
   "Os pedais giram a coroa, e a corrente leva esse movimento até a roda de trás.",
   "Enciclopédia Britannica – verbete 'Bicycle'")
tf(T, "transportes", 1, 6, "O navio é um veículo que anda sobre trilhos.", False,
   "O navio navega na água, flutuando sobre rios, mares e oceanos; quem anda em trilhos é o trem.",
   "Enciclopédia Britannica – verbete 'Ship'")
mc(T, "aparelhos de casa", 1, 7, "Qual aparelho da casa limpa o chão sugando a poeira?",
   ["Aspirador de pó", "Ventilador", "Secador", "Ferro de passar"], "Aspirador de pó",
   "O motor do aspirador cria uma sucção que puxa a sujeira para dentro de um saco ou reservatório.",
   "Enciclopédia Britannica – verbete 'Vacuum cleaner'")
mc(T, "transportes", 1, 7, "Qual veículo anda debaixo da água, como os que exploram o fundo do mar?",
   ["Submarino", "Navio", "Jangada", "Lancha"], "Submarino",
   "O submarino enche e esvazia tanques com água para afundar e voltar à superfície.",
   "Enciclopédia Britannica – verbete 'Submarine'")
mc(T, "transportes", 1, 7, "Como se chama o trem que anda debaixo da terra nas grandes cidades?",
   ["Metrô", "Bonde", "Teleférico", "Ônibus"], "Metrô",
   "O metrô corre em túneis, em linhas próprias, e por isso não pega o trânsito das ruas.",
   "Enciclopédia Britannica – verbete 'Subway'")
op(T, "computador", 1, 7, "Qual aparelho ligado ao computador tem botões e uma rodinha e move a setinha na tela?",
   "Mouse", ["mouse", "rato"],
   "O nome vem do inglês e quer dizer 'camundongo', porque os primeiros modelos tinham um fio parecido com um rabinho.",
   "Enciclopédia Britannica – verbete 'Mouse (computing)'")
mc(T, "comunicação", 1, 7, "Qual aparelho tem programas de música e notícias, mas só tem som e não tem imagem?",
   ["Rádio", "Televisão", "Computador", "Projetor"], "Rádio",
   "O rádio recebe ondas eletromagnéticas e as transforma em som pelo alto-falante.",
   "Enciclopédia Britannica – verbete 'Radio'")
tf(T, "aparelhos de casa", 1, 7, "A geladeira gela melhor quando fica com a porta aberta.", False,
   "Com a porta aberta entra ar quente, e a geladeira gasta mais energia para voltar a esfriar.",
   "Procel – dicas de economia de energia")
tf(T, "segurança na internet", 1, 7, "É seguro ir encontrar alguém que conhecemos só pela internet sem avisar nossos pais.", False,
   "Na internet, uma pessoa pode mentir sobre quem é; por isso as crianças devem sempre contar a um adulto de confiança.",
   "SaferNet Brasil – dicas de segurança para crianças", br=True)
op(T, "transportes", 1, 7, "Como se chama o lugar onde os aviões pousam e decolam e os passageiros embarcam?",
   "Aeroporto", ["aeroporto", "aeroportos"],
   "No aeroporto ficam as pistas, a torre de controle e os portões de embarque.",
   "Enciclopédia Britannica – verbete 'Airport'")
mc(T, "computador", 1, 8, "Qual tecla do teclado é a mais comprida e coloca espaço entre as palavras?",
   ["Barra de espaço", "Enter", "Shift", "Esc"], "Barra de espaço",
   "A barra de espaço fica embaixo das letras e é apertada com o polegar.",
   "Enciclopédia Britannica – verbete 'Computer keyboard'")
mc(T, "robótica", 1, 8, "Como se chama a máquina que pode ser programada para fazer tarefas sozinha, como montar carros numa fábrica?",
   ["Robô", "Calculadora", "Telescópio", "Bússola"], "Robô",
   "Os robôs industriais soldam, pintam e montam peças, repetindo os movimentos com muita precisão.",
   "Enciclopédia Britannica – verbete 'Robot'")
mc(T, "videogames", 1, 8, "Qual personagem dos jogos da Nintendo é um dinossauro verde que carrega o Mario nas costas?",
   ["Yoshi", "Bowser", "Luigi", "Donkey Kong"], "Yoshi",
   "Yoshi estreou em 'Super Mario World' e pega os inimigos com sua língua comprida.",
   "Nintendo – personagens da série Super Mario")
mc(T, "videogames", 1, 8, "Qual é o nome do irmão do Mario, que usa boné e camisa verdes?",
   ["Luigi", "Wario", "Toad", "Link"], "Luigi",
   "Luigi é mais alto e magro que o Mario e também trabalha como encanador.",
   "Nintendo – personagens da série Super Mario")
mc(T, "internet", 1, 8, "Como se chamam as carinhas e figurinhas pequenas usadas nas mensagens, como a do sorriso?",
   ["Emojis", "Pixels", "Links", "Cursores"], "Emojis",
   "A palavra vem do japonês e junta 'e' (imagem) com 'moji' (letra).",
   "Enciclopédia Britannica – verbete 'Emoji'")
op(T, "transportes", 1, 8, "Qual veículo de duas rodas tem motor e é muito usado pelos motoboys nas entregas?",
   "Moto", ["moto", "motocicleta", "motos"],
   "A motocicleta tem motor a combustão ou elétrico e anda bem no trânsito das cidades.",
   "Enciclopédia Britannica – verbete 'Motorcycle'")
mc(T, "transportes", 1, 9, "Qual meio de transporte leva os turistas por cabos no alto até o Pão de Açúcar, no Rio de Janeiro?",
   ["Teleférico", "Metrô", "Monotrilho", "Ônibus"], "Teleférico",
   "O famoso bondinho do Pão de Açúcar, inaugurado em 1912, é um teleférico com cabines penduradas em cabos.",
   "Parque Bondinho Pão de Açúcar – história", br=True)
mc(T, "segurança na internet", 1, 9, "Como deve ser uma senha segura?",
   ["Longa, misturando letras, números e símbolos", "Igual ao nosso nome", "Só com a data de aniversário",
    "A mesma para todos os sites"], "Longa, misturando letras, números e símbolos",
   "Senhas longas e variadas são muito mais difíceis de adivinhar por pessoas ou programas.",
   "CERT.br – Cartilha de Segurança para Internet", br=True)
op(T, "comunicação", 1, 9, "Como se chamava o aparelho de teclas usado para escrever textos no papel antes do computador?",
   "Máquina de escrever", ["máquina de escrever", "maquina de escrever"],
   "Cada tecla batia uma letra de metal numa fita com tinta, que marcava o papel.",
   "Enciclopédia Britannica – verbete 'Typewriter'")
tf(T, "aparelhos de casa", 1, 9, "As lâmpadas de LED gastam mais energia que as antigas lâmpadas incandescentes.", False,
   "O LED gasta bem menos energia para iluminar o mesmo tanto e dura muito mais.",
   "Procel – dicas de economia de energia", br=True)
mc(T, "energia", 1, 9, "Qual combustível, feito da cana-de-açúcar, abastece muitos carros no Brasil?",
   ["Etanol", "Diesel", "Querosene", "Carvão"], "Etanol",
   "O Brasil é um dos maiores produtores de etanol do mundo, e ele é vendido em quase todos os postos.",
   "Embrapa – Agroenergia", br=True, syn=("álcool",))
tf(T, "tecnologia brasileira", 1, 10, "O Pix permite enviar dinheiro a qualquer hora, inclusive à noite e nos fins de semana.", True,
   "O Pix funciona 24 horas por dia, sete dias por semana, e o dinheiro chega em poucos segundos.",
   "Banco Central do Brasil – Pix", br=True)
mc(T, "energia", 1, 9, "Que tipo de usina usa a força da água dos rios para gerar a maior parte da eletricidade do Brasil?",
   ["Hidrelétrica", "Nuclear", "A carvão", "A diesel"], "Hidrelétrica",
   "A água represada passa por turbinas, que giram geradores e produzem eletricidade.",
   "Empresa de Pesquisa Energética (EPE) – Balanço Energético Nacional", br=True, ref="2026-10-13")

# =========================================================== MÉDIAS
mc(T, "aparelhos de casa", 2, 12, "Que tipo de luz invisível a maioria dos controles remotos de TV usa para mandar os comandos?",
   ["Infravermelha", "Ultravioleta", "Raio X", "Laser verde"], "Infravermelha",
   "O controle pisca uma luzinha infravermelha em códigos; dá para vê-la apontando o controle para a câmera do celular.",
   "Enciclopédia Britannica – verbete 'Remote control'")
mc(T, "aparelhos de casa", 2, 12, "O forno de micro-ondas esquenta a comida principalmente agitando as moléculas de qual substância?",
   ["Água", "Sal", "Açúcar", "Ferro"], "Água",
   "As micro-ondas fazem as moléculas de água vibrarem, e esse movimento vira calor.",
   "Enciclopédia Britannica – verbete 'Microwave oven'")
mc(T, "invenções", 2, 12, "Qual inventor criou o fonógrafo, aparelho que gravava e tocava sons, em 1877?",
   ["Thomas Edison", "Graham Bell", "Guglielmo Marconi", "Nikola Tesla"], "Thomas Edison",
   "O fonógrafo gravava o som em um cilindro coberto de papel-alumínio; a primeira gravação foi uma cantiga infantil.",
   "Enciclopédia Britannica – verbete 'Phonograph'")
mc(T, "invenções", 2, 12, "Quais irmãos norte-americanos voaram com o avião Flyer, em 1903?",
   ["Irmãos Wright", "Irmãos Lumière", "Irmãos Grimm", "Irmãos Marx"], "Irmãos Wright",
   "Wilbur e Orville Wright voaram na Carolina do Norte; no Brasil, celebra-se Santos Dumont por decolar o 14-Bis por meios próprios em 1906.",
   "Enciclopédia Britannica – verbete 'Wright brothers'", syn=("wright",))
mc(T, "comunicação", 2, 10, "Qual sistema de pontos e traços era usado para mandar mensagens pelo telégrafo?",
   ["Código Morse", "Braille", "Código de barras", "Libras"], "Código Morse",
   "O nome homenageia o norte-americano Samuel Morse, que ajudou a criar o telégrafo elétrico nos anos 1830.",
   "Enciclopédia Britannica – verbete 'Morse Code'", syn=("morse",))
mc(T, "transportes", 2, 12, "Qual cidade brasileira inaugurou o primeiro metrô do país, em 1974?",
   ["São Paulo", "Rio de Janeiro", "Recife", "Porto Alegre"], "São Paulo",
   "A primeira linha do metrô paulistano, hoje chamada Linha 1-Azul, começou a operar em 1974.",
   "Companhia do Metropolitano de São Paulo – história", br=True)
mc(T, "engenharia", 2, 10, "Qual ponte, inaugurada em 1974, atravessa a Baía de Guanabara?",
   ["Ponte Rio-Niterói", "Ponte Hercílio Luz", "Ponte Estaiada Octavio Frias", "Ponte JK"], "Ponte Rio-Niterói",
   "Com cerca de 13 quilômetros, ela é uma das maiores pontes do Brasil.",
   "Ecoponte – história da Ponte Rio-Niterói", br=True)
mc(T, "engenharia", 2, 10, "Qual usina hidrelétrica, construída pelo Brasil e pelo Paraguai no rio Paraná, é uma das maiores do mundo?",
   ["Itaipu", "Belo Monte", "Tucuruí", "Furnas"], "Itaipu",
   "Itaipu é binacional: metade pertence ao Brasil e metade ao Paraguai.",
   "Itaipu Binacional", br=True)
mc(T, "unidades digitais", 2, 10, "Como se chama cada pontinho colorido que forma a imagem numa tela?",
   ["Pixel", "Byte", "Chip", "Cursor"], "Pixel",
   "Quanto mais pixels uma tela tem, mais nítida a imagem fica.",
   "Enciclopédia Britannica – verbete 'Pixel'")
mc(T, "unidades digitais", 2, 12, "Quantos megabytes, aproximadamente, cabem em um gigabyte?",
   ["Cerca de mil", "Cerca de dez", "Cerca de cem", "Cerca de um milhão"], "Cerca de mil",
   "O prefixo 'giga' indica mil vezes 'mega'; em alguns sistemas a conta usa 1.024.",
   "Enciclopédia Britannica – verbete 'Byte'", syn=("mil", "1000", "1.000", "1024"))
tf(T, "inteligência artificial", 2, 10, "Os assistentes de inteligência artificial podem dar respostas erradas, por isso é bom conferir as informações.", True,
   "Esses programas geram textos a partir de padrões e podem inventar dados com aparência de verdade.",
   "UNESCO – Orientações para a IA generativa na educação e na pesquisa")
mc(T, "videogames", 2, 12, "Na série 'The Legend of Zelda', como se chama o herói de roupa verde que o jogador controla?",
   ["Link", "Ganon", "Kirby", "Toad"], "Link",
   "Muita gente pensa que o herói se chama Zelda, mas esse é o nome da princesa.",
   "Nintendo – série The Legend of Zelda")
tf(T, "transportes", 2, 12, "O Concorde era um avião de passageiros que voava mais rápido que o som.", True,
   "O Concorde cruzava o Atlântico em cerca de três horas e meia e deixou de voar em 2003.",
   "Enciclopédia Britannica – verbete 'Concorde'")
tf(T, "segurança na internet", 2, 10, "Tudo o que postamos na internet pode ser apagado para sempre com facilidade.", False,
   "Outras pessoas podem copiar ou salvar a postagem antes de ela ser apagada, e ela pode continuar circulando.",
   "SaferNet Brasil – dicas de segurança", br=True)
op(T, "transportes", 2, 12, "Como se chama o carro que pode usar gasolina, etanol ou a mistura dos dois no mesmo tanque?",
   "Flex", ["flex", "carro flex", "bicombustível", "bicombustivel", "flexível", "total flex"],
   "Os carros flex chegaram ao mercado brasileiro em 2003 e hoje são maioria no país.",
   "Embrapa – Agroenergia", br=True)
mc(T, "comunicação", 2, 10, "Qual era o apelido dos telefones públicos brasileiros com cobertura em forma de concha?",
   ["Orelhão", "Cabinão", "Bocão", "Caramujo"], "Orelhão",
   "A cobertura arredondada protege do sol e da chuva e diminui o barulho da rua durante a ligação.",
   "Museu das Telecomunicações (Oi Futuro) – história do orelhão", br=True)
mc(T, "internet", 2, 10, "Como se chamam as mensagens indesejadas, geralmente propagandas, que chegam aos montes no e-mail?",
   ["Spam", "Cookie", "Backup", "Download"], "Spam",
   "Os programas de e-mail costumam separar essas mensagens numa pasta própria.",
   "CERT.br – Cartilha de Segurança para Internet")
op(T, "segurança na internet", 2, 10, "Como se chama o programa que protege o computador contra vírus?",
   "Antivírus", ["antivírus", "antivirus", "programa antivírus"],
   "O antivírus procura programas maliciosos e os bloqueia ou remove.",
   "CERT.br – Cartilha de Segurança para Internet")
mc(T, "transportes", 2, 12, "Qual cidade brasileira ficou famosa pelos ônibus em faixas exclusivas e pelas estações em forma de tubo?",
   ["Curitiba", "Salvador", "Belém", "Manaus"], "Curitiba",
   "O sistema de Curitiba, criado nos anos 1970, inspirou corredores de ônibus em várias cidades do mundo.",
   "URBS – Urbanização de Curitiba", br=True)
mc(T, "energia", 2, 12, "Em qual estado ficam as usinas nucleares brasileiras Angra 1 e Angra 2?",
   ["Rio de Janeiro", "São Paulo", "Minas Gerais", "Bahia"], "Rio de Janeiro",
   "As usinas ficam no município de Angra dos Reis, no litoral sul fluminense.",
   "Eletronuclear", br=True)
mc(T, "transportes", 2, 12, "Como é transportada a maior parte das cargas no Brasil?",
   ["Por caminhões, nas rodovias", "Por trens, nas ferrovias", "Por barcos, nos rios", "Por aviões"],
   "Por caminhões, nas rodovias",
   "Mais da metade das mercadorias do país viaja por estradas, em caminhões.",
   "Confederação Nacional do Transporte (CNT)", br=True, ref="2026-10-13")
tf(T, "transportes", 2, 14, "O trem-bala japonês começou a funcionar em 1964, pouco antes da Olimpíada de Tóquio.", True,
   "A primeira linha do Shinkansen ligava Tóquio a Osaka e foi inaugurada em outubro de 1964.",
   "Enciclopédia Britannica – verbete 'Shinkansen'")
mc(T, "transportes", 2, 14, "Em qual cidade paulista fica a sede da Embraer, fabricante brasileira de aviões?",
   ["São José dos Campos", "Campinas", "Santos", "Sorocaba"], "São José dos Campos",
   "A cidade também abriga o ITA e o DCTA, importantes centros da aviação brasileira.",
   "Embraer – história", br=True)

# =========================================================== DIFÍCEIS
mc(T, "aparelhos de casa", 3, 14, "Qual peça da geladeira, geralmente atrás e embaixo dela, bombeia o gás que retira o calor de dentro?",
   ["Compressor", "Termostato", "Lâmpada", "Borracha da porta"], "Compressor",
   "O compressor faz o gás circular; ele absorve o calor lá dentro e o solta pela grade de trás.",
   "Enciclopédia Britannica – verbete 'Refrigeration'")
mc(T, "engenharia", 3, 14, "Qual túnel ferroviário passa por baixo do mar e liga a Inglaterra à França?",
   ["Eurotúnel", "Túnel de São Gotardo", "Túnel Seikan", "Túnel Rebouças"], "Eurotúnel",
   "Inaugurado em 1994, ele tem cerca de 50 quilômetros, boa parte sob o Canal da Mancha.",
   "Enciclopédia Britannica – verbete 'Channel Tunnel'", syn=("túnel do canal da mancha",))
mc(T, "inteligência artificial", 3, 14, "Qual computador da IBM venceu o campeão mundial de xadrez Garry Kasparov, em 1997?",
   ["Deep Blue", "Watson", "ENIAC", "AlphaGo"], "Deep Blue",
   "Foi a primeira vez que um computador derrotou um campeão mundial numa partida com regras de torneio.",
   "Enciclopédia Britannica – verbete 'Deep Blue'")
mc(T, "videogames", 3, 14, "Qual videogame de 1972, um dos primeiros de sucesso, imitava uma partida de tênis de mesa?",
   ["Pong", "Space Invaders", "Pac-Man", "Asteroids"], "Pong",
   "Lançado pela Atari, o Pong tinha duas barrinhas e uma bolinha que ia de um lado para o outro.",
   "Enciclopédia Britannica – verbete 'Pong'")
tf(T, "invenções", 3, 14, "A primeira ligação telefônica de Graham Bell foi um chamado ao seu assistente, Thomas Watson.", True,
   "Em 1876, Bell disse ao aparelho algo como 'Senhor Watson, venha cá, quero vê-lo'.",
   "Enciclopédia Britannica – verbete 'Alexander Graham Bell'")
tf(T, "videogames", 3, 12, "O Mario apareceu pela primeira vez no jogo 'Super Mario Bros.'.", False,
   "Ele estreou em 'Donkey Kong', de 1981, com o nome de Jumpman, tentando salvar uma moça de um gorila.",
   "Nintendo – história da série Super Mario")
mc(T, "invenções", 3, 14, "Qual engenheiro alemão patenteou em 1886 um veículo de três rodas a gasolina, considerado o primeiro automóvel prático?",
   ["Karl Benz", "Henry Ford", "Rudolf Diesel", "Ferdinand Porsche"], "Karl Benz",
   "O Benz Patent-Motorwagen tinha um motor de um cilindro e chegava a cerca de 16 km/h.",
   "Enciclopédia Britannica – verbete 'Karl Benz'")
mc(T, "invenções", 3, 14, "Qual pequeno avião de Santos Dumont, de 1907 a 1909, é considerado um dos primeiros ultraleves?",
   ["Demoiselle", "Flyer", "Bandeirante", "Spirit of St. Louis"], "Demoiselle",
   "Santos Dumont não patenteou o Demoiselle e deixou os desenhos livres para quem quisesse construí-lo.",
   "Força Aérea Brasileira – Santos Dumont", br=True)
mc(T, "tecnologia brasileira", 3, 14, "Qual acelerador de partículas brasileiro, em Campinas, produz uma luz muito intensa para pesquisas?",
   ["Sirius", "Amazonia", "Pampa", "Cruzeiro"], "Sirius",
   "O Sirius, do CNPEM, é uma fonte de luz síncrotron usada para estudar materiais, remédios e até fósseis.",
   "CNPEM – Centro Nacional de Pesquisa em Energia e Materiais", br=True)
mc(T, "transportes", 3, 16, "Qual empresário brasileiro fabricou carros com o próprio sobrenome, como o pequeno BR-800?",
   ["João Gurgel", "Ayrton Senna", "Alberto Santos Dumont", "Assis Chateaubriand"], "João Gurgel",
   "João Augusto Conrado do Amaral Gurgel lançou o BR-800 em 1988, um carro popular inteiramente projetado no Brasil.",
   "Enciclopédia Itaú Cultural – Gurgel", br=True, syn=("gurgel",))
mc(T, "videogames", 3, 14, "Qual empresa brasileira lançou no país os consoles Master System e Mega Drive?",
   ["Tectoy", "Gradiente", "Positivo", "Itautec"], "Tectoy",
   "A Tectoy era parceira da Sega no Brasil e chegou a criar jogos próprios, como os da Turma da Mônica.",
   "Tectoy – história", br=True)
tf(T, "engenharia", 3, 14, "O Cristo Redentor, no Rio de Janeiro, é feito de bronze.", False,
   "A estátua é de concreto armado, revestida por milhares de pequenos triângulos de pedra-sabão.",
   "Santuário Cristo Redentor – história", br=True)

# =========================================================== MUITO DIFÍCEIS
tf(T, "comunicação", 4, 16, "O orelhão foi criado pela arquiteta Chu Ming Silveira, nos anos 1970.", True,
   "Nascida na China e radicada no Brasil, ela desenhou o orelhão para a Companhia Telefônica Brasileira.",
   "Museu das Telecomunicações (Oi Futuro) – história do orelhão", br=True)
mc(T, "robótica", 4, 14, "De que língua vem a palavra 'robô', popularizada por uma peça de teatro de 1920?",
   ["Tcheco", "Japonês", "Inglês", "Latim"], "Tcheco",
   "Na peça 'R.U.R.', de Karel Čapek, a palavra vem de 'robota', que quer dizer trabalho forçado.",
   "Enciclopédia Britannica – verbete 'Robot'")
mc(T, "transportes", 4, 16, "Qual avião turboélice para passageiros foi o primeiro fabricado em série pela Embraer?",
   ["Bandeirante", "Tucano", "Brasília", "Xingu"], "Bandeirante",
   "O EMB 110 Bandeirante voou em 1968, e a Embraer foi criada em 1969 justamente para produzi-lo.",
   "Embraer – história", br=True)
mc(T, "comunicação", 4, 16, "Qual cientista alemão comprovou a existência das ondas de rádio e virou nome de unidade de frequência?",
   ["Heinrich Hertz", "Georg Ohm", "Alessandro Volta", "André-Marie Ampère"], "Heinrich Hertz",
   "Nos anos 1880, Hertz produziu e detectou ondas eletromagnéticas em laboratório.",
   "Enciclopédia Britannica – verbete 'Heinrich Hertz'", syn=("hertz",))
mc(T, "computador", 4, 16, "Qual empresa lançou em 1956 o primeiro disco rígido comercial, do tamanho de um armário grande?",
   ["IBM", "Intel", "Apple", "Microsoft"], "IBM",
   "O IBM 350, do sistema RAMAC, pesava cerca de uma tonelada e guardava uns 5 megabytes.",
   "IBM – história do RAMAC")
mc(T, "videogames", 4, 16, "Qual empresa lançou o Odyssey, de 1972, considerado o primeiro console de videogame doméstico?",
   ["Magnavox", "Atari", "Nintendo", "Sega"], "Magnavox",
   "O Odyssey foi criado pelo engenheiro Ralph Baer e não tinha som nem cores na tela.",
   "Enciclopédia Britannica – verbete 'Ralph Baer'")
