#!/usr/bin/env python3
"""
Generate 40 HTML files:
  - taiwan-visa-for-{nat}-citizens.html   (20 files)
  - sri-lanka-visa-for-{nat}-citizens.html (20 files)
Output directory: www/en/
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATIONALITIES = {
    "us":           {"label": "US",           "demonym": "US",           "flag": "us"},
    "uk":           {"label": "UK",           "demonym": "British",      "flag": "gb"},
    "canadian":     {"label": "Canadian",     "demonym": "Canadian",     "flag": "ca"},
    "french":       {"label": "French",       "demonym": "French",       "flag": "fr"},
    "german":       {"label": "German",       "demonym": "German",       "flag": "de"},
    "japanese":     {"label": "Japanese",     "demonym": "Japanese",     "flag": "jp"},
    "australian":   {"label": "Australian",   "demonym": "Australian",   "flag": "au"},
    "indian":       {"label": "Indian",       "demonym": "Indian",       "flag": "in"},
    "chinese":      {"label": "Chinese",      "demonym": "Chinese",      "flag": "cn"},
    "russian":      {"label": "Russian",      "demonym": "Russian",      "flag": "ru"},
    "brazilian":    {"label": "Brazilian",    "demonym": "Brazilian",    "flag": "br"},
    "mexican":      {"label": "Mexican",      "demonym": "Mexican",      "flag": "mx"},
    "south-african":{"label": "South African","demonym": "South African","flag": "za"},
    "nigerian":     {"label": "Nigerian",     "demonym": "Nigerian",     "flag": "ng"},
    "korean":       {"label": "Korean",       "demonym": "South Korean", "flag": "kr"},
    "singaporean":  {"label": "Singaporean",  "demonym": "Singaporean",  "flag": "sg"},
    "indonesian":   {"label": "Indonesian",   "demonym": "Indonesian",   "flag": "id"},
    "philippine":   {"label": "Philippine",   "demonym": "Filipino",     "flag": "ph"},
    "turkish":      {"label": "Turkish",      "demonym": "Turkish",      "flag": "tr"},
    "argentinian":  {"label": "Argentinian",  "demonym": "Argentinian",  "flag": "ar"},
}

# ---------------------------------------------------------------------------
# Taiwan visa status per nationality
# ---------------------------------------------------------------------------
TAIWAN_VISA_FREE_90 = {"us","uk","canadian","french","german","japanese","australian",
                        "korean","singaporean","brazilian","mexican","argentinian","russian"}
TAIWAN_VISA_FREE_14  = {"philippine","indonesian"}
TAIWAN_VISA_REQUIRED = {"indian","chinese","nigerian","south-african","turkish"}


def taiwan_status(nat_key):
    if nat_key in TAIWAN_VISA_FREE_90:
        return {
            "badge": '<span style="color:green;font-weight:600;">Visa-Free — 90 Days</span>',
            "type": "Visa-Free",
            "fee": "Free",
            "stay": "90 days",
            "processing": "N/A",
            "apply_at": "No visa needed",
        }
    elif nat_key in TAIWAN_VISA_FREE_14:
        return {
            "badge": '<span style="color:green;font-weight:600;">Visa-Free — 14 Days</span>',
            "type": "Visa-Free (14 days)",
            "fee": "Free",
            "stay": "14 days",
            "processing": "N/A",
            "apply_at": "No visa needed",
        }
    else:
        return {
            "badge": '<span style="color:red;font-weight:600;">Visa Required</span>',
            "type": "Tourist Visa / eVisa",
            "fee": "USD 31 (single) / USD 62 (multiple)",
            "stay": "30 days per entry",
            "processing": "3 business days",
            "apply_at": "boca.gov.tw",
        }


def taiwan_body(nat_key, nat_info, status):
    label = nat_info["label"]
    demonym = nat_info["demonym"]

    if nat_key in TAIWAN_VISA_FREE_90:
        return f"""
<h2>Taiwan Visa-Free Access for {label} Citizens</h2>
<p>{demonym} passport holders enjoy <strong>visa-free entry to Taiwan for up to 90 days</strong> per visit. No prior visa application is required — simply present your valid passport at immigration on arrival at Taoyuan (TPE), Songshan (TSA), or Kaohsiung (KHH) international airports.</p>

<h2>Key Details</h2>
<ul>
  <li>Entry: Visa-free</li>
  <li>Maximum stay: <strong>90 days</strong> per visit</li>
  <li>Purpose: Tourism, business, transit, family visits</li>
  <li>Extension: Apply at the National Immigration Agency (NIA) for up to 30-day extensions</li>
  <li>Passport validity: Must be valid for the full duration of your stay</li>
</ul>

<h2>Tips for {label} Travellers</h2>
<ul>
  <li>No prior application or approval needed — just fly and go.</li>
  <li>Keep proof of onward/return flights and accommodation at immigration.</li>
  <li>Working while on visa-free status is not permitted without a separate work permit.</li>
  <li>If you wish to stay longer, apply at NIA before your 90 days expire.</li>
</ul>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://www.boca.gov.tw" target="_blank" rel="noopener">boca.gov.tw — Bureau of Consular Affairs (BOCA)</a></li>
  <li><a href="https://www.immigration.gov.tw" target="_blank" rel="noopener">immigration.gov.tw — National Immigration Agency (NIA)</a></li>
</ul>
"""
    elif nat_key in TAIWAN_VISA_FREE_14:
        return f"""
<h2>Taiwan Visa-Free Access for {label} Citizens</h2>
<p>{demonym} passport holders are eligible for <strong>visa-free entry to Taiwan for up to 14 days</strong>. No visa application is required before departure — present your valid passport on arrival.</p>

<h2>Key Details</h2>
<ul>
  <li>Entry: Visa-free</li>
  <li>Maximum stay: <strong>14 days</strong> per visit</li>
  <li>Purpose: Tourism, transit, short business visits</li>
  <li>Extension: Not available under the 14-day visa-free program; must apply for a separate visa if a longer stay is needed</li>
  <li>Passport validity: Must cover the full intended period of stay</li>
</ul>

<h2>Applying for a Longer Stay</h2>
<p>If you plan to stay more than 14 days, you must apply for a Taiwan eVisa or tourist visa before travel through the Bureau of Consular Affairs (BOCA) portal at <a href="https://visawebapp.boca.gov.tw" target="_blank" rel="noopener">visawebapp.boca.gov.tw</a>.</p>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://www.boca.gov.tw" target="_blank" rel="noopener">boca.gov.tw — Bureau of Consular Affairs (BOCA)</a></li>
  <li><a href="https://www.immigration.gov.tw" target="_blank" rel="noopener">immigration.gov.tw — National Immigration Agency (NIA)</a></li>
</ul>
"""
    else:
        # Visa required
        china_note = ""
        if nat_key == "chinese":
            china_note = """
<div class="alert alert-warning mt-3">
  <strong>Important — PRC Citizens:</strong> Mainland Chinese passport holders are subject to special restrictions and do not use the standard BOCA visa application process. Entry is governed by the <em>Act Governing Relations Between the People of the Taiwan Area and the Mainland Area</em>. Mainland Chinese citizens typically require a special Entry Permit issued through official cross-strait channels. Individual travel permits (自由行) from eligible mainland cities may allow tourism visits. Consult the Straits Exchange Foundation (SEF) or Taiwan's Mainland Affairs Council (MAC) for current rules.
</div>"""
        return f"""
<h2>Taiwan Visa Requirements for {label} Citizens</h2>
<p>{demonym} passport holders <strong>require a visa to enter Taiwan</strong>. You must obtain a visa or eVisa before travelling. Applications are submitted through Taiwan's Bureau of Consular Affairs (BOCA).{china_note}</p>

<h2>How to Apply for a Taiwan Visa / eVisa</h2>
<ol>
  <li>Visit the BOCA eVisa portal at <a href="https://visawebapp.boca.gov.tw" target="_blank" rel="noopener">visawebapp.boca.gov.tw</a>.</li>
  <li>Create an account and select the appropriate visa category (Tourist, Business, etc.).</li>
  <li>Upload a digital passport photo and a scanned copy of your passport data page.</li>
  <li>Provide your travel itinerary and accommodation details.</li>
  <li>Pay the visa fee: <strong>USD 31 (single entry)</strong> or <strong>USD 62 (multiple entry)</strong>.</li>
  <li>Await approval — typically <strong>3 business days</strong>.</li>
  <li>Receive your eVisa by email; print it or save it digitally to present on arrival.</li>
</ol>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport (at least 6 months validity beyond intended stay)</li>
  <li>Digital passport photo (white background)</li>
  <li>Return or onward flight ticket</li>
  <li>Proof of accommodation (hotel booking or host invitation)</li>
  <li>Bank statements showing sufficient funds</li>
  <li>Travel insurance (recommended)</li>
</ul>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://visawebapp.boca.gov.tw" target="_blank" rel="noopener">visawebapp.boca.gov.tw — Taiwan eVisa Application</a></li>
  <li><a href="https://www.boca.gov.tw" target="_blank" rel="noopener">boca.gov.tw — Bureau of Consular Affairs (BOCA)</a></li>
  <li><a href="https://www.immigration.gov.tw" target="_blank" rel="noopener">immigration.gov.tw — National Immigration Agency (NIA)</a></li>
</ul>
"""


# ---------------------------------------------------------------------------
# Sri Lanka visa status per nationality
# ---------------------------------------------------------------------------
SL_EVISA_USD20 = {"us","uk","canadian","french","german","japanese","australian","korean",
                  "singaporean","russian","brazilian","mexican","argentinian","turkish",
                  "south-african","nigerian"}
SL_VISA_FREE   = {"indian"}  # SAARC — 30 days free
SL_EVISA_OA    = {"indonesian","philippine","chinese"}  # eVisa or on arrival


def srilanka_status(nat_key):
    if nat_key in SL_VISA_FREE:
        return {
            "badge": '<span style="color:green;font-weight:600;">Visa-Free — 30 Days (SAARC)</span>',
            "type": "Visa-Free (SAARC)",
            "fee": "Free",
            "stay": "30 days",
            "processing": "N/A",
            "apply_at": "No visa needed",
        }
    elif nat_key in SL_EVISA_OA:
        return {
            "badge": '<span style="color:#e67e00;font-weight:600;">eVisa or On Arrival</span>',
            "type": "eVisa / Visa on Arrival",
            "fee": "USD 20–35",
            "stay": "30 days (double entry)",
            "processing": "24–72 hours (eVisa)",
            "apply_at": "eta.gov.lk",
        }
    else:
        return {
            "badge": '<span style="color:#e67e00;font-weight:600;">eVisa Required — USD 20</span>',
            "type": "Electronic Travel Authorization (ETA)",
            "fee": "USD 20 (tourism) / USD 35 (business)",
            "stay": "30 days, double entry",
            "processing": "24–72 hours",
            "apply_at": "eta.gov.lk",
        }


def srilanka_body(nat_key, nat_info, status):
    label = nat_info["label"]
    demonym = nat_info["demonym"]

    if nat_key in SL_VISA_FREE:
        return f"""
<h2>Sri Lanka Visa-Free Entry for {label} Citizens</h2>
<p>{demonym} passport holders benefit from <strong>visa-free entry to Sri Lanka for up to 30 days</strong> under the SAARC (South Asian Association for Regional Cooperation) agreement. No advance visa or ETA application is required.</p>

<h2>Key Details</h2>
<ul>
  <li>Entry: Visa-free (SAARC exemption)</li>
  <li>Maximum stay: <strong>30 days</strong> per visit</li>
  <li>Purpose: Tourism, business, family visits</li>
  <li>Extension: Apply at the Department of Immigration &amp; Emigration in Sri Lanka to extend your stay</li>
  <li>Passport validity: Must be valid for at least 6 months beyond your intended stay</li>
</ul>

<h2>Tips for {demonym} Travellers</h2>
<ul>
  <li>Carry proof of onward travel and sufficient funds.</li>
  <li>Working while on visa-free entry is not permitted without a separate work permit.</li>
  <li>To stay beyond 30 days, apply at the Department of Immigration &amp; Emigration, Colombo.</li>
</ul>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://www.immigration.gov.lk" target="_blank" rel="noopener">immigration.gov.lk — Sri Lanka Dept. of Immigration &amp; Emigration</a></li>
  <li><a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk — Sri Lanka ETA Portal</a></li>
</ul>
"""
    elif nat_key in SL_EVISA_OA:
        return f"""
<h2>Sri Lanka eVisa or Visa on Arrival for {label} Citizens</h2>
<p>{demonym} passport holders can enter Sri Lanka either by applying for an <strong>Electronic Travel Authorization (ETA)</strong> in advance or by obtaining a <strong>visa on arrival</strong> at the airport. Applying online in advance via <a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk</a> is strongly recommended to avoid delays.</p>

<h2>Key Details</h2>
<ul>
  <li>Visa type: ETA (recommended) or Visa on Arrival</li>
  <li>Fee: <strong>USD 20</strong> (tourism ETA) / <strong>USD 35</strong> (business ETA)</li>
  <li>Stay: <strong>30 days, double entry</strong></li>
  <li>Processing: <strong>24–72 hours</strong> for online ETA; immediate on arrival (subject to queue)</li>
  <li>Validity: 6 months from date of issue</li>
</ul>

<h2>How to Apply for the Sri Lanka ETA</h2>
<ol>
  <li>Go to <a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk</a> — the official Sri Lanka ETA portal.</li>
  <li>Select "Tourist" or "Business" ETA.</li>
  <li>Fill in your passport details and travel information.</li>
  <li>Pay USD 20 (tourism) or USD 35 (business) by credit/debit card.</li>
  <li>Receive ETA approval by email within 24–72 hours.</li>
  <li>Print or save the ETA approval; present at immigration on arrival.</li>
</ol>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport (6+ months validity)</li>
  <li>ETA approval email (or apply on arrival)</li>
  <li>Return or onward ticket</li>
  <li>Proof of accommodation</li>
  <li>Sufficient funds for the duration of stay</li>
</ul>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk — Sri Lanka Electronic Travel Authorization</a></li>
  <li><a href="https://www.immigration.gov.lk" target="_blank" rel="noopener">immigration.gov.lk — Dept. of Immigration &amp; Emigration</a></li>
</ul>
"""
    else:
        # Standard eVisa USD 20
        return f"""
<h2>Sri Lanka eVisa (ETA) for {label} Citizens</h2>
<p>{demonym} passport holders must obtain a Sri Lanka <strong>Electronic Travel Authorization (ETA)</strong> before arrival. The ETA is applied for online at <a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk</a> and costs <strong>USD 20</strong> for tourism or <strong>USD 35</strong> for business. Processing typically takes <strong>24–72 hours</strong>.</p>

<h2>Key Details</h2>
<ul>
  <li>Visa type: Electronic Travel Authorization (ETA)</li>
  <li>Fee: <strong>USD 20</strong> (tourism) / <strong>USD 35</strong> (business)</li>
  <li>Stay: <strong>30 days, double entry</strong></li>
  <li>Processing: <strong>24–72 hours</strong></li>
  <li>Validity: 6 months from date of issue</li>
  <li>Extension: Possible at the Department of Immigration &amp; Emigration in Sri Lanka (up to 6 months total)</li>
</ul>

<h2>How to Apply</h2>
<ol>
  <li>Visit <a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk</a> — Sri Lanka's official ETA portal.</li>
  <li>Select "Individual" and then "Tourist" or "Business" as the purpose of visit.</li>
  <li>Enter your passport details, travel dates, and accommodation information.</li>
  <li>Pay the fee (USD 20 / USD 35) by credit or debit card.</li>
  <li>Receive your ETA approval by email within 24–72 hours.</li>
  <li>Print the ETA confirmation or save it on your phone to present at the airport.</li>
</ol>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport (minimum 6 months validity beyond intended stay)</li>
  <li>ETA approval confirmation (print or digital)</li>
  <li>Return or onward flight ticket</li>
  <li>Proof of accommodation (hotel booking or host invitation)</li>
  <li>Sufficient funds: approx. USD 50/day recommended</li>
  <li>Travel insurance (recommended)</li>
</ul>

<h2>Official Resources</h2>
<ul>
  <li><a href="https://www.eta.gov.lk" target="_blank" rel="noopener">eta.gov.lk — Sri Lanka ETA Application</a></li>
  <li><a href="https://www.immigration.gov.lk" target="_blank" rel="noopener">immigration.gov.lk — Dept. of Immigration &amp; Emigration</a></li>
</ul>
"""


# ---------------------------------------------------------------------------
# HTML template builder
# ---------------------------------------------------------------------------
NAV_TEMPLATE = """\
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
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Fran&#231;ais</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Espa&#241;ol</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Portugu&#234;s</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

FOOTER_TEMPLATE = """\
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


def build_html(slug, title, meta_desc, canonical_url, flag_code, h1,
               status_badge, visa_type, fee, stay, processing, apply_at,
               dest_label, body_html, faq_json, related_html):
    nav = NAV_TEMPLATE.replace("{slug}", slug)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical_url}"/>
    <link rel="alternate" hreflang="en" href="{canonical_url}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical_url}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">{faq_json}</script>
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

<h1><span class="fi fi-{flag_code} mr-2"></span>{h1}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &#8212; {dest_label} for {h1.split(' Visa')[0].split(' for')[0]} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Status</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
</tbody>
</table>

{body_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &#8212; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Visa rules change frequently &#8212; always verify current requirements on the official government portal before booking travel.</p>
</div>

{related_html}

</article>
</div>
</section>

{FOOTER_TEMPLATE}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Taiwan FAQ builder
# ---------------------------------------------------------------------------
def taiwan_faq(nat_key, nat_info, status):
    label = nat_info["label"]
    demonym = nat_info["demonym"]
    if nat_key in TAIWAN_VISA_FREE_90:
        q1a = f"{demonym} passport holders enjoy visa-free entry to Taiwan for up to 90 days. No advance application is required."
        q2a = "Simply present your valid passport at immigration on arrival at Taoyuan (TPE), Songshan (TSA), or Kaohsiung (KHH) airports."
        q3a = "The 90-day visa-free period can be extended at the National Immigration Agency (NIA). Maximum extensions vary but the total stay can reach 180 days in some cases."
    elif nat_key in TAIWAN_VISA_FREE_14:
        q1a = f"{demonym} passport holders enjoy visa-free entry to Taiwan for up to 14 days per visit. No advance visa is needed."
        q2a = "Present your valid passport at the immigration counter on arrival. The officer will stamp you in for 14 days."
        q3a = "The 14-day visa-free stay is generally not extendable. If you need longer, apply for a Taiwan eVisa before travel at visawebapp.boca.gov.tw."
    else:
        q1a = f"Yes. {demonym} passport holders must obtain a visa or eVisa before travelling to Taiwan. Apply at visawebapp.boca.gov.tw."
        q2a = "Apply online at visawebapp.boca.gov.tw. Pay USD 31 (single entry) or USD 62 (multiple entry). Processing takes approximately 3 business days."
        q3a = "The Taiwan tourist eVisa permits a stay of up to 30 days per entry. Extensions may be applied for at the National Immigration Agency (NIA) once in Taiwan."

    import json
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f"Do {label} citizens need a visa for Taiwan?",
             "acceptedAnswer": {"@type": "Answer", "text": q1a}},
            {"@type": "Question", "name": f"How do {label} citizens enter Taiwan?",
             "acceptedAnswer": {"@type": "Answer", "text": q2a}},
            {"@type": "Question", "name": f"How long can {label} citizens stay in Taiwan?",
             "acceptedAnswer": {"@type": "Answer", "text": q3a}},
        ]
    }
    return json.dumps(faq)


# ---------------------------------------------------------------------------
# Sri Lanka FAQ builder
# ---------------------------------------------------------------------------
def srilanka_faq(nat_key, nat_info, status):
    label = nat_info["label"]
    demonym = nat_info["demonym"]
    if nat_key in SL_VISA_FREE:
        q1a = f"{demonym} citizens do not need a visa for Sri Lanka. Under the SAARC agreement, Indian nationals can enter visa-free for up to 30 days."
        q2a = "Simply present your valid Indian passport at immigration on arrival. No prior ETA or visa application is required."
        q3a = "The initial visa-free period is 30 days. Extensions can be applied for at the Department of Immigration and Emigration in Sri Lanka."
    elif nat_key in SL_EVISA_OA:
        q1a = f"{demonym} citizens can obtain a Sri Lanka ETA online or a visa on arrival. Applying in advance at eta.gov.lk is strongly recommended."
        q2a = "Apply online at eta.gov.lk. Pay USD 20 (tourism) and receive approval in 24–72 hours. Alternatively, obtain a visa on arrival at the airport (queues possible)."
        q3a = "The ETA permits a stay of 30 days with double entry. It can be extended at the Department of Immigration and Emigration for up to 6 months total."
    else:
        q1a = f"{demonym} citizens must obtain a Sri Lanka Electronic Travel Authorization (ETA) before travel. Apply at eta.gov.lk for USD 20 (tourism)."
        q2a = "Apply online at eta.gov.lk. Select the visa type, enter passport and travel details, pay USD 20, and receive approval within 24–72 hours."
        q3a = "The ETA allows a 30-day stay with double entry. Extensions can be granted at the Department of Immigration and Emigration in Sri Lanka for up to 6 months total."

    import json
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f"Do {label} citizens need a visa for Sri Lanka?",
             "acceptedAnswer": {"@type": "Answer", "text": q1a}},
            {"@type": "Question", "name": f"How do {label} citizens apply for a Sri Lanka visa?",
             "acceptedAnswer": {"@type": "Answer", "text": q2a}},
            {"@type": "Question", "name": f"How long can {label} citizens stay in Sri Lanka?",
             "acceptedAnswer": {"@type": "Answer", "text": q3a}},
        ]
    }
    return json.dumps(faq)


# ---------------------------------------------------------------------------
# Related guides builders
# ---------------------------------------------------------------------------
def taiwan_related(nat_key):
    return """<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-taiwan.html">Taiwan Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="taiwan-visa-requirements.html">Taiwan Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="taiwan-visa-fees.html">Taiwan Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="taiwan-visa-processing-time.html">Taiwan Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-japan.html">Japan Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-south-korea.html">South Korea Visa Guide</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#8594;</a>
</div>"""


def srilanka_related(nat_key):
    return """<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-sri-lanka.html">Sri Lanka Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="sri-lanka-visa-requirements.html">Sri Lanka Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="sri-lanka-visa-fees.html">Sri Lanka Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="sri-lanka-visa-processing-time.html">Sri Lanka Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-india.html">India Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-maldives.html">Maldives Visa Guide</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#8594;</a>
</div>"""


# ---------------------------------------------------------------------------
# Main generation loop
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    for nat_key, nat_info in NATIONALITIES.items():
        label = nat_info["label"]
        flag  = nat_info["flag"]
        demonym = nat_info["demonym"]

        # ---- TAIWAN ----
        tw_status = taiwan_status(nat_key)
        tw_slug   = f"taiwan-visa-for-{nat_key}-citizens"
        tw_title  = f"Taiwan Visa for {label} Citizens 2026"
        tw_desc   = (
            f"{demonym} passport holders visiting Taiwan in 2026: "
            f"{tw_status['type']}, {tw_status['fee']}, {tw_status['stay']}. "
            f"Updated March 2026."
        )
        tw_canon  = f"https://www.evisa-card.com/en/{tw_slug}"
        tw_h1     = f"Taiwan Visa for {label} Citizens 2026"
        tw_body   = taiwan_body(nat_key, nat_info, tw_status)
        tw_faq    = taiwan_faq(nat_key, nat_info, tw_status)
        tw_rel    = taiwan_related(nat_key)

        tw_html = build_html(
            slug=tw_slug, title=tw_title, meta_desc=tw_desc,
            canonical_url=tw_canon, flag_code=flag, h1=tw_h1,
            status_badge=tw_status["badge"],
            visa_type=tw_status["type"], fee=tw_status["fee"],
            stay=tw_status["stay"], processing=tw_status["processing"],
            apply_at=tw_status["apply_at"],
            dest_label="Taiwan",
            body_html=tw_body, faq_json=tw_faq, related_html=tw_rel,
        )
        tw_path = os.path.join(OUTPUT_DIR, f"{tw_slug}.html")
        with open(tw_path, "w", encoding="utf-8") as f:
            f.write(tw_html)
        created.append(tw_slug + ".html")

        # ---- SRI LANKA ----
        sl_status = srilanka_status(nat_key)
        sl_slug   = f"sri-lanka-visa-for-{nat_key}-citizens"
        sl_title  = f"Sri Lanka Visa for {label} Citizens 2026"
        sl_desc   = (
            f"{demonym} passport holders visiting Sri Lanka in 2026: "
            f"{sl_status['type']}, {sl_status['fee']}, {sl_status['stay']}. "
            f"Updated March 2026."
        )
        sl_canon  = f"https://www.evisa-card.com/en/{sl_slug}"
        sl_h1     = f"Sri Lanka Visa for {label} Citizens 2026"
        sl_body   = srilanka_body(nat_key, nat_info, sl_status)
        sl_faq    = srilanka_faq(nat_key, nat_info, sl_status)
        sl_rel    = srilanka_related(nat_key)

        sl_html = build_html(
            slug=sl_slug, title=sl_title, meta_desc=sl_desc,
            canonical_url=sl_canon, flag_code=flag, h1=sl_h1,
            status_badge=sl_status["badge"],
            visa_type=sl_status["type"], fee=sl_status["fee"],
            stay=sl_status["stay"], processing=sl_status["processing"],
            apply_at=sl_status["apply_at"],
            dest_label="Sri Lanka",
            body_html=sl_body, faq_json=sl_faq, related_html=sl_rel,
        )
        sl_path = os.path.join(OUTPUT_DIR, f"{sl_slug}.html")
        with open(sl_path, "w", encoding="utf-8") as f:
            f.write(sl_html)
        created.append(sl_slug + ".html")

    print(f"\nGenerated {len(created)} files in {OUTPUT_DIR}:")
    for name in created:
        print(f"  {name}")


if __name__ == "__main__":
    main()
