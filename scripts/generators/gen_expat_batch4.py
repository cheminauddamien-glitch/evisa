#!/usr/bin/env python3
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

LANG_META = {
    "en": {"flag":"fi-gb","label":"English","home":"Home","dest":"Destinations","about":"About","blog":"Blog","guides":"Guides"},
    "fr": {"flag":"fi-fr","label":"Français","home":"Accueil","dest":"Destinations","about":"À propos","blog":"Blog","guides":"Guides"},
    "es": {"flag":"fi-es","label":"Español","home":"Inicio","dest":"Destinos","about":"Sobre Nosotros","blog":"Blog","guides":"Guías"},
    "pt": {"flag":"fi-br","label":"Português","home":"Início","dest":"Destinos","about":"Sobre Nós","blog":"Blog","guides":"Guias"},
}

def page(lang, slug, iso, data):
    lm = LANG_META[lang]
    sw_items = ""
    for tl, tm in LANG_META.items():
        active = ' active' if tl == lang else ''
        sw_items += f'\n                        <a class="dropdown-item{active}" href="/{tl}/{slug}.html"><span class="fi fi-{tm["flag"].replace("fi-","")}"></span> {tm["label"]}</a>'

    steps_html = "".join(f"""
                <div class="step-item d-flex mb-4">
                    <div class="step-number mr-4" style="min-width:48px;height:48px;background:#e63946;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:700;">{i+1}</div>
                    <div><h4 style="font-size:1.1rem;margin-bottom:4px;">{s['t']}</h4><p style="color:#555;margin:0;">{s['d']}</p></div>
                </div>""" for i, s in enumerate(data['steps']))

    cards_html = "".join(f"""
                <div class="col-md-3 col-sm-6 mb-4">
                    <div class="card h-100 shadow-sm border-0">
                        <div class="card-body text-center">
                            <div style="font-size:2rem;margin-bottom:8px;">{c['icon']}</div>
                            <h5 class="card-title" style="font-size:1rem;">{c['t']}</h5>
                            <p class="card-text" style="font-size:.88rem;color:#666;">{c['d']}</p>
                        </div>
                    </div>
                </div>""" for c in data['cards'])

    faq_schema = ",\n".join(f'{{"@type":"Question","name":{repr(q["q"])},"acceptedAnswer":{{"@type":"Answer","text":{repr(q["a"])}}}}}' for q in data['faqs'])
    steps_schema = ",\n".join(f'{{"@type":"HowToStep","name":{repr(s["t"])},"text":{repr(s["d"])}}}' for i, s in enumerate(data['steps']))
    faq_html = "".join(f"""
                <div class="mb-4">
                    <h4 style="font-size:1.05rem;color:#333;">{q['q']}</h4>
                    <p style="color:#555;">{q['a']}</p>
                </div>""" for q in data['faqs'])

    hreflang = "\n".join(f'    <link rel="alternate" hreflang="{tl}" href="https://www.evisa-card.com/{tl}/{slug}.html"/>' for tl in LANG_META)
    hreflang += f'\n    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}.html"/>'

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <title>{data['title']}</title>
    <meta name="description" content="{data['desc']}"/>
    <link rel="canonical" href="https://www.evisa-card.com/{lang}/{slug}.html"/>
{hreflang}
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{
      "@context":"https://schema.org",
      "@type":"HowTo",
      "name":{repr(data['h1'])},
      "description":{repr(data['desc'])},
      "step":[{steps_schema}]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context":"https://schema.org",
      "@type":"FAQPage",
      "mainEntity":[{faq_schema}]
    }}
    </script>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav mx-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">{lm['home']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">{lm['dest']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">{lm['about']}</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">{lm['blog']}</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">{lm['guides']}</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {lm['flag']}"></span> {lm['label']}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">{sw_items}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="hero-wrap hero-wrap-2" style="background-image:url('https://flagcdn.com/w1280/{iso}.png');background-size:cover;background-position:center;" data-stellar-background-ratio="0.5">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate pb-5 text-center">
                <p class="breadcrumbs"><span class="mr-2"><a href="../index.html">{lm['home']}</a></span> <span>{data['h1']}</span></p>
                <h1 class="mb-3 bread">{data['h1']}</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
    <div class="container" style="max-width:900px;">
        <div class="row justify-content-center mb-5">
            <div class="col-md-10 text-center">
                <p style="font-size:1.1rem;color:#555;">{data['intro']}</p>
            </div>
        </div>

        <!-- Key Facts -->
        <div class="row mb-5">
            <div class="col-12"><h2 style="border-left:4px solid #e63946;padding-left:12px;margin-bottom:24px;">{data['facts_title']}</h2></div>
            {cards_html}
        </div>

        <!-- Steps -->
        <div class="row mb-5">
            <div class="col-12"><h2 style="border-left:4px solid #e63946;padding-left:12px;margin-bottom:24px;">{data['steps_title']}</h2></div>
            <div class="col-12">{steps_html}
            </div>
        </div>

        <!-- FAQ -->
        <div class="row mb-5">
            <div class="col-12"><h2 style="border-left:4px solid #e63946;padding-left:12px;margin-bottom:24px;">{data['faq_title']}</h2></div>
            <div class="col-12">{faq_html}
            </div>
        </div>

        <p style="color:#999;font-size:13px;text-align:center;">Last updated: March 2026 — Always verify with official government sources.</p>
    </div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">© 2026 eVisa-Card.com</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/en/legal-notice.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/en/disclaimer.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""

COUNTRIES = {
    "colombia": {
        "iso": "co",
        "en": {
            "title": "Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com",
            "desc": "Complete guide to moving to Colombia as an expat in 2026. Visas, cost of living, housing, healthcare, and step-by-step process.",
            "h1": "Expat Guide: Living in Colombia",
            "intro": "Colombia has transformed into one of Latin America's top expat destinations. With a thriving digital nomad scene in Medellín, stunning Caribbean coast, and one of the most affordable costs of living in the region, Colombia offers an outstanding quality of life for internationals.",
            "facts_title": "Colombia at a Glance",
            "steps_title": "Step-by-Step: Moving to Colombia",
            "faq_title": "Frequently Asked Questions",
            "cards": [
                {"icon":"🏙️","t":"Capital","d":"Bogotá (pop. 11M) — Medellín, Cali, Cartagena also popular"},
                {"icon":"💰","t":"Cost of Living","d":"~$800–$1,500/mo for singles. Very affordable vs Western standards"},
                {"icon":"🏥","t":"Healthcare","d":"EPS (public health) or private plans from ~$50/mo. High quality in cities"},
                {"icon":"🌤️","t":"Climate","d":"Varies by altitude. Medellín: eternal spring ~22°C. Coast: tropical 28–32°C"},
            ],
            "steps": [
                {"t":"Entry & Tourist Stay","d":"Most nationalities enter visa-free for 90 days (extendable to 180 days/year). Use this time to explore and decide where to settle."},
                {"t":"Choose Your Visa Type","d":"Main options: Digital Nomad Visa (DNV) — remote workers earning $684+/mo; Rentista Visa — passive income $684+/mo; Pensionado Visa — pension $684+/mo; Cónyuge Visa — spouse of Colombian national."},
                {"t":"Gather Required Documents","d":"Passport (6+ months validity), passport photos, financial proof (bank statements 3 months), employment contract or proof of remote income, health insurance, criminal background check apostilled."},
                {"t":"Apply at Colombian Consulate or Online","d":"Apply via Cancillería Colombia portal (cancilleria.gov.co). Pay visa fee (~$55 USD). Processing: 3–10 business days. Visa issued as PDF — print it."},
                {"t":"Arrive & Register with Migración Colombia","d":"Within 15 days of arrival, register at Migración Colombia office. Get your Cédula de Extranjería (ID card for foreigners) — required for bank accounts, SIM cards, contracts."},
                {"t":"Open a Bank Account","d":"Required: Cédula de Extranjería, proof of address, proof of income. Banks: Bancolombia, Davivienda, Nequi (digital). Some banks accept tourist visa + passport initially."},
                {"t":"Healthcare & Daily Life Setup","d":"Join EPS (public) or take private insurance (Colmédica, SURA). Rent an apartment in Medellín El Poblado, Laureles; Bogotá Chapinero, Usaquén; or Cartagena historic center. $300–$700/mo for furnished 1BR in top neighborhoods."},
            ],
            "faqs": [
                {"q":"Can I work remotely in Colombia on a tourist visa?","a":"Technically you need a Digital Nomad Visa to legally work remotely for foreign companies. However, many digital nomads stay on tourist visas. The DNV provides legal clarity and easier banking access."},
                {"q":"What is the Colombia Digital Nomad Visa?","a":"Introduced in 2022, the Digital Nomad Visa (Type V) allows remote workers to live in Colombia for up to 2 years. Requirements: proof of remote employment/freelance income of at least 3× minimum wage (~$684/mo), health insurance, valid passport."},
                {"q":"Is Colombia safe for expats?","a":"Safety has improved dramatically. Medellín, Bogotá, and Cartagena have vibrant expat communities. Stick to established neighborhoods, take standard precautions, and you will generally feel safe. Avoid frontier regions."},
                {"q":"Do I need to learn Spanish?","a":"Spanish is essential for daily life outside major expat hubs. In El Poblado (Medellín) and Usaquén (Bogotá) you can get by with English, but learning Spanish greatly improves your experience and is highly recommended."},
                {"q":"How do I get Colombian residency?","a":"After 5 years on a temporary visa (or 2 years as spouse of Colombian), you can apply for a Resident Visa (Tipo R). This grants indefinite stay and a path to citizenship after further time."},
            ],
        },
        "fr": {
            "title": "Guide Expatrié Colombie 2026 — Vivre et Travailler en Colombie | eVisa-Card.com",
            "desc": "Guide complet pour s'expatrier en Colombie en 2026. Visas, coût de la vie, logement, santé et processus étape par étape.",
            "h1": "Guide Expatrié : Vivre en Colombie",
            "intro": "La Colombie est devenue l'une des principales destinations d'expatriation en Amérique latine. Avec une scène de nomades numériques florissante à Medellín, une côte caraïbe magnifique et un coût de la vie très abordable, la Colombie offre une excellente qualité de vie aux internationaux.",
            "facts_title": "La Colombie en un Coup d'Œil",
            "steps_title": "Étape par Étape : S'installer en Colombie",
            "faq_title": "Questions Fréquemment Posées",
            "cards": [
                {"icon":"🏙️","t":"Capitale","d":"Bogotá (11M hab.) — Medellín, Cali, Carthagène très prisées"},
                {"icon":"💰","t":"Coût de la Vie","d":"~800–1 500 $/mois. Très abordable comparé aux standards occidentaux"},
                {"icon":"🏥","t":"Santé","d":"EPS (public) ou assurance privée dès ~50 $/mois. Qualité élevée en ville"},
                {"icon":"🌤️","t":"Climat","d":"Variable selon l'altitude. Medellín : printemps éternel ~22°C. Côte : tropical 28–32°C"},
            ],
            "steps": [
                {"t":"Entrée et Séjour Touristique","d":"La plupart des nationalités entrent sans visa pour 90 jours (extensibles à 180 jours/an). Profitez-en pour explorer et décider où vous installer."},
                {"t":"Choisir votre Type de Visa","d":"Principales options : Visa Nomade Numérique — télétravail avec revenus ≥684 $/mois ; Visa Rentista — revenus passifs ≥684 $/mois ; Visa Pensionado — retraite ≥684 $/mois ; Visa Cónyuge — conjoint d'un ressortissant colombien."},
                {"t":"Rassembler les Documents","d":"Passeport valide 6+ mois, photos d'identité, justificatifs financiers (3 derniers relevés bancaires), contrat de travail ou preuve de revenus à distance, assurance maladie, casier judiciaire apostillé."},
                {"t":"Déposer votre Demande","d":"Via le portail Cancillería Colombia (cancilleria.gov.co). Frais de visa : ~55 USD. Délai : 3–10 jours ouvrés. Le visa est délivré en PDF — imprimez-le."},
                {"t":"Arriver et s'Enregistrer","d":"Dans les 15 jours suivant l'arrivée, enregistrez-vous à la Migración Colombia. Obtenez votre Cédula de Extranjería (carte d'identité étrangère) — obligatoire pour ouvrir un compte bancaire, acheter une SIM, signer des contrats."},
                {"t":"Ouvrir un Compte Bancaire","d":"Documents requis : Cédula de Extranjería, justificatif de domicile, preuve de revenus. Banques : Bancolombia, Davivienda, Nequi (digital). Certaines banques acceptent passeport + visa touristique initialement."},
                {"t":"Santé et Installation au Quotidien","d":"Rejoignez l'EPS (public) ou souscrivez une assurance privée (Colmédica, SURA). Loyer : 300–700 $/mois pour un T1 meublé dans les quartiers prisés (El Poblado à Medellín, Chapinero à Bogotá)."},
            ],
            "faqs": [
                {"q":"Puis-je télétravailler en Colombie avec un visa touriste ?","a":"Techniquement, le visa nomade numérique est nécessaire pour exercer légalement une activité à distance. Beaucoup de nomades restent cependant avec un visa touriste. Le visa DNV facilite l'accès aux services bancaires."},
                {"q":"Qu'est-ce que le visa nomade numérique colombien ?","a":"Lancé en 2022, ce visa (type V) permet aux télétravailleurs de résider en Colombie jusqu'à 2 ans. Conditions : preuve d'emploi ou de revenus freelance ≥3× salaire minimum (~684 $/mois), assurance maladie, passeport valide."},
                {"q":"La Colombie est-elle sûre pour les expatriés ?","a":"La sécurité s'est considérablement améliorée. Medellín, Bogotá et Carthagène ont des communautés d'expatriés actives. Dans les quartiers établis, vous vous sentirez généralement en sécurité. Évitez les zones frontalières."},
                {"q":"Faut-il apprendre l'espagnol ?","a":"L'espagnol est indispensable en dehors des hubs d'expatriés. Dans El Poblado (Medellín) ou Usaquén (Bogotá), on peut s'en sortir en anglais, mais l'espagnol améliore considérablement votre quotidien."},
                {"q":"Comment obtenir la résidence permanente colombienne ?","a":"Après 5 ans de visa temporaire (ou 2 ans comme conjoint d'un Colombien), vous pouvez demander le Visa Résident (Type R). Il ouvre droit à un séjour indéfini et à la nationalité colombienne par la suite."},
            ],
        },
        "es": {
            "title": "Guía Expat Colombia 2026 — Vivir y Trabajar en Colombia | eVisa-Card.com",
            "desc": "Guía completa para expatriarse en Colombia en 2026. Visas, costo de vida, vivienda, salud y proceso paso a paso.",
            "h1": "Guía Expat: Vivir en Colombia",
            "intro": "Colombia se ha convertido en uno de los principales destinos de expatriados en América Latina. Con una vibrante escena de nómadas digitales en Medellín, una hermosa costa caribeña y uno de los costos de vida más asequibles de la región, Colombia ofrece una excelente calidad de vida para los extranjeros.",
            "facts_title": "Colombia de un Vistazo",
            "steps_title": "Paso a Paso: Mudarse a Colombia",
            "faq_title": "Preguntas Frecuentes",
            "cards": [
                {"icon":"🏙️","t":"Capital","d":"Bogotá (11M hab.) — Medellín, Cali, Cartagena también populares"},
                {"icon":"💰","t":"Costo de Vida","d":"~$800–$1,500/mes. Muy asequible comparado con estándares occidentales"},
                {"icon":"🏥","t":"Salud","d":"EPS (pública) o planes privados desde ~$50/mes. Alta calidad en ciudades"},
                {"icon":"🌤️","t":"Clima","d":"Variable según altitud. Medellín: primavera eterna ~22°C. Costa: tropical 28–32°C"},
            ],
            "steps": [
                {"t":"Entrada y Estancia Turística","d":"La mayoría de nacionalidades pueden entrar sin visa por 90 días (ampliables a 180 días/año). Usa este tiempo para explorar y decidir dónde establecerte."},
                {"t":"Elegir el Tipo de Visa","d":"Principales opciones: Visa Nómada Digital — trabajo remoto con ingresos ≥$684/mes; Visa Rentista — ingresos pasivos ≥$684/mes; Visa Pensionado — jubilación ≥$684/mes; Visa Cónyuge — cónyuge de ciudadano colombiano."},
                {"t":"Reunir los Documentos Requeridos","d":"Pasaporte con 6+ meses de vigencia, fotos, estados de cuenta bancarios (3 meses), contrato laboral o prueba de ingresos remotos, seguro médico, antecedentes penales apostillados."},
                {"t":"Solicitar el Visa","d":"A través del portal Cancillería Colombia (cancilleria.gov.co). Pago de tasa consular (~$55 USD). Tiempo de procesamiento: 3–10 días hábiles. El visa se emite en PDF — imprímelo."},
                {"t":"Llegar y Registrarse en Migración Colombia","d":"Dentro de los 15 días de llegada, regístrate en Migración Colombia. Obtén tu Cédula de Extranjería — obligatoria para cuentas bancarias, SIM, contratos."},
                {"t":"Abrir una Cuenta Bancaria","d":"Documentos requeridos: Cédula de Extranjería, comprobante de domicilio, prueba de ingresos. Bancos: Bancolombia, Davivienda, Nequi (digital). Algunos bancos aceptan pasaporte + visa turista inicialmente."},
                {"t":"Salud y Vida Cotidiana","d":"Afíliate a EPS (público) o contrata un seguro privado (Colmédica, SURA). Alquiler: $300–$700/mes para un apartamento de 1 habitación amueblado en barrios premium (El Poblado en Medellín, Chapinero en Bogotá)."},
            ],
            "faqs": [
                {"q":"¿Puedo teletrabajar en Colombia con visa de turista?","a":"Técnicamente necesitas una Visa Nómada Digital para trabajar legalmente de forma remota. Muchos nómadas se quedan con visa turista, pero la visa DNV facilita el acceso a servicios bancarios y da tranquilidad legal."},
                {"q":"¿Qué es la Visa Nómada Digital de Colombia?","a":"Lanzada en 2022, esta visa (tipo V) permite a los trabajadores remotos residir en Colombia hasta 2 años. Requisitos: prueba de empleo remoto o freelance con ingresos ≥3× salario mínimo (~$684/mes), seguro médico, pasaporte válido."},
                {"q":"¿Es segura Colombia para los expatriados?","a":"La seguridad ha mejorado notablemente. Medellín, Bogotá y Cartagena tienen comunidades de expatriados activas. En barrios establecidos, generalmente te sentirás seguro. Evita las zonas fronterizas."},
                {"q":"¿Es necesario aprender español?","a":"El español es esencial fuera de los principales hubs de expatriados. En El Poblado (Medellín) o Usaquén (Bogotá) puedes sobrevivir con inglés, pero el español mejora enormemente tu experiencia."},
                {"q":"¿Cómo obtengo la residencia permanente colombiana?","a":"Tras 5 años de visa temporal (o 2 años como cónyuge de colombiano), puedes solicitar la Visa Residente (Tipo R). Otorga residencia indefinida y, eventualmente, acceso a la ciudadanía colombiana."},
            ],
        },
        "pt": {
            "title": "Guia Expat Colômbia 2026 — Viver e Trabalhar na Colômbia | eVisa-Card.com",
            "desc": "Guia completo para se expatriar na Colômbia em 2026. Vistos, custo de vida, moradia, saúde e processo passo a passo.",
            "h1": "Guia Expat: Viver na Colômbia",
            "intro": "A Colômbia tornou-se um dos principais destinos de expatriados na América Latina. Com uma cena de nômades digitais florescente em Medellín, uma bela costa caribenha e um dos custos de vida mais acessíveis da região, a Colômbia oferece uma excelente qualidade de vida para estrangeiros.",
            "facts_title": "Colômbia em Resumo",
            "steps_title": "Passo a Passo: Mudar para a Colômbia",
            "faq_title": "Perguntas Frequentes",
            "cards": [
                {"icon":"🏙️","t":"Capital","d":"Bogotá (11M hab.) — Medellín, Cali, Cartagena também populares"},
                {"icon":"💰","t":"Custo de Vida","d":"~$800–$1.500/mês. Muito acessível em relação aos padrões ocidentais"},
                {"icon":"🏥","t":"Saúde","d":"EPS (pública) ou planos privados a partir de ~$50/mês. Alta qualidade nas cidades"},
                {"icon":"🌤️","t":"Clima","d":"Varia com a altitude. Medellín: primavera eterna ~22°C. Costa: tropical 28–32°C"},
            ],
            "steps": [
                {"t":"Entrada e Estadia Turística","d":"A maioria das nacionalidades pode entrar sem visto por 90 dias (prorrogáveis a 180 dias/ano). Use este tempo para explorar e decidir onde se instalar."},
                {"t":"Escolher o Tipo de Visto","d":"Principais opções: Visto Nômade Digital — trabalho remoto com renda ≥$684/mês; Visto Rentista — renda passiva ≥$684/mês; Visto Pensionado — aposentadoria ≥$684/mês; Visto Cônjuge — cônjuge de cidadão colombiano."},
                {"t":"Reunir a Documentação","d":"Passaporte com 6+ meses de validade, fotos, extratos bancários (3 meses), contrato de trabalho ou prova de renda remota, seguro saúde, antecedentes criminais apostilados."},
                {"t":"Solicitar o Visto","d":"Pelo portal Cancillería Colombia (cancilleria.gov.co). Taxa consular: ~$55 USD. Prazo: 3–10 dias úteis. O visto é emitido em PDF — imprima-o."},
                {"t":"Chegar e Registrar-se na Migración Colombia","d":"Em até 15 dias após a chegada, registre-se na Migración Colombia. Obtenha sua Cédula de Extranjería — obrigatória para conta bancária, SIM, contratos."},
                {"t":"Abrir Conta Bancária","d":"Documentos necessários: Cédula de Extranjería, comprovante de endereço, prova de renda. Bancos: Bancolombia, Davivienda, Nequi (digital). Alguns bancos aceitam passaporte + visto turista inicialmente."},
                {"t":"Saúde e Vida Cotidiana","d":"Filie-se ao EPS (público) ou contrate plano privado (Colmédica, SURA). Aluguel: $300–$700/mês para apartamento de 1 quarto mobiliado em bairros premium (El Poblado em Medellín, Chapinero em Bogotá)."},
            ],
            "faqs": [
                {"q":"Posso trabalhar remotamente na Colômbia com visto de turista?","a":"Tecnicamente, você precisa do Visto Nômade Digital para trabalhar legalmente de forma remota. Muitos nômades ficam com visto turista, mas o DNV facilita o acesso a serviços bancários e oferece segurança jurídica."},
                {"q":"O que é o Visto Nômade Digital da Colômbia?","a":"Lançado em 2022, este visto (tipo V) permite que trabalhadores remotos residam na Colômbia por até 2 anos. Requisitos: prova de emprego remoto ou freelance com renda ≥3× salário mínimo (~$684/mês), seguro saúde, passaporte válido."},
                {"q":"A Colômbia é segura para expatriados?","a":"A segurança melhorou muito. Medellín, Bogotá e Cartagena têm comunidades de expatriados ativas. Em bairros consolidados, você geralmente se sentirá seguro. Evite regiões de fronteira."},
                {"q":"É necessário aprender espanhol?","a":"O espanhol é essencial fora dos principais hubs de expatriados. Em El Poblado (Medellín) ou Usaquén (Bogotá) dá para se virar em inglês, mas o espanhol melhora enormemente sua experiência."},
                {"q":"Como obter a residência permanente colombiana?","a":"Após 5 anos de visto temporário (ou 2 anos como cônjuge de colombiano), você pode solicitar o Visto Residente (Tipo R). Concede residência indefinida e, posteriormente, acesso à cidadania colombiana."},
            ],
        },
    },
}

total = 0
for slug, cdata in COUNTRIES.items():
    iso = cdata["iso"]
    for lang in ["en","fr","es","pt"]:
        html = page(lang, f"expat-guide-{slug}", iso, cdata[lang])
        out = os.path.join(WWW, lang, f"expat-guide-{slug}.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created: {lang}/expat-guide-{slug}.html")
        total += 1

print(f"\nTotal: {total}")
