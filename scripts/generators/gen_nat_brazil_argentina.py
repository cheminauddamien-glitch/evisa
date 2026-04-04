#!/usr/bin/env python3
"""
gen_nat_brazil_argentina.py
Generates 40 HTML pages in www/en/:
  brazil-visa-for-{nat}-citizens.html   (20 nationalities)
  argentina-visa-for-{nat}-citizens.html (20 nationalities)
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

NATIONALITIES = [
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "indian", "chinese", "russian", "brazilian", "mexican", "south-african",
    "nigerian", "korean", "singaporean", "indonesian", "philippine",
    "turkish", "argentinian",
]

# --- nationality metadata ---
NAT_META = {
    "us":           {"label": "US",           "adj": "American",      "flag": "us", "passport": "US passport",          "demonym": "Americans"},
    "uk":           {"label": "UK",           "adj": "British",       "flag": "gb", "passport": "British passport",      "demonym": "British citizens"},
    "canadian":     {"label": "Canadian",     "adj": "Canadian",      "flag": "ca", "passport": "Canadian passport",     "demonym": "Canadians"},
    "french":       {"label": "French",       "adj": "French",        "flag": "fr", "passport": "French passport",       "demonym": "French citizens"},
    "german":       {"label": "German",       "adj": "German",        "flag": "de", "passport": "German passport",       "demonym": "Germans"},
    "japanese":     {"label": "Japanese",     "adj": "Japanese",      "flag": "jp", "passport": "Japanese passport",     "demonym": "Japanese citizens"},
    "australian":   {"label": "Australian",   "adj": "Australian",    "flag": "au", "passport": "Australian passport",   "demonym": "Australians"},
    "indian":       {"label": "Indian",       "adj": "Indian",        "flag": "in", "passport": "Indian passport",       "demonym": "Indians"},
    "chinese":      {"label": "Chinese",      "adj": "Chinese",       "flag": "cn", "passport": "Chinese passport",      "demonym": "Chinese citizens"},
    "russian":      {"label": "Russian",      "adj": "Russian",       "flag": "ru", "passport": "Russian passport",      "demonym": "Russians"},
    "brazilian":    {"label": "Brazilian",    "adj": "Brazilian",     "flag": "br", "passport": "Brazilian passport",    "demonym": "Brazilians"},
    "mexican":      {"label": "Mexican",      "adj": "Mexican",       "flag": "mx", "passport": "Mexican passport",      "demonym": "Mexicans"},
    "south-african":{"label": "South African","adj": "South African", "flag": "za", "passport": "South African passport","demonym": "South Africans"},
    "nigerian":     {"label": "Nigerian",     "adj": "Nigerian",      "flag": "ng", "passport": "Nigerian passport",     "demonym": "Nigerians"},
    "korean":       {"label": "Korean",       "adj": "Korean",        "flag": "kr", "passport": "Korean passport",       "demonym": "Koreans"},
    "singaporean":  {"label": "Singaporean",  "adj": "Singaporean",   "flag": "sg", "passport": "Singaporean passport",  "demonym": "Singaporeans"},
    "indonesian":   {"label": "Indonesian",   "adj": "Indonesian",    "flag": "id", "passport": "Indonesian passport",   "demonym": "Indonesians"},
    "philippine":   {"label": "Philippine",   "adj": "Philippine",    "flag": "ph", "passport": "Philippine passport",   "demonym": "Filipinos"},
    "turkish":      {"label": "Turkish",      "adj": "Turkish",       "flag": "tr", "passport": "Turkish passport",      "demonym": "Turkish citizens"},
    "argentinian":  {"label": "Argentinian",  "adj": "Argentinian",   "flag": "ar", "passport": "Argentinian passport",  "demonym": "Argentinians"},
}

# -----------------------------------------------------------------------
# BRAZIL visa status per nationality
# -----------------------------------------------------------------------
BRAZIL_STATUS = {
    # Visa-free bilateral/Mercosur 90 days
    "french":       {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "german":       {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "uk":           {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "canadian":     {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "japanese":     {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "korean":       {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "singaporean":  {"status": "visa_free",  "stay": "90 days", "basis": "Bilateral agreement",          "fee": "Free",    "processing": "No visa needed"},
    "mexican":      {"status": "visa_free",  "stay": "90 days", "basis": "Mercosur / bilateral",         "fee": "Free",    "processing": "No visa needed"},
    "argentinian":  {"status": "visa_free",  "stay": "90 days", "basis": "Mercosur",                     "fee": "Free",    "processing": "No visa needed"},
    # Visa-free since 2024 (reciprocity abolished)
    "us":           {"status": "visa_free",  "stay": "90 days", "basis": "Reciprocity abolished (2024)", "fee": "Free",    "processing": "No visa needed"},
    "australian":   {"status": "visa_free",  "stay": "90 days", "basis": "Reciprocity abolished (2024)", "fee": "Free",    "processing": "No visa needed"},
    # eVisa USD 80
    "chinese":      {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "russian":      {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "indonesian":   {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "philippine":   {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "nigerian":     {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "south-african":{"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    "turkish":      {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    # eVisa or consular
    "indian":       {"status": "evisa",      "stay": "90 days", "basis": "eVisa (gov.br)",               "fee": "USD 80",  "processing": "Up to 72 hours"},
    # Visa-free (self-reference)
    "brazilian":    {"status": "national",   "stay": "N/A",     "basis": "Brazilian national",           "fee": "Free",    "processing": "N/A"},
}

# -----------------------------------------------------------------------
# ARGENTINA visa status per nationality
# -----------------------------------------------------------------------
ARGENTINA_STATUS = {
    # Visa-free 90 days
    "us":           {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "uk":           {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "canadian":     {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "french":       {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "german":       {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "japanese":     {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "australian":   {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "korean":       {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "singaporean":  {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "brazilian":    {"status": "visa_free", "stay": "90 days", "basis": "Mercosur",               "fee": "Free", "processing": "No visa needed"},
    "mexican":      {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "russian":      {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "chinese":      {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    "turkish":      {"status": "visa_free", "stay": "90 days", "basis": "Bilateral agreement",    "fee": "Free", "processing": "No visa needed"},
    # Visa required
    "indian":       {"status": "visa_req",  "stay": "As granted", "basis": "Tourist visa required", "fee": "Varies", "processing": "4–8 weeks"},
    "indonesian":   {"status": "visa_req",  "stay": "As granted", "basis": "Tourist visa required", "fee": "Varies", "processing": "4–8 weeks"},
    "philippine":   {"status": "visa_req",  "stay": "As granted", "basis": "Tourist visa required", "fee": "Varies", "processing": "4–8 weeks"},
    "nigerian":     {"status": "visa_req",  "stay": "As granted", "basis": "Tourist visa required", "fee": "Varies", "processing": "4–8 weeks"},
    "south-african":{"status": "visa_req",  "stay": "As granted", "basis": "Tourist visa required", "fee": "Varies", "processing": "4–8 weeks"},
    # National
    "argentinian":  {"status": "national",  "stay": "N/A", "basis": "Argentine national", "fee": "Free", "processing": "N/A"},
}

# -----------------------------------------------------------------------
# Helper: status badge HTML
# -----------------------------------------------------------------------
def status_badge(status, dest):
    if status == "visa_free":
        return '<span style="color:green;font-weight:600;">Visa-Free ✓</span>'
    elif status == "evisa":
        return '<span style="color:#d97706;font-weight:600;">eVisa Required</span>'
    elif status == "visa_req":
        return '<span style="color:red;font-weight:600;">Visa Required</span>'
    elif status == "national":
        return '<span style="color:blue;font-weight:600;">Domestic (national)</span>'
    return ""


# -----------------------------------------------------------------------
# Brazil page builder
# -----------------------------------------------------------------------
def build_brazil_page(nat):
    m = NAT_META[nat]
    s = BRAZIL_STATUS[nat]
    adj = m["adj"]
    flag = m["flag"]
    label = m["label"]
    demonym = m["demonym"]
    status = s["status"]
    stay = s["stay"]
    basis = s["basis"]
    fee = s["fee"]
    processing = s["processing"]
    slug = f"brazil-visa-for-{nat}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    badge = status_badge(status, "Brazil")

    if status == "national":
        meta_desc = f"Brazilian citizens are nationals — no visa needed to enter Brazil. Entry rules and travel tips for Brazilians travelling abroad."
        intro = f"<p><strong>{demonym}</strong> hold Brazilian nationality. This page provides general travel information for Brazilian citizens travelling internationally.</p>"
        key_facts_rows = f"""<tr><th>Status</th><td>{badge}</td></tr>
<tr><th>Entry</th><td>Free — no visa or eVisa required for Brazilian nationals</td></tr>"""
        body_sections = """<h2>Travelling as a Brazilian Citizen</h2>
<p>As a Brazilian national, you enjoy visa-free or visa-on-arrival access to over 170 countries, including the European Union (Schengen Area) and the United States. Carry a valid Brazilian passport for international travel.</p>"""
        faq = [
            ("Do Brazilian citizens need a visa to enter Brazil?", "No. Brazilian citizens are nationals of Brazil and need only a valid Brazilian ID card or passport to enter."),
            ("How many countries can Brazilians visit visa-free?", "The Brazilian passport grants visa-free or visa-on-arrival access to over 170 countries worldwide."),
            ("Do I need a passport or just an ID to travel within South America?", "Brazilian citizens can travel to most Mercosur countries (Argentina, Uruguay, Paraguay) using just their national ID card (RG or RNE).")
        ]
    elif status == "visa_free":
        meta_desc = f"{adj} citizens can visit Brazil visa-free for up to {stay} ({basis}). Requirements and entry rules for {demonym} in 2026."
        intro = f"<p><strong>{demonym}</strong> holding a valid {m['passport']} can enter Brazil <strong>without a visa</strong> for stays of up to <strong>{stay}</strong> under {basis}.</p>"
        key_facts_rows = f"""<tr><th>Visa Required</th><td>{badge}</td></tr>
<tr><th>Basis</th><td>{basis}</td></tr>
<tr><th>Max Stay</th><td>{stay}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>"""
        body_sections = f"""<h2>Visa-Free Entry to Brazil for {adj} Citizens</h2>
<p>{demonym} may enter Brazil for tourism, business, or transit purposes without obtaining a visa in advance. Simply present your valid {m['passport']} (with at least 6 months of remaining validity) at the port of entry.</p>
<h2>Conditions of Visa-Free Entry</h2>
<ul>
<li>Maximum stay: <strong>{stay}</strong> per entry</li>
<li>Purpose: tourism, business meetings, transit</li>
<li>Passport must be valid for at least 6 months beyond your intended stay</li>
<li>Proof of onward or return ticket may be requested</li>
<li>Sufficient funds for your stay may be requested at immigration</li>
</ul>
<h2>What to Carry at the Border</h2>
<ul>
<li>Valid {m['passport']} (6+ months validity)</li>
<li>Return or onward flight booking</li>
<li>Proof of accommodation (hotel booking or invitation letter)</li>
<li>Travel insurance (recommended)</li>
<li>Proof of sufficient funds</li>
</ul>"""
        faq = [
            (f"Do {adj} citizens need a visa for Brazil?", f"No. {demonym} can enter Brazil visa-free for up to {stay} under {basis}."),
            (f"How long can {demonym} stay in Brazil without a visa?", f"Up to {stay} per visit. Extensions are generally not granted — you must leave and re-enter."),
            (f"Can {demonym} work in Brazil on a tourist entry?", f"No. Visa-free entry is for tourism and short business visits only. Working in Brazil requires a separate work visa.")
        ]
    else:  # evisa
        meta_desc = f"{adj} citizens need a Brazil eVisa (USD 80) for tourism in 2026. Apply at gov.br — up to 72-hour processing. Full guide."
        intro = f"<p><strong>{demonym}</strong> holding a valid {m['passport']} must obtain a Brazil <strong>eVisa</strong> before travel. The fee is <strong>{fee}</strong> and processing takes <strong>{processing}</strong>.</p>"
        key_facts_rows = f"""<tr><th>Visa Required</th><td>{badge}</td></tr>
<tr><th>Visa Type</th><td>eVisa (Electronic Travel Authorisation)</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>gov.br (official portal)</td></tr>"""
        body_sections = f"""<h2>Brazil eVisa for {adj} Citizens</h2>
<p>{demonym} must apply for the Brazil eVisa through the official portal at <a href="https://www.gov.br/pt-br/servicos/obter-visto-eletronico-para-o-brasil" target="_blank" rel="noopener">gov.br</a>. The eVisa costs <strong>{fee}</strong> and is processed in <strong>{processing}</strong>. It allows a stay of up to <strong>{stay}</strong>.</p>
<h2>How to Apply for the Brazil eVisa</h2>
<ol>
<li>Visit the official Brazil eVisa portal at <a href="https://www.gov.br/pt-br/servicos/obter-visto-eletronico-para-o-brasil" target="_blank" rel="noopener">gov.br</a>.</li>
<li>Create an account and complete the online application form.</li>
<li>Upload required documents (see list below).</li>
<li>Pay the <strong>{fee}</strong> application fee by credit/debit card.</li>
<li>Receive your approved eVisa by email within {processing}.</li>
<li>Print the eVisa approval and carry it when travelling to Brazil.</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid {m['passport']} (at least 6 months validity beyond departure date)</li>
<li>Passport-quality digital photograph (white background)</li>
<li>Valid email address for communication</li>
<li>Credit or debit card for the {fee} fee</li>
<li>Travel itinerary (flight bookings, accommodation)</li>
<li>Bank statements or proof of sufficient funds</li>
</ul>
<h2>eVisa Conditions</h2>
<ul>
<li>Fee: <strong>{fee}</strong> (non-refundable)</li>
<li>Processing: <strong>{processing}</strong></li>
<li>Stay: up to <strong>{stay}</strong> per visit</li>
<li>Purpose: tourism, business, transit</li>
<li>Multiple entries may be granted</li>
</ul>"""
        faq = [
            (f"Do {adj} citizens need a visa for Brazil?", f"Yes. {demonym} must apply for a Brazil eVisa (USD 80) before travel. It can be obtained online at gov.br within {processing}."),
            (f"How much does the Brazil eVisa cost for {adj} citizens?", f"The Brazil eVisa fee is {fee}. Payment is made online at the time of application."),
            (f"How long can {demonym} stay in Brazil with an eVisa?", f"Up to {stay} per entry. The eVisa may allow single or multiple entries depending on the application.")
        ]

    faq_json = ",\n      ".join([
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(q=q.replace('"', '&quot;'), a=a.replace('"', '&quot;'))
        for q, a in faq
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>Brazil Visa for {adj} Citizens 2026</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {faq_json}
    ]}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button"><span class="oi oi-menu"></span> Menu</button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="../retirement-visa-guide.html">Guides</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="/en/{slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}"></span> Brazil Visa for {adj} Citizens 2026</h1>

{intro}

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Brazil for {adj} Citizens</th></tr></thead>
<tbody>
{key_facts_rows}
</tbody>
</table>

{body_sections}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at the <a href="https://www.gov.br/mre/pt-br/assuntos/portal-consular/vistos/informacoes-sobre-vistos-para-estrangeiros-que-desejam-viajar-ao-brasil" target="_blank" rel="noopener">Brazilian Ministry of Foreign Affairs</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-brazil.html">Brazil Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="brazil-visa-requirements.html">Brazil Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="brazil-visa-fees.html">Brazil Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="brazil-visa-processing-time.html">Brazil Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>

</article>
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform</p>
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
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""


# -----------------------------------------------------------------------
# Argentina page builder
# -----------------------------------------------------------------------
def build_argentina_page(nat):
    m = NAT_META[nat]
    s = ARGENTINA_STATUS[nat]
    adj = m["adj"]
    flag = m["flag"]
    label = m["label"]
    demonym = m["demonym"]
    status = s["status"]
    stay = s["stay"]
    basis = s["basis"]
    fee = s["fee"]
    processing = s["processing"]
    slug = f"argentina-visa-for-{nat}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    badge = status_badge(status, "Argentina")

    if status == "national":
        meta_desc = "Argentine citizens are nationals — no visa needed to enter Argentina. Entry rules and travel tips for Argentinians travelling abroad."
        intro = "<p><strong>Argentinians</strong> hold Argentine nationality. This page provides general travel information for Argentine citizens travelling internationally.</p>"
        key_facts_rows = f"""<tr><th>Status</th><td>{badge}</td></tr>
<tr><th>Entry</th><td>Free — no visa required for Argentine nationals</td></tr>"""
        body_sections = """<h2>Travelling as an Argentine Citizen</h2>
<p>As an Argentine national, you have visa-free or visa-on-arrival access to over 170 countries, including the European Union and the United States. Always carry a valid Argentine passport for international travel.</p>"""
        faq = [
            ("Do Argentine citizens need a visa to enter Argentina?", "No. Argentine citizens are nationals and require only a valid Argentine passport or DNI (national ID) to enter."),
            ("How many countries can Argentinians visit visa-free?", "The Argentine passport provides visa-free or visa-on-arrival access to over 170 countries."),
            ("Can Argentinians travel within Mercosur with just their ID?", "Yes. Argentine citizens can travel to Brazil, Uruguay, Paraguay, and other Mercosur countries using their DNI national identity card.")
        ]
    elif status == "visa_free":
        meta_desc = f"{adj} citizens can visit Argentina visa-free for up to {stay} ({basis}). Entry requirements and travel tips for {demonym} in 2026."
        intro = f"<p><strong>{demonym}</strong> holding a valid {m['passport']} can enter Argentina <strong>without a visa</strong> for stays of up to <strong>{stay}</strong> under {basis}.</p>"
        key_facts_rows = f"""<tr><th>Visa Required</th><td>{badge}</td></tr>
<tr><th>Basis</th><td>{basis}</td></tr>
<tr><th>Max Stay</th><td>{stay}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>"""
        body_sections = f"""<h2>Visa-Free Entry to Argentina for {adj} Citizens</h2>
<p>{demonym} can enter Argentina for tourism, business, or transit without a visa. Present your valid {m['passport']} at the port of entry. Ensure your passport has at least 6 months of remaining validity.</p>
<h2>Conditions of Visa-Free Entry</h2>
<ul>
<li>Maximum stay: <strong>{stay}</strong> per entry</li>
<li>Purpose: tourism, business, transit</li>
<li>Passport validity: at least 6 months beyond intended stay</li>
<li>Onward/return ticket may be requested at immigration</li>
<li>Proof of sufficient funds may be requested</li>
</ul>
<h2>What to Carry on Arrival</h2>
<ul>
<li>Valid {m['passport']} (6+ months validity)</li>
<li>Return or onward flight booking</li>
<li>Proof of accommodation</li>
<li>Travel insurance (recommended)</li>
<li>Proof of sufficient funds</li>
</ul>"""
        faq = [
            (f"Do {adj} citizens need a visa for Argentina?", f"No. {demonym} can enter Argentina visa-free for up to {stay} ({basis})."),
            (f"How long can {demonym} stay in Argentina without a visa?", f"Up to {stay} per entry. The stay can sometimes be extended by 90 days at the immigration office (Migraciones)."),
            (f"Can {demonym} work in Argentina on a tourist entry?", f"No. Visa-free entry is for tourism and short-stay purposes only. A work permit or residence visa is required to work legally in Argentina.")
        ]
    else:  # visa_req
        meta_desc = f"{adj} citizens need a tourist visa to visit Argentina in 2026. Apply at the Argentine consulate — processing takes 4–8 weeks. Full guide."
        intro = f"<p><strong>{demonym}</strong> holding a valid {m['passport']} must obtain an Argentine tourist visa before travel. Apply at the nearest Argentine consulate or embassy.</p>"
        key_facts_rows = f"""<tr><th>Visa Required</th><td>{badge}</td></tr>
<tr><th>Visa Type</th><td>Tourist Visa (Visa de Turismo)</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>Argentine consulate or embassy in your country</td></tr>"""
        body_sections = f"""<h2>Argentine Tourist Visa for {adj} Citizens</h2>
<p>{demonym} must apply for an Argentine <strong>Tourist Visa (Visa de Turismo)</strong> at the Argentine consulate or embassy in their home country before travelling. Processing typically takes <strong>{processing}</strong>.</p>
<h2>How to Apply for an Argentine Tourist Visa</h2>
<ol>
<li>Locate the nearest Argentine consulate or embassy.</li>
<li>Complete the visa application form (available at the consulate or online).</li>
<li>Gather all required documents (see list below).</li>
<li>Attend a consulate appointment if required.</li>
<li>Pay the applicable visa fee.</li>
<li>Wait for processing — typically <strong>{processing}</strong>.</li>
<li>Collect your visa and travel to Argentina.</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid {m['passport']} (at least 6 months validity beyond your intended stay)</li>
<li>Completed visa application form</li>
<li>Passport-sized photographs</li>
<li>Bank statements (last 3–6 months) showing sufficient funds</li>
<li>Proof of accommodation in Argentina</li>
<li>Return or onward flight booking</li>
<li>Travel insurance covering the full stay</li>
<li>Employment letter or proof of enrollment (for students)</li>
</ul>
<h2>Visa Conditions</h2>
<ul>
<li>Fee: <strong>{fee}</strong></li>
<li>Processing: <strong>{processing}</strong></li>
<li>Stay: <strong>{stay}</strong> (as determined by immigration)</li>
<li>Purpose: tourism only — no work permitted</li>
</ul>"""
        faq = [
            (f"Do {adj} citizens need a visa for Argentina?", f"Yes. {demonym} must obtain an Argentine tourist visa from the consulate before travelling. Processing takes approximately {processing}."),
            (f"How much does an Argentine tourist visa cost for {adj} citizens?", f"The fee varies by consulate and reciprocity agreements. Contact the nearest Argentine consulate for current fee information."),
            (f"How long can {demonym} stay in Argentina with a tourist visa?", f"The permitted stay is determined at the time of visa issuance, typically up to 90 days for a single entry.")
        ]

    faq_json = ",\n      ".join([
        '{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(q=q.replace('"', '&quot;'), a=a.replace('"', '&quot;'))
        for q, a in faq
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>Argentina Visa for {adj} Citizens 2026</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {faq_json}
    ]}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button"><span class="oi oi-menu"></span> Menu</button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="../retirement-visa-guide.html">Guides</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="/en/{slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}"></span> Argentina Visa for {adj} Citizens 2026</h1>

{intro}

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Argentina for {adj} Citizens</th></tr></thead>
<tbody>
{key_facts_rows}
</tbody>
</table>

{body_sections}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at the <a href="https://www.cancilleria.gob.ar/en/services/consular-services/visas" target="_blank" rel="noopener">Argentine Ministry of Foreign Affairs</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-argentina.html">Argentina Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="argentina-visa-requirements.html">Argentina Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="argentina-visa-fees.html">Argentina Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="argentina-visa-processing-time.html">Argentina Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>

</article>
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform</p>
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
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""


# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    for nat in NATIONALITIES:
        # Brazil
        fname_br = f"brazil-visa-for-{nat}-citizens.html"
        path_br = os.path.join(OUTPUT_DIR, fname_br)
        with open(path_br, "w", encoding="utf-8") as f:
            f.write(build_brazil_page(nat))
        created.append(fname_br)

        # Argentina
        fname_ar = f"argentina-visa-for-{nat}-citizens.html"
        path_ar = os.path.join(OUTPUT_DIR, fname_ar)
        with open(path_ar, "w", encoding="utf-8") as f:
            f.write(build_argentina_page(nat))
        created.append(fname_ar)

    print(f"Generated {len(created)} files in {OUTPUT_DIR}:")
    for fn in sorted(created):
        print(f"  {fn}")


if __name__ == "__main__":
    main()
