#!/usr/bin/env python3
"""
gen_schengen_nationality.py
Generates 8 HTML pages in www/en/ for Schengen visa by nationality:
  schengen-visa-for-russian-citizens.html
  schengen-visa-for-turkish-citizens.html
  schengen-visa-for-chinese-citizens.html
  schengen-visa-for-indian-citizens.html
  schengen-visa-for-nigerian-citizens.html
  schengen-visa-for-south-african-citizens.html
  schengen-visa-for-philippine-citizens.html
  schengen-visa-for-indonesian-citizens.html
"""

import os, json

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NATIONALITIES = [
    {
        "slug": "russian",
        "adj": "Russian",
        "demonym": "Russians",
        "country": "Russia",
        "flag": "ru",
        "passport": "Russian passport",
        "meta_desc": "Complete 2026 guide to the Schengen visa for Russian citizens. EUR 80 fee, 15-day processing, required documents, application steps and FAQ for Russians applying for a Schengen visa.",
        "intro_p1": "Russian citizens require a <strong>Schengen visa</strong> to enter any of the 27 Schengen member states. As Russia is not part of the European Union or the Schengen Area, holders of a Russian passport must apply for a short-stay (Type C) visa before travelling to countries such as France, Germany, Italy or Spain.",
        "intro_p2": "The Schengen visa allows Russians to travel freely within the entire Schengen zone for up to 90 days in any 180-day period. Applications are submitted to the embassy or consulate of the main destination country, or through an authorised visa application centre such as VFS Global.",
        "faq": [
            ("Do Russian citizens need a visa for the Schengen Area?", "Yes. Russian passport holders must obtain a Schengen visa (Type C) before travelling to any of the 27 Schengen member states. Visa-free entry is not available for Russian citizens."),
            ("How long does it take to get a Schengen visa for Russians?", "Standard processing takes up to 15 calendar days from the date of application. During peak travel seasons, processing may take up to 45 days in exceptional cases. It is recommended to apply at least 3 to 4 weeks before the intended travel date."),
            ("Can Russian citizens get a multiple-entry Schengen visa?", "Yes. Russian citizens may be granted a multiple-entry Schengen visa valid for 1, 3 or 5 years, depending on their travel history and the issuing consulate. First-time applicants typically receive a single-entry or short-validity visa."),
            ("Which Schengen country should Russians apply to?", "Apply to the embassy or consulate of the country that is your main destination. If visiting multiple countries equally, apply to the country of first entry. Most Russian applicants submit through VFS Global centres in Moscow, Saint Petersburg or other Russian cities."),
        ],
    },
    {
        "slug": "turkish",
        "adj": "Turkish",
        "demonym": "Turkish citizens",
        "country": "Turkey",
        "flag": "tr",
        "passport": "Turkish passport",
        "meta_desc": "Complete 2026 guide to the Schengen visa for Turkish citizens. EUR 80 fee, 15-day processing, required documents, biometrics and step-by-step application process for Turkish passport holders.",
        "intro_p1": "Turkish citizens require a <strong>Schengen visa</strong> to visit any of the 27 countries in the Schengen Area. Despite Turkey being a candidate for EU membership, Turkish passport holders are not exempt from the Schengen visa requirement and must apply before travel.",
        "intro_p2": "The Schengen visa permits Turkish nationals to stay up to 90 days within any 180-day period across the entire Schengen zone. Turkey has several VFS Global and embassy visa application centres in Istanbul, Ankara and other major cities, making the process accessible for applicants throughout the country.",
        "faq": [
            ("Do Turkish citizens need a visa for the Schengen Area?", "Yes. Turkish passport holders must apply for a Schengen visa (Type C) before travelling to any Schengen member state. There is no visa-free arrangement between Turkey and the Schengen Area."),
            ("How much does a Schengen visa cost for Turkish citizens?", "The standard Schengen visa fee is EUR 80 for adults and EUR 40 for children aged 6 to 12. Children under 6 are exempt. An additional service fee applies when applying through VFS Global or similar centres."),
            ("Where do Turkish citizens apply for a Schengen visa?", "Turkish citizens apply at the embassy or consulate of the main destination country or through authorised centres such as VFS Global, iDATA or TLS Contact. Major application centres operate in Istanbul, Ankara, Izmir and Antalya."),
            ("Can Turkish citizens get a long-term Schengen visa?", "Yes. Turkish applicants with a good travel history may receive multiple-entry visas valid for 1, 3 or 5 years. First-time applicants usually receive a single-entry visa covering their specific travel dates."),
        ],
    },
    {
        "slug": "chinese",
        "adj": "Chinese",
        "demonym": "Chinese citizens",
        "country": "China",
        "flag": "cn",
        "passport": "Chinese passport",
        "meta_desc": "Complete 2026 Schengen visa guide for Chinese citizens. EUR 80 fee, 15-day processing, document checklist, application steps and FAQ for Chinese passport holders visiting Europe.",
        "intro_p1": "Chinese citizens require a <strong>Schengen visa</strong> to travel to any of the 27 Schengen member states in Europe. As holders of a Chinese (PRC) passport, applicants must obtain a short-stay visa (Type C) before departure.",
        "intro_p2": "The Schengen visa allows Chinese nationals to travel freely across all 27 member states for up to 90 days in any 180-day period. Applications are processed through embassy consular sections or through authorised visa centres such as VFS Global and TLScontact, with offices in Beijing, Shanghai, Guangzhou and many other Chinese cities.",
        "faq": [
            ("Do Chinese citizens need a visa for the Schengen Area?", "Yes. Chinese passport holders (PRC) must obtain a Schengen visa (Type C) before travelling to any of the 27 Schengen states. There is no visa-free or eVisa option for Chinese citizens visiting the Schengen Area."),
            ("How long does a Schengen visa take for Chinese citizens?", "Standard processing takes up to 15 calendar days. During busy periods such as Chinese New Year or summer holidays, it is advisable to apply 4 to 6 weeks in advance. Some consulates offer express processing for an additional fee."),
            ("What financial proof do Chinese applicants need?", "Chinese citizens should provide bank statements for the last 3 to 6 months showing sufficient funds to cover the trip. A general guideline is at least EUR 50 to 100 per day of stay. Employed applicants should also submit a company letter and payslips."),
            ("Can Chinese citizens get a multiple-entry Schengen visa?", "Yes. Repeat travellers with a clean visa history may receive multiple-entry visas valid for 1 to 5 years. First-time applicants typically receive a visa limited to their planned travel dates."),
        ],
    },
    {
        "slug": "indian",
        "adj": "Indian",
        "demonym": "Indian citizens",
        "country": "India",
        "flag": "in",
        "passport": "Indian passport",
        "meta_desc": "Complete 2026 Schengen visa guide for Indian citizens. EUR 80 fee, 15-day processing, required documents, application steps and FAQ for Indian passport holders travelling to Europe.",
        "intro_p1": "Indian citizens require a <strong>Schengen visa</strong> to visit any of the 27 Schengen member states. Holders of an Indian passport must apply for a short-stay (Type C) visa before travelling to Europe for tourism, business or family visits.",
        "intro_p2": "With a Schengen visa, Indian nationals can travel freely across all 27 member countries for up to 90 days in any 180-day period. India has an extensive network of visa application centres operated by VFS Global in New Delhi, Mumbai, Chennai, Kolkata, Bengaluru, Hyderabad and other cities, making the process widely accessible.",
        "faq": [
            ("Do Indian citizens need a visa for the Schengen Area?", "Yes. Indian passport holders must apply for a Schengen visa (Type C) before visiting any of the 27 Schengen states. There is no visa-free entry for Indian citizens."),
            ("How much does a Schengen visa cost for Indian citizens?", "The standard fee is EUR 80 for adults and EUR 40 for children aged 6 to 12. Children under 6 are exempt. VFS Global charges an additional service fee of approximately EUR 20 to 30 depending on the destination country."),
            ("What is the Schengen visa processing time for Indians?", "Standard processing takes up to 15 calendar days from the date of application. During peak season (April to August), it is recommended to apply at least 30 to 45 days before travel. Some embassies offer priority processing."),
            ("Which Schengen country is easiest for Indians to get a visa?", "Approval rates vary, but France, Germany, Italy and the Netherlands are among the most commonly applied-to countries by Indian travellers. There is no objectively easiest country, as each consulate applies the same Schengen rules."),
        ],
    },
    {
        "slug": "nigerian",
        "adj": "Nigerian",
        "demonym": "Nigerian citizens",
        "country": "Nigeria",
        "flag": "ng",
        "passport": "Nigerian passport",
        "meta_desc": "Complete 2026 Schengen visa guide for Nigerian citizens. EUR 80 fee, 15-day processing, required documents, embassy application process and FAQ for Nigerian passport holders.",
        "intro_p1": "Nigerian citizens require a <strong>Schengen visa</strong> to enter any of the 27 Schengen states in Europe. Holders of a Nigerian passport must apply for a short-stay visa (Type C) through the embassy or consulate of their intended destination country.",
        "intro_p2": "A Schengen visa allows Nigerian nationals to travel across all 27 member states for up to 90 days within a 180-day period. Visa application centres operated by VFS Global and TLScontact are available in Lagos, Abuja and other Nigerian cities. Given higher scrutiny for applications from Nigeria, thorough documentation is essential.",
        "faq": [
            ("Do Nigerian citizens need a visa for the Schengen Area?", "Yes. Nigerian passport holders must obtain a Schengen visa (Type C) before travelling to any Schengen country. There is no visa-free or eVisa option for Nigerian citizens."),
            ("What documents do Nigerians need for a Schengen visa?", "Nigerian applicants need a valid passport (6+ months validity), two passport photos, travel insurance with EUR 30,000 minimum cover, proof of accommodation, return flight reservation, bank statements showing sufficient funds, and an employer or sponsor letter."),
            ("How long does a Schengen visa take for Nigerian citizens?", "Standard processing is up to 15 calendar days. However, applications from Nigeria may sometimes take up to 30 to 45 days due to additional verification. Apply well in advance of your travel date."),
            ("What is the Schengen visa refusal rate for Nigerians?", "Nigeria historically has one of the higher refusal rates. Common reasons include insufficient financial proof, unclear travel purpose or missing documents. Preparing a complete and well-documented application significantly improves approval chances."),
        ],
    },
    {
        "slug": "south-african",
        "adj": "South African",
        "demonym": "South African citizens",
        "country": "South Africa",
        "flag": "za",
        "passport": "South African passport",
        "meta_desc": "Complete 2026 Schengen visa guide for South African citizens. EUR 80 fee, 15-day processing, full document checklist and step-by-step application for South African passport holders.",
        "intro_p1": "South African citizens require a <strong>Schengen visa</strong> to travel to any of the 27 Schengen member states. Holders of a South African passport must apply for a short-stay (Type C) visa before travelling to Europe for tourism, business or family visits.",
        "intro_p2": "The Schengen visa permits South Africans to move freely across all 27 member countries for up to 90 days in any 180-day period. VFS Global operates visa application centres in Pretoria, Cape Town, Durban and other South African cities on behalf of most European embassies.",
        "faq": [
            ("Do South African citizens need a visa for the Schengen Area?", "Yes. South African passport holders must apply for a Schengen visa (Type C) before entering any Schengen state. Visa-free access is not available for South African citizens."),
            ("How much does a Schengen visa cost for South Africans?", "The standard fee is EUR 80 for adults and EUR 40 for children aged 6 to 12. Children under 6 are exempt. VFS Global charges an additional service fee. Payments are typically converted to South African Rand at the current exchange rate."),
            ("Can South Africans get a multiple-entry Schengen visa?", "Yes. Applicants with prior Schengen travel history may be granted a multiple-entry visa valid for 1 to 5 years. First-time applicants usually receive a single-entry visa matching their planned travel dates."),
            ("Where do South Africans apply for a Schengen visa?", "Apply at the embassy or consulate of the main destination country, or through VFS Global centres in Pretoria, Cape Town, Durban or other cities depending on the destination embassy."),
        ],
    },
    {
        "slug": "philippine",
        "adj": "Philippine",
        "demonym": "Filipino citizens",
        "country": "the Philippines",
        "flag": "ph",
        "passport": "Philippine passport",
        "meta_desc": "Complete 2026 Schengen visa guide for Philippine (Filipino) citizens. EUR 80 fee, 15-day processing, document requirements and application steps for Philippine passport holders.",
        "intro_p1": "Philippine (Filipino) citizens require a <strong>Schengen visa</strong> to visit any of the 27 Schengen states in Europe. Holders of a Philippine passport must obtain a short-stay visa (Type C) before departure.",
        "intro_p2": "The Schengen visa allows Filipino nationals to travel across all 27 member countries for up to 90 days within a 180-day period. Visa applications are submitted through VFS Global centres in Manila, Cebu and other cities, or directly at the embassy of the destination country.",
        "faq": [
            ("Do Filipino citizens need a visa for the Schengen Area?", "Yes. Philippine passport holders must apply for a Schengen visa (Type C) before entering any Schengen member state. There is no visa-free or eVisa option for Filipino citizens."),
            ("How long does a Schengen visa take for Filipinos?", "Standard processing takes up to 15 calendar days from the date of application. It is advisable to apply at least 30 days before travel, especially during peak season (March to May and December)."),
            ("What financial documents do Filipinos need for a Schengen visa?", "Filipino applicants should provide bank statements for the last 3 to 6 months, a certificate of employment with salary details, and an Income Tax Return (ITR). Sponsored applicants need an Affidavit of Support and the sponsor bank statements."),
            ("Can Filipinos apply for a Schengen visa in Manila?", "Yes. VFS Global operates Schengen visa application centres in Manila on behalf of most European embassies. Some embassies, such as the German Embassy, also accept direct applications. Check the specific embassy requirements for your destination."),
        ],
    },
    {
        "slug": "indonesian",
        "adj": "Indonesian",
        "demonym": "Indonesian citizens",
        "country": "Indonesia",
        "flag": "id",
        "passport": "Indonesian passport",
        "meta_desc": "Complete 2026 Schengen visa guide for Indonesian citizens. EUR 80 fee, 15-day processing, document requirements, biometrics and application process for Indonesian passport holders.",
        "intro_p1": "Indonesian citizens require a <strong>Schengen visa</strong> to travel to any of the 27 Schengen member states. Holders of an Indonesian passport must apply for a short-stay (Type C) visa before travelling to Europe.",
        "intro_p2": "With a Schengen visa, Indonesian nationals can travel freely across all 27 member countries for up to 90 days in any 180-day period. VFS Global operates application centres in Jakarta, Surabaya, Bali (Denpasar) and Medan, providing convenient access for applicants across the Indonesian archipelago.",
        "faq": [
            ("Do Indonesian citizens need a visa for the Schengen Area?", "Yes. Indonesian passport holders must obtain a Schengen visa (Type C) before travelling to any of the 27 Schengen states. There is no visa-free entry for Indonesian citizens."),
            ("How much does a Schengen visa cost for Indonesians?", "The standard fee is EUR 80 for adults and EUR 40 for children aged 6 to 12. Children under 6 are exempt. VFS Global charges an additional service fee. Payments are typically made in Indonesian Rupiah at the prevailing exchange rate."),
            ("What is the processing time for Indonesians?", "Standard processing takes up to 15 calendar days from application. During peak travel periods such as Lebaran or school holidays, it is recommended to apply 4 to 6 weeks in advance."),
            ("Where can Indonesians apply for a Schengen visa?", "Indonesian citizens can apply through VFS Global centres in Jakarta, Surabaya, Bali (Denpasar) and Medan, or directly at the embassy or consulate of the destination country. The specific centre depends on the Schengen country being visited."),
        ],
    },
]

# ---------------------------------------------------------------------------
# 27 Schengen countries list
# ---------------------------------------------------------------------------
SCHENGEN_COUNTRIES = [
    ("at", "Austria"),   ("be", "Belgium"),     ("hr", "Croatia"),
    ("cz", "Czech Republic"), ("dk", "Denmark"), ("ee", "Estonia"),
    ("fi", "Finland"),   ("fr", "France"),       ("de", "Germany"),
    ("gr", "Greece"),    ("hu", "Hungary"),      ("is", "Iceland"),
    ("it", "Italy"),     ("lv", "Latvia"),       ("li", "Liechtenstein"),
    ("lt", "Lithuania"), ("lu", "Luxembourg"),   ("mt", "Malta"),
    ("nl", "Netherlands"), ("no", "Norway"),     ("pl", "Poland"),
    ("pt", "Portugal"),  ("sk", "Slovakia"),     ("si", "Slovenia"),
    ("es", "Spain"),     ("se", "Sweden"),       ("ch", "Switzerland"),
]

LANGUAGES = [
    ("en", "fi-gb", "English"),
    ("fr", "fi-fr", "Fran\u00e7ais"),
    ("es", "fi-es", "Espa\u00f1ol"),
    ("pt", "fi-br", "Portugu\u00eas"),
    ("zh", "fi-cn", "\u4e2d\u6587"),
    ("th", "fi-th", "\u0e44\u0e17\u0e22"),
    ("ru", "fi-ru", "\u0420\u0443\u0441\u0441\u043a\u0438\u0439"),
    ("ar", "fi-sa", "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"),
    ("ja", "fi-jp", "\u65e5\u672c\u8a9e"),
    ("ko", "fi-kr", "\ud55c\uad6d\uc5b4"),
]


def build_hreflang_tags(slug):
    lines = []
    for lang_code, _, _ in LANGUAGES:
        lines.append(f'    <link rel="alternate" hreflang="{lang_code}" href="https://www.evisa-card.com/{lang_code}/{slug}.html"/>')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}.html"/>')
    return "\n".join(lines)


def build_lang_dropdown(slug):
    items = []
    for lang_code, flag_cls, label in LANGUAGES:
        active = ' active' if lang_code == "en" else ""
        if lang_code == "en":
            href = f"/en/{slug}.html"
        else:
            href = f"/{lang_code}/{slug}.html"
        items.append(f'                        <a class="dropdown-item{active}" href="{href}"><span class="{flag_cls}"></span> {label}</a>')
    return "\n".join(items)


def build_faq_json(faq_list):
    entities = []
    for q, a in faq_list:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a,
            },
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }
    return json.dumps(schema, ensure_ascii=False)


def build_faq_accordion(faq_list):
    cards = []
    for i, (q, a) in enumerate(faq_list, 1):
        faq_id = f"faq{i}"
        collapsed = "" if i == 1 else " collapsed"
        show = " show" if i == 1 else ""
        cards.append(f"""  <div class="card"><div class="card-header"><h5 class="mb-0"><button class="btn btn-link{collapsed}" data-toggle="collapse" data-target="#{faq_id}">{q}</button></h5></div>
  <div id="{faq_id}" class="collapse{show}" data-parent="#faqAccordion"><div class="card-body">{a}</div></div></div>""")
    return "\n".join(cards)


def build_schengen_country_list():
    items = []
    for flag_code, name in SCHENGEN_COUNTRIES:
        items.append(f'    <li><span class="fi fi-{flag_code}"></span> {name}</li>')
    return "\n".join(items)


def build_page(nat):
    slug = f"schengen-visa-for-{nat['slug']}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    adj = nat["adj"]
    flag = nat["flag"]
    title = f"Schengen Visa for {adj} Citizens 2026 &mdash; Requirements, Cost &amp; How to Apply"
    title_plain = f"Schengen Visa for {adj} Citizens 2026 — Requirements, Cost & How to Apply"

    hreflang_tags = build_hreflang_tags(slug)
    lang_dropdown = build_lang_dropdown(slug)
    faq_json = build_faq_json(nat["faq"])
    faq_accordion = build_faq_accordion(nat["faq"])
    schengen_list = build_schengen_country_list()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title_plain}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="description" content="{nat['meta_desc']}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical}"/>
{hreflang_tags}

    <script type="application/ld+json">
    {faq_json}
    </script>

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
<body>
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
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/expat-guides.html">Guides</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
{lang_dropdown}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="hero-wrap hero-wrap-2" style="background-image:url('../images/bg_2.jpg');background-size:cover;background-position:center">
    <div class="overlay"></div>
    <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-center">
            <div class="col-md-9 ftco-animate text-center pb-5">
                <p class="breadcrumbs"><span class="mr-2"><a href="../index.html">Home <i class="fa fa-chevron-right"></i></a></span> <span class="mr-2"><a href="../destination.html">Destinations <i class="fa fa-chevron-right"></i></a></span> <span>Schengen Visa for {adj} Citizens</span></p>
                <h1 class="mb-0 bread"><span class="fi fi-{flag}"></span> {title}</h1>
            </div>
        </div>
    </div>
</section>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<p class="lead">{nat['intro_p1']}</p>
<p>{nat['intro_p2']}</p>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at the official embassy or consulate of your destination country before applying.</p>
</div>

<h2 class="mt-5">Key Facts &mdash; Schengen Visa for {adj} Citizens</h2>
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Schengen Visa Overview for {adj} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Visa Required</span></td></tr>
<tr><th>Visa Type</th><td>Short-stay Schengen Visa (Type C)</td></tr>
<tr><th>Fee</th><td>EUR 80 (adults) / EUR 40 (children 6&ndash;12) / Free (under 6)</td></tr>
<tr><th>Processing Time</th><td>Up to 15 calendar days (standard)</td></tr>
<tr><th>Validity</th><td>Up to 90 days in any 180-day period</td></tr>
<tr><th>Entries</th><td>Single entry, double entry or multiple entry</td></tr>
<tr><th>Territory</th><td>27 Schengen member states</td></tr>
</tbody>
</table>

<h2>Required Documents for {adj} Citizens</h2>
<ol>
<li><strong>Valid {nat['passport']}</strong> &mdash; at least 6 months validity beyond intended stay, issued within the last 10 years, with at least 2 blank pages</li>
<li><strong>Two recent passport-size photographs</strong> &mdash; 35&times;45 mm, white background, taken within the last 6 months</li>
<li><strong>Completed Schengen visa application form</strong> &mdash; signed and dated</li>
<li><strong>Travel medical insurance</strong> &mdash; minimum EUR 30,000 coverage, valid throughout the Schengen Area</li>
<li><strong>Proof of accommodation</strong> &mdash; hotel bookings, rental agreement or invitation letter from a host</li>
<li><strong>Return or onward flight reservation</strong> &mdash; a confirmed booking or reservation (not necessarily purchased)</li>
<li><strong>Proof of financial means</strong> &mdash; bank statements for the last 3&ndash;6 months showing sufficient funds for the trip</li>
<li><strong>Proof of employment or enrollment</strong> &mdash; employer letter with salary details, payslips, business registration, or student enrollment certificate</li>
<li><strong>Travel itinerary</strong> &mdash; day-by-day plan of your trip</li>
<li><strong>Invitation letter</strong> (if applicable) &mdash; from a host in the Schengen Area, including their residence permit or ID</li>
</ol>

<h2>Application Process &mdash; 5 Steps</h2>
<div class="row mb-4">
<div class="col-md-12">
<ol>
<li class="mb-2"><strong>Step 1: Gather Documents</strong> &mdash; Collect all required documents listed above. Ensure your {nat['passport']} has at least 6 months validity and 2 blank pages. Obtain travel insurance with EUR 30,000 minimum cover.</li>
<li class="mb-2"><strong>Step 2: Book an Appointment</strong> &mdash; Schedule an appointment at the embassy, consulate or authorised visa application centre (e.g., VFS Global) of your main destination country. Book early, as appointment slots fill quickly during peak seasons.</li>
<li class="mb-2"><strong>Step 3: Submit Your Application</strong> &mdash; Attend your appointment in person. Submit all documents, the completed application form and the visa fee (EUR 80 for adults, EUR 40 for children 6&ndash;12).</li>
<li class="mb-2"><strong>Step 4: Biometrics</strong> &mdash; Provide biometric data (10 fingerprints and a digital photograph) at the visa application centre. Biometrics are stored in the Visa Information System (VIS) and are valid for 59 months. If you provided biometrics within the last 59 months, you may be exempt.</li>
<li class="mb-2"><strong>Step 5: Collect Your Passport</strong> &mdash; Wait for processing (up to 15 calendar days). Once a decision is made, collect your passport with the visa sticker from the application centre or have it delivered by courier.</li>
</ol>
</div>
</div>

<h2>The 27 Schengen Countries</h2>
<p>{adj} citizens with a valid Schengen visa can travel freely to all of the following countries:</p>
<ul class="list-unstyled" style="column-count:3;column-gap:20px;">
{schengen_list}
</ul>

<h2 class="mt-5">Frequently Asked Questions</h2>
<div class="accordion mb-4" id="faqAccordion">
{faq_accordion}
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Schengen Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="schengen-visa-guide-2026.html">Schengen Visa Guide 2026</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-france.html">France Visa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-germany.html">Germany Visa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-spain.html">Spain Visa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-italy.html">Italy Visa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-netherlands.html">Netherlands Visa</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
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
</html>"""
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for nat in NATIONALITIES:
        slug = f"schengen-visa-for-{nat['slug']}-citizens"
        filename = f"{slug}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        html = build_page(nat)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Created: {filepath}")
    print(f"\nDone — {len(NATIONALITIES)} pages generated in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
