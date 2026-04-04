#!/usr/bin/env python3
"""
Generate 40 HTML files:
  - cambodia-visa-for-{nat}-citizens.html  (20 files)
  - china-visa-for-{nat}-citizens.html     (20 files)
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NATIONALITIES = {
    "us": {
        "label": "US",
        "demonym": "US",
        "full": "American",
        "flag": "us",
        "passport": "US (American)",
    },
    "uk": {
        "label": "UK",
        "demonym": "UK",
        "full": "British",
        "flag": "gb",
        "passport": "UK (British)",
    },
    "canadian": {
        "label": "Canadian",
        "demonym": "Canadian",
        "full": "Canadian",
        "flag": "ca",
        "passport": "Canadian",
    },
    "french": {
        "label": "French",
        "demonym": "French",
        "full": "French",
        "flag": "fr",
        "passport": "French",
    },
    "german": {
        "label": "German",
        "demonym": "German",
        "full": "German",
        "flag": "de",
        "passport": "German",
    },
    "japanese": {
        "label": "Japanese",
        "demonym": "Japanese",
        "full": "Japanese",
        "flag": "jp",
        "passport": "Japanese",
    },
    "australian": {
        "label": "Australian",
        "demonym": "Australian",
        "full": "Australian",
        "flag": "au",
        "passport": "Australian",
    },
    "indian": {
        "label": "Indian",
        "demonym": "Indian",
        "full": "Indian",
        "flag": "in",
        "passport": "Indian",
    },
    "chinese": {
        "label": "Chinese",
        "demonym": "Chinese",
        "full": "Chinese",
        "flag": "cn",
        "passport": "Chinese",
    },
    "russian": {
        "label": "Russian",
        "demonym": "Russian",
        "full": "Russian",
        "flag": "ru",
        "passport": "Russian",
    },
    "brazilian": {
        "label": "Brazilian",
        "demonym": "Brazilian",
        "full": "Brazilian",
        "flag": "br",
        "passport": "Brazilian",
    },
    "mexican": {
        "label": "Mexican",
        "demonym": "Mexican",
        "full": "Mexican",
        "flag": "mx",
        "passport": "Mexican",
    },
    "south-african": {
        "label": "South African",
        "demonym": "South African",
        "full": "South African",
        "flag": "za",
        "passport": "South African",
    },
    "nigerian": {
        "label": "Nigerian",
        "demonym": "Nigerian",
        "full": "Nigerian",
        "flag": "ng",
        "passport": "Nigerian",
    },
    "korean": {
        "label": "Korean",
        "demonym": "Korean",
        "full": "South Korean",
        "flag": "kr",
        "passport": "South Korean",
    },
    "singaporean": {
        "label": "Singaporean",
        "demonym": "Singaporean",
        "full": "Singaporean",
        "flag": "sg",
        "passport": "Singaporean",
    },
    "indonesian": {
        "label": "Indonesian",
        "demonym": "Indonesian",
        "full": "Indonesian",
        "flag": "id",
        "passport": "Indonesian",
    },
    "philippine": {
        "label": "Philippine",
        "demonym": "Philippine",
        "full": "Filipino",
        "flag": "ph",
        "passport": "Philippine (Filipino)",
    },
    "turkish": {
        "label": "Turkish",
        "demonym": "Turkish",
        "full": "Turkish",
        "flag": "tr",
        "passport": "Turkish",
    },
    "argentinian": {
        "label": "Argentinian",
        "demonym": "Argentinian",
        "full": "Argentine",
        "flag": "ar",
        "passport": "Argentine",
    },
}

# ---------------------------------------------------------------------------
# Cambodia visa status per nationality
# ---------------------------------------------------------------------------
# Possible statuses: "evisa", "voa", "visa_free_asean", "visa_free_india"
CAMBODIA_STATUS = {
    "us":           "evisa",
    "uk":           "evisa",
    "canadian":     "evisa",
    "french":       "evisa",
    "german":       "evisa",
    "japanese":     "evisa",
    "australian":   "evisa",
    "indian":       "visa_free_india",
    "chinese":      "voa",
    "russian":      "evisa",
    "brazilian":    "evisa",
    "mexican":      "evisa",
    "south-african":"evisa",
    "nigerian":     "voa",
    "korean":       "evisa",
    "singaporean":  "visa_free_asean",
    "indonesian":   "visa_free_asean",
    "philippine":   "visa_free_asean",
    "turkish":      "evisa",
    "argentinian":  "evisa",
}

# ---------------------------------------------------------------------------
# China visa status per nationality
# ---------------------------------------------------------------------------
# Possible statuses: "visa_free_15", "twov", "evisa_free", "standard"
# eVisa free overrides TWOV where both apply — we'll combine in the page copy
CHINA_STATUS = {
    "us":           "evisa_free",   # eVisa free + TWOV
    "uk":           "evisa_free",   # eVisa free + TWOV
    "canadian":     "evisa_free",   # eVisa free + TWOV
    "french":       "visa_free_15", # visa-free 15 days + eVisa free
    "german":       "visa_free_15", # visa-free 15 days + eVisa free
    "japanese":     "evisa_free",   # eVisa free + TWOV
    "australian":   "evisa_free",   # eVisa free + TWOV
    "indian":       "standard",
    "chinese":      "citizen",      # domestic — special handling
    "russian":      "evisa_free",
    "brazilian":    "evisa_free",
    "mexican":      "evisa_free",
    "south-african":"standard",
    "nigerian":     "standard",
    "korean":       "evisa_free",   # eVisa free + TWOV
    "singaporean":  "evisa_free",
    "indonesian":   "standard",
    "philippine":   "standard",
    "turkish":      "standard",
    "argentinian":  "evisa_free",
}

# Nationals who also have TWOV in addition to eVisa
CHINA_TWOV = {"us", "uk", "canadian", "japanese", "korean", "australian"}

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------
GA4 = "G-XC1GYM27WC"
ADSENSE = "ca-pub-9298895030863686"


def navbar(current_file: str) -> str:
    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
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
                        <a class="dropdown-item active" href="/en/{current_file}"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""


def footer() -> str:
    return """<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">&copy; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
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
<script src="../js/main.js"></script>"""


def head_block(title: str, description: str, canonical: str, faq_json: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4}');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{description}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{canonical}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {faq_json}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


# ---------------------------------------------------------------------------
# Cambodia page builder
# ---------------------------------------------------------------------------

def cambodia_page(nat_key: str) -> str:
    nat = NATIONALITIES[nat_key]
    status = CAMBODIA_STATUS[nat_key]
    label = nat["label"]
    flag = nat["flag"]
    filename = f"cambodia-visa-for-{nat_key}-citizens.html"
    canonical = f"cambodia-visa-for-{nat_key}-citizens.html"
    title = f"Cambodia Visa for {label} Citizens 2026"

    # ---- Status-specific data ----
    if status == "evisa":
        status_badge = '<span style="color:green;font-weight:600;">eVisa Available — USD 30</span>'
        visa_type = "Tourist eVisa (T class)"
        fee = "USD 30"
        max_stay = "30 days"
        processing = "3 business days"
        apply_at = "evisa.gov.kh"
        description = (
            f"{label} passport holders can apply for a Cambodia eVisa online for USD 30 at evisa.gov.kh. "
            f"30-day tourist stay, 3-day processing. Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for Cambodia?"
        faq_a1 = (
            f"{label} passport holders can apply for an official Cambodia eVisa (USD 30) online at evisa.gov.kh. "
            f"Processing takes 3 business days and grants a 30-day single-entry tourist stay. "
            f"A Visa on Arrival (USD 35) is also available at major international airports."
        )
        faq_q2 = "What is the Cambodia eVisa fee?"
        faq_a2 = "The Cambodia eVisa costs USD 30, payable by credit or debit card at evisa.gov.kh. The Visa on Arrival costs USD 35 in cash at the port of entry."
        faq_q3 = "How long does the Cambodia eVisa take?"
        faq_a3 = "The Cambodia eVisa is typically processed within 3 business days. Apply at least one week before travel."

        intro_h2 = f"Cambodia eVisa for {label} Citizens"
        intro_p = (
            f"{label} passport holders are eligible for the official <strong>Cambodia eVisa</strong> "
            f"(Tourist class), available online at <a href='https://evisa.gov.kh' target='_blank' rel='noopener'>evisa.gov.kh</a> "
            f"for <strong>USD 30</strong>. The eVisa grants a <strong>30-day single-entry</strong> tourist stay "
            f"and is processed within 3 business days."
        )
        details_h2 = "eVisa Key Details"
        details_ul = """<ul>
<li>Fee: <strong>USD 30</strong> (credit/debit card)</li>
<li>Validity: Single entry, 30 days stay</li>
<li>Processing: 3 business days</li>
<li>Entry points: Phnom Penh, Siem Reap, Sihanoukville airports + select land crossings</li>
<li>Alternative: Visa on Arrival (USD 35 cash) at the same entry points</li>
</ul>"""
        how_to = """<ol>
<li>Visit <a href='https://evisa.gov.kh' target='_blank' rel='noopener'>evisa.gov.kh</a> — the official Cambodian eVisa portal.</li>
<li>Complete the online application form with passport details and travel dates.</li>
<li>Upload a passport photo (4×6 cm, white background) and passport bio-data page scan.</li>
<li>Pay USD 30 by credit or debit card.</li>
<li>Receive approval by email within 3 business days; print and carry the eVisa approval letter.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity beyond stay</li>
<li>Passport photo — 4×6 cm, white background, taken within 6 months</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address</li>
<li>Credit/debit card for USD 30 payment</li>
</ul>"""

    elif status == "visa_free_asean":
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free Entry (ASEAN)</span>'
        visa_type = "Visa-Free (ASEAN)"
        fee = "Free"
        max_stay = "30 days"
        processing = "N/A — no visa required"
        apply_at = "No application needed"
        description = (
            f"{label} citizens enjoy visa-free entry to Cambodia as ASEAN members — "
            f"no visa required for stays up to 30 days. Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for Cambodia?"
        faq_a1 = (
            f"No. {label} passport holders benefit from visa-free entry to Cambodia under the ASEAN agreement, "
            f"allowing stays of up to 30 days without a visa."
        )
        faq_q2 = "How long can ASEAN citizens stay in Cambodia visa-free?"
        faq_a2 = "ASEAN nationals, including Indonesian and Philippine passport holders, can stay in Cambodia for up to 30 days without a visa."
        faq_q3 = "What documents do I need to enter Cambodia visa-free?"
        faq_a3 = "A valid passport (6 months validity recommended), return ticket, and proof of sufficient funds are recommended. No visa is required."

        intro_h2 = f"Cambodia Visa-Free Entry for {label} Citizens"
        intro_p = (
            f"{label} passport holders enjoy <strong>visa-free entry</strong> to Cambodia under the "
            f"ASEAN Free Movement Agreement. No advance visa application is needed for stays up to "
            f"<strong>30 days</strong>."
        )
        details_h2 = "Visa-Free Entry Details"
        details_ul = """<ul>
<li>Fee: <strong>Free</strong></li>
<li>Stay: Up to 30 days</li>
<li>Entry: Present valid passport at immigration</li>
<li>Basis: ASEAN bilateral agreement</li>
</ul>"""
        how_to = """<ol>
<li>No advance application is required.</li>
<li>Arrive at Phnom Penh, Siem Reap, or Sihanoukville international airports, or an authorised land crossing.</li>
<li>Present your valid passport at the immigration counter.</li>
<li>Receive a 30-day entry stamp.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity recommended</li>
<li>Return or onward flight ticket</li>
<li>Proof of sufficient funds</li>
<li>Hotel booking or accommodation address (recommended)</li>
</ul>"""

    elif status == "visa_free_india":
        status_badge = '<span style="color:green;font-weight:600;">eVisa Available (Free) + Visa on Arrival</span>'
        visa_type = "eVisa (Free) or Visa on Arrival (USD 35)"
        fee = "Free eVisa or USD 35 VOA"
        max_stay = "30 days"
        processing = "3 business days (eVisa)"
        apply_at = "evisa.gov.kh"
        description = (
            f"Indian passport holders can visit Cambodia with a free eVisa at evisa.gov.kh or USD 35 "
            f"Visa on Arrival. 30-day stay. Updated March 2026."
        )
        faq_q1 = "Do Indian citizens need a visa for Cambodia?"
        faq_a1 = (
            "Indian passport holders can obtain a free Cambodia eVisa at evisa.gov.kh or a USD 35 Visa on Arrival "
            "at major airports. Both grant a 30-day single-entry tourist stay."
        )
        faq_q2 = "Is the Cambodia eVisa free for Indian citizens?"
        faq_a2 = "Yes. Indian passport holders can apply for a free Cambodia eVisa at evisa.gov.kh. Processing takes 3 business days."
        faq_q3 = "Can Indian citizens get a Visa on Arrival in Cambodia?"
        faq_a3 = "Yes. Indian passport holders can obtain a Visa on Arrival for USD 35 cash at Phnom Penh, Siem Reap, and Sihanoukville international airports."

        intro_h2 = "Cambodia eVisa for Indian Citizens"
        intro_p = (
            "Indian passport holders can apply for a <strong>free Cambodia eVisa</strong> at "
            "<a href='https://evisa.gov.kh' target='_blank' rel='noopener'>evisa.gov.kh</a> or obtain a "
            "<strong>Visa on Arrival (USD 35)</strong> at major international airports. Both options grant "
            "a <strong>30-day single-entry</strong> tourist stay."
        )
        details_h2 = "eVisa &amp; Visa on Arrival Details"
        details_ul = """<ul>
<li>eVisa: <strong>Free</strong> — apply at evisa.gov.kh</li>
<li>Visa on Arrival: <strong>USD 35 cash</strong> — available at Phnom Penh, Siem Reap, Sihanoukville airports</li>
<li>Stay: 30 days (single entry)</li>
<li>eVisa processing: 3 business days</li>
</ul>"""
        how_to = """<ol>
<li>Option A — eVisa: Visit <a href='https://evisa.gov.kh' target='_blank' rel='noopener'>evisa.gov.kh</a>, complete the application and submit — no fee for Indian nationals.</li>
<li>Upload a passport photo (4×6 cm, white background) and passport scan.</li>
<li>Receive approval by email within 3 business days; print the approval letter.</li>
<li>Option B — Visa on Arrival: Arrive at an international airport, proceed to the VOA counter, and pay USD 35 in cash.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity</li>
<li>Passport photo — 4×6 cm, white background</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address</li>
<li>USD 35 cash (for Visa on Arrival)</li>
</ul>"""

    else:  # voa
        status_badge = '<span style="color:orange;font-weight:600;">Visa on Arrival — USD 35</span>'
        visa_type = "Visa on Arrival (Tourist)"
        fee = "USD 35 cash"
        max_stay = "30 days"
        processing = "On arrival (~15 min)"
        apply_at = "Port of entry (airport / land crossing)"
        description = (
            f"{label} passport holders obtain a Cambodia Visa on Arrival for USD 35 at Phnom Penh, "
            f"Siem Reap, or Sihanoukville airports. 30-day stay. Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for Cambodia?"
        faq_a1 = (
            f"{label} passport holders obtain a Cambodia Visa on Arrival (USD 35 cash) at major international "
            f"airports. The VOA grants a 30-day single-entry tourist stay. An eVisa may also be available — "
            f"check evisa.gov.kh before travel."
        )
        faq_q2 = "How much is the Cambodia Visa on Arrival?"
        faq_a2 = "The Cambodia Visa on Arrival costs USD 35, payable in cash at the port of entry. Exact change in USD is recommended."
        faq_q3 = "Where can I get a Cambodia Visa on Arrival?"
        faq_a3 = "Visa on Arrival is available at Phnom Penh International Airport (PNH), Siem Reap International Airport, and Sihanoukville International Airport, as well as most major land border crossings."

        intro_h2 = f"Cambodia Visa on Arrival for {label} Citizens"
        intro_p = (
            f"{label} passport holders can obtain a <strong>Cambodia Visa on Arrival</strong> for "
            f"<strong>USD 35 cash</strong> on arrival at Phnom Penh, Siem Reap, or Sihanoukville "
            f"international airports, and most major land border crossings. The VOA grants a "
            f"<strong>30-day single-entry</strong> tourist stay. An eVisa (USD 30) may also be available "
            f"at <a href='https://evisa.gov.kh' target='_blank' rel='noopener'>evisa.gov.kh</a> — "
            f"check before travel."
        )
        details_h2 = "Visa on Arrival Key Details"
        details_ul = """<ul>
<li>Fee: <strong>USD 35 cash</strong> (exact change recommended)</li>
<li>Stay: 30 days (single entry)</li>
<li>Available at: Phnom Penh, Siem Reap, Sihanoukville airports + major land crossings</li>
<li>Processing: ~15 minutes at immigration counter</li>
</ul>"""
        how_to = """<ol>
<li>Arrive at Phnom Penh, Siem Reap, or Sihanoukville international airport.</li>
<li>Proceed to the Visa on Arrival counter before the immigration booths.</li>
<li>Complete the VOA application form (available at the counter).</li>
<li>Submit your passport, one passport photo, and USD 35 in cash.</li>
<li>Collect your passport with the visa stamp and proceed through immigration.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity</li>
<li>One passport photo — 4×6 cm, white background</li>
<li>USD 35 in cash (exact change recommended)</li>
<li>Completed VOA application form</li>
<li>Return or onward flight ticket</li>
</ul>"""

    faq_json = f"""{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"{faq_q1}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a1}"}}}},
      {{"@type":"Question","name":"{faq_q2}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a2}"}}}},
      {{"@type":"Question","name":"{faq_q3}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a3}"}}}}
    ]}}"""

    html = f"""{head_block(title, description, canonical, faq_json)}
<body>
{navbar(filename)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-kh"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Cambodia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Status</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{max_stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
</tbody>
</table>

<h2>{intro_h2}</h2>
<p>{intro_p}</p>

<h2>{details_h2}</h2>
{details_ul}

<h2>How to Apply</h2>
{how_to}

<h2>Required Documents</h2>
{docs}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://evisa.gov.kh" target="_blank" rel="noopener">evisa.gov.kh</a> or the nearest Cambodian embassy before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-cambodia.html">Cambodia Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="cambodia-visa-requirements.html">Cambodia Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="cambodia-visa-fees.html">Cambodia Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="cambodia-visa-processing-time.html">Cambodia Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{footer()}
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# China page builder
# ---------------------------------------------------------------------------

def china_page(nat_key: str) -> str:
    nat = NATIONALITIES[nat_key]
    status = CHINA_STATUS[nat_key]
    has_twov = nat_key in CHINA_TWOV
    label = nat["label"]
    flag = nat["flag"]
    filename = f"china-visa-for-{nat_key}-citizens.html"
    canonical = f"china-visa-for-{nat_key}-citizens.html"
    title = f"China Visa for {label} Citizens 2026"

    if status == "citizen":
        # Chinese citizens travelling to mainland China — domestic travel
        status_badge = '<span style="color:green;font-weight:600;">Domestic — No Visa Required</span>'
        visa_type = "N/A — Domestic travel"
        fee = "N/A"
        max_stay = "Unrestricted"
        processing = "N/A"
        apply_at = "N/A"
        description = (
            "Chinese citizens travelling within mainland China do not require a visa. "
            "This page covers travel from overseas — Chinese passports allow unrestricted entry. Updated March 2026."
        )
        faq_q1 = "Do Chinese citizens need a visa to enter China?"
        faq_a1 = "No. Chinese citizens are not required to obtain a visa to enter mainland China. Chinese nationals use their Chinese passport or ID card for entry."
        faq_q2 = "Can Chinese citizens enter China from overseas?"
        faq_a2 = "Yes. Chinese passport holders can return to mainland China freely using their valid Chinese passport at any port of entry."
        faq_q3 = "What document do Chinese citizens need to enter China?"
        faq_a3 = "A valid Chinese passport or Chinese Resident Identity Card (for land/sea crossings from certain neighbouring regions) is required for entry."

        intro_h2 = "China Entry for Chinese Citizens"
        intro_p = (
            "Chinese citizens do not need a visa to enter mainland China. A valid <strong>Chinese passport</strong> "
            "is sufficient for entry at any international port. Chinese residents abroad may also use their "
            "passport for return travel."
        )
        details_h2 = "Entry Details for Chinese Citizens"
        details_ul = """<ul>
<li>No visa required — Chinese passport grants unrestricted entry</li>
<li>Carry a valid Chinese passport (not expired)</li>
<li>For those with dual nationality: Chinese law does not recognise dual citizenship; enter on your Chinese passport</li>
</ul>"""
        how_to = """<ol>
<li>Ensure your Chinese passport is valid for the duration of your stay.</li>
<li>Proceed directly through the Chinese citizens / Chinese passport lane at immigration.</li>
<li>Present your Chinese passport for stamping.</li>
</ol>"""
        docs = """<ul>
<li>Valid Chinese passport</li>
</ul>"""

    elif status == "visa_free_15":
        twov_note = " Additionally, 72-hour/144-hour Transit Without Visa (TWOV) is available at select Chinese airports." if has_twov else ""
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free 15 Days + Free eVisa Option</span>'
        visa_type = "Visa-Free (15 days) / eVisa (FREE)"
        fee = "Free"
        max_stay = "15 days visa-free; 30 days eVisa"
        processing = "Instant at border (visa-free) / 4 business days (eVisa)"
        apply_at = "evisa.mfa.gov.cn (eVisa)"
        description = (
            f"{label} passport holders enjoy visa-free entry to China for up to 15 days under the 2023–2025 "
            f"bilateral policy. A free eVisa for 30 days is also available at evisa.mfa.gov.cn. Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for China?"
        faq_a1 = (
            f"{label} passport holders benefit from China's visa-free policy (up to 15 days) under the 2023–2025 "
            f"bilateral agreement. A free eVisa allowing 30-day stays is also available at evisa.mfa.gov.cn.{twov_note}"
        )
        faq_q2 = f"How long can {label} citizens stay in China visa-free?"
        faq_a2 = f"{label} nationals can stay in China for up to 15 days without a visa under the current bilateral policy. For longer stays, apply for a free eVisa at evisa.mfa.gov.cn (up to 30 days)."
        faq_q3 = f"Is the China eVisa free for {label} citizens?"
        faq_a3 = f"Yes. {label} passport holders can apply for a free China eVisa at evisa.mfa.gov.cn, granting up to 30 days stay. Processing takes approximately 4 business days."

        intro_h2 = f"China Visa-Free Entry for {label} Citizens"
        intro_p = (
            f"{label} passport holders benefit from <strong>visa-free entry</strong> to China for up to "
            f"<strong>15 days</strong> under the 2023–2025 bilateral agreement. For longer stays, a "
            f"<strong>free eVisa</strong> (up to 30 days) is available at "
            f"<a href='https://evisa.mfa.gov.cn' target='_blank' rel='noopener'>evisa.mfa.gov.cn</a>.{twov_note}"
        )
        details_h2 = "Visa-Free &amp; eVisa Details"
        details_ul = f"""<ul>
<li>Visa-free: <strong>15 days</strong>, no application required</li>
<li>eVisa: <strong>Free</strong>, up to 30 days — apply at evisa.mfa.gov.cn</li>
<li>eVisa processing: ~4 business days</li>
<li>Entry: Most international airports and ports</li>
{"<li>TWOV: 72h/144h transit without visa at select airports (Beijing, Shanghai, Guangzhou, etc.)</li>" if has_twov else ""}
</ul>"""
        how_to = f"""<ol>
<li>For short stays (up to 15 days): No advance application needed — present your valid passport at the immigration counter.</li>
<li>For stays up to 30 days: Visit <a href='https://evisa.mfa.gov.cn' target='_blank' rel='noopener'>evisa.mfa.gov.cn</a> to apply for a free eVisa.</li>
<li>Complete the online form with passport details, travel dates, and upload a passport photo.</li>
<li>Receive eVisa approval by email within 4 business days.</li>
<li>Print and carry the eVisa approval letter alongside your passport.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity</li>
<li>Passport photo (for eVisa application)</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address</li>
</ul>"""

    elif status == "evisa_free":
        twov_note = " A 72-hour/144-hour Transit Without Visa (TWOV) option is also available at select airports." if has_twov else ""
        status_badge = '<span style="color:green;font-weight:600;">Free eVisa Available</span>'
        visa_type = "eVisa (FREE)"
        fee = "Free"
        max_stay = "30 days"
        processing = "4 business days"
        apply_at = "evisa.mfa.gov.cn"
        description = (
            f"{label} passport holders can obtain a free China eVisa at evisa.mfa.gov.cn for up to 30 days. "
            f"Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for China?"
        faq_a1 = (
            f"{label} passport holders can apply for a free China eVisa at evisa.mfa.gov.cn. "
            f"The eVisa grants up to 30 days and is processed within 4 business days.{twov_note}"
        )
        faq_q2 = f"Is the China eVisa free for {label} citizens?"
        faq_a2 = f"Yes. The China eVisa is currently free of charge for {label} passport holders. Apply at the official portal: evisa.mfa.gov.cn."
        faq_q3 = "How do I apply for a China eVisa?"
        faq_a3 = "Visit evisa.mfa.gov.cn, complete the online application, upload your passport photo and bio-data page scan, and submit. You will receive approval by email in approximately 4 business days."

        intro_h2 = f"China eVisa for {label} Citizens (FREE)"
        intro_p = (
            f"{label} passport holders are eligible for China's <strong>free eVisa</strong>, available at "
            f"<a href='https://evisa.mfa.gov.cn' target='_blank' rel='noopener'>evisa.mfa.gov.cn</a>. "
            f"The eVisa grants a <strong>30-day stay</strong> and is processed within 4 business days. "
            + (f"A 72h/144h Transit Without Visa (TWOV) option is also available at select major airports "
               f"(Beijing, Shanghai, Guangzhou, Chengdu, and others)." if has_twov else "")
        )
        details_h2 = "eVisa Key Details"
        details_ul = f"""<ul>
<li>Fee: <strong>Free</strong></li>
<li>Stay: Up to 30 days</li>
<li>Processing: ~4 business days</li>
<li>Apply at: <a href='https://evisa.mfa.gov.cn' target='_blank' rel='noopener'>evisa.mfa.gov.cn</a></li>
{"<li>TWOV: 72h/144h transit without visa at Beijing, Shanghai, Guangzhou and other select airports</li>" if has_twov else ""}
</ul>"""
        how_to = """<ol>
<li>Visit <a href='https://evisa.mfa.gov.cn' target='_blank' rel='noopener'>evisa.mfa.gov.cn</a> — official Ministry of Foreign Affairs eVisa portal.</li>
<li>Create an account and complete the online visa application form.</li>
<li>Upload a passport photo (white background, recent) and a scan of your passport bio-data page.</li>
<li>Submit — there is no fee for eligible nationalities.</li>
<li>Receive approval by email within 4 business days; print and carry the approval letter.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity</li>
<li>Digital passport photo — white background, recent</li>
<li>Scan of passport bio-data page</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or accommodation address in China</li>
</ul>"""

    else:  # standard
        status_badge = '<span style="color:red;font-weight:600;">Standard Visa Required — USD 140</span>'
        visa_type = "Tourist / Business Visa (L / M class)"
        fee = "USD 140 (approx.)"
        max_stay = "30–90 days (as granted)"
        processing = "4–7 business days"
        apply_at = "Chinese embassy / consulate"
        description = (
            f"{label} passport holders must obtain a standard China visa from a Chinese embassy or consulate. "
            f"Fee approx. USD 140, 4–7 business days processing. Updated March 2026."
        )
        faq_q1 = f"Do {label} citizens need a visa for China?"
        faq_a1 = (
            f"Yes. {label} passport holders must obtain a standard China visa from the nearest Chinese embassy "
            f"or consulate. The fee is approximately USD 140 and processing takes 4–7 business days."
        )
        faq_q2 = "How much does a China visa cost?"
        faq_a2 = "The standard China tourist (L) or business (M) visa fee is approximately USD 140. Fees may vary by consulate location and nationality; confirm with your local Chinese embassy."
        faq_q3 = "How do I apply for a China visa?"
        faq_a3 = "Submit your application in person or via the Chinese Visa Application Service Centre (CVASC) in your country. Required documents include a completed application form, valid passport, photo, and supporting documents."

        intro_h2 = f"China Visa for {label} Citizens"
        intro_p = (
            f"{label} passport holders must obtain a <strong>standard China visa</strong> from the nearest "
            f"Chinese embassy or consulate before travelling. The standard tourist (L) visa fee is approximately "
            f"<strong>USD 140</strong>, and processing takes <strong>4–7 business days</strong>. "
            f"Apply via the <a href='https://www.visaforchina.cn' target='_blank' rel='noopener'>Chinese Visa "
            f"Application Service Centre (CVASC)</a> in your country."
        )
        details_h2 = "Standard Visa Key Details"
        details_ul = """<ul>
<li>Fee: <strong>approx. USD 140</strong> (confirm with local Chinese embassy)</li>
<li>Visa types: Tourist (L), Business (M), Transit (G)</li>
<li>Stay: 30–90 days as granted</li>
<li>Processing: 4–7 business days (express available at some locations)</li>
<li>Apply at: Chinese embassy, consulate, or CVASC</li>
</ul>"""
        how_to = """<ol>
<li>Locate the nearest Chinese embassy, consulate, or Chinese Visa Application Service Centre (CVASC) at <a href='https://www.visaforchina.cn' target='_blank' rel='noopener'>visaforchina.cn</a>.</li>
<li>Download and complete the DS-160 equivalent — the China Visa Application Form (V.2013).</li>
<li>Prepare all required documents (see below).</li>
<li>Submit your application and pay the visa fee (approx. USD 140).</li>
<li>Collect your passport with the visa stamp after 4–7 business days.</li>
</ol>"""
        docs = """<ul>
<li>Valid passport — minimum 6 months validity, at least one blank visa page</li>
<li>Completed China Visa Application Form (V.2013)</li>
<li>Passport photo — 48×33 mm, white background, recent</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or invitation letter</li>
<li>Bank statements (last 3–6 months)</li>
<li>Travel insurance (recommended)</li>
</ul>"""

    faq_json = f"""{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"{faq_q1}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a1}"}}}},
      {{"@type":"Question","name":"{faq_q2}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a2}"}}}},
      {{"@type":"Question","name":"{faq_q3}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a3}"}}}}
    ]}}"""

    html = f"""{head_block(title, description, canonical, faq_json)}
<body>
{navbar(filename)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-cn"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — China for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Status</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{max_stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
</tbody>
</table>

<h2>{intro_h2}</h2>
<p>{intro_p}</p>

<h2>{details_h2}</h2>
{details_ul}

<h2>How to Apply</h2>
{how_to}

<h2>Required Documents</h2>
{docs}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://evisa.mfa.gov.cn" target="_blank" rel="noopener">evisa.mfa.gov.cn</a> or your nearest Chinese embassy before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-china.html">China Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="china-visa-requirements.html">China Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="china-visa-fees.html">China Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="china-visa-processing-time.html">China Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{footer()}
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# Main — generate all 40 files
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    generated = []

    for nat_key in NATIONALITIES:
        # Cambodia
        cam_filename = f"cambodia-visa-for-{nat_key}-citizens.html"
        cam_path = os.path.join(OUT_DIR, cam_filename)
        with open(cam_path, "w", encoding="utf-8") as f:
            f.write(cambodia_page(nat_key))
        generated.append(cam_filename)

        # China
        cn_filename = f"china-visa-for-{nat_key}-citizens.html"
        cn_path = os.path.join(OUT_DIR, cn_filename)
        with open(cn_path, "w", encoding="utf-8") as f:
            f.write(china_page(nat_key))
        generated.append(cn_filename)

    print(f"\nGenerated {len(generated)} HTML files in {OUT_DIR}:\n")
    for name in sorted(generated):
        print(f"  {name}")
    print(f"\nTotal: {len(generated)} files.")


if __name__ == "__main__":
    main()
