"""
Generate 40 HTML nationality pages for Portugal and Greece.
Output directory: www/en/
Files: portugal-visa-for-{nat}-citizens.html
       greece-visa-for-{nat}-citizens.html
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# -------------------------------------------------------------------
# Nationality metadata
# -------------------------------------------------------------------
NAT_META = {
    "us": {
        "label": "US",
        "full": "US Citizens",
        "flag": "us",
        "passport": "US passport holders",
    },
    "uk": {
        "label": "UK",
        "full": "UK Citizens",
        "flag": "gb",
        "passport": "UK passport holders",
    },
    "canadian": {
        "label": "Canadian",
        "full": "Canadian Citizens",
        "flag": "ca",
        "passport": "Canadian passport holders",
    },
    "french": {
        "label": "French",
        "full": "French Citizens",
        "flag": "fr",
        "passport": "French passport holders",
    },
    "german": {
        "label": "German",
        "full": "German Citizens",
        "flag": "de",
        "passport": "German passport holders",
    },
    "japanese": {
        "label": "Japanese",
        "full": "Japanese Citizens",
        "flag": "jp",
        "passport": "Japanese passport holders",
    },
    "australian": {
        "label": "Australian",
        "full": "Australian Citizens",
        "flag": "au",
        "passport": "Australian passport holders",
    },
    "indian": {
        "label": "Indian",
        "full": "Indian Citizens",
        "flag": "in",
        "passport": "Indian passport holders",
    },
    "chinese": {
        "label": "Chinese",
        "full": "Chinese Citizens",
        "flag": "cn",
        "passport": "Chinese passport holders",
    },
    "russian": {
        "label": "Russian",
        "full": "Russian Citizens",
        "flag": "ru",
        "passport": "Russian passport holders",
    },
    "brazilian": {
        "label": "Brazilian",
        "full": "Brazilian Citizens",
        "flag": "br",
        "passport": "Brazilian passport holders",
    },
    "mexican": {
        "label": "Mexican",
        "full": "Mexican Citizens",
        "flag": "mx",
        "passport": "Mexican passport holders",
    },
    "south-african": {
        "label": "South African",
        "full": "South African Citizens",
        "flag": "za",
        "passport": "South African passport holders",
    },
    "nigerian": {
        "label": "Nigerian",
        "full": "Nigerian Citizens",
        "flag": "ng",
        "passport": "Nigerian passport holders",
    },
    "korean": {
        "label": "Korean",
        "full": "Korean Citizens",
        "flag": "kr",
        "passport": "South Korean passport holders",
    },
    "singaporean": {
        "label": "Singaporean",
        "full": "Singaporean Citizens",
        "flag": "sg",
        "passport": "Singaporean passport holders",
    },
    "indonesian": {
        "label": "Indonesian",
        "full": "Indonesian Citizens",
        "flag": "id",
        "passport": "Indonesian passport holders",
    },
    "philippine": {
        "label": "Philippine",
        "full": "Philippine Citizens",
        "flag": "ph",
        "passport": "Philippine passport holders",
    },
    "turkish": {
        "label": "Turkish",
        "full": "Turkish Citizens",
        "flag": "tr",
        "passport": "Turkish passport holders",
    },
    "argentinian": {
        "label": "Argentinian",
        "full": "Argentinian Citizens",
        "flag": "ar",
        "passport": "Argentinian passport holders",
    },
}

# Visa status groups
VISA_FREE_ETIAS = {"us", "uk", "canadian", "japanese", "australian", "korean",
                   "singaporean", "brazilian", "mexican", "argentinian"}
EU_FREE = {"french", "german"}
SCHENGEN_VISA = {"indian", "chinese", "russian", "indonesian", "philippine",
                 "nigerian", "south-african", "turkish"}

# -------------------------------------------------------------------
# Country metadata
# -------------------------------------------------------------------
COUNTRIES = {
    "portugal": {
        "label": "Portugal",
        "embassy_url": "https://vistos.mne.gov.pt/en/",
        "embassy_name": "Consular Services Portal (vistos.mne.gov.pt)",
        "related": [
            ("portugal-visa-requirements.html", "Portugal Requirements"),
            ("portugal-visa-fees.html", "Portugal Fees"),
            ("portugal-visa-processing-time.html", "Portugal Processing Times"),
        ],
        "extra_note": True,   # D7 / Golden Visa note
    },
    "greece": {
        "label": "Greece",
        "embassy_url": "https://www.mfa.gr/en/",
        "embassy_name": "Greek Ministry of Foreign Affairs (mfa.gr)",
        "related": [
            ("greece-visa-requirements.html", "Greece Requirements"),
            ("greece-visa-fees.html", "Greece Fees"),
            ("greece-visa-processing-time.html", "Greece Processing Times"),
        ],
        "extra_note": False,
    },
}

# -------------------------------------------------------------------
# HTML helpers
# -------------------------------------------------------------------
HEAD_TMPL = """\
<!DOCTYPE html>
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
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}"/>
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

NAV_TMPL = """\
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
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Fran&ccedil;ais</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Espa&ntilde;ol</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Portugu&ecirc;s</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

FOOTER_TMPL = """\
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
<script src="../js/main.js"></script>
</body>
</html>"""


# -------------------------------------------------------------------
# Content builders
# -------------------------------------------------------------------

def build_visa_free_etias(country_label, country_key, nat_key, nm, cm):
    """Content for visa-free / ETIAS-required nationals."""
    passport = nm["passport"]
    nat_label = nm["label"]
    flag = nm["flag"]
    embassy_url = cm["embassy_url"]

    if country_key == "portugal":
        etias_note = (
            "ETIAS (European Travel Information and Authorisation System) is expected "
            "to launch in 2026. Once operational, {passport} will need to obtain ETIAS "
            "authorisation online before travelling to Portugal and the wider Schengen Area. "
            "Until ETIAS is live, entry remains visa-free for stays up to 90 days in any "
            "180-day period."
        ).format(passport=passport)
        long_stay_note = """\

<h2>Long-Stay Options for {nat_label} Citizens in Portugal</h2>
<p>For stays beyond 90 days, {passport} may consider:</p>
<ul>
<li><strong>D7 Passive Income Visa</strong> — for retirees or those with sufficient passive income (pensions, investments, remote work income). Minimum monthly income requirement applies.</li>
<li><strong>Portugal Golden Visa</strong> — residency by investment programme. Investment thresholds and qualifying routes should be verified at the official SEF/AIMA portal.</li>
</ul>
<p>Both visas are applied for at a Portuguese consulate in your home country prior to travel.</p>
""".format(nat_label=nat_label, passport=passport)
    else:
        etias_note = (
            "ETIAS (European Travel Information and Authorisation System) is expected "
            "to launch in 2026. Once operational, {passport} will need to obtain ETIAS "
            "authorisation online before travelling to Greece and the wider Schengen Area. "
            "Until ETIAS is live, entry remains visa-free for stays up to 90 days in any "
            "180-day period."
        ).format(passport=passport)
        long_stay_note = ""

    faq = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{{"@type":"Question","name":"Do {nat_label} citizens need a visa for {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"{passport} can visit {country_label} '
        'visa-free for up to 90 days in any 180-day period. ETIAS authorisation will be '
        'required once the system launches in 2026."}}}},'
        '{{"@type":"Question","name":"What is ETIAS and does it affect {nat_label} citizens?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"ETIAS is a pre-travel authorisation for '
        'visa-exempt visitors to the Schengen Area. It will apply to {nat_label} travellers '
        'visiting {country_label} once launched."}}}},'
        '{{"@type":"Question","name":"How long can {nat_label} citizens stay in {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"Up to 90 days in any 180-day period '
        'without a visa. Overstaying can result in fines and future entry bans."}}}}'
        ']}}'
    ).format(
        nat_label=nat_label, country_label=country_label, passport=passport
    )

    meta_desc = (
        "{passport} visiting {country_label} in 2026: visa-free up to 90 days, "
        "ETIAS required once live. Complete guide updated March 2026."
    ).format(passport=passport, country_label=country_label)

    title = "{country_label} Visa for {nat_label} Citizens 2026".format(
        country_label=country_label, nat_label=nat_label
    )

    body = """\

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {country_label} for {nat_label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">Visa-Free &mdash; 90 days / 180-day period</span></td></tr>
<tr><th>ETIAS</th><td>Required once launched (expected 2026)</td></tr>
<tr><th>Fee</th><td>ETIAS approx. EUR 7 (waived under 18 / over 70)</td></tr>
<tr><th>Max Stay</th><td>90 days in any 180-day period</td></tr>
<tr><th>Processing</th><td>Visa-free; ETIAS usually approved within minutes to 72 hours</td></tr>
<tr><th>Apply At</th><td>travel-europe.europa.eu (ETIAS official site, once live)</td></tr>
</tbody>
</table>

<h2>Do {nat_label} Citizens Need a Visa for {country_label}?</h2>
<p><strong>{passport}</strong> enjoy <strong>visa-free access</strong> to {country_label} and the entire Schengen Area for short stays of up to <strong>90 days in any 180-day period</strong>. No visa application is required for tourism, visiting family, or short business trips.</p>

<h2>ETIAS &mdash; Pre-Travel Authorisation</h2>
<p>{etias_note}</p>
<ul>
<li>Fee: approximately <strong>EUR 7</strong> (free for travellers under 18 or over 70)</li>
<li>Validity: 3 years or until passport expiry</li>
<li>Covers the entire Schengen Area (multiple entries)</li>
<li>Application: online, approval usually within minutes to 72 hours</li>
</ul>
{long_stay_note}
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (recommended 3+ months validity beyond planned stay)</li>
<li>Proof of sufficient funds for the stay</li>
<li>Return or onward travel ticket</li>
<li>Travel / health insurance (recommended)</li>
<li>Accommodation proof (hotel booking or host invitation)</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{embassy_url}" target="_blank" rel="noopener">{embassy_name}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    {related_links}
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>
""".format(
        title=title,
        country_label=country_label,
        nat_label=nat_label,
        passport=passport,
        etias_note=etias_note,
        long_stay_note=long_stay_note,
        embassy_url=embassy_url,
        embassy_name=cm["embassy_name"],
        related_links=build_related_links(cm),
    )

    return title, meta_desc, faq, body


def build_eu_free(country_label, country_key, nat_key, nm, cm):
    """Content for EU free-movement nationals (French, German)."""
    passport = nm["passport"]
    nat_label = nm["label"]
    embassy_url = cm["embassy_url"]

    if country_key == "portugal":
        long_stay = """\

<h2>Registering for Long-Term Residence</h2>
<p>{passport} planning to reside in Portugal for more than 3 months must register with the local parish council (<em>Junta de Freguesia</em>) and obtain a registration certificate as an EU citizen. No visa is required.</p>
<p><strong>Portugal D7 and Golden Visa</strong> are designed for non-EU nationals and do not apply to French or German citizens exercising EU free-movement rights.</p>
""".format(passport=passport)
    else:
        long_stay = """\

<h2>Registering for Long-Term Residence in Greece</h2>
<p>{passport} who wish to remain in Greece for more than 3 months must register at the local municipality (<em>Dimarcheio</em>) and apply for an EU citizen registration certificate. No visa is required.</p>
""".format(passport=passport)

    faq = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{{"@type":"Question","name":"Do {nat_label} citizens need a visa for {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"{passport} have the right of free movement '
        'within the EU. No visa, ETIAS, or any travel authorisation is required to enter or '
        'reside in {country_label}."}}}},'
        '{{"@type":"Question","name":"Can {nat_label} citizens live and work in {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"Yes. Under EU free-movement rules, '
        '{nat_label} citizens may live, work, and study in {country_label} without any visa '
        'or work permit."}}}},'
        '{{"@type":"Question","name":"Do {nat_label} citizens need ETIAS for {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"No. ETIAS applies only to non-EU nationals. '
        'As EU citizens, {nat_label} passport holders are exempt from ETIAS entirely."}}}}'
        ']}}'
    ).format(nat_label=nat_label, country_label=country_label, passport=passport)

    meta_desc = (
        "{passport} visiting {country_label} in 2026: EU free movement, no visa or ETIAS needed. "
        "Complete guide updated March 2026."
    ).format(passport=passport, country_label=country_label)

    title = "{country_label} Visa for {nat_label} Citizens 2026".format(
        country_label=country_label, nat_label=nat_label
    )

    body = """\

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {country_label} for {nat_label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">No Visa &mdash; EU Free Movement</span></td></tr>
<tr><th>ETIAS</th><td>Not applicable (EU citizens exempt)</td></tr>
<tr><th>Fee</th><td>None</td></tr>
<tr><th>Max Stay</th><td>Unlimited (EU free movement rights)</td></tr>
<tr><th>Work Rights</th><td>Full right to live and work</td></tr>
<tr><th>Apply At</th><td>No application required</td></tr>
</tbody>
</table>

<h2>Do {nat_label} Citizens Need a Visa for {country_label}?</h2>
<p><strong>{passport}</strong> have the unrestricted right to enter, reside, and work in <strong>{country_label}</strong> under <strong>EU free-movement rules</strong> (Directive 2004/38/EC). No visa, no ETIAS, and no pre-travel authorisation of any kind is required.</p>

<h2>Travel Documents</h2>
<ul>
<li>Valid national ID card or passport &mdash; either is accepted for entry</li>
<li>No minimum validity requirement beyond the planned stay</li>
</ul>
{long_stay}
<h2>Healthcare and Social Rights</h2>
<ul>
<li>European Health Insurance Card (EHIC) covers emergency medical treatment during temporary stays</li>
<li>After registration as a resident, full access to local healthcare system</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{embassy_url}" target="_blank" rel="noopener">{embassy_name}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    {related_links}
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>
""".format(
        title=title,
        country_label=country_label,
        nat_label=nat_label,
        passport=passport,
        long_stay=long_stay,
        embassy_url=embassy_url,
        embassy_name=cm["embassy_name"],
        related_links=build_related_links(cm),
    )

    return title, meta_desc, faq, body


def build_schengen_visa(country_label, country_key, nat_key, nm, cm):
    """Content for nationals who need a Schengen visa."""
    passport = nm["passport"]
    nat_label = nm["label"]
    embassy_url = cm["embassy_url"]

    if country_key == "portugal":
        pt_extra = """\

<h2>Portugal-Specific Long-Stay Visas</h2>
<p>After a short-stay Schengen visit, {passport} wishing to stay longer may consider:</p>
<ul>
<li><strong>D7 Passive Income Visa</strong> &mdash; for retirees and those with sufficient passive income. Apply at a Portuguese consulate before travelling.</li>
<li><strong>Portugal Golden Visa</strong> &mdash; residency by qualifying investment. Consult the official AIMA portal for current thresholds and eligible investment types.</li>
</ul>
""".format(passport=passport)
        apply_note = "Apply at <a href='https://vistos.mne.gov.pt/en/' target='_blank' rel='noopener'>vistos.mne.gov.pt</a> or the nearest Portuguese consulate / VFS Global centre."
    else:
        pt_extra = ""
        apply_note = "Apply at the nearest Greek consulate or <a href='https://www.vfsglobal.com/greece/' target='_blank' rel='noopener'>VFS Global</a> application centre."

    faq = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{{"@type":"Question","name":"Do {nat_label} citizens need a visa for {country_label}?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"Yes. {passport} must obtain a Schengen '
        'short-stay (C) visa before travelling to {country_label}. The fee is EUR 80 and '
        'processing takes approximately 15 working days via VFS Global."}}}},'
        '{{"@type":"Question","name":"How much does a {country_label} visa cost for {nat_label} citizens?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"The standard Schengen visa fee is EUR 80. '
        'Children aged 6&ndash;12 pay EUR 40. Children under 6 are exempt."}}}},'
        '{{"@type":"Question","name":"How long does {country_label} visa processing take?",'
        '"acceptedAnswer":{{"@type":"Answer","text":"Approximately 15 working days from the date '
        'of biometric submission. Apply at least 4&ndash;6 weeks before travel."}}}}'
        ']}}'
    ).format(nat_label=nat_label, country_label=country_label, passport=passport)

    meta_desc = (
        "{passport} visiting {country_label} in 2026: Schengen visa required, EUR 80, "
        "15 working days via VFS Global. Complete guide updated March 2026."
    ).format(passport=passport, country_label=country_label)

    title = "{country_label} Visa for {nat_label} Citizens 2026".format(
        country_label=country_label, nat_label=nat_label
    )

    body = """\

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {country_label} for {nat_label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Visa Required &mdash; EUR 80</span></td></tr>
<tr><th>Visa Type</th><td>Schengen Short-Stay Visa (Type C)</td></tr>
<tr><th>Fee</th><td>EUR 80 (adults); EUR 40 (children 6&ndash;12); free (under 6)</td></tr>
<tr><th>Max Stay</th><td>Up to 90 days in any 180-day period</td></tr>
<tr><th>Processing</th><td>Approximately 15 working days</td></tr>
<tr><th>Apply At</th><td>VFS Global / nearest consulate</td></tr>
</tbody>
</table>

<h2>Does a {nat_label} Citizen Need a Visa for {country_label}?</h2>
<p><strong>{passport}</strong> must obtain a <strong>Schengen short-stay visa (Type C)</strong> before travelling to {country_label}. The application is submitted through <strong>VFS Global</strong> or directly at the nearest consulate. The standard fee is <strong>EUR 80</strong> and processing takes approximately <strong>15 working days</strong> after biometric submission.</p>

<h2>Schengen Visa Key Details</h2>
<ul>
<li>Fee: <strong>EUR 80</strong> (adults); EUR 40 (children 6&ndash;12); free under 6</li>
<li>Processing: approximately 15 working days</li>
<li>Maximum stay: 90 days in any 180-day period</li>
<li>Biometrics: required (fingerprints and photograph)</li>
<li>Valid for: all Schengen Area countries</li>
</ul>

<h2>How to Apply for a {country_label} Schengen Visa</h2>
<ol>
<li>Book an appointment at VFS Global or your nearest {country_label} consulate.</li>
<li>Complete the Schengen visa application form online or in person.</li>
<li>Pay the EUR 80 fee.</li>
<li>Attend your appointment and provide biometric data (fingerprints and photo).</li>
<li>Submit supporting documents (see list below).</li>
<li>Await the decision &mdash; approximately 15 working days. Apply at least 4&ndash;6 weeks before travel.</li>
</ol>
<p>{apply_note}</p>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (at least 3 months beyond intended departure; issued within the last 10 years)</li>
<li>Completed Schengen application form</li>
<li>Two recent passport-size photographs (35&times;45 mm, white background)</li>
<li>Travel insurance with minimum EUR 30,000 medical coverage</li>
<li>Proof of accommodation (hotel bookings or invitation letter)</li>
<li>Round-trip flight itinerary</li>
<li>Bank statements (last 3&ndash;6 months) showing sufficient funds</li>
<li>Proof of employment or enrolment / business registration</li>
<li>No-objection letter (if employed)</li>
</ul>
{pt_extra}
<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{embassy_url}" target="_blank" rel="noopener">{embassy_name}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    {related_links}
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>
""".format(
        title=title,
        country_label=country_label,
        nat_label=nat_label,
        passport=passport,
        apply_note=apply_note,
        pt_extra=pt_extra,
        embassy_url=embassy_url,
        embassy_name=cm["embassy_name"],
        related_links=build_related_links(cm),
    )

    return title, meta_desc, faq, body


def build_related_links(cm):
    parts = []
    for href, text in cm["related"]:
        parts.append(
            '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{href}">{text}</a>'.format(
                href=href, text=text
            )
        )
    return "\n    ".join(parts)


# -------------------------------------------------------------------
# Main generator
# -------------------------------------------------------------------

def generate_page(country_key, nat_key):
    nm = NAT_META[nat_key]
    cm = COUNTRIES[country_key]
    country_label = cm["label"]

    slug = "{country_key}-visa-for-{nat_key}-citizens".format(
        country_key=country_key, nat_key=nat_key
    )
    filename = slug + ".html"

    if nat_key in EU_FREE:
        title, meta_desc, faq, body = build_eu_free(country_label, country_key, nat_key, nm, cm)
    elif nat_key in VISA_FREE_ETIAS:
        title, meta_desc, faq, body = build_visa_free_etias(country_label, country_key, nat_key, nm, cm)
    else:
        title, meta_desc, faq, body = build_schengen_visa(country_label, country_key, nat_key, nm, cm)

    head = HEAD_TMPL.format(
        title=title,
        meta_desc=meta_desc,
        slug=slug,
        faq_json=faq,
    )
    nav = NAV_TMPL.format(slug=slug)

    html = head + "\n" + nav + "\n" + body + "\n" + FOOTER_TMPL

    out_path = os.path.join(OUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return filename


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    nationalities = list(NAT_META.keys())
    countries = ["portugal", "greece"]
    created = []

    for country_key in countries:
        for nat_key in nationalities:
            fname = generate_page(country_key, nat_key)
            created.append(fname)
            print("Created:", fname)

    print("\nTotal files created:", len(created))
    assert len(created) == 40, "Expected 40 files, got {}".format(len(created))
    print("All 40 files verified.")


if __name__ == "__main__":
    main()
