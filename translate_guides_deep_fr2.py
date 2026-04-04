#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
translate_guides_deep_fr2.py
Deep translation of remaining English text in FR expat guide pages.
Uses direct string + regex replacements on raw HTML content.
Preserves HTML tags, attributes, URLs, classes, styles, JSON-LD, nav, footer.
"""

import os
import re
import glob

# ---------------------------------------------------------------------------
FR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "fr")
PATTERN = os.path.join(FR_DIR, "expat-guide-*.html")

# ---------------------------------------------------------------------------
# PASS 1: Exact string replacements (longest first, applied in order)
# These replace English text found between HTML tags.
# ---------------------------------------------------------------------------

REPLACEMENTS = [
    # =========================================================================
    # INTRO PARAGRAPHS (full English paragraphs per country)
    # =========================================================================
    # Cambodia
    ("Cambodia is one of Southeast Asia's most accessible expat destinations — ultra-low cost of living, a fully dollarised economy (USD used everywhere), relatively straightforward residency via business or ordinary visa, and Phnom Penh and Siem Reap offer surprisingly vibrant expat communities.",
     "Le Cambodge est l'une des destinations expatriées les plus accessibles d'Asie du Sud-Est — coût de la vie ultra-bas, économie entièrement dollarisée (USD utilisé partout), résidence relativement simple via un visa d'affaires ou ordinaire, et Phnom Penh et Siem Reap offrent des communautés expatriées étonnamment dynamiques."),
    # Colombia
    ("Colombia has transformed dramatically over the past decade", "La Colombie s'est transformée de manière spectaculaire au cours de la dernière décennie"),
    ("was named the world's most innovative city, and cities like", "a été nommée la ville la plus innovante au monde, et des villes comme"),
    ("offer a rich mix of culture, climate and affordability.", "offrent un riche mélange de culture, de climat et d'accessibilité."),
    ("Colombia's digital nomad visa and affordable EPS health system make it increasingly popular with expats.", "Le visa nomade numérique de la Colombie et le système de santé EPS abordable la rendent de plus en plus populaire auprès des expatriés."),
    # Costa Rica
    ("Costa Rica — Pura Vida — is a long-standing favourite of North American and European expats. Stable democracy, no standing army, excellent healthcare, lush biodiversity and a well-developed expat infrastructure make it one of the easiest countries in Latin America to settle in.",
     "Le Costa Rica — Pura Vida — est un favori de longue date des expatriés nord-américains et européens. Démocratie stable, pas d'armée permanente, excellents soins de santé, biodiversité luxuriante et infrastructure expatriée bien développée en font l'un des pays les plus faciles d'Amérique latine pour s'installer."),
    # Georgia
    ("Georgia (the Caucasus country) has emerged as one of the", "La Géorgie (le pays du Caucase) est devenue l'une des"),
    ("destinations for digital nomads, entrepreneurs and expats worldwide. The reasons: 365-day visa-free entry for 95+ nationalities, 1% personal income tax for small businesses, no capital gains tax on crypto, and a low cost of living.",
     "destinations pour les nomades numériques, les entrepreneurs et les expatriés du monde entier. Les raisons : entrée sans visa de 365 jours pour 95+ nationalités, 1 % d'impôt sur le revenu pour les petites entreprises, pas d'impôt sur les plus-values crypto, et un faible coût de la vie."),
    # Greece
    ("Greece offers an extraordinary quality of life — Mediterranean climate, rich history, world-class cuisine and an affordable cost of living by EU standards. The Golden Visa, Non-Dom tax regime and Digital Nomad Visa have made Greece increasingly attractive to international expats.",
     "La Grèce offre une qualité de vie extraordinaire — climat méditerranéen, riche histoire, cuisine de classe mondiale et coût de la vie abordable par rapport aux standards de l'UE. Le Golden Visa, le régime fiscal Non-Dom et le visa nomade numérique ont rendu la Grèce de plus en plus attractive pour les expatriés internationaux."),
    # Japan
    ("Japan combines extraordinary safety, efficient infrastructure, unique culture and excellent healthcare. The 2024 Digital Nomad Visa and the Highly Skilled Professional (HSP) point system have made Japan more accessible than ever for skilled foreign workers.",
     "Le Japon combine une sécurité extraordinaire, une infrastructure efficace, une culture unique et d'excellents soins de santé. Le visa nomade numérique de 2024 et le système de points pour les professionnels hautement qualifiés (HSP) ont rendu le Japon plus accessible que jamais pour les travailleurs étrangers qualifiés."),
    # Laos
    ("Laos is one of Southeast Asia's least-explored expat destinations — very low cost of living, a relaxed pace of life, beautiful natural landscapes and a growing (if small) expat community in Vientiane and Luang Prabang.",
     "Le Laos est l'une des destinations expatriées les moins explorées d'Asie du Sud-Est — coût de la vie très bas, rythme de vie détendu, magnifiques paysages naturels et une communauté expatriée en croissance (bien que petite) à Vientiane et Luang Prabang."),
    # Malaysia
    ("Malaysia is one of Asia's most underrated expat destinations", "La Malaisie est l'une des destinations expatriées les plus sous-estimées d'Asie"),
    ("English is widely spoken, infrastructure", "l'anglais est largement parlé, l'infrastructure"),
    ("the food is extraordinary and the cost of living is among the lowest in the region for this quality of life.",
     "la cuisine est extraordinaire et le coût de la vie est parmi les plus bas de la région pour cette qualité de vie."),
    # Mexico
    ("Mexico is the world's most popular expat destination for North Americans — proximity to the US and Canada, low cost of living, rich culture, year-round warm weather and well-established expat communities in dozens of cities.",
     "Le Mexique est la destination expatriée la plus populaire au monde pour les Nord-Américains — proximité avec les États-Unis et le Canada, faible coût de la vie, riche culture, climat chaud toute l'année et communautés expatriées bien établies dans des dizaines de villes."),
    # Panama
    ("Panama is one of the most popular retirement and expat destinations in Latin America. The Pensionado visa offers extraordinary benefits, the economy is dollarised (USD), healthcare is good and improving, and Panama City is a major international hub.",
     "Le Panama est l'une des destinations de retraite et d'expatriation les plus populaires d'Amérique latine. Le visa Pensionado offre des avantages extraordinaires, l'économie est dollarisée (USD), les soins de santé sont bons et en amélioration, et Panama City est un hub international majeur."),
    # Paraguay
    ("Paraguay is emerging as a top choice for expats seeking a low-tax, low-cost-of-living environment with relatively easy residency. The territorial tax system (no tax on foreign-source income), fast permanent residency and affordable real estate make it particularly attractive for digital nomads, crypto investors and retirees.",
     "Le Paraguay émerge comme un choix de premier plan pour les expatriés recherchant un environnement à faible fiscalité et faible coût de la vie avec une résidence relativement facile. Le système fiscal territorial (pas d'impôt sur les revenus de source étrangère), la résidence permanente rapide et l'immobilier abordable le rendent particulièrement attractif pour les nomades numériques, les investisseurs crypto et les retraités."),
    # Portugal
    ("Portugal has become one of Europe's most popular expat destinations — excellent climate, affordable cost of living (by Western European standards), outstanding healthcare, rich culture and the highly attractive NHR (Non-Habitual Resident) tax regime.",
     "Le Portugal est devenu l'une des destinations expatriées les plus populaires d'Europe — excellent climat, coût de la vie abordable (par rapport aux standards d'Europe de l'Ouest), soins de santé exceptionnels, riche culture et le régime fiscal NHR (Résident Non Habituel) très attractif."),
    # Spain
    ("Spain offers year-round sunshine, rich culture, excellent food and one of Europe's best healthcare systems. With the Non-Lucrative Visa, Digital Nomad Visa and Golden Visa, Spain has become a top destination for expats from around the world.",
     "L'Espagne offre du soleil toute l'année, une riche culture, une excellente gastronomie et l'un des meilleurs systèmes de santé d'Europe. Avec le visa Non Lucratif, le visa Nomade Numérique et le Golden Visa, l'Espagne est devenue une destination de premier plan pour les expatriés du monde entier."),
    # UAE
    ("The UAE — particularly Dubai — has positioned itself as the world's leading destination for high-net-worth expats and remote workers. Zero income tax, world-class infrastructure, modern healthcare and a cosmopolitan lifestyle make it uniquely attractive.",
     "Les EAU — en particulier Dubaï — se sont positionnés comme la destination mondiale de premier plan pour les expatriés fortunés et les travailleurs à distance. Zéro impôt sur le revenu, infrastructure de classe mondiale, soins de santé modernes et style de vie cosmopolite en font une destination unique."),
    # Vietnam
    ("Vietnam is rapidly growing in popularity among expats — Hanoi and Ho Chi Minh City offer vibrant urban life, Da Nang and Hoi An provide a more relaxed coastal lifestyle, and the cost of living is among the lowest in Asia for the quality of life you get.",
     "Le Vietnam gagne rapidement en popularité auprès des expatriés — Hanoï et Hô Chi Minh-Ville offrent une vie urbaine dynamique, Da Nang et Hoi An proposent un style de vie côtier plus détendu, et le coût de la vie est parmi les plus bas d'Asie pour la qualité de vie obtenue."),

    # =========================================================================
    # VISA TABLE CELLS - Detail column content
    # =========================================================================
    # Generic visa detail patterns
    ("For remote workers. Must prove", "Pour les travailleurs à distance. Doit prouver"),
    ("income (3× minimum wage).", "de revenus (3× le salaire minimum)."),
    ("2-year visa with", "Visa de 2 ans avec"),
    ("Does not allow working for Colombian companies.", "Ne permet pas de travailler pour des entreprises colombiennes."),
    ("For retirees with proven pension of at least", "Pour les retraités avec une pension prouvée d'au moins"),
    ("2-year visa, renewable. Includes right to work.", "Visa de 2 ans, renouvelable. Inclut le droit de travailler."),
    ("For various categories: employee, investor, real estate owner", "Pour différentes catégories : employé, investisseur, propriétaire immobilier"),
    ("2-year renewable.", "Renouvelable 2 ans."),
    ("Permanent residency after 5 continuous years on M Visa, or via marriage to Colombian national. Renewable every 5 years.",
     "Résidence permanente après 5 années continues avec un visa M, ou par mariage avec un ressortissant colombien. Renouvelable tous les 5 ans."),
    ("Citizens of most Western countries can enter visa-free for 90 days, extendable to 180 days", "Les citoyens de la plupart des pays occidentaux peuvent entrer sans visa pour 90 jours, extensible à 180 jours"),
    ("Citizens of 95+ countries", "Les citoyens de 95+ pays"),
    ("can stay 365 consecutive days", "peuvent séjourner 365 jours consécutifs"),
    ("No income or investment requirement. The simplest option for digital nomads.", "Pas de condition de revenus ni d'investissement. L'option la plus simple pour les nomades numériques."),

    # Japan visa details
    ("New 6-month visa for remote workers earning", "Nouveau visa de 6 mois pour les travailleurs à distance gagnant"),
    ("Single-entry, extendable for 6 months. Must have health insurance. Cannot work for Japanese companies.",
     "Entrée unique, prolongeable de 6 mois. Assurance santé obligatoire. Ne peut pas travailler pour des entreprises japonaises."),
    ("Points-based system (70+ points). Points for education, income, age, Japanese ability. Allows fast-track to permanent residence (1-3 years vs standard 10).",
     "Système à points (70+ points). Points pour l'éducation, les revenus, l'âge, la maîtrise du japonais. Permet une résidence permanente accélérée (1-3 ans vs 10 ans standard)."),
    ("For IT, engineering and scientific professionals.", "Pour les professionnels de l'informatique, de l'ingénierie et des sciences."),
    ("job offer from Japanese employer.", "offre d'emploi d'un employeur japonais."),
    ("1–5 year renewable permit.", "Permis renouvelable de 1 à 5 ans."),
    ("For specified industries (hospitality, food service, care, construction). No degree required. Up to 5 years.",
     "Pour des industries spécifiques (hôtellerie, restauration, soins, construction). Aucun diplôme requis. Jusqu'à 5 ans."),
    ("For spouses and dependent children of work visa holders or permanent residents. Allows certain types of employment.",
     "Pour les conjoints et enfants à charge des titulaires de visa de travail ou résidents permanents. Permet certains types d'emploi."),
    ("After 10 years continuous residence", "Après 10 ans de résidence continue"),
    ("(or 1-3 years on HSP visa). No work restrictions. Highly desirable.",
     "(ou 1-3 ans avec un visa HSP). Aucune restriction de travail. Très recherché."),

    # UAE visa details
    ("For investors, entrepreneurs, specialised talents and outstanding students.", "Pour les investisseurs, les entrepreneurs, les talents spécialisés et les étudiants exceptionnels."),
    ("Property investment", "Investissement immobilier"),
    ("No employer sponsorship needed. Renewable. Includes family members.", "Pas de parrainage d'employeur nécessaire. Renouvelable. Inclut les membres de la famille."),
    ("For skilled workers, freelancers and investors. Self-sponsored.", "Pour les travailleurs qualifiés, les freelances et les investisseurs. Auto-sponsorisé."),
    ("for skilled employees.", "pour les employés qualifiés."),
    ("Sponsored by employer. Most common route. Employer handles the application. Includes Emirates ID and health card.",
     "Sponsorisé par l'employeur. Voie la plus courante. L'employeur gère la demande. Inclut l'Emirates ID et la carte de santé."),
    ("1-year renewable remote work visa.", "Visa de travail à distance renouvelable d'un an."),
    ("Allows residing in the UAE while working for a foreign company.", "Permet de résider aux EAU tout en travaillant pour une entreprise étrangère."),
    ("For retirees 55+. Must meet one of:", "Pour les retraités de 55 ans et plus. Doit remplir l'une des conditions :"),
    ("real estate worth", "immobilier d'une valeur de"),
    ("financial savings", "épargne financière"),
    ("or", "ou"),

    # Spain visa details
    ("For retirees and those with passive income.", "Pour les retraités et ceux ayant des revenus passifs."),
    ("per additional family member).", "par membre de famille supplémentaire)."),
    ("Cannot work in Spain. 1-year permit, renewable for 2-year periods.",
     "Ne peut pas travailler en Espagne. Permis d'un an, renouvelable par périodes de 2 ans."),
    ("For remote workers with non-Spanish clients.", "Pour les travailleurs à distance avec des clients non espagnols."),
    ("Work permit included.", "Permis de travail inclus."),
    ("1-year permit renewable for 3 years, then long-term residence.", "Permis d'un an renouvelable pour 3 ans, puis résidence longue durée."),
    ("Investment residency:", "Résidence par investissement :"),
    ("No minimum stay requirement. 2-year renewable permit.", "Pas d'exigence de séjour minimum. Permis renouvelable de 2 ans."),
    ("Flat 24% income tax on Spanish-source income for 6 years. For employees relocated to Spain or DNV holders. Apply within 6 months of arrival.",
     "Impôt forfaitaire de 24 % sur les revenus de source espagnole pendant 6 ans. Pour les employés relocalisés en Espagne ou les titulaires de DNV. À demander dans les 6 mois suivant l'arrivée."),
    ("Register at the local Town Hall", "S'inscrire à la mairie locale"),
    ("and obtain a NIE (foreigners tax number). Free, immediate residence rights.",
     "et obtenir un NIE (numéro fiscal pour étrangers). Gratuit, droits de résidence immédiats."),

    # Portugal visa details
    ("For business owners and entrepreneurs.", "Pour les propriétaires d'entreprises et les entrepreneurs."),
    ("business plan and proof of funds. Path to permanent residency.", "plan d'affaires et preuve de fonds. Voie vers la résidence permanente."),
    ("EU/EEA/Swiss citizens register at the local", "Les citoyens UE/EEE/suisses s'inscrivent à la"),
    ("within 3 months. Free, no investment required.", "dans les 3 mois. Gratuit, pas d'investissement requis."),

    # =========================================================================
    # RESIDENCE PROCESS STEPS
    # =========================================================================
    ("Apply online via the Colombian Foreign Ministry visa portal", "Postulez en ligne via le portail des visas du Ministère des Affaires Étrangères colombien"),
    ("Upload all required documents (passport, photos, income proof, criminal record)", "Téléversez tous les documents requis (passeport, photos, preuve de revenus, casier judiciaire)"),
    ("Pay the visa fee", "Payez les frais de visa"),
    ("Receive visa within 15–30 business days", "Recevez votre visa dans les 15 à 30 jours ouvrables"),
    ("Arrive in Colombia and within 15 days register the visa at a", "Arrivez en Colombie et dans les 15 jours enregistrez le visa auprès d'un bureau de"),
    ("Obtain a Cédula de Extranjería (foreigner ID card) at", "Obtenez une Cédula de Extranjería (carte d'identité pour étrangers) auprès de"),
    ("Register with the DIAN (tax authority) to get an RUT (tax ID) if working", "Inscrivez-vous auprès du DIAN (administration fiscale) pour obtenir un RUT (numéro fiscal) si vous travaillez"),

    # Japan process steps
    ("Secure a job offer from a Japanese employer OR qualify for the Digital Nomad Visa",
     "Obtenez une offre d'emploi d'un employeur japonais OU qualifiez-vous pour le visa nomade numérique"),
    ("Employer applies for Certificate of Eligibility (CoE) from the Japan Immigration Services Agency",
     "L'employeur fait la demande du certificat d'éligibilité (CoE) auprès de l'Agence des services d'immigration du Japon"),
    ("Apply for the visa at the Japanese embassy in your country using the CoE",
     "Postulez pour le visa à l'ambassade du Japon dans votre pays en utilisant le CoE"),
    ("Arrive in Japan and register at your ward/municipal office within 14 days",
     "Arrivez au Japon et inscrivez-vous à votre bureau municipal dans les 14 jours"),
    ("Obtain your Residence Card", "Obtenez votre carte de résidence"),
    ("at the airport or municipal office", "à l'aéroport ou au bureau municipal"),
    ("Enrol in National", "Inscrivez-vous à l'assurance"),
    ("at the municipal office", "au bureau municipal"),
    ("Obtain a My Number Card", "Obtenez une carte My Number"),
    ("Japan's national ID", "carte d'identité nationale du Japon"),

    # Spain process steps
    ("Apply for your visa at the Spanish consulate in your country",
     "Postulez pour votre visa au consulat d'Espagne dans votre pays"),
    ("Obtain a NIE", "Obtenez un NIE"),
    ("required for all legal and financial transactions", "requis pour toutes les transactions légales et financières"),
    ("Register on the Padrón (municipal census) at your local Town Hall",
     "Inscrivez-vous au Padrón (recensement municipal) à votre mairie locale"),
    ("Obtain private health insurance (required for NLV)", "Obtenez une assurance santé privée (requise pour le NLV)"),
    ("Apply for TIE", "Demandez la TIE"),
    ("residence card at the", "carte de résidence à la"),
    ("Register with the Seguridad Social if working", "Inscrivez-vous à la Seguridad Social si vous travaillez"),
    ("Consider applying for Beckham Law within 6 months if eligible", "Envisagez de postuler pour la loi Beckham dans les 6 mois si éligible"),

    # Portugal process steps
    ("Apply for the appropriate visa at your local Portuguese consulate",
     "Postulez pour le visa approprié à votre consulat portugais local"),
    ("Open a Portuguese bank account (required for visa purposes)",
     "Ouvrez un compte bancaire portugais (requis pour les demandes de visa)"),
    ("Arrive in Portugal and register your address",
     "Arrivez au Portugal et enregistrez votre adresse"),
    ("Apply for NHR (Non-Habitual Resident) tax status in your first year",
     "Postulez pour le statut fiscal NHR (Résident Non Habituel) dans votre première année"),
    ("it provides a flat 20% income tax rate on Portuguese-source income and 0% on most foreign-source income for 10 years.",
     "il offre un taux d'imposition forfaitaire de 20 % sur les revenus de source portugaise et 0 % sur la plupart des revenus de source étrangère pendant 10 ans."),

    # UAE process steps
    ("Determine your visa category based on your situation", "Déterminez votre catégorie de visa en fonction de votre situation"),
    ("For employment visa: employer initiates the process via Ministry of Human Resources",
     "Pour le visa d'emploi : l'employeur initie le processus via le Ministère des Ressources Humaines"),
    ("Medical fitness test at an approved centre", "Test d'aptitude médicale dans un centre agréé"),
    ("Emirates ID registration (biometrics)", "Enregistrement de l'Emirates ID (biométrie)"),
    ("Obtain residence visa stamp in passport", "Obtenez le tampon de visa de résidence dans le passeport"),
    ("Register tenancy contract on Ejari (Dubai) or Tawtheeq (Abu Dhabi)",
     "Enregistrez le contrat de location sur Ejari (Dubaï) ou Tawtheeq (Abu Dhabi)"),
    ("Open a UAE bank account", "Ouvrez un compte bancaire aux EAU"),
    ("Obtain Dubai Health Authority (DHA) or HAAD (Abu Dhabi) health card",
     "Obtenez la carte de santé de la Dubai Health Authority (DHA) ou HAAD (Abu Dhabi)"),

    # Costa Rica process steps
    ("Hire a Costa Rican immigration lawyer", "Engagez un avocat en immigration costaricien"),
    ("Apostille and notarise all foreign documents; translate to Spanish",
     "Apostillez et notariez tous les documents étrangers ; traduisez en espagnol"),
    ("Submit to DGME", "Soumettez au DGME"),
    ("Receive initial conditional residency within 3-12 months", "Recevez la résidence conditionnelle initiale dans les 3 à 12 mois"),
    ("Receive initial conditional residency within 3–12 months", "Recevez la résidence conditionnelle initiale dans les 3 à 12 mois"),
    ("Enrol in the CAJA (public health system)", "Inscrivez-vous à la CAJA (système de santé public)"),
    ("After 3 years of temporary residency,", "Après 3 ans de résidence temporaire,"),

    # Mexico process steps
    ("Apply at the Mexican consulate in your home country with income/savings proof",
     "Postulez au consulat mexicain dans votre pays d'origine avec une preuve de revenus/épargne"),
    ("Receive entry visa (valid 180 days to complete the process in Mexico)",
     "Recevez votre visa d'entrée (valable 180 jours pour compléter le processus au Mexique)"),
    ("Travel to Mexico and within 30 days visit the INM", "Rendez-vous au Mexique et dans les 30 jours visitez l'INM"),
    ("Receive your Tarjeta de Residente (residence card) within 10-15 business days",
     "Recevez votre Tarjeta de Residente (carte de résidence) dans les 10 à 15 jours ouvrables"),
    ("Receive your Tarjeta de Residente (residence card) within 10–15 business days",
     "Recevez votre Tarjeta de Residente (carte de résidence) dans les 10 à 15 jours ouvrables"),

    # Cambodia process steps
    ("Apply for E-Visa online before travel OR obtain visa on arrival",
     "Demandez un E-Visa en ligne avant le voyage OU obtenez un visa à l'arrivée"),
    ("For long-term stay: extend your E-class visa at an immigration agent or the Department of Immigration",
     "Pour un séjour long : prolongez votre visa de classe E auprès d'un agent d'immigration ou du Département de l'Immigration"),
    ("Most expats use an immigration agent", "La plupart des expatriés utilisent un agent d'immigration"),
    ("for 1-year multiple-entry EB extension", "pour une extension EB d'un an à entrées multiples"),
    ("Register your address at the local sangkat (commune) office",
     "Enregistrez votre adresse au bureau du sangkat (commune) local"),
    ("Obtain a Tax Identification Number (TIN) at the General Department of Taxation if working",
     "Obtenez un numéro d'identification fiscale (TIN) auprès de la Direction Générale des Impôts si vous travaillez"),

    # Laos process steps
    ("Register your residence at the local Police station", "Enregistrez votre résidence au poste de police local"),
    ("of arrival (your hotel/guesthouse does this automatically)", "de l'arrivée (votre hôtel/maison d'hôtes le fait automatiquement)"),

    # Vietnam process steps
    ("Upon arrival, register your stay at the local police station or your accommodation does it",
     "À l'arrivée, enregistrez votre séjour au poste de police local ou votre hébergement le fait"),
    ("Up arrival, register your stay at the local police station or your accommodation does it",
     "À l'arrivée, enregistrez votre séjour au poste de police local ou votre hébergement le fait"),

    # Panama process steps
    ("Choose your visa category", "Choisissez votre catégorie de visa"),
    ("for retirees,", "pour les retraités,"),
    ("for qualified nationals", "pour les ressortissants qualifiés"),
    ("Apostille and translate all foreign documents to Spanish",
     "Apostillez et traduisez tous les documents étrangers en espagnol"),

    # Paraguay process steps
    ("Open a Paraguayan bank account and make the $5,500 deposit",
     "Ouvrez un compte bancaire paraguayen et effectuez le dépôt de 5 500 $"),
    ("Apostille all foreign documents and translate to Spanish",
     "Apostillez tous les documents étrangers et traduisez en espagnol"),

    # =========================================================================
    # HEALTH SECTIONS
    # =========================================================================
    # Public health paragraphs
    ("Colombia has a unique dual healthcare system. The EPS (Entidad Promotora de Salud) system",
     "La Colombie a un système de santé double unique. Le système EPS (Entidad Promotora de Salud)"),
    ("provides universal coverage to all legal residents. Foreigners with a Cédula de Extranjería can enrol in EPS for",
     "fournit une couverture universelle à tous les résidents légaux. Les étrangers avec une Cédula de Extranjería peuvent s'inscrire à l'EPS pour"),
    ("(based on income). Quality varies enormously by city and provider.",
     "(selon les revenus). La qualité varie énormément selon la ville et le prestataire."),
    ("Colombia also has excellent private hospitals that are much cheaper than US/European equivalents.",
     "La Colombie possède également d'excellents hôpitaux privés beaucoup moins chers que les équivalents américains/européens."),
    ("is a world-renowned medical tourism destination:", "est une destination de tourisme médical de renommée mondiale :"),
    ("Dental and cosmetic surgery are 60-80% cheaper than in the US.", "La chirurgie dentaire et esthétique est 60-80 % moins chère qu'aux États-Unis."),
    ("Dental and cosmetic surgery are 60–80% cheaper than in the US.", "La chirurgie dentaire et esthétique est 60-80 % moins chère qu'aux États-Unis."),
    # Costa Rica health
    ("Costa Rica's CAJA (Caja Costarricense de Seguro Social) is widely regarded as one of the best",
     "La CAJA du Costa Rica (Caja Costarricense de Seguro Social) est largement considérée comme l'un des meilleurs"),
    ("All legal residents must enrol and pay monthly contributions", "Tous les résidents légaux doivent s'inscrire et payer des cotisations mensuelles"),
    ("Covers doctor visits, hospitalisation, surgery,", "Couvre les consultations médicales, l'hospitalisation, la chirurgie,"),
    ("and prescription medicines.", "et les médicaments sur ordonnance."),
    ("Private clinics and hospitals operate alongside the public system.",
     "Les cliniques et hôpitaux privés fonctionnent en parallèle du système public."),
    ("offer English-speaking doctors and US-comparable standards at 40-60% lower costs.",
     "proposent des médecins anglophones et des standards comparables aux États-Unis à des coûts 40-60 % inférieurs."),
    ("offer English-speaking doctors and US-comparable standards at 40–60% lower costs.",
     "proposent des médecins anglophones et des standards comparables aux États-Unis à des coûts 40-60 % inférieurs."),
    # Japan health
    ("Japan has a universal health insurance system. All residents (including foreigners with a Residence Card) must enrol in either National",
     "Le Japon dispose d'un système d'assurance maladie universelle. Tous les résidents (y compris les étrangers avec une carte de résidence) doivent s'inscrire soit à l'assurance nationale"),
    ("for self-employed/unemployed, or company health insurance", "pour les travailleurs indépendants/sans emploi, soit à l'assurance santé d'entreprise"),
    ("for employees. Patients pay 30% of medical costs; the insurance covers 70%.",
     "pour les employés. Les patients paient 30 % des frais médicaux ; l'assurance couvre 70 %."),
    ("Japan's public hospitals are excellent — among the best in the world. Private clinics are common for routine care. International clinics in Tokyo",
     "Les hôpitaux publics japonais sont excellents — parmi les meilleurs au monde. Les cliniques privées sont courantes pour les soins courants. Les cliniques internationales à Tokyo"),
    ("offer English-language services.", "offrent des services en anglais."),
    # Laos health
    ("Laos's public health system is among the least developed in Southeast Asia. Public hospitals are severely underfunded and understaffed. Expats should avoid them for anything beyond basic first aid.",
     "Le système de santé public du Laos est parmi les moins développés d'Asie du Sud-Est. Les hôpitaux publics sont gravement sous-financés et en sous-effectif. Les expatriés doivent les éviter pour tout ce qui va au-delà des premiers soins de base."),
    # Malaysia health
    ("Malaysia has an excellent public health system. Government hospitals charge a nominal fee for foreigners",
     "La Malaisie a un excellent système de santé public. Les hôpitaux publics facturent des frais nominaux pour les étrangers"),
    ("per consultation) but waiting times can be long. Non-residents pay more.", "par consultation) mais les temps d'attente peuvent être longs. Les non-résidents paient plus."),
    ("Emergency care is excellent at government hospitals.", "Les soins d'urgence sont excellents dans les hôpitaux publics."),
    ("Private hospitals in Malaysia are among the best in Southeast Asia and significantly cheaper than Singapore equivalents.",
     "Les hôpitaux privés en Malaisie sont parmi les meilleurs d'Asie du Sud-Est et nettement moins chers que les équivalents singapouriens."),
    # Cambodia health
    ("Cambodia's public healthcare system is very limited. Most public hospitals lack basic equipment and medicines. Expats should use private hospitals for all care beyond minor issues.",
     "Le système de santé public du Cambodge est très limité. La plupart des hôpitaux publics manquent d'équipements et de médicaments de base. Les expatriés doivent utiliser les hôpitaux privés pour tous les soins au-delà des problèmes mineurs."),
    ("Private hospitals in Phnom Penh", "Les hôpitaux privés à Phnom Penh"),
    ("provide adequate to good care.", "fournissent des soins adéquats à bons."),
    ("has Royal Angkor International Hospital.", "dispose du Royal Angkor International Hospital."),
    ("For serious conditions, Bangkok is the standard evacuation destination", "Pour les cas graves, Bangkok est la destination d'évacuation standard"),
    ("by plane).", "en avion)."),
    # UAE health
    ("Government hospitals", "Les hôpitaux gouvernementaux"),
    ("are available to UAE residents. Emiratis get free care; expats pay reduced rates. However, most expats prefer private hospitals due to better English service and shorter waiting times.",
     "sont accessibles aux résidents des EAU. Les Émiratis bénéficient de soins gratuits ; les expatriés paient des tarifs réduits. Cependant, la plupart des expatriés préfèrent les hôpitaux privés en raison d'un meilleur service en anglais et de temps d'attente plus courts."),
    ("The UAE has world-class private healthcare.", "Les EAU disposent de soins de santé privés de classe mondiale."),
    ("English is the working language in all major facilities.", "L'anglais est la langue de travail dans tous les grands établissements."),
    # Vietnam health
    ("Public hospitals in Vietnam are overcrowded and language-challenged. Expats generally avoid them for all but emergencies.",
     "Les hôpitaux publics au Vietnam sont surpeuplés et présentent des difficultés linguistiques. Les expatriés les évitent généralement sauf pour les urgences."),
    ("Foreigners registered with a Vietnamese employer can access the public health insurance system.",
     "Les étrangers inscrits auprès d'un employeur vietnamien peuvent accéder au système d'assurance santé publique."),
    ("International private hospitals serve the expat community well in Hanoi and HCMC:",
     "Les hôpitaux privés internationaux servent bien la communauté expatriée à Hanoï et HCMC :"),
    ("Quality is good; costs are moderate.", "La qualité est bonne ; les coûts sont modérés."),
    # Spain health
    ("Spain's public healthcare system (Sistema Nacional de Salud, SNS) is one of the best in the world. Legal residents registered on the Padrón and contributing to Social Security can access it for free.",
     "Le système de santé public espagnol (Sistema Nacional de Salud, SNS) est l'un des meilleurs au monde. Les résidents légaux inscrits au Padrón et cotisant à la Sécurité Sociale y ont accès gratuitement."),
    ("Retired expats with an S1 form from their home country (EU citizens) also qualify.",
     "Les expatriés retraités avec un formulaire S1 de leur pays d'origine (citoyens UE) y ont également droit."),
    ("Private healthcare is excellent and affordable by international standards. Major networks:",
     "Les soins de santé privés sont excellents et abordables par rapport aux standards internationaux. Principaux réseaux :"),
    # Portugal health
    ("Portugal has the SNS", "Le Portugal dispose du SNS"),
    ("a universal public health system. Legal residents with a SNS number can access public healthcare for free or at very low cost",
     "un système de santé public universel. Les résidents légaux avec un numéro SNS peuvent accéder aux soins publics gratuitement ou à très faible coût"),
    ("co-payment for appointments, prescriptions etc.).", "de co-paiement pour les consultations, ordonnances, etc.)."),
    ("Private clinics and hospitals", "Les cliniques et hôpitaux privés"),
    ("offer shorter waiting times and English-speaking doctors. Consultations cost", "offrent des temps d'attente plus courts et des médecins anglophones. Les consultations coûtent"),
    # Paraguay health
    ("Paraguay's public health system (IPS — Instituto de Previsión Social) covers registered workers and their families. Quality is inconsistent — good in Asunción, very limited in rural areas. Emergency handling varies greatly.",
     "Le système de santé public du Paraguay (IPS — Instituto de Previsión Social) couvre les travailleurs inscrits et leurs familles. La qualité est inégale — bonne à Asunción, très limitée dans les zones rurales. La prise en charge des urgences varie considérablement."),
    ("Private hospitals in Asunción provide the best care:", "Les hôpitaux privés à Asunción fournissent les meilleurs soins :"),
    ("Quality is acceptable for routine and moderate care, but complex procedures may require",
     "La qualité est acceptable pour les soins courants et modérés, mais les procédures complexes peuvent nécessiter"),
    ("travel to Brazil, Argentina or the US.", "un déplacement au Brésil, en Argentine ou aux États-Unis."),
    ("Most expats use private healthcare in Asunción and maintain international health insurance for serious conditions requiring treatment in Brazil, Argentina or the US.",
     "La plupart des expatriés utilisent les soins de santé privés à Asunción et maintiennent une assurance santé internationale pour les conditions graves nécessitant un traitement au Brésil, en Argentine ou aux États-Unis."),
    # Panama health
    ("Panama has a two-tier public system: Social Security (CSS) for formal workers and public hospitals (MINSA) for the general population.",
     "Le Panama a un système public à deux niveaux : Sécurité Sociale (CSS) pour les travailleurs formels et hôpitaux publics (MINSA) pour la population générale."),
    ("Pensionado visa holders can access CSS at discounted rates.", "Les titulaires du visa Pensionado peuvent accéder au CSS à tarifs réduits."),
    ("Quality in public hospitals varies significantly; Panama City and David have the best facilities.",
     "La qualité dans les hôpitaux publics varie considérablement ; Panama City et David ont les meilleures installations."),
    ("Panama City has excellent private hospitals:", "Panama City a d'excellents hôpitaux privés :"),
    ("affiliated with Johns Hopkins", "affilié à Johns Hopkins"),
    ("English-speaking doctors are common in private care.", "Les médecins anglophones sont courants dans les soins privés."),
    # Mexico health
    ("Private healthcare in Mexico is significantly cheaper than in the US, with high quality in major cities.",
     "Les soins de santé privés au Mexique sont nettement moins chers qu'aux États-Unis, avec une haute qualité dans les grandes villes."),
    ("Most expats opt for private international health insurance rather than IMSS. IMSS is a good supplement for routine care, but private insurance is essential for hospitalisation.",
     "La plupart des expatriés optent pour une assurance santé internationale privée plutôt que l'IMSS. L'IMSS est un bon complément pour les soins courants, mais l'assurance privée est indispensable pour l'hospitalisation."),

    # =========================================================================
    # RECOMMANDE / CONSEIL PRO BOXES
    # =========================================================================
    ("Enrol in EPS for routine and emergency care. Add a supplementary private plan or use top private hospitals (prepago plan) for specialist care and English-language service.",
     "Inscrivez-vous à l'EPS pour les soins courants et d'urgence. Ajoutez un plan privé complémentaire ou utilisez les meilleurs hôpitaux privés (plan prepago) pour les soins spécialisés et le service en anglais."),
    ("Enrol in CAJA immediately — it's", "Inscrivez-vous immédiatement à la CAJA — c'est"),
    ("and provides comprehensive coverage for a modest monthly fee. Add a private", "et fournit une couverture complète pour des frais mensuels modestes. Ajoutez un plan privé"),
    ("plan for faster access to specialists and English-speaking doctors.",
     "pour un accès plus rapide aux spécialistes et aux médecins anglophones."),
    ("Enrol in the public health insurance system immediately upon registering your residence — it is",
     "Inscrivez-vous au système d'assurance santé public immédiatement après l'enregistrement de votre résidence — c'est"),
    ("and provides excellent value. You will also need a high-limit cost cap — Japan's system caps out-of-pocket costs at",
     "et offre un excellent rapport qualité-prix. Vous aurez également besoin d'un plafond de coûts — le système japonais plafonne les frais à votre charge à"),
    ("for average earners.", "pour les revenus moyens."),
    ("Health insurance is MANDATORY in Dubai (all residents and employers must have coverage) and in Abu Dhabi. Employer-sponsored health insurance is standard. Self-employed residents must arrange their own.",
     "L'assurance santé est OBLIGATOIRE à Dubaï (tous les résidents et employeurs doivent avoir une couverture) et à Abu Dhabi. L'assurance santé sponsorisée par l'employeur est standard. Les résidents travailleurs indépendants doivent organiser la leur."),
    ("For NLV applicants: private health insurance with at least", "Pour les candidats au NLV : une assurance santé privée d'au moins"),
    ("coverage is required for the visa. Even after obtaining residency, many expats keep private insurance for faster service.",
     "de couverture est requise pour le visa. Même après l'obtention de la résidence, de nombreux expatriés conservent une assurance privée pour un service plus rapide."),
    ("Register at your local health centre (Centro de Saúde) within the first months to get a SNS user number.",
     "Inscrivez-vous à votre centre de santé local (Centro de Saúde) dans les premiers mois pour obtenir un numéro d'utilisateur SNS."),
    ("This gives access to the full public health system.", "Cela donne accès à l'ensemble du système de santé public."),
    ("As with Laos, medical evacuation insurance is essential in Cambodia. For anything beyond routine care, Bangkok's Bumrungrad or Samitivej hospitals are the standard destination.",
     "Comme pour le Laos, l'assurance évacuation médicale est indispensable au Cambodge. Pour tout ce qui va au-delà des soins courants, les hôpitaux Bumrungrad ou Samitivej de Bangkok sont la destination standard."),

    # =========================================================================
    # INSURANCE SECTIONS
    # =========================================================================
    # Insurance intro paragraphs
    ("While EPS provides solid basic coverage, wait times for specialists and certain services can be long. A supplementary private plan (medicina prepagada) gives immediate access to private hospitals and specialists.",
     "Bien que l'EPS fournisse une couverture de base solide, les temps d'attente pour les spécialistes et certains services peuvent être longs. Un plan privé complémentaire (medicina prepagada) donne un accès immédiat aux hôpitaux et spécialistes privés."),
    ("While the CAJA public system is comprehensive, wait times for non-emergency", "Bien que le système public CAJA soit complet, les temps d'attente pour les"),
    ("and some procedures can be long. Supplementary private insurance provides immediate access to private hospitals and is also useful for the period before CAJA enrolment is active.",
     "non urgents et certaines procédures peuvent être longs. L'assurance privée complémentaire fournit un accès immédiat aux hôpitaux privés et est également utile pour la période avant que l'inscription à la CAJA soit active."),
    ("Because Japan's National Health Insurance already covers 70% of medical costs, supplementary insurance is less critical than in other countries. However, international health insurance is useful for the period before NHI enrolment, for English-language hospitals, and for coverage during international travel.",
     "Comme l'assurance nationale santé du Japon couvre déjà 70 % des frais médicaux, l'assurance complémentaire est moins critique que dans d'autres pays. Cependant, l'assurance santé internationale est utile pour la période avant l'inscription au NHI, pour les hôpitaux anglophones et pour la couverture lors des voyages internationaux."),
    ("International health insurance is not required for any visa category in Cambodia but is essential for safety. The combination of limited local facilities and proximity to excellent Thai hospitals makes evacuation coverage critical.",
     "L'assurance santé internationale n'est requise pour aucune catégorie de visa au Cambodge mais est indispensable pour la sécurité. La combinaison d'installations locales limitées et de la proximité d'excellents hôpitaux thaïlandais rend la couverture d'évacuation critique."),
    ("Given the very limited local healthcare infrastructure, international health insurance with medical evacuation coverage is not optional — it is a necessity for any expat in Laos. Evacuation to Thailand (Bangkok or Udon Thani) is the standard for serious conditions.",
     "Étant donné l'infrastructure de santé locale très limitée, l'assurance santé internationale avec couverture d'évacuation médicale n'est pas optionnelle — c'est une nécessité pour tout expatrié au Laos. L'évacuation vers la Thaïlande (Bangkok ou Udon Thani) est la norme pour les conditions graves."),
    ("Health insurance is legally mandatory for all residents in Dubai and Abu Dhabi. In Dubai, employers with 100+ employees must provide Essential Benefits Plan (EBP) or above. Self-employed residents must purchase their own.",
     "L'assurance santé est légalement obligatoire pour tous les résidents à Dubaï et Abu Dhabi. À Dubaï, les employeurs de 100+ employés doivent fournir le plan Essential Benefits (EBP) ou supérieur. Les résidents travailleurs indépendants doivent souscrire leur propre assurance."),
    ("The minimum plan (Essential Benefits Plan) costs", "Le plan minimum (Essential Benefits Plan) coûte"),
    ("Private health insurance is mandatory for Non-Lucrative and Digital Nomad visa applications. Even for residents with access to the public system, private coverage provides faster appointments and English-speaking doctors.",
     "L'assurance santé privée est obligatoire pour les demandes de visa Non Lucratif et Nomade Numérique. Même pour les résidents ayant accès au système public, la couverture privée offre des rendez-vous plus rapides et des médecins anglophones."),
    ("Although the public health system is excellent for residents, wait times can be long for non-urgent care. A supplementary private health insurance plan gives faster access to private hospitals and specialists.",
     "Bien que le système de santé public soit excellent pour les résidents, les temps d'attente peuvent être longs pour les soins non urgents. Un plan d'assurance santé privée complémentaire donne un accès plus rapide aux hôpitaux et spécialistes privés."),
    ("Private health insurance is not legally required in Mexico but is strongly recommended. Emergency medical costs and hospitalisation at private facilities can be very high without coverage. US expats not covered by Medicare abroad should definitely get private coverage.",
     "L'assurance santé privée n'est pas légalement requise au Mexique mais est fortement recommandée. Les frais médicaux d'urgence et l'hospitalisation dans les établissements privés peuvent être très élevés sans couverture. Les expatriés américains non couverts par Medicare à l'étranger devraient absolument souscrire une couverture privée."),
    ("Health insurance is not legally required for residency in Panama but is strongly recommended. Hospitalisation and specialist care at private hospitals can be expensive without coverage. Pensionado holders receive 20% discounts on healthcare services.",
     "L'assurance santé n'est pas légalement requise pour la résidence au Panama mais est fortement recommandée. L'hospitalisation et les soins spécialisés dans les hôpitaux privés peuvent être coûteux sans couverture. Les titulaires du Pensionado bénéficient de 20 % de réduction sur les services de santé."),
    ("Health insurance is not legally required for most expat visa categories in Vietnam, but it is essential. Medical evacuation from Vietnam to Singapore or Thailand for serious cases can cost $20,000+.",
     "L'assurance santé n'est pas légalement requise pour la plupart des catégories de visa expatriés au Vietnam, mais elle est indispensable. L'évacuation médicale du Vietnam vers Singapour ou la Thaïlande pour les cas graves peut coûter 20 000 $+."),
    ("MM2H requires Malaysian health insurance coverage. Beyond the visa requirement, private insurance is strongly recommended to cover hospitalisation, specialist care and medical evacuation.",
     "Le MM2H exige une couverture d'assurance santé malaisienne. Au-delà de l'exigence du visa, l'assurance privée est fortement recommandée pour couvrir l'hospitalisation, les soins spécialisés et l'évacuation médicale."),

    # Insurance provider descriptions
    ("Japan's largest private insurer. Cancer and hospitalisation riders. For Japanese-speakers primarily.",
     "Le plus grand assureur privé du Japon. Options cancer et hospitalisation. Principalement pour les japonophones."),
    ("Popular cancer and medical indemnity plans. Useful as a supplement to NHI. English support available.",
     "Plans populaires d'indemnisation cancer et médicale. Utile en complément du NHI. Support en anglais disponible."),
    ("International plans for expats. Good English support.", "Plans internationaux pour les expatriés. Bon support en anglais."),
    ("International plan, ideal for new arrivals. Worldwide coverage.", "Plan international, idéal pour les nouveaux arrivants. Couverture mondiale."),
    ("Colombia's most prestigious private health insurer. Full access to", "L'assureur santé privé le plus prestigieux de Colombie. Accès complet à"),
    ("EPS + private plan combined.", "EPS + plan privé combiné."),
    ("good app, strong emergency coverage.", "bonne application, solide couverture d'urgence."),
    ("International plan for expats needing US or European coverage.", "Plan international pour les expatriés nécessitant une couverture américaine ou européenne."),
    ("International plan with Latin America coverage. Good for frequent travellers.", "Plan international avec couverture Amérique latine. Idéal pour les voyageurs fréquents."),
    ("Abu Dhabi's official mandatory insurer. All Abu Dhabi residents must be covered by Daman as primary insurer.",
     "L'assureur obligatoire officiel d'Abu Dhabi. Tous les résidents d'Abu Dhabi doivent être couverts par Daman comme assureur principal."),
    ("Wide network, strong in Dubai. Good for employer group plans.", "Large réseau, fort à Dubaï. Bon pour les plans de groupe employeur."),
    ("Regional leader. Strong hospital network.", "Leader régional. Solide réseau hospitalier."),
    ("Spain's largest private insurer (owned by Bupa). Excellent network, English-language service, strong app. Accepted for NLV.",
     "Le plus grand assureur privé d'Espagne (propriété de Bupa). Excellent réseau, service en anglais, application solide. Accepté pour le NLV."),
    ("Broad network across Spain. Dental plans available. Popular with expats.", "Large réseau dans toute l'Espagne. Plans dentaires disponibles. Populaire auprès des expatriés."),
    ("Strong in Madrid and Catalonia. Good value plans.", "Fort à Madrid et en Catalogne. Plans bon rapport qualité-prix."),
    ("International plan, ideal for new arrivals.", "Plan international, idéal pour les nouveaux arrivants."),
    ("Local AXA plans with solid network. Dental add-on available.", "Plans AXA locaux avec un solide réseau. Option dentaire disponible."),
    ("Portugal's largest private health insurer.", "Le plus grand assureur santé privé du Portugal."),
    ("of private hospitals and clinics. Plans", "d'hôpitaux et de cliniques privés. Plans"),
    ("State insurer. Mandatory for car insurance; also offers health plans.", "Assureur d'État. Obligatoire pour l'assurance auto ; offre également des plans santé."),
    ("Private complementary plans. Strong hospital network.", "Plans complémentaires privés. Solide réseau hospitalier."),
    ("International plan for new arrivals and frequent travellers.", "Plan international pour les nouveaux arrivants et les voyageurs fréquents."),
    ("Comprehensive worldwide coverage.", "Couverture mondiale complète."),
    ("those splitting time between CR and home country.", "ceux qui partagent leur temps entre le CR et leur pays d'origine."),
    ("Premium plan with repatriation coverage.", "Plan premium avec couverture de rapatriement."),
    ("US citizens.", "les citoyens américains."),
    ("Local expat-focused insurer. Good network of Phnom Penh private hospitals.", "Assureur local axé sur les expatriés. Bon réseau d'hôpitaux privés à Phnom Penh."),
    ("Strong medical evacuation and Thailand coverage.", "Solide couverture d'évacuation médicale et de la Thaïlande."),
    ("International plan with broad coverage. Good for frequent travellers.", "Plan international avec large couverture. Idéal pour les voyageurs fréquents."),
    ("Comprehensive worldwide plan with repatriation.", "Plan mondial complet avec rapatriement."),
    ("Budget nomad insurance. Covers evacuation. Popular in the expat community.", "Assurance nomade économique. Couvre l'évacuation. Populaire dans la communauté expatriée."),
    ("Highly recommended for Laos. Strong medical evacuation coverage.", "Fortement recommandé pour le Laos. Solide couverture d'évacuation médicale."),
    ("International plan with excellent evacuation and Thailand coverage.", "Plan international avec excellente couverture d'évacuation et de la Thaïlande."),
    ("Good worldwide plan with medical evacuation.", "Bon plan mondial avec évacuation médicale."),
    ("Good for short-term stays. Strong emergency and evacuation coverage.", "Bon pour les séjours courts. Solide couverture d'urgence et d'évacuation."),
    ("Strong private hospital network.", "Solide réseau d'hôpitaux privés."),
    ("International coverage option available.", "Option de couverture internationale disponible."),
    ("Good range of health plans. Widely accepted at private hospitals.", "Bonne gamme de plans santé. Largement accepté dans les hôpitaux privés."),
    ("Good international coverage.", "Bonne couverture internationale."),
    ("US and Canadian expats.", "les expatriés américains et canadiens."),
    ("International plans with worldwide coverage including the US — essential if you travel north frequently.",
     "Plans internationaux avec couverture mondiale incluant les États-Unis — indispensable si vous voyagez fréquemment vers le nord."),

    # =========================================================================
    # BANK SECTIONS
    # =========================================================================
    # Bank intro paragraphs
    ("A Costa Rican bank account is needed to pay rent, utilities and CAJA contributions, and to receive local salary or pension transfers. The process has become more regulated but remains manageable.",
     "Un compte bancaire costaricien est nécessaire pour payer le loyer, les services publics et les cotisations CAJA, et pour recevoir les transferts de salaire ou de pension locaux. Le processus est devenu plus réglementé mais reste gérable."),
    ("A Japanese bank account is essential for receiving salary, paying rent, utilities and taxes. It has historically been difficult for new arrivals, but the process has improved significantly.",
     "Un compte bancaire japonais est indispensable pour recevoir son salaire, payer le loyer, les services publics et les impôts. Cela a historiquement été difficile pour les nouveaux arrivants, mais le processus s'est considérablement amélioré."),
    ("A UAE bank account is essential for receiving salary, paying rent (often via post-dated cheques in Dubai), utility bills and daily transactions. The process requires Emirates ID.",
     "Un compte bancaire aux EAU est indispensable pour recevoir son salaire, payer le loyer (souvent par chèques postdatés à Dubaï), les factures et les transactions quotidiennes. Le processus nécessite l'Emirates ID."),
    ("A Colombian bank account simplifies daily life — rent payments, utility bills, salary receipt and online shopping. The process requires a Cédula de Extranjería (foreigner ID).",
     "Un compte bancaire colombien simplifie la vie quotidienne — paiement du loyer, factures, réception du salaire et achats en ligne. Le processus nécessite une Cédula de Extranjería (carte d'identité pour étrangers)."),
    ("Cambodia's fully dollarised economy makes banking straightforward — USD accounts are the norm. Account opening is relatively easy for foreigners, even on tourist visa at some banks.",
     "L'économie entièrement dollarisée du Cambodge simplifie les opérations bancaires — les comptes en USD sont la norme. L'ouverture de compte est relativement facile pour les étrangers, même avec un visa touristique dans certaines banques."),
    ("A Lao bank account is useful for receiving salary in Laos and paying local expenses. The process is straightforward but limited digital banking is available. Many expats use Thai bank accounts for their main savings.",
     "Un compte bancaire laotien est utile pour recevoir un salaire au Laos et payer les dépenses locales. Le processus est simple mais les services bancaires numériques sont limités. De nombreux expatriés utilisent des comptes bancaires thaïlandais pour leur épargne principale."),
    ("A Malaysian bank account is needed for the MM2H fixed deposit requirement and for daily expenses. The process is straightforward for visa holders.",
     "Un compte bancaire malaisien est nécessaire pour l'exigence de dépôt fixe MM2H et pour les dépenses quotidiennes. Le processus est simple pour les titulaires de visa."),
    ("A Portuguese bank account is required for the D7 and D8 visa applications, and essential for receiving transfers, paying rent, utilities and taxes.",
     "Un compte bancaire portugais est requis pour les demandes de visa D7 et D8, et indispensable pour recevoir des transferts, payer le loyer, les services publics et les impôts."),
    ("A Paraguayan bank account is required for the residency deposit ($5,500) and for daily transactions. The process is relatively straightforward compared to other Latin American countries.",
     "Un compte bancaire paraguayen est requis pour le dépôt de résidence (5 500 $) et pour les transactions quotidiennes. Le processus est relativement simple comparé aux autres pays d'Amérique latine."),
    ("Panama is a major banking hub in Latin America. However, post-FATCA compliance has made account opening stricter, especially for US citizens. A Panamanian bank account is essential for visa purposes and daily life.",
     "Le Panama est un centre bancaire majeur en Amérique latine. Cependant, la conformité post-FATCA a rendu l'ouverture de compte plus stricte, notamment pour les citoyens américains. Un compte bancaire panaméen est indispensable pour les demandes de visa et la vie quotidienne."),
    ("A Vietnamese bank account simplifies daily life — cheaper rent payments,", "Un compte bancaire vietnamien simplifie la vie quotidienne — paiements de loyer moins chers,"),
    ("local transfers and receiving salary. The process has become easier for foreigners holding TRCs.",
     "transferts locaux et réception du salaire. Le processus est devenu plus facile pour les étrangers titulaires de TRC."),

    # Bank descriptions
    ("Colombia's largest bank. Most expat-friendly with English app. Extensive ATM network. Good online banking.",
     "La plus grande banque de Colombie. La plus accueillante pour les expatriés avec application en anglais. Vaste réseau de distributeurs. Bonne banque en ligne."),
    ("Second-largest bank. Strong in", "Deuxième plus grande banque. Forte à"),
    ("and main cities.", "et dans les principales villes."),
    ("Good mobile app. Popular with young expats and digital nomads.", "Bonne application mobile. Populaire auprès des jeunes expatriés et des nomades numériques."),
    ("Digital wallet/account. Instant opening with cédula. No fees. Good for daily transactions but not full banking.",
     "Portefeuille/compte numérique. Ouverture instantanée avec cédula. Sans frais. Bon pour les transactions quotidiennes mais pas un service bancaire complet."),
    ("Digital bank. Very easy to open. No fees, great app. Growing rapidly in Colombia.",
     "Banque numérique. Très facile à ouvrir. Sans frais, excellente application. En pleine croissance en Colombie."),
    ("Easiest bank to open for foreigners. Accepts residence cards from 6 months after arrival. No minimum balance. Largest ATM network in Japan.",
     "Banque la plus facile à ouvrir pour les étrangers. Accepte les cartes de résidence à partir de 6 mois après l'arrivée. Pas de solde minimum. Plus grand réseau de distributeurs au Japon."),
    ("Largest megabank. Good international wire capabilities. English online banking available.",
     "Plus grande méga-banque. Bonnes capacités de virement international. Banque en ligne en anglais disponible."),
    ("Online bank with the best FX rates in Japan. Excellent English interface. Requires Residence Card. Popular with expats.",
     "Banque en ligne avec les meilleurs taux de change au Japon. Excellente interface en anglais. Nécessite une carte de résidence. Populaire auprès des expatriés."),
    ("English-language internet banking. No ATM fees at 7-Eleven. Good for international transfers.",
     "Banque en ligne en anglais. Pas de frais de retrait au 7-Eleven. Bon pour les transferts internationaux."),
    ("Not a full bank but widely used by expats for international transfers and multi-currency transactions.",
     "Pas une banque complète mais largement utilisé par les expatriés pour les transferts internationaux et les transactions multidevises."),
    ("UAE's largest bank. Good English service, strong online banking, extensive ATM network.",
     "La plus grande banque des EAU. Bon service en anglais, solide banque en ligne, vaste réseau de distributeurs."),
    ("Best for Abu Dhabi residents. Good international transfer rates.", "Idéal pour les résidents d'Abu Dhabi. Bons taux de transfert international."),
    ("Best for international wire transfers and expats with global banking needs. High minimum balance",
     "Idéal pour les virements internationaux et les expatriés avec des besoins bancaires globaux. Solde minimum élevé"),
    ("for some accounts).", "pour certains comptes)."),
    ("Fastest account opening (sometimes same day). Strong digital banking. Neo account with no minimum balance.",
     "Ouverture de compte la plus rapide (parfois le jour même). Solide banque numérique. Compte Neo sans solde minimum."),
    ("New digital bank. Instant account opening with Emirates ID. No fees. Popular with freelancers and nomads.",
     "Nouvelle banque numérique. Ouverture de compte instantanée avec Emirates ID. Sans frais. Populaire auprès des freelances et des nomades."),
    ("Cambodia's most popular bank among expats. Excellent English app, ABA PAY digital payments, easy account opening. Most recommended.",
     "La banque la plus populaire du Cambodge parmi les expatriés. Excellente application en anglais, paiements numériques ABA PAY, ouverture de compte facile. La plus recommandée."),
    ("Good for business accounts and larger transactions. English service available.",
     "Bon pour les comptes professionnels et les transactions importantes. Service en anglais disponible."),
    ("Good for transfers within Cambodia and to Vietnam/Laos.", "Bon pour les transferts au Cambodge et vers le Vietnam/Laos."),
    ("State bank. Good for USD transfers. Strong relationship with Chinese banks.",
     "Banque d'État. Bon pour les transferts en USD. Solide relation avec les banques chinoises."),
    ("Mobile money service (not a full bank) used for daily transactions. Very popular.",
     "Service de monnaie mobile (pas une banque complète) utilisé pour les transactions quotidiennes. Très populaire."),
    ("Largest state bank. Lowest fees. Extensive branch network throughout the country.",
     "Plus grande banque d'État. Frais les plus bas. Vaste réseau d'agences dans tout le pays."),
    ("Best digital banking.", "Meilleure banque numérique."),
    ("Requires DIMEX card.", "Nécessite la carte DIMEX."),
    ("Canadian bank, familiar to North American expats. International wire capabilities.",
     "Banque canadienne, familière des expatriés nord-américains. Capacités de virement international."),
    ("Good for higher-net-worth expats and investors. English-speaking staff.",
     "Bon pour les expatriés fortunés et les investisseurs. Personnel anglophone."),
    ("Thai bank with branches in Vientiane. Excellent for transfers to Thailand.",
     "Banque thaïlandaise avec des agences à Vientiane. Excellente pour les transferts vers la Thaïlande."),
    ("Paraguay's largest private bank. Good English support. Recommended for residency applications.",
     "La plus grande banque privée du Paraguay. Bon support en anglais. Recommandée pour les demandes de résidence."),
    ("Good for account opening. Accepts foreigners with passport only at some branches.",
     "Bon pour l'ouverture de compte. Accepte les étrangers avec passeport uniquement dans certaines agences."),
    ("International bank. Good for wire transfers to/from Spain and Latin America.",
     "Banque internationale. Bon pour les virements vers/depuis l'Espagne et l'Amérique latine."),
    ("State bank. Most accessible but limited digital services.",
     "Banque d'État. La plus accessible mais services numériques limités."),
    ("Vietnam's largest and most internationally connected bank. Good SWIFT network.",
     "La plus grande banque du Vietnam et la plus connectée internationalement. Bon réseau SWIFT."),
    ("Best option for international transfers. English service.", "Meilleure option pour les transferts internationaux. Service en anglais."),
    ("Requires minimum balance.", "Nécessite un solde minimum."),
    ("Major bank, strong digital platform. Easy account opening with NIE.",
     "Grande banque, solide plateforme numérique. Ouverture de compte facile avec NIE."),
    ("Usable while awaiting NIE but not accepted for visa applications. Good for initial period.",
     "Utilisable en attendant le NIE mais non accepté pour les demandes de visa. Bon pour la période initiale."),
    ("Expat-friendly, good for Friendly Nations visa applicants", "Accueillant pour les expatriés, bon pour les candidats au visa Friendly Nations"),
    ("requires bank balance proof).", "nécessite une preuve de solde bancaire)."),

    # Bank document items
    ("Cédula de Extranjería (foreigner ID card) — mandatory", "Cédula de Extranjería (carte d'identité pour étrangers) — obligatoire"),
    ("Justificatif de domicile (rental contract or utility bill)", "Justificatif de domicile (contrat de location ou facture de services publics)"),
    ("Colombian phone number", "Numéro de téléphone colombien"),
    ("RUT (tax ID) for some account types", "RUT (numéro fiscal) pour certains types de comptes"),
    ("Minimum initial deposit (varies by bank and account type)", "Dépôt initial minimum (varie selon la banque et le type de compte)"),
    ("Residence Card", "Carte de résidence"),
    ("— mandatory", "— obligatoire"),
    ("My Number Card or My Number notification slip", "Carte My Number ou notification My Number"),
    ("Japanese phone number or smartphone", "Numéro de téléphone japonais ou smartphone"),
    ("Cambodian visa (tourist may be accepted at ABA Bank)", "Visa cambodgien (le visa touristique peut être accepté à ABA Bank)"),
    ("Cambodian phone number (for app)", "Numéro de téléphone cambodgien (pour l'application)"),
    ("Visa or TRC (tourist visa may be accepted at BCEL)", "Visa ou TRC (le visa touristique peut être accepté au BCEL)"),
    ("Costa Rican phone number", "Numéro de téléphone costaricien"),
    ("UAE phone number", "Numéro de téléphone émirien"),
    ("Salary certificate or proof of income", "Certificat de salaire ou preuve de revenus"),
    ("Employment contract or trade licence (for freelancers)", "Contrat de travail ou licence commerciale (pour les freelances)"),
    ("valid with UAE visa", "valide avec visa des EAU"),
    ("DIMEX card (for residents) — OR tourist entry for basic account at state banks",
     "Carte DIMEX (pour les résidents) — OU entrée touristique pour un compte de base dans les banques d'État"),
    ("(pension letter, employment contract, bank statements)", "(lettre de pension, contrat de travail, relevés bancaires)"),
    ("Some banks require 6 months of residence before opening", "Certaines banques exigent 6 mois de résidence avant l'ouverture"),
    ("(or residence card address is sufficient)", "(ou l'adresse de la carte de résidence suffit)"),
    ("for some account types)", "pour certains types de comptes)"),
    ("for most account types)", "pour la plupart des types de comptes)"),
    ("Digital banks accepted for day-to-day use but NOT accepted for visa applications. Use as secondary accounts only.",
     "Banques numériques acceptées pour l'usage quotidien mais NON acceptées pour les demandes de visa. À utiliser comme comptes secondaires uniquement."),

    # Bank process steps
    ("Register your address at the ward office and obtain your Residence Card",
     "Enregistrez votre adresse au bureau municipal et obtenez votre carte de résidence"),
    ("Obtain My Number Card (apply at ward office, takes ~1 month)",
     "Obtenez la carte My Number (demande au bureau municipal, prend ~1 mois)"),
    ("Visit Japan Post Bank or apply online at Sony Bank / Shinsei",
     "Rendez-vous à Japan Post Bank ou postulez en ligne à Sony Bank / Shinsei"),
    ("Present Residence Card and My Number", "Présentez votre carte de résidence et votre My Number"),
    ("Receive bankbook and/or debit card within 1-2 weeks", "Recevez votre livret bancaire et/ou carte de débit sous 1 à 2 semaines"),
    ("Receive bankbook and/or debit card within 1–2 weeks", "Recevez votre livret bancaire et/ou carte de débit sous 1 à 2 semaines"),
    ("Obtain your Emirates ID first (issued after residence visa is stamped)",
     "Obtenez d'abord votre Emirates ID (délivré après le tampon du visa de résidence)"),
    ("Book appointment at the bank or apply digitally", "Prenez rendez-vous à la banque ou postulez en ligne"),
    ("Submit all documents", "Soumettez tous les documents"),
    ("Account activated within 1-5 business days", "Compte activé sous 1 à 5 jours ouvrables"),
    ("Account activated within 1–5 business days", "Compte activé sous 1 à 5 jours ouvrables"),
    ("and online banking access", "et accès à la banque en ligne"),
    ("Obtain your Cédula de Extranjería at", "Obtenez votre Cédula de Extranjería auprès de"),
    ("first", "d'abord"),
    ("Visit bank branch or apply digitally", "Rendez-vous à l'agence bancaire ou postulez en ligne"),
    ("Present Cédula and proof of address", "Présentez votre Cédula et justificatif de domicile"),
    ("Account opened same day in most cases", "Compte ouvert le jour même dans la plupart des cas"),
    ("within 5-7 business days", "sous 5 à 7 jours ouvrables"),
    ("within 5–7 business days", "sous 5 à 7 jours ouvrables"),
    ("Visit ABA Bank branch in Phnom Penh or Siem Reap", "Rendez-vous à l'agence ABA Bank à Phnom Penh ou Siem Reap"),
    ("Present passport and visa", "Présentez votre passeport et votre visa"),
    ("Complete account opening form", "Remplissez le formulaire d'ouverture de compte"),
    ("Download ABA Mobile app — one of the best banking apps in Southeast Asia",
     "Téléchargez l'application ABA Mobile — l'une des meilleures applications bancaires d'Asie du Sud-Est"),
    ("For state banks: some accept tourist status for a basic account",
     "Pour les banques d'État : certaines acceptent le statut de touriste pour un compte de base"),
    ("and complete KYC form", "et remplissez le formulaire KYC"),
    ("Account generally opened within 1-5 business days", "Compte généralement ouvert sous 1 à 5 jours ouvrables"),
    ("Account generally opened within 1–5 business days", "Compte généralement ouvert sous 1 à 5 jours ouvrables"),
    ("Present all required documents", "Présentez tous les documents requis"),
    ("For residency deposit: open a fixed-term savings account with $5,500",
     "Pour le dépôt de résidence : ouvrez un compte d'épargne à terme avec 5 500 $"),
    ("Receive account number and access for wire transfers",
     "Recevez votre numéro de compte et l'accès pour les virements"),
    ("Obtain RFC at the SAT office or via the SAT website",
     "Obtenez votre RFC au bureau du SAT ou via le site web du SAT"),
    ("Schedule appointment at bank (walk-in possible but often refused for foreigners)",
     "Prenez rendez-vous à la banque (sans rendez-vous possible mais souvent refusé pour les étrangers)"),

    # =========================================================================
    # REAL ESTATE SECTIONS
    # =========================================================================
    # Real estate intro paragraphs
    ("Costa Rica has no restrictions on foreign property ownership — foreigners have the same rights as citizens. The property market is well-established, with a large inventory of",
     "Le Costa Rica n'a aucune restriction sur la propriété étrangère — les étrangers ont les mêmes droits que les citoyens. Le marché immobilier est bien établi, avec un large inventaire de"),
    ("properties, particularly in the Central Valley, Guanacaste, Manuel Antonio and the Southern Zone.",
     "biens, particulièrement dans la Vallée Centrale, le Guanacaste, Manuel Antonio et la Zone Sud."),
    ("Japan has no restrictions on foreigners buying property — freehold ownership is fully permitted. Japan is unique in that properties (especially houses) can depreciate significantly over time, while land values are more stable. Prices outside Tokyo and major cities are remarkably low.",
     "Le Japon n'a aucune restriction pour les étrangers achetant des biens immobiliers — la pleine propriété est entièrement autorisée. Le Japon est unique en ce que les propriétés (surtout les maisons) peuvent se déprécier considérablement au fil du temps, tandis que les valeurs foncières sont plus stables. Les prix en dehors de Tokyo et des grandes villes sont remarquablement bas."),
    ("Foreigners can freely buy property in Colombia without any restriction. Colombia is one of the most accessible property markets in Latin America for foreigners.",
     "Les étrangers peuvent librement acheter des biens immobiliers en Colombie sans aucune restriction. La Colombie est l'un des marchés immobiliers les plus accessibles d'Amérique latine pour les étrangers."),
    ("has become a hotspot, with", "est devenu un point chaud, avec"),
    ("also very popular.", "également très populaires."),
    ("Foreigners CANNOT own land in Cambodia, but the law was amended in 2010 to allow foreigners to own condominium units on the 2nd floor and above (not ground floor or land). Workarounds include 50-year long-term leases and Cambodian company structures.",
     "Les étrangers NE PEUVENT PAS posséder de terrain au Cambodge, mais la loi a été modifiée en 2010 pour permettre aux étrangers de posséder des unités en copropriété au 2e étage et au-dessus (pas le rez-de-chaussée ni le terrain). Les solutions alternatives incluent les baux à long terme de 50 ans et les structures de société cambodgiennes."),
    ("Foreigners can buy property in Malaysia but with a minimum purchase price restriction.",
     "Les étrangers peuvent acheter des biens immobiliers en Malaisie mais avec une restriction de prix d'achat minimum."),
    ("though some states have higher or lower thresholds.", "bien que certains États aient des seuils plus élevés ou plus bas."),
    ("Foreigners can buy property in Vietnam under the 2014 Housing Law, but with significant restrictions: maximum 30% of apartments in a building, no more than 250 houses in a ward, and ownership is limited to 50 years (renewable once).",
     "Les étrangers peuvent acheter des biens immobiliers au Vietnam en vertu de la loi sur le logement de 2014, mais avec des restrictions importantes : maximum 30 % des appartements dans un immeuble, pas plus de 250 maisons dans un quartier, et la propriété est limitée à 50 ans (renouvelable une fois)."),
    ("Foreigners can own property in Mexico, but with important restrictions in coastal and border zones",
     "Les étrangers peuvent posséder des biens immobiliers au Mexique, mais avec d'importantes restrictions dans les zones côtières et frontalières"),
    ("within 50km of the coast and 100km of a border). These 'restricted zones' require a bank trust (Fideicomiso).",
     "dans un rayon de 50 km de la côte et 100 km d'une frontière). Ces \"zones restreintes\" nécessitent un fidéicommis bancaire (Fideicomiso)."),
    ("Panama has among the most foreigner-friendly property laws in Latin America. Foreigners have the same property rights as Panamanian citizens. No restrictions on type of property, location or amount owned.",
     "Le Panama a l'une des législations immobilières les plus favorables aux étrangers d'Amérique latine. Les étrangers ont les mêmes droits de propriété que les citoyens panaméens. Aucune restriction sur le type de propriété, l'emplacement ou le montant possédé."),
    ("Foreigners can buy property in the UAE in designated freehold zones",
     "Les étrangers peuvent acheter des biens immobiliers aux EAU dans des zones de pleine propriété désignées"),
    ("(Dubai has over 60 freehold areas). Abu Dhabi has more restricted zones. Property purchase can qualify for a Golden Visa",
     "(Dubaï compte plus de 60 zones de pleine propriété). Abu Dhabi a des zones plus restreintes. L'achat immobilier peut qualifier pour un Golden Visa"),

    # Property option descriptions
    ("Full ownership registered at the National Registry. Standard for most urban and suburban properties. Most secure form of ownership.",
     "Pleine propriété enregistrée au Registre National. Standard pour la plupart des propriétés urbaines et suburbaines. Forme de propriété la plus sûre."),
    ("Land within 200m of the ocean. The first 50m from the high tide line is public and inalienable. The next 150m requires a concession from the municipality. Foreigners can hold concessions but must have 5 years legal residency or go through a Costa Rican company.",
     "Terrain à moins de 200 m de l'océan. Les 50 premiers mètres à partir de la ligne de marée haute sont publics et inaliénables. Les 150 m suivants nécessitent une concession de la municipalité. Les étrangers peuvent détenir des concessions mais doivent avoir 5 ans de résidence légale ou passer par une société costaricienne."),
    ("Untitled land. Very risky for foreigners — avoid unless you have expert legal advice.",
     "Terrain sans titre. Très risqué pour les étrangers — à éviter sauf si vous avez des conseils juridiques d'expert."),
    ("Full freehold ownership. Most expats buy condos in Tokyo, Osaka or Kyoto. Popular in international communities.",
     "Pleine propriété. La plupart des expatriés achètent des appartements à Tokyo, Osaka ou Kyoto. Populaire dans les communautés internationales."),
    ("Full ownership of land and structure. Houses depreciate to near-zero after 20-30 years in Japan — land is the main value.",
     "Pleine propriété du terrain et de la structure. Les maisons se déprécient quasiment à zéro après 20-30 ans au Japon — le terrain est la principale valeur."),
    ("Full ownership of land and structure. Houses depreciate to near-zero after 20–30 years in Japan — land is the main value.",
     "Pleine propriété du terrain et de la structure. Les maisons se déprécient quasiment à zéro après 20-30 ans au Japon — le terrain est la principale valeur."),
    ("Vacant properties in rural areas, sometimes available for", "Propriétés vacantes dans les zones rurales, parfois disponibles pour"),
    ("or very low prices. Renovation costs can be high.", "ou à des prix très bas. Les coûts de rénovation peuvent être élevés."),
    ("Foreign ownership permitted from the 2nd floor upward in approved condominium buildings. Growing inventory in Phnom Penh.",
     "Propriété étrangère autorisée à partir du 2e étage dans les immeubles en copropriété approuvés. Inventaire croissant à Phnom Penh."),
    ("also have options.", "ont également des options."),
    ("for 50 years, renewable for another 50. Common for villas and townhouses.",
     "pour 50 ans, renouvelable pour 50 ans supplémentaires. Courant pour les villas et maisons de ville."),
    ("Many foreigners form a Cambodian company (with a Cambodian nominee director holding 51% of shares on paper). Legal but carries risk if done improperly.",
     "De nombreux étrangers créent une société cambodgienne (avec un directeur nominee cambodgien détenant 51 % des parts sur papier). Légal mais comporte des risques si mal fait."),
    ("Land held in a Cambodian spouse's name. Common but risky without legal protections.",
     "Terrain détenu au nom d'un conjoint cambodgien. Courant mais risqué sans protections juridiques."),
    ("Full ownership in designated freehold zones. Available to all nationalities. Most condos and many villas are freehold.",
     "Pleine propriété dans les zones de freehold désignées. Disponible pour toutes les nationalités. La plupart des appartements et de nombreuses villas sont en pleine propriété."),
    ("Available outside freehold zones. Long-term lease but no land ownership.",
     "Disponible hors des zones de freehold. Bail à long terme mais pas de propriété foncière."),
    ("Buying from developers before or during construction.", "Achat auprès de promoteurs avant ou pendant la construction."),
    ("cheaper than ready units. Developer payment plans common", "moins cher que les unités prêtes. Plans de paiement promoteur courants"),
    ("Full ownership, same rights as citizens. Most condos, houses and commercial properties. Registered at the Public Registry.",
     "Pleine propriété, mêmes droits que les citoyens. La plupart des appartements, maisons et biens commerciaux. Enregistré au Registre Public."),
    ("Required in restricted zones (coastal/border). A Mexican bank holds the title for you as beneficiary.",
     "Requis dans les zones restreintes (côtières/frontalières). Une banque mexicaine détient le titre pour vous en tant que bénéficiaire."),
    ("in bank fees. 50-year trust, renewable.", "en frais bancaires. Fidéicommis de 50 ans, renouvelable."),
    ("Foreigners can buy apartments in approved developments. Ownership certificate valid 50 years, renewable once. Most common option.",
     "Les étrangers peuvent acheter des appartements dans des projets approuvés. Certificat de propriété valable 50 ans, renouvelable une fois. Option la plus courante."),
    ("50-year term on the land, with ownership of the structure. Renewable.",
     "Bail de 50 ans sur le terrain, avec propriété de la structure. Renouvelable."),
    ("If you own a Vietnamese company with a local partner, the company can hold land long-term. Risky unless you trust your partner.",
     "Si vous possédez une entreprise vietnamienne avec un partenaire local, l'entreprise peut détenir le terrain à long terme. Risqué à moins de faire confiance à votre partenaire."),
    ("99-year lease on the land. Common for high-rise condominiums. After 99 years, the land reverts to the state.",
     "Bail de 99 ans sur le terrain. Courant pour les condominiums de grande hauteur. Après 99 ans, le terrain revient à l'État."),
    ("Foreigners can own agricultural land. Paraguay has become a major soy and cattle farming country, with expat farmers from Brazil, Germany and Mennonite communities owning large tracts.",
     "Les étrangers peuvent posséder des terres agricoles. Le Paraguay est devenu un grand pays de culture du soja et d'élevage, avec des agriculteurs expatriés du Brésil, d'Allemagne et des communautés mennonites possédant de vastes parcelles."),
    ("Full ownership. No restrictions for foreigners. Standard for all property types.",
     "Pleine propriété. Aucune restriction pour les étrangers. Standard pour tous les types de biens."),
    ("Standard method for all property types.", "Méthode standard pour tous les types de biens."),
    ("Owning property worth", "Posséder un bien d'une valeur de"),
    ("qualifies you for a Migrant Visa (2 years, renewable).", "vous qualifie pour un visa Migrant (2 ans, renouvelable)."),
    ("Common in", "Courant à"),
    ("cheaper than finished properties. Developers offer payment plans during construction.",
     "moins cher que les propriétés finies. Les promoteurs offrent des plans de paiement pendant la construction."),

    # Buying process steps
    ("Hire a Costa Rican real estate lawyer (not optional)", "Engagez un avocat immobilier costaricien (pas optionnel)"),
    ("Obtain an RNPN (National Property Registry) title search", "Obtenez une recherche de titre au RNPN (Registre National de la Propriété)"),
    ("Check for liens, easements, back taxes, survey maps", "Vérifiez les charges, servitudes, arriérés d'impôts, plans cadastraux"),
    ("Sign a Purchase Option contract", "Signez un contrat d'option d'achat"),
    ("Complete due diligence: survey, environmental restrictions, zoning",
     "Effectuez les vérifications préalables : arpentage, restrictions environnementales, zonage"),
    ("Sign Escritura de Compraventa (Purchase Deed) before a Notary Public",
     "Signez l'Escritura de Compraventa (Acte de Vente) devant un Notaire Public"),
    ("the National Registry (Registro Nacional)", "le Registre National (Registro Nacional)"),
    ("Pay transfer taxes and notary fees at closing", "Payez les taxes de transfert et les frais de notaire à la clôture"),
    ("Obtain a long-term residence visa (tourist visa insufficient for mortgage)",
     "Obtenez un visa de résidence longue durée (visa touristique insuffisant pour un prêt hypothécaire)"),
    ("Hire a licensed real estate agent", "Engagez un agent immobilier agréé"),
    ("usually no buyer fee", "généralement pas de frais pour l'acheteur"),
    ("Identify properties via SUUMO, AtHome or an expat-specialist agency",
     "Identifiez les biens via SUUMO, AtHome ou une agence spécialisée expatriés"),
    ("Make an offer and receive the Property Information Document",
     "Faites une offre et recevez le document d'information sur le bien"),
    ("Sign the Purchase Agreement", "Signez le contrat d'achat"),
    ("pay 10% deposit", "versez un acompte de 10 %"),
    ("Arrange mortgage (if applicable) or wire full payment",
     "Organisez le prêt hypothécaire (si applicable) ou virez le paiement intégral"),
    ("Transfer at the notary / legal scrivener", "Transfert chez le notaire / scribe judiciaire"),
    ("title registered in land registry", "titre enregistré au registre foncier"),
    ("Obtain a RUT (Colombian tax ID) at the DIAN — required for property purchase",
     "Obtenez un RUT (numéro fiscal colombien) au DIAN — requis pour l'achat immobilier"),
    ("Hire a Colombian real estate lawyer (abogado)", "Engagez un avocat immobilier colombien (abogado)"),
    ("Sign a Promesa de Compraventa (preliminary agreement) — pay 10-30% deposit",
     "Signez une Promesa de Compraventa (accord préliminaire) — versez un acompte de 10-30 %"),
    ("Sign a Promesa de Compraventa (preliminary agreement) — pay 10–30% deposit",
     "Signez une Promesa de Compraventa (accord préliminaire) — versez un acompte de 10-30 %"),
    ("Lawyer conducts title search at the Public Instruments Registry",
     "L'avocat effectue une recherche de titre au Registre des Instruments Publics"),
    ("Sign the Escritura Pública (deed) before a Notario",
     "Signez l'Escritura Pública (acte) devant un Notario"),
    ("Register at the Public Instruments Registry (Registro de Instrumentos Públicos)",
     "Enregistrez au Registre des Instruments Publics (Registro de Instrumentos Públicos)"),
    ("Pay transfer taxes", "Payez les taxes de transfert"),
    ("Identify property and sign a Memorandum of Understanding (MOU) — pay 10% deposit",
     "Identifiez le bien et signez un protocole d'accord (MOU) — versez un acompte de 10 %"),
    ("Get a No Objection Certificate (NOC) from the developer (if resale)",
     "Obtenez un certificat de non-objection (NOC) du promoteur (si revente)"),
    ("Both parties attend the Dubai Land Department (DLD) for transfer",
     "Les deux parties se rendent au Dubai Land Department (DLD) pour le transfert"),
    ("Pay Transfer Fee (4%) and obtain new title deed",
     "Payez les frais de transfert (4 %) et obtenez le nouveau titre de propriété"),
    ("Register with Ejari if renting out the property",
     "Inscrivez-vous sur Ejari si vous louez le bien"),
    ("Hire a reputable Cambodian real estate lawyer", "Engagez un avocat immobilier cambodgien réputé"),
    ("Verify the title (LMAP Title — the most secure type; avoid Soft Title)",
     "Vérifiez le titre (LMAP Title — le type le plus sûr ; évitez le Soft Title)"),
    ("For condos: check building is registered with MLMUPC as foreigner-eligible",
     "Pour les appartements : vérifiez que l'immeuble est enregistré auprès du MLMUPC comme éligible aux étrangers"),
    ("Sign a Memorandum of Understanding (MOU) and pay deposit",
     "Signez un protocole d'accord (MOU) et versez l'acompte"),
    ("Lawyer conducts due diligence: title, permits, developer reputation",
     "L'avocat effectue les vérifications préalables : titre, permis, réputation du promoteur"),
    ("Sign the Sale and Purchase Agreement (SPA)", "Signez le contrat de vente (SPA)"),
    ("Transfer at the relevant authority and receive your ownership certificate",
     "Transfert auprès de l'autorité compétente et recevez votre certificat de propriété"),
    ("Hire an independent real estate lawyer (separate from the notary)",
     "Engagez un avocat immobilier indépendant (distinct du notaire)"),
    ("the Public Registry of Property (RPP)", "le Registre Public de la Propriété (RPP)"),
    ("Hire a Lao lawyer familiar with foreign investment law",
     "Engagez un avocat laotien familier du droit des investissements étrangers"),
    ("Register the lease at the National Land Management Authority (NLMA)",
     "Enregistrez le bail auprès de l'Autorité Nationale de Gestion Foncière (NLMA)"),
    ("Verify the project is open to foreign ownership (check with developer and local authority)",
     "Vérifiez que le projet est ouvert à la propriété étrangère (vérifiez auprès du promoteur et de l'autorité locale)"),
    ("Sign the Letter of Offer / Booking Form and pay 2-3% deposit",
     "Signez la lettre d'offre / formulaire de réservation et versez un acompte de 2-3 %"),
    ("Sign the Letter of Offer / Booking Form and pay 2–3% deposit",
     "Signez la lettre d'offre / formulaire de réservation et versez un acompte de 2-3 %"),
    ("Obtain a NIF (tax number)", "Obtenez un NIF (numéro fiscal)"),
    ("for property purchase", "pour l'achat immobilier"),
    ("Register property at the Land Registry", "Enregistrez le bien au Registre Foncier"),

    # =========================================================================
    # CONSEIL PRO / TIP BOXES (longer English sentences after French label)
    # =========================================================================
    ("The Digital Nomad Visa is valid for 2 years and is the most popular new route for remote workers. The income requirement of ~$684/month (3× Colombian minimum wage) is very accessible.",
     "Le visa Nomade Numérique est valable 2 ans et est la voie la plus populaire pour les travailleurs à distance. L'exigence de revenu de ~684 $/mois (3× le salaire minimum colombien) est très accessible."),
    ("Colsanitas is considered the gold standard of Colombian private health insurance among expats. The combination of EPS (for routine/emergency) + Colsanitas prepago (for specialists and surgery) offers excellent coverage at a fraction of US costs.",
     "Colsanitas est considéré comme la référence de l'assurance santé privée colombienne parmi les expatriés. La combinaison EPS (pour les soins courants/urgences) + Colsanitas prepago (pour les spécialistes et la chirurgie) offre une excellente couverture pour une fraction des coûts américains."),
    ("Start with Nequi or Nu Colombia (fully digital, instant account) while waiting for your Cédula. Once you have your Cédula, open a Bancolombia account for more complete banking services.",
     "Commencez avec Nequi ou Nu Colombia (entièrement numérique, compte instantané) en attendant votre Cédula. Une fois que vous avez votre Cédula, ouvrez un compte Bancolombia pour des services bancaires plus complets."),
    ("Japan Post Bank is the easiest to open immediately. Sony Bank has the best FX rates and English interface — open it once you've been resident for a few months.",
     "Japan Post Bank est la plus facile à ouvrir immédiatement. Sony Bank a les meilleurs taux de change et une interface en anglais — ouvrez-y un compte une fois que vous êtes résident depuis quelques mois."),
    ("The My Number Card has become increasingly important in Japan — it's needed for taxes, bank accounts, health insurance and government services. Apply for it at your local ward office as soon as possible.",
     "La carte My Number est devenue de plus en plus importante au Japon — elle est nécessaire pour les impôts, les comptes bancaires, l'assurance santé et les services gouvernementaux. Demandez-la à votre bureau municipal dès que possible."),
    ("For most working expats in Japan, the mandatory NHI or company health insurance + a supplementary cancer/hospitalisation plan from a local insurer like Aflac is the most cost-effective setup.",
     "Pour la plupart des expatriés travaillant au Japon, l'assurance NHI obligatoire ou l'assurance santé d'entreprise + un plan cancer/hospitalisation complémentaire d'un assureur local comme Aflac est la configuration la plus rentable."),
    ("In rural Japan, you can buy a fully habitable house for", "Dans le Japon rural, vous pouvez acheter une maison entièrement habitable pour"),
    ("The Akiya Banks", "Les Akiya Banks"),
    ("run by municipalities list vacant properties. The main cost is renovation, not purchase.",
     "gérées par les municipalités répertorient les propriétés vacantes. Le coût principal est la rénovation, pas l'achat."),
    ("The Green Visa is the most flexible option for independent professionals — it allows you to sponsor yourself without a local employer, and you can stay 180 days outside the UAE without losing residency.",
     "Le Green Visa est l'option la plus flexible pour les professionnels indépendants — il vous permet de vous sponsoriser vous-même sans employeur local, et vous pouvez rester 180 jours hors des EAU sans perdre votre résidence."),
    ("In Dubai, even the minimum Essential Benefits Plan (EBP) covers emergency care, maternity and pre-existing conditions. For comprehensive private hospital access and international coverage, upgrade to an enhanced plan.",
     "À Dubaï, même le plan minimum Essential Benefits (EBP) couvre les soins d'urgence, la maternité et les conditions préexistantes. Pour un accès complet aux hôpitaux privés et une couverture internationale, passez à un plan amélioré."),
    ("Mashreq Neo and Wio Bank offer the fastest account opening — sometimes within 24 hours — with no minimum balance. Ideal for new arrivals while waiting for Emirates NBD or HSBC approval.",
     "Mashreq Neo et Wio Bank offrent l'ouverture de compte la plus rapide — parfois dans les 24 heures — sans solde minimum. Idéal pour les nouveaux arrivants en attendant l'approbation d'Emirates NBD ou HSBC."),
    ("Dubai has no annual property tax and no capital gains tax on property — only the 4% transfer fee on purchase. Off-plan properties from developers like Emaar, Damac and Nakheel often come with 0% payment plans stretching 5-8 years.",
     "Dubaï n'a pas de taxe foncière annuelle ni d'impôt sur les plus-values immobilières — seulement les 4 % de frais de transfert à l'achat. Les propriétés sur plan de promoteurs comme Emaar, Damac et Nakheel offrent souvent des plans de paiement à 0 % sur 5 à 8 ans."),
    ("Dubai has no annual property tax and no capital gains tax on property — only the 4% transfer fee on purchase. Off-plan properties from developers like Emaar, Damac and Nakheel often come with 0% payment plans stretching 5–8 years.",
     "Dubaï n'a pas de taxe foncière annuelle ni d'impôt sur les plus-values immobilières — seulement les 4 % de frais de transfert à l'achat. Les propriétés sur plan de promoteurs comme Emaar, Damac et Nakheel offrent souvent des plans de paiement à 0 % sur 5 à 8 ans."),
    ("The Non-Lucrative Visa requires you NOT to work in Spain, but you can receive income from foreign sources (pensions, investments, remote work for non-Spanish companies if done discreetly — grey area). The Digital Nomad Visa is cleaner if you're working remotely.",
     "Le visa Non Lucratif vous interdit de travailler en Espagne, mais vous pouvez recevoir des revenus de sources étrangères (pensions, investissements, travail à distance pour des entreprises non espagnoles si fait discrètement — zone grise). Le visa Nomade Numérique est plus clair si vous travaillez à distance."),
    ("For visa purposes, Sanitas and Adeslas are most commonly accepted by Spanish consulates. Make sure your policy is comprehensive (no exclusions for pre-existing conditions at the consulate stage) and has no co-payments (some consulates require this).",
     "Pour les demandes de visa, Sanitas et Adeslas sont les plus couramment acceptés par les consulats espagnols. Assurez-vous que votre police est complète (pas d'exclusions pour les conditions préexistantes au stade du consulat) et sans co-paiements (certains consulats l'exigent)."),
    ("For D7 visa applications, you need proof of health insurance before arriving. Cigna or AXA Global Healthcare are easiest to obtain from abroad. Once resident, you can switch to a Portuguese plan like Médis or Multicare.",
     "Pour les demandes de visa D7, vous avez besoin d'une preuve d'assurance santé avant d'arriver. Cigna ou AXA Global Healthcare sont les plus faciles à obtenir depuis l'étranger. Une fois résident, vous pouvez passer à un plan portugais comme Médis ou Multicare."),
    ("Ensure your plan explicitly covers medical evacuation to Thailand. Pacific Cross Cambodia is a good local option and is widely accepted at Phnom Penh's private hospitals.",
     "Assurez-vous que votre plan couvre explicitement l'évacuation médicale vers la Thaïlande. Pacific Cross Cambodia est une bonne option locale et est largement accepté dans les hôpitaux privés de Phnom Penh."),
    ("ABA Bank is the unanimous favourite among Phnom Penh expats — the app is excellent, account opening is fast (sometimes with just a tourist visa), and the service is in English.",
     "ABA Bank est le favori unanime des expatriés de Phnom Penh — l'application est excellente, l'ouverture de compte est rapide (parfois même avec un visa touristique), et le service est en anglais."),
    ("Only buy condos in Cambodia — they are the only truly secure form of foreign property ownership under Cambodian law. Leasehold villas and company-held land carry significant legal risk.",
     "N'achetez que des appartements au Cambodge — c'est la seule forme vraiment sûre de propriété étrangère en droit cambodgien. Les villas en bail et les terrains détenus par des sociétés comportent des risques juridiques importants."),
    ("are the most expat-friendly neighbourhoods.", "sont les quartiers les plus accueillants pour les expatriés."),
    ("Your policy MUST include medical evacuation to Thailand. This is the single most important coverage for expats in Laos — verify explicitly that your policy covers helicopter and air ambulance evacuation.",
     "Votre police DOIT inclure l'évacuation médicale vers la Thaïlande. C'est la couverture la plus importante pour les expatriés au Laos — vérifiez explicitement que votre police couvre l'évacuation par hélicoptère et avion ambulance."),
    ("Long-term leases in Laos are common and legally well-established for foreigners. The key risk is title — ensure the land has a proper Title Certificate (not just occupancy rights) before signing any lease agreement.",
     "Les baux à long terme au Laos sont courants et juridiquement bien établis pour les étrangers. Le risque principal est le titre — assurez-vous que le terrain dispose d'un certificat de titre approprié (pas seulement des droits d'occupation) avant de signer tout contrat de bail."),
    ("BCEL is the clear choice for expats in Laos — it has the broadest ATM network and the most foreigner-friendly service. Open both a LAK account and a USD account to handle both local and international transactions.",
     "BCEL est le choix évident pour les expatriés au Laos — il a le réseau de distributeurs le plus étendu et le service le plus accueillant pour les étrangers. Ouvrez à la fois un compte LAK et un compte USD pour gérer les transactions locales et internationales."),
    ("Pensionado visa holders receive a 20% discount on private healthcare services — keep this in mind when comparing insurance plans. Even with insurance, you'll pay a fraction of US costs for the same procedures.",
     "Les titulaires du visa Pensionado bénéficient de 20 % de réduction sur les services de santé privés — gardez cela à l'esprit lors de la comparaison des plans d'assurance. Même avec une assurance, vous paierez une fraction des coûts américains pour les mêmes procédures."),
    ("Combine mandatory CAJA (~$100/month) with a private complementary plan ($100-150/month) for the best of both worlds — comprehensive public coverage plus fast-track private access for specialist care.",
     "Combinez la CAJA obligatoire (~100 $/mois) avec un plan privé complémentaire (100-150 $/mois) pour le meilleur des deux mondes — couverture publique complète plus accès privé rapide pour les soins spécialisés."),
    ("Combine mandatory CAJA (~$100/month) with a private complementary plan ($100–150/month) for the best of both worlds — comprehensive public coverage plus fast-track private access for specialist care.",
     "Combinez la CAJA obligatoire (~100 $/mois) avec un plan privé complémentaire (100-150 $/mois) pour le meilleur des deux mondes — couverture publique complète plus accès privé rapide pour les soins spécialisés."),
    ("the title at the National Registry (Registro Nacional) yourself or via your lawyer before signing anything. Maritime zone properties near the beach require special legal expertise — do not purchase without understanding the concession terms.",
     "le titre au Registre National (Registro Nacional) vous-même ou via votre avocat avant de signer quoi que ce soit. Les propriétés en zone maritime près de la plage nécessitent une expertise juridique spéciale — n'achetez pas sans comprendre les termes de la concession."),
    ("current requirements with official government sources and consult a licensed professional before making major decisions.",
     "les exigences actuelles auprès des sources gouvernementales officielles et consultez un professionnel agréé avant de prendre des décisions importantes."),
    ("If you plan to visit the US for medical care, make sure your plan includes US coverage — this generally doubles the premium but is essential for serious conditions.",
     "Si vous prévoyez de vous rendre aux États-Unis pour des soins médicaux, assurez-vous que votre plan inclut la couverture américaine — cela double généralement la prime mais est indispensable pour les conditions graves."),
    ("BBVA Mexico and HSBC are the most expat-friendly. Avoid trying to open an account with only a tourist visa — most banks require at least a Temporary Resident card.",
     "BBVA Mexico et HSBC sont les plus accueillants pour les expatriés. Évitez d'essayer d'ouvrir un compte avec seulement un visa touristique — la plupart des banques exigent au moins une carte de Résident Temporaire."),
    ("The Notario Público in Mexico is NOT the same as a notary in other countries — they are senior lawyers with quasi-judicial powers who certify the transaction. Use a reputable one. Budget 10-15% of the purchase price for total closing costs.",
     "Le Notario Público au Mexique n'est PAS la même chose qu'un notaire dans d'autres pays — ce sont des avocats seniors avec des pouvoirs quasi-judiciaires qui certifient la transaction. Utilisez un notaire réputé. Prévoyez 10-15 % du prix d'achat pour les frais de clôture totaux."),
    ("The Notario Público in Mexico is NOT the same as a notary in other countries — they are senior lawyers with quasi-judicial powers who certify the transaction. Use a reputable one. Budget 10–15% of the purchase price for total closing costs.",
     "Le Notario Público au Mexique n'est PAS la même chose qu'un notaire dans d'autres pays — ce sont des avocats seniors avec des pouvoirs quasi-judiciaires qui certifient la transaction. Utilisez un notaire réputé. Prévoyez 10-15 % du prix d'achat pour les frais de clôture totaux."),
    ("have dedicated expat advisors with strong English skills. State banks (BCR, Banco Nacional) are the most accessible for new arrivals without a DIMEX card.",
     "ont des conseillers expatriés dédiés avec de solides compétences en anglais. Les banques d'État (BCR, Banco Nacional) sont les plus accessibles pour les nouveaux arrivants sans carte DIMEX."),
    ("have dedicated expat services in English. If you're moving to Madrid or Barcelona,", "ont des services expatriés dédiés en anglais. Si vous déménagez à Madrid ou Barcelone,"),
    ("have the best digital banking experience.", "ont la meilleure expérience de banque numérique."),
    ("is the preferred bank for the fixed deposit requirement — it's the most familiar to the MM2H agents and immigration officers.",
     "est la banque préférée pour l'exigence de dépôt fixe — c'est la plus familière des agents MM2H et des agents d'immigration."),
    ("savings account first, then convert to a fixed deposit once your MM2H is approved.",
     "un compte d'épargne d'abord, puis convertissez-le en dépôt fixe une fois votre MM2H approuvé."),
    ("is the most popular bank for residency purposes among expats. The $5,500 deposit must remain in the account until residency is approved — it earns a small amount of interest in the meantime.",
     "est la banque la plus populaire pour les demandes de résidence parmi les expatriés. Le dépôt de 5 500 $ doit rester sur le compte jusqu'à l'approbation de la résidence — il rapporte un petit montant d'intérêts en attendant."),
    ("Without a TRC, most Vietnamese banks will refuse to open an account.", "Sans TRC, la plupart des banques vietnamiennes refuseront d'ouvrir un compte."),
    ("and", "et"),
    ("are the most foreigner-friendly.", "sont les plus accueillantes pour les étrangers."),
    ("requires a higher minimum balance (~$500) but offers the best international transfer capabilities.",
     "nécessite un solde minimum plus élevé (~500 $) mais offre les meilleures capacités de transfert international."),
    ("Make sure your plan explicitly covers medical evacuation and repatriation — these are the most expensive emergencies for expats in Vietnam and are often excluded from basic plans.",
     "Assurez-vous que votre plan couvre explicitement l'évacuation médicale et le rapatriement — ce sont les urgences les plus coûteuses pour les expatriés au Vietnam et sont souvent exclues des plans de base."),
    ("The 30% cap on foreign ownership in apartment buildings can affect resale — once the cap is hit, only Vietnamese buyers can purchase remaining units. Check the current foreign ownership ratio before buying.",
     "Le plafond de 30 % de propriété étrangère dans les immeubles d'appartements peut affecter la revente — une fois le plafond atteint, seuls les acheteurs vietnamiens peuvent acheter les unités restantes. Vérifiez le ratio de propriété étrangère actuel avant d'acheter."),
    ("Paraguay's permanent residency is one of the fastest and cheapest in the world ($5,500 deposit + lawyer fees). Combined with the territorial tax system (no tax on foreign-source income), it's a powerful option for crypto investors and remote workers.",
     "La résidence permanente au Paraguay est l'une des plus rapides et des moins chères au monde (5 500 $ de dépôt + frais d'avocat). Combinée au système fiscal territorial (pas d'impôt sur les revenus de source étrangère), c'est une option puissante pour les investisseurs crypto et les travailleurs à distance."),
    ("Greece's Non-Dom tax regime (flat", "Le régime fiscal Non-Dom de la Grèce (forfaitaire"),
    ("on all foreign income) is one of Europe's most attractive for wealthy individuals. If your foreign income exceeds ~",
     "sur tous les revenus étrangers) est l'un des plus attractifs d'Europe pour les personnes fortunées. Si vos revenus étrangers dépassent ~"),
    ("this regime saves significant tax.", "ce régime permet des économies fiscales significatives."),
    ("on all foreign-source income (regardless of actual income amount).", "sur tous les revenus de source étrangère (quel que soit le montant réel des revenus)."),
    ("Apply in the first year of residency. Valid 15 years.", "À demander la première année de résidence. Valable 15 ans."),
    ("Open a Greek bank account (required for most visa types)", "Ouvrez un compte bancaire grec (requis pour la plupart des types de visa)"),
    ("Apply for the appropriate visa at your local Greek consulate",
     "Postulez pour le visa approprié à votre consulat grec local"),
    ("the new MM2H requirements (2021) are significantly stricter than before. The DE Rantau Nomad Pass at USD 24,000/year is a much more accessible option for remote workers and is processed much faster.",
     "les nouvelles exigences du MM2H (2021) sont nettement plus strictes qu'avant. Le DE Rantau Nomad Pass à 24 000 USD/an est une option beaucoup plus accessible pour les travailleurs à distance et est traité beaucoup plus rapidement."),
    ("For Employment Pass: employer applies on your behalf via EzXpat system",
     "Pour le permis de travail : l'employeur fait la demande en votre nom via le système EzXpat"),
    ("Upon approval, enter Malaysia and activate the visa",
     "Après approbation, entrez en Malaisie et activez le visa"),
    ("For MM2H specifically, the insurance must be issued by a Malaysian-licensed insurer and must be valid for the full duration of your stay.",
     "Pour le MM2H spécifiquement, l'assurance doit être émise par un assureur agréé en Malaisie et doit être valable pour toute la durée de votre séjour."),
    ("are the most commonly approved.", "sont les plus couramment approuvés."),
    ("Foreigners who invest in or direct a Vietnamese company can obtain a TRC through the company.",
     "Les étrangers qui investissent dans ou dirigent une entreprise vietnamienne peuvent obtenir un TRC par le biais de l'entreprise."),
    ("Minimum investment ~$130,000.", "Investissement minimum ~130 000 $."),
    ("Mexico City's Condesa/Roma Norte, San Miguel de Allende, Puerto Vallarta and Tulum have large expat communities with established support networks for the residency process.",
     "Les quartiers Condesa/Roma Norte de Mexico City, San Miguel de Allende, Puerto Vallarta et Tulum ont de grandes communautés expatriées avec des réseaux de soutien établis pour le processus de résidence."),
    ("Permanent residency with only $5,500 bank deposit", "Résidence permanente avec seulement 5 500 $ de dépôt bancaire"),
    ("Territorial tax system: foreign income not taxed", "Système fiscal territorial : revenus étrangers non imposés"),
    ("Crypto gains from foreign platforms are tax-free", "Les plus-values crypto provenant de plateformes étrangères sont exonérées d'impôt"),

    # =========================================================================
    # TAX SECTION
    # =========================================================================
    ("Territorial tax: no tax on income earned outside Costa Rica", "Fiscalité territoriale : pas d'impôt sur les revenus gagnés hors du Costa Rica"),
    ("No exit tax", "Pas de taxe de sortie"),
    ("Stable democracy with strong rule of law", "Démocratie stable avec un État de droit solide"),
    ("15% flat tax on capital gains realized in Thailand", "Impôt forfaitaire de 15 % sur les plus-values réalisées en Thaïlande"),
    ("No tax on gains from assets held before moving to Thailand", "Pas d'impôt sur les gains d'actifs détenus avant l'installation en Thaïlande"),
    ("LTR Visa holders: 17% flat income tax rate", "Titulaires du visa LTR : taux d'imposition forfaitaire de 17 %"),
    ("No inheritance tax under 100M THB", "Pas de droits de succession sous 100M THB"),
    ("10% CGT on gains up to 1,090 UVT, 15% above", "10 % sur les gains jusqu'à 1 090 UVT, 15 % au-dessus"),
    ("Crypto legally classified as intangible asset", "Crypto légalement classé comme actif incorporel"),
    ("No exit tax on unrealized gains", "Pas de taxe de sortie sur les plus-values latentes"),
    ("Digital nomad visa with favorable tax treatment", "Visa nomade numérique avec traitement fiscal favorable"),
    ("Crypto taxed as miscellaneous income (up to 55%)", "Crypto imposé comme revenu divers (jusqu'à 55 %)"),
    ("One of the highest crypto tax rates globally", "L'un des taux d'imposition crypto les plus élevés au monde"),
    ("Exit tax on unrealized gains if assets > 100M JPY", "Taxe de sortie sur les plus-values latentes si les actifs > 100M JPY"),
    ("Reform discussions ongoing for flat 20% CGT on crypto", "Discussions de réforme en cours pour un impôt forfaitaire de 20 % sur les plus-values crypto"),
    ("Income tax up to 35% could theoretically apply", "L'impôt sur le revenu jusqu'à 35 % pourrait théoriquement s'appliquer"),
    ("on crypto gains (since Jan 2024)", "sur les plus-values crypto (depuis janvier 2024)"),
    ("(misc. income, progressive)", "(revenu divers, progressif)"),
    ("0% on foreign-source income (territorial)", "0 % sur les revenus de source étrangère (territorial)"),
    ("10-15% CGT on crypto gains", "10-15 % sur les plus-values crypto"),
    ("15-55% (misc. income, progressive)", "15-55 % (revenu divers, progressif)"),
    ("Yes (> 100M JPY in assets)", "Oui (> 100M JPY en actifs)"),

    # Table cell label translations
    (">CAJA monthly contribution (resident)<", ">Cotisation mensuelle CAJA (résident)<"),
    (">CAJA consultation (covered)<", ">Consultation CAJA (couverte)<"),
    (">Free or nominal co-pay<", ">Gratuit ou co-paiement nominal<"),
    (">Private hospitalisation (per night)<", ">Hospitalisation privée (par nuit)<"),
    (">National Registry recording fee<", ">Frais d'enregistrement au Registre National<"),
    (">Annual municipality luxury tax (if applicable)<", ">Taxe municipale de luxe annuelle (si applicable)<"),

    # =========================================================================
    # MISC / CATCHALL
    # =========================================================================
    ("in person", "en personne"),
    ("and complete the bank's KYC form", "et remplissez le formulaire KYC de la banque"),
    ("open a", "ouvrez un"),
    ("as the primary account", "comme compte principal"),
    ("business days", "jours ouvrables"),
    ("on arrival or online", "à l'arrivée ou en ligne"),
    ("can be extended multiple times", "peut être prolongé plusieurs fois"),
    ("Popular with expat business owners and remote workers.", "Populaire auprès des propriétaires d'entreprises expatriés et des travailleurs à distance."),
    ("Specific category for foreign family members of Cambodian nationals.", "Catégorie spécifique pour les membres de famille étrangers de ressortissants cambodgiens."),
    ("Specific visa categories for humanitarian, diplomatic and international organisation staff.",
     "Catégories de visa spécifiques pour le personnel humanitaire, diplomatique et des organisations internationales."),
    ("Cambodia's visa system is very foreigner-friendly.", "Le système de visa du Cambodge est très favorable aux étrangers."),
    ("No minimum stay requirement, no income proof needed at most immigration offices.",
     "Pas d'exigence de séjour minimum, pas de preuve de revenus requise dans la plupart des bureaux d'immigration."),
    ("is the de facto 'digital nomad visa'.", "est le visa \"nomade numérique\" de facto."),
    ("The Pensionado visa requires", "Le visa Pensionado nécessite"),
    ("even a modest US Social Security benefit often qualifies.", "même une modeste prestation de sécurité sociale américaine suffit souvent."),
    ("The mandatory CAJA enrolment (~$50-150/month) gives access to Costa Rica's excellent public health system.",
     "L'inscription obligatoire à la CAJA (~50-150 $/mois) donne accès à l'excellent système de santé public du Costa Rica."),
    ("The mandatory CAJA enrolment (~$50–150/month) gives access to Costa Rica's excellent public health system.",
     "L'inscription obligatoire à la CAJA (~50-150 $/mois) donne accès à l'excellent système de santé public du Costa Rica."),
    # Mixed FR/EN cleanup
    ("Rendez-vous à l'agence bancaire in person", "Rendez-vous à l'agence bancaire en personne"),
    ("Account généralement opened within 1-5 business days", "Compte généralement ouvert sous 1 à 5 jours ouvrables"),
    ("Account généralement opened within 1–5 business days", "Compte généralement ouvert sous 1 à 5 jours ouvrables"),
    ("Best option for", "Meilleure option pour"),
    ("particularly to/from Europe and Asia.", "particulièrement vers/depuis l'Europe et l'Asie."),
    ("Paid by buyer", "Payé par l'acheteur"),
    ("paid by the buyer", "payé par l'acheteur"),
    ("'s de facto", "est de facto"),
    # Fix broken diacritics from BS4
    ("système de santé publics", "systèmes de santé publics"),
    ("facture de services publicss", "factures de services publics"),
    # Clean up leftover
    ("Coûtarricense", "Costarricense"),
]


def process_file(filepath):
    """Process a single HTML file."""
    fname = os.path.basename(filepath)
    print(f"\nProcessing: {fname}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)
    changes = 0

    # Separate head/JSON-LD and nav from main content to avoid touching them
    # Find the start of the main content section
    main_start = content.find('<section class="ftco-section">')
    footer_start = content.find('<footer')

    if main_start < 0:
        print("  WARNING: No ftco-section found, skipping")
        return 0

    if footer_start < 0:
        footer_start = len(content)

    head = content[:main_start]
    body = content[main_start:footer_start]
    tail = content[footer_start:]

    # Apply all replacements to body only
    for eng, fra in REPLACEMENTS:
        if eng in body:
            count = body.count(eng)
            body = body.replace(eng, fra)
            changes += count

    # Regex-based replacements for patterns
    regex_patterns = [
        # Fix /year and /month in body (but not in URLs)
        (r'(\$[\d,]+)/year', r'\1/an'),
        (r'(\$[\d,]+)/month', r'\1/mois'),
        (r'(€[\d,]+)/month', r'\1/mois'),
        (r'(AED [\d,]+)/year', r'\1/an'),
        (r'(¥[\d,]+)/month', r'\1/mois'),
        (r'(RM [\d,]+)/month', r'\1/mois'),
        # Fix "Strong in CityName." patterns
        (r'Strong in (\w+)\b', r'Fort à \1'),
        # Fix "Dépôt initial (typically" pattern
        (r'\(typically (\d)', r'(généralement \1'),
        # Fix remaining "from overseas" etc
        (r'from overseas', 'depuis l\'étranger'),
        (r'in foreign currency', 'en devises étrangères'),
        (r'proof required', 'justificatif requis'),
        (r'Most popular option', 'Option la plus populaire'),
        # Fix broken FR-EN
        (r'Justificatif de domicile in (\w+)', r'Justificatif de domicile en \1'),
        (r'Justificatif de domicile \(guesthouse or rental contract\)', 'Justificatif de domicile (maison d\'hôtes ou contrat de location)'),
        (r'for visa purposes', 'pour les demandes de visa'),
        (r'accepted for visa purposes', 'acceptés pour les demandes de visa'),
    ]

    for pattern, replacement in regex_patterns:
        body_new = re.sub(pattern, replacement, body)
        if body_new != body:
            changes += 1
            body = body_new

    result = head + body + tail

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"  -> {changes} replacements applied")
    return changes


def main():
    files = sorted(glob.glob(PATTERN))
    if not files:
        print(f"ERROR: No files found matching {PATTERN}")
        return

    print(f"Found {len(files)} expat guide files in FR directory")
    print("=" * 60)

    total = 0
    for f in files:
        total += process_file(f)

    print("\n" + "=" * 60)
    print(f"DONE. Total replacements: {total}")
    print(f"Files processed: {len(files)}")


if __name__ == '__main__':
    main()
