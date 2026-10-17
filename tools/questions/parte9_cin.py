# Perguntas novas: cinema. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "cin"

# =========================================================== FÁCEIS
mc(T, "sala de cinema", 1, 6, "Como se chama o grande painel branco onde o filme aparece na sala de cinema?",
   ["Tela", "Cortina", "Tapete", "Janela"], "Tela",
   "O projetor lança a luz com as imagens do filme sobre a tela, no fundo da sala escura.",
   "Enciclopédia Britannica – verbete 'Motion picture'")
mc(T, "super-heróis", 1, 6, "Qual super-herói voa usando uma armadura vermelha e dourada?",
   ["Homem de Ferro", "Capitão América", "Thor", "Hulk"], "Homem de Ferro",
   "Tony Stark é um inventor que construiu a própria armadura para se tornar o Homem de Ferro.",
   "Marvel – personagem 'Iron Man'")
mc(T, "franquias", 1, 7, "Em 'Star Wars', que arma brilhante os cavaleiros jedi usam nas lutas?",
   ["Sabre de luz", "Martelo", "Arco e flecha", "Lança"], "Sabre de luz",
   "O sabre de luz tem uma lâmina de energia que brilha e faz um zumbido característico.",
   "Lucasfilm – StarWars.com, verbete 'Lightsaber'")
tf(T, "super-heróis", 1, 7, "O Homem-Aranha usa uma capa vermelha comprida.", False,
   "O uniforme do Homem-Aranha é vermelho e azul, coberto de teias, mas não tem capa.",
   "Marvel – personagem 'Spider-Man'")
mc(T, "super-heróis", 1, 8, "Qual super-herói da Marvel consegue ficar minúsculo e conversa com formigas?",
   ["Homem-Formiga", "Gavião Arqueiro", "Falcão", "Visão"], "Homem-Formiga",
   "O Homem-Formiga usa um traje que o encolhe e um capacete que comanda as formigas.",
   "Marvel – personagem 'Ant-Man'")
mc(T, "franquias", 1, 7, "Nos filmes de Harry Potter, em que os bruxos montam para voar?",
   ["Vassoura", "Tapete", "Guarda-chuva", "Bicicleta"], "Vassoura",
   "Os bruxos voam em vassouras e até disputam partidas de quadribol montados nelas.",
   "Warner Bros. – Wizarding World")
mc(T, "franquias", 1, 7, "Qual é o formato da cicatriz que Harry Potter tem na testa?",
   ["Raio", "Estrela", "Lua", "Coração"], "Raio",
   "A cicatriz em forma de raio ficou depois do ataque de Voldemort quando Harry era bebê.",
   "Warner Bros. – Wizarding World")
mc(T, "franquias", 1, 8, "Em 'Star Wars', qual é o nome do robozinho azul e branco que se comunica com apitos?",
   ["R2-D2", "C-3PO", "BB-8", "WALL-E"], "R2-D2",
   "R2-D2 é o inseparável companheiro do robô dourado C-3PO desde o primeiro filme, de 1977.",
   "Lucasfilm – StarWars.com, verbete 'R2-D2'")
mc(T, "franquias", 1, 9, "Em 'Star Wars', qual é o nome do copiloto alto e peludo de Han Solo?",
   ["Chewbacca", "Yoda", "Jabba", "Lando"], "Chewbacca",
   "Chewbacca é um wookiee, espécie de grandes seres peludos, e pilota a nave Millennium Falcon com Han Solo.",
   "Lucasfilm – StarWars.com, verbete 'Chewbacca'")
tf(T, "super-heróis", 1, 8, "O Batman não tem superpoderes: ele usa inteligência, treino e equipamentos.", True,
   "Bruce Wayne é um humano comum que se preparou durante anos e conta com muitos aparelhos.",
   "DC – personagem 'Batman'")
op(T, "prêmios", 1, 8, "De que cor é o famoso tapete por onde os artistas chegam à festa do Oscar?", "Vermelho",
   ["vermelho", "vermelha"],
   "O tapete vermelho virou símbolo das grandes estreias e das cerimônias de premiação.",
   "Academy of Motion Picture Arts and Sciences – Oscars.org")
mc(T, "gêneros", 1, 8, "Como se chama o tipo de filme feito para dar medo em quem assiste?",
   ["Terror", "Comédia", "Musical", "Romance"], "Terror",
   "Os filmes de terror usam sustos, escuridão e monstros para assustar o público.",
   "Enciclopédia Britannica – verbete 'Horror film'")
mc(T, "gêneros", 1, 9, "Como se chama o tipo de filme em que os personagens cantam e dançam para contar a história?",
   ["Musical", "Faroeste", "Documentário", "Suspense"], "Musical",
   "Nos musicais, as canções fazem parte da história, como em 'Cantando na Chuva' e 'A Noviça Rebelde'.",
   "Enciclopédia Britannica – verbete 'Musical film'")
mc(T, "profissões do cinema", 1, 8, "Como se chama o trabalho de gravar em português as falas de um filme estrangeiro?",
   ["Dublagem", "Legenda", "Maquiagem", "Figurino"], "Dublagem",
   "Na dublagem, atores gravam as falas em português no lugar das vozes originais.",
   "Enciclopédia Britannica – verbete 'Dubbing'")
op(T, "profissões do cinema", 1, 8, "Como se chama o profissional que substitui o ator em cenas perigosas, como quedas e lutas?",
   "Dublê", ["dublê", "duble", "dublê de ação", "dublês"],
   "O dublê é treinado para fazer acrobacias com segurança no lugar do ator.",
   "Enciclopédia Britannica – verbete 'Stunt performer'")
tf(T, "sala de cinema", 1, 7, "Para ver um filme em 3D no cinema, normalmente é preciso usar óculos especiais.", True,
   "Os óculos fazem cada olho ver uma imagem um pouco diferente, e o cérebro junta as duas dando a sensação de profundidade.",
   "Enciclopédia Britannica – verbete '3-D film'")
mc(T, "franquias", 1, 9, "Nos filmes de Harry Potter, qual é o nome do meio-gigante que cuida dos animais de Hogwarts?",
   ["Hagrid", "Snape", "Dobby", "Filch"], "Hagrid",
   "Rúbeo Hagrid é o guarda-caça de Hogwarts e foi quem contou a Harry que ele era bruxo.",
   "Warner Bros. – Wizarding World")
mc(T, "vilões", 1, 10, "Qual vilão gigante e roxo da Marvel junta as Joias do Infinito numa luva?",
   ["Thanos", "Loki", "Ultron", "Galactus"], "Thanos",
   "Em 'Vingadores: Guerra Infinita', Thanos estala os dedos com a manopla e faz metade dos seres vivos sumir.",
   "Marvel – personagem 'Thanos'")
mc(T, "franquias", 1, 9, "Nos filmes de Harry Potter, qual é o nome do melhor amigo ruivo de Harry?",
   ["Rony Weasley", "Draco Malfoy", "Neville Longbottom", "Cedrico Diggory"], "Rony Weasley",
   "Rony vem de uma família grande de bruxos ruivos, os Weasley.",
   "Warner Bros. – Wizarding World", syn=("rony",))
mc(T, "franquias", 1, 9, "Em qual casa de Hogwarts Harry Potter fica?",
   ["Grifinória", "Sonserina", "Corvinal", "Lufa-Lufa"], "Grifinória",
   "O Chapéu Seletor colocou Harry na Grifinória, a casa da coragem, cujo símbolo é um leão.",
   "Warner Bros. – Wizarding World")
op(T, "frases célebres", 1, 10, "Em 'Star Wars', os personagens desejam boa sorte dizendo: 'Que a ... esteja com você'. Que palavra completa a frase?",
   "Força", ["força", "a força"],
   "A Força é a energia que dá poderes aos jedi e também aos vilões sith.",
   "Lucasfilm – StarWars.com, verbete 'The Force'")
mc(T, "cinema brasileiro", 1, 10, "Em 'O Auto da Compadecida', Chicó termina suas histórias dizendo: 'Não sei, só sei que...'. Como a frase termina?",
   ["Foi assim", "Era verdade", "Eu vi", "Aconteceu"], "Foi assim",
   "O bordão 'Não sei, só sei que foi assim', dito por Selton Mello, virou um dos mais lembrados do cinema brasileiro.",
   "Globo Filmes – 'O Auto da Compadecida' (2000)", br=True)
mc(T, "divulgação", 1, 9, "Como se chama o vídeo curto com cenas de um filme, feito para divulgá-lo antes da estreia?",
   ["Trailer", "Legenda", "Roteiro", "Claquete"], "Trailer",
   "O nome vem do inglês e significa 'reboque', porque no início ele passava depois do filme principal.",
   "Enciclopédia Britannica – verbete 'Trailer'", syn=("trêiler",))
mc(T, "gêneros", 1, 10, "Como se chama o filme que mostra fatos e pessoas reais, sem uma história inventada?",
   ["Documentário", "Ficção científica", "Animação", "Comédia"], "Documentário",
   "O documentário registra a realidade, como a vida dos animais, uma viagem ou um acontecimento histórico.",
   "Enciclopédia Britannica – verbete 'Documentary'")
tf(T, "história do cinema", 1, 9, "Os primeiros filmes do cinema já tinham falas gravadas e eram coloridos.", False,
   "Os primeiros filmes eram em preto e branco e mudos; muitas vezes um pianista tocava ao vivo na sala.",
   "Enciclopédia Britannica – verbete 'Silent film'")
mc(T, "cinema brasileiro", 1, 10, "Em 'Central do Brasil', o menino Josué viaja pelo sertão à procura de quem?",
   ["Do pai", "De um tesouro", "De um cachorro", "De um avião"], "Do pai",
   "Depois que a mãe morre, Josué parte com Dora em busca do pai que nunca conheceu.",
   "VideoFilmes – 'Central do Brasil' (1998)", br=True, syn=("o pai", "pai"))
mc(T, "cinema brasileiro", 1, 10, "Em qual região do Brasil se passa a história de 'O Auto da Compadecida'?",
   ["Nordeste", "Sul", "Norte", "Centro-Oeste"], "Nordeste",
   "A história se passa em Taperoá, no sertão da Paraíba, terra de Ariano Suassuna.",
   "Globo Filmes – 'O Auto da Compadecida' (2000)", br=True)

# =========================================================== MÉDIAS
mc(T, "franquias", 2, 10, "Em 'Jurassic Park', o sangue de dinossauro usado pelos cientistas estava dentro de qual inseto preso no âmbar?",
   ["Mosquito", "Formiga", "Abelha", "Besouro"], "Mosquito",
   "No filme, o mosquito picou um dinossauro e ficou preso na resina, que virou âmbar.",
   "Universal Pictures – 'Jurassic Park' (1993)")
mc(T, "clássicos", 2, 9, "No filme 'O Mágico de Oz', de 1939, de que cor são os sapatinhos mágicos de Dorothy?",
   ["Vermelhos", "Azuis", "Verdes", "Amarelos"], "Vermelhos",
   "No livro de L. Frank Baum os sapatos eram prateados, mas o filme colorido os trocou por vermelhos brilhantes.",
   "Smithsonian – National Museum of American History, 'Ruby Slippers'")
op(T, "profissões do cinema", 2, 10, "Como se chama a plaquinha que se bate na frente da câmera antes de filmar cada cena?",
   "Claquete", ["claquete", "claquetes"],
   "A batida da claquete ajuda a sincronizar o som com a imagem na hora da edição.",
   "Enciclopédia Britannica – verbete 'Clapperboard'")
mc(T, "Hollywood", 2, 10, "Na Calçada da Fama de Hollywood, os artistas são homenageados com o que gravado no chão?",
   ["Estrelas", "Corações", "Coroas", "Medalhas"], "Estrelas",
   "Cada homenageado ganha uma estrela de cinco pontas com seu nome na calçada.",
   "Hollywood Chamber of Commerce – Hollywood Walk of Fame")
op(T, "franquias", 2, 9, "Como se chama o esporte jogado em vassouras voadoras nos filmes de Harry Potter?",
   "Quadribol", ["quadribol", "quidditch"],
   "No quadribol, o apanhador tenta pegar o pomo de ouro, uma bolinha dourada com asas.",
   "Warner Bros. – Wizarding World")
tf(T, "vilões", 2, 10, "Em 'Star Wars', Darth Vader luta com um sabre de luz azul.", False,
   "O sabre de Darth Vader é vermelho, a cor dos sabres dos sith, que seguem o lado sombrio da Força.",
   "Lucasfilm – StarWars.com, verbete 'Darth Vader'")
mc(T, "diretores", 2, 12, "Quem criou a saga 'Star Wars' e dirigiu o primeiro filme, de 1977?",
   ["George Lucas", "Steven Spielberg", "James Cameron", "Ridley Scott"], "George Lucas",
   "George Lucas escreveu e dirigiu 'Guerra nas Estrelas' e fundou a produtora Lucasfilm.",
   "Enciclopédia Britannica – verbete 'George Lucas'")
mc(T, "personagens", 2, 12, "Em 'O Senhor dos Anéis', qual criatura obcecada pelo anel o chama de 'meu precioso'?",
   ["Gollum", "Sauron", "Saruman", "Legolas"], "Gollum",
   "Gollum carregou o Um Anel por séculos, e o objeto o deixou magro, pálido e dividido.",
   "Enciclopédia Britannica – verbete 'Gollum'")
tf(T, "diretores", 2, 12, "Os filmes da trilogia 'O Senhor dos Anéis' foram dirigidos por Steven Spielberg.", False,
   "A trilogia foi dirigida pelo neozelandês Peter Jackson e lançada entre 2001 e 2003.",
   "Enciclopédia Britannica – verbete 'Peter Jackson'")
mc(T, "franquias", 2, 12, "Em 'Jogos Vorazes', qual arma a heroína Katniss Everdeen usa?",
   ["Arco e flecha", "Espada", "Lança", "Machado"], "Arco e flecha",
   "Katniss aprendeu a usar o arco caçando para alimentar a família no Distrito 12.",
   "Lionsgate – 'Jogos Vorazes' (2012)")
tf(T, "atores", 2, 14, "Harrison Ford interpretou Indiana Jones e também Han Solo, de 'Star Wars'.", True,
   "Harrison Ford viveu os dois heróis aventureiros, ambos criados por George Lucas.",
   "Enciclopédia Britannica – verbete 'Harrison Ford'")
mc(T, "trilhas sonoras", 2, 12, "A canção 'My Heart Will Go On', cantada por Celine Dion, é tema de qual filme?",
   ["Titanic", "O Guarda-Costas", "Ghost – Do Outro Lado da Vida", "Uma Linda Mulher"], "Titanic",
   "A música ganhou o Oscar de Melhor Canção Original em 1998.",
   "Academy of Motion Picture Arts and Sciences – Oscars.org")
mc(T, "história do cinema", 2, 12, "Quais irmãos franceses fizeram uma das primeiras sessões públicas e pagas de cinema, em Paris, em 1895?",
   ["Irmãos Lumière", "Irmãos Wright", "Irmãos Grimm", "Irmãos Montgolfier"], "Irmãos Lumière",
   "Auguste e Louis Lumière exibiram seus filmes curtos com o cinematógrafo, aparelho que filmava e projetava.",
   "Enciclopédia Britannica – verbete 'Lumière brothers'", syn=("lumière", "lumiere"))
tf(T, "prêmios", 2, 12, "A cerimônia do Oscar costuma acontecer em Nova York.", False,
   "A festa acontece em Los Angeles, no Dolby Theatre, em Hollywood.",
   "Academy of Motion Picture Arts and Sciences – Oscars.org")
mc(T, "cinema brasileiro", 2, 14, "Em 'Tropa de Elite', o Capitão Nascimento faz parte de qual tropa da polícia do Rio de Janeiro?",
   ["BOPE", "FBI", "Interpol", "Exército"], "BOPE",
   "O BOPE é o Batalhão de Operações Policiais Especiais da Polícia Militar do Rio.",
   "Zazen Produções – 'Tropa de Elite' (2007)", br=True)
tf(T, "cinema brasileiro", 2, 14, "A história do filme 'Tropa de Elite' se passa em São Paulo.", False,
   "O filme se passa no Rio de Janeiro e acompanha policiais do BOPE em 1997.",
   "Zazen Produções – 'Tropa de Elite' (2007)", br=True)
mc(T, "cinema brasileiro", 2, 12, "Na comédia 'Se Eu Fosse Você', o que acontece com o casal vivido por Tony Ramos e Glória Pires?",
   ["Eles trocam de corpo", "Eles ficam invisíveis", "Eles voltam no tempo", "Eles encolhem"], "Eles trocam de corpo",
   "Depois de uma briga, marido e mulher acordam um no corpo do outro.",
   "Globo Filmes – 'Se Eu Fosse Você' (2006)", br=True)
tf(T, "atores", 2, 12, "A atriz Fernanda Torres é filha de Fernanda Montenegro.", True,
   "Fernanda Torres é filha de Fernanda Montenegro e do ator Fernando Torres, e as duas atuaram juntas em 'Ainda Estou Aqui'.",
   "Enciclopédia Itaú Cultural – verbete 'Fernanda Montenegro'", br=True)
tf(T, "cinema brasileiro", 2, 12, "O filme 'O Auto da Compadecida 2' chegou aos cinemas em 2024.", True,
   "A continuação, de novo com Matheus Nachtergaele e Selton Mello, estreou no Natal de 2024.",
   "Globo Filmes – 'O Auto da Compadecida 2' (2024)", br=True)
op(T, "gêneros", 2, 12, "Como se chama no Brasil o gênero de filmes com caubóis, xerifes e duelos no Velho Oeste americano?",
   "Faroeste", ["faroeste", "western", "bangue-bangue", "bang-bang", "filme de caubói"],
   "A palavra 'faroeste' vem do inglês 'far west', o 'oeste distante' dos Estados Unidos.",
   "Enciclopédia Britannica – verbete 'Western'")
mc(T, "festivais", 2, 12, "Em qual estado brasileiro acontece o Festival de Cinema de Gramado?",
   ["Rio Grande do Sul", "Santa Catarina", "Paraná", "Minas Gerais"], "Rio Grande do Sul",
   "O festival acontece desde 1973 na cidade serrana de Gramado.",
   "Festival de Cinema de Gramado – site oficial", br=True)
mc(T, "cinema brasileiro", 2, 12, "Qual filme de 2005 conta a história da dupla sertaneja Zezé Di Camargo & Luciano?",
   ["2 Filhos de Francisco", "Central do Brasil", "Tieta do Agreste", "Lisbela e o Prisioneiro"], "2 Filhos de Francisco",
   "O título lembra o pai da dupla, Francisco, que sonhava ver os filhos fazendo sucesso na música.",
   "Columbia Pictures / Conspiração Filmes – '2 Filhos de Francisco' (2005)", br=True,
   syn=("dois filhos de francisco",))
mc(T, "cinema brasileiro", 2, 12, "Em 'Central do Brasil', a personagem Dora escreve cartas na estação Central do Brasil, em qual cidade?",
   ["Rio de Janeiro", "São Paulo", "Salvador", "Recife"], "Rio de Janeiro",
   "Dora, vivida por Fernanda Montenegro, escrevia cartas para quem não sabia escrever.",
   "VideoFilmes – 'Central do Brasil' (1998)", br=True)

# =========================================================== DIFÍCEIS
mc(T, "festivais", 3, 14, "Como se chama o principal prêmio do Festival de Cinema de Berlim?",
   ["Urso de Ouro", "Palma de Ouro", "Leão de Ouro", "Concha de Ouro"], "Urso de Ouro",
   "O urso é o símbolo da cidade de Berlim e aparece no troféu do festival.",
   "Berlinale – site oficial")
tf(T, "festivais", 3, 14, "'Central do Brasil' ganhou o Urso de Ouro no Festival de Berlim.", True,
   "O filme de Walter Salles venceu em 1998, e Fernanda Montenegro levou também o prêmio de melhor atriz.",
   "Berlinale – arquivo de premiados de 1998", br=True)
mc(T, "cinema brasileiro", 3, 14, "Qual personagem Fernanda Torres interpreta em 'Ainda Estou Aqui'?",
   ["Eunice Paiva", "Dona Flor", "Dora", "Dona Hermínia"], "Eunice Paiva",
   "Eunice Paiva lutou por respostas depois que o marido, Rubens Paiva, desapareceu durante a ditadura militar.",
   "VideoFilmes – 'Ainda Estou Aqui' (2024)", br=True, syn=("eunice",))
mc(T, "cinema brasileiro", 3, 14, "'Ainda Estou Aqui' é baseado no livro de qual escritor, filho da família retratada no filme?",
   ["Marcelo Rubens Paiva", "Paulo Coelho", "Ariano Suassuna", "Jorge Amado"], "Marcelo Rubens Paiva",
   "Marcelo Rubens Paiva escreveu o livro sobre sua mãe, Eunice, publicado em 2015.",
   "Companhia das Letras / Alfaguara – 'Ainda Estou Aqui' (2015)", br=True)
mc(T, "cinema brasileiro", 3, 14, "Em 'Que Horas Ela Volta?', qual é a profissão de Val, personagem de Regina Casé?",
   ["Empregada doméstica", "Professora", "Enfermeira", "Cozinheira de restaurante"], "Empregada doméstica",
   "Val trabalha há anos numa casa em São Paulo, e a chegada da filha muda a relação com os patrões.",
   "Gullane Filmes – 'Que Horas Ela Volta?' (2015)", br=True, syn=("doméstica", "empregada"))
mc(T, "cinema brasileiro", 3, 14, "Em 'Cidade de Deus', o narrador Buscapé sonha em seguir qual profissão?",
   ["Fotógrafo", "Jogador de futebol", "Médico", "Professor"], "Fotógrafo",
   "Com uma câmera, Buscapé registra a vida na comunidade e consegue emprego num jornal.",
   "O2 Filmes – 'Cidade de Deus' (2002)", br=True)
mc(T, "cinema brasileiro", 3, 16, "Qual movimento do cinema brasileiro tinha o lema 'uma câmera na mão e uma ideia na cabeça'?",
   ["Cinema Novo", "Chanchada", "Retomada", "Pornochanchada"], "Cinema Novo",
   "O Cinema Novo, dos anos 1960, buscava mostrar a realidade brasileira com poucos recursos.",
   "Enciclopédia Itaú Cultural – verbete 'Cinema Novo'", br=True)
mc(T, "festivais", 3, 14, "Como se chama o troféu entregue aos vencedores do Festival de Cinema de Gramado?",
   ["Kikito", "Candango", "Saci", "Oscarito"], "Kikito",
   "O Kikito, estatueta de um deus sorridente, foi criado pela artista gaúcha Elisabeth Rosenfeld.",
   "Festival de Cinema de Gramado – site oficial", br=True)
mc(T, "diretores", 3, 16, "Qual diretor fez '2001: Uma Odisseia no Espaço' e 'O Iluminado'?",
   ["Stanley Kubrick", "Alfred Hitchcock", "Francis Ford Coppola", "Martin Scorsese"], "Stanley Kubrick",
   "Kubrick era conhecido pelo perfeccionismo e por filmar muitas vezes a mesma cena.",
   "Enciclopédia Britannica – verbete 'Stanley Kubrick'")
tf(T, "diretores", 3, 16, "Steven Spielberg ganhou o Oscar de Melhor Diretor por 'A Lista de Schindler'.", True,
   "O filme, sobre um empresário que salvou mais de mil judeus no Holocausto, também ganhou o Oscar de Melhor Filme.",
   "Academy of Motion Picture Arts and Sciences – 66ª cerimônia (1994)")
tf(T, "atores", 3, 14, "Charles Chaplin nasceu nos Estados Unidos.", False,
   "Chaplin nasceu em Londres, na Inglaterra, em 1889, e só depois foi fazer filmes em Hollywood.",
   "Enciclopédia Britannica – verbete 'Charlie Chaplin'")
mc(T, "história do cinema", 3, 14, "Qual filme de 1927 é considerado o primeiro longa-metragem com falas sincronizadas?",
   ["O Cantor de Jazz", "Cantando na Chuva", "Metrópolis", "O Garoto"], "O Cantor de Jazz",
   "Estrelado por Al Jolson, o filme tinha poucas falas e canções gravadas, e abriu a era do cinema falado.",
   "Enciclopédia Britannica – verbete 'The Jazz Singer'")

# =========================================================== MUITO DIFÍCEIS
mc(T, "história do cinema", 4, 16, "Qual pioneiro francês fez 'Viagem à Lua', de 1902, em que um foguete acerta o olho da Lua?",
   ["Georges Méliès", "Louis Lumière", "Jean Renoir", "François Truffaut"], "Georges Méliès",
   "Méliès era ilusionista e criou alguns dos primeiros efeitos especiais do cinema.",
   "Enciclopédia Britannica – verbete 'Georges Méliès'", syn=("méliès", "melies"))
mc(T, "técnica", 4, 16, "Quantos quadros por segundo é o padrão clássico de projeção do cinema?",
   ["24", "10", "60", "100"], "24",
   "Com o cinema falado, a velocidade foi padronizada em 24 quadros por segundo.",
   "Enciclopédia Britannica – verbete 'Motion picture technology'", syn=("vinte e quatro",))
mc(T, "prêmios", 4, 16, "O filme 'Orfeu Negro', rodado no Rio durante o Carnaval, ganhou o Oscar de filme estrangeiro representando qual país?",
   ["França", "Brasil", "Portugal", "Itália"], "França",
   "Dirigido pelo francês Marcel Camus, o filme também venceu a Palma de Ouro em Cannes, em 1959.",
   "Academy of Motion Picture Arts and Sciences – 32ª cerimônia (1960)", br=True)
mc(T, "atores", 4, 16, "Qual ator, parceiro de Oscarito nas chanchadas, tinha o nome verdadeiro de Sebastião Prata?",
   ["Grande Otelo", "Mazzaropi", "Ankito", "Zé Trindade"], "Grande Otelo",
   "Grande Otelo também atuou em 'Macunaíma', de 1969, no papel do herói quando nasce.",
   "Enciclopédia Itaú Cultural – verbete 'Grande Otelo'", br=True)
op(T, "clássicos", 4, 16, "Em qual cidade americana o boxeador Rocky Balboa sobe correndo a escadaria de um museu?",
   "Filadélfia", ["filadélfia", "filadelfia", "philadelphia"],
   "A escadaria do Museu de Arte da Filadélfia ficou conhecida como 'Rocky Steps' e ganhou uma estátua do personagem.",
   "Philadelphia Museum of Art – 'Rocky Statue and Steps'")
mc(T, "cinema brasileiro", 4, 16, "Qual filme de 1995, de Carla Camurati, é considerado o marco da Retomada do cinema brasileiro?",
   ["Carlota Joaquina, Princesa do Brazil", "Bye Bye Brasil", "Pixote", "O Quatrilho"], "Carlota Joaquina, Princesa do Brazil",
   "Depois de anos de pouquíssimas produções, o filme levou mais de um milhão de pessoas aos cinemas.",
   "Enciclopédia Itaú Cultural – verbete 'Carla Camurati'", br=True, syn=("carlota joaquina",))
