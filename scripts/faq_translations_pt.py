"""
Brazilian Portuguese translations for all 48 FAQ questions across 7 categories.
Links are updated from /en/ to /pt/ paths.
"""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "Perguntas Gerais sobre Vistos",
    "Schengen & European Visas": "Vistos Schengen e Europeus",
    "Documents & Application Process": "Documentos e Processo de Candidatura",
    "Fees & Processing Times": "Taxas e Prazos de Processamento",
    "Extensions, Overstay & Refusal": "Extensões, Permanência Excessiva e Recusa",
    "Special Visa Types": "Tipos Especiais de Visto",
    "Embassy & Application Process": "Embaixada e Processo de Candidatura",
}

FAQ_TRANSLATIONS = [
    # ===== Category 1: General Visa Questions (7 questions) =====
    {
        "q_en": "What is an eVisa?",
        "q_pt": "O que é um eVisa?",
        "a_pt": 'Um eVisa (visto eletrônico) é uma autorização de viagem emitida digitalmente. Você solicita online, paga a taxa e recebe a aprovação por e-mail. Não é necessário ir à embaixada. Países como <a href="/pt/visa-turkey.html">Turquia</a>, <a href="/pt/visa-india.html">Índia</a>, <a href="/pt/visa-vietnam.html">Vietnã</a>, <a href="/pt/visa-cambodia.html">Camboja</a> e <a href="/pt/visa-australia.html">Austrália</a> oferecem eVisas.',
    },
    {
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_pt": "Qual é a diferença entre um visto e um eVisa?",
        "a_pt": "Um visto tradicional exige uma visita à embaixada ou consulado, entrega de documentos em papel e, às vezes, uma entrevista. Um eVisa é solicitado totalmente online, processado mais rapidamente (geralmente em 24 a 72 horas) e entregue eletronicamente por e-mail.",
    },
    {
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_pt": "O que é uma ETA (Autorização Eletrônica de Viagem)?",
        "a_pt": 'Uma ETA é uma triagem pré-viagem para cidadãos de países isentos de visto. Não é um visto, mas uma autorização de viagem vinculada ao seu passaporte. Países como <a href="/pt/visa-australia.html">Austrália</a>, Canadá, Nova Zelândia e Reino Unido utilizam sistemas de ETA. O sistema ETIAS da União Europeia será lançado em 2026.',
    },
    {
        "q_en": "What is visa-free travel?",
        "q_pt": "O que é viagem sem visto?",
        "a_pt": "Viagem sem visto significa que você pode entrar em um país sem solicitar visto previamente. Basta apresentar o passaporte na imigração. A permanência permitida geralmente é de 30 a 90 dias. Passaportes fortes (Japão, Singapura, UE) oferecem acesso sem visto a mais de 190 países.",
    },
    {
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_pt": "O que é um visto na chegada (VOA)?",
        "a_pt": 'Um visto na chegada é emitido no ponto de entrada (aeroporto ou posto de fronteira) sem solicitação prévia. Você apresenta o passaporte, preenche um formulário, paga a taxa e recebe o carimbo do visto. Países como <a href="/pt/visa-indonesia.html">Indonésia</a>, <a href="/pt/visa-nepal.html">Nepal</a> e <a href="/pt/visa-jordan.html">Jordânia</a> oferecem VOA para diversas nacionalidades.',
    },
    {
        "q_en": "How do I check if I need a visa?",
        "q_pt": "Como verifico se preciso de visto?",
        "a_pt": 'Os requisitos de visto dependem da sua nacionalidade e destino. Use nossa <a href="../index.html">ferramenta de busca de vistos</a> na página inicial ou consulte a <a href="../destination.html">página do país</a> específico. Em geral, cidadãos de países com passaportes fortes (UE, EUA, Reino Unido, Japão) têm acesso sem visto a mais de 150 países.',
    },
    {
        "q_en": "What is the strongest passport in the world?",
        "q_pt": "Qual é o passaporte mais forte do mundo?",
        "a_pt": "Em 2026, Japão, Singapura e vários passaportes da UE continuam sendo os mais fortes, oferecendo acesso sem visto ou com visto na chegada a mais de 190 países. O Henley Passport Index e o Arton Capital Index classificam os passaportes trimestralmente com base na liberdade de viagem.",
    },
    # ===== Category 2: Schengen & European Visas (6 questions) =====
    {
        "q_en": "What is a Schengen visa?",
        "q_pt": "O que é um visto Schengen?",
        "a_pt": 'Um visto Schengen permite viajar para 27 países europeus com um único visto. É válido para estadias curtas de até 90 dias em qualquer período de 180 dias. Você solicita na embaixada do país que mais visitará (ou pelo qual entrará primeiro). Consulte nossas páginas de visto para <a href="/pt/visa-france.html">França</a>, <a href="/pt/visa-germany.html">Alemanha</a>, <a href="/pt/visa-spain.html">Espanha</a> e <a href="/pt/visa-italy.html">Itália</a>.',
    },
    {
        "q_en": "How many countries are in the Schengen Area?",
        "q_pt": "Quantos países fazem parte do Espaço Schengen?",
        "a_pt": "Em 2026, o Espaço Schengen inclui 27 países: Áustria, Bélgica, Croácia, República Tcheca, Dinamarca, Estônia, Finlândia, França, Alemanha, Grécia, Hungria, Islândia, Itália, Letônia, Liechtenstein, Lituânia, Luxemburgo, Malta, Países Baixos, Noruega, Polônia, Portugal, Romênia, Eslováquia, Eslovênia, Espanha, Suécia e Suíça.",
    },
    {
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_pt": "Posso visitar vários países Schengen com um único visto?",
        "a_pt": "Sim. Um visto Schengen permite livre circulação entre os 27 países Schengen durante sua estadia autorizada (até 90 dias em 180 dias). Você deve solicitar na embaixada do seu destino principal ou do país de primeira entrada.",
    },
    {
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_pt": "O que é a regra dos 90/180 dias para Schengen?",
        "a_pt": 'A regra 90/180 significa que você pode permanecer no Espaço Schengen por no máximo 90 dias dentro de qualquer período de 180 dias. O cálculo é feito de forma contínua. Depois de usar 90 dias, você deve sair e aguardar até que dias suficientes tenham "expirado" antes de reentrar.',
    },
    {
        "q_en": "What is ETIAS and when does it start?",
        "q_pt": "O que é o ETIAS e quando começa a funcionar?",
        "a_pt": "O ETIAS (Sistema Europeu de Informação e Autorização de Viagem) é uma nova autorização pré-viagem para viajantes isentos de visto que visitam o Espaço Schengen. Será lançado em 2026. Cidadãos de mais de 60 países (EUA, Reino Unido, Canadá, Austrália, Japão) precisarão da aprovação ETIAS (EUR 7, válida por 3 anos) antes de viajar para a Europa.",
    },
    {
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_pt": "Posso entrar em um país Schengen diferente do país do meu visto?",
        "a_pt": "Sim, mas seu visto Schengen deve ser emitido pelo país do seu destino principal (estadia mais longa). Se você entrar por outro país, a imigração poderá questionar seu itinerário. Se todas as estadias forem iguais, solicite ao país de primeira entrada.",
    },
    # ===== Category 3: Documents & Application Process (9 questions) =====
    {
        "q_en": "What documents do I need for a visa application?",
        "q_pt": "Quais documentos são necessários para solicitar um visto?",
        "a_pt": 'Requisitos comuns: passaporte válido (mínimo 6 meses de validade), fotos para passaporte, formulário de solicitação preenchido, itinerário de viagem, reserva de hotel, comprovante de meios financeiros (extratos bancários), seguro viagem e carta-convite (se aplicável). Consulte nossa <a href="/pt/visa-documents-checklist.html">lista de documentos</a>.',
    },
    {
        "q_en": "What size photo is needed for a visa?",
        "q_pt": "Qual tamanho de foto é necessário para o visto?",
        "a_pt": 'A maioria dos países exige fotos de 35x45mm com fundo branco. Os EUA exigem 51x51mm (2x2 polegadas). As fotos devem ser recentes (últimos 6 meses), com expressão neutra e requisitos específicos de iluminação. Consulte nosso <a href="/pt/visa-photo-requirements.html">guia de requisitos de foto para visto</a>.',
    },
    {
        "q_en": "Do I need travel insurance for a visa?",
        "q_pt": "Preciso de seguro viagem para o visto?",
        "a_pt": 'Sim, para vistos Schengen é obrigatório ter seguro viagem com cobertura mínima de EUR 30.000. Muitos outros países também exigem ou recomendam fortemente. Consulte nosso <a href="/pt/travel-insurance-for-visa-applications.html">guia de seguro viagem</a>.',
    },
    {
        "q_en": "How long must my passport be valid for travel?",
        "q_pt": "Por quanto tempo meu passaporte deve ser válido para viajar?",
        "a_pt": "A maioria dos países exige que seu passaporte tenha validade de pelo menos 6 meses além da estadia planejada. Os países Schengen exigem 3 meses além da data de saída, mais duas páginas em branco. Sempre verifique os requisitos específicos do país.",
    },
    {
        "q_en": "Can I apply for a visa if my passport expires soon?",
        "q_pt": "Posso solicitar visto se meu passaporte vence em breve?",
        "a_pt": "Em geral, não. A maioria dos países exige 6 meses de validade no passaporte. Se seu passaporte vence dentro de 6 meses, renove-o antes de solicitar o visto. Alguns países também exigem páginas em branco para o adesivo de visto (geralmente 2 páginas em branco).",
    },
    {
        "q_en": "What bank statement amount do I need for a visa?",
        "q_pt": "Qual valor de extrato bancário é necessário para o visto?",
        "a_pt": "Para vistos Schengen, apresente EUR 50-100 por dia de estadia. Para o B1/B2 dos EUA, demonstre fundos suficientes (sem valor fixo). Para o Reino Unido, mostre 3 a 6 meses de renda consistente. Em geral, apresente um saldo bancário que cubra os custos da viagem mais 30-50% de margem.",
    },
    {
        "q_en": "Is a hotel booking required for a visa application?",
        "q_pt": "É necessária uma reserva de hotel para solicitar o visto?",
        "a_pt": "A maioria das solicitações de visto exige comprovante de hospedagem para toda a estadia. Pode ser uma reserva de hotel (não necessariamente paga), reserva no Airbnb ou carta do anfitrião. Para vistos Schengen, todas as noites devem estar cobertas.",
    },
    {
        "q_en": "Do I need a return ticket to get a visa?",
        "q_pt": "Preciso de passagem de volta para obter o visto?",
        "a_pt": "A maioria dos países exige comprovante de viagem de retorno ou continuação para solicitações de visto e na imigração. Pode ser uma reserva de voo confirmada, passagem de ônibus ou balsa mostrando que você planeja sair antes do vencimento do visto.",
    },
    {
        "q_en": "What is an invitation letter for a visa?",
        "q_pt": "O que é uma carta-convite para visto?",
        "a_pt": "Uma carta-convite é um documento de uma pessoa ou organização no país de destino convidando você a visitar. Inclui dados do anfitrião, seu relacionamento, objetivo e datas da visita, acomodação e responsabilidade financeira. É exigida em muitas solicitações de visto Schengen e de negócios.",
    },
    {
        "q_en": "What are biometrics for a visa?",
        "q_pt": "O que são dados biométricos para visto?",
        "a_pt": "Dados biométricos incluem impressões digitais e foto digital coletados durante a solicitação do visto. Países Schengen, Reino Unido, EUA, Canadá e muitos outros exigem biometria. São armazenados para verificação de identidade e geralmente têm validade de 5 anos.",
    },
    # ===== Category 4: Fees & Processing Times (6 questions) =====
    {
        "q_en": "How much does a visa cost?",
        "q_pt": "Quanto custa um visto?",
        "a_pt": 'As taxas de visto variam bastante. Exemplos: visto Schengen EUR 80, visto B1/B2 dos EUA USD 185, eVisa da Índia USD 25-80, eVisa da Turquia USD 50, ETA da Austrália AUD 20, eVisa do Camboja USD 36. Crianças e algumas nacionalidades podem ter taxas reduzidas. Consulte nossa página de <a href="/pt/visa-processing-times.html">prazos de processamento</a>.',
    },
    {
        "q_en": "How long does visa processing take?",
        "q_pt": "Quanto tempo leva o processamento do visto?",
        "a_pt": "eVisas geralmente levam de 24 a 72 horas. Vistos Schengen levam de 15 a 45 dias corridos. Vistos B1/B2 dos EUA podem levar semanas a meses, dependendo da embaixada. Sempre solicite com bastante antecedência da data de viagem.",
    },
    {
        "q_en": "How far in advance should I apply for a visa?",
        "q_pt": "Com quanta antecedência devo solicitar o visto?",
        "a_pt": "Para eVisas: 1 a 2 semanas antes da viagem. Para vistos Schengen: 3 a 6 meses de antecedência (mínimo 15 dias antes da partida, máximo 6 meses). Para vistos dos EUA: 3 a 6 meses ou mais, devido aos longos tempos de espera. Temporadas de pico podem exigir solicitações mais antecipadas.",
    },
    {
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_pt": "Posso obter reembolso do visto se minha solicitação for recusada?",
        "a_pt": "Na maioria dos casos, as taxas de visto não são reembolsáveis, independentemente do resultado. A taxa cobre o custo de processamento da sua solicitação, não uma garantia de aprovação.",
    },
    {
        "q_en": "How do I track my visa application status?",
        "q_pt": "Como acompanho o status da minha solicitação de visto?",
        "a_pt": "A maioria das embaixadas e escritórios da VFS Global oferece rastreamento online. Você receberá um número de referência ao enviar a solicitação. Insira esse número no site da embaixada ou da VFS. Alguns países também enviam atualizações por e-mail/SMS em cada etapa do processamento.",
    },
    {
        "q_en": "What is VFS Global?",
        "q_pt": "O que é a VFS Global?",
        "a_pt": "A VFS Global é uma empresa privada que processa solicitações de visto em nome de governos. Ela opera centros de solicitação de visto (VACs) em todo o mundo. Você entrega os documentos em um centro VFS em vez de ir diretamente à embaixada. A VFS cobra uma taxa de serviço além da taxa do visto.",
    },
    # ===== Category 5: Extensions, Overstay & Refusal (4 questions) =====
    {
        "q_en": "Can I extend my visa?",
        "q_pt": "Posso estender meu visto?",
        "a_pt": 'Depende do país e do tipo de visto. Alguns países permitem extensões (por exemplo, o VOA da Indonésia pode ser estendido por 30 dias, o visto de turismo da Tailândia pode ser estendido por 30 dias). Vistos Schengen só podem ser estendidos em circunstâncias excepcionais. Consulte nossa página sobre <a href="/pt/visa-rejection-reasons.html">motivos de recusa de visto</a> para informações relacionadas.',
    },
    {
        "q_en": "What happens if my visa is refused?",
        "q_pt": "O que acontece se meu visto for recusado?",
        "a_pt": "Você receberá uma notificação por escrito com o motivo. Razões comuns incluem comprovação financeira insuficiente, documentos incompletos ou suspeita de intenção migratória. Geralmente, você pode recorrer dentro de 1 a 3 meses ou solicitar novamente com documentação aprimorada.",
    },
    {
        "q_en": "What is overstaying a visa?",
        "q_pt": "O que é permanência excessiva (overstay) de visto?",
        "a_pt": "Permanência excessiva significa ficar além da estadia autorizada. As consequências incluem multas (por exemplo, a Tailândia cobra 500 THB/dia), deportação, detenção, proibição de entrada (1 a 10 anos) e dificuldade para obter vistos futuros. Sempre respeite as datas de validade do seu visto.",
    },
    {
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_pt": "O que acontece se eu perder meu passaporte com um visto válido?",
        "a_pt": "Entre em contato imediatamente com a embaixada mais próxima do seu país para obter um documento de viagem de emergência. Você precisará solicitar um novo visto, pois vistos em passaportes perdidos são considerados nulos. Faça um boletim de ocorrência e guarde uma cópia para a nova solicitação.",
    },
    # ===== Category 6: Special Visa Types (10 questions) =====
    {
        "q_en": "What is a transit visa?",
        "q_pt": "O que é um visto de trânsito?",
        "a_pt": "Um visto de trânsito permite passar por um país a caminho do seu destino final. Geralmente é válido por 24 a 72 horas. Alguns países exigem visto de trânsito mesmo que você não saia do aeroporto.",
    },
    {
        "q_en": "Can I work on a tourist visa?",
        "q_pt": "Posso trabalhar com visto de turismo?",
        "a_pt": "Não. Vistos de turismo geralmente não permitem emprego. Trabalhar com visto de turismo é ilegal na maioria dos países e pode resultar em deportação, multas e negação de vistos futuros. Você precisa de um visto de trabalho ou autorização de trabalho separada.",
    },
    {
        "q_en": "What is a digital nomad visa?",
        "q_pt": "O que é um visto para nômade digital?",
        "a_pt": 'Um visto para nômade digital permite que trabalhadores remotos vivam em um país enquanto trabalham para empregadores ou clientes no exterior. Países populares incluem <a href="/pt/visa-portugal.html">Portugal</a>, <a href="/pt/visa-spain.html">Espanha</a>, <a href="/pt/visa-thailand.html">Tailândia</a>, <a href="/pt/visa-colombia.html">Colômbia</a> e <a href="/pt/visa-indonesia.html">Indonésia</a>. Consulte nosso <a href="/pt/digital-nomad-visas-guide.html">guia de vistos para nômades digitais</a>.',
    },
    {
        "q_en": "What is a student visa?",
        "q_pt": "O que é um visto de estudante?",
        "a_pt": "Um visto de estudante permite estudar em uma instituição educacional em outro país. Os requisitos incluem carta de aceitação, comprovante de pagamento de mensalidade ou bolsa de estudos, meios financeiros para despesas de moradia, seguro saúde e, às vezes, certificados de proficiência no idioma.",
    },
    {
        "q_en": "What is a Working Holiday Visa?",
        "q_pt": "O que é um Visto de Férias-Trabalho (Working Holiday Visa)?",
        "a_pt": 'Um Visto de Férias-Trabalho (WHV) permite que jovens (geralmente de 18 a 30 ou 18 a 35 anos) viajem e trabalhem em outro país por 1 a 2 anos. Programas populares incluem <a href="/pt/visa-australia.html">Austrália</a>, <a href="/pt/visa-new-zealand.html">Nova Zelândia</a>, <a href="/pt/visa-canada.html">Canadá</a> e <a href="/pt/visa-japan.html">Japão</a>.',
    },
    {
        "q_en": "What is a Golden Visa?",
        "q_pt": "O que é um Golden Visa (Visto Dourado)?",
        "a_pt": 'Um Golden Visa é uma autorização de residência concedida a investidores que fazem um investimento financeiro significativo (geralmente imobiliário ou empresarial). Programas populares existem em <a href="/pt/visa-portugal.html">Portugal</a>, <a href="/pt/visa-spain.html">Espanha</a>, <a href="/pt/visa-greece.html">Grécia</a> e <a href="/pt/visa-uae.html">Emirados Árabes Unidos</a>. Investimentos variam de EUR 250.000 a EUR 500.000+.',
    },
    {
        "q_en": "What is a long-stay visa (Type D)?",
        "q_pt": "O que é um visto de longa duração (Tipo D)?",
        "a_pt": "Um visto Tipo D (visto nacional) permite estadias superiores a 90 dias em um país específico. Diferente do visto Schengen de curta duração (Tipo C), o Tipo D é emitido por países individuais para fins como estudo, trabalho, reunificação familiar ou aposentadoria.",
    },
    {
        "q_en": "What is a multiple-entry visa?",
        "q_pt": "O que é um visto de múltiplas entradas?",
        "a_pt": "Um visto de múltiplas entradas permite entrar e sair de um país várias vezes durante a validade do visto. É útil para viajantes de negócios ou pessoas que visitam países vizinhos. Vistos de entrada única tornam-se inválidos após a primeira saída do país.",
    },
    {
        "q_en": "Do children need their own visa?",
        "q_pt": "Crianças precisam do próprio visto?",
        "a_pt": "Sim, crianças precisam do próprio visto na maioria dos casos, inclusive bebês. Alguns países oferecem taxas reduzidas para menores de 6 ou 12 anos. Crianças devem ter passaporte próprio para a maioria das viagens internacionais.",
    },
    {
        "q_en": "Can dual citizens use either passport for visas?",
        "q_pt": "Cidadãos com dupla nacionalidade podem usar qualquer passaporte para vistos?",
        "a_pt": "Sim, cidadãos com dupla nacionalidade podem escolher qual passaporte usar. Use o que oferece melhores condições de visto. Sempre entre e saia de um país com o mesmo passaporte. Alguns países não reconhecem a dupla cidadania — verifique as leis de ambos os seus países.",
    },
    # ===== Category 7: Embassy & Application Process (5 questions) =====
    {
        "q_en": "How do I apply for a visa at an embassy?",
        "q_pt": "Como solicito um visto em uma embaixada?",
        "a_pt": 'Passos: 1) Verifique os requisitos no site da embaixada. 2) Reúna os documentos. 3) Agende um horário. 4) Compareça e entregue os documentos. 5) Pague a taxa. 6) Aguarde o processamento. 7) Retire seu passaporte com o visto. Consulte nosso <a href="/pt/how-to-apply-evisa.html">guia de como solicitar</a>.',
    },
    {
        "q_en": "What is a visa interview?",
        "q_pt": "O que é uma entrevista de visto?",
        "a_pt": "Alguns países (especialmente EUA, Reino Unido e Canadá) exigem uma entrevista presencial na embaixada. O oficial consular perguntará sobre seus planos de viagem, vínculos com seu país de origem, situação financeira e motivo da visita. Seja honesto e leve documentos comprobatórios.",
    },
    {
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_pt": "Posso solicitar visto em um país do qual não sou cidadão?",
        "a_pt": "Sim, em muitos casos você pode solicitar na embaixada de um país onde tenha residência legal. Será necessário apresentar comprovante de residência legal (autorização de residência, visto de longa duração). Alguns países só aceitam solicitações de cidadãos ou residentes permanentes do país anfitrião.",
    },
    {
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_pt": "Qual a diferença entre adesivo de visto, carimbo e e-visa?",
        "a_pt": "Um adesivo de visto é uma etiqueta física afixada em uma página do passaporte (Schengen, EUA, Reino Unido). Um carimbo de visto é uma marca de entrada/saída carimbada pela imigração. Um e-visa é uma autorização digital vinculada ao número do seu passaporte — sem necessidade de adesivo físico.",
    },
    {
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_pt": "Posso viajar com um visto em um passaporte cancelado?",
        "a_pt": "Em alguns casos sim, se o visto ainda for válido. Países como os EUA e o Reino Unido permitem que você viaje com um visto válido em um passaporte antigo junto com o passaporte novo. Verifique as regras específicas do país, pois alguns exigem que o visto seja transferido para o novo passaporte.",
    },
]

# Verify count
# The HTML accordion contains 47 visible cards (the JSON-LD schema has 48
# entries but "Can I apply for a visa if my passport expires soon?" only
# appears in the schema, not as an accordion card). We include the extra
# question here for completeness so translations cover all schema entries too.
assert len(FAQ_TRANSLATIONS) == 48, f"Expected 48 questions, got {len(FAQ_TRANSLATIONS)}"
