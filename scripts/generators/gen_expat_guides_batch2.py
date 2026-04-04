#!/usr/bin/env python3
"""Batch 2: Spain, Mexico, Vietnam, Malaysia, Japan, UAE, Colombia expat guides."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

LANG_FLAGS = {"en":"fi-gb","fr":"fi-fr","es":"fi-es","pt":"fi-br"}
LANG_NAMES = {"en":"English","fr":"Français","es":"Español","pt":"Português"}
LANG_LABELS = {
    "en":{"home":"Home","dest":"Destinations","about":"About","blog":"Blog","guides":"Guides"},
    "fr":{"home":"Accueil","dest":"Destinations","about":"À propos","blog":"Blog","guides":"Guides"},
    "es":{"home":"Inicio","dest":"Destinos","about":"Sobre Nosotros","blog":"Blog","guides":"Guías"},
    "pt":{"home":"Início","dest":"Destinos","about":"Sobre Nós","blog":"Blog","guides":"Guias"},
}
FOOTER_COPY = {
    "en":"© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform",
    "fr":"© 2026 eVisa-Card.com — Plateforme mondiale d'information eVisa",
    "es":"© 2026 eVisa-Card.com — Plataforma global de información eVisa",
    "pt":"© 2026 eVisa-Card.com — Plataforma global de informações eVisa",
}
FOOTER_LEGAL = {
    "en":('/en/legal-notice.html','Legal Notice','/en/disclaimer.html','Disclaimer'),
    "fr":('/fr/mentions-legales.html','Mentions légales','/fr/disclaimer.html','Disclaimer'),
    "es":('/es/aviso-legal.html','Aviso Legal','/es/disclaimer.html','Disclaimer'),
    "pt":('/pt/aviso-legal.html','Aviso Legal','/pt/disclaimer.html','Disclaimer'),
}

def make_navbar(lang, slug):
    L = LANG_LABELS[lang]
    sw = ""
    for tl in ["en","fr","es","pt"]:
        active = ' active' if tl == lang else ''
        url = f"/{tl}/{slug}.html"
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
    visa_slug = data.get("visa_slug","")
    visa_link = f'<a href="/{lang}/visa-{visa_slug}.html">' if visa_slug else '<a href="../destination.html">'

    steps_html = ""
    for i,step in enumerate(d["steps"],1):
        steps_html += f"""
        <div class="step-item d-flex mb-4">
            <div class="step-number mr-3" style="min-width:40px;height:40px;background:#f15d30;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:18px;">{i}</div>
            <div><h3 style="font-size:18px;margin-bottom:6px;">{step['title']}</h3><p style="margin:0;color:#555;">{step['desc']}</p></div>
        </div>"""

    faq_items = ""
    schema_faq = ""
    for q,a in d["faq"]:
        faq_items += f'<div class="mb-4"><h3 style="font-size:17px;color:#1d2d50;">❓ {q}</h3><p style="color:#555;">{a}</p></div>'
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
    <div class="row mb-5"><div class="col-md-12">
        <p style="font-size:17px;color:#444;">{d['intro']}</p>
        <p style="font-size:13px;color:#999;">Last updated: March 2026 — <em>Editorial Team, eVisa-Card.com</em></p>
    </div></div>
    <div class="row mb-5"><div class="col-md-12">
        <div style="background:#f8f9fc;border-left:4px solid #f15d30;padding:20px 25px;border-radius:4px;">
            <h2 style="font-size:20px;margin-bottom:15px;color:#1d2d50;"><span class="fi fi-{iso}" style="margin-right:8px;"></span> {d['facts_title']}</h2>
            <div class="row">{d['facts_html']}</div>
        </div>
    </div></div>
    <div class="row mb-5"><div class="col-md-12">
        <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['visa_section_title']}</h2>
        <p>{d['visa_section_text']}</p>
        <p>{visa_link}{d['visa_link_text']}</a></p>
    </div></div>
    <div class="row mb-5"><div class="col-md-12">
        <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['steps_title']}</h2>
        {steps_html}
    </div></div>
    <div class="row mb-5">
        <div class="col-md-6 mb-4"><div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
            <h3 style="font-size:17px;color:#1d2d50;">🏠 {d['housing_title']}</h3>
            <p style="font-size:14px;color:#555;">{d['housing_text']}</p>
        </div></div>
        <div class="col-md-6 mb-4"><div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
            <h3 style="font-size:17px;color:#1d2d50;">🏦 {d['banking_title']}</h3>
            <p style="font-size:14px;color:#555;">{d['banking_text']}</p>
        </div></div>
        <div class="col-md-6 mb-4"><div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
            <h3 style="font-size:17px;color:#1d2d50;">🏥 {d['health_title']}</h3>
            <p style="font-size:14px;color:#555;">{d['health_text']}</p>
        </div></div>
        <div class="col-md-6 mb-4"><div style="background:#fff;border:1px solid #eee;border-radius:6px;padding:20px;">
            <h3 style="font-size:17px;color:#1d2d50;">💰 {d['cost_title']}</h3>
            <p style="font-size:14px;color:#555;">{d['cost_text']}</p>
        </div></div>
    </div>
    <div class="row mb-5"><div class="col-md-12">
        <h2 style="color:#1d2d50;border-bottom:2px solid #f15d30;padding-bottom:8px;">{d['faq_title']}</h2>
        {faq_items}
    </div></div>
</div>
</section>
{footer}
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body></html>"""

# ─── COUNTRY DATA ─────────────────────────────────────────────────────────────
COUNTRIES = {

"expat-guide-spain": {
    "iso":"es","visa_slug":"spain",
    "en":{
        "title":"Expat Guide Spain 2026 — How to Live in Spain | eVisa-Card.com",
        "meta_desc":"Complete expat guide Spain 2026. Non-Lucrative Visa, Digital Nomad Visa, NIE, step-by-step residency, housing, banking, healthcare.",
        "h1":"Expat Guide: Living in Spain 2026",
        "breadcrumb":"Expat Guide Spain",
        "intro":"Spain remains one of the world's top expat destinations thanks to its Mediterranean climate, vibrant culture, excellent healthcare, high quality of life and relatively affordable cost of living outside major cities. Whether you're retiring, working remotely or starting a business, Spain has a path for you.",
        "facts_title":"Spain at a Glance",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Madrid</div><div class="col-md-3 col-6"><strong>Currency</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Language</strong><br/>Spanish</div><div class="col-md-3 col-6"><strong>Schengen</strong><br/>Yes</div>',
        "visa_section_title":"Visa & Residency Options",
        "visa_section_text":"Key options: Non-Lucrative Visa (NLV) — no work, passive income ≥ €2,400/month; Digital Nomad Visa (Startup Act 2023) — remote work for non-Spanish employers, income ≥ €2,334/month; Golden Visa — property investment ≥ €500k (under review); EU citizens register at local Foreigner's Office (Oficina de Extranjeros).",
        "visa_link_text":"→ Full Spain Visa Requirements Guide",
        "steps_title":"Step-by-Step: How to Move to Spain",
        "steps":[
            {"title":"Apply for your visa","desc":"Non-EU applicants apply at a Spanish consulate. Required: passport, proof of income (€2,400+/month for NLV), private health insurance, criminal background check, proof of accommodation, medical certificate."},
            {"title":"Get your NIE (Foreigners' Identity Number)","desc":"Apply at a Spanish consulate before arrival or at a Foreigners' Office (Oficina de Extranjeros) in Spain. The NIE is required for almost every official transaction: buying property, signing contracts, opening bank accounts."},
            {"title":"Register on the Padrón Municipal","desc":"Register your address at your local town hall (Ayuntamiento). The Padrón is required to access healthcare, schools, and apply for residence permits."},
            {"title":"Open a Spanish bank account","desc":"Open with Santander, BBVA, CaixaBank, or online banks like WISE or Revolut. You'll need your passport and NIE. Some banks require proof of Spanish income."},
            {"title":"Apply for Tarjeta de Identidad de Extranjero (TIE)","desc":"Exchange your long-stay visa for a residence card at the Foreigners' Office within 30 days of arrival. The TIE is your official residence document."},
            {"title":"Register with public healthcare (INSS)","desc":"EU citizens: present your EHIC initially. Non-EU residents: register at the health centre (Centro de Salud) with your TIE and Padrón. Public healthcare is free for registered residents."},
            {"title":"Tax registration (Hacienda)","desc":"Register with the Agencia Tributaria. Spain taxes worldwide income for residents (183+ days/year). The Beckham Law offers a flat 24% tax rate on Spanish income for first 6 years for qualifying workers."},
        ],
        "housing_title":"Housing",
        "housing_text":"Madrid 1-bed: €1,200–€1,800/month. Barcelona 1-bed: €1,300–€2,000/month. Valencia/Alicante: €700–€1,100/month. Interior cities (Seville, Málaga): €700–€1,200/month. Short-term furnished flats common via Idealista, Fotocasa.",
        "banking_title":"Banking",
        "banking_text":"Main banks: Santander, BBVA, CaixaBank, Sabadell. Open with NIE + passport. Revolut and Wise widely used. Many banks offer English-language services in expat areas.",
        "health_title":"Healthcare",
        "health_text":"Excellent public SNS (Sistema Nacional de Salud) for registered residents. World-class private hospitals. Private insurance: €50–€200/month. Sanitas, Adeslas, AXA popular for expats.",
        "cost_title":"Cost of Living",
        "cost_text":"Madrid/Barcelona: €2,500–€4,000/month couple. Valencia/Alicante: €1,800–€2,800/month. Rural inland: €1,200–€2,000/month. Spain is ~25% cheaper than UK, France or Germany.",
        "faq_title":"Frequently Asked Questions",
        "faq":[
            ("What is the Non-Lucrative Visa income requirement?","€2,400/month for the main applicant (2024 figure), plus €600 for each additional family member. Must be passive income: pension, dividends, rental income."),
            ("Can I work in Spain on a Non-Lucrative Visa?","No. The NLV prohibits working in Spain. To work remotely for non-Spanish clients, apply for the Digital Nomad Visa instead."),
            ("How long does it take to get permanent residency?","5 years of continuous legal residency. Spanish citizenship requires 10 years (2 years for citizens of Spanish-speaking countries)."),
            ("Is Spain safe for expats?","Yes — Spain consistently ranks among the safest countries in the world. Low violent crime, excellent infrastructure."),
            ("Do I need to speak Spanish?","Not mandatory, especially in coastal expat areas (Costa del Sol, Costa Blanca). Learning Spanish significantly improves integration and daily life."),
        ],
    },
    "fr":{
        "title":"Guide Expatriation Espagne 2026 — Vivre en Espagne | eVisa-Card.com",
        "meta_desc":"Guide complet expatriation Espagne 2026. Visa Non Lucratif, Nomade Numérique, NIE, résidence, logement, banque, santé.",
        "h1":"Guide Expatriation : Vivre en Espagne 2026",
        "breadcrumb":"Guide Expatriation Espagne",
        "intro":"L'Espagne reste l'une des premières destinations mondiales pour les expatriés grâce à son climat méditerranéen, sa culture vibrante, son système de santé excellent et son coût de la vie relativement abordable hors grandes métropoles.",
        "facts_title":"L'Espagne en bref",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capitale</strong><br/>Madrid</div><div class="col-md-3 col-6"><strong>Monnaie</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Langue</strong><br/>Espagnol</div><div class="col-md-3 col-6"><strong>Schengen</strong><br/>Oui</div>',
        "visa_section_title":"Options de visa et résidence",
        "visa_section_text":"Options principales : Visa Non Lucratif (pas de travail, revenus passifs ≥ 2 400 €/mois), Visa Nomade Numérique (travail à distance pour employeurs non espagnols, revenus ≥ 2 334 €/mois), Golden Visa (investissement ≥ 500 k€). Les citoyens UE s'enregistrent au bureau des étrangers.",
        "visa_link_text":"→ Guide complet des visas Espagne",
        "steps_title":"Étapes pour s'installer en Espagne",
        "steps":[
            {"title":"Déposer sa demande de visa","desc":"Demande au consulat espagnol : passeport, justificatif de revenus (2 400 €+/mois pour NLV), assurance santé privée, casier judiciaire, justificatif d'hébergement, certificat médical."},
            {"title":"Obtenir le NIE (Numéro d'Identification des Étrangers)","desc":"Demande au consulat espagnol avant l'arrivée ou au bureau des étrangers en Espagne. Obligatoire pour presque toutes les démarches officielles."},
            {"title":"S'inscrire au Padrón Municipal","desc":"Inscrivez-vous à votre mairie (Ayuntamiento). Obligatoire pour accéder aux soins de santé, aux écoles et demander un titre de séjour."},
            {"title":"Ouvrir un compte bancaire espagnol","desc":"Ouvrez un compte chez Santander, BBVA ou CaixaBank avec votre passeport et NIE."},
            {"title":"Obtenir la Tarjeta de Identidad de Extranjero (TIE)","desc":"Échangez votre visa de long séjour contre une carte de résident au bureau des étrangers dans les 30 jours suivant l'arrivée."},
            {"title":"S'inscrire aux soins de santé publics","desc":"Citoyens UE : CEAM valide initialement. Résidents non-UE : inscrivez-vous au Centro de Salud avec TIE + Padrón. Soins gratuits pour les résidents inscrits."},
            {"title":"Déclaration fiscale (Hacienda)","desc":"Inscrivez-vous à l'Agencia Tributaria. L'Espagne impose les revenus mondiaux des résidents (183+ jours/an). La Loi Beckham offre un taux forfaitaire de 24% pour 6 ans."},
        ],
        "housing_title":"Logement",
        "housing_text":"Madrid 1 pièce : 1 200–1 800 €/mois. Barcelone : 1 300–2 000 €/mois. Valence/Alicante : 700–1 100 €/mois. Villes intérieures : 700–1 200 €/mois. Sites : Idealista, Fotocasa.",
        "banking_title":"Banque",
        "banking_text":"Principales banques : Santander, BBVA, CaixaBank, Sabadell. Ouverture avec NIE + passeport. Revolut et Wise très utilisés. Services en anglais disponibles dans les zones expatriées.",
        "health_title":"Santé",
        "health_text":"Excellent système public SNS pour les résidents inscrits. Cliniques privées de haute qualité. Assurance privée : 50–200 €/mois (Sanitas, Adeslas, AXA).",
        "cost_title":"Coût de la vie",
        "cost_text":"Madrid/Barcelone : 2 500–4 000 €/mois pour un couple. Valence/Alicante : 1 800–2 800 €/mois. Intérieur rural : 1 200–2 000 €/mois. L'Espagne est ~25% moins chère que la France ou l'Allemagne.",
        "faq_title":"Questions fréquentes",
        "faq":[
            ("Quel est le revenu minimum pour le Visa Non Lucratif ?","2 400 €/mois pour le demandeur principal + 600 € par membre de la famille. Revenus passifs uniquement : retraite, dividendes, loyers."),
            ("Peut-on travailler avec un Visa Non Lucratif ?","Non. Ce visa interdit le travail en Espagne. Pour travailler à distance pour des clients non espagnols, demandez le Visa Nomade Numérique."),
            ("Combien de temps faut-il pour la résidence permanente ?","5 ans de résidence légale continue. La nationalité espagnole demande 10 ans (2 ans pour les ressortissants des pays hispanophones)."),
            ("L'Espagne est-elle sûre pour les expatriés ?","Oui, l'Espagne figure parmi les pays les plus sûrs du monde. Faible criminalité violente."),
            ("Faut-il parler espagnol ?","Non obligatoire dans les zones côtières très expatriées (Costa del Sol, Costa Blanca). L'apprentissage de l'espagnol facilite grandement l'intégration."),
        ],
    },
    "es":{
        "title":"Guía Expatriados España 2026 — Vivir en España | eVisa-Card.com",
        "meta_desc":"Guía completa expatriados España 2026. Visa No Lucrativa, Nómada Digital, NIE, residencia, vivienda, banca, sanidad.",
        "h1":"Guía Expatriados: Vivir en España 2026",
        "breadcrumb":"Guía Expatriados España",
        "intro":"España sigue siendo uno de los principales destinos mundiales para expatriados gracias a su clima mediterráneo, cultura vibrante, excelente sistema sanitario y coste de vida relativamente asequible fuera de las grandes ciudades.",
        "facts_title":"España de un vistazo",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Madrid</div><div class="col-md-3 col-6"><strong>Moneda</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Español</div><div class="col-md-3 col-6"><strong>Schengen</strong><br/>Sí</div>',
        "visa_section_title":"Opciones de Visa y Residencia",
        "visa_section_text":"Opciones clave: Visa No Lucrativa (sin trabajo, ingresos pasivos ≥ €2.400/mes), Visa Nómada Digital (trabajo remoto para empleadores no españoles, ingresos ≥ €2.334/mes), Golden Visa (inversión ≥ €500k). Ciudadanos UE se registran en la Oficina de Extranjeros.",
        "visa_link_text":"→ Guía completa de visas para España",
        "steps_title":"Paso a Paso: Cómo Mudarse a España",
        "steps":[
            {"title":"Solicitar el visado","desc":"Solicitud en el consulado español: pasaporte, prueba de ingresos (€2.400+/mes para VNL), seguro médico privado, antecedentes penales, prueba de alojamiento, certificado médico."},
            {"title":"Obtener el NIE","desc":"Solicítalo en el consulado español antes de llegar o en la Oficina de Extranjeros en España. Imprescindible para casi cualquier trámite oficial."},
            {"title":"Empadronarse","desc":"Regístrate en tu Ayuntamiento. Obligatorio para acceder a sanidad, colegios y solicitar permiso de residencia."},
            {"title":"Abrir cuenta bancaria española","desc":"Abre cuenta en Santander, BBVA o CaixaBank con pasaporte + NIE."},
            {"title":"Obtener la Tarjeta de Identidad de Extranjero (TIE)","desc":"Canjea tu visado de larga estancia por una tarjeta de residencia en la Oficina de Extranjeros en los 30 días siguientes a la llegada."},
            {"title":"Inscribirse en sanidad pública","desc":"Ciudadanos UE: tarjeta sanitaria europea válida inicialmente. Residentes no UE: regístrate en el Centro de Salud con TIE + empadronamiento."},
            {"title":"Registro fiscal (Hacienda)","desc":"Regístrate en la Agencia Tributaria. España grava los ingresos mundiales de residentes (183+ días/año). La Ley Beckham ofrece un tipo fijo del 24% durante 6 años."},
        ],
        "housing_title":"Vivienda",
        "housing_text":"Madrid 1 hab.: €1.200–€1.800/mes. Barcelona: €1.300–€2.000/mes. Valencia/Alicante: €700–€1.100/mes. Ciudades interiores: €700–€1.200/mes. Portales: Idealista, Fotocasa.",
        "banking_title":"Banca",
        "banking_text":"Bancos principales: Santander, BBVA, CaixaBank, Sabadell. Apertura con NIE + pasaporte. Revolut y Wise muy usados. Servicios en inglés disponibles en zonas de expatriados.",
        "health_title":"Sanidad",
        "health_text":"Excelente SNS público para residentes empadronados. Clínicas privadas de alta calidad. Seguro privado: €50–€200/mes (Sanitas, Adeslas, AXA).",
        "cost_title":"Costo de Vida",
        "cost_text":"Madrid/Barcelona: €2.500–€4.000/mes (pareja). Valencia/Alicante: €1.800–€2.800/mes. Interior rural: €1.200–€2.000/mes. España es ~25% más barata que Francia, Alemania o el Reino Unido.",
        "faq_title":"Preguntas Frecuentes",
        "faq":[
            ("¿Cuál es el ingreso mínimo para la Visa No Lucrativa?","€2.400/mes para el solicitante principal + €600 por familiar. Solo ingresos pasivos: pensión, dividendos, alquileres."),
            ("¿Se puede trabajar con la Visa No Lucrativa?","No. Prohíbe trabajar en España. Para trabajo remoto para clientes no españoles, solicita la Visa Nómada Digital."),
            ("¿Cuánto tiempo lleva la residencia permanente?","5 años de residencia legal continua. La ciudadanía española requiere 10 años (2 para ciudadanos de países hispanohablantes)."),
            ("¿Es España segura?","Sí, aparece entre los países más seguros del mundo. Baja criminalidad violenta."),
            ("¿Es necesario hablar español?","No obligatorio en zonas costeras de expats. Aprender español facilita mucho la integración."),
        ],
    },
    "pt":{
        "title":"Guia Expatriados Espanha 2026 — Viver na Espanha | eVisa-Card.com",
        "meta_desc":"Guia completo expatriados Espanha 2026. Visto Não Lucrativo, Nômade Digital, NIE, residência, moradia, banco, saúde.",
        "h1":"Guia Expatriados: Viver na Espanha 2026",
        "breadcrumb":"Guia Expatriados Espanha",
        "intro":"A Espanha continua sendo um dos principais destinos para expatriados no mundo, graças ao seu clima mediterrâneo, cultura vibrante, excelente sistema de saúde e custo de vida relativamente acessível fora das grandes cidades.",
        "facts_title":"Espanha em Resumo",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Madri</div><div class="col-md-3 col-6"><strong>Moeda</strong><br/>Euro (EUR)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Espanhol</div><div class="col-md-3 col-6"><strong>Schengen</strong><br/>Sim</div>',
        "visa_section_title":"Opções de Visto e Residência",
        "visa_section_text":"Opções principais: Visto Não Lucrativo (sem trabalho, renda passiva ≥ €2.400/mês), Visto Nômade Digital (trabalho remoto para empregadores não espanhóis, renda ≥ €2.334/mês), Golden Visa (investimento ≥ €500k). Cidadãos UE registram-se no Escritório de Estrangeiros.",
        "visa_link_text":"→ Guia completo de vistos para a Espanha",
        "steps_title":"Passo a Passo: Como se Mudar para a Espanha",
        "steps":[
            {"title":"Solicitar o visto","desc":"Solicitação no consulado espanhol: passaporte, comprovante de renda (€2.400+/mês para VNL), seguro saúde privado, antecedentes criminais, comprovante de hospedagem, atestado médico."},
            {"title":"Obter o NIE","desc":"Solicite no consulado espanhol antes de chegar ou no Escritório de Estrangeiros na Espanha. Imprescindível para quase qualquer trâmite oficial."},
            {"title":"Empadronar-se","desc":"Registre-se na Prefeitura (Ayuntamiento). Obrigatório para acesso à saúde, escolas e solicitação de permissão de residência."},
            {"title":"Abrir conta bancária espanhola","desc":"Abra conta no Santander, BBVA ou CaixaBank com passaporte + NIE."},
            {"title":"Obter a Tarjeta de Identidad de Extranjero (TIE)","desc":"Troque seu visto de longa permanência por um cartão de residência no Escritório de Estrangeiros dentro de 30 dias após a chegada."},
            {"title":"Inscrever-se na saúde pública","desc":"Cidadãos UE: cartão europeu de seguro saúde válido inicialmente. Residentes não-UE: inscreva-se no Centro de Salud com TIE + registro municipal."},
            {"title":"Registro fiscal (Hacienda)","desc":"Registre-se na Agencia Tributaria. A Espanha tributa rendimentos mundiais de residentes (+183 dias/ano). A Lei Beckham oferece taxa fixa de 24% por 6 anos."},
        ],
        "housing_title":"Moradia",
        "housing_text":"Madri 1 quarto: €1.200–€1.800/mês. Barcelona: €1.300–€2.000/mês. Valência/Alicante: €700–€1.100/mês. Cidades interiores: €700–€1.200/mês. Portais: Idealista, Fotocasa.",
        "banking_title":"Banco",
        "banking_text":"Principais bancos: Santander, BBVA, CaixaBank, Sabadell. Abertura com NIE + passaporte. Revolut e Wise muito usados. Serviços em inglês disponíveis em zonas de expatriados.",
        "health_title":"Saúde",
        "health_text":"Excelente SNS público para residentes registrados. Clínicas privadas de alta qualidade. Seguro privado: €50–€200/mês (Sanitas, Adeslas, AXA).",
        "cost_title":"Custo de Vida",
        "cost_text":"Madri/Barcelona: €2.500–€4.000/mês (casal). Valência/Alicante: €1.800–€2.800/mês. Interior rural: €1.200–€2.000/mês. Espanha é ~25% mais barata que França, Alemanha ou Reino Unido.",
        "faq_title":"Perguntas Frequentes",
        "faq":[
            ("Qual é a renda mínima para o Visto Não Lucrativo?","€2.400/mês para o requerente principal + €600 por familiar. Somente renda passiva: aposentadoria, dividendos, aluguéis."),
            ("É possível trabalhar com o Visto Não Lucrativo?","Não. Proíbe trabalhar na Espanha. Para trabalho remoto para clientes não espanhóis, solicite o Visto Nômade Digital."),
            ("Quanto tempo leva a residência permanente?","5 anos de residência legal contínua. A cidadania espanhola requer 10 anos (2 anos para cidadãos de países hispanofalantes)."),
            ("A Espanha é segura?","Sim, aparece entre os países mais seguros do mundo. Baixa criminalidade violenta."),
            ("É necessário falar espanhol?","Não obrigatório em zonas costeiras de expatriados. Aprender espanhol facilita muito a integração."),
        ],
    },
},

"expat-guide-mexico": {
    "iso":"mx","visa_slug":"mexico",
    "en":{
        "title":"Expat Guide Mexico 2026 — How to Live in Mexico | eVisa-Card.com",
        "meta_desc":"Complete expat guide Mexico 2026. Temporary and permanent residency, step-by-step process, housing in Mexico City & Mérida, banking, healthcare, cost of living.",
        "h1":"Expat Guide: Living in Mexico 2026",
        "breadcrumb":"Expat Guide Mexico",
        "intro":"Mexico has become the number-one destination for American expats and a top choice for digital nomads worldwide. With its warm climate, rich culture, affordable cost of living, excellent food and proximity to the US, Mexico City, Mérida, Puerto Vallarta and Oaxaca are booming expat hubs.",
        "facts_title":"Mexico at a Glance",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Mexico City</div><div class="col-md-3 col-6"><strong>Currency</strong><br/>Mexican Peso (MXN)</div><div class="col-md-3 col-6"><strong>Language</strong><br/>Spanish</div><div class="col-md-3 col-6"><strong>Cost of Living</strong><br/>Low–Medium</div>',
        "visa_section_title":"Visa & Residency Options",
        "visa_section_text":"Temporary Resident Visa (1–4 years, renewable): income ≥ $2,500/month or savings $43,000+. Permanent Resident Visa: income ≥ $4,166/month or savings $175,000+, OR after 4 years as temporary resident. Retirement/Pension Visa: same income thresholds apply. No digital nomad visa specifically but temporary resident covers remote workers.",
        "visa_link_text":"→ Full Mexico Visa Requirements Guide",
        "steps_title":"Step-by-Step: How to Move to Mexico",
        "steps":[
            {"title":"Apply for Temporary Resident Visa","desc":"Apply at a Mexican consulate in your home country. Required: passport, proof of income (bank statements showing $2,500+/month for 6 months, or $43,000 savings), passport photos, application form. Processing: 5–10 business days."},
            {"title":"Enter Mexico and get your visa stamped","desc":"Present your visa at the port of entry. The immigration officer issues a Form FMM. You have 30 days to convert your consular visa to a Residente Temporal card."},
            {"title":"Get your Residente Temporal card (INM)","desc":"Visit the National Migration Institute (INM) office in your city within 30 days of arrival. Bring passport, consular visa, proof of address, photos, and payment (~$400 USD). Processing: 2–8 weeks."},
            {"title":"Get your RFC (tax ID)","desc":"Register with the SAT (Servicio de Administración Tributaria) tax authority. Required for opening bank accounts, signing leases and working legally."},
            {"title":"Open a Mexican bank account","desc":"Open with BBVA Mexico, Santander Mexico, Banamex or HSBC Mexico. Required: passport, residence card, CURP number. Online banks like Nu Bank are increasingly popular."},
            {"title":"Get CURP (unique population register code)","desc":"The CURP is your unique ID in Mexico. Obtained automatically at INM when you get your residency card, or apply at a Registro Civil office."},
            {"title":"Register with IMSS or get private insurance","desc":"Residents can voluntarily enrol in IMSS (public health insurance, ~$600/year). Most expats prefer private health insurance (AXA Mexico, GNP, Cigna): $200–$600/year."},
        ],
        "housing_title":"Housing",
        "housing_text":"Mexico City (Roma/Condesa): $800–$1,500/month. Mérida: $400–$800/month. Puerto Vallarta: $700–$1,500/month. Oaxaca: $400–$700/month. Foreigner-friendly platforms: Airbnb initially, then Inmuebles24, Lamudi for long-term.",
        "banking_title":"Banking",
        "banking_text":"Main banks: BBVA Mexico, Santander, Banamex, HSBC, Nu Bank. Open with residence card + CURP. Wise and Revolut popular for international transfers. Cash still widely used in smaller cities.",
        "health_title":"Healthcare",
        "health_text":"Public IMSS available to voluntary residents (~$600/year). Excellent private hospitals in major cities (American British Cowdray Hospital CDMX, Star Médica). Private insurance ~$200–$600/year. Medical costs 60–80% lower than USA.",
        "cost_title":"Cost of Living",
        "cost_text":"Mexico City (comfortable): $1,500–$2,500/month. Mérida/Oaxaca: $1,000–$1,800/month. Puerto Vallarta: $1,500–$2,500/month. Mexico is one of the most affordable expat destinations for North Americans.",
        "faq_title":"Frequently Asked Questions",
        "faq":[
            ("Can I work remotely in Mexico on a Temporary Resident Visa?","Yes. The Temporary Resident Visa does not restrict foreign-source remote work. You can work for non-Mexican employers without a separate work permit."),
            ("Can foreigners own property in Mexico?","Yes, with restrictions. Foreigners cannot directly own land within 50km of a coast or 100km of a border (restricted zone). They must use a Fideicomiso (bank trust) or a Mexican corporation."),
            ("Is Mexico City safe?","Safety varies by neighbourhood. Expat-popular areas (Roma, Condesa, Polanco, Coyoacán) are generally safe. Avoid high-crime areas and use common sense precautions."),
            ("How long does it take to get permanent residency?","After 4 consecutive years as a temporary resident, you qualify for permanent residency. Or immediately if income ≥ $4,166/month or savings ≥ $175,000."),
            ("Do I need to speak Spanish?","Not mandatory in major expat hubs (Mexico City, Puerto Vallarta, San Miguel de Allende). Spanish is helpful and highly appreciated everywhere."),
        ],
    },
    "fr":{
        "title":"Guide Expatriation Mexique 2026 — Vivre au Mexique | eVisa-Card.com",
        "meta_desc":"Guide complet expatriation Mexique 2026. Résidence temporaire et permanente, démarches, logement à Mexico et Mérida, banque, santé, coût de la vie.",
        "h1":"Guide Expatriation : Vivre au Mexique 2026",
        "breadcrumb":"Guide Expatriation Mexique",
        "intro":"Le Mexique est devenu la première destination des expatriés américains et un hub mondial pour les nomades numériques. Mexico, Mérida, Puerto Vallarta et Oaxaca attirent les expatriés grâce à leur coût de vie abordable, leur culture riche et leur proximité avec les États-Unis.",
        "facts_title":"Le Mexique en bref",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capitale</strong><br/>Mexico</div><div class="col-md-3 col-6"><strong>Monnaie</strong><br/>Peso mexicain (MXN)</div><div class="col-md-3 col-6"><strong>Langue</strong><br/>Espagnol</div><div class="col-md-3 col-6"><strong>Coût de vie</strong><br/>Faible–Moyen</div>',
        "visa_section_title":"Options de visa et résidence",
        "visa_section_text":"Visa de Résident Temporaire (1–4 ans, renouvelable) : revenus ≥ 2 500 $/mois ou épargne ≥ 43 000 $. Résident Permanent : revenus ≥ 4 166 $/mois ou épargne ≥ 175 000 $, ou après 4 ans en tant que résident temporaire.",
        "visa_link_text":"→ Guide complet des visas Mexique",
        "steps_title":"Étapes pour s'installer au Mexique",
        "steps":[
            {"title":"Demander le visa Résident Temporaire","desc":"Demande au consulat mexicain : passeport, justificatifs de revenus (relevés bancaires 2 500 $/mois sur 6 mois, ou 43 000 $ d'épargne), photos, formulaire. Délai : 5–10 jours ouvrés."},
            {"title":"Entrer au Mexique et faire tamponner le visa","desc":"Présentez votre visa à l'entrée. L'officier d'immigration délivre le formulaire FMM. Vous avez 30 jours pour convertir votre visa consulaire en carte Residente Temporal."},
            {"title":"Obtenir la carte Residente Temporal (INM)","desc":"Rendez-vous à l'Institut National de la Migration (INM) dans les 30 jours suivant l'arrivée. Documents : passeport, visa consulaire, justificatif de domicile, photos, paiement (~400 USD)."},
            {"title":"Obtenir le RFC (identifiant fiscal)","desc":"Inscrivez-vous auprès du SAT. Nécessaire pour ouvrir un compte bancaire, signer un bail et travailler légalement."},
            {"title":"Ouvrir un compte bancaire mexicain","desc":"Ouvrez un compte chez BBVA Mexico, Santander Mexico, Banamex ou HSBC avec passeport + carte de résident + CURP."},
            {"title":"Obtenir le CURP","desc":"Le CURP est votre identifiant unique au Mexique, obtenu automatiquement à l'INM lors de l'obtention de la carte de résident."},
            {"title":"S'inscrire à l'IMSS ou souscrire une assurance privée","desc":"Inscription volontaire à l'IMSS (~600 $/an). La plupart des expatriés préfèrent une assurance privée (AXA Mexico, GNP) : 200–600 $/an."},
        ],
        "housing_title":"Logement",
        "housing_text":"Mexico (Roma/Condesa) : 800–1 500 $/mois. Mérida : 400–800 $/mois. Puerto Vallarta : 700–1 500 $/mois. Oaxaca : 400–700 $/mois. Plateformes : Airbnb pour commencer, puis Inmuebles24 pour le long terme.",
        "banking_title":"Banque",
        "banking_text":"Principales banques : BBVA Mexico, Santander, Banamex, HSBC, Nu Bank. Ouverture avec carte de résident + CURP. Wise et Revolut pour les virements internationaux.",
        "health_title":"Santé",
        "health_text":"IMSS public disponible pour les résidents (~600 $/an). Excellents hôpitaux privés dans les grandes villes. Assurance privée ~200–600 $/an. Coûts médicaux 60–80% moins chers qu'aux États-Unis.",
        "cost_title":"Coût de la vie",
        "cost_text":"Mexico (confortable) : 1 500–2 500 $/mois. Mérida/Oaxaca : 1 000–1 800 $/mois. Puerto Vallarta : 1 500–2 500 $/mois. Parmi les destinations les plus abordables pour les expatriés.",
        "faq_title":"Questions fréquentes",
        "faq":[
            ("Puis-je travailler à distance avec un visa Résident Temporaire ?","Oui. Le visa de Résident Temporaire n'interdit pas le télétravail pour des employeurs non mexicains. Pas de permis de travail séparé nécessaire."),
            ("Les étrangers peuvent-ils acheter de l'immobilier au Mexique ?","Oui, avec restrictions. Les étrangers ne peuvent pas posséder directement de terrain dans les 50 km du littoral ou 100 km des frontières (zone restreinte) — un Fideicomiso (fiducie bancaire) est nécessaire."),
            ("Mexico est-elle sûre ?","La sécurité varie selon les quartiers. Les zones populaires chez les expatriés (Roma, Condesa, Polanco, Coyoacán) sont généralement sûres."),
            ("Combien de temps faut-il pour la résidence permanente ?","Après 4 ans consécutifs en tant que résident temporaire, ou immédiatement si revenus ≥ 4 166 $/mois ou épargne ≥ 175 000 $."),
            ("Faut-il parler espagnol ?","Non obligatoire dans les grands hubs d'expatriés. L'espagnol est utile et très apprécié partout."),
        ],
    },
    "es":{
        "title":"Guía Expatriados México 2026 — Vivir en México | eVisa-Card.com",
        "meta_desc":"Guía completa expatriados México 2026. Residencia temporal y permanente, trámites, vivienda en CDMX y Mérida, banca, salud, costo de vida.",
        "h1":"Guía Expatriados: Vivir en México 2026",
        "breadcrumb":"Guía Expatriados México",
        "intro":"México se ha convertido en el destino número uno para expatriados estadounidenses y un hub mundial para nómadas digitales. Ciudad de México, Mérida, Puerto Vallarta y Oaxaca atraen expatriados por su bajo costo de vida, rica cultura y cercanía a EE.UU.",
        "facts_title":"México de un vistazo",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Ciudad de México</div><div class="col-md-3 col-6"><strong>Moneda</strong><br/>Peso mexicano (MXN)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Español</div><div class="col-md-3 col-6"><strong>Costo de vida</strong><br/>Bajo–Medio</div>',
        "visa_section_title":"Opciones de Visa y Residencia",
        "visa_section_text":"Visa de Residente Temporal (1–4 años, renovable): ingresos ≥ $2.500/mes o ahorros ≥ $43.000. Residente Permanente: ingresos ≥ $4.166/mes o ahorros ≥ $175.000, o tras 4 años como residente temporal.",
        "visa_link_text":"→ Guía completa de visas para México",
        "steps_title":"Paso a Paso: Cómo Mudarse a México",
        "steps":[
            {"title":"Solicitar la Visa de Residente Temporal","desc":"Solicitud en el consulado mexicano: pasaporte, prueba de ingresos (estados de cuenta $2.500+/mes por 6 meses, o $43.000 en ahorros), fotos, formulario. Tiempo: 5–10 días hábiles."},
            {"title":"Entrar a México y sellar la visa","desc":"Presenta tu visa en el punto de entrada. El oficial de inmigración emite el formulario FMM. Tienes 30 días para convertir la visa consular en tarjeta de Residente Temporal."},
            {"title":"Obtener la tarjeta de Residente Temporal (INM)","desc":"Ve al Instituto Nacional de Migración (INM) dentro de los 30 días de llegada. Documentos: pasaporte, visa consular, comprobante de domicilio, fotos, pago (~$400 USD)."},
            {"title":"Obtener el RFC","desc":"Regístrate en el SAT. Necesario para abrir cuenta bancaria, firmar contratos y trabajar legalmente."},
            {"title":"Abrir cuenta bancaria mexicana","desc":"Abre cuenta en BBVA México, Santander, Banamex o HSBC con pasaporte + tarjeta de residente + CURP."},
            {"title":"Obtener el CURP","desc":"El CURP es tu identificador único en México, obtenido automáticamente en el INM al tramitar la tarjeta de residente."},
            {"title":"Inscribirse al IMSS o contratar seguro privado","desc":"Inscripción voluntaria al IMSS (~$600/año). La mayoría de expatriados prefiere seguro privado (AXA México, GNP): $200–$600/año."},
        ],
        "housing_title":"Vivienda",
        "housing_text":"CDMX (Roma/Condesa): $800–$1.500/mes. Mérida: $400–$800/mes. Puerto Vallarta: $700–$1.500/mes. Oaxaca: $400–$700/mes. Plataformas: Airbnb al inicio, luego Inmuebles24 para largo plazo.",
        "banking_title":"Banca",
        "banking_text":"Bancos principales: BBVA México, Santander, Banamex, HSBC, Nu Bank. Apertura con tarjeta de residente + CURP. Wise y Revolut para transferencias internacionales.",
        "health_title":"Salud",
        "health_text":"IMSS público disponible para residentes (~$600/año). Excelentes hospitales privados en las principales ciudades. Seguro privado ~$200–$600/año. Costos médicos 60–80% más bajos que en EE.UU.",
        "cost_title":"Costo de Vida",
        "cost_text":"CDMX (cómodo): $1.500–$2.500/mes. Mérida/Oaxaca: $1.000–$1.800/mes. Puerto Vallarta: $1.500–$2.500/mes. Uno de los destinos más asequibles para expatriados.",
        "faq_title":"Preguntas Frecuentes",
        "faq":[
            ("¿Puedo trabajar remotamente con la Visa de Residente Temporal?","Sí. No restringe el trabajo remoto para empleadores no mexicanos. No se necesita permiso de trabajo adicional."),
            ("¿Pueden los extranjeros comprar propiedad en México?","Sí, con restricciones. No pueden poseer terreno directamente dentro de 50 km de costas o 100 km de fronteras — se requiere un Fideicomiso o sociedad mexicana."),
            ("¿Es segura la Ciudad de México?","Depende del barrio. Zonas populares entre expatriados (Roma, Condesa, Polanco, Coyoacán) son generalmente seguras."),
            ("¿Cuánto tiempo lleva la residencia permanente?","Tras 4 años consecutivos como residente temporal, o de inmediato si ingresos ≥ $4.166/mes o ahorros ≥ $175.000."),
            ("¿Es necesario hablar español?","No obligatorio en los principales hubs de expatriados. El español es útil y muy apreciado."),
        ],
    },
    "pt":{
        "title":"Guia Expatriados México 2026 — Viver no México | eVisa-Card.com",
        "meta_desc":"Guia completo expatriados México 2026. Residência temporária e permanente, trâmites, moradia na CDMX e Mérida, banco, saúde, custo de vida.",
        "h1":"Guia Expatriados: Viver no México 2026",
        "breadcrumb":"Guia Expatriados México",
        "intro":"O México tornou-se o destino número um para expatriados americanos e um hub global para nômades digitais. Cidade do México, Mérida, Puerto Vallarta e Oaxaca atraem expatriados pelo baixo custo de vida, cultura rica e proximidade aos EUA.",
        "facts_title":"México em Resumo",
        "facts_html":'<div class="col-md-3 col-6"><strong>Capital</strong><br/>Cidade do México</div><div class="col-md-3 col-6"><strong>Moeda</strong><br/>Peso mexicano (MXN)</div><div class="col-md-3 col-6"><strong>Idioma</strong><br/>Espanhol</div><div class="col-md-3 col-6"><strong>Custo de vida</strong><br/>Baixo–Médio</div>',
        "visa_section_title":"Opções de Visto e Residência",
        "visa_section_text":"Visto de Residente Temporário (1–4 anos, renovável): renda ≥ $2.500/mês ou poupança ≥ $43.000. Residente Permanente: renda ≥ $4.166/mês ou poupança ≥ $175.000, ou após 4 anos como residente temporário.",
        "visa_link_text":"→ Guia completo de vistos para o México",
        "steps_title":"Passo a Passo: Como se Mudar para o México",
        "steps":[
            {"title":"Solicitar o Visto de Residente Temporário","desc":"Solicitação no consulado mexicano: passaporte, comprovante de renda ($2.500+/mês por 6 meses ou $43.000 em poupança), fotos, formulário. Prazo: 5–10 dias úteis."},
            {"title":"Entrar no México e carimbar o visto","desc":"Apresente seu visto na entrada. O oficial de imigração emite o formulário FMM. Você tem 30 dias para converter o visto consular em cartão de Residente Temporário."},
            {"title":"Obter o cartão de Residente Temporário (INM)","desc":"Vá ao Instituto Nacional de Migração (INM) dentro de 30 dias da chegada. Documentos: passaporte, visto consular, comprovante de endereço, fotos, pagamento (~$400 USD)."},
            {"title":"Obter o RFC","desc":"Registre-se no SAT. Necessário para abrir conta bancária, assinar contratos e trabalhar legalmente."},
            {"title":"Abrir conta bancária mexicana","desc":"Abra conta no BBVA México, Santander, Banamex ou HSBC com passaporte + cartão de residente + CURP."},
            {"title":"Obter o CURP","desc":"O CURP é seu identificador único no México, obtido automaticamente no INM ao emitir o cartão de residente."},
            {"title":"Inscrever-se no IMSS ou contratar seguro privado","desc":"Inscrição voluntária no IMSS (~$600/ano). A maioria dos expatriados prefere seguro privado (AXA México, GNP): $200–$600/ano."},
        ],
        "housing_title":"Moradia",
        "housing_text":"CDMX (Roma/Condesa): $800–$1.500/mês. Mérida: $400–$800/mês. Puerto Vallarta: $700–$1.500/mês. Oaxaca: $400–$700/mês. Plataformas: Airbnb no início, depois Inmuebles24 para longo prazo.",
        "banking_title":"Banco",
        "banking_text":"Principais bancos: BBVA México, Santander, Banamex, HSBC, Nu Bank. Abertura com cartão de residente + CURP. Wise e Revolut para transferências internacionais.",
        "health_title":"Saúde",
        "health_text":"IMSS público disponível para residentes (~$600/ano). Excelentes hospitais privados nas principais cidades. Seguro privado ~$200–$600/ano. Custos médicos 60–80% menores que nos EUA.",
        "cost_title":"Custo de Vida",
        "cost_text":"CDMX (confortável): $1.500–$2.500/mês. Mérida/Oaxaca: $1.000–$1.800/mês. Puerto Vallarta: $1.500–$2.500/mês. Um dos destinos mais acessíveis para expatriados.",
        "faq_title":"Perguntas Frequentes",
        "faq":[
            ("Posso trabalhar remotamente com o Visto de Residente Temporário?","Sim. Não restringe trabalho remoto para empregadores não mexicanos. Não é necessário permissão de trabalho adicional."),
            ("Estrangeiros podem comprar imóvel no México?","Sim, com restrições. Não podem possuir terreno diretamente dentro de 50 km de costas ou 100 km de fronteiras — necessário Fideicomiso ou empresa mexicana."),
            ("A Cidade do México é segura?","Depende do bairro. Zonas populares entre expatriados (Roma, Condesa, Polanco, Coyoacán) são geralmente seguras."),
            ("Quanto tempo leva a residência permanente?","Após 4 anos consecutivos como residente temporário, ou imediatamente se renda ≥ $4.166/mês ou poupança ≥ $175.000."),
            ("É necessário falar espanhol?","Não obrigatório nos principais hubs de expatriados. O espanhol é muito útil e apreciado."),
        ],
    },
},

}  # end COUNTRIES

# Generate
created = 0
for slug, data in COUNTRIES.items():
    for lang in ["en","fr","es","pt"]:
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

print(f"\nTotal: {created}")
