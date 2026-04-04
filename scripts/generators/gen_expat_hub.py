#!/usr/bin/env python3
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

COUNTRIES = [
    {
        "slug":"expat-guide-thailand", "iso":"th",
        "en":"Thailand",  "fr":"Thaïlande", "es":"Tailandia",  "pt":"Tailândia",
        "summary":{
            "en":"Warm climate, low cost of living (~$1,000/mo) and world-class food. Thailand Retirement & LTR visas make it a top expat choice.",
            "fr":"Climat chaud, faible coût de la vie (~1 000 $/mois) et gastronomie incomparable. Les visas Retraite et LTR en font une destination phare.",
            "es":"Clima cálido, bajo costo de vida (~$1,000/mes) y gastronomía excepcional. Las visas de Jubilación y LTR lo convierten en destino líder.",
            "pt":"Clima quente, custo de vida baixo (~$1.000/mês) e gastronomia de excelência. Os vistos de Aposentadoria e LTR atraem expatriados do mundo todo.",
        }
    },
    {
        "slug":"expat-guide-portugal", "iso":"pt",
        "en":"Portugal",  "fr":"Portugal",  "es":"Portugal",   "pt":"Portugal",
        "summary":{
            "en":"EU member with a Golden Visa and D7 Passive Income Visa. Lisbon and Porto offer mild weather, safety and a vibrant expat scene.",
            "fr":"Membre UE avec Golden Visa et visa D7. Lisbonne et Porto offrent douceur de vivre, sécurité et une scène d'expatriés dynamique.",
            "es":"Miembro de la UE con Golden Visa y visa D7. Lisboa y Oporto ofrecen buen clima, seguridad y una animada comunidad de expatriados.",
            "pt":"Membro da UE com Golden Visa e visto D7. Lisboa e Porto oferecem clima agradável, segurança e uma vibrante comunidade de expatriados.",
        }
    },
    {
        "slug":"expat-guide-spain", "iso":"es",
        "en":"Spain",     "fr":"Espagne",   "es":"España",     "pt":"Espanha",
        "summary":{
            "en":"Sun, culture and EU access. Spain's Digital Nomad Visa and Non-Lucrative Visa attract thousands of expats every year.",
            "fr":"Soleil, culture et accès à l'UE. Le visa nomade numérique et le visa non-lucratif attirent chaque année des milliers d'expatriés.",
            "es":"Sol, cultura y acceso a la UE. La Visa Nómada Digital y la visa no lucrativa atraen a miles de expatriados cada año.",
            "pt":"Sol, cultura e acesso à UE. A Visa Nômade Digital e o visto não lucrativo atraem milhares de expatriados por ano.",
        }
    },
    {
        "slug":"expat-guide-mexico", "iso":"mx",
        "en":"Mexico",    "fr":"Mexique",   "es":"México",     "pt":"México",
        "summary":{
            "en":"Diverse landscapes, affordable living (~$1,200/mo) and easy visa access. Mexico City is a global digital nomad hub.",
            "fr":"Paysages variés, vie abordable (~1 200 $/mois) et accès visa facile. Mexico City est un hub mondial pour les nomades numériques.",
            "es":"Paisajes diversos, vida asequible (~$1,200/mes) y acceso fácil a visas. Ciudad de México es un hub global de nómadas digitales.",
            "pt":"Paisagens diversas, custo de vida acessível (~$1.200/mês) e facilidade de visto. Cidade do México é um hub global de nômades digitais.",
        }
    },
    {
        "slug":"expat-guide-vietnam", "iso":"vn",
        "en":"Vietnam",   "fr":"Vietnam",   "es":"Vietnam",    "pt":"Vietnã",
        "summary":{
            "en":"Ultra-low cost of living (~$700/mo), fast internet and vibrant cities. Hanoi and Ho Chi Minh City draw thousands of expats.",
            "fr":"Coût de vie ultra-bas (~700 $/mois), internet rapide et villes animées. Hanoï et Hô Chi Minh-Ville attirent des milliers d'expatriés.",
            "es":"Costo de vida ultra-bajo (~$700/mes), internet rápido y ciudades vibrantes. Hanói y Ho Chi Minh atraen a miles de expatriados.",
            "pt":"Custo de vida ultra-baixo (~$700/mês), internet rápida e cidades vibrantes. Hanói e Ho Chi Minh atraem milhares de expatriados.",
        }
    },
    {
        "slug":"expat-guide-malaysia", "iso":"my",
        "en":"Malaysia",  "fr":"Malaisie",  "es":"Malasia",    "pt":"Malásia",
        "summary":{
            "en":"English-speaking, modern infrastructure and low taxes. The MM2H visa makes Malaysia one of Asia's best retirement destinations.",
            "fr":"Anglophone, infrastructure moderne et faibles impôts. Le visa MM2H fait de la Malaisie l'une des meilleures destinations retraite d'Asie.",
            "es":"Anglófono, infraestructura moderna y bajos impuestos. La visa MM2H convierte a Malasia en uno de los mejores destinos de jubilación en Asia.",
            "pt":"Anglófono, infraestrutura moderna e impostos baixos. O visto MM2H torna a Malásia um dos melhores destinos de aposentadoria na Ásia.",
        }
    },
    {
        "slug":"expat-guide-japan", "iso":"jp",
        "en":"Japan",     "fr":"Japon",     "es":"Japón",      "pt":"Japão",
        "summary":{
            "en":"Unique culture, ultra-safe cities and excellent healthcare. The new Digital Nomad Visa (2024) opens Japan to remote workers.",
            "fr":"Culture unique, villes ultra-sûres et excellente santé. Le nouveau visa nomade numérique (2024) ouvre le Japon aux télétravailleurs.",
            "es":"Cultura única, ciudades ultra-seguras y excelente atención médica. La nueva Visa Nómada Digital (2024) abre Japón a los trabajadores remotos.",
            "pt":"Cultura única, cidades ultra-seguras e saúde excelente. A nova Visa Nômade Digital (2024) abre o Japão para trabalhadores remotos.",
        }
    },
    {
        "slug":"expat-guide-uae", "iso":"ae",
        "en":"UAE",       "fr":"Émirats Arabes Unis", "es":"Emiratos Árabes Unidos", "pt":"Emirados Árabes Unidos",
        "summary":{
            "en":"0% income tax, luxury lifestyle and world-class connectivity. Dubai's Golden Visa and Green Visa attract top global talent.",
            "fr":"0% d'impôt sur le revenu, style de vie luxueux et connectivité mondiale. Le Golden Visa de Dubaï attire les meilleurs talents du monde.",
            "es":"0% de impuesto sobre la renta, estilo de vida lujoso y conectividad mundial. El Golden Visa de Dubái atrae a los mejores talentos globales.",
            "pt":"0% de imposto de renda, estilo de vida luxuoso e conectividade mundial. O Golden Visa de Dubai atrai os melhores talentos globais.",
        }
    },
    {
        "slug":"expat-guide-colombia", "iso":"co",
        "en":"Colombia",  "fr":"Colombie",  "es":"Colombia",   "pt":"Colômbia",
        "summary":{
            "en":"Affordable living (~$1,200/mo), eternal spring in Medellín and a booming digital nomad scene. Digital Nomad Visa available.",
            "fr":"Vie abordable (~1 200 $/mois), printemps éternel à Medellín et scène nomade en plein essor. Visa nomade numérique disponible.",
            "es":"Vida asequible (~$1,200/mes), primavera eterna en Medellín y una scena nómada en auge. Visa Nómada Digital disponible.",
            "pt":"Custo de vida acessível (~$1.200/mês), primavera eterna em Medellín e cena nômade em expansão. Visa Nômade Digital disponível.",
        }
    },
]

LANG_META = {
    "en": {
        "flag":"fi-gb","label":"English","home":"Home","dest":"Destinations","about":"About","blog":"Blog","guides":"Guides",
        "title":"Expat Guides 2026 — How to Move Abroad | eVisa-Card.com",
        "desc":"Complete expat guides for moving abroad in 2026. Step-by-step immigration process, visas, cost of living, housing & healthcare for 9 countries.",
        "h1":"Expat Guides: Move Abroad in 2026",
        "intro":"Everything you need to know to move abroad. Our expert guides cover the complete relocation process — visas, housing, banking, healthcare and cost of living — for the world's top expat destinations.",
        "card_label":"Read the Guide",
    },
    "fr": {
        "flag":"fi-fr","label":"Français","home":"Accueil","dest":"Destinations","about":"À propos","blog":"Blog","guides":"Guides",
        "title":"Guides Expatrié 2026 — S'installer à l'Étranger | eVisa-Card.com",
        "desc":"Guides complets pour les expatriés qui souhaitent s'installer à l'étranger en 2026. Processus d'immigration, visas, logement et santé pour 9 pays.",
        "h1":"Guides Expatrié : Partir Vivre à l'Étranger en 2026",
        "intro":"Tout ce qu'il faut savoir pour s'expatrier. Nos guides experts couvrent le processus complet — visas, logement, banque, santé et coût de la vie — pour les principales destinations d'expatriation.",
        "card_label":"Lire le Guide",
    },
    "es": {
        "flag":"fi-es","label":"Español","home":"Inicio","dest":"Destinos","about":"Sobre Nosotros","blog":"Blog","guides":"Guías",
        "title":"Guías para Expatriados 2026 — Vivir en el Extranjero | eVisa-Card.com",
        "desc":"Guías completas para expatriados que quieren mudarse al extranjero en 2026. Visas, vivienda, salud y costo de vida para 9 países.",
        "h1":"Guías para Expatriados: Vivir en el Extranjero en 2026",
        "intro":"Todo lo que necesitas saber para emigrar al extranjero. Nuestras guías expertas cubren el proceso completo — visas, vivienda, banca, salud y costo de vida — para los principales destinos de expatriados.",
        "card_label":"Leer la Guía",
    },
    "pt": {
        "flag":"fi-br","label":"Português","home":"Início","dest":"Destinos","about":"Sobre Nós","blog":"Blog","guides":"Guias",
        "title":"Guias para Expatriados 2026 — Morar no Exterior | eVisa-Card.com",
        "desc":"Guias completos para expatriados que querem se mudar para o exterior em 2026. Vistos, moradia, saúde e custo de vida para 9 países.",
        "h1":"Guias para Expatriados: Morar no Exterior em 2026",
        "intro":"Tudo o que você precisa saber para se expatriar. Nossos guias cobrem o processo completo — vistos, moradia, banco, saúde e custo de vida — para os principais destinos de expatriados.",
        "card_label":"Ler o Guia",
    },
}

NAVBAR_STYLE = 'style="background-color:#0d2461 !important;"'

def make_hub(lang):
    lm = LANG_META[lang]
    sw_items = ""
    for tl, tm in LANG_META.items():
        active = ' active' if tl == lang else ''
        sw_items += f'\n                        <a class="dropdown-item{active}" href="/{tl}/expat-guides.html"><span class="fi fi-{tm["flag"].replace("fi-","")}"></span> {tm["label"]}</a>'

    hreflang = "\n".join(f'    <link rel="alternate" hreflang="{tl}" href="https://www.evisa-card.com/{tl}/expat-guides.html"/>' for tl in LANG_META)
    hreflang += f'\n    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/expat-guides.html"/>'

    cards_html = ""
    for c in COUNTRIES:
        name = c[lang]
        summary = c["summary"][lang]
        cards_html += f"""
                <div class="col-md-4 col-sm-6 mb-4 ftco-animate">
                    <div class="card h-100 shadow-sm border-0" style="border-radius:8px;overflow:hidden;">
                        <div style="height:160px;overflow:hidden;position:relative;">
                            <img src="https://flagcdn.com/w640/{c['iso']}.png" alt="{name}" style="width:100%;height:100%;object-fit:cover;object-position:center;"/>
                            <div style="position:absolute;inset:0;background:rgba(13,36,97,0.55);"></div>
                            <h5 style="position:absolute;bottom:12px;left:16px;right:16px;color:#fff;margin:0;font-size:1.2rem;font-weight:700;">{name}</h5>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <p style="font-size:.88rem;color:#555;flex:1;margin-bottom:12px;">{summary}</p>
                            <a href="/{lang}/{c['slug']}.html" class="btn btn-primary btn-sm align-self-start">{lm['card_label']} →</a>
                        </div>
                    </div>
                </div>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <title>{lm['title']}</title>
    <meta name="description" content="{lm['desc']}"/>
    <link rel="canonical" href="https://www.evisa-card.com/{lang}/expat-guides.html"/>
{hreflang}
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" {NAVBAR_STYLE}>
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
                <li class="nav-item"><a class="nav-link active" href="/{lang}/expat-guides.html">{lm['guides']}</a></li>
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

<section class="hero-wrap hero-wrap-2" style="background-image:url('../images/bg_3.jpg');background-size:cover;background-position:center;">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate pb-5 text-center">
                <h1 class="mb-3 bread">{lm['h1']}</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
    <div class="container">
        <div class="row justify-content-center mb-5">
            <div class="col-md-8 text-center">
                <p style="font-size:1.1rem;color:#555;">{lm['intro']}</p>
            </div>
        </div>
        <div class="row">
            {cards_html}
        </div>
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

total = 0
for lang in ["en","fr","es","pt"]:
    html = make_hub(lang)
    out = os.path.join(WWW, lang, "expat-guides.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {lang}/expat-guides.html")
    total += 1

print(f"\nTotal: {total}")
