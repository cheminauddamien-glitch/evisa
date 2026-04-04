#!/usr/bin/env python3
"""
Generate 40 HTML files in www/en/:
  singapore-visa-for-{nat}-citizens.html  (20 files)
  philippines-visa-for-{nat}-citizens.html (20 files)
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Nationality meta-data
# ---------------------------------------------------------------------------
NAT_META = {
    "us": {
        "label": "US", "adjective": "US", "demonym": "US citizens",
        "flag": "us", "passport": "US passport holders",
    },
    "uk": {
        "label": "UK", "adjective": "British", "demonym": "UK citizens",
        "flag": "gb", "passport": "UK / British passport holders",
    },
    "canadian": {
        "label": "Canadian", "adjective": "Canadian", "demonym": "Canadian citizens",
        "flag": "ca", "passport": "Canadian passport holders",
    },
    "french": {
        "label": "French", "adjective": "French", "demonym": "French citizens",
        "flag": "fr", "passport": "French passport holders",
    },
    "german": {
        "label": "German", "adjective": "German", "demonym": "German citizens",
        "flag": "de", "passport": "German passport holders",
    },
    "japanese": {
        "label": "Japanese", "adjective": "Japanese", "demonym": "Japanese citizens",
        "flag": "jp", "passport": "Japanese passport holders",
    },
    "australian": {
        "label": "Australian", "adjective": "Australian", "demonym": "Australian citizens",
        "flag": "au", "passport": "Australian passport holders",
    },
    "indian": {
        "label": "Indian", "adjective": "Indian", "demonym": "Indian citizens",
        "flag": "in", "passport": "Indian passport holders",
    },
    "chinese": {
        "label": "Chinese", "adjective": "Chinese", "demonym": "Chinese citizens",
        "flag": "cn", "passport": "Chinese passport holders",
    },
    "russian": {
        "label": "Russian", "adjective": "Russian", "demonym": "Russian citizens",
        "flag": "ru", "passport": "Russian passport holders",
    },
    "brazilian": {
        "label": "Brazilian", "adjective": "Brazilian", "demonym": "Brazilian citizens",
        "flag": "br", "passport": "Brazilian passport holders",
    },
    "mexican": {
        "label": "Mexican", "adjective": "Mexican", "demonym": "Mexican citizens",
        "flag": "mx", "passport": "Mexican passport holders",
    },
    "south-african": {
        "label": "South African", "adjective": "South African", "demonym": "South African citizens",
        "flag": "za", "passport": "South African passport holders",
    },
    "nigerian": {
        "label": "Nigerian", "adjective": "Nigerian", "demonym": "Nigerian citizens",
        "flag": "ng", "passport": "Nigerian passport holders",
    },
    "korean": {
        "label": "Korean", "adjective": "South Korean", "demonym": "Korean citizens",
        "flag": "kr", "passport": "South Korean passport holders",
    },
    "singaporean": {
        "label": "Singaporean", "adjective": "Singaporean", "demonym": "Singaporean citizens",
        "flag": "sg", "passport": "Singaporean passport holders",
    },
    "indonesian": {
        "label": "Indonesian", "adjective": "Indonesian", "demonym": "Indonesian citizens",
        "flag": "id", "passport": "Indonesian passport holders",
    },
    "philippine": {
        "label": "Philippine", "adjective": "Philippine", "demonym": "Philippine citizens",
        "flag": "ph", "passport": "Philippine passport holders",
    },
    "turkish": {
        "label": "Turkish", "adjective": "Turkish", "demonym": "Turkish citizens",
        "flag": "tr", "passport": "Turkish passport holders",
    },
    "argentinian": {
        "label": "Argentinian", "adjective": "Argentinian", "demonym": "Argentinian citizens",
        "flag": "ar", "passport": "Argentinian passport holders",
    },
}

NATIONALITIES = list(NAT_META.keys())

# ---------------------------------------------------------------------------
# Singapore visa status per nationality
# ---------------------------------------------------------------------------
# Groups:
#   vf30   – Visa-free 30 days
#   vf96h  – Visa-free 96-hour transit (with conditions)
#   req    – Visa required (ICA e-service)
# Note: chinese appears in BOTH vf96h and req (96h transit is a separate scheme
#       but standard entry requires a visa).

SG_STATUS = {
    "us":           "vf30",
    "uk":           "vf30",
    "canadian":     "vf30",
    "french":       "vf30",
    "german":       "vf30",
    "japanese":     "vf30",
    "australian":   "vf30",
    "korean":       "vf30",
    "brazilian":    "vf30",
    "mexican":      "vf30",
    "argentinian":  "vf30",
    "indonesian":   "vf30",   # ASEAN
    "philippine":   "vf30",   # ASEAN
    "chinese":      "vf96h",  # 96-hour visa-free transit; standard visit needs visa
    "indian":       "req",    # 96-hour VFTF exists but with strict conditions → listed as req
    "russian":      "req",
    "nigerian":     "req",
    "south-african":"req",
    "turkish":      "req",
    "singaporean":  "citizen", # Singaporean citizens in Singapore – special case
}

# ---------------------------------------------------------------------------
# Philippines visa status per nationality
# ---------------------------------------------------------------------------
# Groups:
#   vf30  – Visa-free 30 days on arrival
#   vf59  – Visa-free 59 days (extended, since 2023)
#   evisa – eVisa required (evisa.gov.ph, PHP 1,500)

PH_STATUS = {
    "us":           "vf30",
    "uk":           "vf30",
    "canadian":     "vf30",
    "french":       "vf30",
    "german":       "vf30",
    "japanese":     "vf30",
    "australian":   "vf30",
    "korean":       "vf30",
    "singaporean":  "vf30",
    "brazilian":    "vf30",
    "mexican":      "vf30",
    "argentinian":  "vf30",
    "indonesian":   "vf30",   # ASEAN
    "chinese":      "vf59",   # Extended since 2023
    "indian":       "evisa",
    "russian":      "evisa",
    "nigerian":     "evisa",
    "south-african":"evisa",
    "turkish":      "evisa",
    "philippine":   "citizen", # Philippine citizens in Philippines – special case
}

# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

GA4 = """    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>"""

NAVBAR = """<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
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
                        <a class="dropdown-item active" href="#"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="../destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

FOOTER = """<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                    <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                    <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                    <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                </ul>
                <p class="mt-4">&#169; 2026 eVisa-Card.com &#8212; Global eVisa &amp; Travel Information Platform</p>
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

# ---------------------------------------------------------------------------
# Singapore page builder
# ---------------------------------------------------------------------------

def build_sg_page(nat_key):
    m = NAT_META[nat_key]
    status = SG_STATUS[nat_key]
    nat_label = m["label"]
    adj = m["adjective"]
    demonym = m["demonym"]
    passport = m["passport"]
    flag = m["flag"]
    slug = f"singapore-visa-for-{nat_key}-citizens"
    title = f"Singapore Visa for {nat_label} Citizens 2026"
    canonical = f"https://www.evisa-card.com/en/{slug}"

    # ---- status-specific content ----
    if status == "vf30":
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 Days</span>'
        desc = (
            f"{passport} enjoy <strong>visa-free entry to Singapore for up to 30 days</strong>. "
            "No pre-arranged visa is required; simply present a valid passport, proof of onward travel, "
            "and sufficient funds at the Singapore Immigration checkpoint."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Maximum Stay</th><td>30 days</td></tr>
<tr><th>Entry Type</th><td>Multiple entries permitted</td></tr>
<tr><th>Extension</th><td>Possible in-country (ICA discretion)</td></tr>
<tr><th>Official Authority</th><td>ICA — ica.gov.sg</td></tr>"""
        body_sections = f"""<h2>Visa-Free Entry for {nat_label} Citizens</h2>
<p>{desc}</p>
<h2>Conditions for Entry</h2>
<ul>
<li>Valid passport with at least 6 months validity</li>
<li>Confirmed onward/return ticket</li>
<li>Sufficient funds for the duration of stay</li>
<li>Accommodation details (hotel booking or host address)</li>
<li>No criminal record that would bar entry</li>
</ul>
<h2>Extending Your Stay</h2>
<p>Extensions beyond 30 days may be requested at an <a href="https://www.ica.gov.sg" target="_blank" rel="noopener">ICA service centre</a> before expiry. Approval is at the Immigration &amp; Checkpoints Authority's discretion.</p>"""
        faq = [
            (f"Do {nat_label} citizens need a visa for Singapore?",
             f"No. {passport} can enter Singapore visa-free for up to 30 days for tourism and short business visits."),
            ("Can I extend my stay in Singapore?",
             "Yes. Visit an ICA service centre before your 30-day allowance expires to apply for an extension."),
            ("What documents do I need to enter Singapore visa-free?",
             "You need a valid passport (6+ months), onward/return ticket, accommodation details, and sufficient funds."),
        ]

    elif status == "vf96h":
        status_badge = '<span style="color:orange;font-weight:600;">Visa-Free Transit — 96 Hours (with conditions) / Visa Required for Standard Visit</span>'
        desc = (
            f"{passport} may use Singapore's <strong>96-Hour Visa-Free Transit Facility (VFTF)</strong> "
            "when transiting through Changi Airport, subject to meeting specific conditions. "
            "For a standard tourist visit beyond transit, a <strong>Singapore Tourist Visa</strong> must be obtained in advance through ICA."
        )
        table_rows = f"""<tr><th>Transit (VFTF)</th><td><span style="color:orange;font-weight:600;">Visa-Free — 96 Hours (conditions apply)</span></td></tr>
<tr><th>Standard Tourist Visit</th><td><span style="color:red;font-weight:600;">Visa Required</span></td></tr>
<tr><th>Tourist Visa Fee</th><td>SGD 30 (approximately)</td></tr>
<tr><th>Processing</th><td>3–5 working days</td></tr>
<tr><th>Apply At</th><td>ICA e-Service (ica.gov.sg) or Singapore Embassy</td></tr>"""
        body_sections = f"""<h2>96-Hour Visa-Free Transit for {nat_label} Citizens</h2>
<p>{desc}</p>
<h3>VFTF Eligibility Conditions</h3>
<ul>
<li>Confirmed onward ticket departing Singapore within 96 hours</li>
<li>Valid travel document and destination country visa (if applicable)</li>
<li>Sufficient funds and no adverse immigration history</li>
<li>Transit through Changi Airport only</li>
</ul>
<h2>Singapore Tourist Visa (Standard Visit)</h2>
<p>For a regular tourist visit, {passport} must apply for a <strong>Singapore Tourist Visa</strong> via the <a href="https://www.ica.gov.sg" target="_blank" rel="noopener">ICA e-Service portal</a> or through an authorised agent or Singapore embassy.</p>
<h3>Application Requirements</h3>
<ul>
<li>Valid passport (6+ months validity)</li>
<li>Completed visa application form</li>
<li>Passport-sized photographs</li>
<li>Bank statements (last 3 months)</li>
<li>Confirmed return/onward ticket</li>
<li>Hotel booking or invitation letter</li>
</ul>"""
        faq = [
            (f"Can {nat_label} citizens enter Singapore without a visa?",
             "For transit up to 96 hours, the Visa-Free Transit Facility may apply with conditions. For a standard tourist visit, a visa must be obtained in advance."),
            ("How do I apply for a Singapore Tourist Visa?",
             "Apply through the ICA e-Service portal at ica.gov.sg or submit your application at a Singapore embassy in your home country."),
            ("How long does Singapore visa processing take?",
             "Typically 3–5 working days. Apply well in advance of your travel date."),
        ]

    elif status == "req":
        status_badge = '<span style="color:red;font-weight:600;">Visa Required</span>'
        desc = (
            f"{passport} <strong>require a visa to enter Singapore</strong>. "
            "Applications are submitted online through the ICA e-Service portal or via a Singapore embassy. "
            "The tourist visa fee is approximately SGD 30 and processing takes 3–5 working days."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Fee</th><td>SGD 30 (approximately)</td></tr>
<tr><th>Processing Time</th><td>3–5 working days</td></tr>
<tr><th>Maximum Stay</th><td>30 days (as granted)</td></tr>
<tr><th>Apply At</th><td>ICA e-Service — ica.gov.sg</td></tr>"""
        body_sections = f"""<h2>Singapore Visa for {nat_label} Citizens</h2>
<p>{desc}</p>
<h2>How to Apply</h2>
<ol>
<li>Visit <a href="https://www.ica.gov.sg" target="_blank" rel="noopener">ica.gov.sg</a> and access the e-Visa application portal, or contact a Singapore embassy in your country.</li>
<li>Complete the Singapore Tourist Visa application form.</li>
<li>Upload all required supporting documents.</li>
<li>Pay the visa fee of approximately SGD 30.</li>
<li>Await a decision (typically 3–5 working days).</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Completed visa application form</li>
<li>Recent passport-sized photographs</li>
<li>Bank statements (last 3 months)</li>
<li>Confirmed return/onward ticket</li>
<li>Hotel booking or host invitation letter</li>
<li>Travel insurance (recommended)</li>
</ul>"""
        faq = [
            (f"Do {nat_label} citizens need a visa for Singapore?",
             f"Yes. {passport} must obtain a Singapore Tourist Visa before travel. Apply via the ICA e-Service portal at ica.gov.sg."),
            ("How much does a Singapore visa cost?",
             "The Singapore tourist visa fee is approximately SGD 30. Additional service charges may apply if applying through an agent."),
            ("How long does Singapore visa processing take?",
             "Standard processing takes 3–5 working days. Apply at least 2 weeks before your intended travel date."),
        ]

    elif status == "citizen":
        status_badge = '<span style="color:green;font-weight:600;">No Visa Required — Citizens</span>'
        desc = (
            "Singaporean citizens do not require any visa to enter Singapore — it is their home country."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Entry</th><td>Unrestricted — home country</td></tr>"""
        body_sections = f"""<h2>Singapore for Singaporean Citizens</h2>
<p>{desc}</p>"""
        faq = [
            ("Do Singaporean citizens need a visa for Singapore?",
             "No. Singapore is their home country and citizens have unconditional right of entry."),
        ]
    else:
        status_badge = "See details below"
        desc = ""
        table_rows = ""
        body_sections = ""
        faq = []

    faq_schema_items = ",\n".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq
    )
    faq_html = "\n".join(
        f"<details class='mb-2'><summary><strong>{q}</strong></summary><p class='pt-2'>{a}</p></details>"
        for q, a in faq
    )

    meta_desc = (
        f"{nat_label} passport holders visiting Singapore 2026: {desc[:120].rstrip('.')}. "
        "Updated March 2026."
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA4}
    <title>{title}</title>
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
      {faq_schema_items}
    ]}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}" style="vertical-align:middle;margin-right:8px;"></span><span class="fi fi-sg" style="vertical-align:middle;margin-right:8px;"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Singapore for {nat_label} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_sections}

<h2>Frequently Asked Questions</h2>
{faq_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://www.ica.gov.sg" target="_blank" rel="noopener">ica.gov.sg</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-singapore.html">Singapore Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="singapore-visa-requirements.html">Singapore Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="singapore-visa-fees.html">Singapore Fees</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#8594;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# Philippines page builder
# ---------------------------------------------------------------------------

def build_ph_page(nat_key):
    m = NAT_META[nat_key]
    status = PH_STATUS[nat_key]
    nat_label = m["label"]
    adj = m["adjective"]
    demonym = m["demonym"]
    passport = m["passport"]
    flag = m["flag"]
    slug = f"philippines-visa-for-{nat_key}-citizens"
    title = f"Philippines Visa for {nat_label} Citizens 2026"
    canonical = f"https://www.evisa-card.com/en/{slug}"

    if status == "vf30":
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 Days on Arrival</span>'
        desc = (
            f"{passport} enjoy <strong>visa-free entry to the Philippines for up to 30 days on arrival</strong>. "
            "No prior visa is required for tourism or short business trips."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Maximum Stay</th><td>30 days (on arrival)</td></tr>
<tr><th>Extension</th><td>Up to 29 days (Bureau of Immigration)</td></tr>
<tr><th>Fee</th><td>Free</td></tr>
<tr><th>Official Authority</th><td>Bureau of Immigration — immigration.gov.ph</td></tr>"""
        body_sections = f"""<h2>Visa-Free Entry for {nat_label} Citizens</h2>
<p>{desc}</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport with at least 6 months validity beyond intended stay</li>
<li>Confirmed return or onward ticket</li>
<li>Proof of sufficient funds (USD 50/day or equivalent)</li>
<li>Accommodation details</li>
</ul>
<h2>Extending Your Stay</h2>
<p>Visitors may extend their stay at a <a href="https://www.immigration.gov.ph" target="_blank" rel="noopener">Bureau of Immigration</a> office. Extensions are issued in 29-day increments up to a maximum of 36 months total, at a fee per extension.</p>"""
        faq = [
            (f"Do {nat_label} citizens need a visa for the Philippines?",
             f"No. {passport} can enter the Philippines visa-free for up to 30 days on arrival for tourism."),
            ("Can I extend my 30-day visa-free stay in the Philippines?",
             "Yes. Visit a Bureau of Immigration office to apply for extensions in 29-day increments."),
            ("What documents are needed to enter the Philippines visa-free?",
             "You need a valid passport (6+ months validity), a confirmed return/onward ticket, proof of funds, and accommodation details."),
        ]

    elif status == "vf59":
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 59 Days (since 2023 policy)</span>'
        desc = (
            f"{passport} benefit from an <strong>extended visa-free stay of up to 59 days</strong> in the Philippines "
            "under the policy introduced in 2023, allowing longer tourism and business visits without a prior visa."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Maximum Stay</th><td>59 days (on arrival)</td></tr>
<tr><th>Extension</th><td>Available at Bureau of Immigration</td></tr>
<tr><th>Fee</th><td>Free</td></tr>
<tr><th>Policy Introduced</th><td>2023</td></tr>
<tr><th>Official Authority</th><td>Bureau of Immigration — immigration.gov.ph</td></tr>"""
        body_sections = f"""<h2>Extended Visa-Free Entry for {nat_label} Citizens</h2>
<p>{desc}</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport with at least 6 months validity</li>
<li>Confirmed return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details</li>
</ul>
<h2>Policy Background</h2>
<p>The Philippines extended visa-free access for Chinese nationals to 59 days as part of bilateral tourism initiatives in 2023. Travellers should confirm current policy at <a href="https://www.immigration.gov.ph" target="_blank" rel="noopener">immigration.gov.ph</a> before travel.</p>"""
        faq = [
            (f"Do {nat_label} citizens need a visa for the Philippines?",
             f"No. {passport} can enter the Philippines visa-free for up to 59 days under the 2023 extended stay policy."),
            ("Is the 59-day visa-free policy permanent?",
             "The policy was introduced in 2023. Travellers should verify current status at immigration.gov.ph before departure."),
            ("Can the 59-day stay be extended?",
             "Yes. Extensions can be applied for at a Bureau of Immigration office before the initial period expires."),
        ]

    elif status == "evisa":
        status_badge = '<span style="color:orange;font-weight:600;">eVisa Required — PHP 1,500</span>'
        desc = (
            f"{passport} must obtain a Philippine <strong>eVisa before travel</strong>. "
            "Applications are submitted online at <a href='https://evisa.gov.ph' target='_blank' rel='noopener'>evisa.gov.ph</a>. "
            "The fee is <strong>PHP 1,500</strong> and processing typically takes 3–5 business days."
        )
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>Philippine eVisa</td></tr>
<tr><th>Fee</th><td>PHP 1,500</td></tr>
<tr><th>Processing Time</th><td>3–5 business days</td></tr>
<tr><th>Maximum Stay</th><td>30 days (extendable)</td></tr>
<tr><th>Apply At</th><td>evisa.gov.ph</td></tr>"""
        body_sections = f"""<h2>Philippine eVisa for {nat_label} Citizens</h2>
<p>{desc}</p>
<h2>How to Apply</h2>
<ol>
<li>Go to <a href="https://evisa.gov.ph" target="_blank" rel="noopener">evisa.gov.ph</a>.</li>
<li>Create an account and start a new eVisa application.</li>
<li>Upload required documents (passport bio-page, photo, return ticket, accommodation).</li>
<li>Pay PHP 1,500 via the online payment portal.</li>
<li>Receive your approved eVisa by email (3–5 business days).</li>
<li>Print or save the eVisa and present it on arrival.</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid passport (6+ months validity)</li>
<li>Digital passport-sized photograph</li>
<li>Confirmed return/onward ticket</li>
<li>Hotel booking or invitation letter</li>
<li>Proof of sufficient funds</li>
<li>Travel insurance (recommended)</li>
</ul>"""
        faq = [
            (f"Do {nat_label} citizens need a visa for the Philippines?",
             f"Yes. {passport} must apply for a Philippine eVisa online at evisa.gov.ph before travelling."),
            ("How much does the Philippine eVisa cost?",
             "The eVisa fee is PHP 1,500 (approximately USD 26). Payment is made online during the application."),
            ("How long does Philippine eVisa processing take?",
             "Processing typically takes 3–5 business days. Apply at least 2 weeks before travel for safety."),
        ]

    elif status == "citizen":
        status_badge = '<span style="color:green;font-weight:600;">No Visa Required — Citizens</span>'
        desc = "Philippine citizens do not require any visa to enter the Philippines — it is their home country."
        table_rows = f"""<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Entry</th><td>Unrestricted — home country</td></tr>"""
        body_sections = f"""<h2>Philippines for Philippine Citizens</h2>
<p>{desc}</p>"""
        faq = [
            ("Do Philippine citizens need a visa for the Philippines?",
             "No. The Philippines is their home country and citizens have unconditional right of entry."),
        ]
    else:
        status_badge = "See details below"
        desc = ""
        table_rows = ""
        body_sections = ""
        faq = []

    faq_schema_items = ",\n".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq
    )
    faq_html = "\n".join(
        f"<details class='mb-2'><summary><strong>{q}</strong></summary><p class='pt-2'>{a}</p></details>"
        for q, a in faq
    )

    meta_desc = (
        f"{nat_label} passport holders visiting the Philippines 2026: {desc[:120].rstrip('.')}. "
        "Updated March 2026."
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA4}
    <title>{title}</title>
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
      {faq_schema_items}
    ]}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}" style="vertical-align:middle;margin-right:8px;"></span><span class="fi fi-ph" style="vertical-align:middle;margin-right:8px;"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Philippines for {nat_label} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_sections}

<h2>Frequently Asked Questions</h2>
{faq_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://www.immigration.gov.ph" target="_blank" rel="noopener">immigration.gov.ph</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-philippines.html">Philippines Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="philippines-visa-requirements.html">Philippines Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="philippines-visa-fees.html">Philippines Fees</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#8594;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>"""
    return html


# ---------------------------------------------------------------------------
# Main — generate all 40 files
# ---------------------------------------------------------------------------

def main():
    created = []
    for nat in NATIONALITIES:
        # Singapore
        sg_filename = f"singapore-visa-for-{nat}-citizens.html"
        sg_path = os.path.join(OUT_DIR, sg_filename)
        with open(sg_path, "w", encoding="utf-8") as f:
            f.write(build_sg_page(nat))
        created.append(sg_filename)

        # Philippines
        ph_filename = f"philippines-visa-for-{nat}-citizens.html"
        ph_path = os.path.join(OUT_DIR, ph_filename)
        with open(ph_path, "w", encoding="utf-8") as f:
            f.write(build_ph_page(nat))
        created.append(ph_filename)

    print(f"\nDone. Generated {len(created)} HTML files in {OUT_DIR}\n")
    for fn in sorted(created):
        print(f"  {fn}")


if __name__ == "__main__":
    main()
