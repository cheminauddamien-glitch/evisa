"""
gen_nat_uae_turkey.py
Generates 40 HTML files:
  - uae-visa-for-{nat}-citizens.html   (20 files)
  - turkey-visa-for-{nat}-citizens.html (20 files)
in www/en/ using the Pacific/Bootstrap 4 site structure.
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATS = [
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "indian", "chinese", "russian", "brazilian", "mexican", "south-african",
    "nigerian", "korean", "singaporean", "indonesian", "philippine",
    "turkish", "argentinian",
]

# Pretty labels
NAT_LABEL = {
    "us": "US", "uk": "UK", "canadian": "Canadian", "french": "French",
    "german": "German", "japanese": "Japanese", "australian": "Australian",
    "indian": "Indian", "chinese": "Chinese", "russian": "Russian",
    "brazilian": "Brazilian", "mexican": "Mexican",
    "south-african": "South African", "nigerian": "Nigerian",
    "korean": "South Korean", "singaporean": "Singaporean",
    "indonesian": "Indonesian", "philippine": "Philippine",
    "turkish": "Turkish", "argentinian": "Argentinian",
}

# Flag icon country codes (flag-icons library)
FLAG_CODE = {
    "us": "us", "uk": "gb", "canadian": "ca", "french": "fr",
    "german": "de", "japanese": "jp", "australian": "au",
    "indian": "in", "chinese": "cn", "russian": "ru",
    "brazilian": "br", "mexican": "mx", "south-african": "za",
    "nigerian": "ng", "korean": "kr", "singaporean": "sg",
    "indonesian": "id", "philippine": "ph", "turkish": "tr",
    "argentinian": "ar",
}

# ---------------------------------------------------------------------------
# UAE visa status
# ---------------------------------------------------------------------------
UAE_VISA_FREE_90 = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian", "russian",
}
UAE_EVISA = {
    "indian", "chinese", "indonesian", "philippine",
    "south-african", "nigerian", "turkish",
}
# fee range for UAE eVisa
UAE_EVISA_FEE = "AED 250–350"
UAE_EVISA_URL = "https://icp.gov.ae"

# ---------------------------------------------------------------------------
# Turkey visa status
# ---------------------------------------------------------------------------
TURKEY_EVISA = {
    "us": "USD 50", "uk": "USD 50", "canadian": "USD 60",
    "australian": "USD 60", "japanese": "USD 50", "korean": "USD 50",
    "singaporean": "USD 50", "brazilian": "USD 50", "mexican": "USD 50",
    "argentinian": "USD 50", "russian": "USD 50", "indonesian": "USD 60",
    "philippine": "USD 60", "south-african": "USD 60", "chinese": "USD 60",
    "nigerian": "USD 50",
}
TURKEY_VISA_FREE = {"french", "german", "indian"}
TURKEY_DOMESTIC = {"turkish"}
TURKEY_EVISA_URL = "https://www.evisa.gov.tr"


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def cap(s):
    return s.replace("-", " ").title()


def head(title, desc, slug, flag_nat):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


def navbar(slug):
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
                        <a class="dropdown-item active" href="/en/{slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
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
# UAE page generator
# ---------------------------------------------------------------------------

def make_uae_page(nat):
    label = NAT_LABEL[nat]
    flag = FLAG_CODE[nat]
    slug = f"uae-visa-for-{nat}-citizens"
    title = f"UAE Visa for {label} Citizens 2026"

    if nat in UAE_VISA_FREE_90:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 90 Days</span>'
        status_type = "Visa-Free"
        fee_cell = "Free"
        stay_cell = "90 days per visit"
        apply_cell = "No action required — arrive and receive entry stamp"
        desc = (f"{label} passport holders can enter the UAE visa-free for up to 90 days. "
                f"No prior application needed. Complete guide updated March 2026.")
        body_content = f"""<h2>Do {label} Citizens Need a Visa for the UAE?</h2>
<p>{label} passport holders enjoy <strong>visa-free entry</strong> to the United Arab Emirates for up to <strong>90 days</strong> per visit. No prior application or fee is required — you will receive an entry stamp upon arrival at any UAE port of entry.</p>

<h2>Entry Requirements at a Glance</h2>
<ul>
<li>Valid passport (valid for at least 6 months beyond your intended stay)</li>
<li>Return or onward travel ticket</li>
<li>Proof of accommodation (hotel booking or host invitation)</li>
<li>Sufficient funds for the duration of stay</li>
</ul>

<h2>Extension &amp; Long Stays</h2>
<p>If you wish to stay beyond 90 days, you may apply for an extension through the <strong>UAE Federal Authority for Identity, Citizenship, Customs &amp; Port Security (ICP)</strong> at <a href="https://icp.gov.ae" target="_blank" rel="noopener">icp.gov.ae</a>, or exit and re-enter (subject to immigration officer discretion).</p>

<h2>Permitted Activities</h2>
<ul>
<li>Tourism and leisure</li>
<li>Visiting family or friends</li>
<li>Short-term business meetings (not employment)</li>
<li>Transit through UAE airports</li>
</ul>"""

    elif nat in UAE_EVISA:
        status_badge = f'<span style="color:orange;font-weight:600;">eVisa Required — {UAE_EVISA_FEE}</span>'
        status_type = "eVisa"
        fee_cell = UAE_EVISA_FEE
        stay_cell = "30–90 days (as approved)"
        apply_cell = f'<a href="{UAE_EVISA_URL}" target="_blank" rel="noopener">icp.gov.ae</a>'
        desc = (f"{label} passport holders need a UAE eVisa ({UAE_EVISA_FEE}) before travel. "
                f"Apply online at icp.gov.ae. Complete guide updated March 2026.")
        body_content = f"""<h2>Do {label} Citizens Need a Visa for the UAE?</h2>
<p>Yes — {label} passport holders must obtain a <strong>UAE eVisa</strong> before travelling to the United Arab Emirates. Applications are processed online through the <strong>UAE ICP portal</strong> at <a href="{UAE_EVISA_URL}" target="_blank" rel="noopener">icp.gov.ae</a>. Fees range from <strong>{UAE_EVISA_FEE}</strong> depending on visa type and duration.</p>

<h2>UAE eVisa Types for {label} Citizens</h2>
<ul>
<li><strong>Tourist eVisa (30 days, single entry)</strong> — most common for short visits</li>
<li><strong>Tourist eVisa (60 days, single entry)</strong> — for longer stays</li>
<li><strong>Multi-entry eVisa (90 days)</strong> — for multiple short visits within 12 months</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Visit <a href="{UAE_EVISA_URL}" target="_blank" rel="noopener">icp.gov.ae</a> and select "eVisa Services".</li>
<li>Complete the online application form with your passport details and travel information.</li>
<li>Upload a passport-size photo and a scanned copy of your passport bio page.</li>
<li>Pay the fee ({UAE_EVISA_FEE}) by credit/debit card.</li>
<li>Receive the eVisa by email — processing typically takes 3–5 business days.</li>
<li>Print the eVisa or save it to your device and present it on arrival.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Recent passport-size photograph</li>
<li>Return or onward flight ticket</li>
<li>Hotel booking or proof of accommodation</li>
<li>Credit/debit card for the eVisa fee</li>
</ul>"""
    else:
        # fallback — should not occur with current nat list
        status_badge = '<span style="color:grey;">Check Requirements</span>'
        status_type = "Check Requirements"
        fee_cell = "Varies"
        stay_cell = "Varies"
        apply_cell = f'<a href="{UAE_EVISA_URL}" target="_blank" rel="noopener">icp.gov.ae</a>'
        desc = f"UAE visa requirements for {label} citizens. Updated March 2026."
        body_content = f"<p>Please check current UAE visa requirements for {label} citizens at <a href='{UAE_EVISA_URL}' target='_blank' rel='noopener'>icp.gov.ae</a>.</p>"

    faq_q1 = f"Do {label} citizens need a visa for the UAE?"
    if nat in UAE_VISA_FREE_90:
        faq_a1 = f"No. {label} passport holders can enter the UAE visa-free for up to 90 days without a prior application."
        faq_q2 = f"How long can {label} citizens stay in the UAE without a visa?"
        faq_a2 = "Up to 90 days per visit under the visa-free policy. Extensions may be applied for through the ICP portal."
    else:
        faq_a1 = f"Yes. {label} passport holders must apply for a UAE eVisa at icp.gov.ae before travel. Fees are {UAE_EVISA_FEE}."
        faq_q2 = f"How much does the UAE eVisa cost for {label} citizens?"
        faq_a2 = f"The UAE eVisa fee ranges from {UAE_EVISA_FEE} depending on visa type and duration of stay."

    faq_json = f"""    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"{faq_q1}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a1}"}}}},
      {{"@type":"Question","name":"{faq_q2}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a2}"}}}}
    ]}}"""

    page = f"""{head(title, desc, slug, flag)}
    <script type="application/ld+json">
{faq_json}
    </script>
{navbar(slug)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-ae mr-2"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — UAE for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{status_type}</td></tr>
<tr><th>Fee</th><td>{fee_cell}</td></tr>
<tr><th>Max Stay</th><td>{stay_cell}</td></tr>
<tr><th>Processing</th><td>{'Immediate on arrival' if nat in UAE_VISA_FREE_90 else '3–5 business days'}</td></tr>
<tr><th>Apply At</th><td>{apply_cell if nat in UAE_EVISA else 'N/A — no advance application needed'}</td></tr>
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current entry requirements at <a href="https://icp.gov.ae" target="_blank" rel="noopener">icp.gov.ae</a> or your nearest UAE embassy before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="turkey-visa-for-{nat}-citizens.html"><span class="fi fi-tr mr-1"></span>Turkey Visa for {label} Citizens</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="australia-visa-for-{nat}-citizens.html">Australia Visa for {label} Citizens</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="canada-visa-for-{nat}-citizens.html">Canada Visa for {label} Citizens</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>

</article>
</div>
</section>

{FOOTER}"""
    return page


# ---------------------------------------------------------------------------
# Turkey page generator
# ---------------------------------------------------------------------------

def make_turkey_page(nat):
    label = NAT_LABEL[nat]
    flag = FLAG_CODE[nat]
    slug = f"turkey-visa-for-{nat}-citizens"
    title = f"Turkey Visa for {label} Citizens 2026"

    if nat in TURKEY_DOMESTIC:
        # Turkish citizens — domestic page
        status_badge = '<span style="color:green;font-weight:600;">No Visa Required — Domestic</span>'
        status_type = "Domestic (no visa)"
        fee_cell = "N/A"
        stay_cell = "Unlimited (own country)"
        apply_cell = "N/A"
        desc = (f"Turkish citizens do not need a visa to enter Turkey — it is their home country. "
                f"Travel information for Turkish nationals updated March 2026.")
        body_content = """<h2>Turkish Citizens Travelling to Turkey</h2>
<p>Turkey is the home country for Turkish citizens. No visa, eVisa, or prior travel authorisation is required to enter Turkey with a valid Turkish passport or national ID card.</p>

<h2>Travel Documents Accepted</h2>
<ul>
<li>Valid Turkish passport (biometric recommended)</li>
<li>Turkish National ID card (for land border crossings within certain arrangements)</li>
</ul>

<h2>Re-entry After Abroad</h2>
<p>Turkish citizens have the right of return guaranteed by the Turkish constitution. Present your Turkish passport at the border — no additional documents are required for entry.</p>"""

    elif nat in TURKEY_VISA_FREE:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 90 Days</span>'
        status_type = "Visa-Free"
        fee_cell = "Free"
        stay_cell = "90 days within any 180-day period"
        apply_cell = "No advance application required"
        desc = (f"{label} passport holders can visit Turkey visa-free for up to 90 days. "
                f"No eVisa or prior application needed. Complete guide updated March 2026.")
        body_content = f"""<h2>Do {label} Citizens Need a Visa for Turkey?</h2>
<p>{label} passport holders enjoy <strong>visa-free access</strong> to Turkey for tourism and short stays of up to <strong>90 days within any 180-day period</strong>. No eVisa or prior application is required — simply present your valid passport on arrival.</p>

<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (at least 6 months validity beyond your intended stay)</li>
<li>Return or onward travel ticket</li>
<li>Proof of sufficient funds</li>
<li>Hotel booking or invitation letter (if requested at border)</li>
</ul>

<h2>Permitted Activities</h2>
<ul>
<li>Tourism and leisure</li>
<li>Visiting family or friends</li>
<li>Short business meetings (not employment)</li>
<li>Transit</li>
</ul>

<h2>Exceeding 90 Days</h2>
<p>If you plan to stay longer than 90 days, you must apply for a residence permit at the local Provincial Directorate of Migration Management before your visa-free period expires.</p>"""

    elif nat in TURKEY_EVISA:
        fee = TURKEY_EVISA[nat]
        status_badge = f'<span style="color:orange;font-weight:600;">eVisa Required — {fee}</span>'
        status_type = "eVisa"
        fee_cell = fee
        stay_cell = "90 days within 180 days (single or multiple entry)"
        apply_cell = f'<a href="{TURKEY_EVISA_URL}" target="_blank" rel="noopener">evisa.gov.tr</a>'
        desc = (f"{label} passport holders need a Turkey eVisa ({fee}) to enter Turkey. "
                f"Apply online at evisa.gov.tr in minutes. Complete guide updated March 2026.")
        body_content = f"""<h2>Do {label} Citizens Need a Visa for Turkey?</h2>
<p>Yes — {label} passport holders must obtain a <strong>Turkish eVisa</strong> before travel. The eVisa is available entirely online at <a href="{TURKEY_EVISA_URL}" target="_blank" rel="noopener">evisa.gov.tr</a>, the official Turkish government portal. The fee is <strong>{fee}</strong>.</p>

<h2>Turkey eVisa Key Details</h2>
<ul>
<li>Fee: <strong>{fee}</strong></li>
<li>Validity: 180 days from issue date</li>
<li>Stay: Up to 90 days per entry (within the 180-day window)</li>
<li>Entry: Single or multiple entry (depends on nationality)</li>
<li>Processing: Usually 24 hours or less</li>
<li>Permitted activities: Tourism, business, transit</li>
</ul>

<h2>How to Apply for the Turkey eVisa</h2>
<ol>
<li>Go to <a href="{TURKEY_EVISA_URL}" target="_blank" rel="noopener">evisa.gov.tr</a> — the only official government portal.</li>
<li>Select your nationality and intended date of entry.</li>
<li>Enter your passport details and travel dates.</li>
<li>Pay the fee of <strong>{fee}</strong> by credit/debit card.</li>
<li>Receive the eVisa by email — print it or save a digital copy.</li>
<li>Present the eVisa along with your passport at the Turkish border.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (at least 6 months validity beyond entry date)</li>
<li>Valid email address</li>
<li>Credit/debit card for the {fee} fee</li>
<li>Return or onward travel booking (may be requested at the border)</li>
</ul>

<div class="alert alert-warning mt-3">
    <strong>Warning:</strong> Only use the official government site <a href="{TURKEY_EVISA_URL}" target="_blank" rel="noopener">evisa.gov.tr</a>. Many third-party sites charge additional fees for the same service.
</div>"""
    else:
        # fallback
        status_badge = '<span style="color:grey;">Check Requirements</span>'
        status_type = "Check Requirements"
        fee_cell = "Varies"
        stay_cell = "Varies"
        apply_cell = f'<a href="{TURKEY_EVISA_URL}" target="_blank" rel="noopener">evisa.gov.tr</a>'
        desc = f"Turkey visa requirements for {label} citizens. Updated March 2026."
        body_content = f"<p>Please check current Turkey visa requirements for {label} citizens at <a href='{TURKEY_EVISA_URL}' target='_blank' rel='noopener'>evisa.gov.tr</a>.</p>"

    if nat == "turkish":
        faq_q1 = "Do Turkish citizens need a visa to enter Turkey?"
        faq_a1 = "No — Turkey is the home country for Turkish citizens. No visa is required."
        faq_q2 = "What documents do Turkish citizens need to enter Turkey?"
        faq_a2 = "A valid Turkish passport or, in some cases, a Turkish national ID card is sufficient to enter Turkey."
    elif nat in TURKEY_VISA_FREE:
        faq_q1 = f"Do {label} citizens need a visa for Turkey?"
        faq_a1 = f"No. {label} passport holders can enter Turkey visa-free for up to 90 days within any 180-day period."
        faq_q2 = f"How long can {label} citizens stay in Turkey without a visa?"
        faq_a2 = "Up to 90 days within any 180-day period. For longer stays a residence permit is required."
    else:
        fee = TURKEY_EVISA.get(nat, "varies")
        faq_q1 = f"Do {label} citizens need a visa for Turkey?"
        faq_a1 = f"Yes. {label} passport holders must obtain a Turkey eVisa ({fee}) before travel. Apply at evisa.gov.tr."
        faq_q2 = f"How much is the Turkey eVisa for {label} citizens?"
        faq_a2 = f"The Turkey eVisa fee for {label} citizens is {fee}. Apply at the official portal evisa.gov.tr."

    faq_json = f"""    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {{"@type":"Question","name":"{faq_q1}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a1}"}}}},
      {{"@type":"Question","name":"{faq_q2}","acceptedAnswer":{{"@type":"Answer","text":"{faq_a2}"}}}}
    ]}}"""

    page = f"""{head(title, desc, slug, flag)}
    <script type="application/ld+json">
{faq_json}
    </script>
{navbar(slug)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-tr mr-2"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Turkey for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{status_type}</td></tr>
<tr><th>Fee</th><td>{fee_cell}</td></tr>
<tr><th>Max Stay</th><td>{stay_cell}</td></tr>
<tr><th>Processing</th><td>{'Immediate on arrival' if nat in TURKEY_VISA_FREE or nat == 'turkish' else 'Usually within 24 hours'}</td></tr>
<tr><th>Apply At</th><td>{apply_cell if nat in TURKEY_EVISA else 'N/A'}</td></tr>
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current entry requirements at <a href="https://evisa.gov.tr" target="_blank" rel="noopener">evisa.gov.tr</a> or the nearest Turkish embassy before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="uae-visa-for-{nat}-citizens.html"><span class="fi fi-ae mr-1"></span>UAE Visa for {label} Citizens</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="australia-visa-for-{nat}-citizens.html">Australia Visa for {label} Citizens</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="canada-visa-for-{nat}-citizens.html">Canada Visa for {label} Citizens</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
</div>

</article>
</div>
</section>

{FOOTER}"""
    return page


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    for nat in NATS:
        # UAE page
        uae_filename = f"uae-visa-for-{nat}-citizens.html"
        uae_path = os.path.join(OUTPUT_DIR, uae_filename)
        with open(uae_path, "w", encoding="utf-8") as f:
            f.write(make_uae_page(nat))
        created.append(uae_filename)

        # Turkey page
        turkey_filename = f"turkey-visa-for-{nat}-citizens.html"
        turkey_path = os.path.join(OUTPUT_DIR, turkey_filename)
        with open(turkey_path, "w", encoding="utf-8") as f:
            f.write(make_turkey_page(nat))
        created.append(turkey_filename)

    print(f"Created {len(created)} files in {OUTPUT_DIR}:")
    for fn in created:
        print(f"  {fn}")


if __name__ == "__main__":
    main()
