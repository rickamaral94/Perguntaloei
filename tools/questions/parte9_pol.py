# Perguntas novas: política e cidadania. IDs continuam a numeração do tema.
from qdsl import mc, op, tf
T = "pol"

# =========================================================== FÁCEIS (crianças pequenas)
mc(T, "convivência", 1, 6, "Na sala de aula, o que devemos fazer enquanto um colega está falando?",
   ["Esperar a nossa vez de falar", "Falar mais alto que ele", "Sair correndo da sala", "Tapar os ouvidos"],
   "Esperar a nossa vez de falar",
   "Ouvir os outros e esperar a vez é uma forma básica de respeito na convivência em grupo.",
   "Base Nacional Comum Curricular (BNCC) – competências gerais")
mc(T, "convivência", 1, 6, "O que fazer com um objeto perdido que você encontra na escola?",
   ["Entregar para a professora ou para a secretaria", "Guardar escondido na mochila", "Jogar no lixo", "Esconder no banheiro"],
   "Entregar para a professora ou para a secretaria",
   "Entregar o objeto a um adulto responsável ajuda o dono a recuperá-lo.",
   "Base Nacional Comum Curricular (BNCC) – competências gerais")
mc(T, "convivência", 1, 6, "Se um colega se machuca no recreio, a quem devemos pedir ajuda?",
   ["A um adulto da escola, como a professora", "A ninguém", "Ao colega mais novo da turma", "Ao cachorro da vizinha"],
   "A um adulto da escola, como a professora",
   "Em caso de acidente, um adulto responsável sabe como cuidar do machucado e chamar socorro.",
   "Ministério da Saúde – Primeiros socorros")
mc(T, "convivência", 1, 6, "O que quer dizer respeitar as diferenças?",
   ["Tratar bem quem é diferente de nós", "Brincar só com quem é igual a nós", "Rir de quem é diferente", "Não falar com ninguém"],
   "Tratar bem quem é diferente de nós",
   "Respeitar as diferenças é tratar com gentileza pessoas de outras aparências, origens e jeitos de ser.",
   "ONU – Declaração Universal dos Direitos Humanos, artigo 2")
mc(T, "serviços públicos", 1, 6, "Qual destes serviços públicos ajuda a manter a cidade limpa?",
   ["Coleta de lixo", "Cinema", "Parque de diversões", "Loja de brinquedos"], "Coleta de lixo",
   "Os caminhões de coleta recolhem o lixo das casas e levam para lugares apropriados.",
   "Ministério do Meio Ambiente – Política Nacional de Resíduos Sólidos", br=True)
mc(T, "serviços públicos", 1, 6, "Como se chama a escola mantida pelo governo, onde as crianças estudam de graça?",
   ["Escola pública", "Escola particular", "Escola de natação", "Escola de idiomas"], "Escola pública",
   "No Brasil, o ensino nas escolas públicas é gratuito, como garante a Constituição.",
   "Constituição Federal de 1988 – artigo 206", br=True)
op(T, "formas de governo", 1, 6, "Como se chama o homem que governa um reino e usa coroa?", "Rei",
   ["rei", "o rei", "um rei"],
   "Reis e rainhas são os chefes de Estado nas monarquias.",
   "Enciclopédia Britannica – verbete 'Monarchy'")
tf(T, "direitos da criança", 1, 6, "Toda criança tem direito de ir à escola.", True,
   "A Constituição e o Estatuto da Criança e do Adolescente garantem a educação como direito de todos.",
   "Constituição Federal de 1988 – artigo 205", br=True)
tf(T, "direitos da criança", 1, 7, "Brincar é um dos direitos das crianças garantidos pelo Estatuto da Criança e do Adolescente.", True,
   "O ECA inclui brincar, praticar esportes e divertir-se entre os direitos de liberdade das crianças.",
   "Estatuto da Criança e do Adolescente – Lei 8.069/1990, artigo 16", br=True)
mc(T, "escola e cidadania", 1, 7, "Como se chama o aluno escolhido pela turma para representá-la?",
   ["Representante de turma", "Diretor", "Inspetor", "Merendeiro"], "Representante de turma",
   "Muitas escolas fazem eleições para que a turma escolha quem vai falar em nome dela.",
   "Ministério da Educação – Grêmio estudantil e participação", br=True)
tf(T, "eleições", 1, 7, "No Brasil, crianças de 8 anos já podem votar.", False,
   "No Brasil, só é possível votar a partir dos 16 anos.",
   "Constituição Federal de 1988 – artigo 14", br=True)
tf(T, "convivência", 1, 7, "Pichar as paredes da escola é uma forma correta de cuidar do lugar onde estudamos.", False,
   "Pichar estraga o patrimônio que é de todos; cuidar é manter limpo e conservado.",
   "Lei de Crimes Ambientais – Lei 9.605/1998, artigo 65", br=True)
mc(T, "símbolos nacionais", 1, 7, "De que cor é a faixa onde está escrito 'Ordem e Progresso' na bandeira do Brasil?",
   ["Branca", "Verde", "Amarela", "Vermelha"], "Branca",
   "A faixa branca atravessa o círculo azul da bandeira, com o lema escrito em letras verdes.",
   "Lei 5.700/1971 – Símbolos Nacionais", br=True)
mc(T, "serviços públicos", 1, 7, "Onde as pessoas são atendidas pelo SUS perto de casa, para tomar vacina ou consultar?",
   ["Posto de saúde", "Delegacia", "Cartório", "Agência dos Correios"], "Posto de saúde",
   "Os postos, ou Unidades Básicas de Saúde, são a porta de entrada do SUS.",
   "Ministério da Saúde – Unidades Básicas de Saúde", br=True)
mc(T, "documentos", 1, 8, "Qual é o primeiro documento de um bebê, feito no cartório logo depois que ele nasce?",
   ["Certidão de nascimento", "Título de eleitor", "Carteira de motorista", "Passaporte"], "Certidão de nascimento",
   "A certidão de nascimento registra o nome, a data e o local de nascimento e é gratuita no Brasil.",
   "Lei 9.534/1997 – gratuidade do registro civil de nascimento", br=True)
mc(T, "impostos", 1, 8, "Como se chama o dinheiro que pessoas e empresas pagam ao governo para manter escolas, hospitais e ruas?",
   ["Imposto", "Mesada", "Troco", "Gorjeta"], "Imposto",
   "Os impostos financiam os serviços públicos usados por toda a população.",
   "Receita Federal – Educação Fiscal", br=True)
tf(T, "impostos", 1, 8, "Os salários de policiais, bombeiros e professores de escolas públicas são pagos com dinheiro dos impostos.", True,
   "Servidores públicos são pagos pelo governo, que arrecada dinheiro principalmente por meio de impostos.",
   "Receita Federal – Educação Fiscal", br=True)
mc(T, "eleições", 1, 8, "Como se chamam as pessoas que disputam uma eleição para tentar ganhar um cargo?",
   ["Candidatos", "Eleitores", "Mesários", "Juízes"], "Candidatos",
   "Os candidatos pedem votos, e os eleitores escolhem um deles na urna.",
   "Tribunal Superior Eleitoral – Glossário eleitoral")
mc(T, "eleições", 1, 8, "Em que lugar o eleitor fica sozinho para votar em segredo?",
   ["Cabine de votação", "Sala dos professores", "Cartório", "Secretaria da escola"], "Cabine de votação",
   "A cabine, protegida por um biombo, garante que ninguém veja em quem o eleitor votou.",
   "Tribunal Superior Eleitoral – Como votar", br=True)

# =========================================================== FÁCEIS (9–12)
mc(T, "eleições", 1, 9, "Na identificação biométrica antes de votar, qual parte do corpo a Justiça Eleitoral usa?",
   ["A impressão digital do dedo", "A cor dos olhos", "O som da voz", "O formato da orelha"], "A impressão digital do dedo",
   "A biometria compara a impressão digital do eleitor com a que foi cadastrada no cartório eleitoral.",
   "Tribunal Superior Eleitoral – Biometria", br=True)
tf(T, "eleições", 1, 9, "Na urna eletrônica, a tecla 'Corrige' serve para apagar o número digitado e recomeçar.", True,
   "Antes de confirmar, o eleitor pode apertar 'Corrige' para apagar e digitar o número de novo.",
   "Tribunal Superior Eleitoral – Urna eletrônica", br=True)
tf(T, "três Poderes", 1, 9, "Os prefeitos fazem parte do Poder Legislativo.", False,
   "O prefeito chefia o Poder Executivo do município; o Legislativo municipal é a Câmara de Vereadores.",
   "Constituição Federal de 1988 – artigo 29", br=True)
mc(T, "formas de governo", 1, 9, "Qual é a forma de governo do Brasil desde 1889?",
   ["República", "Monarquia", "Império", "Reinado"], "República",
   "Em 1889, o Império acabou e o Brasil passou a ser uma república, com presidentes eleitos.",
   "Constituição Federal de 1988 – artigo 1º", br=True)
mc(T, "formas de governo", 1, 10, "Como se chama a forma de governo em que um rei ou uma rainha é o chefe de Estado?",
   ["Monarquia", "República", "Federação", "Anarquia"], "Monarquia",
   "Na monarquia, o cargo de chefe de Estado costuma passar de pai ou mãe para filho.",
   "Enciclopédia Britannica – verbete 'Monarchy'")
mc(T, "formas de governo", 1, 10, "Qual destes países tem um rei ou uma rainha como chefe de Estado?",
   ["Reino Unido", "França", "Brasil", "Estados Unidos"], "Reino Unido",
   "O Reino Unido é uma monarquia constitucional: o monarca é chefe de Estado e o governo é chefiado por um primeiro-ministro.",
   "Enciclopédia Britannica – verbete 'United Kingdom'", ref="2026-10-13")
op(T, "organismos internacionais", 1, 10, "Qual é o nome da moeda usada pela maior parte dos países da União Europeia?", "Euro",
   ["euro", "o euro", "euros"],
   "O euro começou a circular em notas e moedas em 2002.",
   "Banco Central Europeu – The euro")
mc(T, "história política mundial", 1, 10, "Quem foi o primeiro presidente dos Estados Unidos?",
   ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "Benjamin Franklin"], "George Washington",
   "George Washington governou de 1789 a 1797 e dá nome à capital do país.",
   "Enciclopédia Britannica – verbete 'George Washington'")

# =========================================================== MÉDIAS
mc(T, "eleições", 2, 12, "Como se chamam as pessoas convocadas pela Justiça Eleitoral para trabalhar nas seções no dia da votação?",
   ["Mesários", "Vereadores", "Fiscais de trânsito", "Oficiais de justiça"], "Mesários",
   "Os mesários conferem os documentos, liberam a urna e ajudam a organizar a votação.",
   "Tribunal Superior Eleitoral – Mesário", br=True)
mc(T, "eleições", 2, 12, "Em que mês acontece o primeiro turno das eleições no Brasil?",
   ["Outubro", "Janeiro", "Abril", "Dezembro"], "Outubro",
   "Pela Constituição, o primeiro turno acontece no primeiro domingo de outubro.",
   "Constituição Federal de 1988 – artigo 77", br=True)
mc(T, "eleições", 2, 12, "Na urna eletrônica, como se chama o voto de quem aperta a tecla que não escolhe nenhum candidato?",
   ["Voto em branco", "Voto secreto", "Voto aberto", "Voto distrital"], "Voto em branco",
   "A urna tem uma tecla própria para o voto em branco, que não é contado para nenhum candidato.",
   "Tribunal Superior Eleitoral – Urna eletrônica", br=True)
mc(T, "eleições", 2, 12, "Como se chama o tribunal eleitoral que existe em cada estado brasileiro?",
   ["Tribunal Regional Eleitoral", "Tribunal de Contas", "Tribunal do Júri", "Tribunal de Justiça Desportiva"],
   "Tribunal Regional Eleitoral",
   "Cada estado e o Distrito Federal têm um TRE, que organiza as eleições na sua região.",
   "Constituição Federal de 1988 – artigos 118 e 120", br=True)
tf(T, "eleições", 2, 14, "Se nenhum candidato a presidente tiver mais da metade dos votos válidos, acontece um segundo turno.", True,
   "No segundo turno, disputam apenas os dois candidatos mais votados no primeiro.",
   "Constituição Federal de 1988 – artigo 77", br=True)
op(T, "impostos", 2, 12, "Qual imposto estadual é cobrado todo ano de quem tem carro ou moto?", "IPVA",
   ["ipva", "imposto sobre a propriedade de veículos automotores", "imposto sobre veículos"],
   "O IPVA é cobrado pelos estados, e parte do valor vai para o município onde o veículo está registrado.",
   "Constituição Federal de 1988 – artigos 155 e 158", br=True)
tf(T, "impostos", 2, 14, "O IPTU, cobrado sobre casas e terrenos nas cidades, é um imposto do governo federal.", False,
   "O IPTU é um imposto municipal, cobrado pelas prefeituras.",
   "Constituição Federal de 1988 – artigo 156", br=True)
op(T, "Congresso Nacional", 2, 12, "Quantos senadores o Brasil tem ao todo?", "81",
   ["81", "oitenta e um", "81 senadores"],
   "São três senadores para cada um dos 26 estados e para o Distrito Federal.",
   "Senado Federal – Senadores em exercício", br=True)
mc(T, "símbolos nacionais", 2, 12, "Em que dia se comemora o Dia da Bandeira no Brasil?",
   ["19 de novembro", "7 de setembro", "15 de novembro", "21 de abril"], "19 de novembro",
   "A data lembra a adoção da bandeira republicana, quatro dias depois da Proclamação da República.",
   "Lei 5.700/1971 – Símbolos Nacionais", br=True)
mc(T, "organismos internacionais", 2, 12, "Qual é o título de quem dirige a Secretaria da ONU?",
   ["Secretário-geral", "Presidente mundial", "Primeiro-ministro", "Imperador"], "Secretário-geral",
   "O secretário-geral é escolhido pela Assembleia Geral, por recomendação do Conselho de Segurança.",
   "Nações Unidas – The Secretary-General")
mc(T, "organismos internacionais", 2, 12, "Como são chamados os soldados das missões de paz da ONU, por causa da cor que usam na cabeça?",
   ["Capacetes azuis", "Boinas vermelhas", "Chapéus verdes", "Lenços amarelos"], "Capacetes azuis",
   "Os soldados das forças de paz usam capacetes ou boinas azuis, a cor da ONU.",
   "Nações Unidas – Peacekeeping")
mc(T, "organismos internacionais", 2, 12, "Qual organização humanitária, fundada em Genebra em 1863, socorre feridos em guerras e catástrofes?",
   ["Cruz Vermelha", "UNESCO", "OTAN", "Banco Mundial"], "Cruz Vermelha",
   "A Cruz Vermelha nasceu da iniciativa do suíço Henry Dunant, que ganhou o primeiro Nobel da Paz.",
   "Comitê Internacional da Cruz Vermelha – History")
op(T, "formas de governo", 2, 12, "No parlamentarismo, qual é o título de quem chefia o governo?", "Primeiro-ministro",
   ["primeiro-ministro", "primeiro ministro", "primeira-ministra", "primeira ministra", "premiê"],
   "No parlamentarismo, o primeiro-ministro depende do apoio do Parlamento para governar.",
   "Enciclopédia Britannica – verbete 'Parliamentary system'")
mc(T, "formas de governo", 2, 14, "Como se chama a forma de Estado do Brasil, em que União, estados e municípios têm autonomia?",
   ["Federação", "Monarquia", "Estado unitário", "Império"], "Federação",
   "A Constituição chama o país de República Federativa do Brasil, formada pela união de estados, municípios e Distrito Federal.",
   "Constituição Federal de 1988 – artigo 1º", br=True)
tf(T, "formas de governo", 2, 12, "A Espanha é uma república, sem rei nem rainha.", False,
   "A Espanha é uma monarquia parlamentar, com um rei como chefe de Estado.",
   "Constituição Espanhola de 1978 – artigo 1º", ref="2026-10-13")
mc(T, "história política mundial", 2, 12, "Qual era o lema da Revolução Francesa?",
   ["Liberdade, Igualdade, Fraternidade", "Ordem e Progresso", "Paz, Pão e Terra", "A União Faz a Força"],
   "Liberdade, Igualdade, Fraternidade",
   "O lema da Revolução virou o lema oficial da República Francesa.",
   "Enciclopédia Britannica – verbete 'French Revolution'")
op(T, "história política mundial", 2, 12, "Qual prisão de Paris foi tomada pela população em 14 de julho de 1789?", "Bastilha",
   ["bastilha", "a bastilha", "fortaleza da bastilha"],
   "A queda da Bastilha virou símbolo da Revolução, e 14 de julho é hoje a festa nacional da França.",
   "Enciclopédia Britannica – verbete 'Bastille'")
tf(T, "história política mundial", 2, 14, "Na democracia da antiga Atenas, as mulheres podiam votar nas assembleias.", False,
   "Em Atenas, só votavam homens adultos considerados cidadãos; mulheres, estrangeiros e escravizados ficavam de fora.",
   "Enciclopédia Britannica – verbete 'Athenian democracy'")
mc(T, "formas de governo", 2, 12, "De qual língua vem a palavra 'democracia', que quer dizer 'governo do povo'?",
   ["Grego", "Latim", "Árabe", "Tupi"], "Grego",
   "Democracia junta as palavras gregas 'demos', povo, e 'kratos', poder.",
   "Dicionário Houaiss – verbete 'democracia'")
mc(T, "direitos da criança", 2, 12, "Pelo Estatuto da Criança e do Adolescente, a pessoa é considerada criança até completar quantos anos?",
   ["12", "10", "14", "18"], "12",
   "Para o ECA, criança tem até 12 anos incompletos, e adolescente vai dos 12 aos 18.",
   "Estatuto da Criança e do Adolescente – Lei 8.069/1990, artigo 2º", br=True)
op(T, "direitos da criança", 2, 12, "Qual órgão de cada município é encarregado de zelar pelos direitos de crianças e adolescentes?", "Conselho Tutelar",
   ["conselho tutelar", "o conselho tutelar"],
   "Todo município deve ter pelo menos um Conselho Tutelar, com conselheiros escolhidos pela comunidade.",
   "Estatuto da Criança e do Adolescente – Lei 8.069/1990, artigos 131 e 132", br=True)
mc(T, "presidentes históricos", 2, 14, "Qual presidente brasileiro tinha como lema fazer o país crescer '50 anos em 5'?",
   ["Juscelino Kubitschek", "Getúlio Vargas", "Deodoro da Fonseca", "Prudente de Morais"], "Juscelino Kubitschek",
   "O Plano de Metas de JK, de 1956 a 1961, incentivou indústrias, estradas e a construção de Brasília.",
   "CPDOC/FGV – verbete 'Juscelino Kubitschek'", br=True)
tf(T, "organismos internacionais", 2, 14, "Por tradição, o Brasil é o primeiro país a discursar no debate geral da Assembleia Geral da ONU.", True,
   "A tradição existe desde os primeiros anos da ONU, quando o Brasil se ofereceu para abrir os discursos.",
   "Ministério das Relações Exteriores – Brasil nas Nações Unidas", br=True)

# =========================================================== DIFÍCEIS
tf(T, "Judiciário", 3, 14, "Os ministros do Supremo Tribunal Federal são eleitos pelo voto popular.", False,
   "Eles são indicados pelo presidente da República e precisam ser aprovados pelo Senado.",
   "Constituição Federal de 1988 – artigo 101", br=True)
mc(T, "Constituições brasileiras", 3, 14, "De que ano é a primeira Constituição do Brasil republicano?",
   ["1891", "1824", "1934", "1946"], "1891",
   "A Constituição de 1891 criou o regime presidencialista e a federação no Brasil.",
   "Senado Federal – Constituições brasileiras", br=True)
mc(T, "presidentes históricos", 3, 14, "Quem foi o primeiro presidente civil do Brasil, que tomou posse em 1894?",
   ["Prudente de Morais", "Floriano Peixoto", "Campos Sales", "Rodrigues Alves"], "Prudente de Morais",
   "Os dois primeiros presidentes eram marechais; Prudente de Morais foi também o primeiro eleito pelo voto direto.",
   "Biblioteca da Presidência da República – Prudente de Morais", br=True)
mc(T, "presidentes históricos", 3, 14, "Qual presidente, eleito em 1985 pelo Colégio Eleitoral, morreu antes de tomar posse?",
   ["Tancredo Neves", "Juscelino Kubitschek", "Ulysses Guimarães", "Getúlio Vargas"], "Tancredo Neves",
   "Tancredo adoeceu na véspera da posse e morreu em 21 de abril de 1985.",
   "Biblioteca da Presidência da República – Tancredo Neves", br=True)
mc(T, "símbolos nacionais", 3, 14, "Além da Bandeira, do Hino e do Selo Nacional, qual é o quarto símbolo nacional do Brasil?",
   ["Armas Nacionais", "Cruzeiro do Sul", "Ipê-amarelo", "Pau-brasil"], "Armas Nacionais",
   "As Armas Nacionais, também chamadas de Brasão da República, aparecem em prédios e documentos oficiais.",
   "Lei 5.700/1971 – Símbolos Nacionais", br=True)
mc(T, "organismos internacionais", 3, 14, "Qual aliança militar foi criada em 1949 pelos Estados Unidos, pelo Canadá e por países da Europa Ocidental?",
   ["OTAN", "ONU", "OEA", "OPEP"], "OTAN",
   "A OTAN, Organização do Tratado do Atlântico Norte, prevê que um ataque a um membro é um ataque a todos.",
   "OTAN – A short history of NATO")
mc(T, "organismos internacionais", 3, 14, "Em qual cidade fica a sede da Organização Mundial da Saúde?",
   ["Genebra", "Nova York", "Paris", "Londres"], "Genebra",
   "A OMS, criada em 1948, tem sede em Genebra, na Suíça.",
   "Organização Mundial da Saúde – About WHO")
tf(T, "organismos internacionais", 3, 14, "O português é uma das línguas oficiais da ONU.", False,
   "As seis línguas oficiais da ONU são inglês, francês, espanhol, russo, chinês e árabe.",
   "Nações Unidas – Official Languages")
mc(T, "direitos humanos", 3, 14, "Qual documento, aprovado na França em 1789, afirmou que os homens nascem livres e iguais em direitos?",
   ["Declaração dos Direitos do Homem e do Cidadão", "Magna Carta", "Declaração de Independência", "Código de Hamurábi"],
   "Declaração dos Direitos do Homem e do Cidadão",
   "O texto foi aprovado pela Assembleia Nacional francesa em agosto de 1789.",
   "Enciclopédia Britannica – verbete 'Declaration of the Rights of Man and of the Citizen'")
mc(T, "direitos humanos", 3, 14, "Em que dia se comemora o Dia Internacional dos Direitos Humanos?",
   ["10 de dezembro", "1º de maio", "8 de março", "12 de outubro"], "10 de dezembro",
   "A data lembra o dia em que a ONU proclamou a Declaração Universal dos Direitos Humanos, em 1948.",
   "Nações Unidas – Human Rights Day")
mc(T, "Justiça", 3, 14, "Qual instituição defende na Justiça, de graça, as pessoas que não podem pagar um advogado?",
   ["Defensoria Pública", "Receita Federal", "Polícia Rodoviária", "Banco Central"], "Defensoria Pública",
   "A Constituição atribui à Defensoria Pública a orientação jurídica e a defesa dos necessitados.",
   "Constituição Federal de 1988 – artigo 134", br=True)
mc(T, "história política mundial", 3, 14, "Como se chamou o regime de separação racial que vigorou na África do Sul de 1948 até o início dos anos 1990?",
   ["Apartheid", "Feudalismo", "Absolutismo", "Colonato"], "Apartheid",
   "A palavra significa 'separação' em africâner; o regime terminou com as eleições multirraciais de 1994.",
   "Enciclopédia Britannica – verbete 'Apartheid'")

# =========================================================== MUITO DIFÍCEIS
mc(T, "eleições", 4, 16, "Pela Constituição, só pode haver segundo turno para prefeito em municípios com mais de quantos eleitores?",
   ["200 mil", "50 mil", "100 mil", "1 milhão"], "200 mil",
   "Nas cidades menores, vence quem tiver mais votos já no primeiro turno.",
   "Constituição Federal de 1988 – artigo 29", br=True)
mc(T, "Constituições brasileiras", 4, 16, "Qual apelido ganhou a Constituição de 1937, imposta no Estado Novo?",
   ["Polaca", "Cidadã", "Imperial", "Mineira"], "Polaca",
   "O apelido vem da inspiração na Constituição autoritária da Polônia de 1935.",
   "CPDOC/FGV – verbete 'Constituição de 1937'", br=True)
tf(T, "formas de governo", 4, 16, "O Brasil já adotou o parlamentarismo durante a República, entre 1961 e 1963.", True,
   "O sistema foi adotado após a renúncia de Jânio Quadros e derrubado pelo plebiscito de janeiro de 1963.",
   "CPDOC/FGV – verbete 'Parlamentarismo'", br=True)
mc(T, "símbolos nacionais", 4, 16, "Qual estrela representa o Distrito Federal na bandeira do Brasil?",
   ["Sigma do Oitante", "Sirius", "Canopus", "Antares"], "Sigma do Oitante",
   "Ela fica perto do polo sul celeste, por isso parece imóvel, como a capital no centro do país.",
   "Lei 5.700/1971 – Símbolos Nacionais, anexo", br=True)
mc(T, "história política mundial", 4, 16, "Como se chamava a assembleia em que os cidadãos da antiga Atenas votavam as leis?",
   ["Eclésia", "Senado", "Conclave", "Parlamento"], "Eclésia",
   "A Eclésia reunia os cidadãos atenienses, que votavam erguendo as mãos.",
   "Enciclopédia Britannica – verbete 'Ecclesia'")
mc(T, "direitos humanos", 4, 16, "Qual ex-primeira-dama dos Estados Unidos presidiu a comissão da ONU que redigiu a Declaração Universal dos Direitos Humanos?",
   ["Eleanor Roosevelt", "Jacqueline Kennedy", "Martha Washington", "Abigail Adams"], "Eleanor Roosevelt",
   "Eleanor Roosevelt presidiu a Comissão de Direitos Humanos da ONU de 1946 a 1951.",
   "Nações Unidas – The Drafters of the Universal Declaration of Human Rights")
