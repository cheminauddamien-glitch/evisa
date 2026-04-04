#!/usr/bin/env python3
"""
Generate 40 HTML files for Indonesia and Malaysia visa pages.
Output: www/en/indonesia-visa-for-{nat}-citizens.html
        www/en/malaysia-visa-for-{nat}-citizens.html
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NAT_META = {
    "us": {
        "label": "US",
        "adjective": "American",
        "flag": "us",
        "passport": "US",
    },
    "uk": {
        "label": "UK",
        "adjective": "British",
        "flag": "gb",
        "passport": "British",
    },
    "canadian": {
        "label": "Canadian",
        "adjective": "Canadian",
        "flag": "ca",
        "passport": "Canadian",
    },
    "french": {
        "label": "French",
        "adjective": "French",
        "flag": "fr",
        "passport": "French",
    },
    "german": {
        "label": "German",
        "adjective": "German",
        "flag": "de",
        "passport": "German",
    },
    "japanese": {
        "label": "Japanese",
        "adjective": "Japanese",
        "flag": "jp",
        "passport": "Japanese",
    },
    "australian": {
        "label": "Australian",
        "adjective": "Australian",
        "flag": "au",
        "passport": "Australian",
    },
    "indian": {
        "label": "Indian",
        "adjective": "Indian",
        "flag": "in",
        "passport": "Indian",
    },
    "chinese": {
        "label": "Chinese",
        "adjective": "Chinese",
        "flag": "cn",
        "passport": "Chinese",
    },
    "russian": {
        "label": "Russian",
        "adjective": "Russian",
        "flag": "ru",
        "passport": "Russian",
    },
    "brazilian": {
        "label": "Brazilian",
        "adjective": "Brazilian",
        "flag": "br",
        "passport": "Brazilian",
    },
    "mexican": {
        "label": "Mexican",
        "adjective": "Mexican",
        "flag": "mx",
        "passport": "Mexican",
    },
    "south-african": {
        "label": "South African",
        "adjective": "South African",
        "flag": "za",
        "passport": "South African",
    },
    "nigerian": {
        "label": "Nigerian",
        "adjective": "Nigerian",
        "flag": "ng",
        "passport": "Nigerian",
    },
    "korean": {
        "label": "Korean",
        "adjective": "South Korean",
        "flag": "kr",
        "passport": "South Korean",
    },
    "singaporean": {
        "label": "Singaporean",
        "adjective": "Singaporean",
        "flag": "sg",
        "passport": "Singaporean",
    },
    "indonesian": {
        "label": "Indonesian",
        "adjective": "Indonesian",
        "flag": "id",
        "passport": "Indonesian",
    },
    "philippine": {
        "label": "Philippine",
        "adjective": "Filipino",
        "flag": "ph",
        "passport": "Philippine",
    },
    "turkish": {
        "label": "Turkish",
        "adjective": "Turkish",
        "flag": "tr",
        "passport": "Turkish",
    },
    "argentinian": {
        "label": "Argentinian",
        "adjective": "Argentinian",
        "flag": "ar",
        "passport": "Argentinian",
    },
}

NATIONALITIES = list(NAT_META.keys())

# ---------------------------------------------------------------------------
# Indonesia visa status per nationality
# eVOA = Electronic Visa on Arrival, IDR 500,000 (~USD 32), 30 days
# Visa-free (ASEAN) = 30 days
# VoA/eVOA = Visa on Arrival or eVOA option
# Domestic = Indonesian nationals (no visa needed)
# ---------------------------------------------------------------------------
INDONESIA_EVOA_NATS = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian",
    "russian", "turkish",
}
INDONESIA_VISAFREE_ASEAN_NATS = {"philippine"}   # singaporean covered by eVOA group too
INDONESIA_VOA_NATS = {"indian", "chinese", "south-african", "nigerian"}
INDONESIA_DOMESTIC_NATS = {"indonesian"}

# ---------------------------------------------------------------------------
# Malaysia visa status per nationality
# Visa-free 90 days
# Visa-free 30 days (ASEAN)
# Visa required
# ---------------------------------------------------------------------------
MALAYSIA_VISAFREE90_NATS = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian",
}
MALAYSIA_VISAFREE30_ASEAN_NATS = {"indonesian", "philippine"}
MALAYSIA_VISAREQ_NATS = {"indian", "chinese", "russian", "nigerian", "south-african", "turkish"}


# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

def head_section(title, description, canonical_slug, nat_flag, nat_label):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{description}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


def navbar_section(current_slug, nat_flag):
    return f"""<body>
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
                        <a class="dropdown-item active" href="/en/{current_slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""


def footer_section():
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


# ---------------------------------------------------------------------------
# Indonesia page builder
# ---------------------------------------------------------------------------

def build_indonesia_page(nat_key):
    m = NAT_META[nat_key]
    adj = m["adjective"]
    flag = m["flag"]
    label = m["label"]

    slug = f"indonesia-visa-for-{nat_key}-citizens"
    title = f"Indonesia Visa for {label} Citizens 2026"

    # Determine visa status
    if nat_key == "indonesian":
        status_badge = '<span style="color:green;font-weight:600;">No Visa Required — Indonesian Citizens</span>'
        status_short = "No visa required (domestic travel)"
        visa_type = "N/A — Indonesian passport"
        fee = "Free"
        max_stay = "Unlimited (own country)"
        processing = "N/A"
        apply_at = "N/A"
        description = (
            f"Indonesian citizens travelling within Indonesia do not need a visa. "
            f"Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do Indonesian citizens need a visa for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"No. Indonesian citizens are travelling in their own country and do not require any visa."}}}},
      {{"@type":"Question","name":"What document does an Indonesian citizen need to travel domestically?","acceptedAnswer":{{"@type":"Answer","text":"A valid Indonesian national ID (KTP) or passport is sufficient for domestic travel in Indonesia."}}}}
    ]"""
        body_html = f"""<h1><span class="fi fi-{flag}"></span> Indonesia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Indonesia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{max_stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
</tbody>
</table>

<h2>No Visa Required for Indonesian Citizens</h2>
<p>{adj} passport holders are travelling in their own country. No visa is required for travel anywhere in Indonesia.</p>

<h2>Travel Documents</h2>
<ul>
<li>Valid Indonesian passport or national ID (KTP)</li>
<li>No immigration formalities for domestic travel</li>
</ul>"""

    elif nat_key in INDONESIA_EVOA_NATS and nat_key == "singaporean":
        # Singaporean gets both eVOA and visa-free ASEAN — use visa-free (simpler / no fee)
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 days (ASEAN)</span>'
        description = (
            f"Singaporean citizens can enter Indonesia visa-free for up to 30 days under the ASEAN agreement. "
            f"No fee required. Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do Singaporean citizens need a visa for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"No. Singaporean passport holders can enter Indonesia visa-free for up to 30 days under the ASEAN agreement."}}}},
      {{"@type":"Question","name":"Can Singaporeans extend their stay in Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"A 30-day visa-free entry cannot be extended. To stay longer, Singaporeans must apply for an eVOA or a social/business visa."}}}},
      {{"@type":"Question","name":"Which ports of entry are open for visa-free entry?","acceptedAnswer":{{"@type":"Answer","text":"All major international airports and seaports in Indonesia accept visa-free ASEAN arrivals."}}}}
    ]"""
        body_html = _indonesia_visafree_body(adj, flag, label, days=30, reason="ASEAN agreement")

    elif nat_key in INDONESIA_EVOA_NATS:
        status_badge = '<span style="color:darkorange;font-weight:600;">eVOA — IDR 500,000 (~USD 32), 30 days</span>'
        description = (
            f"{adj} citizens visiting Indonesia in 2026 can obtain an Electronic Visa on Arrival (eVOA) "
            f"for IDR 500,000 (~USD 32), valid 30 days, via molina.imigrasi.go.id. Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"{adj} passport holders can obtain an Electronic Visa on Arrival (eVOA) for Indonesia. The fee is IDR 500,000 (~USD 32) and the visa is valid for 30 days."}}}},
      {{"@type":"Question","name":"How do I apply for the Indonesia eVOA?","acceptedAnswer":{{"@type":"Answer","text":"Apply online at molina.imigrasi.go.id before departure. Pay IDR 500,000 (~USD 32) and receive an approval letter to show on arrival."}}}},
      {{"@type":"Question","name":"Can I extend the Indonesia eVOA?","acceptedAnswer":{{"@type":"Answer","text":"Yes. The eVOA can be extended once for an additional 30 days at an Indonesian Immigration office, bringing the total stay to 60 days."}}}}
    ]"""
        body_html = _indonesia_evoa_body(adj, flag, label)

    elif nat_key in INDONESIA_VISAFREE_ASEAN_NATS:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 days (ASEAN)</span>'
        description = (
            f"{adj} citizens can enter Indonesia visa-free for up to 30 days under the ASEAN agreement. "
            f"No fee required. Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"No. {adj} passport holders can enter Indonesia visa-free for up to 30 days under the ASEAN agreement."}}}},
      {{"@type":"Question","name":"Can {adj} citizens extend their stay in Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"The 30-day visa-free entry cannot be extended. To stay longer, a social/business visa or KITAS is required."}}}},
      {{"@type":"Question","name":"Which ports are open for ASEAN visa-free entry?","acceptedAnswer":{{"@type":"Answer","text":"All major international airports and seaports in Indonesia accept ASEAN visa-free arrivals."}}}}
    ]"""
        body_html = _indonesia_visafree_body(adj, flag, label, days=30, reason="ASEAN agreement")

    elif nat_key in INDONESIA_VOA_NATS:
        status_badge = '<span style="color:darkorange;font-weight:600;">Visa on Arrival / eVOA — IDR 500,000 (~USD 32)</span>'
        description = (
            f"{adj} citizens visiting Indonesia in 2026 can obtain a Visa on Arrival (VoA) or eVOA "
            f"for IDR 500,000 (~USD 32), valid 30 days. Apply online at molina.imigrasi.go.id or on arrival. "
            f"Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"{adj} passport holders can obtain a Visa on Arrival (VoA) or Electronic Visa on Arrival (eVOA) for Indonesia. The fee is IDR 500,000 (~USD 32) and the visa is valid for 30 days."}}}},
      {{"@type":"Question","name":"What is the difference between VoA and eVOA for Indonesia?","acceptedAnswer":{{"@type":"Answer","text":"The eVOA is applied online before travel at molina.imigrasi.go.id. The VoA can be obtained on arrival at designated airports. Both cost IDR 500,000 (~USD 32)."}}}},
      {{"@type":"Question","name":"Can {adj} citizens extend the Indonesia VoA?","acceptedAnswer":{{"@type":"Answer","text":"Yes. The VoA/eVOA can be extended once for an additional 30 days at an Indonesian Immigration office."}}}}
    ]"""
        body_html = _indonesia_voa_body(adj, flag, label, nat_key)
    else:
        # Fallback
        status_badge = '<span style="color:red;font-weight:600;">Visa Required</span>'
        description = f"{adj} citizens need a visa for Indonesia. Updated March 2026."
        faq_json = "[]"
        body_html = f"<h1>Indonesia Visa for {label} Citizens 2026</h1><p>Please check the Indonesian immigration website for the latest requirements.</p>"

    faq_ld = f"""{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}"""

    head = head_section(title, description, slug, flag, label)
    head = head.replace("</head>", f"""    <script type="application/ld+json">
    {faq_ld}
    </script>
</head>""")

    related = _related_indonesia(nat_key)

    page = f"""{head}
{navbar_section(slug, flag)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

{body_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current entry requirements at <a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a> before travel.</p>
</div>

{related}

</article>
</div>
</section>

{footer_section()}"""
    return page


def _indonesia_evoa_body(adj, flag, label):
    return f"""<h1><span class="fi fi-{flag}"></span> Indonesia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Indonesia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:darkorange;font-weight:600;">eVOA — IDR 500,000 (~USD 32)</span></td></tr>
<tr><th>Visa Type</th><td>Electronic Visa on Arrival (eVOA)</td></tr>
<tr><th>Fee</th><td>IDR 500,000 (~USD 32)</td></tr>
<tr><th>Max Stay</th><td>30 days (extendable once for 30 more days)</td></tr>
<tr><th>Processing</th><td>Instant to 24 hours online</td></tr>
<tr><th>Apply At</th><td><a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a></td></tr>
</tbody>
</table>

<h2>Indonesia eVOA for {label} Citizens</h2>
<p>{adj} passport holders can enter Indonesia using the <strong>Electronic Visa on Arrival (eVOA)</strong>. The fee is <strong>IDR 500,000 (~USD 32)</strong>, the visa is valid for <strong>30 days</strong>, and it can be extended once for a further 30 days at an Indonesian Immigration office.</p>

<h2>eVOA Key Details</h2>
<ul>
<li>Fee: <strong>IDR 500,000 (~USD 32)</strong></li>
<li>Validity: 30 days from entry</li>
<li>Extension: Once, for 30 additional days (total 60 days)</li>
<li>Entries: Single entry</li>
<li>Purpose: Tourism / short-stay</li>
</ul>

<h2>How to Apply for the Indonesia eVOA</h2>
<ol>
<li>Visit <a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a>.</li>
<li>Complete the online eVOA application form with your passport details.</li>
<li>Upload a passport photo and the passport biographical page.</li>
<li>Pay IDR 500,000 (~USD 32) by credit/debit card.</li>
<li>Receive an approval e-mail with a QR code (usually within minutes to 24 hours).</li>
<li>Print or save the approval letter and present it at immigration on arrival.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond intended stay)</li>
<li>Passport-size photo (digital)</li>
<li>Return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation booking</li>
</ul>

<h2>Entry Points</h2>
<p>The eVOA is accepted at all major international airports (Soekarno-Hatta, Ngurah Rai/Bali, Juanda, Kualanamu, etc.) and major seaports.</p>"""


def _indonesia_voa_body(adj, flag, label, nat_key):
    return f"""<h1><span class="fi fi-{flag}"></span> Indonesia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Indonesia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:darkorange;font-weight:600;">Visa on Arrival (VoA) / eVOA — IDR 500,000 (~USD 32)</span></td></tr>
<tr><th>Visa Type</th><td>Visa on Arrival (VoA) or Electronic Visa on Arrival (eVOA)</td></tr>
<tr><th>Fee</th><td>IDR 500,000 (~USD 32)</td></tr>
<tr><th>Max Stay</th><td>30 days (extendable once for 30 more days)</td></tr>
<tr><th>Processing</th><td>On arrival or online pre-arrival</td></tr>
<tr><th>Apply At</th><td><a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a> (eVOA) or on arrival counter</td></tr>
</tbody>
</table>

<h2>Indonesia Visa on Arrival for {label} Citizens</h2>
<p>{adj} passport holders can enter Indonesia using either the <strong>Visa on Arrival (VoA)</strong> obtained at the airport counter, or the online <strong>Electronic Visa on Arrival (eVOA)</strong> via <a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a>. Both cost <strong>IDR 500,000 (~USD 32)</strong> and allow a 30-day stay.</p>

<h2>VoA / eVOA Key Details</h2>
<ul>
<li>Fee: <strong>IDR 500,000 (~USD 32)</strong></li>
<li>Validity: 30 days from entry</li>
<li>Extension: Once, for 30 additional days</li>
<li>Entries: Single entry</li>
<li>Purpose: Tourism / short-stay</li>
</ul>

<h2>How to Apply</h2>
<h3>Option A — eVOA (recommended, apply before travel)</h3>
<ol>
<li>Visit <a href="https://molina.imigrasi.go.id" target="_blank" rel="noopener">molina.imigrasi.go.id</a>.</li>
<li>Fill in the application with your passport details and upload a photo.</li>
<li>Pay IDR 500,000 online by card.</li>
<li>Receive approval by e-mail; present QR code on arrival.</li>
</ol>
<h3>Option B — Visa on Arrival counter</h3>
<ol>
<li>Proceed to the VoA counter on arrival at a designated airport or seaport.</li>
<li>Pay IDR 500,000 (cash or card, USD/IDR accepted at most airports).</li>
<li>Collect the visa stamp and proceed to immigration.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Return or onward ticket</li>
<li>Proof of accommodation</li>
<li>Sufficient funds for the stay</li>
</ul>"""


def _indonesia_visafree_body(adj, flag, label, days, reason):
    return f"""<h1><span class="fi fi-{flag}"></span> Indonesia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Indonesia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">Visa-Free — {days} days ({reason})</span></td></tr>
<tr><th>Visa Type</th><td>Visa-free entry</td></tr>
<tr><th>Fee</th><td>Free</td></tr>
<tr><th>Max Stay</th><td>{days} days</td></tr>
<tr><th>Processing</th><td>No advance application required</td></tr>
<tr><th>Apply At</th><td>N/A — present passport at immigration</td></tr>
</tbody>
</table>

<h2>Visa-Free Entry to Indonesia for {label} Citizens</h2>
<p>{adj} passport holders can enter Indonesia <strong>visa-free for up to {days} days</strong> under the {reason}. No visa application or fee is required — simply present a valid passport on arrival.</p>

<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond intended stay)</li>
<li>Return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation booking (may be requested)</li>
</ul>

<h2>Important Notes</h2>
<ul>
<li>The {days}-day visa-free stay <strong>cannot be extended</strong> under this category.</li>
<li>For longer stays, apply for an eVOA or social/business visa before travel.</li>
<li>Entry is permitted through all major international airports and seaports.</li>
</ul>"""


def _related_indonesia(nat_key):
    return """<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-indonesia.html">Indonesia Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="indonesia-visa-requirements.html">Indonesia Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="indonesia-visa-fees.html">Indonesia Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="indonesia-visa-processing-time.html">Indonesia Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>"""


# ---------------------------------------------------------------------------
# Malaysia page builder
# ---------------------------------------------------------------------------

def build_malaysia_page(nat_key):
    m = NAT_META[nat_key]
    adj = m["adjective"]
    flag = m["flag"]
    label = m["label"]

    slug = f"malaysia-visa-for-{nat_key}-citizens"
    title = f"Malaysia Visa for {label} Citizens 2026"

    if nat_key in MALAYSIA_VISAFREE90_NATS:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 90 days</span>'
        description = (
            f"{adj} citizens can visit Malaysia visa-free for up to 90 days. "
            f"No application required. Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Malaysia?","acceptedAnswer":{{"@type":"Answer","text":"No. {adj} passport holders can enter Malaysia visa-free for up to 90 days for tourism or business."}}}},
      {{"@type":"Question","name":"Can {adj} citizens extend their stay in Malaysia?","acceptedAnswer":{{"@type":"Answer","text":"Extensions beyond 90 days are generally not granted for tourist entries. Contact the Immigration Department of Malaysia for further options."}}}},
      {{"@type":"Question","name":"What documents are needed to enter Malaysia visa-free?","acceptedAnswer":{{"@type":"Answer","text":"A valid passport (6+ months validity), return ticket, and proof of accommodation are typically required."}}}}
    ]"""
        body_html = _malaysia_visafree_body(adj, flag, label, days=90)

    elif nat_key in MALAYSIA_VISAFREE30_ASEAN_NATS:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 days (ASEAN)</span>'
        description = (
            f"{adj} citizens can visit Malaysia visa-free for up to 30 days under the ASEAN agreement. "
            f"No application required. Updated March 2026."
        )
        faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Malaysia?","acceptedAnswer":{{"@type":"Answer","text":"No. {adj} passport holders can enter Malaysia visa-free for up to 30 days under the ASEAN agreement."}}}},
      {{"@type":"Question","name":"Can {adj} citizens extend their stay in Malaysia?","acceptedAnswer":{{"@type":"Answer","text":"The 30-day ASEAN visa-free stay may be extendable at the Immigration Department. Check with authorities before travel."}}}},
      {{"@type":"Question","name":"What documents are needed?","acceptedAnswer":{{"@type":"Answer","text":"A valid passport (6+ months validity), return ticket, and proof of sufficient funds are typically required."}}}}
    ]"""
        body_html = _malaysia_visafree_body(adj, flag, label, days=30, note="ASEAN agreement")

    elif nat_key in MALAYSIA_VISAREQ_NATS:
        # Special handling: Indian eVisa available online
        if nat_key == "indian":
            status_badge = '<span style="color:red;font-weight:600;">Visa Required — eVisa available online</span>'
            description = (
                "Indian citizens visiting Malaysia in 2026 must obtain a visa. "
                "An eVisa (eNTRI or eVisa) is available online via the Malaysian Immigration portal. Updated March 2026."
            )
            faq_json = """[
      {"@type":"Question","name":"Do Indian citizens need a visa for Malaysia?","acceptedAnswer":{"@type":"Answer","text":"Yes. Indian passport holders must obtain a Malaysian visa. An eVisa (eNTRI or eVisa) is available online via the Malaysian Immigration eVisa portal."}},
      {"@type":"Question","name":"How do Indian citizens apply for a Malaysia eVisa?","acceptedAnswer":{"@type":"Answer","text":"Apply online through the Malaysian Immigration eVisa portal at evisa.imi.gov.my. Submit your passport details, photo, and pay the fee online."}},
      {"@type":"Question","name":"What is the Malaysia eNTRI for Indian citizens?","acceptedAnswer":{"@type":"Answer","text":"The eNTRI (Electronic Travel Registration and Information) allows eligible Indian citizens to visit Malaysia for up to 15 days. It is a simplified online registration linked to specific routes."}}
    ]"""
            body_html = _malaysia_evisa_body_indian(adj, flag, label)
        else:
            status_badge = '<span style="color:red;font-weight:600;">Visa Required</span>'
            description = (
                f"{adj} citizens visiting Malaysia in 2026 must obtain a visa in advance. "
                f"Apply via the Malaysian eVisa portal or at a Malaysian consulate. Updated March 2026."
            )
            faq_json = f"""[
      {{"@type":"Question","name":"Do {adj} citizens need a visa for Malaysia?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {adj} passport holders must obtain a Malaysian visa before travel. Apply via the eVisa portal at evisa.imi.gov.my or through a Malaysian consulate."}}}},
      {{"@type":"Question","name":"How do {adj} citizens apply for a Malaysia visa?","acceptedAnswer":{{"@type":"Answer","text":"Apply online at evisa.imi.gov.my or in person at the nearest Malaysian consulate or embassy. Provide a valid passport, photo, and supporting documents."}}}},
      {{"@type":"Question","name":"How long does a Malaysian visa take to process?","acceptedAnswer":{{"@type":"Answer","text":"Online eVisa applications are typically processed within 3–5 business days. Consular applications may take 5–10 business days."}}}}
    ]"""
            body_html = _malaysia_visareq_body(adj, flag, label, nat_key)
    else:
        status_badge = '<span style="color:red;font-weight:600;">Visa Required</span>'
        description = f"{adj} citizens need a visa for Malaysia. Updated March 2026."
        faq_json = "[]"
        body_html = f"<h1>Malaysia Visa for {label} Citizens 2026</h1><p>Please check the Malaysian Immigration website for the latest requirements.</p>"

    faq_ld = f"""{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}"""

    head = head_section(title, description, slug, flag, label)
    head = head.replace("</head>", f"""    <script type="application/ld+json">
    {faq_ld}
    </script>
</head>""")

    related = _related_malaysia(nat_key)

    page = f"""{head}
{navbar_section(slug, flag)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

{body_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current entry requirements at <a href="https://www.imi.gov.my" target="_blank" rel="noopener">imi.gov.my</a> before travel.</p>
</div>

{related}

</article>
</div>
</section>

{footer_section()}"""
    return page


def _malaysia_visafree_body(adj, flag, label, days, note=None):
    note_str = f" under the {note}" if note else ""
    return f"""<h1><span class="fi fi-{flag}"></span> Malaysia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Malaysia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">Visa-Free — {days} days{note_str}</span></td></tr>
<tr><th>Visa Type</th><td>Visa-free entry</td></tr>
<tr><th>Fee</th><td>Free</td></tr>
<tr><th>Max Stay</th><td>{days} days per entry</td></tr>
<tr><th>Processing</th><td>No advance application required</td></tr>
<tr><th>Apply At</th><td>N/A — present passport at immigration</td></tr>
</tbody>
</table>

<h2>Visa-Free Entry to Malaysia for {label} Citizens</h2>
<p>{adj} passport holders can enter Malaysia <strong>visa-free for up to {days} days</strong>{note_str}. No visa application or fee is required — present a valid passport at the point of entry.</p>

<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond intended stay)</li>
<li>Return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details (may be requested)</li>
</ul>

<h2>Important Notes</h2>
<ul>
<li>The visa-free allowance of {days} days is for tourism and short business visits.</li>
<li>Extensions are generally not available; depart before your allowed period expires.</li>
<li>Working or studying in Malaysia requires separate authorisation.</li>
<li>Entry is through all designated international ports of entry in Malaysia.</li>
</ul>"""


def _malaysia_visareq_body(adj, flag, label, nat_key):
    return f"""<h1><span class="fi fi-{flag}"></span> Malaysia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Malaysia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Visa Required</span></td></tr>
<tr><th>Visa Type</th><td>Single/Multiple Entry Tourist Visa or eVisa</td></tr>
<tr><th>Fee</th><td>Varies (approx. MYR 100–200 / USD 22–45)</td></tr>
<tr><th>Max Stay</th><td>30 days (single entry tourist visa)</td></tr>
<tr><th>Processing</th><td>3–10 business days</td></tr>
<tr><th>Apply At</th><td><a href="https://evisa.imi.gov.my" target="_blank" rel="noopener">evisa.imi.gov.my</a> or Malaysian consulate</td></tr>
</tbody>
</table>

<h2>Malaysia Visa for {label} Citizens</h2>
<p>{adj} passport holders must obtain a Malaysian visa before travelling. Apply via the <strong>Malaysian eVisa portal</strong> at <a href="https://evisa.imi.gov.my" target="_blank" rel="noopener">evisa.imi.gov.my</a> or at the nearest Malaysian embassy or consulate.</p>

<h2>Visa Options</h2>
<ul>
<li><strong>eVisa (online)</strong> — apply at evisa.imi.gov.my; single or multiple entry; valid 3 months from issue; stay up to 30 days</li>
<li><strong>Consular visa</strong> — apply in person at a Malaysian embassy/consulate</li>
</ul>

<h2>How to Apply Online (eVisa)</h2>
<ol>
<li>Visit <a href="https://evisa.imi.gov.my" target="_blank" rel="noopener">evisa.imi.gov.my</a>.</li>
<li>Create an account and complete the application form.</li>
<li>Upload passport bio page, recent passport photo, and supporting documents.</li>
<li>Pay the visa fee online.</li>
<li>Receive the eVisa by e-mail (typically within 3–5 business days).</li>
<li>Print or save the eVisa approval and present it on arrival.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Recent passport-size photo</li>
<li>Return or onward flight ticket</li>
<li>Accommodation booking / hotel confirmation</li>
<li>Bank statement / proof of sufficient funds</li>
<li>Travel itinerary</li>
</ul>"""


def _malaysia_evisa_body_indian(adj, flag, label):
    return f"""<h1><span class="fi fi-{flag}"></span> Malaysia Visa for {label} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Malaysia for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Visa Required — eVisa available online</span></td></tr>
<tr><th>Visa Type</th><td>Malaysia eVisa or eNTRI</td></tr>
<tr><th>Fee</th><td>Approx. MYR 100–200 (~USD 22–45)</td></tr>
<tr><th>Max Stay</th><td>eNTRI: 15 days; eVisa: 30 days</td></tr>
<tr><th>Processing</th><td>1–5 business days</td></tr>
<tr><th>Apply At</th><td><a href="https://evisa.imi.gov.my" target="_blank" rel="noopener">evisa.imi.gov.my</a></td></tr>
</tbody>
</table>

<h2>Malaysia Visa for {label} Citizens</h2>
<p>{adj} passport holders are required to obtain a visa before entering Malaysia. Two convenient online options are available: the <strong>Malaysia eVisa</strong> and the <strong>eNTRI</strong> (Electronic Travel Registration and Information).</p>

<h2>eNTRI vs eVisa — Which to Choose?</h2>
<ul>
<li><strong>eNTRI</strong> — for stays up to 15 days; available for specific air routes; lower fee; processed quickly</li>
<li><strong>eVisa</strong> — for stays up to 30 days; broader eligibility; single or multiple entry</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Visit <a href="https://evisa.imi.gov.my" target="_blank" rel="noopener">evisa.imi.gov.my</a>.</li>
<li>Register and complete the eVisa or eNTRI application.</li>
<li>Upload your passport bio page and a recent passport photo.</li>
<li>Pay the fee online by credit/debit card.</li>
<li>Receive your approved eVisa/eNTRI by e-mail.</li>
<li>Present the approval document on arrival in Malaysia.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid Indian passport (minimum 6 months validity)</li>
<li>Recent passport-size photograph</li>
<li>Return or onward flight ticket</li>
<li>Hotel or accommodation booking</li>
<li>Bank statement / proof of funds</li>
<li>Travel itinerary</li>
</ul>"""


def _related_malaysia(nat_key):
    return """<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-malaysia.html">Malaysia Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="malaysia-visa-requirements.html">Malaysia Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="malaysia-visa-fees.html">Malaysia Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="malaysia-visa-processing-time.html">Malaysia Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for nat in NATIONALITIES:
        # Indonesia
        idn_filename = f"indonesia-visa-for-{nat}-citizens.html"
        idn_path = os.path.join(OUT_DIR, idn_filename)
        content = build_indonesia_page(nat)
        with open(idn_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(idn_filename)

        # Malaysia
        mys_filename = f"malaysia-visa-for-{nat}-citizens.html"
        mys_path = os.path.join(OUT_DIR, mys_filename)
        content = build_malaysia_page(nat)
        with open(mys_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(mys_filename)

    print(f"Created {len(created)} files in {OUT_DIR}:")
    for fname in sorted(created):
        print(f"  {fname}")


if __name__ == "__main__":
    main()
