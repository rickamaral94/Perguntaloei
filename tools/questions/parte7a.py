# Perguntas novas (parte 7a). IDs continuam a numeração de cada tema.
from qdsl import mc, op, tf

# =========================================================== GEOGRAFIA
G = "geo"
mc(G, "mapas", 1, 6, "Como se chama o desenho que mostra países, rios e oceanos numa folha de papel?",
   ["Mapa", "Calendário", "Retrato", "Cartaz"], "Mapa",
   "Muitos mapas trazem uma rosa dos ventos para indicar norte, sul, leste e oeste.",
   "IBGE – Atlas Geográfico Escolar")
mc(G, "continentes", 1, 6, "Qual destes é o nome de um continente?",
   ["Europa", "Amazonas", "Paris", "Pacífico"], "Europa",
   "Os continentes são América, Europa, Ásia, África, Oceania e Antártida.",
   "IBGE – Atlas Geográfico Escolar")
tf(G, "pontos cardeais", 1, 8, "O Sol nasce do lado leste.", True,
   "Por isso o leste também é chamado de nascente ou oriente.",
   "IBGE – Atlas Geográfico Escolar")
mc(G, "capitais", 1, 8, "Qual cidade é a capital da Inglaterra?",
   ["Londres", "Paris", "Dublin", "Lisboa"], "Londres",
   "Londres é cortada pelo rio Tâmisa.",
   "Enciclopédia Britannica – verbete 'London'")
mc(G, "estados", 1, 9, "Qual cidade é a capital do estado do Ceará?",
   ["Fortaleza", "Natal", "Teresina", "São Luís"], "Fortaleza",
   "Fortaleza é uma das cidades mais populosas do Nordeste.",
   "IBGE – Cidades", br=True)
mc(G, "capitais", 1, 9, "Qual é a capital da Alemanha?",
   ["Berlim", "Munique", "Viena", "Hamburgo"], "Berlim",
   "Berlim ficou dividida por um muro entre 1961 e 1989.",
   "Enciclopédia Britannica – verbete 'Berlin'")
mc(G, "estados", 2, 10, "Curitiba é a capital de qual estado brasileiro?",
   ["Paraná", "Santa Catarina", "São Paulo", "Mato Grosso do Sul"], "Paraná",
   "Curitiba é conhecida pelo Jardim Botânico e pelas estações-tubo de ônibus.",
   "IBGE – Cidades", br=True)
tf(G, "regiões", 2, 10, "O estado do Rio de Janeiro fica na região Sudeste.", True,
   "O Sudeste é formado por São Paulo, Rio de Janeiro, Minas Gerais e Espírito Santo.",
   "IBGE – Divisão Regional do Brasil", br=True)
mc(G, "capitais", 2, 12, "Qual cidade, às margens do rio Nilo, é a capital do Egito?",
   ["Cairo", "Alexandria", "Luxor", "Túnis"], "Cairo",
   "As pirâmides de Gizé ficam bem perto do Cairo.",
   "Enciclopédia Britannica – verbete 'Cairo'")
op(G, "estados", 2, 12, "Qual é a capital de Santa Catarina?", "Florianópolis",
   ["florianópolis", "florianopolis", "floripa"],
   "Grande parte de Florianópolis fica na Ilha de Santa Catarina.",
   "IBGE – Cidades", br=True)
mc(G, "fronteiras", 2, 12, "Assunção é a capital de qual país vizinho do Brasil?",
   ["Paraguai", "Uruguai", "Bolívia", "Peru"], "Paraguai",
   "Assunção fica às margens do rio Paraguai.",
   "Enciclopédia Britannica – verbete 'Asunción'")
mc(G, "países", 2, 12, "Qual país africano tem o português como língua oficial e Luanda como capital?",
   ["Angola", "Quênia", "Marrocos", "Nigéria"], "Angola",
   "Angola foi colônia de Portugal até 1975.",
   "Enciclopédia Britannica – verbete 'Angola'")
mc(G, "lagos", 3, 14, "Qual lago fica na fronteira entre Peru e Bolívia, a mais de 3.800 metros de altitude?",
   ["Titicaca", "Baikal", "Vitória", "Maracaibo"], "Titicaca",
   "É considerado o lago navegável mais alto do mundo.",
   "Enciclopédia Britannica – verbete 'Lake Titicaca'")
mc(G, "capitais", 3, 14, "Qual é a capital da Turquia?",
   ["Ancara", "Istambul", "Esmirna", "Atenas"], "Ancara",
   "Istambul é a maior cidade, mas Ancara virou capital em 1923.",
   "Enciclopédia Britannica – verbete 'Ankara'")
tf(G, "ilhas", 3, 14, "O arquipélago de Fernando de Noronha pertence ao estado de Pernambuco.", True,
   "Noronha é Patrimônio Natural da Humanidade desde 2001.",
   "IBGE – Cidades", br=True)
op(G, "estados", 3, 14, "Qual estado brasileiro tem Boa Vista como capital?", "Roraima", ["roraima"],
   "Roraima é o estado que chega mais ao norte do Brasil.",
   "IBGE – Cidades", br=True)
mc(G, "capitais", 4, 16, "Qual é a capital do Marrocos?",
   ["Rabat", "Casablanca", "Marrakech", "Argel"], "Rabat",
   "Casablanca é a maior cidade do país, mas a capital é Rabat.",
   "Enciclopédia Britannica – verbete 'Rabat'")

# =========================================================== HISTÓRIA
H = "his"
mc(H, "pré-história", 1, 7, "Qual animal pré-histórico gigante tinha pelos longos e presas curvas?",
   ["Mamute", "Rinoceronte", "Hipopótamo", "Camelo"], "Mamute",
   "Os mamutes viveram na Era do Gelo e eram parentes dos elefantes.",
   "Enciclopédia Britannica – verbete 'Mammoth'")
mc(H, "Idade Média", 1, 6, "Como se chamavam as grandes construções de pedra onde moravam reis e rainhas na Idade Média?",
   ["Castelos", "Iglus", "Ocas", "Tendas"], "Castelos",
   "Muitos castelos tinham muralhas grossas e um fosso com água em volta.",
   "Enciclopédia Britannica – verbete 'Castle'")
tf(H, "Antiguidade", 1, 8, "Os Jogos Olímpicos foram criados pelos antigos gregos.", True,
   "Os primeiros jogos registrados aconteceram em Olímpia, em 776 a.C.",
   "Enciclopédia Britannica – verbete 'Olympic Games'")
mc(H, "Antiguidade", 1, 8, "Como se chamavam os lutadores que enfrentavam uns aos outros nas arenas da Roma Antiga?",
   ["Gladiadores", "Samurais", "Vikings", "Mosqueteiros"], "Gladiadores",
   "O Coliseu de Roma recebia lutas de gladiadores para milhares de espectadores.",
   "Enciclopédia Britannica – verbete 'Gladiator'")
op(H, "pré-história", 2, 10, "Que nome se dá ao período da história humana antes da invenção da escrita?",
   "Pré-história", ["pré-história", "pre-historia", "pré história", "pre historia", "prehistoria"],
   "A escrita surgiu há cerca de 5 mil anos, na Mesopotâmia.",
   "Enciclopédia Britannica – verbete 'Prehistory'")
tf(H, "Brasil Império", 2, 12, "Dom Pedro I nasceu em Portugal.", True,
   "Ele nasceu em 1798 no Palácio de Queluz, perto de Lisboa.",
   "Enciclopédia Britannica – verbete 'Pedro I'", br=True)
mc(H, "povos antigos", 2, 12, "Qual povo construiu a cidade de Chichén Itzá e criou um calendário famoso?",
   ["Maias", "Incas", "Astecas", "Egípcios"], "Maias",
   "Chichén Itzá fica na península de Yucatán, no México.",
   "UNESCO – Patrimônio Mundial")
mc(H, "ciência", 2, 12, "Qual cientista italiano foi julgado pela Inquisição por defender que a Terra gira em torno do Sol?",
   ["Galileu Galilei", "Leonardo da Vinci", "Isaac Newton", "Charles Darwin"], "Galileu Galilei",
   "Com um telescópio, Galileu descobriu quatro luas de Júpiter.",
   "Enciclopédia Britannica – verbete 'Galileo'")
mc(H, "invenções", 2, 12, "Qual invenção de Gutenberg, por volta de 1450, facilitou a produção de livros?",
   ["Prensa de tipos móveis", "Máquina de escrever", "Fotocopiadora", "Lápis"], "Prensa de tipos móveis",
   "A Bíblia de Gutenberg está entre os primeiros livros impressos na Europa.",
   "Enciclopédia Britannica – verbete 'Johannes Gutenberg'")
mc(H, "Antiguidade", 2, 12, "Qual cidade romana foi soterrada pela erupção do vulcão Vesúvio, no ano 79?",
   ["Pompeia", "Veneza", "Florença", "Milão"], "Pompeia",
   "As cinzas preservaram casas, pinturas e até o formato do corpo das vítimas.",
   "UNESCO – Patrimônio Mundial")
mc(H, "realeza", 2, 14, "Qual rainha deu nome a toda uma era do Reino Unido, no século XIX?",
   ["Vitória", "Elizabeth I", "Maria Antonieta", "Isabel de Castela"], "Vitória",
   "A rainha Vitória reinou de 1837 a 1901.",
   "Enciclopédia Britannica – verbete 'Victoria'")
tf(H, "escravidão", 3, 14, "O Brasil foi o último país das Américas a abolir a escravidão.", True,
   "A Lei Áurea, de 1888, encerrou a escravidão legal no país.",
   "Arquivo Nacional", br=True)
mc(H, "Revolução Francesa", 3, 14, "Qual rei da França foi guilhotinado em 1793, durante a Revolução Francesa?",
   ["Luís XVI", "Luís XIV", "Carlos Magno", "Henrique VIII"], "Luís XVI",
   "Sua esposa, Maria Antonieta, também foi guilhotinada no mesmo ano.",
   "Enciclopédia Britannica – verbete 'Louis XVI'")
mc(H, "Brasil República", 3, 14, "Como ficou conhecida a revolta de marinheiros de 1910, liderada por João Cândido?",
   ["Revolta da Chibata", "Revolta da Armada", "Revolta da Vacina", "Guerra de Canudos"], "Revolta da Chibata",
   "Os marinheiros protestavam contra os castigos físicos; João Cândido ficou conhecido como 'Almirante Negro'.",
   "Arquivo Nacional", br=True)
mc(H, "Astecas", 3, 14, "Qual era a capital do Império Asteca?",
   ["Tenochtitlán", "Cusco", "Machu Picchu", "Teotihuacán"], "Tenochtitlán",
   "Sobre as ruínas de Tenochtitlán foi construída a Cidade do México.",
   "Enciclopédia Britannica – verbete 'Tenochtitlán'")
mc(H, "Brasil Colônia", 3, 16, "Qual movimento de 1798, na Bahia, também ficou conhecido como Revolta dos Alfaiates?",
   ["Conjuração Baiana", "Sabinada", "Balaiada", "Cabanagem"], "Conjuração Baiana",
   "Entre os participantes havia alfaiates, soldados e pessoas escravizadas e libertas.",
   "Arquivo Nacional", br=True)
mc(H, "Idade Média", 4, 16, "Qual guerra entre Inglaterra e França durou, com pausas, de 1337 a 1453?",
   ["Guerra dos Cem Anos", "Guerra dos Trinta Anos", "Guerra das Rosas", "Guerra da Crimeia"], "Guerra dos Cem Anos",
   "Joana d'Arc lutou nessa guerra pelo lado francês.",
   "Enciclopédia Britannica – verbete 'Hundred Years' War'")

# =========================================================== POLÍTICA
P = "pol"
mc(P, "cidadania", 1, 6, "Onde o pedestre deve atravessar a rua?",
   ["Na faixa de pedestres", "No meio dos carros", "Na curva", "Em qualquer lugar"], "Na faixa de pedestres",
   "Onde houver semáforo para pedestres, é preciso esperar o boneco verde.",
   "Código de Trânsito Brasileiro", br=True)
tf(P, "cidadania", 1, 8, "Pelas leis de trânsito, crianças menores de 10 anos devem viajar no banco de trás do carro.", True,
   "O Código de Trânsito também exige cadeirinha ou assento de elevação conforme a idade.",
   "Código de Trânsito Brasileiro", br=True)
mc(P, "eleições", 1, 8, "Quem escolhe o prefeito de uma cidade?",
   ["Os eleitores da cidade", "O presidente", "O governador", "Os vereadores"], "Os eleitores da cidade",
   "O prefeito é eleito pelo voto direto da população do município.",
   "Tribunal Superior Eleitoral", br=True)
mc(P, "cidadania", 1, 9, "Como se chama a pessoa que tem direitos e deveres garantidos pelas leis do seu país?",
   ["Cidadão", "Turista", "Visitante", "Estrangeiro"], "Cidadão",
   "Votar, estudar e respeitar as leis fazem parte da cidadania.",
   "Câmara dos Deputados – Plenarinho")
op(P, "mandatos", 2, 10, "Quantos anos dura o mandato de um prefeito no Brasil?", "4 anos",
   ["4", "quatro", "4 anos", "quatro anos"],
   "Prefeitos e vereadores são eleitos juntos, na mesma eleição municipal.",
   "Constituição Federal de 1988", br=True)
mc(P, "mandatos", 2, 12, "Quanto tempo dura o mandato de um deputado federal?",
   ["4 anos", "5 anos", "6 anos", "8 anos"], "4 anos",
   "Já os senadores têm mandato de 8 anos.",
   "Câmara dos Deputados", br=True)
mc(P, "leis", 2, 12, "Como se chama a proposta que os parlamentares discutem e votam antes de ela virar lei?",
   ["Projeto de lei", "Sentença", "Alvará", "Certidão"], "Projeto de lei",
   "Qualquer cidadão pode acompanhar a tramitação dos projetos nos sites do Congresso.",
   "Câmara dos Deputados", br=True)
mc(P, "documentos", 2, 12, "O que significa a sigla RG, nome popular da carteira de identidade?",
   ["Registro Geral", "Registro Governamental", "Relação Geral", "Registro de Garantia"], "Registro Geral",
   "O RG é emitido pelo órgão de identificação de cada estado.",
   "Governo Federal – gov.br", br=True)
mc(P, "direitos", 2, 12, "Qual é o número do Disque Direitos Humanos, que recebe denúncias de violações de direitos?",
   ["100", "180", "188", "192"], "100",
   "A ligação é gratuita, funciona 24 horas e pode ser anônima.",
   "Governo Federal – gov.br", br=True)
mc(P, "organizações", 2, 12, "Qual bloco econômico foi criado em 1991 por Brasil, Argentina, Paraguai e Uruguai?",
   ["Mercosul", "União Europeia", "Otan", "Opep"], "Mercosul",
   "O bloco nasceu com o Tratado de Assunção.",
   "Ministério das Relações Exteriores", br=True)
tf(P, "eleições", 2, 14, "No Brasil, o voto é obrigatório para quem não sabe ler nem escrever.", False,
   "A Constituição torna o voto facultativo para analfabetos, para maiores de 70 anos e para jovens de 16 e 17 anos.",
   "Constituição Federal de 1988", br=True)
mc(P, "leis", 2, 14, "Quem sanciona ou veta as leis aprovadas pelo Congresso Nacional?",
   ["O presidente da República", "O presidente do Supremo", "O presidente do Senado", "O Tribunal Superior Eleitoral"],
   "O presidente da República",
   "Se o presidente vetar, o Congresso pode derrubar o veto em votação.",
   "Constituição Federal de 1988", br=True)
tf(P, "Congresso", 3, 14, "Pela Constituição, os senadores representam os estados e os deputados federais representam o povo.", True,
   "Por isso cada estado tem o mesmo número de senadores, enquanto os deputados variam com a população.",
   "Constituição Federal de 1988", br=True)
mc(P, "instituições", 3, 14, "Como se chama o processo em que o Congresso pode afastar o presidente por crime de responsabilidade?",
   ["Impeachment", "Plebiscito", "Referendo", "Veto"], "Impeachment",
   "A Câmara autoriza a abertura do processo e o Senado faz o julgamento.",
   "Constituição Federal de 1988", br=True)
mc(P, "organizações", 3, 14, "Qual organização, criada em 1948, reúne os países do continente americano?",
   ["OEA", "Otan", "União Europeia", "Liga Árabe"], "OEA",
   "A Organização dos Estados Americanos tem sede em Washington.",
   "Organização dos Estados Americanos")
mc(P, "história política", 3, 14, "Em qual cidade foi aprovada a Declaração de Independência dos Estados Unidos, em 1776?",
   ["Filadélfia", "Washington", "Nova York", "Chicago"], "Filadélfia",
   "O documento foi aprovado em 4 de julho, data nacional dos Estados Unidos.",
   "Arquivos Nacionais dos EUA")
op(P, "Brasil Império", 4, 16, "Como se chamava o quarto Poder, exclusivo do imperador, criado pela Constituição de 1824?",
   "Poder Moderador", ["poder moderador", "moderador"],
   "Ele permitia ao imperador, por exemplo, dissolver a Câmara dos Deputados.",
   "Senado Federal – Constituições Brasileiras", br=True)

# =========================================================== CULTURA BRASILEIRA
C = "cul"
mc(C, "brincadeiras", 1, 6, "Qual brinquedo feito de papel e varetas as crianças soltam no céu, também chamado de papagaio?",
   ["Pipa", "Pião", "Ioiô", "Bolinha de gude"], "Pipa",
   "Dependendo da região, a pipa também é chamada de arraia, raia ou pandorga.",
   "IPHAN – Brinquedos e brincadeiras", br=True)
mc(C, "festas juninas", 1, 6, "Qual brincadeira de festa junina usa uma varinha com anzol para pegar prêmios?",
   ["Pescaria", "Corrida do saco", "Boca do palhaço", "Correio elegante"], "Pescaria",
   "Nas barracas de pescaria, cada peixinho tem um número que vale um brinde.",
   "IPHAN – Festas juninas", br=True)
tf(C, "festas", 1, 7, "O Carnaval brasileiro acontece no mês de dezembro.", False,
   "O Carnaval acontece em fevereiro ou março, antes da Quaresma.",
   "Enciclopédia Britannica – verbete 'Carnival'", br=True)
tf(C, "festas juninas", 1, 8, "Nas festas juninas, muita gente se veste de caipira.", True,
   "Chapéu de palha, camisa xadrez e vestido de chita são as roupas mais comuns.",
   "IPHAN – Festas juninas", br=True)
mc(C, "doces", 1, 8, "Qual doce é feito de coco ralado e açúcar e vendido em pedaços nas praias?",
   ["Cocada", "Pé de moleque", "Brigadeiro", "Pamonha"], "Cocada",
   "Existem cocadas brancas, queimadas e até de maracujá.",
   "Câmara Cascudo – História da Alimentação no Brasil", br=True)
mc(C, "tradições", 1, 9, "Como se chama o homem do campo do Rio Grande do Sul que usa bombacha e lenço no pescoço?",
   ["Gaúcho", "Caiçara", "Jangadeiro", "Seringueiro"], "Gaúcho",
   "O gaúcho também vive em partes do Uruguai e da Argentina.",
   "Movimento Tradicionalista Gaúcho", br=True)
mc(C, "festas", 2, 12, "Qual cidade paulista é famosa pela Festa do Peão de Boiadeiro, um dos maiores rodeios do país?",
   ["Barretos", "Gramado", "Petrópolis", "Caruaru"], "Barretos",
   "A festa de Barretos acontece desde 1956.",
   "IBGE – Cidades", br=True)
mc(C, "patrimônio", 2, 12, "Em qual cidade fica o Pelourinho, bairro histórico famoso pelo casario colorido e pelos tambores do Olodum?",
   ["Salvador", "Recife", "São Luís", "Fortaleza"], "Salvador",
   "O centro histórico de Salvador é Patrimônio Mundial da UNESCO desde 1985.",
   "UNESCO – Patrimônio Mundial", br=True)
mc(C, "religiosidade", 2, 12, "A cidade de Juazeiro do Norte, centro de devoção ao Padre Cícero, fica em qual estado?",
   ["Ceará", "Bahia", "Pernambuco", "Paraíba"], "Ceará",
   "A cidade recebe romeiros de todo o Nordeste o ano inteiro.",
   "IBGE – Cidades", br=True)
tf(C, "patrimônio", 2, 12, "O Teatro Amazonas, inaugurado em 1896, fica em Belém.", False,
   "O teatro fica em Manaus e foi construído no auge do ciclo da borracha.",
   "IPHAN", br=True)
mc(C, "danças", 2, 12, "Qual dança de roda do Pará, com saias rodadas e tambores, tem nome de origem indígena?",
   ["Carimbó", "Xote", "Frevo", "Axé"], "Carimbó",
   "O carimbó é reconhecido como Patrimônio Cultural do Brasil pelo IPHAN.",
   "IPHAN", br=True)
tf(C, "patrimônio", 2, 14, "O samba de roda do Recôncavo Baiano foi reconhecido pela UNESCO como patrimônio da humanidade.", True,
   "O reconhecimento veio em 2005, como obra-prima do patrimônio oral e imaterial.",
   "UNESCO – Patrimônio Imaterial", br=True)
op(C, "festas", 3, 14, "Qual cidade gaúcha é famosa pela tradicional Festa da Uva?", "Caxias do Sul",
   ["caxias do sul", "caxias"],
   "A festa começou em 1931 e celebra a imigração italiana na Serra Gaúcha.",
   "IBGE – Cidades", br=True)
mc(C, "cidades históricas", 3, 14, "Qual cidade histórica do litoral fluminense sedia a Festa Literária Internacional, a Flip?",
   ["Paraty", "Petrópolis", "Ouro Preto", "Tiradentes"], "Paraty",
   "Paraty e Ilha Grande viraram Patrimônio Mundial da UNESCO em 2019.",
   "UNESCO – Patrimônio Mundial", br=True)
mc(C, "museus", 3, 16, "Em qual cidade mineira fica o Instituto Inhotim, grande museu de arte a céu aberto?",
   ["Brumadinho", "Tiradentes", "Mariana", "Diamantina"], "Brumadinho",
   "O Inhotim reúne obras de arte contemporânea no meio de um enorme jardim botânico.",
   "IBGE – Cidades", br=True)
mc(C, "artes", 4, 16, "Qual artista nascido na Argentina ficou famoso por retratar Salvador e os orixás do candomblé?",
   ["Carybé", "Portinari", "Di Cavalcanti", "Volpi"], "Carybé",
   "Seus painéis com os orixás estão no Museu Afro-Brasileiro, em Salvador.",
   "Enciclopédia Itaú Cultural – verbete 'Carybé'", br=True)
mc(C, "festas", 4, 16, "Em Pirenópolis, Goiás, as Cavalhadas que encenam batalhas entre mouros e cristãos fazem parte de qual festa?",
   ["Festa do Divino", "Festa de Iemanjá", "Círio de Nazaré", "Lavagem do Bonfim"], "Festa do Divino",
   "A Festa do Divino de Pirenópolis é Patrimônio Cultural do Brasil.",
   "IPHAN", br=True)

# =========================================================== NOVELAS
N = "nov"
mc(N, "personagens", 1, 6, "Como se chama o personagem malvado de uma novela?",
   ["Vilão", "Mocinho", "Galã", "Figurante"], "Vilão",
   "Muitos vilões de novela fazem tanto sucesso que viram assunto no país inteiro.",
   "Memória Globo")
op(N, "personagens", 1, 8, "Como se chama, nas novelas, o personagem bonzinho, o contrário do vilão?", "Mocinho",
   ["mocinho", "mocinha", "herói", "heroi", "heroína", "heroina"],
   "Nas novelas, o público costuma torcer para o mocinho ficar com o par romântico no final.",
   "Memória Globo")
mc(N, "novelas infantis", 1, 8, "Qual novela do SBT, de 2018, conta a história de uma menina órfã que pratica o 'jogo do contente'?",
   ["As Aventuras de Poliana", "Carrossel", "Chiquititas", "Cúmplices de um Resgate"], "As Aventuras de Poliana",
   "A história é inspirada no livro 'Pollyanna', da americana Eleanor H. Porter.",
   "SBT", br=True)
mc(N, "personagens", 1, 10, "Como se chama o personagem principal de uma história?",
   ["Protagonista", "Figurante", "Antagonista", "Contrarregra"], "Protagonista",
   "O antagonista é quem se opõe ao protagonista, muitas vezes o vilão.",
   "Memória Globo")
tf(N, "novelas estrangeiras", 1, 10, "A novela mexicana 'Rebelde', exibida pelo SBT, deu origem à banda RBD.", True,
   "A banda formada pelo elenco fez shows lotados no Brasil.",
   "SBT")
mc(N, "elenco", 2, 14, "Em 'Avenida Brasil' (2012), qual ator interpretou o ex-jogador de futebol Tufão?",
   ["Murilo Benício", "Cauã Reymond", "Marcos Palmeira", "Tony Ramos"], "Murilo Benício",
   "Tufão era casado com a vilã Carminha.",
   "Memória Globo", br=True)
mc(N, "elenco", 2, 14, "Em 'Senhora do Destino' (2004), qual atriz interpretou a vilã Nazaré Tedesco?",
   ["Renata Sorrah", "Beatriz Segall", "Christiane Torloni", "Adriana Esteves"], "Renata Sorrah",
   "Anos depois, uma cena de Nazaré fazendo contas virou meme no mundo todo.",
   "Memória Globo", br=True)
mc(N, "elenco", 2, 14, "Em 'Senhora do Destino', qual atriz viveu a protagonista Maria do Carmo na maior parte da novela?",
   ["Susana Vieira", "Regina Duarte", "Glória Pires", "Vera Fischer"], "Susana Vieira",
   "Na primeira fase, a jovem Maria do Carmo foi vivida por Carolina Dieckmann.",
   "Memória Globo", br=True)
mc(N, "personagens", 2, 14, "Qual era o nome do prefeito de Sucupira na novela 'O Bem-Amado' (1973)?",
   ["Odorico Paraguaçu", "Sinhozinho Malta", "Zeca Diabo", "Roque Santeiro"], "Odorico Paraguaçu",
   "Odorico foi interpretado por Paulo Gracindo.",
   "Memória Globo", br=True)
tf(N, "história da TV", 3, 16, "'O Bem-Amado', de 1973, foi a primeira novela em cores da TV brasileira.", True,
   "A novela de Dias Gomes estreou pouco depois do início das transmissões em cores no país.",
   "Memória Globo", br=True)
mc(N, "elenco", 3, 16, "Qual atriz interpretou Juma Marruá na primeira versão de 'Pantanal', em 1990?",
   ["Cristiana Oliveira", "Luana Piovani", "Ana Paula Arósio", "Giovanna Antonelli"], "Cristiana Oliveira",
   "A novela da Rede Manchete chegou a vencer a Globo na audiência.",
   "Enciclopédia Itaú Cultural", br=True)
mc(N, "história da TV", 3, 16, "Qual novela da Globo foi proibida pela censura em 1975 e só estreou dez anos depois, em 1985?",
   ["Roque Santeiro", "Vale Tudo", "Dancin' Days", "Irmãos Coragem"], "Roque Santeiro",
   "A versão de 1985 virou um dos maiores sucessos da história da TV brasileira.",
   "Memória Globo", br=True)
mc(N, "elenco", 3, 16, "Qual atriz interpretou a protagonista de 'A Escrava Isaura', de 1976?",
   ["Lucélia Santos", "Regina Duarte", "Sônia Braga", "Vera Fischer"], "Lucélia Santos",
   "A novela fez de Lucélia Santos uma estrela até na China.",
   "Memória Globo", br=True)
tf(N, "elenco", 3, 16, "Sônia Braga foi a protagonista da novela 'Gabriela', de 1975.", True,
   "A novela adaptou o romance 'Gabriela, Cravo e Canela', de Jorge Amado.",
   "Memória Globo", br=True)
op(N, "autores", 3, 16, "Qual autor escreveu 'Roque Santeiro' junto com Aguinaldo Silva?", "Dias Gomes",
   ["dias gomes", "alfredo dias gomes"],
   "Dias Gomes também foi autor de 'O Bem-Amado' e 'Saramandaia'.",
   "Memória Globo", br=True)
mc(N, "cenários", 4, 16, "Em qual cidade fictícia se passava a novela 'Tieta' (1989)?",
   ["Santana do Agreste", "Asa Branca", "Sucupira", "Ilhéus"], "Santana do Agreste",
   "A cidade baiana inventada por Jorge Amado fica no livro 'Tieta do Agreste'.",
   "Memória Globo", br=True)
mc(N, "história da TV", 4, 16, "Qual foi a primeira novela da TV Globo, exibida em 1965?",
   ["Ilusões Perdidas", "Irmãos Coragem", "Selva de Pedra", "Véu de Noiva"], "Ilusões Perdidas",
   "A novela foi ao ar no mesmo ano em que a emissora foi inaugurada.",
   "Memória Globo", br=True)

# =========================================================== TELEVISÃO
T = "tv"
mc(T, "desenhos", 1, 6, "No desenho 'Bob Esponja', dentro de que fruta ele mora?",
   ["Abacaxi", "Coco", "Melancia", "Laranja"], "Abacaxi",
   "A casa-abacaxi fica no fundo do mar, na Fenda do Biquíni.",
   "Nickelodeon")
mc(T, "desenhos", 1, 6, "Qual desenho tem uma menina exploradora com uma mochila falante e o macaco Botas?",
   ["Dora, a Aventureira", "Peppa Pig", "Masha e o Urso", "Doutora Brinquedos"], "Dora, a Aventureira",
   "Dora ensina palavras em outra língua durante as aventuras.",
   "Nickelodeon")
mc(T, "programas infantis", 1, 7, "No 'Sítio do Picapau Amarelo', quem é a cozinheira famosa pelos bolinhos?",
   ["Tia Nastácia", "Dona Benta", "Emília", "Narizinho"], "Tia Nastácia",
   "Foi Tia Nastácia quem costurou a boneca Emília.",
   "Monteiro Lobato – Reinações de Narizinho", br=True)
mc(T, "desenhos", 1, 7, "Qual coelho dos desenhos tem o bordão 'O que é que há, velhinho'?",
   ["Pernalonga", "Patolino", "Piu-Piu", "Frajola"], "Pernalonga",
   "Pernalonga é o personagem mais famoso dos 'Looney Tunes'.",
   "Warner Bros.")
tf(T, "desenhos", 1, 8, "Os Jetsons são uma família de desenho animado que vive no futuro, com carros voadores.", True,
   "O desenho foi criado pelos estúdios Hanna-Barbera, os mesmos de 'Os Flintstones'.",
   "Enciclopédia Britannica – verbete 'Hanna-Barbera'")
mc(T, "desenhos", 1, 9, "Qual desenho mostra quatro tartarugas que lutam artes marciais e moram nos esgotos?",
   ["Tartarugas Ninja", "Thundercats", "Power Rangers", "Os Smurfs"], "Tartarugas Ninja",
   "Leonardo, Michelangelo, Donatello e Rafael têm nomes de artistas italianos.",
   "Nickelodeon")
op(T, "seriados", 1, 9, "No seriado 'Chaves', qual é o nome do menino que usa roupa de marinheiro?", "Quico",
   ["quico", "kiko"],
   "Quico vive dizendo 'Você não vai com a minha cara?'.",
   "Televisa")
mc(T, "seriados", 2, 9, "No seriado 'Chaves', qual moradora as crianças chamam de 'bruxa do 71'?",
   ["Dona Clotilde", "Dona Florinda", "Chiquinha", "Paty"], "Dona Clotilde",
   "Dona Clotilde é apaixonada pelo Seu Madruga.",
   "Televisa")
mc(T, "desenhos", 2, 10, "Em 'Os Simpsons', qual é o nome da mãe da família, dona de um enorme cabelo azul?",
   ["Marge", "Lisa", "Maggie", "Patty"], "Marge",
   "Marge é casada com Homer e mãe de Bart, Lisa e Maggie.",
   "Enciclopédia Britannica – verbete 'The Simpsons'")
mc(T, "programas infantis", 2, 10, "Em 'Castelo Rá-Tim-Bum', que animal é a Celeste?",
   ["Cobra", "Gata", "Coruja", "Rato"], "Cobra",
   "Celeste vive numa árvore dentro do castelo.",
   "TV Cultura", br=True)
mc(T, "humor", 2, 12, "Qual humorista criou e interpretou o personagem Didi, de 'Os Trapalhões'?",
   ["Renato Aragão", "Dedé Santana", "Chico Anysio", "Jô Soares"], "Renato Aragão",
   "Renato Aragão é cearense, de Sobral.",
   "Memória Globo", br=True)
tf(T, "seriados", 2, 12, "'Chapolin Colorado' foi criado pelo mesmo autor de 'Chaves'.", True,
   "Os dois personagens foram criados e interpretados por Roberto Gómez Bolaños.",
   "Televisa")
mc(T, "humor", 2, 14, "Em qual série da Globo Fernanda Torres e Luiz Fernando Guimarães viviam o casal Vani e Rui?",
   ["Os Normais", "Sai de Baixo", "A Grande Família", "Toma Lá, Dá Cá"], "Os Normais",
   "A série também virou filme, lançado em 2003.",
   "Memória Globo", br=True)
mc(T, "séries", 2, 14, "Em 'Friends', qual personagem toca violão e canta a música 'Smelly Cat'?",
   ["Phoebe", "Rachel", "Monica", "Joey"], "Phoebe",
   "Phoebe tem uma irmã gêmea chamada Ursula.",
   "Enciclopédia Britannica – verbete 'Friends'")
tf(T, "telejornais", 3, 14, "O 'Jornal Nacional' foi o primeiro telejornal transmitido em rede nacional no Brasil.", True,
   "Ele estreou em 1º de setembro de 1969.",
   "Memória Globo", br=True)
mc(T, "séries", 3, 14, "Qual série britânica mostra um viajante do tempo chamado 'Doutor', que viaja numa cabine azul?",
   ["Doctor Who", "Sherlock", "Black Mirror", "Downton Abbey"], "Doctor Who",
   "A série estreou na BBC em 1963.",
   "BBC")
mc(T, "humor", 4, 16, "Qual dos Trapalhões tinha o nome verdadeiro de Antônio Carlos Bernardes Gomes?",
   ["Mussum", "Zacarias", "Dedé", "Didi"], "Mussum",
   "Mussum também era sambista do grupo Os Originais do Samba.",
   "Memória Globo", br=True)
