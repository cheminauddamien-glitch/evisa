#!/usr/bin/env python3
"""
Generate missing visa-extension pages for 33 countries in EN.
Template based on existing australia-visa-extension.html structure.
"""
import os, re

BASE = r"C:/Users/chemi/Documents/evisa/pacific-main/www/en"

# Country data: slug -> (name, flag_code, portal_url, portal_name, ext_type, duration, fee, processing, overstay_text, official_link_label)
COUNTRIES = {
    "argentina": ("Argentina", "ar",
        "https://www.migraciones.gov.ar", "Dirección Nacional de Migraciones",
        "Temporary Residence Extension (Prórroga)", "90 days (renewable)",
        "ARS ~7,000 (approx. USD 7)", "2–4 weeks",
        "Overstaying in Argentina can result in fines and a ban from re-entering. The Dirección Nacional de Migraciones may issue a deportation order for serious overstays. Always apply before your current permit expires.",
        "https://www.migraciones.gov.ar", "Argentine Migration Authority"),

    "austria": ("Austria", "at",
        "https://www.bmi.gv.at", "Austrian Ministry of Interior (BMI)",
        "Schengen Stay Extension (rare — exceptional circumstances only)", "Max 90 days total in Schengen zone",
        "EUR 160 (national visa extension)", "2–4 weeks at local immigration office",
        "Overstaying the 90-day Schengen limit is a serious violation. You may be fined, detained, and subject to a Schengen-wide entry ban. Austria enforces Schengen rules strictly.",
        "https://www.bmi.gv.at", "Austrian Federal Ministry of Interior"),

    "belgium": ("Belgium", "be",
        "https://dofi.ibz.be", "Belgian Immigration Office (CGVS/OE)",
        "Short-stay extension (exceptional circumstances only)", "Max 90 days total in Schengen zone",
        "EUR 160 (national visa)", "2–4 weeks",
        "Exceeding 90 days in the Schengen Area without authorisation is a violation. Belgium may impose fines, detention and a Schengen re-entry ban. Contact the Aliens Office immediately if your situation changes.",
        "https://dofi.ibz.be", "Belgian Immigration Office"),

    "brazil": ("Brazil", "br",
        "https://www.gov.br/pf/en", "Federal Police of Brazil (Polícia Federal)",
        "Tourist Stay Extension", "90 days (max 180 days/year)",
        "BRL 200 (~USD 40)", "Same-day at Federal Police office",
        "Overstaying in Brazil results in a daily fine (BRL 100/day up to BRL 10,000) and possible deportation. Repeat overstays may lead to a ban from future entry.",
        "https://www.gov.br/pf/en", "Brazilian Federal Police"),

    "china": ("China", "cn",
        "https://www.nia.gov.cn", "National Immigration Administration of China (NIA)",
        "Stay Extension (延长停留期限)", "Varies by visa type (tourist: usually +30 days)",
        "CNY 50–200 (~USD 7–28)", "5–7 working days at local Exit-Entry Bureau",
        "Overstaying in China carries heavy fines (CNY 500/day, up to CNY 10,000) and can lead to detention, deportation, and a future entry ban. The Chinese government tracks overstays closely.",
        "https://www.nia.gov.cn", "National Immigration Administration of China"),

    "colombia": ("Colombia", "co",
        "https://www.migracioncolombia.gov.co", "Migración Colombia",
        "Salvoconducto (emergency stay permit) or PTP extension", "Up to 90 days",
        "COP 90,000–200,000 (~USD 22–50)", "1–5 business days",
        "Overstaying in Colombia without a valid permit results in fines and a mandatory exit order. Repeat overstays can result in being barred from future entry. Always regularise your status with Migración Colombia before your current permit expires.",
        "https://www.migracioncolombia.gov.co", "Migración Colombia"),

    "costa-rica": ("Costa Rica", "cr",
        "https://www.migracion.go.cr", "General Directorate of Migration (DGME)",
        "Tourist Stay Extension", "Up to 90 days",
        "CRC 3,000–5,000 (~USD 5–9)", "Same day at DGME offices",
        "Overstaying in Costa Rica results in fines and possible detention. The DGME may issue a deportation order. Many travelers use border runs to reset their 90-day stay, but the government has tightened enforcement.",
        "https://www.migracion.go.cr", "Costa Rica DGME"),

    "croatia": ("Croatia", "hr",
        "https://mup.gov.hr", "Croatian Ministry of Interior (MUP)",
        "Short-stay Schengen extension (exceptional)", "Max 90 days in Schengen zone",
        "EUR 100 (approximate)", "Contact local police for emergency extension",
        "Croatia is a full Schengen member since 2023. Overstaying the 90-day limit is a violation that can result in fines, deportation and a Schengen entry ban.",
        "https://mup.gov.hr", "Croatian Ministry of Interior"),

    "czech-republic": ("Czech Republic", "cz",
        "https://www.mvcr.cz/mvcren", "Ministry of Interior of the Czech Republic",
        "Short-stay Schengen extension (force majeure only)", "Max 90 days in Schengen",
        "CZK 1,500 (~EUR 60)", "Contact local Foreign Police immediately",
        "Overstaying the Schengen limit in the Czech Republic is a serious offence. The Foreign Police can detain and deport overstayers and impose a Schengen entry ban.",
        "https://www.mvcr.cz/mvcren", "Czech Ministry of Interior"),

    "denmark": ("Denmark", "dk",
        "https://www.nyidanmark.dk/en-GB", "Danish Immigration Service (SIRI)",
        "Schengen short-stay extension (exceptional circumstances)", "Max 90 days in Schengen",
        "DKK 1,800 (~EUR 240)", "Apply at Danish Agency for International Recruitment and Integration",
        "Overstaying the 90-day Schengen limit in Denmark results in fines, deportation and a Schengen entry ban. Denmark has strict border controls and registration requirements.",
        "https://www.nyidanmark.dk/en-GB", "Danish Immigration Service"),

    "france": ("France", "fr",
        "https://www.immigration.interieur.gouv.fr", "French Ministry of the Interior — DGEF",
        "Schengen short-stay extension (force majeure / humanitarian)", "Max 90 days in Schengen",
        "EUR 99 (visa de retour) or free (force majeure)", "Apply at local prefecture",
        "Overstaying in France (and the Schengen area) is an administrative violation. You may be issued an OQTF (Obligation de Quitter le Territoire Français) and face a Schengen re-entry ban of 1–3 years.",
        "https://www.immigration.interieur.gouv.fr", "French Interior Ministry"),

    "germany": ("Germany", "de",
        "https://www.bamf.de/EN", "Federal Office for Migration and Refugees (BAMF)",
        "Schengen short-stay extension (exceptional)", "Max 90 days in Schengen",
        "EUR 50–100", "Apply at local Ausländerbehörde (immigration office)",
        "Overstaying the Schengen 90-day limit in Germany can result in deportation, a Schengen-wide re-entry ban, and a permanent note on your immigration record. The Ausländerbehörde is strict about enforcement.",
        "https://www.bamf.de/EN", "German BAMF"),

    "greece": ("Greece", "gr",
        "https://migration.gov.gr/en", "Greek Ministry of Migration and Asylum",
        "Schengen short-stay extension (humanitarian / force majeure)", "Max 90 days in Schengen",
        "EUR 30–100", "Apply at the Regional Asylum Service or local police",
        "Overstaying the Schengen limit in Greece can result in deportation and a 3-year Schengen entry ban. Greece has strengthened immigration enforcement in recent years.",
        "https://migration.gov.gr/en", "Greek Ministry of Migration"),

    "hong-kong": ("Hong Kong", "hk",
        "https://www.immd.gov.hk/eng/index.html", "Hong Kong Immigration Department",
        "Extension of Stay", "Usually in multiples of weeks up to 12 months",
        "HKD 230 (~USD 30)", "Same day at Immigration Tower (Wan Chai)",
        "Overstaying in Hong Kong without valid permission is a criminal offence. Overstayers may be detained and prosecuted. This can result in a ban from future entry to Hong Kong.",
        "https://www.immd.gov.hk/eng/index.html", "HK Immigration Department"),

    "hungary": ("Hungary", "hu",
        "https://www.police.hu/en/content/immigration", "National Directorate-General for Aliens Policing (OIF)",
        "Schengen short-stay extension (humanitarian)", "Max 90 days in Schengen",
        "HUF 7,500 (~EUR 20)", "Apply at Hungarian Immigration Police",
        "Hungary enforces Schengen 90-day rules. Overstaying can result in an expulsion order and a Schengen entry ban. Contact the OIF before your visa expires.",
        "https://www.police.hu/en/content/immigration", "Hungarian Immigration Police"),

    "ireland": ("Ireland", "ie",
        "https://www.inis.gov.ie", "Irish Naturalisation and Immigration Service (INIS)",
        "Tourist Stamp Extension (Stamp 0 / Stamp 1)", "2–6 months (discretionary)",
        "EUR 300 (application fee)", "4–8 weeks at INIS offices",
        "Ireland is not in the Schengen Area and applies its own immigration rules. Overstaying in Ireland can result in detention and removal, and may affect future visa applications. Always apply for an extension before your current leave to remain expires.",
        "https://www.inis.gov.ie", "Irish INIS"),

    "italy": ("Italy", "it",
        "https://www.interno.gov.it/en", "Italian Ministry of the Interior (Questura)",
        "Permesso di soggiorno extension (short-stay exceptional)", "Max 90 days in Schengen",
        "EUR 73.50–206 (varies)", "Apply at local Questura or Post Office (Sportello Amico)",
        "Italy enforces the Schengen 90-day rule strictly. Overstaying can result in an expulsion decree (decreto di espulsione) and a Schengen re-entry ban of 3–5 years.",
        "https://www.interno.gov.it/en", "Italian Ministry of Interior"),

    "jordan": ("Jordan", "jo",
        "https://www.psd.gov.jo", "Public Security Directorate (Jawazat)",
        "Tourist Stay Extension (via Jawazat)", "1–3 months",
        "JOD 1–3/day (after first month)", "Same day at Jawazat offices",
        "Overstaying in Jordan triggers daily fines (JOD 1.5/day). You cannot leave the country without paying all outstanding fines at the airport. Long overstays can also lead to deportation.",
        "https://www.psd.gov.jo", "Jordan Public Security Directorate"),

    "maldives": ("Maldives", "mv",
        "https://immigration.gov.mv", "Maldives Immigration",
        "Tourist Visa Extension", "Up to 90 days",
        "USD 90 (30-day extension)", "3–5 working days",
        "Overstaying in the Maldives is taken seriously. Overstayers are fined USD 100/day and may face deportation and a future entry ban. Extensions must be applied for before the current stamp expires.",
        "https://immigration.gov.mv", "Maldives Immigration"),

    "mexico": ("Mexico", "mx",
        "https://www.inm.gob.mx", "Instituto Nacional de Migración (INM)",
        "FMM Tourist Card Extension (rarely granted)", "Up to 180 days total",
        "MXN 500–900 (~USD 25–45)", "Apply at INM offices",
        "Mexico generally allows up to 180 days for tourists. Overstaying results in fines proportional to the overstay duration and can lead to deportation and a ban from future entry. Always clarify your FMM card duration at entry.",
        "https://www.inm.gob.mx", "Mexican National Migration Institute"),

    "nepal": ("Nepal", "np",
        "https://www.immigration.gov.np", "Department of Immigration Nepal",
        "Tourist Visa Extension", "Up to 150 days per year",
        "USD 25 (15 days) / USD 2/day (up to 30 extra days)", "Same day at Kathmandu or Pokhara immigration",
        "Nepal has a strict 150-day annual limit for tourists. Overstaying results in fines and can lead to detention at the airport upon departure. Always extend before your visa expires.",
        "https://www.immigration.gov.np", "Nepal Department of Immigration"),

    "netherlands": ("Netherlands", "nl",
        "https://ind.nl/en", "Immigration and Naturalisation Service (IND)",
        "Schengen short-stay extension (exceptional circumstances)", "Max 90 days in Schengen",
        "EUR 192", "Apply at IND Desk",
        "The Netherlands strictly enforces Schengen 90-day rules. Overstaying can result in an expulsion order and a Schengen entry ban. The IND monitors overstays closely.",
        "https://ind.nl/en", "Dutch Immigration and Naturalisation Service"),

    "norway": ("Norway", "no",
        "https://www.udi.no/en", "Norwegian Directorate of Immigration (UDI)",
        "Schengen short-stay extension (force majeure / humanitarian)", "Max 90 days in Schengen",
        "NOK 690 (~EUR 60)", "Apply at UDI Service Centre",
        "Norway is a Schengen associate member. Overstaying the 90-day Schengen limit can result in fines, deportation and a Schengen entry ban. The UDI has strict policies on overstays.",
        "https://www.udi.no/en", "Norwegian Directorate of Immigration"),

    "poland": ("Poland", "pl",
        "https://www.gov.pl/web/udsc/aliens", "Office for Foreigners (Urząd do Spraw Cudzoziemców)",
        "Schengen short-stay extension (humanitarian)", "Max 90 days in Schengen",
        "PLN 340 (~EUR 80)", "Apply at Provincial Governor (Voivode) office",
        "Poland enforces Schengen rules. Overstaying can result in an obligation to leave the Schengen Area and a re-entry ban. Contact the Office for Foreigners immediately.",
        "https://www.gov.pl/web/udsc/aliens", "Polish Office for Foreigners"),

    "portugal": ("Portugal", "pt",
        "https://www.sef.pt/en", "Immigration and Borders Service (SEF / AIMA)",
        "Schengen short-stay extension (exceptional)", "Max 90 days in Schengen",
        "EUR 72", "Apply at AIMA (previously SEF) local office",
        "Portugal enforces Schengen 90-day rules. Overstaying can result in a fine, deportation and a Schengen re-entry ban. Contact AIMA immediately if your stay needs to be extended.",
        "https://www.sef.pt/en", "AIMA Portugal"),

    "qatar": ("Qatar", "qa",
        "https://www.moi.gov.qa/site/english/home.html", "Ministry of Interior Qatar",
        "Tourist Visa Extension (via Hayya / MOI portal)", "30 days",
        "QAR 200 (~USD 55)", "Online via MOI portal or immigration offices",
        "Overstaying in Qatar results in fines (QAR 200 per day) and potential deportation. You may also be banned from re-entering Qatar. Always extend your visa before it expires via the MOI portal.",
        "https://www.moi.gov.qa/site/english/home.html", "Qatar Ministry of Interior"),

    "romania": ("Romania", "ro",
        "https://igi.mai.gov.ro/en", "General Inspectorate for Immigration (IGI)",
        "Short-stay extension (exceptional)", "Max 90 days in Schengen / Schengen-equivalent",
        "RON 255 (~EUR 50)", "Apply at IGI territorial structures",
        "Romania joined the Schengen Area in 2024 (air/sea borders). Overstaying the permitted period can result in expulsion and a re-entry ban. Contact IGI immediately if you need an extension.",
        "https://igi.mai.gov.ro/en", "Romanian General Inspectorate for Immigration"),

    "spain": ("Spain", "es",
        "https://sede.administracionespublicas.gob.es", "Spanish National Police — Foreigners Office",
        "Schengen short-stay extension (exceptional circumstances only)", "Max 90 days in Schengen",
        "EUR 51 (Tasas — Form 790)", "Apply at local Oficina de Extranjería",
        "Spain strictly enforces the Schengen 90-day limit. Overstaying can result in an expulsion order, heavy fines, and a Schengen re-entry ban of up to 5 years. Apply for an extension before your 90 days expire.",
        "https://sede.administracionespublicas.gob.es", "Spanish Foreigners Office"),

    "sri-lanka": ("Sri Lanka", "lk",
        "https://eservices.immigration.gov.lk", "Department of Immigration and Emigration Sri Lanka",
        "Tourist Visa Extension (ETA Extension)", "30-day increments (max 6 months)",
        "USD 40 (30 days) per extension", "Same day online or at Colombo offices",
        "Overstaying in Sri Lanka results in fines (USD 3/day) and possible detention. You cannot depart without paying outstanding fines. Sri Lanka has recently tightened overstay enforcement.",
        "https://eservices.immigration.gov.lk", "Sri Lanka Department of Immigration"),

    "sweden": ("Sweden", "se",
        "https://www.migrationsverket.se/en", "Swedish Migration Agency (Migrationsverket)",
        "Schengen short-stay extension (force majeure / medical)", "Max 90 days in Schengen",
        "SEK 1,500 (~EUR 130)", "Apply at Migrationsverket",
        "Sweden enforces Schengen rules. Overstaying can result in an expulsion decision and a Schengen re-entry ban. The Swedish Migration Agency has clear procedures for force majeure extensions.",
        "https://www.migrationsverket.se/en", "Swedish Migration Agency"),

    "switzerland": ("Switzerland", "ch",
        "https://www.sem.admin.ch/sem/en/home.html", "State Secretariat for Migration (SEM)",
        "Schengen short-stay extension (exceptional circumstances)", "Max 90 days in Schengen",
        "CHF 60–150", "Apply at cantonal migration office",
        "Switzerland is a Schengen associate. Overstaying the 90-day Schengen period can result in fines, deportation and a Schengen re-entry ban. Contact the SEM or your cantonal migration office immediately.",
        "https://www.sem.admin.ch/sem/en/home.html", "Swiss State Secretariat for Migration"),

    "taiwan": ("Taiwan", "tw",
        "https://www.immigration.gov.tw/5385/7244/7250/7317", "National Immigration Agency (NIA) Taiwan",
        "Visitor Visa Extension", "30 days per extension (max 6 months)",
        "TWD 300 (~USD 10)", "Same day at NIA service centres",
        "Overstaying in Taiwan results in fines (TWD 2,000–10,000) and a ban from re-entering for 1–10 years depending on the length of the overstay. Always extend before your visa expires at a local NIA office.",
        "https://www.immigration.gov.tw", "Taiwan National Immigration Agency"),

    "united-kingdom": ("United Kingdom", "gb",
        "https://www.gov.uk/extend-uk-visa", "UK Visas and Immigration (UKVI)",
        "Standard Visitor Visa Extension (rarely granted, exceptional only)", "Subject to individual circumstances",
        "GBP 993 (leave to remain application fee)", "8 weeks processing at UKVI",
        "Overstaying in the UK is a criminal offence. You may be detained, deported, and banned from re-entering the UK for 1–10 years. Overstays are recorded on your immigration history and will seriously affect future UK visa applications.",
        "https://www.gov.uk/extend-uk-visa", "UK Government — Extend a UK Visa"),
}

NAVBAR_EN = '''<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
<div class="container">
    <a class="navbar-brand" href="../index.html" style="padding:0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:120px;width:auto;display:block;"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation"><span class="oi oi-menu"></span> Menu</button>
    <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
        <ul class="navbar-nav align-items-center">
            <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
            <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
            <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
            <li class="nav-item"><a class="nav-link" href="/en/expat-guides.html">Guides</a></li>
            <li class="nav-item dropdown ml-3">
                <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                    <span class="fi fi-gb"></span> English</a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                    <a class="dropdown-item active" href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>
                    <a class="dropdown-item" href="/fr/destination.html"><span class="fi fi-fr"></span> Français</a>
                    <a class="dropdown-item" href="/es/destination.html"><span class="fi fi-es"></span> Español</a>
                    <a class="dropdown-item" href="/pt/destination.html"><span class="fi fi-br"></span> Português</a>
                    <a class="dropdown-item" href="/zh/destination.html"><span class="fi fi-cn"></span> 中文</a>
                    <a class="dropdown-item" href="/th/destination.html"><span class="fi fi-th"></span> ไทย</a>
                    <a class="dropdown-item" href="/ru/destination.html"><span class="fi fi-ru"></span> Русский</a>
                    <a class="dropdown-item" href="/ar/destination.html"><span class="fi fi-sa"></span> العربية</a>
                    <a class="dropdown-item" href="/ja/destination.html"><span class="fi fi-jp"></span> 日本語</a>
                    <a class="dropdown-item" href="/ko/destination.html"><span class="fi fi-kr"></span> 한국어</a>
                </div>
            </li>
        </ul>
    </div>
</div>
</nav>'''

JS_BLOCK = '''<div class="show fullscreen" id="ftco-loader">
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
<script src="../js/jquery.animateNumber.min.js"></script>
<script src="../js/bootstrap-datepicker.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/google-map.js"></script>
<script src="../js/main.js"></script>'''

def make_page(slug, name, flag, portal_url, portal_name, ext_type, duration, fee, proc_time, overstay, link_url, link_label):
    fname = f"{slug}-visa-extension.html"
    # Check if already exists
    if os.path.exists(os.path.join(BASE, fname)):
        return None

    nav = NAVBAR_EN.replace("{slug}", slug)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{name} Visa Extension 2026 — How to Extend, Cost &amp; Requirements</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{name} visa extension 2026: how to extend your stay, fees, required documents and overstay consequences. Complete guide."/>
    <meta name="keywords" content="{name.lower()} visa extension 2026, extend {name.lower()} visa, {name.lower()} stay extension, {name.lower()} overstay"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>
    <meta property="og:title" content="{name} Visa Extension 2026 — How to Extend, Cost &amp; Requirements"/>
    <meta property="og:description" content="{name} visa extension 2026: how to extend your stay, fees, required documents and overstay consequences."/>
    <meta property="og:type" content="website"/>
    <meta property="og:url" content="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>
    <meta property="og:image" content="https://www.evisa-card.com/images/og-image.jpg"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&amp;display=swap" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/bootstrap-datepicker.css" rel="stylesheet"/>
    <link href="../css/jquery.timepicker.css" rel="stylesheet"/>
    <link href="../css/flaticon.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{nav}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag} mr-2"></span>How to Extend Your {name} Visa in 2026</h1>
<p class="lead">Extending your stay in {name} requires applying through the official immigration authority before your current visa or permitted stay expires. This guide covers the extension process, fees, documents required and the consequences of overstaying.</p>

<h2 id="overview">Extension at a Glance</h2>
<p>Apply <strong>before your current visa expires</strong> to remain in legal status throughout the process.</p>
<div class="table-responsive">
<table class="table table-bordered table-sm mt-3 mb-4">
<thead class="thead-dark">
<tr><th>Extension Type</th><th>Duration</th><th>Fee</th><th>Where to Apply</th><th>Processing Time</th></tr>
</thead>
<tbody>
<tr>
<td>{ext_type}</td>
<td>{duration}</td>
<td>{fee}</td>
<td><a href="{portal_url}" target="_blank" rel="noopener">{portal_name}</a></td>
<td>{proc_time}</td>
</tr>
</tbody>
</table>
</div>

<h2 id="can-extend">Can You Extend Your {name} Visa?</h2>
<p>Yes, in most cases tourists can request a stay extension through <a href="{portal_url}" target="_blank" rel="noopener">{portal_name}</a>. Extensions are typically processed within <strong>{proc_time}</strong>. The standard fee is <strong>{fee}</strong>. You must apply before your current authorised stay expires — applying in time ensures you remain in lawful status during processing.</p>

<h2 id="requirements">Requirements &amp; Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond requested stay)</li>
<li>Current {name} visa or entry stamp (not yet expired)</li>
<li>Completed extension application form (available from {portal_name})</li>
<li>Proof of sufficient funds (recent bank statement)</li>
<li>Proof of accommodation in {name}</li>
<li>Onward or return travel booking</li>
<li>Proof of reason for extension (if required)</li>
<li>Application fee: <strong>{fee}</strong></li>
</ul>

<h2 id="steps">Step-by-Step Extension Process</h2>
<ol>
<li class="mb-2"><strong>Gather your documents</strong><br>Prepare passport, bank statements, accommodation proof, and a completed application form before visiting the immigration office.</li>
<li class="mb-2"><strong>Visit or apply online at {portal_name}</strong><br>Submit your extension application at <a href="{portal_url}" target="_blank" rel="noopener">{portal_url}</a> or at a local immigration office.</li>
<li class="mb-2"><strong>Pay the fee</strong><br>The current standard fee is <strong>{fee}</strong>. Payment is usually required at the time of application.</li>
<li class="mb-2"><strong>Wait for processing</strong><br>Processing typically takes <strong>{proc_time}</strong>. Do not depart {name} while your application is pending if you have not been granted a bridging status.</li>
<li class="mb-2"><strong>Receive your extension</strong><br>Your new authorised stay will be noted in your passport or issued as an official document. Keep a copy for your records.</li>
</ol>

<h2 id="overstay">Overstay Consequences — Important!</h2>
<div class="alert alert-danger">
<span class="fa fa-exclamation-triangle mr-1"></span>
<strong>Warning:</strong> Overstaying your visa or authorised stay in {name} can have serious consequences.
</div>
<p>{overstay}</p>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <div class="d-flex align-items-start">
        <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
        <div>
            <strong>Editorial Team &mdash; eVisa-Card.com</strong>
            <p class="mb-1 small text-muted">This guide is maintained by our visa research team. Last updated: <strong>March 2026</strong>.</p>
            <p class="mb-0 small"><strong>Important:</strong> Visa extension rules change frequently. Always verify current requirements at <a href="{link_url}" target="_blank" rel="noopener">{link_label}</a> before making travel plans. This page is for informational purposes only.</p>
        </div>
    </div>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related {name} Visa Guides</h3>
    <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{slug}.html">{name} Visa Overview</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{slug}-visa-requirements.html">{name} Visa Requirements</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{slug}-visa-fees.html">{name} Visa Fees</a>
        <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
    </div>
</div>

</article>
</div>
</section>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type":"Question","name":"Can I extend my {name} visa while inside the country?","acceptedAnswer":{{"@type":"Answer","text":"Yes. You can apply for a {name} visa extension through {portal_name} before your current authorised stay expires. The standard extension type is: {ext_type}. Processing takes approximately {proc_time}."}}}},
    {{"@type":"Question","name":"How long does a {name} visa extension take?","acceptedAnswer":{{"@type":"Answer","text":"Processing time for a {name} visa extension is approximately: {proc_time}. Always apply well before your current visa or permitted stay expires to avoid any lapse in status."}}}},
    {{"@type":"Question","name":"What is the fee for a {name} visa extension?","acceptedAnswer":{{"@type":"Answer","text":"The standard fee for a {name} visa extension is {fee}. Additional service fees may apply. Always confirm current rates with {portal_name}."}}}},
    {{"@type":"Question","name":"What happens if I overstay my {name} visa?","acceptedAnswer":{{"@type":"Answer","text":"{overstay}"}}}}
  ]
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Apply for a {name} Visa Extension",
  "description": "Step-by-step guide to extending your {name} tourist visa in 2026.",
  "step": [
    {{"@type":"HowToStep","name":"Step 1: Gather documents","text":"Prepare passport, bank statements, accommodation proof, and a completed application form."}},
    {{"@type":"HowToStep","name":"Step 2: Apply at {portal_name}","text":"Submit your extension application online or at a local immigration office."}},
    {{"@type":"HowToStep","name":"Step 3: Pay the fee","text":"The current standard fee is {fee}. Payment is required at the time of application."}},
    {{"@type":"HowToStep","name":"Step 4: Wait for processing","text":"Processing typically takes {proc_time}."}},
    {{"@type":"HowToStep","name":"Step 5: Receive your extension","text":"Your new authorised stay will be noted in your passport or issued as an official document."}}
  ]
}}
</script>

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
{JS_BLOCK}
</body>
</html>"""
    return fname, html

created = 0
for slug, data in COUNTRIES.items():
    name, flag, portal_url, portal_name, ext_type, duration, fee, proc_time, overstay, link_url, link_label = data
    result = make_page(slug, name, flag, portal_url, portal_name, ext_type, duration, fee, proc_time, overstay, link_url, link_label)
    if result is None:
        print(f"  SKIP (exists): {slug}-visa-extension.html")
        continue
    fname, html = result
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {fname}")
    created += 1

print(f"\nDONE — {created} extension pages created")
