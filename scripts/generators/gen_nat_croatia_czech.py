#!/usr/bin/env python3
"""
Generate 40 HTML nationality pages for Croatia and Czech Republic.
Output: www/en/croatia-visa-for-{nat}-citizens.html
        www/en/czech-republic-visa-for-{nat}-citizens.html
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------

NATIONALITIES = [
    # slug, display, flag-icon code, passport adjective
    ("us",            "US",            "us", "US"),
    ("uk",            "UK",            "gb", "British"),
    ("canadian",      "Canadian",      "ca", "Canadian"),
    ("french",        "French",        "fr", "French"),
    ("german",        "German",        "de", "German"),
    ("japanese",      "Japanese",      "jp", "Japanese"),
    ("australian",    "Australian",    "au", "Australian"),
    ("indian",        "Indian",        "in", "Indian"),
    ("chinese",       "Chinese",       "cn", "Chinese"),
    ("russian",       "Russian",       "ru", "Russian"),
    ("brazilian",     "Brazilian",     "br", "Brazilian"),
    ("mexican",       "Mexican",       "mx", "Mexican"),
    ("south-african", "South African", "za", "South African"),
    ("nigerian",      "Nigerian",      "ng", "Nigerian"),
    ("korean",        "Korean",        "kr", "South Korean"),
    ("singaporean",   "Singaporean",   "sg", "Singaporean"),
    ("indonesian",    "Indonesian",    "id", "Indonesian"),
    ("philippine",    "Philippine",    "ph", "Philippine"),
    ("turkish",       "Turkish",       "tr", "Turkish"),
    ("argentinian",   "Argentinian",   "ar", "Argentinian"),
]

# Visa-free (ETIAS) nationalities
VISA_FREE_ETIAS = {"us", "uk", "canadian", "japanese", "australian",
                   "korean", "singaporean", "brazilian", "mexican", "argentinian"}

# EU free-movement nationalities
EU_FREE = {"french", "german"}

# Schengen-visa nationalities (everything else)
# indian, chinese, russian, indonesian, philippine, nigerian, south-african, turkish


# ---------------------------------------------------------------------------
# Helper: determine status for a given nationality slug
# ---------------------------------------------------------------------------

def visa_status(nat_slug):
    if nat_slug in EU_FREE:
        return "eu"
    if nat_slug in VISA_FREE_ETIAS:
        return "etias"
    return "visa"


# ---------------------------------------------------------------------------
# Shared HTML fragments
# ---------------------------------------------------------------------------

NAV = """\
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


# ---------------------------------------------------------------------------
# Content builders
# ---------------------------------------------------------------------------

def build_croatia_page(nat_slug, nat_display, flag_code, passport_adj):
    status = visa_status(nat_slug)
    file_slug = f"croatia-visa-for-{nat_slug}-citizens"

    # ---- meta ----
    if status == "eu":
        title       = f"Croatia Visa for {nat_display} Citizens 2026 — EU Free Movement"
        description = (f"{nat_display} passport holders visiting Croatia in 2026: EU free movement rights, "
                       f"no visa needed, unlimited stay. Complete guide updated March 2026.")
    elif status == "etias":
        title       = f"Croatia Visa for {nat_display} Citizens 2026 — Visa Free + ETIAS"
        description = (f"{nat_display} passport holders visiting Croatia in 2026: visa-free 90 days, "
                       f"ETIAS required from 2025. Complete guide updated March 2026.")
    else:
        title       = f"Croatia Visa for {nat_display} Citizens 2026 — Schengen Requirements"
        description = (f"{nat_display} passport holders visiting Croatia in 2026: Schengen visa requirements, "
                       f"\u20ac80 fee, 15 working days via VFS. Complete guide updated March 2026.")

    # ---- FAQ schema ----
    if status == "eu":
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Croatia?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens enjoy full EU free movement rights in Croatia. No visa or ETIAS is required. You may live, work, and stay indefinitely with a valid passport or national ID."}}}},
      {{"@type":"Question","name":"How long can {nat_display} citizens stay in Croatia?","acceptedAnswer":{{"@type":"Answer","text":"As EU nationals, {passport_adj} citizens may stay in Croatia without any time limit. Stays beyond 3 months may require registering with local authorities."}}}},
      {{"@type":"Question","name":"Do {nat_display} citizens need a passport for Croatia?","acceptedAnswer":{{"@type":"Answer","text":"A valid national identity card or passport is sufficient for {passport_adj} citizens to enter Croatia, as both countries are EU member states."}}}}
    ]"""
    elif status == "etias":
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Croatia?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens are visa-free for Croatia. Since Croatia joined the Schengen Area in January 2023, visits of up to 90 days in any 180-day period require no visa. ETIAS pre-travel authorisation (€7) is required from 2025."}}}},
      {{"@type":"Question","name":"What is ETIAS and do {nat_display} citizens need it for Croatia?","acceptedAnswer":{{"@type":"Answer","text":"ETIAS is a mandatory online travel authorisation for visa-exempt nationalities entering the Schengen Area, including Croatia. It costs €7, takes minutes to obtain online, and is valid for 3 years."}}}},
      {{"@type":"Question","name":"How long can {nat_display} citizens stay in Croatia?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens may stay up to 90 days in any 180-day period in Croatia (and across the entire Schengen Area). For longer stays a national visa (D-visa) is required."}}}}
    ]"""
    else:
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Croatia?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {passport_adj} passport holders must obtain a Schengen Type C visa before travelling to Croatia. Applications are submitted at the Croatian embassy or authorised VFS Global centre."}}}},
      {{"@type":"Question","name":"How much does a Croatia Schengen visa cost for {nat_display} applicants?","acceptedAnswer":{{"@type":"Answer","text":"The Schengen visa fee is €80 for adults (13+) and €40 for children aged 6\u201312. Children under 6 are free. Fees are non-refundable."}}}},
      {{"@type":"Question","name":"How long does Croatia visa processing take?","acceptedAnswer":{{"@type":"Answer","text":"Standard processing is 15 working days from submission at VFS Global. Apply at least 3\u20134 weeks before your intended travel date."}}}}
    ]"""

    # ---- key-facts table ----
    if status == "eu":
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">No &#8212; EU Free Movement</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>Unlimited (EU citizen)</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>N/A</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>N/A</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>No application needed</td></tr>"
    elif status == "etias":
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">No &#8212; Visa Free (ETIAS required)</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>90 days in any 180-day period</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>N/A (ETIAS &euro;7)</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>Instant (ETIAS online)</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>etias.com (when required)</td></tr>"
    else:
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Yes &#8212; Schengen Visa Required</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>90 days in any 180-day period</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>&euro;80 (adults), &euro;40 (children 6&ndash;12)</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>15 working days</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>Croatian Embassy / VFS Global</td></tr>"

    # ---- body content ----
    if status == "eu":
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Croatia?</h2>
<p>No. As fellow EU member-state nationals, {passport_adj} citizens enjoy <strong>full freedom of movement</strong> in Croatia. You may enter, reside, work, and stay without any time limit using a valid passport or national identity card. No visa, ETIAS, or prior authorisation is needed.</p>

<h2>Entry Requirements for {nat_display} Citizens</h2>
<ul>
<li>Valid EU national identity card <em>or</em> passport</li>
<li>No advance visa or ETIAS required</li>
<li>Stays beyond 3 months: register with the local police or municipality</li>
</ul>

<h2>Living and Working in Croatia</h2>
<p>EU citizens may work in Croatia without a work permit. For stays longer than 3 months you must register your residence at the local police station or administrative office within 8 days of arrival. After 5 years of continuous residence you may apply for a permanent residence certificate.</p>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://mup.gov.hr" target="_blank" rel="noopener">mup.gov.hr</a> before travel.</p>
</div>"""

    elif status == "etias":
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Croatia?</h2>
<p>No. {passport_adj} passport holders can visit Croatia <strong>visa-free for up to 90 days in any 180-day period</strong>. Croatia joined the Schengen Area in January 2023, so your 90-day allowance now counts across the entire Schengen zone, not just Croatia.</p>
<p>From 2025, {nat_display} travellers must register for <strong>ETIAS</strong> before entering any Schengen country including Croatia. The online application costs &euro;7 and is valid for 3 years.</p>

<h2>ETIAS for Croatia</h2>
<ul>
<li>Cost: <strong>&euro;7</strong></li>
<li>Validity: 3 years (or until passport expiry)</li>
<li>Apply: online at the official ETIAS website &mdash; approval usually within minutes</li>
<li>Required: before boarding any flight/ferry to a Schengen country</li>
</ul>

<h2>Border Documents</h2>
<ul>
<li>Valid {passport_adj} passport (min. 3 months validity beyond planned departure)</li>
<li>ETIAS authorisation (from 2025)</li>
<li>Return or onward travel ticket</li>
<li>Proof of accommodation</li>
<li>Proof of sufficient funds (~&euro;100/day recommended)</li>
<li>Travel/health insurance</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://mup.gov.hr" target="_blank" rel="noopener">mup.gov.hr</a> before travel.</p>
</div>"""

    else:
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Croatia?</h2>
<p>Yes. {passport_adj} passport holders must obtain a <strong>Schengen Type C visa</strong> before travelling to Croatia. Croatia joined the Schengen Area in January 2023, so a standard Schengen visa covers Croatia along with all other Schengen countries. There is no separate Croatian visa. Applications must be submitted in person at the Croatian embassy, consulate, or an authorised <strong>VFS Global</strong> application centre.</p>

<h2>Schengen Visa Key Details</h2>
<ul>
<li>Fee: <strong>&euro;80</strong> for adults (13+); &euro;40 for children aged 6&ndash;12; free under 6</li>
<li>Processing time: <strong>15 working days</strong> (up to 45 days in peak season)</li>
<li>Max stay: <strong>90 days in any 180-day period</strong> across the Schengen Area</li>
<li>Apply: at least 3&ndash;4 weeks before travel; no earlier than 6 months before departure</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Book an appointment at your nearest <strong>VFS Global</strong> centre or Croatian embassy.</li>
<li>Complete the Schengen visa application form (available at VFS or the embassy website).</li>
<li>Attend in person: submit documents and provide biometric data (fingerprints and photo).</li>
<li>Pay the &euro;80 visa fee. Track your application online via VFS.</li>
<li>Collect your passport with the visa sticker (allow extra time for courier return).</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid {passport_adj} passport (min. 2 blank pages, issued within last 10 years)</li>
<li>Two recent passport photos (35&times;45 mm, white background)</li>
<li>Completed Schengen visa application form</li>
<li>Bank statements &mdash; last 3 months (min. &euro;100/day of stay)</li>
<li>Travel insurance &mdash; min. &euro;30,000 coverage valid across the Schengen Area</li>
<li>Confirmed return flight itinerary</li>
<li>Proof of accommodation (hotel booking or host invitation letter)</li>
<li>Employment letter / approved leave / proof of self-employment or student enrolment</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://mup.gov.hr" target="_blank" rel="noopener">mup.gov.hr</a> before travel.</p>
</div>"""

    # ---- related guides ----
    related = f"""\
<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-croatia.html">Croatia Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="croatia-visa-requirements.html">Croatia Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="croatia-visa-fees.html">Croatia Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="croatia-visa-processing-time.html">Croatia Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    nav_html = NAV.replace("{slug}", file_slug)

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
    <link rel="canonical" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq}}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{nav_html}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>Croatia Visa for {nat_display} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Croatia for {nat_display} Citizens</th></tr></thead>
<tbody>
{kf_visa_row}
{kf_stay_row}
{kf_fee_row}
{kf_proc_row}
{kf_apply_row}
</tbody>
</table>

{body_content}

{related}

</article>
</div>
</section>

{FOOTER}
</body>
</html>
"""


def build_czech_page(nat_slug, nat_display, flag_code, passport_adj):
    status = visa_status(nat_slug)
    file_slug = f"czech-republic-visa-for-{nat_slug}-citizens"

    # ---- meta ----
    if status == "eu":
        title       = f"Czech Republic Visa for {nat_display} Citizens 2026 — EU Free Movement"
        description = (f"{nat_display} passport holders visiting Czech Republic in 2026: EU free movement rights, "
                       f"no visa needed, unlimited stay. Complete guide updated March 2026.")
    elif status == "etias":
        title       = f"Czech Republic Visa for {nat_display} Citizens 2026 — Visa Free + ETIAS"
        description = (f"{nat_display} passport holders visiting Czech Republic in 2026: visa-free 90 days, "
                       f"ETIAS required from 2025. Complete guide updated March 2026.")
    else:
        title       = f"Czech Republic Visa for {nat_display} Citizens 2026 — Schengen Requirements"
        description = (f"{nat_display} passport holders visiting Czech Republic in 2026: Schengen visa requirements, "
                       f"\u20ac80 fee, 15 working days via VFS. Complete guide updated March 2026.")

    # ---- FAQ schema ----
    if status == "eu":
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens enjoy full EU free movement rights in the Czech Republic. No visa or ETIAS is required. You may live, work, and stay indefinitely with a valid passport or national ID."}}}},
      {{"@type":"Question","name":"How long can {nat_display} citizens stay in Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"As EU nationals, {passport_adj} citizens may stay in Czech Republic without any time limit. Stays beyond 30 days should be registered with the Foreign Police."}}}},
      {{"@type":"Question","name":"Do {nat_display} citizens need a passport for Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"A valid EU national identity card or passport is sufficient for {passport_adj} citizens to enter Czech Republic."}}}}
    ]"""
    elif status == "etias":
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens are visa-free for Czech Republic. Visits of up to 90 days in any 180-day period across the Schengen Area require no visa. ETIAS pre-travel authorisation (€7) is required from 2025."}}}},
      {{"@type":"Question","name":"What is ETIAS and do {nat_display} citizens need it for Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"ETIAS is a mandatory online travel authorisation for visa-exempt nationalities entering the Schengen Area, including Czech Republic. It costs €7, takes minutes to obtain, and is valid for 3 years."}}}},
      {{"@type":"Question","name":"How long can {nat_display} citizens stay in Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"{passport_adj} citizens may stay up to 90 days in any 180-day period in Czech Republic (and across the Schengen Area). For longer stays a national long-stay visa is required."}}}}
    ]"""
    else:
        faq = f"""[
      {{"@type":"Question","name":"Do {nat_display} citizens need a visa for Czech Republic?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {passport_adj} passport holders must obtain a Schengen Type C visa before travelling to Czech Republic. Applications are submitted at the Czech embassy or authorised VFS Global centre."}}}},
      {{"@type":"Question","name":"How much does a Czech Republic Schengen visa cost for {nat_display} applicants?","acceptedAnswer":{{"@type":"Answer","text":"The Schengen visa fee is €80 for adults (13+) and €40 for children aged 6\u201312. Children under 6 are free. Fees are non-refundable."}}}},
      {{"@type":"Question","name":"How long does Czech Republic visa processing take?","acceptedAnswer":{{"@type":"Answer","text":"Standard processing is 15 working days from submission at VFS Global. Apply at least 3\u20134 weeks before your intended travel date."}}}}
    ]"""

    # ---- key-facts table ----
    if status == "eu":
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">No &#8212; EU Free Movement</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>Unlimited (EU citizen)</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>N/A</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>N/A</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>No application needed</td></tr>"
    elif status == "etias":
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">No &#8212; Visa Free (ETIAS required)</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>90 days in any 180-day period</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>N/A (ETIAS &euro;7)</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>Instant (ETIAS online)</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>etias.com (when required)</td></tr>"
    else:
        kf_visa_row  = '<tr><th>Visa Required</th><td><span style="color:red;font-weight:600;">Yes &#8212; Schengen Visa Required</span></td></tr>'
        kf_stay_row  = "<tr><th>Max Stay</th><td>90 days in any 180-day period</td></tr>"
        kf_fee_row   = "<tr><th>Visa Fee</th><td>&euro;80 (adults), &euro;40 (children 6&ndash;12)</td></tr>"
        kf_proc_row  = "<tr><th>Processing Time</th><td>15 working days</td></tr>"
        kf_apply_row = "<tr><th>Apply At</th><td>Czech Embassy / VFS Global</td></tr>"

    # ---- body content ----
    if status == "eu":
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Czech Republic?</h2>
<p>No. As EU nationals, {passport_adj} citizens enjoy <strong>full EU freedom of movement</strong> in the Czech Republic. You may enter, reside, work, and stay without any time limit using a valid passport or national identity card. No visa, ETIAS, or prior authorisation is required.</p>

<h2>Entry Requirements for {nat_display} Citizens</h2>
<ul>
<li>Valid EU national identity card <em>or</em> passport</li>
<li>No advance visa or ETIAS required</li>
<li>Stays beyond 30 days: register with the Foreign Police (Cizineck&aacute; policie)</li>
</ul>

<h2>Living and Working in Czech Republic</h2>
<p>EU citizens may work in Czech Republic without a work permit. For stays longer than 30 days you should report your residence to the Foreign Police. After 5 years of uninterrupted residence you may apply for permanent residence.</p>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://www.mvcr.cz/mvcren/" target="_blank" rel="noopener">mvcr.cz</a> before travel.</p>
</div>"""

    elif status == "etias":
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Czech Republic?</h2>
<p>No. {passport_adj} passport holders can visit Czech Republic <strong>visa-free for up to 90 days in any 180-day period</strong> across the entire Schengen Area. This covers tourism, family visits, and short business trips.</p>
<p>From 2025, {nat_display} travellers must register for <strong>ETIAS</strong> before entering the Schengen Area. The online application costs &euro;7 and is valid for 3 years.</p>

<h2>ETIAS for Czech Republic</h2>
<ul>
<li>Cost: <strong>&euro;7</strong></li>
<li>Validity: 3 years (or until passport expiry)</li>
<li>Apply: online at the official ETIAS website &mdash; approval usually within minutes</li>
<li>Required: before boarding any flight/train to a Schengen country</li>
</ul>

<h2>Border Documents</h2>
<ul>
<li>Valid {passport_adj} passport (min. 3 months validity beyond planned departure)</li>
<li>ETIAS authorisation (from 2025)</li>
<li>Return or onward travel ticket</li>
<li>Proof of accommodation</li>
<li>Proof of sufficient funds (~&euro;100/day recommended)</li>
<li>Travel/health insurance</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://www.mvcr.cz/mvcren/" target="_blank" rel="noopener">mvcr.cz</a> before travel.</p>
</div>"""

    else:
        body_content = f"""\
<h2>Do {nat_display} Citizens Need a Visa for Czech Republic?</h2>
<p>Yes. {passport_adj} passport holders must obtain a <strong>Schengen Type C visa</strong> before travelling to Czech Republic. A Schengen visa covers the Czech Republic along with all 26 other Schengen member states. Applications must be submitted in person at the Czech embassy, consulate, or an authorised <strong>VFS Global</strong> application centre.</p>

<h2>Schengen Visa Key Details</h2>
<ul>
<li>Fee: <strong>&euro;80</strong> for adults (13+); &euro;40 for children aged 6&ndash;12; free under 6</li>
<li>Processing time: <strong>15 working days</strong> (up to 45 days during peak season)</li>
<li>Max stay: <strong>90 days in any 180-day period</strong> across the Schengen Area</li>
<li>Apply: at least 3&ndash;4 weeks before travel; no earlier than 6 months before departure</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Book an appointment at your nearest <strong>VFS Global</strong> centre handling Czech Republic visas, or at the Czech embassy/consulate directly.</li>
<li>Download and complete the Schengen visa application form from the Czech embassy website.</li>
<li>Attend in person: submit your documents and provide biometric data (fingerprints and photo).</li>
<li>Pay the &euro;80 visa fee. Track application status online via VFS.</li>
<li>Collect your passport with the Schengen visa sticker.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid {passport_adj} passport (min. 2 blank pages, issued within last 10 years)</li>
<li>Two recent passport photos (35&times;45 mm, white background)</li>
<li>Completed Schengen visa application form</li>
<li>Bank statements &mdash; last 3 months (min. &euro;100/day of stay)</li>
<li>Travel insurance &mdash; min. &euro;30,000 coverage valid across the Schengen Area</li>
<li>Confirmed return flight itinerary</li>
<li>Proof of accommodation (hotel booking or host invitation letter)</li>
<li>Employment letter / approved leave / proof of self-employment or student enrolment</li>
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://www.mvcr.cz/mvcren/" target="_blank" rel="noopener">mvcr.cz</a> before travel.</p>
</div>"""

    # ---- related guides ----
    related = f"""\
<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-czech-republic.html">Czech Republic Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="czech-republic-visa-requirements.html">Czech Republic Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="czech-republic-visa-fees.html">Czech Republic Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="czech-republic-visa-processing-time.html">Czech Republic Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    nav_html = NAV.replace("{slug}", file_slug)

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
    <link rel="canonical" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{file_slug}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq}}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{nav_html}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>Czech Republic Visa for {nat_display} Citizens 2026</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Czech Republic for {nat_display} Citizens</th></tr></thead>
<tbody>
{kf_visa_row}
{kf_stay_row}
{kf_fee_row}
{kf_proc_row}
{kf_apply_row}
</tbody>
</table>

{body_content}

{related}

</article>
</div>
</section>

{FOOTER}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for nat_slug, nat_display, flag_code, passport_adj in NATIONALITIES:
        # Croatia
        croatia_html = build_croatia_page(nat_slug, nat_display, flag_code, passport_adj)
        croatia_file = os.path.join(OUT_DIR, f"croatia-visa-for-{nat_slug}-citizens.html")
        with open(croatia_file, "w", encoding="utf-8") as f:
            f.write(croatia_html)
        created.append(croatia_file)

        # Czech Republic
        czech_html = build_czech_page(nat_slug, nat_display, flag_code, passport_adj)
        czech_file = os.path.join(OUT_DIR, f"czech-republic-visa-for-{nat_slug}-citizens.html")
        with open(czech_file, "w", encoding="utf-8") as f:
            f.write(czech_html)
        created.append(czech_file)

    print(f"Generated {len(created)} HTML files:")
    for p in created:
        print(f"  {os.path.basename(p)}")


if __name__ == "__main__":
    main()
