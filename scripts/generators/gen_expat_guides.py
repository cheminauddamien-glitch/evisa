#!/usr/bin/env python3
"""Generate expatriation guide pages per country in EN/FR/ES/PT."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

LANG_FLAGS = {"en": "fi-gb", "fr": "fi-fr", "es": "fi-es", "pt": "fi-br"}
LANG_NAMES = {"en": "English", "fr": "Français", "es": "Español", "pt": "Português"}
LANG_LABELS = {
    "en": {"home":"Home","dest":"Destinations","about":"About","blog":"Blog","guides":"Guides"},
    "fr": {"home":"Accueil","dest":"Destinations","about":"À propos","blog":"Blog","guides":"Guides"},
    "es": {"home":"Inicio","dest":"Destinos","about":"Sobre Nosotros","blog":"Blog","guides":"Guías"},
    "pt": {"home":"Início","dest":"Destinos","about":"Sobre Nós","blog":"Blog","guides":"Guias"},
}
FOOTER_COPY = {
    "en": "© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform",
    "fr": "© 2026 eVisa-Card.com — Plateforme mondiale d'information eVisa",
    "es": "© 2026 eVisa-Card.com — Plataforma global de información eVisa",
    "pt": "© 2026 eVisa-Card.com — Plataforma global de informações eVisa",
}
FOOTER_LEGAL = {
    "en": ('/en/legal-notice.html','Legal Notice','/en/disclaimer.html','Disclaimer'),
    "fr": ('/fr/mentions-legales.html','Mentions légales','/fr/disclaimer.html','Disclaimer'),
    "es": ('/es/aviso-legal.html','Aviso Legal','/es/disclaimer.html','Disclaimer'),
    "pt": ('/pt/aviso-legal.html','Aviso Legal','/pt/disclaimer.html','Disclaimer'),
}

def make_navbar(lang, slug):
    L = LANG_LABELS[lang]
    sw = ""
    for tl in ["en","fr","es","pt"]:
        active = ' active' if tl == lang else ''
        url = f"/{tl}/{slug}.html" if tl != "en" else f"/en/{slug}.html"
        sw += f'\n                        <a class="dropdown-item{active}" href="{url}"><span class="fi {LANG_FLAGS[tl]}"></span> {LANG_NAMES[tl]}</a>'
    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav mx-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">{L['home']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">{L['dest']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">{L['about']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">{L['blog']}</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">{L['guides']}</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {LANG_FLAGS[lang]}"></span> {LANG_NAMES[lang]}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">{sw}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

def make_footer(lang):
    copy = FOOTER_COPY[lang]
    u1,l1,u2,l2 = FOOTER_LEGAL[lang]
    return f"""<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">{copy}</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="{u1}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l1}</a>
                    &nbsp;|&nbsp;
                    <a href="{u2}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l2}</a>
                </p>
            </div>
        </div>
    </div>
</footer>"""

def make_page(lang, slug, data):
    d = data[lang]
    navbar = make_navbar(lang, slug)
    footer = make_footer(lang)
    iso = data["iso"]
    visa_slug = data.get("visa_slug", "")
    visa_link = f'<a href="/{lang}/visa-{visa_slug}.html">' if visa_slug else '<a href="../destination.html">'

    steps_html = ""
    for i, step in enumerate(d["steps"], 1):
        steps_html += f"""
        <div class="step-item d-flex mb-4">
            <div class="step-number mr-3" style="min-width:40px;height:40px;background:#f15d30;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:18px;">{i}</div>
            <div>
                <h3 style="font-size:18px;margin-bottom:6px;">{step['title']}</h3>
                <p style="margin:0;color:#555;">{step['desc']}</p>
            </div>
        </div>"""

    faq_items = ""
    schema_faq = ""
    for q, a in d["faq"]:
        faq_items += f"""
        <div class="mb-4">
            <h3 style="font-size:17px;color:#1d2d50;">❓ {q}</h3>
            <p style="color:#555;">{a}</p>
        </div>"""
        schema_faq += f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}},'

    howto_steps = ",".join([f'{{"@type":"HowToStep","name":"{s["title"]}","text":"{s["desc"]}"}}' for s in d["steps"]])

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{d['title']}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content="{d['meta_desc']}"/>
    <link rel="canonical" href="https://www.evisa-card.com/{lang}/{slug}.html"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}.html"/>
    <link rel="alternate" hreflang="fr" href="https://www.evisa-card.com/fr/{slug}.html"/>
    <link rel="alternate" hreflang="es" href="https://www.evisa-card.com/es/{slug}.html"/>
    <link rel="alternate" hreflang="pt" href="https://www.evisa-card.com/pt/{slug}.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}.html"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@graph":[
    {{"@type":"HowTo","name":"{d['h1']}","description":"{d['meta_desc']}","step":[{howto_steps}]}},
    {{"@type":"FAQPage","mainEntity":[{schema_faq.rstrip(',')}]}}
    ]}}
    </script>
</head>
<body>
{navbar}

<section class="hero-wrap hero-wrap-2" style="background-image: url(https://flagcdn.com/w1280/{iso}.png);" data-stellar-background-ratio="0.5">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate text-center pb-5">
                <p class="breadcrumbs"><span class="mr-2"><a href="../index.html">{LANG_LABELS[lang]['home']} <i class="fa fa-chevron-right"></i></a></span> <span>{d['breadcrumb']} <i class="fa fa-chevron-right"></i></span></p>
                <h1 class="mb-0 bread">{d['h1']}</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
<div class="container" style="max-width:900px;">

    <div class="row mb-5">
        <div class="col-md-12">
            <p style="font-size:17px;color:#444;">{d['intro']}</p>
            <p style="font-size:13px;color:#999;">Last updated: March 2026 — <em>Editorial Team, eVisa-Card.com</em></p>
        </div>
    </div>

    <!-- Key Facts -->
    <div class="row mb-5">
        <div class="col-md-12">
            <div style="background:#f8f9fc;border-left:4px solid #f15d30;padding:20px 25px;border-radius:4px;">
                <h2 style="font-size:20px;margin-bottom:15px;color:#1d2d50;"><span class="fi fi-{iso}" style="margin-right:8px;"></span> {d['facts_title']}</h2>
                <div class="row">
                    {d['facts_html']}
                </div>
            </div>
        </div>
    </div>

    <!-- Visa Section -->
    <div class="row mb-5">
        <div class="col-md-12">
            <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['visa_section_title']}</h2>
            <p>{d['visa_section_text']}</p>
            <p>{visa_link}{d['visa_link_text']}</a></p>
        </div>
    </div>

    <!-- Step-by-step -->
    <div class="row mb-5">
        <div class="col-md-12">
            <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['steps_title']}</h2>
            {steps_html}
        </div>
    </div>

    <!-- Practical Info Grid -->
    <div class="row mb-5">
        <div class="col-md-6 mb-4">
            <div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
                <h3 style="font-size:17px;color:#1d2d50;">🏠 {d['housing_title']}</h3>
                <p style="font-size:14px;color:#555;">{d['housing_text']}</p>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
                <h3 style="font-size:17px;color:#1d2d50;">🏦 {d['banking_title']}</h3>
                <p style="font-size:14px;color:#555;">{d['banking_text']}</p>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
                <h3 style="font-size:17px;color:#1d2d50;">🏥 {d['health_title']}</h3>
                <p style="font-size:14px;color:#555;">{d['health_text']}</p>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
                <h3 style="font-size:17px;color:#1d2d50;">💰 {d['cost_title']}</h3>
                <p style="font-size:14px;color:#555;">{d['cost_text']}</p>
            </div>
        </div>
    </div>

    <!-- FAQ -->
    <div class="row mb-5">
        <div class="col-md-12">
            <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['faq_title']}</h2>
            {faq_items}
        </div>
    </div>

</div>
</section>

{footer}
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""

# ─── COUNTRY DATA ────────────────────────────────────────────────────────────
COUNTRIES = {

"expat-guide-thailand": {
    "iso": "th",
    "visa_slug": "thailand",
    "en": {
        "title": "Expat Guide Thailand 2026 — How to Live in Thailand | eVisa-Card.com",
        "meta_desc": "Complete expat guide to living in Thailand 2026. Visa options, step-by-step residency process, housing, banking, healthcare and cost of living.",
        "h1": "Expat Guide: Living in Thailand 2026",
        "breadcrumb": "Expat Guide Thailand",
        "intro": "Thailand is one of the world's top expat destinations, attracting retirees, digital nomads and families with its warm climate, affordable cost of living, world-class cuisine and welcoming culture. This guide walks you through everything you need to know to relocate to Thailand in 2026.",
        "facts_title": "Thailand at a Glance",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Bangkok</div><div class="col-md-3 col-6"><strong>Currency</strong><br/>Thai Baht (THB)</div><div class="col-md-3 col-6"><strong>Language</strong><br/>Thai</div><div class="col-md-3 col-6"><strong>Cost of Living</strong><br/>Low–Medium</div>',
        "visa_section_title": "Visa & Residency Options",
        "visa_section_text": "Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
        "visa_link_text": "→ Full Thailand Visa Requirements & Application Guide",
        "steps_title": "Step-by-Step: How to Move to Thailand",
        "steps": [
            {"title": "Choose your visa type", "desc": "Determine if you qualify for the Retirement O-A (50+, pension/savings proof), LTR Visa (remote worker, $80k income), or Thailand Elite. Most expats start with a Tourist Visa and switch after arrival."},
            {"title": "Gather required documents", "desc": "Passport (6+ months validity), passport photos, bank statements (800,000 THB in Thai bank for retirement visa or proof of $80k income for LTR), health insurance, medical certificate."},
            {"title": "Apply at a Thai embassy or consulate", "desc": "Submit your visa application at your nearest Thai embassy. Processing takes 3–5 business days. You can also enter on a tourist visa and extend at the Immigration Bureau in Thailand."},
            {"title": "Arrive and register your address", "desc": "Within 24 hours of arriving, notify your accommodation. If renting, your landlord must file a TM.30 report. You receive a TM.6 arrival card."},
            {"title": "Open a Thai bank account", "desc": "Open a Kasikorn Bank (KBank) or Bangkok Bank account. You'll need your passport, Non-Immigrant visa, and proof of address. Required for the 800,000 THB retirement deposit."},
            {"title": "Get health insurance", "desc": "Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage."},
            {"title": "Annual extension / 90-day report", "desc": "Renew your visa annually at the local Immigration office. File 90-day reports in person, by post, or online via the Immigration Bureau website."},
        ],
        "housing_title": "Housing",
        "housing_text": "Bangkok studio: ฿8,000–฿15,000/month. Chiang Mai 1-bed: ฿6,000–฿12,000/month. Phuket condo: ฿12,000–฿25,000/month. Foreigners cannot own land but can own condo units (49% foreign quota per building).",
        "banking_title": "Banking",
        "banking_text": "Major banks: Kasikorn (KBank), Bangkok Bank, SCB. Open with Non-Immigrant visa + passport. Online banking available in English. Wise and Revolut are popular for international transfers.",
        "health_title": "Healthcare",
        "health_text": "Excellent private hospitals (Bumrungrad, BNH, Samitivej) with English-speaking staff. Private health insurance required for most long-stay visas. Costs significantly lower than Western countries.",
        "cost_title": "Cost of Living",
        "cost_text": "Budget: ฿30,000–฿40,000/month ($850–$1,100). Comfortable: ฿60,000–฿90,000/month ($1,700–$2,500). Luxury: ฿120,000+/month. Chiang Mai cheaper than Bangkok or Phuket.",
        "faq_title": "Frequently Asked Questions",
        "faq": [
            ("Can foreigners work in Thailand?", "Yes, with a work permit. Remote workers can use the LTR Visa to work for overseas employers legally without a Thai work permit."),
            ("What is the minimum income for a retirement visa?", "You need to show 800,000 THB (~$22,000) in a Thai bank account, OR a monthly income/pension of 65,000 THB (~$1,800), OR a combination totaling 800,000 THB."),
            ("Can I bring my spouse?", "Yes. Your spouse can apply for a Non-Immigrant O visa as a dependent. They will need to do 90-day reports and annual extensions as well."),
            ("Is Thailand safe for expats?", "Thailand is generally safe for expats. Petty crime exists in tourist areas. Natural disasters (floods, occasional storms) can affect some regions."),
            ("Do I need to speak Thai?", "Not necessary in major cities and tourist areas. English is widely spoken in Bangkok, Chiang Mai and Phuket. Learning basic Thai is appreciated and helpful."),
        ],
    },
    "fr": {
        "title": "Guide Expatriation Thaïlande 2026 — Vivre en Thaïlande | eVisa-Card.com",
        "meta_desc": "Guide complet pour s'expatrier en Thaïlande 2026. Options de visa, démarches résidence, logement, banque, santé et coût de la vie.",
        "h1": "Guide Expatriation : Vivre en Thaïlande 2026",
        "breadcrumb": "Guide Expatriation Thaïlande",
        "intro": "La Thaïlande est l'une des destinations préférées des expatriés dans le monde, séduisant retraités, nomades numériques et familles par son climat chaud, son coût de vie abordable et sa culture accueillante. Ce guide vous accompagne pas à pas pour vous installer en Thaïlande en 2026.",
        "facts_title": "La Thaïlande en bref",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capitale</strong><br/>Bangkok</div><div class="col-md-3 col-6"><strong>Monnaie</strong><br/>Baht thaïlandais (THB)</div><div class="col-md-3 col-6"><strong>Langue</strong><br/>Thaï</div><div class="col-md-3 col-6"><strong>Coût de vie</strong><br/>Faible–Moyen</div>',
        "visa_section_title": "Options de visa et résidence",
        "visa_section_text": "La Thaïlande propose plusieurs options pour un long séjour : Visa Touriste (60 jours, prorogeable), Visa Non-Immigrant O-A Retraite (1 an renouvelable, dès 50 ans), Thailand Elite Visa (5–20 ans, premium), Visa LTR pour professionnels et nomades numériques.",
        "visa_link_text": "→ Guide complet des visas Thaïlande",
        "steps_title": "Étapes pour s'installer en Thaïlande",
        "steps": [
            {"title": "Choisir son type de visa", "desc": "Déterminez si vous êtes éligible au visa retraite O-A (50+, justificatif de revenus/épargne), au visa LTR (travail à distance, revenus ≥ 80k$/an) ou au Thailand Elite. La plupart des expatriés entrent d'abord avec un visa touriste."},
            {"title": "Rassembler les documents requis", "desc": "Passeport valide (6+ mois), photos d'identité, relevés bancaires (800 000 THB en banque thaïlandaise pour retraite ou preuve de revenus 80k$ pour LTR), assurance santé, certificat médical."},
            {"title": "Déposer la demande à l'ambassade", "desc": "Déposez votre demande de visa à l'ambassade thaïlandaise la plus proche. Délai de traitement : 3–5 jours ouvrés."},
            {"title": "Arriver et déclarer son adresse", "desc": "Dans les 24h suivant votre arrivée, déclarez votre hébergement. Votre propriétaire doit déposer un formulaire TM.30. Vous recevez la carte d'arrivée TM.6."},
            {"title": "Ouvrir un compte bancaire thaïlandais", "desc": "Ouvrez un compte chez Kasikorn Bank (KBank) ou Bangkok Bank. Nécessaire pour le dépôt de 800 000 THB pour le visa retraite."},
            {"title": "Souscrire une assurance santé", "desc": "Obligatoire pour les visas retraite et LTR. Prestataires : Pacific Cross, BUPA Thaïlande, AXA. Budget : 15 000–60 000 ฿/an."},
            {"title": "Renouvellement annuel et rapport 90 jours", "desc": "Renouvelez votre visa chaque année au bureau de l'Immigration. Effectuez des déclarations tous les 90 jours en personne, par courrier ou en ligne."},
        ],
        "housing_title": "Logement",
        "housing_text": "Studio à Bangkok : 8 000–15 000 ฿/mois. 1 pièce à Chiang Mai : 6 000–12 000 ฿/mois. Appartement à Phuket : 12 000–25 000 ฿/mois. Les étrangers ne peuvent pas posséder de terrain mais peuvent acheter un appartement en copropriété.",
        "banking_title": "Banque",
        "banking_text": "Principales banques : Kasikorn (KBank), Bangkok Bank, SCB. Ouverture de compte avec visa Non-Immigrant + passeport. Services en ligne disponibles en anglais. Wise et Revolut populaires pour les virements internationaux.",
        "health_title": "Santé",
        "health_text": "Excellents hôpitaux privés (Bumrungrad, BNH, Samitivej) avec personnel anglophone. Assurance santé privée obligatoire pour la plupart des visas longue durée. Coûts bien inférieurs à ceux de l'Europe.",
        "cost_title": "Coût de la vie",
        "cost_text": "Budget : 30 000–40 000 ฿/mois (770–1 030 €). Confortable : 60 000–90 000 ฿/mois. Luxe : 120 000 ฿+/mois. Chiang Mai est moins cher que Bangkok ou Phuket.",
        "faq_title": "Questions fréquentes",
        "faq": [
            ("Les étrangers peuvent-ils travailler en Thaïlande ?", "Oui, avec un permis de travail. Les télétravailleurs peuvent utiliser le visa LTR pour travailler légalement pour un employeur étranger sans permis de travail thaïlandais."),
            ("Quel est le revenu minimum pour le visa retraite ?", "Il faut justifier de 800 000 THB (~22 000 $) en banque thaïlandaise, OU d'un revenu/pension mensuel de 65 000 THB (~1 700 €), ou d'une combinaison équivalente."),
            ("Puis-je emmener mon conjoint ?", "Oui. Votre conjoint peut demander un visa Non-Immigrant O à titre de dépendant. Il devra effectuer les déclarations 90 jours et les renouvellements annuels."),
            ("La Thaïlande est-elle sûre pour les expatriés ?", "Oui, la Thaïlande est généralement sûre. La petite criminalité existe dans les zones touristiques. Certaines régions peuvent être touchées par des inondations."),
            ("Faut-il parler thaï ?", "Non, dans les grandes villes et zones touristiques. L'anglais est largement parlé à Bangkok, Chiang Mai et Phuket. Apprendre quelques bases est apprécié."),
        ],
    },
    "es": {
        "title": "Guía Expatriados Tailandia 2026 — Vivir en Tailandia | eVisa-Card.com",
        "meta_desc": "Guía completa para expatriados en Tailandia 2026. Opciones de visa, proceso de residencia, vivienda, banca, salud y coste de vida.",
        "h1": "Guía Expatriados: Vivir en Tailandia 2026",
        "breadcrumb": "Guía Expatriados Tailandia",
        "intro": "Tailandia es uno de los principales destinos para expatriados del mundo, atrayendo a jubilados, nómadas digitales y familias por su clima cálido, bajo costo de vida y cultura acogedora. Esta guía te explica todo lo que necesitas saber para mudarte a Tailandia en 2026.",
        "facts_title": "Tailandia de un vistazo",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Bangkok</div><div class="col-md-3 col-6"><strong>Moneda</strong><br/>Baht tailandés (THB)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Tailandés</div><div class="col-md-3 col-6"><strong>Costo de vida</strong><br/>Bajo–Medio</div>',
        "visa_section_title": "Opciones de Visa y Residencia",
        "visa_section_text": "Tailandia ofrece varias opciones para estadías largas: Visa de Turista (60 días, prorrogable), Visa No Inmigrante O-A de Jubilación (1 año renovable, para mayores de 50), Thailand Elite Visa (5–20 años, premium), Visa LTR para profesionales y nómadas digitales.",
        "visa_link_text": "→ Guía completa de visas para Tailandia",
        "steps_title": "Paso a Paso: Cómo Mudarse a Tailandia",
        "steps": [
            {"title": "Elegir el tipo de visa", "desc": "Determina si calificas para la visa de jubilación O-A (50+, prueba de ingresos/ahorros), la Visa LTR (trabajo remoto, ingresos ≥ $80k/año) o el Thailand Elite. La mayoría empieza con visa de turista."},
            {"title": "Reunir los documentos requeridos", "desc": "Pasaporte vigente (+6 meses), fotos de pasaporte, estados de cuenta (800,000 THB en banco tailandés para jubilación o prueba de $80k para LTR), seguro médico, certificado médico."},
            {"title": "Solicitar en la embajada tailandesa", "desc": "Presenta tu solicitud de visa en la embajada tailandesa más cercana. Tiempo de procesamiento: 3–5 días hábiles."},
            {"title": "Llegar y registrar tu dirección", "desc": "Dentro de las 24 horas de llegar, notifica tu alojamiento. Tu arrendador debe presentar el formulario TM.30. Recibirás la tarjeta de llegada TM.6."},
            {"title": "Abrir una cuenta bancaria tailandesa", "desc": "Abre una cuenta en Kasikorn Bank (KBank) o Bangkok Bank. Necesario para el depósito de 800,000 THB del visado de jubilación."},
            {"title": "Contratar seguro médico", "desc": "Obligatorio para visas de jubilación y LTR. Proveedores: Pacific Cross, BUPA Tailandia, AXA. Presupuesto: 15,000–60,000 ฿/año."},
            {"title": "Renovación anual e informe 90 días", "desc": "Renueva tu visa cada año en la oficina de Inmigración local. Presenta informes cada 90 días en persona, por correo o en línea."},
        ],
        "housing_title": "Vivienda",
        "housing_text": "Estudio en Bangkok: 8,000–15,000 ฿/mes. 1 habitación en Chiang Mai: 6,000–12,000 ฿/mes. Condo en Phuket: 12,000–25,000 ฿/mes. Los extranjeros no pueden poseer terrenos pero sí apartamentos (cuota 49% por edificio).",
        "banking_title": "Banca",
        "banking_text": "Principales bancos: Kasikorn (KBank), Bangkok Bank, SCB. Apertura con visa No Inmigrante + pasaporte. Banca en línea disponible en inglés. Wise y Revolut populares para transferencias internacionales.",
        "health_title": "Salud",
        "health_text": "Excelentes hospitales privados (Bumrungrad, BNH, Samitivej) con personal anglófono. Seguro médico privado obligatorio para la mayoría de visas de larga estancia. Costos significativamente menores que en Occidente.",
        "cost_title": "Costo de Vida",
        "cost_text": "Presupuesto: 30,000–40,000 ฿/mes (~$850–$1,100). Cómodo: 60,000–90,000 ฿/mes. Lujo: 120,000+ ฿/mes. Chiang Mai es más barato que Bangkok o Phuket.",
        "faq_title": "Preguntas Frecuentes",
        "faq": [
            ("¿Pueden trabajar los extranjeros en Tailandia?", "Sí, con permiso de trabajo. Los trabajadores remotos pueden usar la Visa LTR para trabajar legalmente para empleadores extranjeros sin permiso tailandés."),
            ("¿Cuál es el ingreso mínimo para la visa de jubilación?", "Se requieren 800,000 THB (~$22,000) en banco tailandés, O ingresos/pensión mensuales de 65,000 THB (~$1,800), o una combinación equivalente."),
            ("¿Puedo traer a mi cónyuge?", "Sí. Tu cónyuge puede solicitar una visa No Inmigrante O como dependiente. Deberá hacer informes de 90 días y renovaciones anuales."),
            ("¿Es Tailandia segura para expatriados?", "En general sí. Existe delincuencia menor en zonas turísticas. Algunas regiones pueden verse afectadas por inundaciones."),
            ("¿Es necesario hablar tailandés?", "No en grandes ciudades y zonas turísticas. El inglés se habla ampliamente en Bangkok, Chiang Mai y Phuket."),
        ],
    },
    "pt": {
        "title": "Guia Expatriados Tailândia 2026 — Viver na Tailândia | eVisa-Card.com",
        "meta_desc": "Guia completo para expatriados na Tailândia 2026. Opções de visto, processo de residência, moradia, banco, saúde e custo de vida.",
        "h1": "Guia Expatriados: Viver na Tailândia 2026",
        "breadcrumb": "Guia Expatriados Tailândia",
        "intro": "A Tailândia é um dos principais destinos para expatriados no mundo, atraindo aposentados, nômades digitais e famílias pelo clima quente, custo de vida acessível e cultura acolhedora. Este guia explica tudo o que você precisa saber para se mudar para a Tailândia em 2026.",
        "facts_title": "Tailândia em Resumo",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Bangcoc</div><div class="col-md-3 col-6"><strong>Moeda</strong><br/>Baht tailandês (THB)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Tailandês</div><div class="col-md-3 col-6"><strong>Custo de vida</strong><br/>Baixo–Médio</div>',
        "visa_section_title": "Opções de Visto e Residência",
        "visa_section_text": "A Tailândia oferece várias opções para longa estadia: Visto de Turista (60 dias, prorrogável), Visto Não-Imigrante O-A de Aposentadoria (1 ano renovável, para maiores de 50), Thailand Elite Visa (5–20 anos, premium), Visto LTR para profissionais e nômades digitais.",
        "visa_link_text": "→ Guia completo de vistos para a Tailândia",
        "steps_title": "Passo a Passo: Como se Mudar para a Tailândia",
        "steps": [
            {"title": "Escolher o tipo de visto", "desc": "Verifique se você se qualifica para o visto de aposentadoria O-A (50+, comprovante de renda/poupança), Visto LTR (trabalho remoto, renda ≥ $80k/ano) ou Thailand Elite. A maioria começa com visto de turista."},
            {"title": "Reunir os documentos necessários", "desc": "Passaporte válido (+6 meses), fotos, extratos bancários (800.000 THB em banco tailandês para aposentadoria ou prova de $80k para LTR), seguro saúde, atestado médico."},
            {"title": "Solicitar na embaixada tailandesa", "desc": "Apresente seu pedido de visto na embaixada tailandesa mais próxima. Prazo de processamento: 3–5 dias úteis."},
            {"title": "Chegar e registrar seu endereço", "desc": "Dentro de 24 horas após a chegada, notifique sua acomodação. Seu proprietário deve registrar o formulário TM.30. Você receberá o cartão de chegada TM.6."},
            {"title": "Abrir conta bancária tailandesa", "desc": "Abra uma conta no Kasikorn Bank (KBank) ou Bangkok Bank. Necessário para o depósito de 800.000 THB do visto de aposentadoria."},
            {"title": "Contratar seguro saúde", "desc": "Obrigatório para vistos de aposentadoria e LTR. Fornecedores: Pacific Cross, BUPA Tailândia, AXA. Orçamento: 15.000–60.000 ฿/ano."},
            {"title": "Renovação anual e relatório 90 dias", "desc": "Renove seu visto anualmente no escritório de Imigração local. Envie relatórios a cada 90 dias pessoalmente, por correio ou online."},
        ],
        "housing_title": "Moradia",
        "housing_text": "Estúdio em Bangkok: 8.000–15.000 ฿/mês. 1 quarto em Chiang Mai: 6.000–12.000 ฿/mês. Condomínio em Phuket: 12.000–25.000 ฿/mês. Estrangeiros não podem possuir terrenos, mas podem comprar apartamentos.",
        "banking_title": "Banco",
        "banking_text": "Principais bancos: Kasikorn (KBank), Bangkok Bank, SCB. Abertura com visto Não-Imigrante + passaporte. Internet banking em inglês. Wise e Revolut populares para transferências internacionais.",
        "health_title": "Saúde",
        "health_text": "Excelentes hospitais privados (Bumrungrad, BNH, Samitivej) com equipe anglófona. Seguro saúde privado obrigatório para a maioria dos vistos de longa estadia. Custos muito menores que no Brasil ou Europa.",
        "cost_title": "Custo de Vida",
        "cost_text": "Básico: 30.000–40.000 ฿/mês (~R$6.500–R$8.500). Confortável: 60.000–90.000 ฿/mês. Luxo: 120.000+ ฿/mês. Chiang Mai é mais barato que Bangkok ou Phuket.",
        "faq_title": "Perguntas Frequentes",
        "faq": [
            ("Estrangeiros podem trabalhar na Tailândia?", "Sim, com permissão de trabalho. Trabalhadores remotos podem usar o Visto LTR para trabalhar legalmente para empregadores estrangeiros sem permissão tailandesa."),
            ("Qual é a renda mínima para o visto de aposentadoria?", "É necessário comprovar 800.000 THB (~R$170.000) em banco tailandês, OU renda/pensão mensal de 65.000 THB (~R$14.000), ou combinação equivalente."),
            ("Posso levar meu cônjuge?", "Sim. Seu cônjuge pode solicitar visto Não-Imigrante O como dependente e precisará fazer relatórios de 90 dias e renovações anuais."),
            ("A Tailândia é segura para expatriados?", "Em geral sim. Existe pequena criminalidade em zonas turísticas. Algumas regiões podem ser afetadas por enchentes."),
            ("É necessário falar tailandês?", "Não nas grandes cidades e áreas turísticas. O inglês é amplamente falado em Bangkok, Chiang Mai e Phuket."),
        ],
    },
},

"expat-guide-portugal": {
    "iso": "pt",
    "visa_slug": "portugal",
    "en": {
        "title": "Expat Guide Portugal 2026 — How to Live in Portugal | eVisa-Card.com",
        "meta_desc": "Complete expat guide Portugal 2026. D7 Visa, NHR tax regime, step-by-step residency, housing in Lisbon & Porto, banking, healthcare, cost of living.",
        "h1": "Expat Guide: Living in Portugal 2026",
        "breadcrumb": "Expat Guide Portugal",
        "intro": "Portugal has become one of Europe's most sought-after expat destinations, offering a D7 Passive Income Visa, Golden Visa, affordable cost of living compared to Western Europe, mild climate, safety, and the NHR tax regime for significant tax savings. This guide covers everything you need to relocate to Portugal.",
        "facts_title": "Portugal at a Glance",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Lisbon</div><div class="col-md-3 col-6"><strong>Currency</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Language</strong><br/>Portuguese</div><div class="col-md-3 col-6"><strong>Schengen Area</strong><br/>Yes</div>',
        "visa_section_title": "Visa & Residency Options",
        "visa_section_text": "Key options: D7 Passive Income Visa (for retirees/remote workers, €760/month income), Digital Nomad Visa (€3,040/month income), D2 Entrepreneur Visa, Golden Visa (investment, path to citizenship). EU/EEA citizens register at the local council (Câmara Municipal) without a visa.",
        "visa_link_text": "→ Full Portugal Visa Requirements & Application Guide",
        "steps_title": "Step-by-Step: How to Move to Portugal",
        "steps": [
            {"title": "Obtain a Portuguese NIF (tax number)", "desc": "Apply at any Finanças office or Portuguese consulate. You can use a fiscal representative initially. The NIF is required to open a bank account and sign a lease."},
            {"title": "Apply for your D7 or Digital Nomad visa", "desc": "Submit at a Portuguese consulate: passport, proof of income (€760+/month for D7), health insurance, criminal background check, accommodation proof, passport photos."},
            {"title": "Open a Portuguese bank account", "desc": "Open with Millennium BCP, BPI, Santander Portugal, or Caixa Geral. You'll need your NIF, passport, and visa. Some banks offer non-resident accounts (NHR applicants)."},
            {"title": "Arrive and get your AIMA appointment", "desc": "Book an appointment with AIMA (Agency for Integration, Migration and Asylum) to convert your visa to a residence permit. The appointment backlog can be 3–6 months — book immediately upon arrival."},
            {"title": "Apply for NHR tax status", "desc": "Apply for Non-Habitual Resident status within 31 March of the year following your first tax registration. NHR provides 10 years of flat 20% tax rate on Portuguese income and exemptions on foreign income."},
            {"title": "Register with local health centre (Centro de Saúde)", "desc": "Register at your local SNS (National Health Service) health centre with your residence permit. Public healthcare is free or very low-cost for registered residents."},
            {"title": "Obtain Portuguese driving licence", "desc": "EU licence holders: no exchange needed. Non-EU: exchange your licence within 90 days of residency or take Portuguese driving test."},
        ],
        "housing_title": "Housing",
        "housing_text": "Lisbon 1-bed: €1,200–€1,800/month. Porto 1-bed: €900–€1,400/month. Algarve villa: €900–€2,500/month. Silver Coast / interior towns: €500–€800/month. Prices rose sharply post-2020 — book accommodation before arriving.",
        "banking_title": "Banking",
        "banking_text": "Major banks: Millennium BCP, BPI, Santander, Novobanco. Open with NIF + passport. Revolut and N26 popular among expats. Wise essential for receiving international transfers.",
        "health_title": "Healthcare",
        "health_text": "SNS public healthcare for registered residents (utentes). Excellent private hospitals (CUF, HPA). Private health insurance averages €50–€150/month. EU EHIC card valid for tourists transitioning.",
        "cost_title": "Cost of Living",
        "cost_text": "Lisbon: €2,000–€3,000/month couple. Porto: €1,700–€2,500/month. Algarve/interior: €1,200–€2,000/month. Portugal remains 20–30% cheaper than France, Germany or UK.",
        "faq_title": "Frequently Asked Questions",
        "faq": [
            ("What is the D7 Visa minimum income?", "€760/month for the main applicant (Portugal's minimum wage), plus €380 for a spouse and €228 per dependent child. Proof via pension, rental income, dividends or remote employment contract."),
            ("How long does the AIMA appointment backlog take?", "In 2025–2026, AIMA appointments can take 3–9 months. Apply online immediately after arrival and get a document confirming your application (to show authorities if needed)."),
            ("Can I buy property in Portugal?", "Yes, with no restrictions. You'll need a NIF and Portuguese bank account. Notarial fees and property transfer tax (IMT) apply. Prices in Lisbon/Porto are €4,000–€8,000/m²."),
            ("Is Portugal safe?", "Yes — Portugal consistently ranks among the world's safest countries (Global Peace Index top 10). Low crime, stable politics, friendly population."),
            ("Can I apply for citizenship?", "Yes, after 5 years of legal residency. You need A2 Portuguese language proficiency, clean criminal record, and proof of community ties."),
        ],
    },
    "fr": {
        "title": "Guide Expatriation Portugal 2026 — Vivre au Portugal | eVisa-Card.com",
        "meta_desc": "Guide complet expatriation Portugal 2026. Visa D7, régime RNH, démarches résidence, logement à Lisbonne et Porto, banque, santé, coût de la vie.",
        "h1": "Guide Expatriation : Vivre au Portugal 2026",
        "breadcrumb": "Guide Expatriation Portugal",
        "intro": "Le Portugal est devenu l'une des destinations expatriées les plus prisées d'Europe, offrant le Visa D7, le régime fiscal RNH (Résident Non Habituel), un coût de la vie abordable, un climat doux et une grande sécurité. Ce guide couvre tout ce dont vous avez besoin pour vous installer au Portugal.",
        "facts_title": "Le Portugal en bref",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capitale</strong><br/>Lisbonne</div><div class="col-md-3 col-6"><strong>Monnaie</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Langue</strong><br/>Portugais</div><div class="col-md-3 col-6"><strong>Espace Schengen</strong><br/>Oui</div>',
        "visa_section_title": "Options de visa et résidence",
        "visa_section_text": "Principales options : Visa D7 Revenus Passifs (retraités/télétravailleurs, revenus ≥ 760 €/mois), Visa Nomade Numérique (3 040 €/mois), Visa D2 Entrepreneur, Golden Visa (investissement). Les citoyens UE/EEE s'inscrivent directement à la Câmara Municipal.",
        "visa_link_text": "→ Guide complet des visas Portugal",
        "steps_title": "Étapes pour s'installer au Portugal",
        "steps": [
            {"title": "Obtenir un NIF (numéro fiscal portugais)", "desc": "Déposez votre demande dans un bureau des Finanças ou au consulat portugais. Indispensable pour ouvrir un compte bancaire et signer un bail."},
            {"title": "Déposer sa demande de visa D7 ou Nomade Numérique", "desc": "Déposez au consulat : passeport, justificatif de revenus (760 €+/mois pour D7), assurance santé, casier judiciaire, justificatif d'hébergement, photos."},
            {"title": "Ouvrir un compte bancaire portugais", "desc": "Ouvrez un compte chez Millennium BCP, BPI, Santander Portugal ou Caixa Geral. Nécessite NIF + passeport + visa."},
            {"title": "Arriver et prendre un RDV AIMA", "desc": "Réservez un RDV auprès de l'AIMA (anciennement SEF) pour convertir votre visa en titre de séjour. Délais actuels : 3–9 mois — réservez dès l'arrivée."},
            {"title": "Demander le statut RNH (Résident Non Habituel)", "desc": "À déposer avant le 31 mars de l'année suivant votre première inscription fiscale. Le RNH offre 10 ans de taux flat 20% sur revenus portugais et exonérations sur revenus étrangers."},
            {"title": "S'inscrire au centre de santé local (Centro de Saúde)", "desc": "Inscrivez-vous avec votre titre de séjour. Les soins publics sont gratuits ou très peu onéreux pour les résidents inscrits au SNS."},
            {"title": "Permis de conduire", "desc": "Les titulaires d'un permis UE n'ont pas à l'échanger. Les non-UE doivent l'échanger dans les 90 jours suivant l'établissement de la résidence."},
        ],
        "housing_title": "Logement",
        "housing_text": "Lisbonne 1 pièce : 1 200–1 800 €/mois. Porto 1 pièce : 900–1 400 €/mois. Algarve villa : 900–2 500 €/mois. Côte d'Argent/intérieur : 500–800 €/mois. Les prix ont fortement augmenté depuis 2020.",
        "banking_title": "Banque",
        "banking_text": "Principales banques : Millennium BCP, BPI, Santander, Novobanco. Ouverture avec NIF + passeport. Revolut et N26 très populaires chez les expatriés. Wise essentiel pour les virements internationaux.",
        "health_title": "Santé",
        "health_text": "Soins publics SNS pour les résidents inscrits. Excellentes cliniques privées (CUF, HPA). Assurance santé privée : 50–150 €/mois. La Carte Européenne d'Assurance Maladie (CEAM) est valide pendant la transition.",
        "cost_title": "Coût de la vie",
        "cost_text": "Lisbonne : 2 000–3 000 €/mois pour un couple. Porto : 1 700–2 500 €/mois. Algarve/intérieur : 1 200–2 000 €/mois. Le Portugal reste 20–30% moins cher que la France ou l'Allemagne.",
        "faq_title": "Questions fréquentes",
        "faq": [
            ("Quel est le revenu minimum pour le visa D7 ?", "760 €/mois pour le demandeur principal (salaire minimum portugais), + 380 € pour un conjoint et 228 € par enfant à charge. Justifiable par retraite, loyers, dividendes ou contrat de télétravail."),
            ("Combien de temps faut-il attendre pour un RDV AIMA ?", "En 2025–2026, les RDV AIMA peuvent prendre 3–9 mois. Postulez en ligne dès l'arrivée et conservez la confirmation de dépôt."),
            ("Peut-on acheter un bien immobilier au Portugal ?", "Oui, sans restriction. Un NIF et un compte bancaire portugais sont nécessaires. Des frais notariaux et une taxe de mutation (IMT) s'appliquent."),
            ("Le Portugal est-il sûr ?", "Oui, le Portugal figure régulièrement dans le top 10 mondial des pays les plus sûrs (Global Peace Index). Faible criminalité, stabilité politique."),
            ("Peut-on demander la nationalité portugaise ?", "Oui, après 5 ans de résidence légale, avec niveau A2 de portugais et casier judiciaire vierge."),
        ],
    },
    "es": {
        "title": "Guía Expatriados Portugal 2026 — Vivir en Portugal | eVisa-Card.com",
        "meta_desc": "Guía completa expatriados Portugal 2026. Visa D7, régimen RNH, residencia, vivienda en Lisboa y Oporto, banco, salud, coste de vida.",
        "h1": "Guía Expatriados: Vivir en Portugal 2026",
        "breadcrumb": "Guía Expatriados Portugal",
        "intro": "Portugal se ha convertido en uno de los destinos expatriados más buscados de Europa, ofreciendo el Visa D7, el régimen fiscal RNH, costo de vida asequible, clima suave y seguridad. Esta guía cubre todo lo que necesitas para mudarte a Portugal.",
        "facts_title": "Portugal de un vistazo",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Lisboa</div><div class="col-md-3 col-6"><strong>Moneda</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Portugués</div><div class="col-md-3 col-6"><strong>Espacio Schengen</strong><br/>Sí</div>',
        "visa_section_title": "Opciones de Visa y Residencia",
        "visa_section_text": "Opciones principales: Visa D7 de Ingresos Pasivos (para jubilados/trabajadores remotos, ingresos ≥ €760/mes), Visa Nómada Digital (€3,040/mes), Visa D2 Emprendedor, Golden Visa (inversión). Los ciudadanos UE/EEE se registran directamente en el ayuntamiento.",
        "visa_link_text": "→ Guía completa de visas para Portugal",
        "steps_title": "Paso a Paso: Cómo Mudarse a Portugal",
        "steps": [
            {"title": "Obtener un NIF (número fiscal portugués)", "desc": "Solicítalo en cualquier oficina de Finanças o en el consulado portugués. Imprescindible para abrir cuenta bancaria y firmar contrato de arrendamiento."},
            {"title": "Solicitar tu Visa D7 o Nómada Digital", "desc": "Presenta en el consulado: pasaporte, prueba de ingresos (€760+/mes para D7), seguro médico, antecedentes penales, prueba de alojamiento, fotos."},
            {"title": "Abrir una cuenta bancaria portuguesa", "desc": "Abre cuenta en Millennium BCP, BPI, Santander Portugal o Caixa Geral. Necesitas NIF + pasaporte + visa."},
            {"title": "Llegar y pedir cita en AIMA", "desc": "Reserva cita en AIMA (antes SEF) para convertir tu visa en permiso de residencia. Los tiempos de espera actuales son de 3–9 meses — reserva al llegar."},
            {"title": "Solicitar el estatus RNH", "desc": "Solicita antes del 31 de marzo del año siguiente a tu primera inscripción fiscal. El RNH ofrece 10 años de tipo fijo del 20% sobre ingresos portugueses y exenciones sobre ingresos extranjeros."},
            {"title": "Registrarse en el centro de salud local", "desc": "Regístrate con tu permiso de residencia. La atención médica pública es gratuita o de muy bajo costo para los residentes registrados en el SNS."},
            {"title": "Carnet de conducir", "desc": "Los titulares de carnet UE no necesitan canjearlo. Los no comunitarios deben canjearlo en los 90 días desde el establecimiento de la residencia."},
        ],
        "housing_title": "Vivienda",
        "housing_text": "Lisboa 1 habitación: €1,200–€1,800/mes. Oporto 1 hab.: €900–€1,400/mes. Algarve villa: €900–€2,500/mes. Costa de Plata/interior: €500–€800/mes. Los precios han subido considerablemente desde 2020.",
        "banking_title": "Banca",
        "banking_text": "Principales bancos: Millennium BCP, BPI, Santander, Novobanco. Apertura con NIF + pasaporte. Revolut y N26 muy populares entre expatriados. Wise esencial para transferencias internacionales.",
        "health_title": "Salud",
        "health_text": "Atención pública SNS para residentes registrados. Excelentes clínicas privadas (CUF, HPA). Seguro médico privado: €50–€150/mes. La Tarjeta Sanitaria Europea es válida durante la transición.",
        "cost_title": "Costo de Vida",
        "cost_text": "Lisboa: €2,000–€3,000/mes (pareja). Oporto: €1,700–€2,500/mes. Algarve/interior: €1,200–€2,000/mes. Portugal sigue siendo un 20–30% más barato que Francia, Alemania o el Reino Unido.",
        "faq_title": "Preguntas Frecuentes",
        "faq": [
            ("¿Cuál es el ingreso mínimo para la Visa D7?", "€760/mes para el solicitante principal, + €380 para cónyuge y €228 por hijo dependiente. Demostrable con pensión, alquileres, dividendos o contrato de trabajo remoto."),
            ("¿Cuánto tiempo tarda la cita AIMA?", "En 2025–2026, las citas AIMA pueden tardar 3–9 meses. Solicita en línea al llegar y guarda el comprobante de presentación."),
            ("¿Se puede comprar propiedad en Portugal?", "Sí, sin restricciones. Se necesitan NIF y cuenta bancaria portuguesa. Se aplican gastos notariales e impuesto de transmisión (IMT)."),
            ("¿Es seguro Portugal?", "Sí, Portugal aparece regularmente entre los 10 países más seguros del mundo (Global Peace Index). Baja criminalidad y estabilidad política."),
            ("¿Se puede pedir la nacionalidad portuguesa?", "Sí, tras 5 años de residencia legal, con nivel A2 de portugués y antecedentes penales limpios."),
        ],
    },
    "pt": {
        "title": "Guia Expatriados Portugal 2026 — Viver em Portugal | eVisa-Card.com",
        "meta_desc": "Guia completo para expatriados em Portugal 2026. Visto D7, regime RNH, residência, moradia em Lisboa e Porto, banco, saúde, custo de vida.",
        "h1": "Guia Expatriados: Viver em Portugal 2026",
        "breadcrumb": "Guia Expatriados Portugal",
        "intro": "Portugal tornou-se um dos destinos mais procurados por expatriados na Europa, oferecendo o Visto D7, o regime fiscal RNH, custo de vida acessível comparado à Europa Ocidental, clima ameno e segurança. Este guia cobre tudo o que você precisa para se mudar para Portugal.",
        "facts_title": "Portugal em Resumo",
        "facts_html": '<div class="col-md-3 col-6"><strong>Capital</strong><br/>Lisboa</div><div class="col-md-3 col-6"><strong>Moeda</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Português</div><div class="col-md-3 col-6"><strong>Espaço Schengen</strong><br/>Sim</div>',
        "visa_section_title": "Opções de Visto e Residência",
        "visa_section_text": "Principais opções: Visto D7 de Renda Passiva (para aposentados/trabalhadores remotos, renda ≥ €760/mês), Visto Nômade Digital (€3.040/mês), Visto D2 Empreendedor, Golden Visa (investimento). Cidadãos UE/EEE registram-se diretamente na Câmara Municipal.",
        "visa_link_text": "→ Guia completo de vistos para Portugal",
        "steps_title": "Passo a Passo: Como se Mudar para Portugal",
        "steps": [
            {"title": "Obter um NIF (número fiscal português)", "desc": "Solicite em qualquer escritório da Finanças ou no consulado português. Imprescindível para abrir conta bancária e assinar contrato de arrendamento."},
            {"title": "Solicitar o Visto D7 ou Nômade Digital", "desc": "Apresente no consulado: passaporte, comprovante de renda (€760+/mês para D7), seguro saúde, antecedentes criminais, comprovante de hospedagem, fotos."},
            {"title": "Abrir conta bancária portuguesa", "desc": "Abra conta no Millennium BCP, BPI, Santander Portugal ou Caixa Geral. Necessário: NIF + passaporte + visto."},
            {"title": "Chegar e agendar na AIMA", "desc": "Agende consulta na AIMA (antes SEF) para converter o visto em título de residência. Os atrasos atuais são de 3–9 meses — agende imediatamente após a chegada."},
            {"title": "Solicitar o status RNH (Residente Não Habitual)", "desc": "Solicite antes de 31 de março do ano seguinte ao seu primeiro registro fiscal. O RNH oferece 10 anos de taxa fixa de 20% sobre rendimentos portugueses e isenções sobre rendimentos estrangeiros."},
            {"title": "Inscrever-se no centro de saúde local", "desc": "Inscreva-se com seu título de residência. A atenção médica pública é gratuita ou de baixíssimo custo para residentes inscritos no SNS."},
            {"title": "Carteira de motorista", "desc": "Titulares de carteira UE não precisam trocar. Não comunitários devem trocar nos 90 dias após o estabelecimento da residência."},
        ],
        "housing_title": "Moradia",
        "housing_text": "Lisboa 1 quarto: €1.200–€1.800/mês. Porto 1 quarto: €900–€1.400/mês. Algarve villa: €900–€2.500/mês. Costa de Prata/interior: €500–€800/mês. Os preços subiram muito desde 2020.",
        "banking_title": "Banco",
        "banking_text": "Principais bancos: Millennium BCP, BPI, Santander, Novobanco. Abertura com NIF + passaporte. Revolut e N26 muito populares entre expatriados. Wise essencial para transferências internacionais.",
        "health_title": "Saúde",
        "health_text": "SNS público para residentes cadastrados. Excelentes clínicas privadas (CUF, HPA). Seguro saúde privado: €50–€150/mês. O Cartão Europeu de Seguro de Doença é válido durante a transição.",
        "cost_title": "Custo de Vida",
        "cost_text": "Lisboa: €2.000–€3.000/mês (casal). Porto: €1.700–€2.500/mês. Algarve/interior: €1.200–€2.000/mês. Portugal continua sendo 20–30% mais barato que França, Alemanha ou Reino Unido.",
        "faq_title": "Perguntas Frequentes",
        "faq": [
            ("Qual é a renda mínima para o Visto D7?", "€760/mês para o requerente principal, + €380 para cônjuge e €228 por filho dependente. Comprovável por aposentadoria, aluguéis, dividendos ou contrato de trabalho remoto."),
            ("Quanto tempo leva o agendamento AIMA?", "Em 2025–2026, os agendamentos AIMA podem levar 3–9 meses. Solicite online ao chegar e guarde o comprovante de apresentação."),
            ("Posso comprar imóvel em Portugal?", "Sim, sem restrições. São necessários NIF e conta bancária portuguesa. Aplicam-se taxas notariais e imposto de transmissão (IMT)."),
            ("Portugal é seguro?", "Sim, Portugal aparece regularmente entre os 10 países mais seguros do mundo (Global Peace Index). Baixa criminalidade e estabilidade política."),
            ("Posso pedir a nacionalidade portuguesa?", "Sim, após 5 anos de residência legal, com nível A2 de português e antecedentes criminais limpos."),
        ],
    },
},

}  # end COUNTRIES

# ─── GENERATE PAGES ──────────────────────────────────────────────────────────
created = 0
for slug, data in COUNTRIES.items():
    for lang in ["en", "fr", "es", "pt"]:
        if lang not in data:
            continue
        out_dir = os.path.join(WWW, lang)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{slug}.html")
        html = make_page(lang, slug, data)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        created += 1
        print(f"Created: {lang}/{slug}.html")

print(f"\nTotal pages created: {created}")
