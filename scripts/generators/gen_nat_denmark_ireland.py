#!/usr/bin/env python3
"""
Generate 40 HTML pages:
  - denmark-visa-for-{nat}-citizens.html  (20 nationalities)
  - ireland-visa-for-{nat}-citizens.html  (20 nationalities)
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATIONALITIES = [
    # slug          display            adjective           flag  demonym (passport)
    ("us",            "US",              "US",               "us",  "US"),
    ("uk",            "UK",              "British",          "gb",  "British"),
    ("canadian",      "Canadian",        "Canadian",         "ca",  "Canadian"),
    ("french",        "French",          "French",           "fr",  "French"),
    ("german",        "German",          "German",           "de",  "German"),
    ("japanese",      "Japanese",        "Japanese",         "jp",  "Japanese"),
    ("australian",    "Australian",      "Australian",       "au",  "Australian"),
    ("indian",        "Indian",          "Indian",           "in",  "Indian"),
    ("chinese",       "Chinese",         "Chinese",          "cn",  "Chinese"),
    ("russian",       "Russian",         "Russian",          "ru",  "Russian"),
    ("brazilian",     "Brazilian",       "Brazilian",        "br",  "Brazilian"),
    ("mexican",       "Mexican",         "Mexican",          "mx",  "Mexican"),
    ("south-african", "South African",   "South African",    "za",  "South African"),
    ("nigerian",      "Nigerian",        "Nigerian",         "ng",  "Nigerian"),
    ("korean",        "Korean",          "South Korean",     "kr",  "South Korean"),
    ("singaporean",   "Singaporean",     "Singaporean",      "sg",  "Singaporean"),
    ("indonesian",    "Indonesian",      "Indonesian",       "id",  "Indonesian"),
    ("philippine",    "Philippine",      "Philippine",       "ph",  "Philippine"),
    ("turkish",       "Turkish",         "Turkish",          "tr",  "Turkish"),
    ("argentinian",   "Argentinian",     "Argentinian",      "ar",  "Argentinian"),
]

# ---------------------------------------------------------------------------
# Denmark visa categories
# ---------------------------------------------------------------------------
DK_VISA_FREE_ETIAS = {"us", "uk", "canadian", "japanese", "australian",
                      "korean", "singaporean", "brazilian", "mexican", "argentinian"}
DK_EU_FREE         = {"french", "german"}
DK_VISA_REQUIRED   = {"indian", "chinese", "russian", "indonesian",
                      "philippine", "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# Ireland visa categories
# ---------------------------------------------------------------------------
IE_VISA_FREE  = {"uk", "canadian", "australian", "us", "japanese",
                 "korean", "singaporean", "brazilian", "mexican", "argentinian"}
IE_EU_FREE    = {"french", "german"}
IE_VISA_REQ   = {"indian", "chinese", "russian", "indonesian",
                 "philippine", "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

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

HEAD_COMMON = """\
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>"""

LINKS_COMMON = """\
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>"""

# ---------------------------------------------------------------------------
# Denmark generator
# ---------------------------------------------------------------------------

def dk_page(slug, display, adj, flag, demonym):
    filename = f"denmark-visa-for-{slug}-citizens.html"
    page_url = f"https://www.evisa-card.com/en/denmark-visa-for-{slug}-citizens"
    title_suffix = "2026"

    # Determine category
    if slug in DK_EU_FREE:
        cat = "eu_free"
    elif slug in DK_VISA_FREE_ETIAS:
        cat = "visa_free_etias"
    else:
        cat = "visa_required"

    # ---- title / description / schema ----
    if cat == "eu_free":
        page_title = f"Denmark Visa for {display} Citizens 2026 — EU Free Movement"
        meta_desc  = (f"{display} passport holders enjoy EU free movement rights in Denmark. "
                      f"No visa required. {adj} citizens may live, work, and travel freely. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Denmark?",
             f"No. As EU citizens, {adj} nationals enjoy free movement rights and do not need a visa to enter, live, or work in Denmark."),
            (f"How long can {display} citizens stay in Denmark?",
             "EU citizens may reside in Denmark indefinitely under EU free movement rules. No stay limit applies."),
            (f"Do {display} citizens need ETIAS for Denmark?",
             "No. ETIAS does not apply to EU citizens. French and German nationals are exempt from ETIAS entirely."),
        ]
        status_cell = '<span style="color:green;font-weight:600;">EU Free Movement — No Visa Required</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Status</th><td>EU free movement (Treaty rights)</td></tr>
<tr><th>Max Stay</th><td>Unlimited (register after 3 months)</td></tr>
<tr><th>ETIAS</th><td>Not required</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Denmark?</h2>
<p>No. {adj} citizens hold EU passports and benefit from <strong>EU free movement rights</strong> in Denmark. No visa, permit, or ETIAS is needed. You may enter freely and stay for an unlimited period; if you reside for more than three months you should register with the Danish authorities.</p>

<h2>Entry Requirements for {display} Citizens</h2>
<ul>
<li>Valid {adj} passport or national ID card</li>
<li>No prior approval, visa, or ETIAS needed</li>
<li>Register with local authorities (Folkeregisteret) after 3 months of continuous stay</li>
<li>EU citizens have the right to work, study, and live in Denmark</li>
</ul>

<h2>Travelling Within the Schengen Area</h2>
<p>Denmark is a Schengen member. {adj} citizens may cross Schengen internal borders freely with a national ID card or passport. There are no systematic border checks between Schengen states for EU nationals.</p>"""
        eeat_link = "https://www.nyidanmark.dk"
        eeat_anchor = "nyidanmark.dk"

    elif cat == "visa_free_etias":
        page_title = f"Denmark Visa for {display} Citizens 2026 — Visa-Free + ETIAS"
        meta_desc  = (f"{display} passport holders can visit Denmark visa-free for up to 90 days. "
                      f"ETIAS authorisation required from 2025. Schengen rules apply. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Denmark?",
             f"No. {adj} nationals are visa-exempt for short stays up to 90 days in any 180-day period within the Schengen Area, including Denmark."),
            ("What is ETIAS and do I need it?",
             "ETIAS (European Travel Information and Authorisation System) is a pre-travel electronic authorisation required for visa-exempt nationals. It is valid for 3 years, costs €7, and must be obtained before travel."),
            (f"How long can {display} citizens stay in Denmark?",
             "Up to 90 days in any 180-day period across the entire Schengen Area (not just Denmark)."),
        ]
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — ETIAS Required</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Max Stay</th><td>90 days / 180-day period (Schengen)</td></tr>
<tr><th>ETIAS</th><td>Required (€7, 3-year validity)</td></tr>
<tr><th>Apply</th><td>travel-europe.europa.eu/etias</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Denmark?</h2>
<p>No. {adj} passport holders are <strong>visa-exempt</strong> for short stays in Denmark and the entire Schengen Area. However, ETIAS (European Travel Information and Authorisation System) is required before travel.</p>

<h2>ETIAS — What You Need to Know</h2>
<p>ETIAS is an electronic pre-travel authorisation (not a visa). You apply online, pay <strong>€7</strong>, and receive approval within minutes in most cases. ETIAS is valid for <strong>3 years</strong> or until your passport expires, whichever comes first, and covers unlimited trips across all Schengen countries.</p>

<h2>Entry Requirements for {display} Citizens</h2>
<ul>
<li>Valid {adj} passport (at least 3 months beyond planned stay)</li>
<li>Valid ETIAS authorisation (obtained before departure)</li>
<li>Proof of sufficient funds (approx. €100/day)</li>
<li>Return or onward travel ticket</li>
<li>Travel/health insurance recommended</li>
</ul>

<h2>Schengen 90/180 Day Rule</h2>
<p>The 90-day limit applies across the entire Schengen Area, not just Denmark. Time spent in any Schengen country counts toward your 90-day allowance in any rolling 180-day period.</p>"""
        eeat_link = "https://travel-europe.europa.eu/etias_en"
        eeat_anchor = "travel-europe.europa.eu/etias"

    else:  # visa_required
        page_title = f"Denmark Schengen Visa for {display} Citizens 2026"
        meta_desc  = (f"{display} passport holders need a Schengen visa for Denmark in 2026. "
                      f"Fee EUR 80, 15 working days processing, apply via VFS Global. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Denmark?",
             f"Yes. {adj} nationals must obtain a Schengen Type C visa before travelling to Denmark. The fee is EUR 80 and processing takes 15 working days."),
            ("How much does a Denmark Schengen visa cost?",
             "The standard Schengen visa fee is EUR 80 for adults (13+), EUR 40 for children aged 6–12, and free for children under 6. Fees are non-refundable."),
            ("Where do I apply for a Denmark Schengen visa?",
             "Applications are submitted through VFS Global centres. Denmark's consular section handles decisions."),
        ]
        status_cell = '<span style="color:red;font-weight:600;">Schengen Visa Required — EUR 80</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Visa Type</th><td>Schengen Type C (short-stay)</td></tr>
<tr><th>Fee</th><td>EUR 80 (adults), EUR 40 (children 6–12)</td></tr>
<tr><th>Max Stay</th><td>90 days / 180-day period</td></tr>
<tr><th>Processing</th><td>15 working days</td></tr>
<tr><th>Apply At</th><td>VFS Global</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Denmark?</h2>
<p>Yes. {adj} passport holders must obtain a <strong>Schengen Type C short-stay visa</strong> before travelling to Denmark. The visa fee is <strong>EUR 80</strong> and processing takes <strong>15 working days</strong>. Applications are submitted via VFS Global.</p>

<h2>Schengen Visa Details</h2>
<p>A Schengen visa for Denmark allows stays of up to <strong>90 days in any 180-day period</strong> across all 27 Schengen countries. The visa is typically issued as single or double entry; multiple-entry visas may be granted to frequent travellers.</p>

<h2>How to Apply</h2>
<ol>
<li>Book an appointment at your nearest <a href="https://www.vfsglobal.com" target="_blank" rel="noopener">VFS Global</a> application centre handling Danish visa applications.</li>
<li>Complete the Schengen visa application form online or at the centre.</li>
<li>Gather all required documents and attend your appointment in person.</li>
<li>Provide biometrics (fingerprints and photograph) at the VFS centre.</li>
<li>Pay the EUR 80 fee and await the decision (15 working days).</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (min. 2 blank pages, valid at least 3 months beyond stay)</li>
<li>Completed Schengen visa application form</li>
<li>Two passport photos (35×45 mm, white background)</li>
<li>Travel insurance (min. EUR 30,000 coverage, valid across Schengen Area)</li>
<li>Bank statements — last 3 months</li>
<li>Confirmed return flight booking</li>
<li>Proof of accommodation (hotel booking or host invitation)</li>
<li>Employment letter / leave approval / business registration</li>
</ul>"""
        eeat_link = "https://www.vfsglobal.com"
        eeat_anchor = "vfsglobal.com"

    # ---- Assemble FAQ schema ----
    faq_items = "\n".join(
        f'      {{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq
    )
    faq_schema = f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n{faq_items}\n    ]}}'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>{page_title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{page_url}"/>
    <link rel="alternate" hreflang="en" href="{page_url}"/>
    <link rel="alternate" hreflang="x-default" href="{page_url}"/>
{LINKS_COMMON}
    <script type="application/ld+json">
    {faq_schema}
    </script>
</head>
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{page_title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Denmark for {display} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{eeat_link}" target="_blank" rel="noopener">{eeat_anchor}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-requirements.html">Denmark Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-fees.html">Denmark Visa Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-processing-time.html">Denmark Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="ireland-visa-for-{slug}-citizens.html">Ireland for {display} Citizens</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>
"""
    return filename, html


# ---------------------------------------------------------------------------
# Ireland generator
# ---------------------------------------------------------------------------

def ie_page(slug, display, adj, flag, demonym):
    filename = f"ireland-visa-for-{slug}-citizens.html"
    page_url = f"https://www.evisa-card.com/en/ireland-visa-for-{slug}-citizens"

    if slug in IE_EU_FREE:
        cat = "eu_free"
    elif slug in IE_VISA_FREE:
        cat = "visa_free"
    else:
        cat = "visa_required"

    if cat == "eu_free":
        page_title = f"Ireland Visa for {display} Citizens 2026 — EU Free Movement"
        meta_desc  = (f"{display} passport holders enjoy EU free movement rights in Ireland. "
                      f"No visa required. {adj} citizens may live and work freely. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Ireland?",
             f"No. {adj} nationals enjoy EU free movement rights and do not require a visa to enter or reside in Ireland."),
            (f"How long can {display} citizens stay in Ireland?",
             "EU citizens may stay and reside in Ireland indefinitely under EU free movement rules."),
            ("Is Ireland in the Schengen Area?",
             "No. Ireland is not in the Schengen Area and operates its own separate immigration system, but EU free movement rights still apply to EU citizens."),
        ]
        status_cell = '<span style="color:green;font-weight:600;">EU Free Movement — No Visa Required</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Status</th><td>EU free movement (Treaty rights)</td></tr>
<tr><th>Max Stay</th><td>Unlimited (register after 3 months)</td></tr>
<tr><th>Schengen</th><td>Ireland is NOT in Schengen</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Ireland?</h2>
<p>No. {adj} citizens benefit from <strong>EU free movement rights</strong> in Ireland. No visa is required. Ireland is not part of the Schengen Area but fully implements EU free movement rules for EU nationals.</p>

<h2>Entry Requirements for {display} Citizens</h2>
<ul>
<li>Valid {adj} passport or national ID card</li>
<li>No visa, ETIAS, or prior approval required</li>
<li>Register with local authorities after 3 months of continuous residence</li>
<li>Right to live, work, and study in Ireland</li>
</ul>

<h2>Ireland and the Common Travel Area (CTA)</h2>
<p>Ireland is part of the <strong>Common Travel Area (CTA)</strong> with the United Kingdom, the Isle of Man, and the Channel Islands. EU citizens may also travel freely to the UK via Ireland without border checks.</p>"""
        eeat_link = "https://www.irishimmigration.ie"
        eeat_anchor = "irishimmigration.ie"

    elif cat == "visa_free":
        page_title = f"Ireland Visa for {display} Citizens 2026 — Visa-Free Entry"
        meta_desc  = (f"{display} passport holders can visit Ireland visa-free for up to 90 days. "
                      f"Common Travel Area rules apply. No Schengen needed. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Ireland?",
             f"No. {adj} nationals are visa-exempt and can visit Ireland for up to 90 days without a visa."),
            ("Is Ireland part of the Schengen Area?",
             "No. Ireland has its own immigration system separate from Schengen. A Schengen visa does not grant entry to Ireland."),
            (f"How long can {display} citizens stay in Ireland?",
             "Up to 90 days per visit. Border officers can grant permission to land and determine the exact duration of your stay."),
        ]
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — Up to 90 Days</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Max Stay</th><td>90 days per visit</td></tr>
<tr><th>Schengen</th><td>Ireland is NOT in Schengen</td></tr>
<tr><th>CTA</th><td>Common Travel Area (Ireland + UK)</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Ireland?</h2>
<p>No. {adj} passport holders are <strong>visa-exempt</strong> for short stays in Ireland of up to <strong>90 days</strong>. Note that Ireland operates its own immigration system, separate from Schengen — a Schengen visa is not valid for Ireland.</p>

<h2>Key Entry Information</h2>
<ul>
<li>Valid {adj} passport required (6 months validity recommended)</li>
<li>No visa or ETIAS needed for Ireland</li>
<li>Border officers may ask about purpose of visit and onward travel</li>
<li>Sufficient funds for the duration of stay required</li>
<li>Return/onward travel ticket recommended</li>
</ul>

<h2>Ireland vs Schengen</h2>
<p>Ireland is <strong>not</strong> part of the Schengen Area. Entry to Ireland does not give you access to Schengen countries, and a Schengen visa does not cover Ireland. Ireland is part of the Common Travel Area (CTA) with the United Kingdom.</p>

<h2>Common Travel Area (CTA)</h2>
<p>The CTA allows free movement of people between Ireland and the UK. Visa-exempt visitors who enter Ireland may also travel freely to the UK (England, Scotland, Wales, Northern Ireland) and vice versa without further immigration checks.</p>"""
        eeat_link = "https://www.irishimmigration.ie"
        eeat_anchor = "irishimmigration.ie"

    else:  # visa_required
        page_title = f"Ireland Visa for {display} Citizens 2026 — Irish Visa Required"
        meta_desc  = (f"{display} passport holders need an Irish visa to visit Ireland in 2026. "
                      f"Single EUR 60 / Multiple EUR 100, 8-week processing, apply at inis.gov.ie. Updated March 2026.")
        faq = [
            (f"Do {display} citizens need a visa for Ireland?",
             f"Yes. {adj} nationals must obtain an Irish Short-Stay 'C' visa before travelling to Ireland. The fee is EUR 60 for a single-entry visa or EUR 100 for multiple-entry."),
            ("How long does Ireland visa processing take?",
             "Processing typically takes up to 8 weeks. Apply well in advance of your intended travel date."),
            ("Is Ireland part of Schengen? Can I use my Schengen visa?",
             "No. Ireland is not in the Schengen Area and does not accept Schengen visas. You must apply separately for an Irish visa at inis.gov.ie."),
        ]
        status_cell = '<span style="color:red;font-weight:600;">Irish Visa Required — EUR 60 (single) / EUR 100 (multiple)</span>'
        table_rows = f"""\
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Visa Type</th><td>Irish Short-Stay Visa (Type C)</td></tr>
<tr><th>Fee (Single)</th><td>EUR 60</td></tr>
<tr><th>Fee (Multiple)</th><td>EUR 100</td></tr>
<tr><th>Max Stay</th><td>90 days per visit</td></tr>
<tr><th>Processing</th><td>Up to 8 weeks</td></tr>
<tr><th>Apply At</th><td>inis.gov.ie</td></tr>"""
        body_content = f"""\
<h2>Do {display} Citizens Need a Visa for Ireland?</h2>
<p>Yes. {adj} passport holders must obtain an <strong>Irish Short-Stay Visa (Type C)</strong> before travelling to Ireland. Ireland is not part of the Schengen Area — a Schengen visa is not valid for entry into Ireland.</p>

<h2>Irish Visa Fees and Processing</h2>
<ul>
<li>Single-entry visa: <strong>EUR 60</strong></li>
<li>Multiple-entry visa: <strong>EUR 100</strong></li>
<li>Processing time: up to <strong>8 weeks</strong></li>
<li>Applications submitted online at <a href="https://www.inis.gov.ie" target="_blank" rel="noopener">inis.gov.ie</a></li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Create an account at <a href="https://www.inis.gov.ie/en/INIS/Pages/WP07000019" target="_blank" rel="noopener">inis.gov.ie</a> and complete the online visa application form.</li>
<li>Pay the visa fee online (EUR 60 single / EUR 100 multiple).</li>
<li>Print the application summary and post or submit your passport and supporting documents to the Irish Visa Office serving your country.</li>
<li>Await the decision (up to 8 weeks). Your passport will be returned with a visa sticker if approved.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (6+ months beyond stay, signed)</li>
<li>Completed online visa application (printed and signed)</li>
<li>Two passport-size photographs</li>
<li>Bank statements — last 6 months</li>
<li>Proof of employment / student enrolment / business registration</li>
<li>Travel insurance (recommended)</li>
<li>Confirmed return flight booking</li>
<li>Proof of accommodation in Ireland</li>
<li>Cover letter explaining purpose of visit</li>
</ul>

<h2>Ireland vs Schengen</h2>
<p>Ireland is <strong>not</strong> part of the Schengen Area. You cannot use a Schengen visa to enter Ireland, and an Irish visa does not give access to Schengen countries. You will need separate visas if you plan to visit both.</p>"""
        eeat_link = "https://www.inis.gov.ie"
        eeat_anchor = "inis.gov.ie"

    # ---- Assemble FAQ schema ----
    faq_items = "\n".join(
        f'      {{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in faq
    )
    faq_schema = f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n{faq_items}\n    ]}}'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>{page_title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{page_url}"/>
    <link rel="alternate" hreflang="en" href="{page_url}"/>
    <link rel="alternate" hreflang="x-default" href="{page_url}"/>
{LINKS_COMMON}
    <script type="application/ld+json">
    {faq_schema}
    </script>
</head>
<body>
{NAVBAR}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{page_title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Ireland for {display} Citizens</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{eeat_link}" target="_blank" rel="noopener">{eeat_anchor}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-for-{slug}-citizens.html">Denmark for {display} Citizens</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-requirements.html">Denmark Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="denmark-visa-fees.html">Denmark Fees</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER}
</body>
</html>
"""
    return filename, html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for nat in NATIONALITIES:
        slug, display, adj, flag, demonym = nat

        # Denmark
        fn_dk, html_dk = dk_page(slug, display, adj, flag, demonym)
        path_dk = os.path.join(OUT_DIR, fn_dk)
        with open(path_dk, "w", encoding="utf-8") as f:
            f.write(html_dk)
        created.append(fn_dk)

        # Ireland
        fn_ie, html_ie = ie_page(slug, display, adj, flag, demonym)
        path_ie = os.path.join(OUT_DIR, fn_ie)
        with open(path_ie, "w", encoding="utf-8") as f:
            f.write(html_ie)
        created.append(fn_ie)

    print(f"\nCreated {len(created)} files in {OUT_DIR}:\n")
    for name in sorted(created):
        print(f"  {name}")
    print(f"\nTotal: {len(created)}")


if __name__ == "__main__":
    main()
