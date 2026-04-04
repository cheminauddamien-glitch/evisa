"""
gen_nat_india_mexico.py
Generates 40 HTML files in www/en/:
  india-visa-for-{nat}-citizens.html  (20 files)
  mexico-visa-for-{nat}-citizens.html (20 files)

Bootstrap 4 Pacific theme, GA4 G-XC1GYM27WC, AdSense ca-pub-9298895030863686,
flag-icons, ../css/ ../js/
"""

import os
import pathlib

# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------

NATIONALITIES = [
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "indian", "chinese", "russian", "brazilian", "mexican", "south-african",
    "nigerian", "korean", "singaporean", "indonesian", "philippine",
    "turkish", "argentinian",
]

# Display labels
NAT_LABEL = {
    "us":           "US",
    "uk":           "UK",
    "canadian":     "Canadian",
    "french":       "French",
    "german":       "German",
    "japanese":     "Japanese",
    "australian":   "Australian",
    "indian":       "Indian",
    "chinese":      "Chinese",
    "russian":      "Russian",
    "brazilian":    "Brazilian",
    "mexican":      "Mexican",
    "south-african":"South African",
    "nigerian":     "Nigerian",
    "korean":       "Korean",
    "singaporean":  "Singaporean",
    "indonesian":   "Indonesian",
    "philippine":   "Philippine",
    "turkish":      "Turkish",
    "argentinian":  "Argentinian",
}

# ISO 3166-1 alpha-2 flag codes
FLAG_CODE = {
    "us":           "us",
    "uk":           "gb",
    "canadian":     "ca",
    "french":       "fr",
    "german":       "de",
    "japanese":     "jp",
    "australian":   "au",
    "indian":       "in",
    "chinese":      "cn",
    "russian":      "ru",
    "brazilian":    "br",
    "mexican":      "mx",
    "south-african":"za",
    "nigerian":     "ng",
    "korean":       "kr",
    "singaporean":  "sg",
    "indonesian":   "id",
    "philippine":   "ph",
    "turkish":      "tr",
    "argentinian":  "ar",
}

# --- India visa status ---
# All 20 nationalities need an e-Tourist Visa (none are visa-free)
# Indian nationals are domestic (not included as a foreign visitor page,
# but a page is still generated for completeness — marked as domestic)
INDIA_EVISA = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "russian", "brazilian", "mexican", "argentinian",
    "indonesian", "philippine", "turkish", "south-african", "nigerian", "chinese",
}

# --- Mexico visa status ---
MEXICO_VISAFREE = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "russian", "brazilian", "argentinian",
}
# Mexican nationals are domestic
# Everyone pays FMM card: MXN 685 / USD 36
MEXICO_CONSULAR = {
    "indian", "chinese", "indonesian", "philippine", "nigerian",
    "south-african", "turkish",
}

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

NAVBAR = """\
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation"
            class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="../retirement-visa-guide.html">Guides</a></li>
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button"
                        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"
                        style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi fi-gb"></span> English
                    </a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="#"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

FOOTER = """\
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

def head_block(title, description, canonical_slug, faq_json):
    return f"""\
<!DOCTYPE html>
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
    <script type="application/ld+json">
    {faq_json}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


# ---------------------------------------------------------------------------
# INDIA PAGE GENERATOR
# ---------------------------------------------------------------------------

def build_india_page(nat):
    label = NAT_LABEL[nat]
    flag = FLAG_CODE[nat]
    slug = f"india-visa-for-{nat}-citizens"
    filename = f"{slug}.html"
    year = 2026

    if nat == "indian":
        # Domestic — short informational page
        title = f"India Visa for Indian Citizens 2026"
        desc = ("Indian citizens are domestic nationals and do not require a visa to visit India. "
                "Learn about Indian Passport services, OCI cards, and international travel.")
        faq = ('{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
               '{"@type":"Question","name":"Do Indian citizens need a visa for India?",'
               '"acceptedAnswer":{"@type":"Answer","text":"No. Indian citizens are domestic nationals '
               'and do not require a visa to travel within India. For travel abroad, Indian passport '
               'holders should check the visa requirements of their destination country."}},'
               '{"@type":"Question","name":"What is an OCI card?",'
               '"acceptedAnswer":{"@type":"Answer","text":"An Overseas Citizen of India (OCI) card '
               'allows persons of Indian origin who are foreign nationals to live and work in India '
               'indefinitely. It is not a visa but a long-term residency status."}}]}')
        h1 = f"India Visa for Indian Citizens"
        status_badge = '<span style="color:green;font-weight:600;">Domestic &mdash; No Visa Required</span>'
        body_content = f"""\
<p><span class="fi fi-in mr-1"></span> <strong>Indian citizens</strong> are domestic nationals and
require <strong>no visa</strong> to travel within India. India is your home country.</p>

<h2>Indian Passport &amp; Travel Services</h2>
<p>For Indian citizens travelling <em>abroad</em>, visa requirements vary by destination. Use the links
below to explore requirements for popular destinations.</p>

<h2>Overseas Citizen of India (OCI)</h2>
<p>Persons of Indian origin holding foreign nationality may apply for an <strong>OCI card</strong>,
which grants lifelong multiple-entry to India and near-parity rights with Indian citizens for most purposes.
Apply via the Passport Seva portal at <a href="https://passportindia.gov.in" target="_blank" rel="noopener">passportindia.gov.in</a>.</p>

<h2>Indian Passport Renewal</h2>
<ul>
<li>Apply online at <a href="https://passportindia.gov.in" target="_blank" rel="noopener">passportindia.gov.in</a></li>
<li>Book a Passport Seva Kendra (PSK) appointment</li>
<li>Standard processing: 7&ndash;15 working days; Tatkal: 1&ndash;3 working days</li>
</ul>
"""
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Nationality</th><td>Domestic</td></tr>
<tr><th>Official Portal</th><td><a href="https://passportindia.gov.in" target="_blank" rel="noopener">passportindia.gov.in</a></td></tr>"""

    else:
        # e-Tourist Visa page
        title = f"India Visa for {label} Citizens 2026"
        desc = (f"{label} passport holders visiting India in 2026: e-Tourist Visa options "
                f"(USD 25 / USD 40 / USD 80), how to apply at evisa.india.gov.in, "
                f"requirements and processing times.")
        faq = (f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
               f'{{"@type":"Question","name":"Do {label} citizens need a visa for India?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"{label} passport holders require an '
               f'Indian e-Tourist Visa before travel. Apply online at evisa.india.gov.in. '
               f'Choose from 30-day (USD 25), 1-year (USD 40) or 5-year (USD 80) options."}}}},'
               f'{{"@type":"Question","name":"How do I apply for an India e-Visa?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"Visit evisa.india.gov.in, complete '
               f'the online application form, upload your passport scan and photo, pay the fee '
               f'by card, and receive your ETA by email within 72 hours."}}}},'
               f'{{"@type":"Question","name":"How long can I stay in India on an e-Tourist Visa?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"The 30-day e-Tourist Visa allows a '
               f'single or double entry with up to 30 days per visit. The 1-year multiple-entry '
               f'visa allows stays of up to 90 days per visit (60 days for some nationalities). '
               f'The 5-year multiple-entry visa allows stays of up to 90 days per visit."}}}}]}}')
        h1 = f"India Visa for {label} Citizens 2026"
        status_badge = '<span style="color:orange;font-weight:600;">e-Tourist Visa Required</span>'
        body_content = f"""\
<h2>Do {label} Citizens Need a Visa for India?</h2>
<p><span class="fi fi-{flag} mr-1"></span> <strong>{label} passport holders</strong> require an
<strong>Indian e-Tourist Visa</strong> before travelling to India. The e-Visa is applied for entirely
online at <a href="https://evisa.india.gov.in" target="_blank" rel="noopener">evisa.india.gov.in</a>
&mdash; no consular visit is required.</p>

<h2>India e-Tourist Visa Options</h2>
<div class="table-responsive">
<table class="table table-bordered table-sm">
<thead class="thead-light">
<tr><th>Validity</th><th>Fee (USD)</th><th>Entries</th><th>Max Stay per Visit</th></tr>
</thead>
<tbody>
<tr><td><strong>30 Days</strong></td><td><strong>USD 25</strong></td><td>Double entry</td><td>30 days</td></tr>
<tr><td><strong>1 Year</strong></td><td><strong>USD 40</strong></td><td>Multiple entry</td><td>90 days</td></tr>
<tr><td><strong>5 Years</strong></td><td><strong>USD 80</strong></td><td>Multiple entry</td><td>90 days</td></tr>
</tbody>
</table>
</div>
<p class="small text-muted">Fees are approximate and subject to change. Check <a href="https://evisa.india.gov.in" target="_blank" rel="noopener">evisa.india.gov.in</a> for current fees at time of application.</p>

<h2>How to Apply for an India e-Tourist Visa</h2>
<ol>
<li>Go to <a href="https://evisa.india.gov.in" target="_blank" rel="noopener">evisa.india.gov.in</a> (official Indian government portal).</li>
<li>Click <strong>"Apply"</strong> and select <em>e-Tourist Visa</em>.</li>
<li>Complete the online application with your personal and passport details.</li>
<li>Upload a recent passport-sized photo and a scanned copy of the bio-data page of your passport.</li>
<li>Pay the e-Visa fee by credit/debit card (Visa, Mastercard, Amex accepted).</li>
<li>Receive your Electronic Travel Authorisation (ETA) by email &mdash; typically within <strong>72 hours</strong> (allow up to 4 business days).</li>
<li>Print the ETA and carry it with you when you travel to India.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport with at least 6 months validity beyond your planned departure from India</li>
<li>At least two blank pages in your passport</li>
<li>Passport-sized photograph (white background, recent)</li>
<li>Return or onward travel ticket</li>
<li>Proof of accommodation in India</li>
<li>Sufficient funds for your stay</li>
<li>Credit/debit card for fee payment</li>
</ul>

<h2>Entry Points</h2>
<p>e-Tourist Visa holders may enter India through designated airports (including Delhi, Mumbai, Bengaluru,
Chennai, Hyderabad, Kolkata, Goa, Kochi, Ahmedabad, Amritsar, Varanasi) and select seaports.
Land border entry is <strong>not</strong> permitted on an e-Visa.</p>

<h2>Important Notes</h2>
<ul>
<li>Apply at least <strong>4&ndash;7 business days</strong> before travel to allow processing time.</li>
<li>The e-Visa cannot be extended or converted inside India.</li>
<li>A new e-Visa application is required for each trip if your current e-Visa has expired or entries are used.</li>
<li>The e-Tourist Visa is valid from the date of issue, not from entry date.</li>
<li>Carry a printed copy of your ETA; airline staff will request it at check-in.</li>
</ul>
"""
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>e-Tourist Visa (online)</td></tr>
<tr><th>30-Day Fee</th><td>USD 25</td></tr>
<tr><th>1-Year Fee</th><td>USD 40</td></tr>
<tr><th>5-Year Fee</th><td>USD 80</td></tr>
<tr><th>Processing Time</th><td>Up to 72 hours (allow 4 business days)</td></tr>
<tr><th>Apply At</th><td><a href="https://evisa.india.gov.in" target="_blank" rel="noopener">evisa.india.gov.in</a></td></tr>"""

    eeat_url = "https://evisa.india.gov.in"
    if nat == "indian":
        eeat_url = "https://passportindia.gov.in"

    html = f"""{head_block(title, desc, slug, faq)}
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-in mr-2"></span>{h1}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; India Visa for {label} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at
    <a href="{eeat_url}" target="_blank" rel="noopener">{eeat_url}</a> before travel.
    See our <a href="our-methodology.html">editorial methodology</a>.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-india.html">India Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="india-visa-requirements.html">India Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="india-visa-fees.html">India Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="india-visa-processing-time.html">India Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>"""
    return filename, html


# ---------------------------------------------------------------------------
# MEXICO PAGE GENERATOR
# ---------------------------------------------------------------------------

def build_mexico_page(nat):
    label = NAT_LABEL[nat]
    flag = FLAG_CODE[nat]
    slug = f"mexico-visa-for-{nat}-citizens"
    filename = f"{slug}.html"

    if nat == "mexican":
        # Domestic
        title = "Mexico Visa for Mexican Citizens 2026"
        desc = ("Mexican citizens are domestic nationals and require no visa to live in Mexico. "
                "Information on Mexican passport renewal, CURP, and international travel.")
        faq = ('{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
               '{"@type":"Question","name":"Do Mexican citizens need a visa for Mexico?",'
               '"acceptedAnswer":{"@type":"Answer","text":"No. Mexican citizens are domestic nationals '
               'and do not require a visa to live or travel in Mexico. For international travel, '
               'Mexican passport holders enjoy visa-free or visa-on-arrival access to over 140 countries."}}]}')
        h1 = "Mexico Visa for Mexican Citizens"
        status_badge = '<span style="color:green;font-weight:600;">Domestic &mdash; No Visa Required</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Nationality</th><td>Domestic</td></tr>
<tr><th>Passport Portal</th><td><a href="https://www.gob.mx/sre/acciones-y-programas/tramite-de-pasaporte" target="_blank" rel="noopener">gob.mx/sre</a></td></tr>"""
        body_content = """\
<p><span class="fi fi-mx mr-1"></span> <strong>Mexican citizens</strong> are domestic nationals
and require <strong>no visa</strong> to travel within Mexico.</p>

<h2>Mexican Passport Renewal</h2>
<p>Renew your Mexican passport through the <strong>Secretaría de Relaciones Exteriores (SRE)</strong>:</p>
<ul>
<li>Book an appointment at <a href="https://www.gob.mx/sre" target="_blank" rel="noopener">gob.mx/sre</a></li>
<li>Present your current passport, CURP, and proof of Mexican nationality (birth certificate)</li>
<li>Processing: 5&ndash;10 working days at most SRE offices</li>
</ul>

<h2>International Travel for Mexican Citizens</h2>
<p>Mexican passport holders enjoy <strong>visa-free or visa-on-arrival</strong> access to over
140 countries and territories, including the Schengen Area, United Kingdom, and Japan.
Check destination requirements before travel.</p>
"""
        eeat_url = "https://www.gob.mx/sre"

    elif nat in MEXICO_VISAFREE:
        # Visa-free + FMM
        title = f"Mexico Visa for {label} Citizens 2026"
        desc = (f"{label} passport holders do not need a visa for Mexico (up to 180 days). "
                f"Learn about the FMM tourist card (MXN 685 / approx USD 36), entry requirements, "
                f"and tips for visiting Mexico in 2026.")
        faq = (f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
               f'{{"@type":"Question","name":"Do {label} citizens need a visa for Mexico?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"{label} passport holders are '
               f'visa-exempt for Mexico for stays up to 180 days. However, all visitors must '
               f'complete the Forma Migratoria Múltiple (FMM) tourist card, which costs approximately '
               f'MXN 685 (about USD 36). The FMM fee is often included in airline tickets."}}}},'
               f'{{"@type":"Question","name":"What is the FMM card for Mexico?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"The Forma Migratoria Múltiple (FMM) is '
               f'Mexico\'s tourist entry card. All foreign visitors must complete it on arrival. '
               f'The fee (approx. MXN 685 / USD 36) is often pre-paid when purchasing airline tickets. '
               f'Keep the FMM stamp in your passport &mdash; you need it to depart Mexico."}}}},'
               f'{{"@type":"Question","name":"How long can {label} citizens stay in Mexico?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"{label} citizens may stay in Mexico '
               f'for up to 180 days per visit without a visa. The exact permitted stay is determined '
               f'by the immigration officer at the port of entry."}}}}]}}')
        h1 = f"Mexico Visa for {label} Citizens 2026"
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free &mdash; Up to 180 Days</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Max Stay</th><td>Up to 180 days per visit</td></tr>
<tr><th>FMM Tourist Card</th><td>Required &mdash; MXN 685 (approx. USD 36)</td></tr>
<tr><th>FMM Often Included</th><td>In airfare for flights to Mexico</td></tr>
<tr><th>Entry</th><td>Air, land, and sea ports of entry</td></tr>"""
        body_content = f"""\
<h2>Do {label} Citizens Need a Visa for Mexico?</h2>
<p><span class="fi fi-{flag} mr-1"></span> <strong>{label} passport holders</strong> are
<strong>visa-exempt</strong> for Mexico. You can stay for up to <strong>180 days</strong>
per visit for tourism, business visits, or transit &mdash; no visa application required.</p>

<h2>FMM Tourist Card (Forma Migratoria Múltiple)</h2>
<p>All foreign visitors to Mexico &mdash; even those visa-exempt &mdash; must complete the
<strong>Forma Migratoria Múltiple (FMM)</strong> tourist card. The fee is approximately
<strong>MXN 685 (about USD 36)</strong>.</p>
<ul>
<li>The FMM fee is <strong>usually included</strong> in the price of airline tickets to Mexico.</li>
<li>If travelling by land or sea, you pay the FMM fee at the port of entry.</li>
<li>Keep the FMM tear-off stub stamped in your passport &mdash; you <strong>must present it when departing</strong> Mexico.</li>
<li>Losing the FMM stub may result in a fine when exiting the country.</li>
</ul>

<h2>Entry Requirements for {label} Citizens</h2>
<ul>
<li>Valid passport (6 months validity recommended beyond your stay)</li>
<li>Return or onward travel ticket</li>
<li>Proof of sufficient funds (roughly USD 50 per day recommended)</li>
<li>Completed FMM card (provided on the aircraft or at land entry)</li>
<li>Accommodation details if requested by immigration officer</li>
</ul>

<h2>Extending Your Stay</h2>
<p>If you wish to stay longer than the period granted by the immigration officer (maximum 180 days),
you must leave Mexico and re-enter. Extensions inside Mexico are not routinely granted to tourists.</p>

<h2>Practical Tips</h2>
<ul>
<li>The 180-day limit is the maximum &mdash; the immigration officer may grant a shorter period.</li>
<li>You may be asked to show proof of accommodation and funds at the border.</li>
<li>Working in Mexico on a tourist permit is <strong>not permitted</strong>.</li>
</ul>
"""
        eeat_url = "https://www.inm.gob.mx"

    else:
        # Consular visa required
        title = f"Mexico Visa for {label} Citizens 2026"
        desc = (f"{label} passport holders require a consular visa to visit Mexico. "
                f"Learn about Mexico visa types, requirements, fees, and the FMM tourist card "
                f"(MXN 685 / approx USD 36) for {label} travellers in 2026.")
        faq = (f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
               f'{{"@type":"Question","name":"Do {label} citizens need a visa for Mexico?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"{label} passport holders require '
               f'a Mexican consular visa before travelling to Mexico. Apply at your nearest '
               f'Mexican embassy or consulate. Additionally, all visitors must pay the FMM '
               f'tourist card fee (approx. MXN 685 / USD 36) on arrival."}}}},'
               f'{{"@type":"Question","name":"How do I apply for a Mexican visa?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"Contact the Mexican embassy or '
               f'consulate in your country, book an appointment, and submit the required documents '
               f'including passport, application form, photos, proof of funds, travel itinerary, '
               f'and proof of accommodation. Processing typically takes 5&ndash;15 business days."}}}},'
               f'{{"@type":"Question","name":"What is the FMM fee for Mexico?",'
               f'"acceptedAnswer":{{"@type":"Answer","text":"All foreign visitors to Mexico pay '
               f'the Forma Migratoria Múltiple (FMM) fee of approximately MXN 685 (about USD 36). '
               f'This is separate from the visa fee and is payable on arrival or included in airfare."}}}}]}}')
        h1 = f"Mexico Visa for {label} Citizens 2026"
        status_badge = '<span style="color:red;font-weight:600;">Mexican Consular Visa Required</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>Mexican Consular Visa (Tourist / FMT)</td></tr>
<tr><th>Apply At</th><td>Mexican Embassy or Consulate</td></tr>
<tr><th>FMM Tourist Card</th><td>Also Required &mdash; MXN 685 (approx. USD 36) on arrival</td></tr>
<tr><th>Processing Time</th><td>5&ndash;15 business days (varies by consulate)</td></tr>"""
        body_content = f"""\
<h2>Do {label} Citizens Need a Visa for Mexico?</h2>
<p><span class="fi fi-{flag} mr-1"></span> <strong>{label} passport holders</strong> require a
<strong>Mexican consular visa</strong> before travelling to Mexico. You must apply at the
Mexican embassy or consulate in your country prior to travel.</p>

<h2>Mexico Visa Types for Tourists</h2>
<ul>
<li><strong>Visitor Visa (FMT) &mdash; Tourism:</strong> For tourism visits up to 180 days.</li>
<li><strong>Visitor Visa &mdash; Business:</strong> For business meetings and conferences.</li>
<li><strong>Visitor Visa &mdash; Transit:</strong> For passing through Mexico to a third country.</li>
</ul>

<h2>How to Apply for a Mexico Visa</h2>
<ol>
<li>Locate the nearest <strong>Mexican Embassy or Consulate</strong> in your country via
<a href="https://embamex.sre.gob.mx" target="_blank" rel="noopener">embamex.sre.gob.mx</a>.</li>
<li>Book an appointment online or by telephone.</li>
<li>Complete the official visa application form.</li>
<li>Gather required documents (see list below).</li>
<li>Attend your appointment and pay the visa fee.</li>
<li>Receive visa decision &mdash; typically within <strong>5&ndash;15 business days</strong>.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (at least 6 months validity beyond intended travel dates, with at least 2 blank pages)</li>
<li>Completed and signed visa application form</li>
<li>Two recent passport-sized photographs (white background)</li>
<li>Proof of economic solvency (bank statements for last 3&ndash;6 months)</li>
<li>Round-trip flight itinerary or booking confirmation</li>
<li>Hotel reservations or accommodation proof</li>
<li>Travel insurance (recommended; may be required)</li>
<li>Proof of ties to home country (employment letter, property ownership, family ties)</li>
</ul>

<h2>FMM Tourist Card</h2>
<p>In addition to your consular visa, you will also be required to pay the
<strong>Forma Migratoria Múltiple (FMM)</strong> fee of approximately <strong>MXN 685 (about USD 36)</strong>
on arrival in Mexico. This is typically included in international airfare but may be payable
separately at land or sea borders. Keep the FMM stub until you leave Mexico.</p>

<h2>Visa Fees</h2>
<p>Mexican visa fees vary by nationality and visa type. Contact your local Mexican consulate
for the current fee schedule. Fees are generally in the range of USD 36&ndash;100.</p>
"""
        eeat_url = "https://embamex.sre.gob.mx"

    html = f"""{head_block(title, desc, slug, faq)}
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-mx mr-2"></span>{h1}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Mexico Visa for {label} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at
    <a href="{eeat_url}" target="_blank" rel="noopener">{eeat_url}</a> before travel.
    See our <a href="our-methodology.html">editorial methodology</a>.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-mexico.html">Mexico Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="mexico-visa-requirements.html">Mexico Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="mexico-visa-fees.html">Mexico Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="mexico-visa-processing-time.html">Mexico Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>"""
    return filename, html


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    out_dir = pathlib.Path(__file__).parent / "www" / "en"
    out_dir.mkdir(parents=True, exist_ok=True)

    created = []

    for nat in NATIONALITIES:
        # India
        fname, html = build_india_page(nat)
        fpath = out_dir / fname
        fpath.write_text(html, encoding="utf-8")
        created.append(fname)
        print(f"  CREATED: {fname}")

        # Mexico
        fname, html = build_mexico_page(nat)
        fpath = out_dir / fname
        fpath.write_text(html, encoding="utf-8")
        created.append(fname)
        print(f"  CREATED: {fname}")

    print(f"\nTotal files created: {len(created)}")
    return created


if __name__ == "__main__":
    main()
