#!/usr/bin/env python3
"""
Generate 40 HTML pages:
  spain-visa-for-{nat}-citizens.html
  italy-visa-for-{nat}-citizens.html
for 20 nationalities.
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")
os.makedirs(OUT_DIR, exist_ok=True)

# ── nationality metadata ───────────────────────────────────────────────────────
#  key        : slug used in filename
#  label      : "X Citizens" text
#  adjective  : "X travellers" text
#  flag       : ISO 3166-1 alpha-2 for flag-icons (fi-XX)
#  status     : "visa_free" | "schengen_visa" | "eu_free"

NATS = [
    # visa-free (ETIAS)
    dict(key="us",           label="US",           adjective="American",     flag="us", status="visa_free"),
    dict(key="uk",           label="UK",           adjective="British",      flag="gb", status="visa_free"),
    dict(key="canadian",     label="Canadian",     adjective="Canadian",     flag="ca", status="visa_free"),
    dict(key="japanese",     label="Japanese",     adjective="Japanese",     flag="jp", status="visa_free"),
    dict(key="australian",   label="Australian",   adjective="Australian",   flag="au", status="visa_free"),
    dict(key="korean",       label="Korean",       adjective="South Korean", flag="kr", status="visa_free"),
    dict(key="singaporean",  label="Singaporean",  adjective="Singaporean",  flag="sg", status="visa_free"),
    dict(key="brazilian",    label="Brazilian",    adjective="Brazilian",    flag="br", status="visa_free"),
    dict(key="mexican",      label="Mexican",      adjective="Mexican",      flag="mx", status="visa_free"),
    dict(key="argentinian",  label="Argentinian",  adjective="Argentinian",  flag="ar", status="visa_free"),
    # schengen visa required
    dict(key="indian",       label="Indian",       adjective="Indian",       flag="in", status="schengen_visa"),
    dict(key="chinese",      label="Chinese",      adjective="Chinese",      flag="cn", status="schengen_visa"),
    dict(key="russian",      label="Russian",      adjective="Russian",      flag="ru", status="schengen_visa"),
    dict(key="indonesian",   label="Indonesian",   adjective="Indonesian",   flag="id", status="schengen_visa"),
    dict(key="philippine",   label="Philippine",   adjective="Filipino",     flag="ph", status="schengen_visa"),
    dict(key="nigerian",     label="Nigerian",     adjective="Nigerian",     flag="ng", status="schengen_visa"),
    dict(key="south-african",label="South African",adjective="South African",flag="za", status="schengen_visa"),
    dict(key="turkish",      label="Turkish",      adjective="Turkish",      flag="tr", status="schengen_visa"),
    # EU free movement
    dict(key="french",       label="French",       adjective="French",       flag="fr", status="eu_free"),
    dict(key="german",       label="German",       adjective="German",       flag="de", status="eu_free"),
]

# ── destination metadata ───────────────────────────────────────────────────────
DESTINATIONS = [
    dict(
        key="spain",
        label="Spain",
        flag="es",
        slug_guide="visa-spain.html",
        iso2="es",
    ),
    dict(
        key="italy",
        label="Italy",
        flag="it",
        slug_guide="visa-italy.html",
        iso2="it",
    ),
]

# ── helper: related nationality links (exclude self) ──────────────────────────
RELATED_NATS = {
    "us":           ["uk", "canadian", "australian"],
    "uk":           ["us", "canadian", "australian"],
    "canadian":     ["us", "uk", "australian"],
    "japanese":     ["korean", "singaporean", "australian"],
    "australian":   ["us", "uk", "canadian"],
    "korean":       ["japanese", "singaporean", "chinese"],
    "singaporean":  ["japanese", "korean", "indonesian"],
    "brazilian":    ["argentinian", "mexican", "us"],
    "mexican":      ["us", "brazilian", "argentinian"],
    "argentinian":  ["brazilian", "mexican", "us"],
    "indian":       ["chinese", "philippine", "indonesian"],
    "chinese":      ["japanese", "korean", "indian"],
    "russian":      ["turkish", "indian", "chinese"],
    "indonesian":   ["philippine", "indian", "singaporean"],
    "philippine":   ["indonesian", "indian", "singaporean"],
    "nigerian":     ["south-african", "indian", "turkish"],
    "south-african":["nigerian", "indian", "turkish"],
    "turkish":      ["russian", "south-african", "nigerian"],
    "french":       ["german", "us", "uk"],
    "german":       ["french", "us", "uk"],
}

# ── status-dependent content blocks ───────────────────────────────────────────

def key_facts_table(dest_label, nat_label, status):
    dest_cap = dest_label
    if status == "visa_free":
        return f"""
      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {nat_label} Citizens &amp; {dest_cap}</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td>No &mdash; Visa-Free (ETIAS required from 2025)</td></tr>
          <tr><th>Max Stay</th><td>90 days in any 180-day period (Schengen)</td></tr>
          <tr><th>Fee</th><td>EUR 7 (ETIAS, adults 18&ndash;70)</td></tr>
          <tr><th>Processing Time</th><td>ETIAS: up to 4 days (usually minutes)</td></tr>
          <tr><th>Apply At</th><td>travel.ec.europa.eu (ETIAS)</td></tr>
        </tbody>
      </table>"""
    elif status == "schengen_visa":
        return f"""
      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {nat_label} Citizens &amp; {dest_cap}</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td>Yes &mdash; Schengen Visa (Short-Stay C)</td></tr>
          <tr><th>Max Stay</th><td>90 days in any 180-day period (Schengen)</td></tr>
          <tr><th>Fee</th><td>EUR 80 (adults)</td></tr>
          <tr><th>Processing Time</th><td>15 working days (apply at least 3 weeks ahead)</td></tr>
          <tr><th>Apply At</th><td>VFS Global / {dest_cap} Embassy or Consulate</td></tr>
        </tbody>
      </table>"""
    else:  # eu_free
        return f"""
      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {nat_label} Citizens &amp; {dest_cap}</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td>No &mdash; EU Free Movement (no visa, no ETIAS)</td></tr>
          <tr><th>Max Stay</th><td>Unlimited (EU/EEA citizen)</td></tr>
          <tr><th>Fee</th><td>Free</td></tr>
          <tr><th>Processing Time</th><td>N/A</td></tr>
          <tr><th>Apply At</th><td>N/A &mdash; show national ID or passport at border</td></tr>
        </tbody>
      </table>"""


def body_sections(dest, nat, status):
    dest_label = dest["label"]
    dest_flag  = dest["flag"]
    dest_guide = dest["slug_guide"]
    nat_key    = nat["key"]
    nat_label  = nat["label"]
    adj        = nat["adjective"]

    if status == "visa_free":
        return f"""
      <h2>Do {nat_label} Citizens Need a Visa for {dest_label}?</h2>
      <p>{adj} passport holders enjoy <strong>visa-free</strong> access to {dest_label} and the entire Schengen Area.
      Stays of up to <strong>90 days in any 180-day period</strong> require no advance visa.
      However, from 2025 the EU&rsquo;s <strong>ETIAS</strong> (European Travel Information and Authorisation System)
      is required before travel. ETIAS costs EUR 7 (waived under 18 and over 70), is valid for 3 years or until
      passport expiry, and is linked to your passport. Apply online at
      <a href="https://travel.ec.europa.eu/etias_en" target="_blank" rel="noopener">travel.ec.europa.eu</a>.</p>

      <h2>Entry Requirements for {nat_label} Citizens</h2>
      <ul>
        <li>Valid passport (at least 6 months validity beyond your planned return date)</li>
        <li>ETIAS authorisation (apply at travel.ec.europa.eu; valid 3 years or until passport expiry)</li>
        <li>Return or onward travel ticket</li>
        <li>Proof of accommodation for the duration of your stay</li>
        <li>Proof of sufficient funds (approx. EUR 50 per day recommended)</li>
        <li>Travel or health insurance (strongly recommended)</li>
      </ul>

      <h2>How to Obtain ETIAS Before Travelling to {dest_label}</h2>
      <ol>
        <li><strong>Apply online</strong> at <a href="https://travel.ec.europa.eu/etias_en" target="_blank" rel="noopener">travel.ec.europa.eu</a> &mdash; the form takes about 10 minutes.</li>
        <li><strong>Pay EUR 7</strong> by credit or debit card (free for travellers under 18 or over 70).</li>
        <li><strong>Receive approval</strong> &mdash; most applications are approved within minutes; allow up to 4 days.</li>
        <li><strong>Travel</strong> &mdash; your ETIAS is electronically linked to your passport. Present your passport at the border.</li>
      </ol>
      <p>For stays beyond 90 days, contact the {dest_label} Embassy or Consulate in your country to apply for a national long-stay visa.</p>

      <h2>Tips for {adj} Travellers to {dest_label} in 2026</h2>
      <ul>
        <li>ETIAS is tied to your passport &mdash; renew ETIAS if you renew your passport before travel.</li>
        <li>The 90-day Schengen limit is cumulative across <em>all</em> Schengen countries, not just {dest_label}.</li>
        <li>Keep a digital copy of your ETIAS approval email and passport data page on your phone.</li>
        <li>Purchase travel insurance covering medical emergencies and trip cancellation.</li>
        <li>Check the EU short-stay calculator at ec.europa.eu to track your Schengen days.</li>
      </ul>"""

    elif status == "schengen_visa":
        return f"""
      <h2>Do {nat_label} Citizens Need a Visa for {dest_label}?</h2>
      <p>{adj} passport holders require a <strong>Schengen Visa (Short-Stay Type C)</strong> to visit {dest_label}.
      The visa allows stays of up to <strong>90 days in any 180-day period</strong> across the entire Schengen Area.
      The standard visa fee is <strong>EUR 80</strong> and applications typically take
      <strong>15 working days</strong> to process. Apply through VFS Global or directly at the
      {dest_label} Embassy or Consulate in your country.</p>

      <h2>Required Documents for {nat_label} Citizens</h2>
      <ul>
        <li>Valid passport (at least 3 months validity beyond your intended departure date)</li>
        <li>Completed Schengen visa application form (signed)</li>
        <li>Two recent passport-size photographs (35&times;45 mm, white background)</li>
        <li>Round-trip flight reservation or travel itinerary</li>
        <li>Proof of accommodation (hotel bookings or invitation letter)</li>
        <li>Travel medical insurance (min. EUR 30,000 coverage, valid in all Schengen states)</li>
        <li>Proof of sufficient funds (bank statements for the last 3 months)</li>
        <li>Proof of employment or enrolment (letter from employer/university)</li>
        <li>Visa fee: EUR 80 (adults); EUR 40 (children 6&ndash;12)</li>
      </ul>

      <h2>How to Apply for a {dest_label} Schengen Visa</h2>
      <ol>
        <li><strong>Determine the correct consulate</strong> &mdash; apply at the {dest_label} Embassy/Consulate or VFS Global centre in {adj.split()[-1]}.</li>
        <li><strong>Book a biometric appointment</strong> &mdash; fingerprints and photo are collected at the visa application centre.</li>
        <li><strong>Submit your documents</strong> &mdash; bring originals and photocopies of all required documents plus the EUR 80 fee.</li>
        <li><strong>Wait for processing</strong> &mdash; standard processing is 15 working days; apply at least 3 weeks before travel.</li>
        <li><strong>Collect your passport</strong> &mdash; once the visa is affixed, verify the dates before travelling.</li>
      </ol>

      <h2>Tips for {adj} Travellers to {dest_label} in 2026</h2>
      <ul>
        <li>Apply early &mdash; VFS Global appointment slots can fill up weeks in advance during peak season.</li>
        <li>A multiple-entry Schengen visa lets you visit other Schengen countries on the same trip.</li>
        <li>Travel insurance must be valid for the entire Schengen Area and cover a minimum of EUR 30,000.</li>
        <li>Bank statements should show a consistent balance &mdash; sudden large deposits may raise concerns.</li>
        <li>Overstaying a Schengen visa can result in a ban from the Schengen Area for up to 5 years.</li>
      </ul>"""

    else:  # eu_free
        return f"""
      <h2>Do {nat_label} Citizens Need a Visa for {dest_label}?</h2>
      <p>As EU citizens, {adj} nationals enjoy full <strong>EU Free Movement</strong> rights.
      No visa, no ETIAS, and no prior authorisation is required to enter {dest_label}.
      {adj} citizens may live, work, and study in {dest_label} indefinitely under EU treaties.
      Simply present a valid passport or national ID card at the border.</p>

      <h2>Rights of {nat_label} Citizens in {dest_label}</h2>
      <ul>
        <li>Right to enter and reside without a visa or permit for any duration</li>
        <li>Right to work, study, and access public services on equal terms with nationals</li>
        <li>Right to be joined by family members (including non-EU family) under EU Directive 2004/38/EC</li>
        <li>Right to register as a resident after 3 months (obtain a &ldquo;Certificate of Registration&rdquo;)</li>
        <li>Right to permanent residence after 5 years of continuous lawful residence</li>
      </ul>

      <h2>What {nat_label} Citizens Should Know Before Travelling to {dest_label}</h2>
      <ol>
        <li><strong>Carry valid ID</strong> &mdash; a national ID card or passport is sufficient at all border crossings.</li>
        <li><strong>Register after 3 months</strong> &mdash; if staying longer than 3 months, register with the local municipal authority (<em>padr&oacute;n</em> in Spain / <em>Anagrafe</em> in Italy).</li>
        <li><strong>European Health Insurance Card (EHIC)</strong> &mdash; carry your EHIC for access to public healthcare.</li>
        <li><strong>No currency restrictions</strong> &mdash; the euro is the currency of both {dest_label} and your home country.</li>
      </ol>

      <h2>Tips for {adj} Travellers to {dest_label} in 2026</h2>
      <ul>
        <li>Your national ID card is sufficient &mdash; no need for a full passport for short trips within the EU.</li>
        <li>Keep your EHIC up to date to avoid unexpected medical costs abroad.</li>
        <li>If you plan to drive, your home driving licence is valid throughout the EU.</li>
        <li>For residency beyond 3 months, register locally to access full resident benefits.</li>
      </ul>"""


def faq_json(dest_label, nat_label, adj, status):
    if status == "visa_free":
        q1 = f"Do {nat_label} citizens need ETIAS for {dest_label}?"
        a1 = (f"Yes. From 2025, {adj} passport holders must obtain an ETIAS authorisation (EUR 7) "
              f"before travelling to {dest_label} and the rest of the Schengen Area, even though no visa is required.")
        q2 = f"How long can {nat_label} citizens stay in {dest_label} visa-free?"
        a2 = (f"Up to 90 days in any 180-day period across the entire Schengen Area. "
              f"This includes time spent in other Schengen countries, not just {dest_label}.")
        q3 = f"How much does ETIAS cost for {nat_label} citizens?"
        a3 = "ETIAS costs EUR 7 for adults aged 18 to 70. It is free for travellers under 18 or over 70 and is valid for 3 years or until passport expiry."
    elif status == "schengen_visa":
        q1 = f"Do {nat_label} citizens need a visa for {dest_label}?"
        a1 = (f"Yes. {adj} passport holders require a Schengen Visa (Short-Stay Type C) to visit {dest_label}. "
              f"The visa fee is EUR 80 and processing typically takes 15 working days.")
        q2 = f"Where can {nat_label} citizens apply for a {dest_label} Schengen visa?"
        a2 = (f"{adj} citizens can apply through VFS Global or directly at the {dest_label} Embassy or Consulate "
              f"in their home country. Biometric data (fingerprints and photo) must be submitted in person.")
        q3 = f"How long can {nat_label} citizens stay in {dest_label} with a Schengen visa?"
        a3 = ("A Schengen visa allows stays of up to 90 days in any 180-day period across all Schengen Area countries, "
              "not just the destination country.")
    else:
        q1 = f"Do {nat_label} citizens need a visa or ETIAS for {dest_label}?"
        a1 = (f"No. As EU citizens, {adj} nationals have the right to enter and reside in {dest_label} "
              f"without a visa, ETIAS, or any prior authorisation under EU Free Movement rules.")
        q2 = f"Can {nat_label} citizens work and live in {dest_label} permanently?"
        a2 = (f"Yes. {adj} citizens enjoy full EU Free Movement rights in {dest_label} and may live, work, "
              f"and study indefinitely. After 5 years of continuous legal residence they may apply for permanent residency.")
        q3 = f"Do {nat_label} citizens need to register if staying more than 3 months in {dest_label}?"
        a3 = (f"Yes. EU citizens staying longer than 3 months should register with the local municipal authority "
              f"to obtain a Certificate of Registration, which serves as proof of legal residency.")

    import json
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q1, "acceptedAnswer": {"@type": "Answer", "text": a1}},
            {"@type": "Question", "name": q2, "acceptedAnswer": {"@type": "Answer", "text": a2}},
            {"@type": "Question", "name": q3, "acceptedAnswer": {"@type": "Answer", "text": a3}},
        ]
    }
    return json.dumps(faq, ensure_ascii=False)


def meta_desc(dest_label, nat_label, adj, status):
    if status == "visa_free":
        desc = (f"{nat_label} citizens visit {dest_label} visa-free in 2026. "
                f"Learn about ETIAS (EUR 7), the 90-day Schengen rule and entry tips for {adj} travellers.")
    elif status == "schengen_visa":
        desc = (f"{nat_label} citizens need a Schengen visa for {dest_label} in 2026. "
                f"EUR 80 fee, 15 working days processing. Full document checklist and VFS Global tips.")
    else:
        desc = (f"{nat_label} citizens travel to {dest_label} freely under EU rules in 2026. "
                f"No visa, no ETIAS needed. Learn about EU Free Movement rights and residency registration.")
    # trim to 155 chars
    if len(desc) > 155:
        desc = desc[:152] + "..."
    return desc


def build_page(dest, nat):
    dest_label  = dest["label"]
    dest_flag   = dest["flag"]
    dest_guide  = dest["slug_guide"]
    dest_key    = dest["key"]
    nat_key     = nat["key"]
    nat_label   = nat["label"]
    nat_flag    = nat["flag"]
    adj         = nat["adjective"]
    status      = nat["status"]

    slug        = f"{dest_key}-visa-for-{nat_key}-citizens"
    filename    = f"{slug}.html"
    page_url    = f"https://www.evisa-card.com/en/{slug}"

    title = f"{dest_label} Visa for {nat_label} Citizens 2026 — Requirements, Fees & How to Apply"
    desc  = meta_desc(dest_label, nat_label, adj, status)
    faq   = faq_json(dest_label, nat_label, adj, status)
    facts = key_facts_table(dest_label, nat_label, status)
    body  = body_sections(dest, nat, status)

    # related links
    rel_keys   = RELATED_NATS.get(nat_key, [])[:3]
    rel_links  = "\n".join(
        f'        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" '
        f'href="{dest_key}-visa-for-{rk}-citizens.html">'
        f'{dest_label} Visa &mdash; {next(n["label"] for n in NATS if n["key"]==rk)} Citizens</a>'
        for rk in rel_keys
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <title>{title}</title>
    <meta name="description" content="{desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{page_url}"/>
    <link rel="alternate" hreflang="en" href="{page_url}"/>
    <link rel="alternate" hreflang="x-default" href="{page_url}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/flaticon.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {faq}
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
    <button aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-target="#ftco-nav" data-toggle="collapse" type="button">
      <span class="oi oi-menu"></span> Menu
    </button>
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
          <a class="dropdown-item active" href="/en/{filename}"><span class="fi fi-gb"></span> English</a>
          <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Fran&ccedil;ais</a>
          <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Espa&ntilde;ol</a>
          <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Portugu&ecirc;s</a>
        </div>
        </li>
      </ul>
    </div>
  </div>
</nav>

<section class="ftco-section">
  <div class="container">
    <article class="country-page">
      <h1><span class="fi fi-{nat_flag} mr-2"></span><span class="fi fi-{dest_flag} mr-2"></span>{dest_label} Visa for {nat_label} Citizens 2026</h1>
{facts}
{body}

      <div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026.</div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Guides</h3>
      <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_guide}">{dest_label} Visa Guide</a>
{rel_links}
        <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#x2192;</a>
      </div>
    </div>
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
        <p class="mt-4">&#169; 2026 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
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
<script src="../js/jquery-migrate-3.0.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/jquery.easing.1.3.js"></script>
<script src="../js/jquery.waypoints.min.js"></script>
<script src="../js/jquery.stellar.min.js"></script>
<script src="../js/owl.carousel.min.js"></script>
<script src="../js/jquery.magnific-popup.min.js"></script>
<script src="../js/jquery.animateNumber.min.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""
    return filename, html


# ── main ──────────────────────────────────────────────────────────────────────
def main():
    created = []
    for dest in DESTINATIONS:
        for nat in NATS:
            filename, html = build_page(dest, nat)
            path = os.path.join(OUT_DIR, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  created: {filename}")

    print(f"\nTotal files created: {len(created)}")
    assert len(created) == 40, f"Expected 40 files, got {len(created)}"
    print("All 40 files verified.")


if __name__ == "__main__":
    main()
