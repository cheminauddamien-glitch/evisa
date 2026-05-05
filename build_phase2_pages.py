"""Build the 7 remaining Phase 2 pages (EN) + localize to 9 other languages.
Each destination has a config dict with content; we render via the
maldives template skeleton.
"""
import os, json, re

LANGS = {
    'en': {'lang_attr':'en','flag':'fi-gb','label':'English','dir':None},
    'fr': {'lang_attr':'fr','flag':'fi-fr','label':'Français','dir':None},
    'es': {'lang_attr':'es','flag':'fi-es','label':'Español','dir':None},
    'pt': {'lang_attr':'pt','flag':'fi-br','label':'Português','dir':None},
    'zh': {'lang_attr':'zh','flag':'fi-cn','label':'中文','dir':None},
    'th': {'lang_attr':'th','flag':'fi-th','label':'ไทย','dir':None},
    'ru': {'lang_attr':'ru','flag':'fi-ru','label':'Русский','dir':None},
    'ar': {'lang_attr':'ar','flag':'fi-sa','label':'العربية','dir':'rtl'},
    'ja': {'lang_attr':'ja','flag':'fi-jp','label':'日本語','dir':None},
    'ko': {'lang_attr':'ko','flag':'fi-kr','label':'한국어','dir':None},
}

# Per-destination content (English source).
# host_country = main country whose visa applies. parent_flags shown in H1.
DESTINATIONS = {
    'laos': {
        'slug':'laos-visa-requirements',
        'title_en':'Laos Visa Requirements 2026 — eVisa, Visa on Arrival & Entry Rules',
        'h1_en':'Laos Visa Requirements 2026 — eVisa, Visa on Arrival & Entry Rules',
        'meta_en':'Laos visa requirements 2026: eVisa USD 30, visa on arrival USD 30–45, 30-day stay, passport rules and documents needed for Vientiane, Luang Prabang and Vang Vieng.',
        'flags':['la'],
        'titles_loc':{
            'fr':'Laos conditions de visa 2026 — eVisa, visa à l&rsquo;arrivée &amp; règles d&rsquo;entrée',
            'es':'Laos requisitos de visa 2026 — eVisa, visa al llegar y reglas de entrada',
            'pt':'Laos requisitos de visto 2026 — eVisa, visto na chegada e regras de entrada',
        },
        'metas_loc':{
            'fr':'Laos conditions de visa 2026 : eVisa USD 30, visa à l&rsquo;arrivée USD 30–45, séjour 30 jours, règles de passeport et documents pour Vientiane, Luang Prabang et Vang Vieng.',
            'es':'Laos requisitos de visa 2026: eVisa USD 30, visa al llegar USD 30–45, estancia de 30 días, reglas de pasaporte y documentos para Vientián, Luang Prabang y Vang Vieng.',
            'pt':'Laos requisitos de visto 2026: eVisa USD 30, visto na chegada USD 30–45, estadia de 30 dias, regras de passaporte e documentos para Vientiane, Luang Prabang e Vang Vieng.',
        },
        'key_facts':[
            ('eVisa', 'Available since 2019 — USD 30, 30-day stay'),
            ('Visa on arrival', 'USD 30–45 at airports and major land borders'),
            ('Stay allowed', '30 days (extendable up to 90 days in country)'),
            ('Passport validity', 'Minimum 6 months beyond entry'),
            ('Photo requirement', '1 passport photo required'),
            ('Entry points', 'Wattay (VTE), Luang Prabang (LPQ), Pakse, plus 30+ land borders'),
            ('Official portal', 'laoevisa.gov.la'),
        ],
        'h2_blocks':[
            ('Overview of Laos Entry Requirements 2026',
             'Laos welcomes foreign tourists through three channels in 2026: a 30-day eVisa applied online before travel, a visa on arrival at major airports and selected land borders, and full visa-free entry for ASEAN passport holders. Most travelers from Europe, North America, Australia, Japan and South Korea use either the eVisa or the visa on arrival, whichever is more convenient for their entry route.'),
            ('Documents Checklist for Laos Entry 2026',
             '<ul><li>Valid passport — minimum 6 months validity beyond entry</li><li>One blank passport page</li><li>One recent passport photo (4×6 cm)</li><li>Return or onward ticket</li><li>Proof of accommodation (hotel booking or invitation)</li><li>Visa fee in USD cash (visa on arrival) or paid online (eVisa)</li><li>Sufficient funds — USD 50 per day per person</li></ul>'),
            ('Laos eVisa vs Visa on Arrival',
             'The eVisa is recommended if you enter Laos through a remote land border (some borders do not issue visas on arrival), or if you want to lock in costs and avoid queues. The visa on arrival is faster if you fly into Vientiane (VTE) or Luang Prabang (LPQ) — counters are well-organized and processing takes 15–30 minutes. Both visas grant the same 30-day single-entry stay and the same USD 30 fee for most nationalities.'),
            ('Visa-Free Nationalities for Laos',
             'Citizens of Brunei, Cambodia, Indonesia, Malaysia, Myanmar, Philippines, Singapore, Thailand and Vietnam (ASEAN members) enter Laos visa-free for 14–30 days. Japanese, South Korean, Russian and Mongolian citizens also enjoy 30-day visa-free entry under bilateral agreements. All other nationalities require an eVisa or visa on arrival.'),
            ('Extending Your Stay in Laos',
             'A Laos tourist visa can be extended in-country at the Department of Immigration in Vientiane for an additional 30 to 60 days. Extensions cost USD 2 per day. Overstays are fined USD 10 per day at the airport on departure — keep your stay current.'),
        ],
        'related':[
            ('Main Laos Visa Guide', '/en/visa-laos.html'),
            ('How to Apply for an eVisa', '/en/how-to-apply-evisa.html'),
            ('Visa Documents Checklist', '/en/visa-documents-checklist.html'),
            ('Visa Processing Times', '/en/visa-processing-times.html'),
        ],
        'related_loc_h':{'fr':'Guides Laos liés','es':'Guías de Laos relacionadas','pt':'Guias do Laos relacionados'},
        'h2_loc':{
            'fr':[
                'Aperçu des conditions d&rsquo;entrée au Laos 2026',
                'Liste des documents pour l&rsquo;entrée au Laos 2026',
                'eVisa Laos vs visa à l&rsquo;arrivée',
                'Nationalités exemptées de visa pour le Laos',
                'Prolonger son séjour au Laos',
            ],
            'es':[
                'Resumen de requisitos de entrada a Laos 2026',
                'Lista de documentos para entrar a Laos 2026',
                'eVisa Laos vs visa al llegar',
                'Nacionalidades exentas de visa para Laos',
                'Extender la estancia en Laos',
            ],
            'pt':[
                'Visão geral dos requisitos de entrada em Laos 2026',
                'Lista de documentos para entrar em Laos 2026',
                'eVisa Laos vs visto na chegada',
                'Nacionalidades isentas de visto para Laos',
                'Estender a estadia em Laos',
            ],
        },
    },
    'taipei': {
        'slug':'taipei-visa-requirements',
        'title_en':'Taipei Visa Requirements 2026 — Taiwan eVisa & Visa-Free Entry for the Capital',
        'h1_en':'Taipei Visa Requirements 2026 — Taiwan Entry Rules',
        'meta_en':'Taipei visa requirements 2026: Taiwan eVisa USD 31, 90-day visa-free for US/EU/UK/Canada/Australia/Japan, Taoyuan airport entry, documents and passport rules.',
        'flags':['tw'],
        'titles_loc':{
            'fr':'Taipei conditions de visa 2026 — eVisa Taïwan &amp; entrée sans visa pour la capitale',
            'es':'Taipéi requisitos de visa 2026 — eVisa Taiwán y entrada sin visa para la capital',
            'pt':'Taipei requisitos de visto 2026 — eVisa Taiwan e entrada sem visto para a capital',
        },
        'metas_loc':{
            'fr':'Taipei conditions de visa 2026 : eVisa Taïwan USD 31, exemption 90 jours pour US/UE/UK/Canada/Australie/Japon, aéroport de Taoyuan, documents et passeport.',
            'es':'Taipéi requisitos de visa 2026: eVisa Taiwán USD 31, 90 días sin visa para US/UE/UK/Canadá/Australia/Japón, aeropuerto de Taoyuan, documentos y pasaporte.',
            'pt':'Taipei requisitos de visto 2026: eVisa Taiwan USD 31, 90 dias sem visto para US/UE/UK/Canadá/Austrália/Japão, aeroporto de Taoyuan, documentos e passaporte.',
        },
        'key_facts':[
            ('Taipei is in', 'Taiwan (Republic of China) — its capital'),
            ('Visa-free stay', '90 days for US, EU, UK, Canada, Australia, NZ, Japan, South Korea'),
            ('eVisa', 'USD 31 for nationalities not on visa-free list — 30-day stay'),
            ('Entry airport', 'Taiwan Taoyuan International (TPE) — 40 km from central Taipei'),
            ('Passport validity', 'Minimum 6 months beyond intended stay'),
            ('Onward ticket', 'Required at check-in and on arrival'),
            ('Official portal', 'boca.gov.tw'),
        ],
        'h2_blocks':[
            ('Why Taipei Visa Rules Are Taiwan Visa Rules',
             'Taipei is the capital of Taiwan, so the visa requirements for visiting Taipei are identical to those for entering Taiwan. There is no separate Taipei visa or city-specific entry permit. The only entry airport for Taipei is Taiwan Taoyuan International (TPE), about 40 km from the city, served by the Taoyuan Airport MRT.'),
            ('Visa-Free Entry to Taipei (Taiwan) 2026',
             'Citizens of the United States, United Kingdom, all 27 EU member states, Canada, Australia, New Zealand, Japan, South Korea, Singapore, Malaysia and 60+ other countries can enter Taiwan visa-free for up to 90 days. No eVisa, no advance application — just present a valid passport and an onward ticket on arrival at TPE.'),
            ('Taiwan eVisa for Other Nationalities',
             'Travelers from countries not on the visa-free list (including most of Africa, Central Asia and parts of the Middle East) can apply for the Taiwan eVisa online at boca.gov.tw before traveling. The eVisa costs USD 31, allows a 30-day single-entry stay and is processed within 5 business days. Indian, Filipino, Thai, Indonesian, Vietnamese and Cambodian citizens have a streamlined eVisa process.'),
            ('Documents for Entry into Taipei',
             '<ul><li>Passport valid for 6+ months from entry date</li><li>Return or onward flight ticket</li><li>Proof of accommodation in Taipei (hotel booking, host address)</li><li>Sufficient funds (USD 100 per day suggested)</li><li>Arrival card filled in on the plane</li><li>For eVisa holders: printed eVisa approval letter</li></ul>'),
            ('Travel Within Taipei After Arrival',
             'No additional permits are needed for moving around Taipei or anywhere in Taiwan. EasyCard transit pass works on the MRT, buses and trains. Travelers wishing to visit Kinmen, Matsu or Penghu (outlying islands) use the same Taiwan visa or visa-free entry — no extra documents required.'),
        ],
        'related':[
            ('Main Taiwan Visa Guide', '/en/visa-taiwan.html'),
            ('Taiwan Visa Requirements', '/en/taiwan-visa-requirements.html'),
            ('Taiwan Visa Fees', '/en/taiwan-visa-fees.html'),
            ('Taiwan Visa Processing Time', '/en/taiwan-visa-processing-time.html'),
        ],
        'related_loc_h':{'fr':'Guides Taïwan liés','es':'Guías de Taiwán relacionadas','pt':'Guias de Taiwan relacionados'},
        'h2_loc':{
            'fr':['Pourquoi les règles de visa Taipei sont celles de Taïwan',
                  'Entrée sans visa à Taipei (Taïwan) 2026',
                  'eVisa Taïwan pour les autres nationalités',
                  'Documents pour entrer à Taipei',
                  'Se déplacer dans Taipei après l&rsquo;arrivée'],
            'es':['Por qué las reglas de visa de Taipéi son las de Taiwán',
                  'Entrada sin visa a Taipéi (Taiwán) 2026',
                  'eVisa Taiwán para otras nacionalidades',
                  'Documentos para entrar a Taipéi',
                  'Moverse por Taipéi después de la llegada'],
            'pt':['Por que as regras de visto de Taipei são as de Taiwan',
                  'Entrada sem visto em Taipei (Taiwan) 2026',
                  'eVisa Taiwan para outras nacionalidades',
                  'Documentos para entrar em Taipei',
                  'Locomoção em Taipei após a chegada'],
        },
    },
    'machu-picchu': {
        'slug':'machu-picchu-visa-requirements',
        'title_en':'Machu Picchu Visa Requirements 2026 — Peru Entry Rules & Citadel Permit',
        'h1_en':'Machu Picchu Visa Requirements 2026 — Peru Entry Rules',
        'meta_en':'Machu Picchu visa requirements 2026: Peru visa-free 183 days for US/EU/UK/Canada/Australia, citadel ticket online, documents and passport rules for Cusco entry.',
        'flags':['pe'],
        'titles_loc':{
            'fr':'Machu Picchu conditions de visa 2026 — Pérou règles d&rsquo;entrée &amp; permis de la citadelle',
            'es':'Machu Picchu requisitos de visa 2026 — Perú reglas de entrada y permiso de la ciudadela',
            'pt':'Machu Picchu requisitos de visto 2026 — Peru regras de entrada e permissão da cidadela',
        },
        'metas_loc':{
            'fr':'Machu Picchu conditions de visa 2026 : Pérou exemption 183 jours pour US/UE/UK/Canada/Australie, billet de la citadelle en ligne, documents et passeport pour Cusco.',
            'es':'Machu Picchu requisitos de visa 2026: Perú sin visa 183 días para US/UE/UK/Canadá/Australia, boleto de la ciudadela en línea, documentos y pasaporte para Cusco.',
            'pt':'Machu Picchu requisitos de visto 2026: Peru sem visto 183 dias para US/UE/UK/Canadá/Austrália, bilhete da cidadela online, documentos e passaporte para Cusco.',
        },
        'key_facts':[
            ('Machu Picchu is in', 'Peru — Cusco region, accessed via Aguas Calientes'),
            ('Peru visa-free', '183 days for US, EU, UK, Canada, Australia, NZ, Japan and 100+ countries'),
            ('Citadel entry ticket', 'Required separately — book at machupicchu.gob.pe in advance'),
            ('Daily visitor cap', '5,600 visitors/day in 2026 — book 1–3 months ahead in high season'),
            ('Passport validity', 'Minimum 6 months beyond entry date'),
            ('Altitude warning', 'Cusco at 3,400 m — acclimatize 2 days before the citadel'),
            ('Official portals', 'migraciones.gob.pe (visa) · machupicchu.gob.pe (ticket)'),
        ],
        'h2_blocks':[
            ('Visiting Machu Picchu Means Entering Peru',
             'Machu Picchu is a UNESCO World Heritage site located in the Cusco region of southern Peru, at 2,430 m altitude. There is no Machu Picchu visa — visitors enter Peru first, then travel to the citadel via Cusco and Aguas Calientes. Two separate documents are needed: (1) a Peruvian tourist entry stamp at the airport, and (2) a Machu Picchu citadel ticket booked online before arrival.'),
            ('Peru Entry Requirements for Machu Picchu Visitors 2026',
             'Citizens of the United States, United Kingdom, all 27 EU countries, Canada, Australia, New Zealand, Japan, South Korea, Brazil, Argentina, Chile and 100+ others enter Peru visa-free for up to 183 days as tourists. The stamp is given at Lima (LIM) or Cusco (CUZ) airport on arrival. No advance application needed for these passports.'),
            ('Machu Picchu Citadel Tickets — How to Book',
             'The citadel ticket is mandatory and sold online at machupicchu.gob.pe. There are several circuits (1, 2, 3, 4) and time slots. A standard ticket costs around USD 45–55, students get a discount with valid ID. Book 1–3 months ahead for July–August peak. Tickets are non-refundable and tied to the entry date.'),
            ('Documents Checklist for the Machu Picchu Trip',
             '<ul><li>Passport valid 6+ months</li><li>Onward ticket out of Peru</li><li>Machu Picchu citadel ticket (printed or PDF on phone)</li><li>Train ticket (Cusco/Ollantaytambo to Aguas Calientes — PeruRail or IncaRail)</li><li>Bus ticket Aguas Calientes to citadel entry (USD 24 round-trip)</li><li>ISIC card if claiming student discount</li><li>Yellow fever vaccine — recommended if combining with Amazon trip</li></ul>'),
            ('Inca Trail Permit (Optional 4-Day Trek)',
             'For those hiking the classic Inca Trail to Machu Picchu, a separate permit is required and only 500 places are released daily (200 trekkers + 300 porters/guides). Permits sell out 4–6 months in advance through licensed operators. The Salkantay Trail and Lares Trek are alternatives that do not require permits.'),
        ],
        'related':[
            ('Main Peru Visa Guide', '/en/visa-peru.html'),
            ('How to Apply for an eVisa', '/en/how-to-apply-evisa.html'),
            ('Visa Documents Checklist', '/en/visa-documents-checklist.html'),
            ('Visa Processing Times', '/en/visa-processing-times.html'),
        ],
        'related_loc_h':{'fr':'Guides Pérou liés','es':'Guías de Perú relacionadas','pt':'Guias do Peru relacionados'},
        'h2_loc':{
            'fr':['Visiter le Machu Picchu signifie entrer au Pérou',
                  'Pérou conditions d&rsquo;entrée pour les visiteurs du Machu Picchu 2026',
                  'Billets pour la citadelle du Machu Picchu — comment réserver',
                  'Liste des documents pour le voyage au Machu Picchu',
                  'Permis du Chemin de l&rsquo;Inca (trek 4 jours en option)'],
            'es':['Visitar Machu Picchu significa entrar a Perú',
                  'Perú requisitos de entrada para visitantes de Machu Picchu 2026',
                  'Boletos para la ciudadela de Machu Picchu — cómo reservar',
                  'Lista de documentos para el viaje a Machu Picchu',
                  'Permiso del Camino Inca (trek opcional de 4 días)'],
            'pt':['Visitar Machu Picchu significa entrar no Peru',
                  'Peru requisitos de entrada para visitantes de Machu Picchu 2026',
                  'Bilhetes para a cidadela de Machu Picchu — como reservar',
                  'Lista de documentos para a viagem a Machu Picchu',
                  'Permissão da Trilha Inca (caminhada opcional de 4 dias)'],
        },
    },
    'bermuda': {
        'slug':'bermuda-visa-requirements',
        'title_en':'Bermuda Visa Requirements 2026 — British Overseas Territory Entry Rules',
        'h1_en':'Bermuda Visa Requirements 2026 — Entry Rules for the British Overseas Territory',
        'meta_en':'Bermuda visa requirements 2026: visa-free 90 days for US/UK/EU/Canada, Bermuda Travel Authorization not required since 2022, documents and passport rules.',
        'flags':['bm'],
        'titles_loc':{
            'fr':'Bermudes conditions de visa 2026 — règles d&rsquo;entrée du territoire britannique d&rsquo;outre-mer',
            'es':'Bermudas requisitos de visa 2026 — reglas de entrada del territorio británico de ultramar',
            'pt':'Bermudas requisitos de visto 2026 — regras de entrada do território britânico ultramarino',
        },
        'metas_loc':{
            'fr':'Bermudes conditions de visa 2026 : exemption 90 jours pour US/UK/UE/Canada, autorisation de voyage Bermudes supprimée depuis 2022, documents et passeport.',
            'es':'Bermudas requisitos de visa 2026: 90 días sin visa para US/UK/UE/Canadá, autorización de viaje a Bermudas eliminada desde 2022, documentos y pasaporte.',
            'pt':'Bermudas requisitos de visto 2026: 90 dias sem visto para US/UK/UE/Canadá, autorização de viagem para Bermudas removida desde 2022, documentos e passaporte.',
        },
        'key_facts':[
            ('Bermuda status', 'British Overseas Territory — separate visa system from UK'),
            ('Visa-free stay', '90 days for US, UK, EU, Canada, Australia, NZ and 80+ countries'),
            ('Bermuda Travel Authorization', 'No longer required since June 2022'),
            ('Passport validity', 'Minimum 45 days beyond intended departure'),
            ('Onward ticket', 'Required at boarding and on arrival'),
            ('Entry airport', 'L.F. Wade International (BDA) — only airport on the island'),
            ('Official portal', 'gov.bm/department/immigration'),
        ],
        'h2_blocks':[
            ('Bermuda Has Its Own Visa System',
             'Although Bermuda is a British Overseas Territory, it is not part of the United Kingdom and operates its own immigration regime. A UK visitor visa does not automatically grant entry to Bermuda. However, the visa-free list is similar to the UK&rsquo;s: most Western passports do not need any visa, while nationalities that need a UK visa generally also need a Bermuda visa.'),
            ('Visa-Free Entry to Bermuda 2026',
             'Citizens of the United States, United Kingdom, Canada, Australia, New Zealand, Japan, all EU member states and 80+ other countries can enter Bermuda for up to 90 days as tourists with no advance authorization. The Bermuda Travel Authorization (BTA) was suspended in June 2022 and remains discontinued in 2026. Just present a valid passport and onward ticket on arrival at BDA.'),
            ('Documents Checklist for Bermuda Entry',
             '<ul><li>Passport valid for at least 45 days beyond intended departure</li><li>Return or onward flight ticket</li><li>Proof of accommodation (hotel, Airbnb, or sponsor letter)</li><li>Sufficient funds for the stay (USD 200/day recommended)</li><li>Bermuda Customs Declaration form (handed out on the plane)</li><li>No advance visa or eTA required for visa-exempt nationalities</li></ul>'),
            ('Who Needs a Visa for Bermuda',
             'Travelers from countries that require a UK visit visa generally also require a Bermuda visa — including most African, Central Asian and some Middle Eastern nationalities. Apply through a British High Commission or Bermuda&rsquo;s overseas representations. Processing takes 4–8 weeks; book the visa appointment well in advance.'),
            ('Working or Living in Bermuda',
             'A tourist stay does not allow paid work, even short-term. Bermuda&rsquo;s &ldquo;Work From Bermuda&rdquo; certificate (introduced 2020) allows remote workers and students to live in Bermuda for one year — applications are made online before travel and cost USD 263.'),
        ],
        'related':[
            ('Main Bermuda Visa Guide', '/en/visa-bermuda.html'),
            ('How to Apply for an eVisa', '/en/how-to-apply-evisa.html'),
            ('Visa Documents Checklist', '/en/visa-documents-checklist.html'),
            ('Visa Processing Times', '/en/visa-processing-times.html'),
        ],
        'related_loc_h':{'fr':'Guides Bermudes liés','es':'Guías de Bermudas relacionadas','pt':'Guias das Bermudas relacionados'},
        'h2_loc':{
            'fr':['Les Bermudes ont leur propre système de visa',
                  'Entrée sans visa aux Bermudes 2026',
                  'Liste des documents pour l&rsquo;entrée aux Bermudes',
                  'Qui a besoin d&rsquo;un visa pour les Bermudes',
                  'Travailler ou vivre aux Bermudes'],
            'es':['Bermudas tiene su propio sistema de visa',
                  'Entrada sin visa a Bermudas 2026',
                  'Lista de documentos para entrar a Bermudas',
                  'Quién necesita visa para Bermudas',
                  'Trabajar o vivir en Bermudas'],
            'pt':['Bermudas tem seu próprio sistema de vistos',
                  'Entrada sem visto nas Bermudas 2026',
                  'Lista de documentos para entrar nas Bermudas',
                  'Quem precisa de visto para Bermudas',
                  'Trabalhar ou viver nas Bermudas'],
        },
    },
    'macau': {
        'slug':'macau-visa-requirements',
        'title_en':'Macau Visa Requirements 2026 — China SAR Entry Rules & Visa-Free List',
        'h1_en':'Macau Visa Requirements 2026 — China SAR Entry Rules',
        'meta_en':'Macau visa requirements 2026: visa-free 30–90 days for US/EU/UK/Canada/Australia, separate from China visa, documents and passport rules for the Macau SAR.',
        'flags':['mo'],
        'titles_loc':{
            'fr':'Macao conditions de visa 2026 — règles d&rsquo;entrée RAS de Chine et liste sans visa',
            'es':'Macao requisitos de visa 2026 — reglas de entrada RAE de China y lista sin visa',
            'pt':'Macau requisitos de visto 2026 — regras de entrada RAE da China e lista sem visto',
        },
        'metas_loc':{
            'fr':'Macao conditions de visa 2026 : exemption 30–90 jours pour US/UE/UK/Canada/Australie, distinct du visa Chine, documents et passeport pour la RAS de Macao.',
            'es':'Macao requisitos de visa 2026: 30–90 días sin visa para US/UE/UK/Canadá/Australia, separado del visado China, documentos y pasaporte para la RAE de Macao.',
            'pt':'Macau requisitos de visto 2026: 30–90 dias sem visto para US/UE/UK/Canadá/Austrália, separado do visto China, documentos e passaporte para a RAE de Macau.',
        },
        'key_facts':[
            ('Macau status', 'Special Administrative Region (SAR) of China — separate immigration'),
            ('Visa-free stay', '30 days for most passports, 90 days for UK/Brazil, 60 days for Hong Kong residents'),
            ('China visa', 'Not valid for Macau — separate entry stamp required'),
            ('Passport validity', 'Minimum 30 days beyond intended departure'),
            ('Entry points', 'Macau International Airport (MFM), ferry terminals, HZMB land border'),
            ('Visa on arrival', 'Available for some nationalities (USD 25–125 depending on passport)'),
            ('Official portal', 'fsm.gov.mo'),
        ],
        'h2_blocks':[
            ('Macau Is Separate from Mainland China',
             'Macau is a Special Administrative Region of China but operates a completely separate immigration system. A Chinese visa does not allow entry to Macau, and a Macau entry stamp does not allow entry to mainland China. Travelers crossing between Zhuhai (mainland) and Macau must clear immigration in both directions.'),
            ('Visa-Free Entry to Macau 2026',
             'Citizens of the United States, all EU countries, Canada, Australia, New Zealand, Japan, South Korea and 70+ others enter Macau visa-free for 30 days. UK and Brazilian passports get 90 days. Hong Kong permanent residents get 60 days. No advance application — entry stamp issued on arrival at Macau International Airport, ferry terminal or land border.'),
            ('Visa on Arrival for Other Nationalities',
             'Macau offers a visa on arrival for nationalities not on the visa-free list, including Indian, Filipino, Indonesian, Vietnamese and Pakistani passports. Fees range from MOP 100 (~USD 12) for individual transit to MOP 200 (~USD 25) for a 30-day single-entry visa. Some passports must apply at a Chinese embassy in advance — check with fsm.gov.mo before flying.'),
            ('Documents for Entering Macau',
             '<ul><li>Passport valid for 30+ days beyond intended departure</li><li>Onward or return ticket</li><li>Sufficient funds (HKD 1,000–3,000/day suggested)</li><li>Hotel booking (only required for first night, very flexible)</li><li>Health Declaration card (currently waived in 2026)</li><li>Macau-specific entry: no Chinese visa needed</li></ul>'),
            ('Crossing Between Macau and Mainland China',
             'The Hong Kong-Zhuhai-Macau Bridge (HZMB) and the Gongbei border crossing connect Macau to mainland China. Travelers exit Macau immigration, then enter Chinese immigration at Zhuhai — a Chinese visa is required separately. The 144-hour visa-free transit policy applies to Zhuhai for many nationalities flying through.'),
        ],
        'related':[
            ('Main Macau Visa Guide', '/en/visa-macau.html'),
            ('Hong Kong Visa Requirements', '/en/hong-kong-visa-requirements.html'),
            ('China Visa Requirements', '/en/china-visa-requirements.html'),
            ('How to Apply for an eVisa', '/en/how-to-apply-evisa.html'),
        ],
        'related_loc_h':{'fr':'Guides Macao &amp; Chine liés','es':'Guías de Macao y China relacionadas','pt':'Guias de Macau e China relacionados'},
        'h2_loc':{
            'fr':['Macao est distinct de la Chine continentale',
                  'Entrée sans visa à Macao 2026',
                  'Visa à l&rsquo;arrivée pour les autres nationalités',
                  'Documents pour entrer à Macao',
                  'Traverser entre Macao et la Chine continentale'],
            'es':['Macao es separado de China continental',
                  'Entrada sin visa a Macao 2026',
                  'Visa al llegar para otras nacionalidades',
                  'Documentos para entrar a Macao',
                  'Cruzar entre Macao y China continental'],
            'pt':['Macau é separado da China continental',
                  'Entrada sem visto em Macau 2026',
                  'Visto na chegada para outras nacionalidades',
                  'Documentos para entrar em Macau',
                  'Atravessar entre Macau e a China continental'],
        },
    },
    'amsterdam': {
        'slug':'amsterdam-visa-requirements',
        'title_en':'Amsterdam Visa Requirements 2026 — Netherlands Schengen Entry Rules',
        'h1_en':'Amsterdam Visa Requirements 2026 — Netherlands Schengen Entry Rules',
        'meta_en':'Amsterdam visa requirements 2026: Netherlands Schengen visa, 90/180-day rule, ETIAS from 2026, US/EU/UK/Canada visa-free, documents and Schiphol airport rules.',
        'flags':['nl'],
        'titles_loc':{
            'fr':'Amsterdam conditions de visa 2026 — règles d&rsquo;entrée Schengen Pays-Bas',
            'es':'Ámsterdam requisitos de visa 2026 — reglas de entrada Schengen Países Bajos',
            'pt':'Amsterdã requisitos de visto 2026 — regras de entrada Schengen Países Baixos',
        },
        'metas_loc':{
            'fr':'Amsterdam conditions de visa 2026 : visa Schengen Pays-Bas, règle 90/180 jours, ETIAS dès 2026, US/UE/UK/Canada sans visa, documents et règles aéroport Schiphol.',
            'es':'Ámsterdam requisitos de visa 2026: visa Schengen Países Bajos, regla 90/180 días, ETIAS desde 2026, US/UE/UK/Canadá sin visa, documentos y aeropuerto Schiphol.',
            'pt':'Amsterdã requisitos de visto 2026: visto Schengen Países Baixos, regra 90/180 dias, ETIAS desde 2026, US/UE/UK/Canadá sem visto, documentos e aeroporto Schiphol.',
        },
        'key_facts':[
            ('Amsterdam is in', 'The Netherlands — Schengen Area member'),
            ('Visa-free stay', '90 days within any 180-day period for US/UK/Canada/Australia/Japan'),
            ('Schengen visa', 'Required for nationalities not on the visa-free list'),
            ('ETIAS 2026', 'Required for visa-exempt non-EU travelers from late 2026 — €7'),
            ('Passport validity', 'Minimum 3 months beyond Schengen exit date'),
            ('Entry airport', 'Amsterdam Schiphol (AMS) — Europe&rsquo;s 3rd-busiest hub'),
            ('Official portal', 'netherlandsworldwide.nl'),
        ],
        'h2_blocks':[
            ('Amsterdam Visa = Netherlands Schengen Visa',
             'Amsterdam has no separate visa or city-specific entry permit. The Netherlands is a member of the Schengen Area, so the same visa rules apply for Amsterdam, Rotterdam, Utrecht and any other Dutch city. A Schengen visa issued by any of the 29 Schengen states allows entry to Amsterdam through Schiphol Airport (AMS) or land/sea borders.'),
            ('Visa-Free Entry to Amsterdam (Schengen) 2026',
             'Citizens of the United States, United Kingdom, Canada, Australia, New Zealand, Japan, South Korea, Singapore and 60+ other countries enter the Schengen Area visa-free for 90 days within any 180-day period. The 90/180-day rule is enforced strictly — overstays trigger fines and entry bans. Time spent in any Schengen country counts against the same 90-day quota.'),
            ('Schengen Visa Application for Amsterdam',
             'For nationalities that need a Schengen visa, the Netherlands embassy or consulate (or VFS Global outsourcing center) accepts applications when the Netherlands is the main destination. The fee is €90 (~USD 95). Required documents: completed form, passport, photo, travel insurance with €30,000 coverage, hotel booking, return ticket, financial proof and itinerary. Processing takes 15 days standard, up to 45 in busy periods.'),
            ('ETIAS Authorization From Late 2026',
             'The European Travel Information and Authorization System (ETIAS) is rolling out from late 2026. Visa-exempt non-EU travelers (US, UK, Canada, Australia, etc.) will need an ETIAS authorization (€7, valid 3 years) before entering any Schengen country, including the Netherlands. Apply online at travel-europe.europa.eu — most approvals are issued within minutes.'),
            ('Documents Checklist for Schiphol Arrival',
             '<ul><li>Passport valid 3+ months beyond Schengen exit date</li><li>Schengen visa (if required) or ETIAS approval (from late 2026)</li><li>Return or onward ticket</li><li>Hotel booking or address of stay</li><li>Travel insurance with €30,000 medical coverage (mandatory for visa applicants, recommended for all)</li><li>Sufficient funds (€34/day or €55/day if not pre-booked)</li></ul>'),
        ],
        'related':[
            ('Main Netherlands Visa Guide', '/en/visa-netherlands.html'),
            ('Netherlands Visa Requirements', '/en/netherlands-visa-requirements.html'),
            ('Schengen Visa Application Guide', '/en/how-to-apply-evisa.html'),
            ('Visa Documents Checklist', '/en/visa-documents-checklist.html'),
        ],
        'related_loc_h':{'fr':'Guides Pays-Bas &amp; Schengen liés','es':'Guías de Países Bajos y Schengen relacionadas','pt':'Guias dos Países Baixos e Schengen relacionados'},
        'h2_loc':{
            'fr':['Visa Amsterdam = visa Schengen Pays-Bas',
                  'Entrée sans visa à Amsterdam (Schengen) 2026',
                  'Demande de visa Schengen pour Amsterdam',
                  'Autorisation ETIAS dès fin 2026',
                  'Liste des documents pour l&rsquo;arrivée à Schiphol'],
            'es':['Visa Ámsterdam = visa Schengen Países Bajos',
                  'Entrada sin visa a Ámsterdam (Schengen) 2026',
                  'Solicitud de visa Schengen para Ámsterdam',
                  'Autorización ETIAS desde fines de 2026',
                  'Lista de documentos para llegar a Schiphol'],
            'pt':['Visto Amsterdã = visto Schengen Países Baixos',
                  'Entrada sem visto em Amsterdã (Schengen) 2026',
                  'Solicitação de visto Schengen para Amsterdã',
                  'Autorização ETIAS a partir do final de 2026',
                  'Lista de documentos para a chegada em Schiphol'],
        },
    },
    'cappadocia': {
        'slug':'cappadocia-visa-requirements',
        'title_en':'Cappadocia Visa Requirements 2026 — Turkey eVisa & Entry Rules for Göreme',
        'h1_en':'Cappadocia Visa Requirements 2026 — Turkey Entry Rules',
        'meta_en':'Cappadocia visa requirements 2026: Turkey eVisa USD 50, visa-free 90 days for EU/UK, hot air balloon permits, Kayseri/Nevşehir airports, documents and rules.',
        'flags':['tr'],
        'titles_loc':{
            'fr':'Cappadoce conditions de visa 2026 — eVisa Turquie &amp; règles d&rsquo;entrée pour Göreme',
            'es':'Capadocia requisitos de visa 2026 — eVisa Turquía y reglas de entrada para Göreme',
            'pt':'Capadócia requisitos de visto 2026 — eVisa Turquia e regras de entrada para Göreme',
        },
        'metas_loc':{
            'fr':'Cappadoce conditions de visa 2026 : eVisa Turquie USD 50, exemption 90 jours pour UE/UK, permis de montgolfière, aéroports Kayseri/Nevşehir, documents et règles.',
            'es':'Capadocia requisitos de visa 2026: eVisa Turquía USD 50, 90 días sin visa para UE/UK, permisos de globo aerostático, aeropuertos Kayseri/Nevşehir, documentos.',
            'pt':'Capadócia requisitos de visto 2026: eVisa Turquia USD 50, 90 dias sem visto para UE/UK, permissões de balão, aeroportos Kayseri/Nevşehir, documentos.',
        },
        'key_facts':[
            ('Cappadocia is in', 'Turkey — Nevşehir Province, central Anatolia'),
            ('Turkey eVisa', 'USD 50 for US/UK/Canada/Australia, valid 90/180 days'),
            ('Visa-free stay', '90 days per 180 for EU, Japan, Korea, Singapore'),
            ('Main airports', 'Kayseri (ASR) and Nevşehir (NAV) — both 1 hour from Göreme'),
            ('Passport validity', 'Minimum 6 months beyond intended stay'),
            ('Hot air balloon', 'No additional visa or permit needed for tourists'),
            ('Official portal', 'evisa.gov.tr'),
        ],
        'h2_blocks':[
            ('Cappadocia Visa = Turkey eVisa or Schengen-Style Stamp',
             'Cappadocia is a region in central Turkey, not a separate state. Visiting Göreme, Üçhisar, Avanos or any Cappadocia town requires a Turkish entry visa or visa exemption. There is no Cappadocia-specific permit. The standard Turkey eVisa or visa-free entry stamp suffices for the entire country.'),
            ('Turkey eVisa for Cappadocia 2026',
             'Citizens of the United States, United Kingdom, Canada, Australia, India, China, Mexico, South Africa and 100+ others can apply for the Turkey eVisa online at evisa.gov.tr before traveling. Cost: USD 50, valid for stays up to 90 days within 180 days. Approval is typically immediate; print the eVisa or save the PDF on your phone.'),
            ('Visa-Free Entry for Cappadocia Tourism',
             'Citizens of all 27 EU member states, Switzerland, Norway, Iceland, Japan, South Korea, Singapore, Brazil, Argentina and 30+ others enter Turkey visa-free for 90 days within any 180-day period. The Russian Federation has its own bilateral agreement allowing 60-day visa-free stays.'),
            ('How to Reach Cappadocia',
             'Most international travelers fly to Istanbul (IST or SAW) and connect to Kayseri (ASR) or Nevşehir (NAV) — both airports are 60–80 minutes from Göreme by road. Direct flights from European hubs to Kayseri are available in summer. The eVisa or stamp is issued at the international entry point (typically Istanbul), not at the regional airport.'),
            ('Documents for Cappadocia and Hot Air Balloon Rides',
             '<ul><li>Passport valid 6+ months beyond stay</li><li>Turkey eVisa printed or on phone (or visa-free entry stamp)</li><li>Onward ticket out of Turkey</li><li>Hotel booking in Göreme/Ürgüp/Avanos</li><li>Sufficient funds (USD 50/day suggested)</li><li>For hot air balloon rides: no extra visa needed; just the activity booking and waiver signed at the operator</li><li>Travel insurance recommended (balloon flights are activity-class)</li></ul>'),
        ],
        'related':[
            ('Main Turkey Visa Guide', '/en/visa-turkey.html'),
            ('Turkey Visa Requirements', '/en/turkey-visa-requirements.html'),
            ('Turkey Visa Fees', '/en/turkey-visa-fees.html'),
            ('Turkey Visa Processing Time', '/en/turkey-visa-processing-time.html'),
        ],
        'related_loc_h':{'fr':'Guides Turquie liés','es':'Guías de Turquía relacionadas','pt':'Guias da Turquia relacionados'},
        'h2_loc':{
            'fr':['Visa Cappadoce = eVisa Turquie ou tampon style Schengen',
                  'eVisa Turquie pour la Cappadoce 2026',
                  'Entrée sans visa pour le tourisme en Cappadoce',
                  'Comment rejoindre la Cappadoce',
                  'Documents pour la Cappadoce et les vols en montgolfière'],
            'es':['Visa Capadocia = eVisa Turquía o sello tipo Schengen',
                  'eVisa Turquía para Capadocia 2026',
                  'Entrada sin visa para turismo en Capadocia',
                  'Cómo llegar a Capadocia',
                  'Documentos para Capadocia y paseos en globo'],
            'pt':['Visto Capadócia = eVisa Turquia ou carimbo tipo Schengen',
                  'eVisa Turquia para Capadócia 2026',
                  'Entrada sem visto para turismo na Capadócia',
                  'Como chegar à Capadócia',
                  'Documentos para Capadócia e voos de balão'],
        },
    },
}


HEAD_TPL = """<!DOCTYPE html>
<html lang="{html_lang}"{html_dir}>
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-XC1GYM27WC');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686"
            crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport" />
    <meta content="{meta}" name="description"/>
    <meta content="index, follow" name="robots" />
    <link href="https://www.evisa-card.com/{lang}/{slug}.html" rel="canonical" />
    <meta content="{title}" property="og:title" />
    <meta content="{meta}" property="og:description" />
    <meta content="website" property="og:type" />
    <meta content="https://www.evisa-card.com/{lang}/{slug}.html" property="og:url" />
    <meta content="https://www.evisa-card.com/images/og-image.jpg" property="og:image" />
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "eVisa-Card.com",
      "url": "https://www.evisa-card.com",
      "logo": "https://www.evisa-card.com/images/logo.png",
      "sameAs": [
        "https://facebook.com/evisacard",
        "https://twitter.com/evisacard",
        "https://instagram.com/evisacard"
      ],
      "description": "eVisa-Card.com provides global eVisa information and online travel authorization guides for tourists and business travelers."
    }}
    </script>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}.html"/>
    <link rel="alternate" hreflang="fr" href="https://www.evisa-card.com/fr/{slug}.html"/>
    <link rel="alternate" hreflang="es" href="https://www.evisa-card.com/es/{slug}.html"/>
    <link rel="alternate" hreflang="pt" href="https://www.evisa-card.com/pt/{slug}.html"/>
    <link rel="alternate" hreflang="zh" href="https://www.evisa-card.com/zh/{slug}.html"/>
    <link rel="alternate" hreflang="th" href="https://www.evisa-card.com/th/{slug}.html"/>
    <link rel="alternate" hreflang="ru" href="https://www.evisa-card.com/ru/{slug}.html"/>
    <link rel="alternate" hreflang="ar" href="https://www.evisa-card.com/ar/{slug}.html"/>
    <link rel="alternate" hreflang="ja" href="https://www.evisa-card.com/ja/{slug}.html"/>
    <link rel="alternate" hreflang="ko" href="https://www.evisa-card.com/ko/{slug}.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}.html"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
</head>
"""

NAV_TPL_ITEM = '<a class="dropdown-item{active}" href="/{lang}/{slug}.html"><span class="fi {flag}"></span> {label}</a>\n                        '

NAV_TPL = """<body>
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
    <div class="container">
        <a class="navbar-brand" href="../index.html" style="padding:0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:120px;width:auto;display:block;"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
            <ul class="navbar-nav align-items-center">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/expat-guides.html">Guides</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {current_flag}"></span> {current_label}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        {dropdown_items}
</div>
                </li>
            </ul>
        </div>
    </div>
</nav>
"""


def render_dropdown(slug, current_lang):
    items = []
    for code, c in LANGS.items():
        active = ' active' if code == current_lang else ''
        items.append(NAV_TPL_ITEM.format(active=active, lang=code, slug=slug, flag=c['flag'], label=c['label']))
    return ''.join(items).rstrip()


def render_body(dest, lang):
    flags_html = ''.join(f'<span class="fi fi-{f}"></span>' for f in dest['flags'])

    if lang in ('fr','es','pt'):
        title = dest['titles_loc'][lang]
        h1 = dest['titles_loc'][lang]
        meta = dest['metas_loc'][lang]
        h2_list = dest['h2_loc'][lang]
        related_h = dest['related_loc_h'][lang]
    else:
        title = dest['title_en']
        h1 = dest['h1_en']
        meta = dest['meta_en']
        h2_list = [b[0] for b in dest['h2_blocks']]
        related_h = 'Related Guides'

    key_facts_rows = '\n'.join(
        f'<tr><th>{k}</th><td>{v}</td></tr>' for k, v in dest['key_facts']
    )

    h2_blocks_html = []
    for i, (en_h2, content) in enumerate(dest['h2_blocks']):
        h2_text = h2_list[i] if i < len(h2_list) else en_h2
        h2_id = re.sub(r'[^a-z0-9]+', '-', en_h2.lower()).strip('-')
        if content.startswith('<ul>') or content.startswith('<ol>'):
            block = f'<h2 id="{h2_id}">{h2_text}</h2>\n{content}'
        else:
            block = f'<h2 id="{h2_id}">{h2_text}</h2>\n<p>{content}</p>'
        h2_blocks_html.append(block)
    h2_html = '\n\n'.join(h2_blocks_html)

    related_btns = '\n    '.join(
        f'<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{href}">{label}</a>'
        for label, href in dest['related']
    )

    related_pages_btns = '\n        '.join(
        f'<a href="{href}" style="display:inline-block;padding:6px 14px;border:1px solid #3b82f6;border-radius:6px;color:#3b82f6;text-decoration:none;font-size:13px;font-weight:500;transition:background .2s,color .2s;" class="btn btn-outline-primary btn-sm">{label}</a>'
        for label, href in dest['related']
    )

    body = f"""<section class="ftco-section"><div class="container"><article>
<h1>{flags_html} {h1}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts 2026</th></tr></thead>
<tbody>
{key_facts_rows}
</tbody>
</table>

{h2_html}

<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: April 2026. Sources: official embassy and immigration websites.</div>
<div class="mt-4 pt-3 border-top">
    <h3 class="h6">{related_h}</h3>
    {related_btns}
</div>
</article></div></section>
<!-- Related Pages -->
<div style="background:#f8f9fc;border-radius:8px;padding:20px 24px;margin:0 auto 30px;max-width:960px;">
    <h3 style="font-size:16px;color:#1d2d50;margin-bottom:14px;">{related_h}</h3>
    <div style="display:flex;flex-wrap:wrap;gap:8px;">
        {related_pages_btns}
    </div>
</div>
<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
        <div class="container">
            <div class="row mb-5 justify-content-center">
                <div class="col-md-6 text-center">
                    <p class="mt-4">&copy; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
                    <p class="mt-2" style="font-size:13px;">
                        <a href="/en/legal-notice.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Legal Notice</a>
                        &nbsp;|&nbsp;
                        <a href="/en/disclaimer.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">Disclaimer</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <div class="show fullscreen" id="ftco-loader">
        <svg class="circular" height="48px" width="48px">
            <circle class="path-bg" cx="24" cy="24" fill="none" r="22" stroke="#eeeeee" stroke-width="4"></circle>
            <circle class="path" cx="24" cy="24" fill="none" r="22" stroke="#F96D00" stroke-miterlimit="10" stroke-width="4"></circle>
        </svg>
    </div>
<script src="../js/jquery.min.js"></script>
<script src="../js/jquery-migrate-3.0.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/jquery.easing.1.3.js"></script>
<script src="../js/jquery.waypoints.min.js"></script>
<script src="../js/jquery.stellar.min.js"></script>
<script src="../js/owl.carousel.min.js"></script>
<script src="../js/jquery.magnific-popup.min.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>
"""
    return body, title, meta


def render_page(dest, lang):
    cfg = LANGS[lang]
    body, title, meta = render_body(dest, lang)
    head = HEAD_TPL.format(
        html_lang=cfg['lang_attr'],
        html_dir=' dir="rtl"' if cfg.get('dir') == 'rtl' else '',
        title=title,
        meta=meta,
        slug=dest['slug'],
        lang=lang,
    )
    nav = NAV_TPL.format(
        current_flag=cfg['flag'],
        current_label=cfg['label'],
        dropdown_items=render_dropdown(dest['slug'], lang),
    )
    return head + nav + body


def main():
    os.makedirs('www', exist_ok=True)
    count = 0
    for key, dest in DESTINATIONS.items():
        for lang in LANGS:
            html = render_page(dest, lang)
            target = f'www/{lang}/{dest["slug"]}.html'
            with open(target, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
    print(f'Generated {count} files')


if __name__ == '__main__':
    main()
