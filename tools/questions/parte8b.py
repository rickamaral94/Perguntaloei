# Perguntas novas (parte 8b): ciência, natureza, astronomia, corpo humano, tecnologia, matemática.
from qdsl import mc, op, tf

# =========================================================== CIÊNCIA
C = "cie"
tf(C, "ar", 1, 6, "O vento é o ar em movimento.", True,
   "O vento surge quando o ar se desloca de regiões de pressão mais alta para regiões de pressão mais baixa.",
   "Enciclopédia Britannica – verbete 'Wind'")
mc(C, "luz", 1, 6, "Qual destes materiais é transparente e deixa a luz passar?",
   ["Vidro", "Madeira", "Tijolo", "Papelão"], "Vidro",
   "O vidro comum deixa a luz atravessar, por isso é usado nas janelas; madeira, tijolo e papelão bloqueiam a luz.",
   "Enciclopédia Britannica – verbete 'Glass'")
mc(C, "eletricidade", 1, 6, "Qual destes objetos precisa de eletricidade para funcionar?",
   ["Lâmpada", "Vassoura", "Colher", "Lápis"], "Lâmpada",
   "A lâmpada acende quando a corrente elétrica passa por ela; vassoura, colher e lápis funcionam sem energia elétrica.",
   "Enciclopédia Britannica – verbete 'Electric light'")
mc(C, "instrumentos", 1, 7, "Qual instrumento usamos para ver coisas muito pequenas, como as células, bem aumentadas?",
   ["Microscópio", "Telescópio", "Periscópio", "Estetoscópio"], "Microscópio",
   "O microscópio usa lentes para ampliar objetos pequenos demais para serem vistos a olho nu.",
   "Enciclopédia Britannica – verbete 'Microscope'")
mc(C, "estados da matéria", 1, 8, "Quando a manteiga derrete na frigideira quente, ela passa para qual estado físico?",
   ["Líquido", "Gasoso", "Sólido"], "Líquido",
   "Com o calor, a manteiga sólida sofre fusão e passa para o estado líquido.",
   "Enciclopédia Britannica – verbete 'Melting'")
mc(C, "energia", 1, 9, "Qual destas é uma fonte de energia renovável?",
   ["Vento", "Petróleo", "Carvão mineral", "Gás natural"], "Vento",
   "A energia dos ventos se renova continuamente, enquanto petróleo, carvão e gás natural são combustíveis fósseis que se esgotam.",
   "Ministério de Minas e Energia – Energias renováveis")
tf(C, "som e luz", 1, 9, "A luz viaja muito mais rápido do que o som.", True,
   "Por isso numa tempestade vemos o relâmpago antes de ouvir o trovão.",
   "Enciclopédia Britannica – verbete 'Speed of light'")
mc(C, "estados da matéria", 2, 12, "Como se chama a passagem direta do estado sólido para o gasoso, como acontece com as bolinhas de naftalina?",
   ["Sublimação", "Fusão", "Condensação", "Ebulição"], "Sublimação",
   "Na sublimação, a substância sólida vira gás sem passar pelo estado líquido.",
   "Enciclopédia Britannica – verbete 'Sublimation'")
mc(C, "eletricidade", 2, 12, "Qual unidade mede a tensão elétrica, aquela que aparece nas tomadas como cento e vinte e sete ou duzentos e vinte?",
   ["Volt", "Watt", "Ampère", "Ohm"], "Volt",
   "A tensão elétrica é medida em volts, nome dado em homenagem ao italiano Alessandro Volta.",
   "Enciclopédia Britannica – verbete 'Volt'")
tf(C, "estados da matéria", 2, 12, "O gelo boia na água porque é menos denso do que a água líquida.", True,
   "Ao congelar, a água se expande e fica menos densa, por isso o gelo flutua.",
   "Enciclopédia Britannica – verbete 'Ice'")
op(C, "química", 2, 10, "Qual gás, mais leve que o ar, enche os balões de festa que sobem sozinhos?",
   "Hélio", ["hélio", "helio", "gás hélio", "gas helio"],
   "O hélio é menos denso que o ar, por isso os balões cheios dele sobem.",
   "Enciclopédia Britannica – verbete 'Helium'")
mc(C, "misturas", 2, 12, "Qual processo separa a água do sal fervendo a mistura e depois resfriando o vapor?",
   ["Destilação", "Filtração", "Decantação", "Peneiração"], "Destilação",
   "Na destilação, a água evapora, o vapor é resfriado e volta a ser líquido, e o sal fica para trás.",
   "Enciclopédia Britannica – verbete 'Distillation'")
mc(C, "eletricidade", 2, 12, "Qual cientista italiano inventou a pilha elétrica, por volta de 1800?",
   ["Alessandro Volta", "Galileu Galilei", "Guglielmo Marconi", "Luigi Galvani"], "Alessandro Volta",
   "Volta empilhou discos de metais diferentes separados por tecido molhado, criando a primeira pilha elétrica.",
   "Enciclopédia Britannica – verbete 'Alessandro Volta'")
mc(C, "luz", 3, 14, "Qual tipo de lente é usado nas lupas para aumentar o tamanho das coisas?",
   ["Convergente", "Divergente", "Plana", "Espelhada"], "Convergente",
   "A lupa usa uma lente convergente, mais grossa no meio, que forma uma imagem ampliada de objetos próximos.",
   "Enciclopédia Britannica – verbete 'Magnifying glass'")
mc(C, "magnetismo", 3, 14, "Qual cientista inglês descobriu, em 1831, que um ímã em movimento pode gerar corrente elétrica num fio?",
   ["Michael Faraday", "James Clerk Maxwell", "André-Marie Ampère", "Benjamin Franklin"], "Michael Faraday",
   "Faraday descobriu a indução eletromagnética, princípio usado nos geradores das usinas.",
   "Enciclopédia Britannica – verbete 'Michael Faraday'")
mc(C, "cientistas brasileiros", 3, 14, "Qual físico brasileiro, nascido em Curitiba, participou da descoberta da partícula chamada méson pi, em 1947?",
   ["César Lattes", "Mário Schenberg", "José Leite Lopes", "Carlos Chagas"], "César Lattes",
   "César Lattes integrou a equipe que identificou o méson pi, um dos marcos da física de partículas.",
   "CNPq – Plataforma Lattes, 'Quem foi César Lattes'", br=True)
mc(C, "estados da matéria", 3, 14, "Como se chama o estado da matéria formado por gás muito quente com partículas eletricamente carregadas, presente nas estrelas?",
   ["Plasma", "Vapor", "Coloide", "Cristal"], "Plasma",
   "O plasma é um gás ionizado; o Sol e as outras estrelas são formados principalmente por plasma.",
   "Enciclopédia Britannica – verbete 'Plasma (physics)'")
mc(C, "física", 4, 16, "Qual físico alemão propôs, em 1900, que a energia é emitida em pequenos pacotes chamados quanta?",
   ["Max Planck", "Niels Bohr", "Werner Heisenberg", "Erwin Schrödinger"], "Max Planck",
   "A hipótese de Planck sobre os quanta de energia deu origem à física quântica.",
   "Enciclopédia Britannica – verbete 'Max Planck'")

# =========================================================== NATUREZA
C = "nat"
mc(C, "oceanos", 1, 6, "Qual animal do mar tem o corpo com cinco braços e costuma viver nas pedras e na areia do fundo?",
   ["Estrela-do-mar", "Polvo", "Siri", "Tartaruga-marinha"], "Estrela-do-mar",
   "A maioria das estrelas-do-mar tem cinco braços e se move devagar pelo fundo do mar.",
   "Enciclopédia Britannica – verbete 'Sea star'")
tf(C, "insetos", 1, 6, "A joaninha é um inseto.", True,
   "A joaninha é um pequeno besouro, e os besouros são insetos, com seis patas.",
   "Enciclopédia Britannica – verbete 'Ladybird beetle'")
mc(C, "insetos", 1, 7, "Qual inseto acende uma luz no próprio corpo à noite?",
   ["Vaga-lume", "Grilo", "Formiga", "Mosquito"], "Vaga-lume",
   "O vaga-lume produz luz por uma reação química no corpo, fenômeno chamado bioluminescência.",
   "Enciclopédia Britannica – verbete 'Firefly'")
mc(C, "aves", 1, 8, "Qual ave brasileira é famosa pelo bico enorme e colorido?",
   ["Tucano", "Pica-pau", "Bem-te-vi", "Gavião"], "Tucano",
   "O bico do tucano parece pesado, mas é leve e oco por dentro; a ave o usa para alcançar frutas e ajudar a controlar a temperatura do corpo.",
   "Enciclopédia Britannica – verbete 'Toucan'", br=True)
mc(C, "aves", 1, 8, "Qual ave caça à noite e consegue girar muito a cabeça para olhar para os lados e para trás?",
   ["Coruja", "Galinha", "Pato", "Pombo"], "Coruja",
   "As corujas têm o pescoço muito flexível e podem girar a cabeça cerca de duzentos e setenta graus.",
   "Enciclopédia Britannica – verbete 'Owl'")
mc(C, "oceanos", 1, 9, "Qual animal marinho tem o corpo gelatinoso e tentáculos que podem queimar a pele de quem encosta?",
   ["Água-viva", "Estrela-do-mar", "Cavalo-marinho", "Lula"], "Água-viva",
   "Os tentáculos da água-viva têm células urticantes que soltam substâncias irritantes.",
   "Enciclopédia Britannica – verbete 'Jellyfish'")
tf(C, "oceanos", 2, 10, "O cavalo-marinho é um peixe.", True,
   "Apesar da forma diferente, o cavalo-marinho é um peixe ósseo que respira por brânquias.",
   "Enciclopédia Britannica – verbete 'Seahorse'")
mc(C, "biomas", 2, 10, "Qual bioma de campos abertos, no Brasil, só existe no Rio Grande do Sul?",
   ["Pampa", "Caatinga", "Pantanal", "Cerrado"], "Pampa",
   "O Pampa, formado principalmente por campos, cobre mais da metade do Rio Grande do Sul e continua pelo Uruguai e pela Argentina.",
   "IBGE – Biomas do Brasil", br=True)
op(C, "comportamento animal", 2, 10, "Como se chama o animal que fica ativo à noite e descansa durante o dia?",
   "Noturno", ["noturno", "animal noturno", "noturna", "animais noturnos"],
   "Animais noturnos, como corujas e morcegos, buscam alimento principalmente à noite.",
   "Enciclopédia Britannica – verbete 'Nocturnal'")
mc(C, "aves", 2, 10, "Qual ave brasileira constrói com barro um ninho em forma de forno?",
   ["João-de-barro", "Bem-te-vi", "Quero-quero", "Beija-flor"], "João-de-barro",
   "O joão-de-barro usa barro e palha para fazer um ninho redondo, com entrada lateral.",
   "Enciclopédia Britannica – verbete 'Ovenbird'", br=True)
tf(C, "oceanos", 2, 12, "Os corais são animais.", True,
   "Os corais são pequenos animais, parentes das águas-vivas, que vivem em colônias e formam os recifes.",
   "NOAA – 'Is coral an animal or a plant?'")
mc(C, "biomas", 2, 12, "Qual ambiente do litoral, de água salobra e chão de lama, serve de berçário para caranguejos e peixes?",
   ["Manguezal", "Restinga", "Duna", "Campo rupestre"], "Manguezal",
   "O manguezal fica onde o rio encontra o mar, e muitas espécies se reproduzem ali.",
   "ICMBio – Atlas dos Manguezais do Brasil", br=True)
mc(C, "conservação", 2, 12, "Qual projeto brasileiro, criado em 1980, protege as tartarugas marinhas no litoral?",
   ["Projeto Tamar", "Projeto Baleia Jubarte", "Projeto Peixe-Boi", "Projeto Golfinho Rotador"], "Projeto Tamar",
   "O Projeto Tamar monitora praias de desova e ajuda a proteger as cinco espécies de tartaruga marinha do Brasil.",
   "Fundação Projeto Tamar", br=True)
tf(C, "insetos", 3, 12, "As abelhas-melíferas fazem uma espécie de dança para mostrar às companheiras onde há flores.", True,
   "A chamada dança do requebrado indica a direção e a distância da comida, como descobriu Karl von Frisch.",
   "Enciclopédia Britannica – verbete 'Karl von Frisch'")
mc(C, "aves", 3, 12, "Qual grande ave de rapina das florestas brasileiras, também chamada de gavião-real, tem garras enormes?",
   ["Harpia", "Carcará", "Urubu-rei", "Coruja-buraqueira"], "Harpia",
   "A harpia é uma das águias mais fortes do mundo e caça macacos e preguiças no alto das árvores.",
   "ICMBio – Harpia (Harpia harpyja)", br=True)
mc(C, "aves", 3, 14, "Qual ave foi declarada, por decreto de 2002, a ave símbolo do Brasil?",
   ["Sabiá-laranjeira", "Bem-te-vi", "Tucano-toco", "Arara-vermelha"], "Sabiá-laranjeira",
   "Um decreto presidencial de 2002 tornou o sabiá-laranjeira a ave símbolo nacional.",
   "Presidência da República – Decreto de 3 de outubro de 2002", br=True)
mc(C, "ciência da vida", 3, 14, "Como se chama a área da ciência que estuda os insetos?",
   ["Entomologia", "Ornitologia", "Ictiologia", "Herpetologia"], "Entomologia",
   "A entomologia estuda os insetos; a ornitologia estuda as aves, e a ictiologia, os peixes.",
   "Enciclopédia Britannica – verbete 'Entomology'")
op(C, "mamíferos", 3, 14, "Em quantos compartimentos é dividido o estômago de uma vaca?",
   "4", ["4", "quatro", "quatro compartimentos", "4 compartimentos"],
   "O estômago dos ruminantes tem rúmen, retículo, omaso e abomaso.",
   "Embrapa – Fisiologia digestiva dos ruminantes")

# =========================================================== ASTRONOMIA
C = "ast"
tf(C, "Sol", 1, 6, "O Sol é muito maior do que a Terra.", True,
   "O diâmetro do Sol é cerca de cento e nove vezes o diâmetro da Terra.",
   "NASA – Sun: Facts")
tf(C, "dia e noite", 1, 7, "Quando é noite no Brasil, o Sol continua brilhando e iluminando o outro lado da Terra.", True,
   "A Terra gira, e enquanto um lado está virado para o Sol, o lado oposto fica no escuro.",
   "NASA Space Place – 'What causes day and night?'")
mc(C, "astros", 1, 7, "Qual destes astros tem luz própria?",
   ["Sol", "Lua", "Marte", "Vênus"], "Sol",
   "O Sol é uma estrela e produz a própria luz; a Lua e os planetas apenas refletem a luz do Sol.",
   "NASA – Sun: Facts")
mc(C, "estrelas", 1, 8, "Por que não conseguimos ver as estrelas durante o dia?",
   ["A luz do Sol ofusca o brilho delas", "Elas se apagam de dia", "A Lua cobre todas elas", "Elas vão para o outro lado do céu"],
   "A luz do Sol ofusca o brilho delas",
   "As estrelas continuam no céu de dia, mas a luz do Sol espalhada pelo ar é muito mais forte que a delas.",
   "NASA Space Place – 'Why can't we see stars during the day?'")
mc(C, "constelações", 1, 8, "Como se chama um grupo de estrelas que forma um desenho no céu, como o Escorpião?",
   ["Constelação", "Galáxia", "Órbita", "Cometa"], "Constelação",
   "As constelações são agrupamentos de estrelas que as pessoas ligam com linhas imaginárias para formar figuras.",
   "União Astronômica Internacional – The Constellations")
mc(C, "Sistema Solar", 1, 9, "Como se chama o caminho que um planeta percorre em volta do Sol?",
   ["Órbita", "Eixo", "Atmosfera", "Eclipse"], "Órbita",
   "A órbita é a trajetória de um astro ao redor de outro, mantida pela gravidade.",
   "NASA – 'What Is an Orbit?'")
mc(C, "constelações", 2, 10, "As Três Marias, três estrelas em fila no céu, fazem parte de qual constelação?",
   ["Órion", "Escorpião", "Cruzeiro do Sul", "Ursa Maior"], "Órion",
   "As Três Marias formam o cinturão do caçador Órion.",
   "Enciclopédia Britannica – verbete 'Orion'")
op(C, "Sistema Solar", 2, 10, "Quantos planetas ficam entre a Terra e o Sol?",
   "2", ["2", "dois", "dois planetas"],
   "Mercúrio e Vênus são os únicos planetas com órbitas mais próximas do Sol do que a da Terra.",
   "NASA – Solar System Exploration")
tf(C, "eclipses", 2, 12, "Num eclipse lunar, a Terra fica entre o Sol e a Lua.", True,
   "No eclipse lunar, a sombra da Terra cobre a Lua cheia.",
   "NASA – Lunar Eclipses")
tf(C, "luas", 2, 12, "Marte tem duas pequenas luas, chamadas Fobos e Deimos.", True,
   "Fobos e Deimos foram descobertas em 1877 pelo astrônomo norte-americano Asaph Hall.",
   "NASA – Mars Moons")
op(C, "luas", 2, 12, "Quantas luas tem o planeta Mercúrio?",
   "Nenhuma", ["nenhuma", "nenhum", "nenhuma lua", "zero", "0", "não tem", "nao tem"],
   "Mercúrio, assim como Vênus, não tem nenhum satélite natural.",
   "NASA – Mercury: Facts")
mc(C, "exploração espacial", 2, 12, "Qual astronauta norte-americano pisou na Lua logo depois de Neil Armstrong, em 1969?",
   ["Buzz Aldrin", "Michael Collins", "John Glenn", "Alan Shepard"], "Buzz Aldrin",
   "Buzz Aldrin desceu do módulo lunar minutos depois de Armstrong, enquanto Michael Collins ficou em órbita.",
   "NASA – Apollo 11 Mission Overview")
mc(C, "exploração espacial", 3, 12, "Qual cosmonauta soviética foi a primeira mulher a viajar ao espaço, em 1963?",
   ["Valentina Tereshkova", "Sally Ride", "Svetlana Savitskaya", "Mae Jemison"], "Valentina Tereshkova",
   "Valentina Tereshkova deu quarenta e oito voltas na Terra a bordo da nave Vostok 6.",
   "Enciclopédia Britannica – verbete 'Valentina Tereshkova'")
mc(C, "observação do céu", 3, 14, "Como se chama o ponto do céu que fica exatamente acima da cabeça de quem observa?",
   ["Zênite", "Nadir", "Horizonte", "Meridiano"], "Zênite",
   "O zênite fica bem acima do observador; o ponto oposto, sob os pés, é o nadir.",
   "Enciclopédia Britannica – verbete 'Zenith'")
mc(C, "luas", 3, 14, "Io, a lua com mais vulcões ativos do Sistema Solar, gira em torno de qual planeta?",
   ["Júpiter", "Saturno", "Urano", "Netuno"], "Júpiter",
   "Io é uma das quatro grandes luas de Júpiter, e as forças de maré causadas pela gravidade do planeta aquecem seu interior.",
   "NASA – Io: Facts")
mc(C, "exploração espacial", 3, 14, "Qual robô da NASA pousou em Marte em 2021 levando um pequeno helicóptero chamado Ingenuity?",
   ["Perseverance", "Curiosity", "Opportunity", "Spirit"], "Perseverance",
   "O Perseverance pousou na cratera Jezero, e o Ingenuity fez o primeiro voo motorizado em outro planeta.",
   "NASA – Mars 2020 Perseverance Rover")
mc(C, "exploração espacial", 3, 14, "Qual sonda espacial, lançada em 1977, é o objeto feito pelo ser humano que está mais longe da Terra?",
   ["Voyager 1", "Pioneer 10", "New Horizons", "Cassini"], "Voyager 1",
   "A Voyager 1 passou por Júpiter e Saturno e hoje viaja pelo espaço interestelar.",
   "NASA – Voyager Mission", ref="2026-10-13")
mc(C, "estrelas", 4, 16, "Qual aglomerado de estrelas da constelação de Touro é chamado popularmente no Brasil de Sete-Estrelo?",
   ["Plêiades", "Híades", "Nebulosa de Órion", "Ômega Centauri"], "Plêiades",
   "As Plêiades são um aglomerado de estrelas jovens, e a olho nu se costuma ver de seis a sete delas.",
   "Enciclopédia Britannica – verbete 'Pleiades'")

# =========================================================== CORPO HUMANO
C = "cor"
mc(C, "sentidos", 1, 6, "Com qual parte do corpo sentimos se algo é quente, frio, liso ou áspero ao tocar?",
   ["Pele", "Nariz", "Orelhas", "Olhos"], "Pele",
   "A pele tem receptores que percebem toque, temperatura, pressão e dor; é o sentido do tato.",
   "Enciclopédia Britannica – verbete 'Touch'")
tf(C, "saúde", 1, 6, "Beber água ao longo do dia é importante para o corpo funcionar bem.", True,
   "A água ajuda a controlar a temperatura do corpo, levar nutrientes e eliminar resíduos.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
op(C, "olhos", 1, 6, "Como se chama a gotinha de água salgada que sai dos olhos quando choramos?",
   "Lágrima", ["lágrima", "lágrimas", "lagrima", "lagrimas"],
   "As lágrimas, produzidas pelas glândulas lacrimais, também limpam e protegem os olhos.",
   "Enciclopédia Britannica – verbete 'Tear'")
mc(C, "sentidos", 1, 7, "Qual parte do corpo tem as papilas gustativas, que percebem os sabores?",
   ["Língua", "Nariz", "Dentes", "Lábios"], "Língua",
   "As papilas da língua guardam os botões gustativos, que identificam doce, salgado, azedo, amargo e umami.",
   "Enciclopédia Britannica – verbete 'Taste bud'")
mc(C, "esqueleto", 1, 8, "Qual articulação liga a perna ao pé?",
   ["Tornozelo", "Joelho", "Quadril", "Calcanhar"], "Tornozelo",
   "O tornozelo une os ossos da perna, a tíbia e a fíbula, ao pé.",
   "Enciclopédia Britannica – verbete 'Ankle'")
mc(C, "alimentação", 1, 8, "Qual destes alimentos é rico em cálcio, importante para os ossos e os dentes?",
   ["Leite", "Arroz", "Maçã", "Pão"], "Leite",
   "O leite e seus derivados, como queijo e iogurte, são boas fontes de cálcio.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
mc(C, "sistema imunológico", 1, 8, "O que as vacinas ensinam o nosso corpo a fazer?",
   ["Defender-se de doenças", "Crescer mais rápido", "Enxergar melhor", "Dormir mais cedo"], "Defender-se de doenças",
   "A vacina apresenta ao corpo uma parte ou uma versão enfraquecida do micróbio, e o sistema de defesa aprende a combatê-lo.",
   "Ministério da Saúde – Programa Nacional de Imunizações", br=True)
tf(C, "saúde", 2, 10, "Os antibióticos curam gripes e resfriados causados por vírus.", False,
   "Os antibióticos agem contra bactérias e não têm efeito sobre os vírus da gripe e do resfriado.",
   "Ministério da Saúde – Uso racional de antibióticos")
mc(C, "audição", 2, 10, "Qual membrana fina do ouvido vibra quando o som chega até ela?",
   ["Tímpano", "Bigorna", "Cóclea", "Canal auditivo"], "Tímpano",
   "O tímpano vibra com as ondas sonoras e passa essa vibração para os ossinhos do ouvido médio.",
   "Enciclopédia Britannica – verbete 'Eardrum'")
mc(C, "sistema imunológico", 2, 12, "Como se chamam as proteínas que o corpo produz para combater vírus e bactérias específicos?",
   ["Anticorpos", "Hormônios", "Enzimas", "Vitaminas"], "Anticorpos",
   "Os anticorpos são produzidos por linfócitos B e se ligam a invasores específicos, marcando-os para destruição.",
   "Enciclopédia Britannica – verbete 'Antibody'")
mc(C, "olhos", 2, 12, "Qual camada do fundo do olho capta a luz e envia as imagens ao cérebro pelo nervo óptico?",
   ["Retina", "Córnea", "Pupila", "Pálpebra"], "Retina",
   "A retina tem células sensíveis à luz, os cones e os bastonetes.",
   "Enciclopédia Britannica – verbete 'Retina'")
tf(C, "sangue", 2, 12, "O sangue dentro das veias é azul e só fica vermelho quando entra em contato com o ar.", False,
   "O sangue é sempre vermelho, mais escuro nas veias; as veias só parecem azuladas vistas através da pele.",
   "Enciclopédia Britannica – verbete 'Blood'")
mc(C, "esqueleto", 2, 12, "Qual osso fica no braço, entre o ombro e o cotovelo?",
   ["Úmero", "Rádio", "Ulna", "Fêmur"], "Úmero",
   "O úmero é o osso longo do braço; rádio e ulna ficam no antebraço.",
   "Enciclopédia Britannica – verbete 'Humerus'")
mc(C, "audição", 3, 14, "Qual parte do ouvido interno, em forma de caracol, transforma as vibrações do som em sinais nervosos?",
   ["Cóclea", "Tímpano", "Bigorna", "Pavilhão auditivo"], "Cóclea",
   "Dentro da cóclea, células ciliadas convertem as vibrações em impulsos levados ao cérebro.",
   "Enciclopédia Britannica – verbete 'Cochlea'")
mc(C, "vitaminas", 3, 14, "Qual doença, comum entre marinheiros em longas viagens antigamente, é causada pela falta de vitamina C?",
   ["Escorbuto", "Raquitismo", "Beribéri", "Bócio"], "Escorbuto",
   "Sem vitamina C, o corpo não produz colágeno direito, e surgem sangramento nas gengivas e feridas que não cicatrizam.",
   "Enciclopédia Britannica – verbete 'Scurvy'")
mc(C, "vitaminas", 3, 14, "Qual vitamina, encontrada quase só em alimentos de origem animal, é essencial para o sangue e os nervos?",
   ["Vitamina B12", "Vitamina C", "Vitamina A", "Vitamina E"], "Vitamina B12",
   "A vitamina B12 está em carnes, ovos e leite, e sua falta pode causar anemia e problemas nos nervos.",
   "Enciclopédia Britannica – verbete 'Vitamin B12'")
mc(C, "medicina no Brasil", 3, 14, "Qual cientista brasileiro desenvolveu soros contra picadas de cobra e foi o primeiro diretor do Instituto Butantan?",
   ["Vital Brazil", "Oswaldo Cruz", "Carlos Chagas", "Adolfo Lutz"], "Vital Brazil",
   "Vital Brazil criou soros antiofídicos específicos para cada tipo de serpente e dirigiu o Butantan desde 1901.",
   "Instituto Butantan – História", br=True)
mc(C, "sistema imunológico", 4, 16, "Quais células de defesa do corpo são o principal alvo do vírus HIV?",
   ["Linfócitos T", "Hemácias", "Plaquetas", "Neurônios"], "Linfócitos T",
   "O HIV infecta principalmente os linfócitos T do tipo CD4, enfraquecendo o sistema imunológico.",
   "Ministério da Saúde – HIV e aids")

# =========================================================== TECNOLOGIA
C = "tec"
mc(C, "aparelhos", 1, 6, "Qual aparelho colocamos nos ouvidos para escutar música sem incomodar ninguém?",
   ["Fone de ouvido", "Microfone", "Lanterna", "Controle remoto"], "Fone de ouvido",
   "O fone de ouvido leva o som direto aos ouvidos de quem o usa.",
   "Enciclopédia Britannica – verbete 'Headphones'")
tf(C, "segurança digital", 1, 6, "Podemos contar nossas senhas para pessoas desconhecidas na internet.", False,
   "Senhas devem ser secretas; contar a estranhos pode permitir que invadam contas e roubem dados.",
   "CERT.br – Cartilha de Segurança para Internet")
mc(C, "aparelhos", 1, 7, "Qual aparelho da cozinha bate e mistura frutas para fazer suco e vitamina?",
   ["Liquidificador", "Torradeira", "Geladeira", "Ferro de passar"], "Liquidificador",
   "O liquidificador tem lâminas que giram rápido no fundo do copo e trituram os alimentos.",
   "Enciclopédia Britannica – verbete 'Blender'")
tf(C, "transportes", 1, 8, "Os carros totalmente elétricos não usam gasolina; eles andam com a energia de baterias.", True,
   "O carro elétrico tem um motor elétrico alimentado por baterias recarregáveis.",
   "Enciclopédia Britannica – verbete 'Electric automobile'")
mc(C, "internet", 1, 9, "Como se chama a foto que a pessoa tira de si mesma com o celular?",
   ["Selfie", "Print", "Meme", "Emoji"], "Selfie",
   "Selfie é o autorretrato fotográfico, geralmente feito com a câmera frontal do celular.",
   "Dicionário Oxford – verbete 'selfie'")
mc(C, "internet", 1, 10, "O que significa fazer o download de um arquivo?",
   ["Baixar o arquivo da internet para o aparelho", "Apagar o arquivo", "Imprimir o arquivo", "Mudar o nome do arquivo"],
   "Baixar o arquivo da internet para o aparelho",
   "No download, o arquivo é copiado de outro computador ou da internet para o nosso aparelho.",
   "Enciclopédia Britannica – verbete 'Download'")
op(C, "telefonia", 2, 10, "Qual geração de internet móvel, sucessora do 4G, começou a funcionar no Brasil em 2022?",
   "5G", ["5g", "cinco g", "quinta geração", "quinta geracao"],
   "O 5G começou a funcionar em Brasília em julho de 2022 e depois chegou às outras capitais.",
   "Anatel – Implantação do 5G no Brasil", br=True)
mc(C, "inventores", 2, 10, "Qual sistema de escrita com pontinhos em relevo permite que pessoas cegas leiam com os dedos?",
   ["Braille", "Código Morse", "Libras", "Código de barras"], "Braille",
   "O sistema foi criado pelo francês Louis Braille, que perdeu a visão na infância.",
   "Fundação Dorina Nowill para Cegos – O Sistema Braille")
mc(C, "inventores", 2, 12, "Qual cientista e político norte-americano inventou o para-raios, no século XVIII?",
   ["Benjamin Franklin", "Thomas Edison", "Samuel Morse", "James Watt"], "Benjamin Franklin",
   "Franklin mostrou que o raio é uma descarga elétrica e criou a haste metálica que o conduz com segurança ao chão.",
   "Enciclopédia Britannica – verbete 'Benjamin Franklin'")
mc(C, "internet", 2, 12, "O que faz o roteador de Wi-Fi dentro de uma casa?",
   ["Distribui a conexão de internet entre os aparelhos", "Guarda as fotos da família", "Recarrega a bateria do celular", "Imprime documentos"],
   "Distribui a conexão de internet entre os aparelhos",
   "O roteador recebe a internet do provedor e a compartilha com celulares, computadores e TVs.",
   "Enciclopédia Britannica – verbete 'Router'")
mc(C, "internet", 2, 12, "Quando dizemos que as fotos estão guardadas na nuvem, onde elas realmente ficam?",
   ["Em servidores de empresas, acessados pela internet", "Só na memória do celular", "Em satélites no céu", "Num pen drive"],
   "Em servidores de empresas, acessados pela internet",
   "A computação em nuvem guarda os arquivos em grandes centros de dados, que acessamos pela internet.",
   "Enciclopédia Britannica – verbete 'Cloud computing'")
mc(C, "inventores", 2, 12, "Qual inventor italiano ganhou o Nobel de Física de 1909 por seus trabalhos com a telegrafia sem fio?",
   ["Guglielmo Marconi", "Alessandro Volta", "Enrico Fermi", "Antonio Meucci"], "Guglielmo Marconi",
   "Marconi desenvolveu sistemas de transmissão por ondas de rádio e dividiu o Nobel de 1909 com Ferdinand Braun.",
   "Fundação Nobel – Prêmio Nobel de Física de 1909")
tf(C, "internet", 3, 12, "A internet e a World Wide Web são exatamente a mesma coisa.", False,
   "A internet é a rede mundial de computadores; a Web é um dos serviços que funcionam sobre ela, como o e-mail é outro.",
   "Enciclopédia Britannica – verbete 'World Wide Web'")
mc(C, "computação", 3, 14, "Qual memória do computador guarda os programas abertos enquanto ele está ligado e se apaga quando ele é desligado?",
   ["RAM", "ROM", "SSD", "Pen drive"], "RAM",
   "A memória RAM é volátil: guarda os dados em uso e perde tudo sem energia.",
   "Enciclopédia Britannica – verbete 'RAM'")
mc(C, "inventores", 3, 14, "Qual inventor sérvio-americano ficou famoso pelos estudos com a corrente alternada?",
   ["Nikola Tesla", "Thomas Edison", "George Westinghouse", "Alexander Graham Bell"], "Nikola Tesla",
   "Tesla inventou o motor de indução e ajudou a criar o sistema de corrente alternada usado até hoje na distribuição de energia.",
   "Enciclopédia Britannica – verbete 'Nikola Tesla'")
mc(C, "inventores brasileiros", 3, 14, "Qual padre gaúcho fez transmissões de voz sem fio em São Paulo, por volta de 1900, e é lembrado como pioneiro do rádio?",
   ["Roberto Landell de Moura", "Bartolomeu de Gusmão", "José de Anchieta", "Padre Cícero"], "Roberto Landell de Moura",
   "Landell de Moura demonstrou transmissões de voz sem fio em São Paulo e obteve patentes no Brasil e nos Estados Unidos.",
   "Enciclopédia Britannica – verbete 'Roberto Landell de Moura'", br=True)
mc(C, "inventores brasileiros", 4, 16, "Qual padre nascido em Santos demonstrou um pequeno balão de ar quente diante do rei de Portugal, em 1709?",
   ["Bartolomeu de Gusmão", "Roberto Landell de Moura", "Manuel da Nóbrega", "Antônio Vieira"], "Bartolomeu de Gusmão",
   "Bartolomeu de Gusmão, apelidado de 'padre voador', fez subir um balão de ar quente em Lisboa e projetou a Passarola.",
   "Enciclopédia Britannica – verbete 'Bartolomeu de Gusmão'", br=True)
mc(C, "internet", 4, 16, "Qual rede de computadores, criada nos Estados Unidos em 1969, é considerada a precursora da internet?",
   ["ARPANET", "Ethernet", "Usenet", "Minitel"], "ARPANET",
   "A ARPANET, financiada pelo Departamento de Defesa dos Estados Unidos, conectou as primeiras universidades em 1969.",
   "Enciclopédia Britannica – verbete 'ARPANET'")

# =========================================================== MATEMÁTICA
C = "mat"
op(C, "multiplicação", 1, 6, "Uma galinha tem duas patas. Quantas patas têm três galinhas juntas?",
   "6", ["6", "seis"],
   "Duas patas vezes três galinhas dá seis patas.",
   "Aritmética básica")
tf(C, "números", 1, 6, "O número dez é maior que o número doze.", False,
   "Doze vem depois de dez na contagem, então doze é maior.",
   "Aritmética básica")
mc(C, "geometria", 1, 7, "Qual sólido geométrico tem o formato de uma bola, como uma laranja?",
   ["Esfera", "Cubo", "Cone", "Cilindro"], "Esfera",
   "A esfera é o sólido redondo em que todos os pontos da superfície ficam à mesma distância do centro.",
   "Enciclopédia Britannica – verbete 'Sphere'")
mc(C, "multiplicação", 1, 8, "Quanto é cinco vezes quatro?",
   ["20", "9", "25", "15"], "20",
   "Cinco vezes quatro é o mesmo que somar quatro cinco vezes: vinte.",
   "Aritmética básica")
mc(C, "contagem", 1, 8, "Quantas laranjas há numa dúzia de laranjas?",
   ["12", "10", "6", "20"], "12",
   "Uma dúzia é um grupo de doze unidades.",
   "Dicionário Houaiss – verbete 'dúzia'")
op(C, "medidas", 1, 9, "Quantos centímetros há em meio metro?",
   "50", ["50", "cinquenta", "50 centímetros", "cinquenta centímetros"],
   "Um metro tem cem centímetros, e a metade disso é cinquenta.",
   "Inmetro – Sistema Internacional de Unidades")
mc(C, "probabilidade", 2, 10, "Ao jogar uma moeda comum, qual é a chance de sair cara?",
   ["Um meio", "Um terço", "Um quarto", "Um sexto"], "Um meio",
   "A moeda tem dois lados igualmente prováveis, então a chance de cara é uma em duas.",
   "Enciclopédia Britannica – verbete 'Probability theory'")
op(C, "medidas", 2, 10, "Uma garrafa de dois litros tem quantos mililitros?",
   "2.000", ["2000", "2.000", "dois mil", "2000 mililitros", "dois mil mililitros"],
   "Cada litro tem mil mililitros, então dois litros têm dois mil mililitros.",
   "Inmetro – Sistema Internacional de Unidades")
mc(C, "frações", 2, 10, "Uma pizza foi cortada em oito pedaços iguais e João comeu três. Que fração da pizza sobrou?",
   ["Cinco oitavos", "Três oitavos", "Cinco terços", "Três quintos"], "Cinco oitavos",
   "Sobraram cinco dos oito pedaços, ou seja, cinco oitavos da pizza.",
   "Aritmética básica")
mc(C, "raciocínio lógico", 2, 10, "Numa fila de cinco pessoas, Lia é a segunda contando do começo. Em que posição ela fica contando do fim?",
   ["Quarta", "Terceira", "Segunda", "Quinta"], "Quarta",
   "Com cinco pessoas, quem está em segundo do começo tem três pessoas atrás de si, então é a quarta a partir do fim.",
   "Raciocínio lógico")
mc(C, "probabilidade", 2, 12, "Ao jogar um dado comum, qual é a chance de sair o número seis?",
   ["Um sexto", "Um meio", "Um terço", "Seis sextos"], "Um sexto",
   "O dado tem seis faces igualmente prováveis, e só uma delas tem o seis.",
   "Enciclopédia Britannica – verbete 'Probability theory'")
tf(C, "números", 2, 12, "A soma de dois números ímpares é sempre um número par.", True,
   "Cada ímpar é um par mais um; somando dois deles, as duas sobras de um formam mais um par.",
   "Aritmética básica")
mc(C, "sequências", 2, 12, "Na sequência um, quatro, nove, dezesseis, qual número vem em seguida?",
   ["25", "20", "24", "32"], "25",
   "São os quadrados de um, dois, três e quatro; o próximo é cinco vezes cinco, vinte e cinco.",
   "Aritmética básica")
mc(C, "geometria", 2, 12, "Quanto mede cada ângulo interno de um triângulo equilátero?",
   ["60 graus", "90 graus", "45 graus", "120 graus"], "60 graus",
   "Os três ângulos são iguais e somam cento e oitenta graus, então cada um mede sessenta.",
   "Euclides – Os Elementos")
tf(C, "geometria", 3, 12, "Um triângulo pode ter dois ângulos retos.", False,
   "Dois ângulos retos já somam cento e oitenta graus, sem sobrar nada para o terceiro ângulo.",
   "Euclides – Os Elementos")
mc(C, "geometria", 3, 12, "Qual é o volume de um cubo com aresta de dois centímetros?",
   ["8 centímetros cúbicos", "6 centímetros cúbicos", "4 centímetros cúbicos", "12 centímetros cúbicos"], "8 centímetros cúbicos",
   "O volume do cubo é a aresta multiplicada três vezes: dois vezes dois vezes dois dá oito.",
   "Enciclopédia Britannica – verbete 'Cube'")
op(C, "decimais", 3, 12, "Quanto é zero vírgula dois vezes cinquenta?",
   "10", ["10", "dez"],
   "Zero vírgula dois é um quinto, e um quinto de cinquenta é dez.",
   "Aritmética básica")
mc(C, "medidas", 3, 14, "Quantos centímetros quadrados cabem em um metro quadrado?",
   ["10.000", "100", "1.000", "100.000"], "10.000",
   "Um metro quadrado é um quadrado de cem por cem centímetros, ou seja, dez mil centímetros quadrados.",
   "Inmetro – Sistema Internacional de Unidades")
mc(C, "combinatória", 3, 14, "De quantas maneiras diferentes três pessoas podem se sentar lado a lado em três cadeiras?",
   ["6", "3", "9", "27"], "6",
   "A primeira cadeira tem três opções, a segunda duas e a terceira uma: três vezes dois vezes um dá seis.",
   "Enciclopédia Britannica – verbete 'Permutation'")
mc(C, "geometria", 4, 16, "Somando todos os ângulos internos de um hexágono, qual é o resultado?",
   ["720 graus", "540 graus", "360 graus", "1.080 graus"], "720 graus",
   "Ligando um vértice aos outros, o hexágono se divide em quatro triângulos, e quatro vezes cento e oitenta dá setecentos e vinte graus.",
   "Euclides – Os Elementos")
