# Perguntas novas: corpo humano. IDs continuam a numeração do tema.
from qdsl import mc, op, tf

T = "cor"

# =========================================================== FÁCEIS
mc(T, "partes do corpo", 1, 7, "Como se chamam os pelinhos na borda das pálpebras que protegem os olhos da poeira?",
   ["Cílios", "Sobrancelhas", "Bigodes", "Franjas"], "Cílios",
   "Os cílios funcionam como uma cortininha que segura poeira e ciscos antes que entrem nos olhos.",
   "Enciclopédia Britannica – verbete 'Eyelash'")
mc(T, "dentes", 1, 6, "Qual parte da boca usamos para cortar e triturar os alimentos?",
   ["Dentes", "Lábios", "Bochechas", "Gengivas"], "Dentes",
   "Os dentes cortam e moem a comida em pedaços pequenos, o que facilita a digestão.",
   "Ministério da Saúde – Saúde Bucal")
tf(T, "cabelo e unhas", 1, 6, "O cabelo e as unhas continuam crescendo depois que a gente corta.", True,
   "Cabelo e unhas crescem a partir da raiz, embaixo da pele, por isso voltam a crescer depois do corte.",
   "Enciclopédia Britannica – verbete 'Hair'")
tf(T, "cabelo e unhas", 1, 7, "Cortar o cabelo dói porque os fios têm nervos.", False,
   "A parte do fio que fica para fora da pele não tem nervos, por isso cortar o cabelo não dói.",
   "Enciclopédia Britannica – verbete 'Hair'")
mc(T, "partes do corpo", 1, 6, "Qual marquinha na barriga mostra onde ficava o cordão que nos ligava à mãe antes de nascermos?",
   ["Umbigo", "Joelho", "Cotovelo", "Queixo"], "Umbigo",
   "O umbigo é a cicatriz que fica no lugar do cordão umbilical, que levava alimento ao bebê na barriga da mãe.",
   "Enciclopédia Britannica – verbete 'Umbilical cord'")
op(T, "corpo no dia a dia", 1, 6, "Como se chama quando abrimos bem a boca e puxamos muito ar, geralmente quando estamos com sono?",
   "Bocejo", ["bocejo", "bocejar", "bocejando", "bocejada"],
   "Bocejamos quando estamos com sono ou cansados, e o bocejo costuma ser contagioso entre as pessoas.",
   "Enciclopédia Britannica – verbete 'Yawning'")
mc(T, "ossos e músculos", 1, 8, "Em qual parte da perna fica a rótula, um ossinho arredondado?",
   ["Joelho", "Tornozelo", "Quadril", "Calcanhar"], "Joelho",
   "A rótula, também chamada de patela, fica na frente do joelho e protege essa articulação.",
   "Enciclopédia Britannica – verbete 'Patella'")
mc(T, "partes do corpo", 1, 7, "Como se chama o dedo mais grosso da mão, que fica separado dos outros?",
   ["Polegar", "Indicador", "Mindinho", "Anelar"], "Polegar",
   "O polegar consegue encostar nos outros dedos, o que nos permite segurar objetos com firmeza.",
   "Enciclopédia Britannica – verbete 'Thumb'")
tf(T, "pele", 1, 7, "Quando sentimos frio, os pelinhos do braço podem ficar em pé e a pele fica arrepiada.", True,
   "Pequenos músculos na base de cada pelo se contraem com o frio, formando o arrepio.",
   "Enciclopédia Britannica – verbete 'Goose bumps'")
tf(T, "higiene", 1, 6, "Ao tossir ou espirrar, o certo é cobrir a boca e o nariz com o braço dobrado ou um lenço.", True,
   "Cobrir a tosse e o espirro evita que gotículas com germes se espalhem para outras pessoas.",
   "Ministério da Saúde")
mc(T, "profissionais da saúde", 1, 6, "Qual profissional cuida da saúde dos nossos dentes?",
   ["Dentista", "Veterinário", "Bombeiro", "Farmacêutico"], "Dentista",
   "O dentista, ou cirurgião-dentista, trata cáries e ensina a cuidar bem da boca.",
   "Conselho Federal de Odontologia")
mc(T, "profissionais da saúde", 1, 8, "Qual médico é especialista na saúde das crianças?",
   ["Pediatra", "Cardiologista", "Ortopedista", "Dermatologista"], "Pediatra",
   "O pediatra acompanha o crescimento e a saúde das crianças, desde o nascimento até a adolescência.",
   "Sociedade Brasileira de Pediatria")
op(T, "respiração", 1, 9, "Qual gás, produzido pelas nossas células, o corpo elimina quando soltamos o ar dos pulmões?",
   "Gás carbônico", ["gás carbônico", "gas carbonico", "dióxido de carbono", "dioxido de carbono", "co2"],
   "As células produzem gás carbônico ao gerar energia, e os pulmões o eliminam quando soltamos o ar.",
   "Enciclopédia Britannica – verbete 'Respiration'")
mc(T, "profissionais da saúde", 1, 8, "Qual instrumento o médico encosta no peito para ouvir o coração e a respiração?",
   ["Estetoscópio", "Termômetro", "Microscópio", "Telescópio"], "Estetoscópio",
   "O estetoscópio foi inventado pelo médico francês René Laennec, em 1816.",
   "Enciclopédia Britannica – verbete 'Stethoscope'")
op(T, "rins", 1, 8, "Quantos rins tem normalmente uma pessoa?", "2", ["2", "dois", "dois rins"],
   "Os dois rins ficam na parte de trás do abdome, um de cada lado da coluna.",
   "Enciclopédia Britannica – verbete 'Kidney'")
mc(T, "vacinação", 1, 7, "Qual personagem em forma de gotinha é o mascote das campanhas de vacinação no Brasil?",
   ["Zé Gotinha", "Zé Carioca", "Sujismundo", "Cebolinha"], "Zé Gotinha",
   "O Zé Gotinha foi criado em 1986 para incentivar as crianças a se vacinar.",
   "Ministério da Saúde", br=True)
tf(T, "prevenção", 1, 8, "Não deixar água parada em vasos, pneus e garrafas ajuda a combater o mosquito da dengue.", True,
   "O mosquito Aedes aegypti coloca seus ovos em água parada, então eliminar esses locais impede que ele se reproduza.",
   "Ministério da Saúde", br=True)
mc(T, "prevenção", 1, 9, "Qual mosquito transmite a dengue?",
   ["Aedes aegypti", "Anopheles", "Pernilongo comum", "Mosquito-palha"], "Aedes aegypti",
   "O Aedes aegypti, que tem listras brancas no corpo, também transmite zika e chikungunya.",
   "Ministério da Saúde", br=True)
mc(T, "visão", 1, 9, "Como se chama a bolinha preta no centro do olho, por onde a luz entra?",
   ["Pupila", "Íris", "Retina", "Córnea"], "Pupila",
   "A pupila é uma abertura que aumenta no escuro e diminui na claridade para controlar a entrada de luz.",
   "Enciclopédia Britannica – verbete 'Pupil'")
mc(T, "pele", 1, 9, "Como se chamam os desenhos de linhas na ponta dos dedos, diferentes em cada pessoa?",
   ["Impressões digitais", "Cutículas", "Sardas", "Pintas"], "Impressões digitais",
   "Os desenhos das pontas dos dedos se formam antes do nascimento e são usados para identificar as pessoas.",
   "Enciclopédia Britannica – verbete 'Fingerprint'")
mc(T, "alimentação", 1, 9, "Qual destes alimentos é fonte de fibras, que ajudam o intestino a funcionar bem?",
   ["Feijão", "Refrigerante", "Bala de goma", "Manteiga"], "Feijão",
   "Feijão, frutas, verduras e grãos integrais têm fibras, que ajudam a digestão e o funcionamento do intestino.",
   "Ministério da Saúde – Guia Alimentar para a População Brasileira")
op(T, "coração e circulação", 1, 9, "Como se chamam as batidinhas que sentimos ao apertar de leve o punho ou o pescoço, causadas pelo coração?",
   "Pulsação", ["pulsação", "pulsacao", "pulso", "batimentos", "batimentos cardíacos", "batimento cardíaco"],
   "A cada batida, o coração empurra o sangue pelas artérias, e esse movimento pode ser sentido como pulsação.",
   "Enciclopédia Britannica – verbete 'Pulse'")
tf(T, "dentes", 1, 6, "O fio dental serve para limpar entre os dentes, onde a escova não alcança bem.", True,
   "O fio dental remove restos de comida e placa bacteriana dos espaços entre os dentes.",
   "Ministério da Saúde – Saúde Bucal")
tf(T, "dentes", 1, 8, "Se um dente permanente cair, nasce outro no lugar dele.", False,
   "Temos só duas dentições, a de leite e a permanente; um dente permanente perdido não nasce de novo.",
   "Enciclopédia Britannica – verbete 'Tooth'")
mc(T, "ossos e músculos", 1, 7, "Como se chama o conjunto de todos os ossos do corpo?",
   ["Esqueleto", "Músculo", "Cérebro", "Estômago"], "Esqueleto",
   "O esqueleto sustenta o corpo, protege os órgãos e, junto com os músculos, permite os movimentos.",
   "Enciclopédia Britannica – verbete 'Human skeleton'")
tf(T, "higiene", 1, 7, "O sabonete só deixa as mãos cheirosas, mas não ajuda a tirar os germes.", False,
   "Lavar as mãos com água e sabão remove a sujeira e grande parte dos germes da pele.",
   "Ministério da Saúde")
tf(T, "sono e crescimento", 1, 8, "Dormir bem não faz nenhuma diferença para o crescimento das crianças.", False,
   "É durante o sono profundo que o corpo libera boa parte do hormônio do crescimento.",
   "Sociedade Brasileira de Pediatria")

# =========================================================== MÉDIAS
mc(T, "ossos e músculos", 2, 10, "Como se chamam os ossinhos empilhados que formam a coluna?",
   ["Vértebras", "Costelas", "Falanges", "Clavículas"], "Vértebras",
   "As vértebras ficam umas sobre as outras e protegem a medula espinhal, que passa por dentro delas.",
   "Enciclopédia Britannica – verbete 'Vertebral column'")
mc(T, "ossos e músculos", 2, 10, "Qual músculo da frente do braço aparece quando alguém dobra o braço para 'mostrar o muque'?",
   ["Bíceps", "Tríceps", "Deltoide", "Panturrilha"], "Bíceps",
   "O bíceps dobra o braço no cotovelo; o tríceps, na parte de trás, faz o movimento contrário.",
   "Enciclopédia Britannica – verbete 'Biceps'")
mc(T, "dentes", 2, 10, "Como se chamam os dentes pontudos, ao lado dos incisivos, que servem para rasgar os alimentos?",
   ["Caninos", "Molares", "Pré-molares", "Sisos"], "Caninos",
   "Temos quatro caninos na dentição permanente, dois em cima e dois embaixo.",
   "Enciclopédia Britannica – verbete 'Tooth'")
mc(T, "dentes", 2, 10, "Como se chama a camada branca e duríssima que cobre a parte de fora dos dentes?",
   ["Esmalte", "Gengiva", "Polpa", "Tártaro"], "Esmalte",
   "O esmalte dos dentes é a substância mais dura do corpo humano.",
   "Enciclopédia Britannica – verbete 'Enamel'")
mc(T, "sistema nervoso", 2, 10, "Quando o médico bate de leve logo abaixo do joelho e a perna dá um chute sozinha, como se chama essa reação?",
   ["Reflexo", "Soluço", "Espirro", "Bocejo"], "Reflexo",
   "No reflexo, a resposta passa pela medula espinhal e acontece antes mesmo de pensarmos nela.",
   "Enciclopédia Britannica – verbete 'Reflex'")
tf(T, "primeiros socorros", 2, 10, "Em uma queimadura leve, o certo é passar manteiga ou pasta de dente no local.", False,
   "O recomendado é deixar a queimadura sob água corrente fria; manteiga e pasta de dente podem piorar a lesão.",
   "Ministério da Saúde")
tf(T, "rins", 2, 10, "É possível viver com apenas um rim.", True,
   "Um único rim saudável consegue filtrar o sangue do corpo todo, por isso existem doadores de rim vivos.",
   "Enciclopédia Britannica – verbete 'Kidney'")
tf(T, "cinco sentidos", 2, 10, "Com o nariz entupido, a comida parece ter menos sabor porque o olfato ajuda a perceber os gostos.", True,
   "Boa parte do que chamamos de sabor vem dos cheiros que o nariz capta enquanto comemos.",
   "Enciclopédia Britannica – verbete 'Taste'")
mc(T, "pele", 2, 10, "O protetor solar ajuda a proteger a pele de qual tipo de raio do Sol?",
   ["Ultravioleta", "Infravermelho", "Raio X", "Raio gama"], "Ultravioleta",
   "Os raios ultravioleta podem queimar a pele, e o excesso de exposição aumenta o risco de câncer de pele.",
   "Instituto Nacional de Câncer (INCA)")
op(T, "saúde do bebê", 2, 10, "O teste do pezinho, feito nos recém-nascidos, usa gotinhas de sangue tiradas de qual parte do pé?",
   "Calcanhar", ["calcanhar", "do calcanhar", "o calcanhar"],
   "O teste do pezinho detecta cedo doenças que podem ser tratadas, e é oferecido de graça pelo SUS.",
   "Ministério da Saúde", br=True)
mc(T, "vacinação", 2, 10, "Qual doença transmitida por mosquitos tem uma cor no nome e pode ser evitada com vacina?",
   ["Febre amarela", "Malária", "Zika", "Chikungunya"], "Febre amarela",
   "A vacina contra a febre amarela faz parte do Calendário Nacional de Vacinação.",
   "Ministério da Saúde", br=True)
mc(T, "sangue", 2, 12, "Como se chama a parte líquida e amarelada do sangue, que forma mais da metade do seu volume?",
   ["Plasma", "Linfa", "Bile", "Saliva"], "Plasma",
   "O plasma é feito principalmente de água e transporta nutrientes, hormônios e as células do sangue.",
   "Enciclopédia Britannica – verbete 'Blood'")
tf(T, "ossos e músculos", 2, 12, "Um bebê recém-nascido tem mais ossos do que um adulto.", True,
   "Ao longo do crescimento, vários ossos do bebê se juntam, até chegar aos 206 do adulto.",
   "Enciclopédia Britannica – verbete 'Human skeleton'")
mc(T, "ossos e músculos", 2, 12, "Qual é o maior músculo do corpo humano, que fica no bumbum?",
   ["Glúteo máximo", "Bíceps", "Deltoide", "Masseter"], "Glúteo máximo",
   "O glúteo máximo ajuda a manter o corpo em pé e é muito usado para andar, correr e subir escadas.",
   "Enciclopédia Britannica – verbete 'Gluteus maximus'")
mc(T, "sistema nervoso", 2, 12, "Como se chamam as células do sistema nervoso que transmitem mensagens pelo corpo?",
   ["Neurônios", "Hemácias", "Plaquetas", "Linfócitos"], "Neurônios",
   "Os neurônios conduzem sinais elétricos e químicos entre o cérebro, a medula e o resto do corpo.",
   "Enciclopédia Britannica – verbete 'Neuron'")
mc(T, "sistema nervoso", 2, 12, "Como se chamam as duas metades em que o cérebro é dividido?",
   ["Hemisférios", "Lóbulos", "Ventrículos", "Átrios"], "Hemisférios",
   "Os hemisférios direito e esquerdo são ligados por uma faixa de fibras chamada corpo caloso.",
   "Enciclopédia Britannica – verbete 'Cerebrum'")
mc(T, "hormônios", 2, 12, "Qual hormônio é liberado num susto ou num perigo e faz o coração bater mais rápido?",
   ["Adrenalina", "Insulina", "Melatonina", "Ocitocina"], "Adrenalina",
   "A adrenalina é produzida pelas glândulas suprarrenais e prepara o corpo para reagir rápido.",
   "Enciclopédia Britannica – verbete 'Epinephrine'")
mc(T, "cabelo e unhas", 2, 12, "De qual proteína são feitos os cabelos e as unhas?",
   ["Queratina", "Hemoglobina", "Insulina", "Caseína"], "Queratina",
   "A queratina é uma proteína resistente que também forma a camada mais externa da pele.",
   "Enciclopédia Britannica – verbete 'Keratin'")
mc(T, "visão", 2, 12, "Como se chama o problema de visão em que a pessoa vê bem de perto, mas tem dificuldade para enxergar de longe?",
   ["Miopia", "Hipermetropia", "Daltonismo", "Catarata"], "Miopia",
   "Na miopia, a imagem se forma antes da retina, e óculos ou lentes corrigem o foco.",
   "Conselho Brasileiro de Oftalmologia")
mc(T, "digestão", 2, 12, "Depois do intestino delgado, os restos da comida passam por qual órgão, que absorve água e forma as fezes?",
   ["Intestino grosso", "Estômago", "Esôfago", "Pâncreas"], "Intestino grosso",
   "O intestino grosso absorve água e sais minerais e abriga bactérias que ajudam na digestão.",
   "Enciclopédia Britannica – verbete 'Large intestine'")
tf(T, "primeiros socorros", 2, 12, "Quando o nariz sangra, o recomendado é inclinar a cabeça para trás.", False,
   "O certo é inclinar a cabeça um pouco para a frente e apertar a parte mole do nariz, para o sangue não descer pela garganta.",
   "Enciclopédia Britannica – verbete 'Nosebleed'")
mc(T, "saúde pública", 2, 12, "Como se chama o sistema público de saúde do Brasil, criado pela Constituição de 1988?",
   ["Sistema Único de Saúde (SUS)", "INSS", "SAMU", "Anvisa"], "Sistema Único de Saúde (SUS)",
   "O SUS garante atendimento gratuito a qualquer pessoa no Brasil, de vacinas a transplantes.",
   "Ministério da Saúde", syn=("sus",), br=True)
op(T, "doenças e prevenção", 2, 12, "Qual doença, causada por um vírus e prevenida com vacina, é chamada popularmente de paralisia infantil?",
   "Poliomielite", ["poliomielite", "pólio", "polio"],
   "Graças à vacinação, o último caso de poliomielite no Brasil foi registrado em 1989.",
   "Ministério da Saúde")

# =========================================================== DIFÍCEIS
mc(T, "sangue", 3, 14, "Qual proteína dos glóbulos vermelhos, que contém ferro, carrega o oxigênio pelo corpo?",
   ["Hemoglobina", "Queratina", "Insulina", "Colágeno"], "Hemoglobina",
   "É a hemoglobina, rica em ferro, que dá a cor vermelha ao sangue.",
   "Enciclopédia Britannica – verbete 'Hemoglobin'")
mc(T, "sangue", 3, 14, "No adulto, onde é produzida a maior parte das células do sangue?",
   ["Medula óssea", "Coração", "Estômago", "Pulmões"], "Medula óssea",
   "A medula óssea é um tecido macio dentro de alguns ossos que produz glóbulos vermelhos, brancos e plaquetas.",
   "Enciclopédia Britannica – verbete 'Bone marrow'")
mc(T, "alimentação", 3, 14, "Qual nutriente a lei brasileira manda acrescentar ao sal de cozinha para prevenir o bócio?",
   ["Iodo", "Ferro", "Cálcio", "Flúor"], "Iodo",
   "O iodo é necessário para a glândula tireoide, e a falta dele pode fazer a tireoide crescer, o que se chama bócio e incha o pescoço.",
   "Anvisa", br=True)
tf(T, "cinco sentidos", 3, 12, "Cada parte da língua sente só um sabor: o doce na ponta e o amargo no fundo.", False,
   "Esse 'mapa da língua' é um mito: as papilas de todas as regiões da língua percebem todos os sabores.",
   "Enciclopédia Britannica – verbete 'Taste'")
op(T, "cinco sentidos", 3, 14, "Como se chama o quinto gosto básico, além de doce, salgado, azedo e amargo, identificado por um cientista japonês?",
   "Umami", ["umami"],
   "O umami foi descrito em 1908 por Kikunae Ikeda e lembra o gosto de caldos de carne e de tomate maduro.",
   "Enciclopédia Britannica – verbete 'Umami'")
mc(T, "cientistas da saúde", 3, 14, "Qual cientista francês criou a vacina contra a raiva, em 1885?",
   ["Louis Pasteur", "Robert Koch", "Joseph Lister", "Alexander Fleming"], "Louis Pasteur",
   "Pasteur também criou a pasteurização, processo que aquece alimentos como o leite para eliminar micróbios.",
   "Enciclopédia Britannica – verbete 'Louis Pasteur'")
mc(T, "cientistas da saúde", 3, 14, "Qual cientista brasileiro, pioneiro da medicina tropical, dá nome ao laboratório central de saúde pública de São Paulo?",
   ["Adolfo Lutz", "Emílio Ribas", "Carlos Chagas", "Oswaldo Cruz"], "Adolfo Lutz",
   "Adolfo Lutz estudou doenças tropicais e insetos transmissores, e o instituto com seu nome existe desde 1940.",
   "Instituto Adolfo Lutz", br=True)
mc(T, "saúde pública", 3, 14, "Qual instituição de pesquisa em saúde, no Rio de Janeiro, tem como símbolo um castelo em estilo mourisco?",
   ["Fundação Oswaldo Cruz", "Instituto Butantan", "Instituto Adolfo Lutz", "Instituto Nacional de Câncer"],
   "Fundação Oswaldo Cruz",
   "O Pavilhão Mourisco, no bairro de Manguinhos, é a sede histórica da Fiocruz.",
   "Fiocruz", syn=("fiocruz",), br=True)
mc(T, "cientistas da saúde", 3, 14, "Qual baiana, que cuidou de feridos na Guerra do Paraguai, é considerada a primeira enfermeira do Brasil?",
   ["Ana Néri", "Maria Quitéria", "Joana Angélica", "Anita Garibaldi"], "Ana Néri",
   "Ana Néri dá nome à escola de enfermagem da UFRJ e está no Livro dos Heróis e Heroínas da Pátria.",
   "Escola de Enfermagem Anna Nery – UFRJ", syn=("anna nery", "ana nery"), br=True)
tf(T, "ossos e músculos", 3, 14, "Os músculos do esqueleto só conseguem puxar, nunca empurrar.", True,
   "Os músculos trabalham em pares: quando um se contrai e puxa, o outro relaxa, como o bíceps e o tríceps.",
   "Enciclopédia Britannica – verbete 'Muscle'")
mc(T, "vacinação", 3, 14, "A vacina BCG, aplicada nos recém-nascidos, protege principalmente contra qual doença?",
   ["Tuberculose", "Sarampo", "Catapora", "Caxumba"], "Tuberculose",
   "A BCG protege as crianças contra as formas mais graves da tuberculose e é dada logo após o nascimento.",
   "Ministério da Saúde", br=True)
tf(T, "sistema nervoso", 3, 14, "O lado esquerdo do cérebro controla principalmente os movimentos do lado esquerdo do corpo.", False,
   "É o contrário: o hemisfério esquerdo comanda sobretudo o lado direito do corpo, e vice-versa.",
   "Enciclopédia Britannica – verbete 'Cerebrum'")

# =========================================================== MUITO DIFÍCEIS
mc(T, "cientistas da saúde", 4, 16, "Qual cirurgião fez o primeiro transplante de coração do Brasil, em 1968?",
   ["Euryclides de Jesus Zerbini", "Adib Jatene", "Ivo Pitanguy", "Christiaan Barnard"],
   "Euryclides de Jesus Zerbini",
   "A cirurgia foi feita no Hospital das Clínicas de São Paulo, poucos meses depois do primeiro transplante cardíaco do mundo.",
   "InCor – Instituto do Coração (HCFMUSP)", syn=("zerbini",), br=True)
mc(T, "cientistas da saúde", 4, 16, "Qual cientista descobriu os grupos sanguíneos A, B e O, em 1901?",
   ["Karl Landsteiner", "Robert Koch", "Joseph Lister", "Paul Ehrlich"], "Karl Landsteiner",
   "A descoberta tornou as transfusões de sangue seguras e rendeu a Landsteiner o Prêmio Nobel de 1930.",
   "Enciclopédia Britannica – verbete 'Karl Landsteiner'", syn=("landsteiner",))
mc(T, "sangue", 4, 16, "O fator Rh do sangue recebeu esse nome por causa de qual animal usado nas pesquisas?",
   ["Macaco", "Coelho", "Rato", "Porquinho-da-índia"], "Macaco",
   "O nome vem do macaco rhesus, usado nos estudos que identificaram esse fator, em 1940.",
   "Enciclopédia Britannica – verbete 'Rh blood group system'")
mc(T, "saúde pública", 4, 16, "Em que dia se comemora o Dia Nacional da Saúde, data do nascimento de Oswaldo Cruz?",
   ["5 de agosto", "7 de abril", "12 de outubro", "15 de novembro"], "5 de agosto",
   "Oswaldo Cruz nasceu em 5 de agosto de 1872, em São Luiz do Paraitinga (SP).",
   "Fiocruz", br=True)
mc(T, "vacinação", 4, 16, "Em que ano foi criado o Programa Nacional de Imunizações (PNI) do Brasil?",
   ["1973", "1988", "1960", "1994"], "1973",
   "O PNI organiza a vacinação gratuita no país e oferece dezenas de vacinas pelo SUS.",
   "Ministério da Saúde", br=True, ref="2026-10-13")
mc(T, "cientistas da saúde", 4, 16, "Qual psiquiatra alagoana usou a pintura no tratamento de pacientes e criou o Museu de Imagens do Inconsciente?",
   ["Nise da Silveira", "Zilda Arns", "Bertha Lutz", "Rachel de Queiroz"], "Nise da Silveira",
   "Nise da Silveira rejeitou tratamentos agressivos como o eletrochoque e defendeu a arte e o afeto no cuidado psiquiátrico.",
   "Enciclopédia Itaú Cultural – verbete 'Nise da Silveira'", br=True)
