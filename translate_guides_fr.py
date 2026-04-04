#!/usr/bin/env python3
"""
Translate English content in French expat guide pages to French.
Processes all 16 country files in www/fr/.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FR_DIR = os.path.join(BASE_DIR, "www", "fr")

COUNTRIES = [
    "thailand", "portugal", "spain", "mexico", "vietnam", "malaysia",
    "japan", "uae", "colombia", "panama", "costa-rica", "greece",
    "georgia", "paraguay", "laos", "cambodia"
]

# Country name translations for "in <Country>" patterns in H2 headings
COUNTRY_IN_TRANSLATIONS = {
    "in Thailand": "en Tha\u00eflande",
    "in Portugal": "au Portugal",
    "in Spain": "en Espagne",
    "in Mexico": "au Mexique",
    "in Vietnam": "au Vietnam",
    "in Malaysia": "en Malaisie",
    "in Japan": "au Japon",
    "in the UAE": "aux \u00c9mirats Arabes Unis",
    "in Colombia": "en Colombie",
    "in Panama": "au Panama",
    "in Co\u00fbta Rica": "au Costa Rica",
    "in Costa Rica": "au Costa Rica",
    "in Greece": "en Gr\u00e8ce",
    "in Georgia": "en G\u00e9orgie",
    "in Paraguay": "au Paraguay",
    "in Laos": "au Laos",
    "in Cambodia": "au Cambodge",
}

# Common replacements applied to ALL files
# Order matters - longer/more specific strings first to avoid partial matches
COMMON_REPLACEMENTS = [
    # =============================================
    # FIX: "Coûta Rica" typo -> "Costa Rica" throughout
    # =============================================
    ("Co\u00fbta Rica", "Costa Rica"),

    # =============================================
    # SECTION TITLES (H2) - "Supplementary" in insurance heading
    # =============================================
    ("Supplementary Assurance Sant\u00e9", "Assurance Sant\u00e9 Compl\u00e9mentaire"),

    # H2 "Healthcare in the UAE" / "Healthcare in Costa Rica" (after Coûta Rica fix)
    ("Healthcare in the UAE", "Sant\u00e9 aux \u00c9mirats Arabes Unis"),
    ("Healthcare in Costa Rica", "Sant\u00e9 au Costa Rica"),

    # =============================================
    # TOC items for compact pages (laos, cambodia, georgia, etc.)
    # =============================================
    ('>Visa &amp; Residency<', '>Visa &amp; Options de R\u00e9sidence<'),
    ('>Healthcare<', '>Syst\u00e8me de Sant\u00e9<'),
    ('>Bank Account<', '>Ouvrir un Compte Bancaire<'),

    # =============================================
    # TABLE HEADERS
    # =============================================
    ("Estimated Co\u00fbt", "Co\u00fbt Estim\u00e9"),
    ("Typical Co\u00fbts", "Co\u00fbts Typiques"),

    # =============================================
    # SECTION 1 - Visa common phrases
    # =============================================
    ("Available Type de Visas", "Types de Visa Disponibles"),
    ("Available Visa Types", "Types de Visa Disponibles"),
    ("\u00c9tapes pour Obtenir la R\u00e9sidence", "Processus de R\u00e9sidence \u00c9tape par \u00c9tape"),
    ("Step-by-Step Residency Process", "Processus de R\u00e9sidence \u00c9tape par \u00c9tape"),

    # Visa table details (be careful with order - longer first)
    ("For expats 50+", "Pour les expatri\u00e9s de 50 ans et plus"),
    ("For remote workers earning", "Pour les travailleurs \u00e0 distance gagnant"),
    ("Membership programme", "Programme d\u2019adh\u00e9sion"),
    ("Required if working for", "Requis pour travailler dans"),

    # Residency steps
    ("Determine your visa category", "D\u00e9terminez votre cat\u00e9gorie de visa"),
    ("Gather documents:", "Rassemblez les documents :"),
    ("Apply at the nearest", "Postulez aupr\u00e8s de la plus proche"),
    ("Upon arrival, file", "\u00c0 votre arriv\u00e9e, d\u00e9posez"),
    ("Open a", "Ouvrez un"),
    ("Report every 90 days", "Signalement tous les 90 jours"),
    ("Renew annually", "Renouvellement annuel"),
    ("Valid passport", "Passeport valide"),
    ("Proof of address", "Justificatif de domicile"),
    ("Initial deposit", "D\u00e9p\u00f4t initial"),

    # =============================================
    # SECTION 2 - Healthcare
    # =============================================
    ("Public Healthcare", "Sant\u00e9 Publique"),
    ("Private Healthcare", "Sant\u00e9 Priv\u00e9e"),
    ("Typical Healthcare Costs", "Co\u00fbts de Sant\u00e9 Typiques"),
    ("GP consultation", "Consultation m\u00e9decin g\u00e9n\u00e9raliste"),
    ("Specialist consultation", "Consultation sp\u00e9cialiste"),
    ("Emergency room visit", "Visite aux urgences"),
    ("Hospitalisation (per night)", "Hospitalisation (par nuit)"),
    ("Dental cleaning", "D\u00e9tartrage dentaire"),
    ("Eye exam + glasses", "Examen de la vue + lunettes"),

    # =============================================
    # SECTION 3 - Insurance
    # =============================================
    ("Top Providers for Expats", "Meilleurs Assureurs pour Expatri\u00e9s"),
    ("Local insurer specialising in expats", "Assureur local sp\u00e9cialis\u00e9 dans les expatri\u00e9s"),
    ("Strong regional network", "R\u00e9seau r\u00e9gional solide"),
    ("International coverage", "Couverture internationale"),
    ("Comprehensive plans", "Formules compl\u00e8tes"),
    ("Flexible modular plans", "Formules modulaires flexibles"),
    ("ideal if you travel frequently", "id\u00e9al si vous voyagez fr\u00e9quemment"),
    ("or split time between countries", "ou partagez votre temps entre plusieurs pays"),

    # =============================================
    # SECTION 4 - Bank Account
    # =============================================
    ("Recommended Banks", "Banques Recommand\u00e9es"),
    ("Required Documents", "Documents Requis"),
    ("Step-by-Step Process", "Processus \u00c9tape par \u00c9tape"),
    ("Visit the bank branch in person", "Rendez-vous \u00e0 l\u2019agence bancaire en personne"),
    ("Request a savings account", "Demandez un compte d\u2019\u00e9pargne"),
    ("Present all documents", "Pr\u00e9sentez tous les documents"),
    ("Receive debit card", "Recevez votre carte de d\u00e9bit"),
    ("Activate online/mobile banking", "Activez les services bancaires en ligne/mobile"),
    ("Most expat-friendly bank", "Banque la plus adapt\u00e9e aux expatri\u00e9s"),
    ("Largest bank", "Plus grande banque"),
    ("Good English-language online banking", "Bons services bancaires en ligne en anglais"),
    ("Easier account opening", "Ouverture de compte plus facile"),
    ("Thai SIM card or phone number", "Carte SIM tha\u00eflandaise ou num\u00e9ro de t\u00e9l\u00e9phone"),

    # =============================================
    # SECTION 5 - Real Estate
    # =============================================
    ("Ownership Options for Foreigners", "Options de Propri\u00e9t\u00e9 pour les \u00c9trangers"),
    ("Options for Foreigners", "Options pour les \u00c9trangers"),
    ("Purchase Process", "Processus d\u2019Achat"),
    ("Typical Purchase Costs", "Co\u00fbts d\u2019Achat Typiques"),
    ("Full ownership permitted for foreigners", "Propri\u00e9t\u00e9 pleine autoris\u00e9e pour les \u00e9trangers"),
    ("Land and houses can be leased", "Les terrains et maisons peuvent \u00eatre lou\u00e9s"),
    ("Hire a reputable real estate lawyer", "Engagez un avocat immobilier r\u00e9put\u00e9"),
    ("Verify the title deed", "V\u00e9rifiez le titre de propri\u00e9t\u00e9"),
    ("Sign a Reservation Agreement", "Signez un contrat de r\u00e9servation"),
    ("Transfer fee", "Frais de transfert"),
    ("Stamp duty", "Droit de timbre"),
    ("specific business tax", "taxe professionnelle sp\u00e9cifique"),
    ("Withholding tax", "Retenue \u00e0 la source"),
    ("Lawyer fees", "Honoraires d\u2019avocat"),
    ("Agent commission", "Commission de l\u2019agent"),
    ("Land can be registered in", "Le terrain peut \u00eatre enregistr\u00e9 au nom de"),

    # =============================================
    # Common across all sections
    # =============================================
    ("Pro Tip:", "Conseil Pro :"),
    ("Recommended:", "Recommand\u00e9 :"),
    ("About This Guide", "\u00c0 propos de ce Guide"),
    ("This guide is researched and maintained by", "Ce guide est recherch\u00e9 et maintenu par"),
    ("the editorial team at", "l\u2019\u00e9quipe \u00e9ditoriale de"),
    ("Last updated:", "Derni\u00e8re mise \u00e0 jour :"),
    ("Related Expat Guides", "Guides Expatriation Connexes"),
    ("All Expat Guides", "Tous les Guides Expatriation"),
    ("Retirement Visa Guide", "Guide Visa Retraite"),
    ("Digital Nomad Visas", "Visas Nomade Num\u00e9rique"),
    ("Read the Guide", "Lire le Guide"),
    ("Global eVisa &amp; Travel Information Platform", "Plateforme Mondiale d\u2019Information eVisa &amp; Voyage"),

    # =============================================
    # Footer
    # =============================================
    ("Follow eVisa-Card.com", "Suivez eVisa-Card.com"),

    # =============================================
    # Compact pages: "Property in X for Foreigners" -> translate
    # =============================================
    ("Property in Laos for Foreigners", "Immobilier au Laos pour les \u00c9trangers"),
]

# H2 headings with "in <Country>" pattern - for bank and real estate sections
# These need the country-specific translation
COUNTRY_H2_PATTERNS = [
    # Bank Account section: "Ouvrir un Compte Bancaire in <Country>"
    "Ouvrir un Compte Bancaire",
    # Real Estate section: "Acheter un Bien Immobilier in <Country>"
    "Acheter un Bien Immobilier",
    # Insurance: "Assurance Santé in <Country>" (after the Supplementary fix)
    "Assurance Sant\u00e9",
    # Healthcare: "Healthcare in <Country>" (UAE specific)
    "Healthcare",
]

# JSON-LD FAQ translations
FAQ_TRANSLATIONS = {
    "Can foreigners buy property in Thailand?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en Tha\u00eflande ?",
    "What health insurance do I need in Thailand?":
        "De quelle assurance sant\u00e9 ai-je besoin en Tha\u00eflande ?",
    "How do I open a bank account in Thailand?":
        "Comment ouvrir un compte bancaire en Tha\u00eflande ?",

    "Can foreigners buy property in Portugal?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Portugal ?",
    "What health insurance do I need in Portugal?":
        "De quelle assurance sant\u00e9 ai-je besoin au Portugal ?",
    "How do I open a bank account in Portugal?":
        "Comment ouvrir un compte bancaire au Portugal ?",

    "Can foreigners buy property in Spain?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en Espagne ?",
    "What health insurance do I need in Spain?":
        "De quelle assurance sant\u00e9 ai-je besoin en Espagne ?",
    "How do I open a bank account in Spain?":
        "Comment ouvrir un compte bancaire en Espagne ?",

    "Can foreigners buy property in Mexico?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Mexique ?",
    "What health insurance do I need in Mexico?":
        "De quelle assurance sant\u00e9 ai-je besoin au Mexique ?",
    "How do I open a bank account in Mexico?":
        "Comment ouvrir un compte bancaire au Mexique ?",

    "Can foreigners buy property in Vietnam?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Vietnam ?",
    "What health insurance do I need in Vietnam?":
        "De quelle assurance sant\u00e9 ai-je besoin au Vietnam ?",
    "How do I open a bank account in Vietnam?":
        "Comment ouvrir un compte bancaire au Vietnam ?",

    "Can foreigners buy property in Malaysia?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en Malaisie ?",
    "What health insurance do I need in Malaysia?":
        "De quelle assurance sant\u00e9 ai-je besoin en Malaisie ?",
    "How do I open a bank account in Malaysia?":
        "Comment ouvrir un compte bancaire en Malaisie ?",

    "Can foreigners buy property in Japan?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Japon ?",
    "What health insurance do I need in Japan?":
        "De quelle assurance sant\u00e9 ai-je besoin au Japon ?",
    "How do I open a bank account in Japan?":
        "Comment ouvrir un compte bancaire au Japon ?",

    "Can foreigners buy property in the UAE?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier aux \u00c9mirats Arabes Unis ?",
    "What health insurance do I need in the UAE?":
        "De quelle assurance sant\u00e9 ai-je besoin aux \u00c9mirats Arabes Unis ?",
    "How do I open a bank account in the UAE?":
        "Comment ouvrir un compte bancaire aux \u00c9mirats Arabes Unis ?",

    "Can foreigners buy property in Colombia?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en Colombie ?",
    "What health insurance do I need in Colombia?":
        "De quelle assurance sant\u00e9 ai-je besoin en Colombie ?",
    "How do I open a bank account in Colombia?":
        "Comment ouvrir un compte bancaire en Colombie ?",

    "Can foreigners buy property in Panama?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Panama ?",
    "What health insurance do I need in Panama?":
        "De quelle assurance sant\u00e9 ai-je besoin au Panama ?",
    "How do I open a bank account in Panama?":
        "Comment ouvrir un compte bancaire au Panama ?",

    "Can foreigners buy property in Costa Rica?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Costa Rica ?",
    "What health insurance do I need in Costa Rica?":
        "De quelle assurance sant\u00e9 ai-je besoin au Costa Rica ?",
    "How do I open a bank account in Costa Rica?":
        "Comment ouvrir un compte bancaire au Costa Rica ?",

    "Can foreigners buy property in Greece?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en Gr\u00e8ce ?",
    "What health insurance do I need in Greece?":
        "De quelle assurance sant\u00e9 ai-je besoin en Gr\u00e8ce ?",
    "How do I open a bank account in Greece?":
        "Comment ouvrir un compte bancaire en Gr\u00e8ce ?",

    "Can foreigners buy property in Georgia?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier en G\u00e9orgie ?",
    "What health insurance do I need in Georgia?":
        "De quelle assurance sant\u00e9 ai-je besoin en G\u00e9orgie ?",
    "How do I open a bank account in Georgia?":
        "Comment ouvrir un compte bancaire en G\u00e9orgie ?",

    "Can foreigners buy property in Paraguay?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Paraguay ?",
    "What health insurance do I need in Paraguay?":
        "De quelle assurance sant\u00e9 ai-je besoin au Paraguay ?",
    "How do I open a bank account in Paraguay?":
        "Comment ouvrir un compte bancaire au Paraguay ?",

    "Can foreigners buy property in Laos?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Laos ?",
    "What health insurance do I need in Laos?":
        "De quelle assurance sant\u00e9 ai-je besoin au Laos ?",
    "How do I open a bank account in Laos?":
        "Comment ouvrir un compte bancaire au Laos ?",

    "Can foreigners buy property in Cambodia?":
        "Les \u00e9trangers peuvent-ils acheter un bien immobilier au Cambodge ?",
    "What health insurance do I need in Cambodia?":
        "De quelle assurance sant\u00e9 ai-je besoin au Cambodge ?",
    "How do I open a bank account in Cambodia?":
        "Comment ouvrir un compte bancaire au Cambodge ?",
}

# FAQ answer translations (common patterns in JSON-LD answers)
FAQ_ANSWER_TRANSLATIONS = [
    ("Foreigners cannot own land in Thailand", "Les \u00e9trangers ne peuvent pas poss\u00e9der de terrain en Tha\u00eflande"),
    ("but they can own condominium units freehold", "mais ils peuvent poss\u00e9der des appartements en copropri\u00e9t\u00e9 en pleine propri\u00e9t\u00e9"),
    ("International health insurance is mandatory", "L\u2019assurance sant\u00e9 internationale est obligatoire"),
    ("A Thai bank account is practically essential for expats", "Un compte bancaire tha\u00eflandais est pratiquement indispensable pour les expatri\u00e9s"),
    ("Portugal has no restrictions on foreigners buying property", "Le Portugal n\u2019impose aucune restriction aux \u00e9trangers pour l\u2019achat de biens immobiliers"),
    ("The process is transparent and well-regulated", "Le processus est transparent et bien r\u00e9glement\u00e9"),
    ("While public healthcare is excellent for residents", "Bien que le syst\u00e8me de sant\u00e9 public soit excellent pour les r\u00e9sidents"),
    ("A Portuguese bank account is required", "Un compte bancaire portugais est requis"),
    ("Foreigners can freely buy property in Spain", "Les \u00e9trangers peuvent librement acheter des biens immobiliers en Espagne"),
    ("with no restrictions", "sans aucune restriction"),
    ("Private health insurance is compulsory", "L\u2019assurance sant\u00e9 priv\u00e9e est obligatoire"),
    ("A Spanish bank account is needed", "Un compte bancaire espagnol est n\u00e9cessaire"),
    ("A Mexican bank account is required", "Un compte bancaire mexicain est requis"),
    ("A Colombian bank account simplifies daily life", "Un compte bancaire colombien simplifie la vie quotidienne"),
    ("Health insurance is legally mandatory", "L\u2019assurance sant\u00e9 est l\u00e9galement obligatoire"),
    ("A UAE bank account is essential", "Un compte bancaire aux \u00c9mirats est indispensable"),
    ("Foreigners can buy property in the UAE", "Les \u00e9trangers peuvent acheter des biens immobiliers aux \u00c9mirats Arabes Unis"),
    ("Foreigners can buy property in Mexico", "Les \u00e9trangers peuvent acheter des biens immobiliers au Mexique"),
    ("Foreigners can freely buy property in Colombia", "Les \u00e9trangers peuvent librement acheter des biens immobiliers en Colombie"),
]

# Meta description translations
META_DESC_TRANSLATIONS = {
    "thailand": (
        'content="Complete guide to living in Tha\u00eflande as an expat in 2026. Visa options, residency, healthcare, supplementary insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en Tha\u00eflande en tant qu\u2019expatri\u00e9 en 2026. Options de visa, r\u00e9sidence, soins de sant\u00e9, assurance compl\u00e9mentaire, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "portugal": (
        'content="Complete guide to living in Portugal as an expat in 2026. D7 visa, Golden Visa, NHR tax status, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Portugal en tant qu\u2019expatri\u00e9 en 2026. Visa D7, Golden Visa, statut fiscal RNH, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "spain": (
        'content="Complete guide to living in Espagne as an expat in 2026. Non-lucrative visa, digital nomad visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en Espagne en tant qu\u2019expatri\u00e9 en 2026. Visa non lucratif, visa nomade num\u00e9rique, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "mexico": (
        'content="Complete guide to living in Mexique as an expat in 2026. Temporary resident visa, retirement visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Mexique en tant qu\u2019expatri\u00e9 en 2026. Visa de r\u00e9sident temporaire, visa retraite, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "vietnam": (
        'content="Complete guide to living in Vietnam as an expat in 2026. Work permit, investor visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Vietnam en tant qu\u2019expatri\u00e9 en 2026. Permis de travail, visa investisseur, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "malaysia": (
        'content="Complete guide to living in Malaisie as an expat in 2026. MM2H visa, work permit, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en Malaisie en tant qu\u2019expatri\u00e9 en 2026. Visa MM2H, permis de travail, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "japan": (
        'content="Complete guide to living in Japon as an expat in 2026. Work visa, business manager visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Japon en tant qu\u2019expatri\u00e9 en 2026. Visa de travail, visa business manager, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "uae": (
        'content="Complete guide to living in the UAE as an expat in 2026. Golden visa, freelancer visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre aux \u00c9mirats Arabes Unis en tant qu\u2019expatri\u00e9 en 2026. Golden visa, visa freelance, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "colombia": (
        'content="Complete guide to living in Colombie as an expat in 2026. Migrant visa, digital nomad visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en Colombie en tant qu\u2019expatri\u00e9 en 2026. Visa migrant, visa nomade num\u00e9rique, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "panama": (
        'content="Complete guide to living in Panama as an expat in 2026. Pensionado visa, friendly nations visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Panama en tant qu\u2019expatri\u00e9 en 2026. Visa Pensionado, visa des nations amies, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "costa-rica": (
        'content="Complete guide to living in Costa Rica as an expat in 2026. Pensionado visa, rentista visa, CAJA healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Costa Rica en tant qu\u2019expatri\u00e9 en 2026. Visa Pensionado, visa Rentista, syst\u00e8me de sant\u00e9 CAJA, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "greece": (
        'content="Complete guide to living in Gr\u00e8ce as an expat in 2026. Golden visa, digital nomad visa, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en Gr\u00e8ce en tant qu\u2019expatri\u00e9 en 2026. Golden visa, visa nomade num\u00e9rique, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "georgia": (
        'content="Complete guide to living in G\u00e9orgie as an expat in 2026. Visa-free stays, residency permits, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre en G\u00e9orgie en tant qu\u2019expatri\u00e9 en 2026. S\u00e9jours sans visa, permis de r\u00e9sidence, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "paraguay": (
        'content="Complete guide to living in Paraguay as an expat in 2026. Permanent residency, SUACE process, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Paraguay en tant qu\u2019expatri\u00e9 en 2026. R\u00e9sidence permanente, processus SUACE, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
    "laos": (
        'content="Complete guide to living in Laos as an expat in 2026. Business visa, temporary residence, healthcare, health insurance, bank accounts and property for foreigners."',
        'content="Guide complet pour vivre au Laos en tant qu\u2019expatri\u00e9 en 2026. Visa d\u2019affaires, r\u00e9sidence temporaire, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et immobilier pour les \u00e9trangers."'
    ),
    "cambodia": (
        'content="Complete guide to living in Cambodge as an expat in 2026. E-class visa, work permit, healthcare, health insurance, bank accounts and property buying for foreigners."',
        'content="Guide complet pour vivre au Cambodge en tant qu\u2019expatri\u00e9 en 2026. Visa classe E, permis de travail, soins de sant\u00e9, assurance sant\u00e9, comptes bancaires et achat immobilier pour les \u00e9trangers."'
    ),
}

# Related Guides link fixes: /en/ -> /fr/ (only in the Related Guides section at the bottom)
RELATED_GUIDES_LINK_REPLACEMENTS = [
    ('href="/en/expat-guides.html"', 'href="/fr/expat-guides.html"'),
    ('href="/en/retirement-visa-guide.html"', 'href="/fr/retirement-visa-guide.html"'),
    ('href="/en/digital-nomad-visas-guide.html"', 'href="/fr/digital-nomad-visas-guide.html"'),
    ('href="/en/cheapest-countries-to-retire-abroad-2026.html"', 'href="/fr/cheapest-countries-to-retire-abroad-2026.html"'),
]

# "Cheapest Countries to Retire" link text translation
LINK_TEXT_TRANSLATIONS = [
    (">Cheapest Countries to Retire<", ">Pays les Moins Chers pour la Retraite<"),
    (">Visas Nomades Num\u00e9riques<", ">Visas Nomade Num\u00e9rique<"),
]


def translate_file(filepath, country):
    """Apply all translations to a single file. Returns number of replacements made."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    total_replacements = 0

    # 1) Apply common replacements
    for old, new in COMMON_REPLACEMENTS:
        if old in content and old != new:
            count = content.count(old)
            content = content.replace(old, new)
            total_replacements += count

    # 2) Apply country-specific "in <Country>" H2 translations
    for country_en, country_fr in COUNTRY_IN_TRANSLATIONS.items():
        # Replace "in <Country>" at end of H2 headings (in context)
        for h2_prefix in COUNTRY_H2_PATTERNS:
            old_text = f"{h2_prefix} {country_en}"
            new_text = f"{h2_prefix} {country_fr}"
            if old_text in content:
                count = content.count(old_text)
                content = content.replace(old_text, new_text)
                total_replacements += count

    # 3) Apply FAQ translations (JSON-LD)
    for faq_en, faq_fr in FAQ_TRANSLATIONS.items():
        if faq_en in content:
            count = content.count(faq_en)
            content = content.replace(faq_en, faq_fr)
            total_replacements += count

    # 4) Apply FAQ answer translations
    for old, new in FAQ_ANSWER_TRANSLATIONS:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            total_replacements += count

    # 5) Apply meta description translation
    if country in META_DESC_TRANSLATIONS:
        old_meta, new_meta = META_DESC_TRANSLATIONS[country]
        if old_meta in content:
            count = content.count(old_meta)
            content = content.replace(old_meta, new_meta)
            total_replacements += count

    # 6) Fix Related Guides links: /en/ -> /fr/
    for old_link, new_link in RELATED_GUIDES_LINK_REPLACEMENTS:
        if old_link in content:
            count = content.count(old_link)
            content = content.replace(old_link, new_link)
            total_replacements += count

    # 7) Link text translations
    for old_text, new_text in LINK_TEXT_TRANSLATIONS:
        if old_text in content:
            count = content.count(old_text)
            content = content.replace(old_text, new_text)
            total_replacements += count

    # Write back only if changed
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return total_replacements


def main():
    print("=" * 60)
    print("French Expat Guide Translation Script")
    print("=" * 60)
    print()

    total_files_updated = 0
    total_replacements = 0

    for country in COUNTRIES:
        filename = f"expat-guide-{country}.html"
        filepath = os.path.join(FR_DIR, filename)

        if not os.path.exists(filepath):
            print(f"  [SKIP] {filename} — file not found")
            continue

        replacements = translate_file(filepath, country)

        if replacements > 0:
            print(f"  [OK]   {filename} — {replacements} replacements")
            total_files_updated += 1
            total_replacements += replacements
        else:
            print(f"  [--]   {filename} — no changes needed")

    print()
    print("-" * 60)
    print(f"Total files updated: {total_files_updated}/{len(COUNTRIES)}")
    print(f"Total replacements:  {total_replacements}")
    print("=" * 60)


if __name__ == "__main__":
    main()
