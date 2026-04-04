"""
gen_nat_netherlands_belgium.py
Generate 40 HTML pages:
  netherlands-visa-for-{nat}-citizens.html  (20 files)
  belgium-visa-for-{nat}-citizens.html      (20 files)
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATIONALITIES = [
    # slug           label           flag_code  passport_label
    ("us",           "US",           "us",       "US"),
    ("uk",           "UK",           "gb",       "British"),
    ("canadian",     "Canadian",     "ca",       "Canadian"),
    ("french",       "French",       "fr",       "French"),
    ("german",       "German",       "de",       "German"),
    ("japanese",     "Japanese",     "jp",       "Japanese"),
    ("australian",   "Australian",   "au",       "Australian"),
    ("indian",       "Indian",       "in",       "Indian"),
    ("chinese",      "Chinese",      "cn",       "Chinese"),
    ("russian",      "Russian",      "ru",       "Russian"),
    ("brazilian",    "Brazilian",    "br",       "Brazilian"),
    ("mexican",      "Mexican",      "mx",       "Mexican"),
    ("south-african","South African","za",       "South African"),
    ("nigerian",     "Nigerian",     "ng",       "Nigerian"),
    ("korean",       "Korean",       "kr",       "Korean"),
    ("singaporean",  "Singaporean",  "sg",       "Singaporean"),
    ("indonesian",   "Indonesian",   "id",       "Indonesian"),
    ("philippine",   "Philippine",   "ph",       "Philippine"),
    ("turkish",      "Turkish",      "tr",       "Turkish"),
    ("argentinian",  "Argentinian",  "ar",       "Argentinian"),
]

# ---------------------------------------------------------------------------
# Visa status categories
# ---------------------------------------------------------------------------
# Visa-free / ETIAS (no Schengen visa needed, but ETIAS required from 2025)
ETIAS = {"us", "uk", "canadian", "japanese", "australian", "korean",
         "singaporean", "brazilian", "mexican", "argentinian"}

# EU free movement (no visa, no ETIAS)
EU_FREE = {"french", "german"}

# Schengen visa required EUR 80 / 15 working days / VFS
VISA_REQUIRED = {"indian", "chinese", "russian", "indonesian", "philippine",
                 "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# Country data
# ---------------------------------------------------------------------------
COUNTRIES = [
    {
        "slug":        "netherlands",
        "name":        "Netherlands",
        "flag":        "nl",
        "schengen":    True,
        "embassy_url": "https://www.netherlandsworldwide.nl/",
        "vfs_url":     "https://www.vfsglobal.com/netherlands/",
        "req_url":     "netherlands-visa-requirements.html",
        "fees_url":    "netherlands-visa-fees.html",
        "time_url":    "netherlands-visa-processing-time.html",
        "overview_url":"visa-netherlands.html",
    },
    {
        "slug":        "belgium",
        "name":        "Belgium",
        "flag":        "be",
        "schengen":    True,
        "embassy_url": "https://diplomatie.belgium.be/",
        "vfs_url":     "https://www.vfsglobal.com/belgium/",
        "req_url":     "belgium-visa-requirements.html",
        "fees_url":    "belgium-visa-fees.html",
        "time_url":    "belgium-visa-processing-time.html",
        "overview_url":"visa-belgium.html",
    },
]

# ---------------------------------------------------------------------------
# Helper: determine visa status block
# ---------------------------------------------------------------------------
def visa_info(nat_slug, country):
    cname = country["name"]

    if nat_slug in EU_FREE:
        return {
            "status_label": "No Visa Required — EU Free Movement",
            "status_color": "green",
            "visa_type":    "EU Free Movement",
            "fee":          "Free",
            "max_stay":     "Unlimited (EU citizens)",
            "processing":   "N/A",
            "apply_at":     "No application needed",
            "category":     "eu_free",
        }
    elif nat_slug in ETIAS:
        return {
            "status_label": "Visa-Free — ETIAS Required",
            "status_color": "orange",
            "visa_type":    "ETIAS (European Travel Information and Authorisation System)",
            "fee":          "EUR 7",
            "max_stay":     "90 days in any 180-day period",
            "processing":   "Instant to 96 hours",
            "apply_at":     "travel-europe.europa.eu/etias",
            "category":     "etias",
        }
    else:  # VISA_REQUIRED
        return {
            "status_label": "Schengen Visa Required — EUR 80",
            "status_color": "red",
            "visa_type":    f"Schengen Short-Stay Visa (Type C) — {cname} embassy / VFS",
            "fee":          "EUR 80",
            "max_stay":     "90 days in any 180-day period",
            "processing":   "15 working days",
            "apply_at":     f"VFS Global / {cname} Embassy or Consulate",
            "category":     "visa_required",
        }

# ---------------------------------------------------------------------------
# FAQ content per category
# ---------------------------------------------------------------------------
def faq_json(nat_label, country_name, vi):
    cname = country_name
    cat = vi["category"]

    if cat == "eu_free":
        q1 = f"Do {nat_label} citizens need a visa for {cname}?"
        a1 = (f"No. {nat_label} citizens are EU nationals and benefit from EU free movement. "
              f"No visa or ETIAS is required to live, work, or travel in {cname}.")
        q2 = f"How long can {nat_label} citizens stay in {cname}?"
        a2 = f"As EU citizens, {nat_label} nationals can reside in {cname} indefinitely under EU free movement rights."
        q3 = f"Do {nat_label} citizens need any travel authorisation for {cname}?"
        a3 = f"No. {nat_label} passport holders can travel freely to {cname} with a valid national ID card or passport."
    elif cat == "etias":
        q1 = f"Do {nat_label} citizens need a visa for {cname}?"
        a1 = (f"No visa is required. However, {nat_label} passport holders must obtain ETIAS "
              f"(European Travel Information and Authorisation System) before travelling to {cname}. "
              f"The fee is EUR 7 and approval is usually instant.")
        q2 = "What is ETIAS and how do I apply?"
        a2 = ("ETIAS is a pre-travel authorisation for visa-exempt travellers to the Schengen Area. "
              "Apply online at travel-europe.europa.eu/etias before your trip. Processing is usually instant "
              "but can take up to 96 hours. Cost is EUR 7.")
        q3 = f"How long can {nat_label} citizens stay in {cname} with ETIAS?"
        a3 = ("With a valid ETIAS you may stay up to 90 days in any 180-day period across the entire Schengen Area, "
              f"including {cname}. ETIAS is valid for 3 years or until your passport expires.")
    else:  # visa_required
        q1 = f"Do {nat_label} citizens need a visa for {cname}?"
        a1 = (f"Yes. {nat_label} passport holders must apply for a Schengen Short-Stay Visa (Type C) "
              f"at the {cname} embassy or through VFS Global. The fee is EUR 80.")
        q2 = f"What is the {cname} Schengen visa fee for {nat_label} citizens?"
        a2 = (f"The standard Schengen visa fee is EUR 80 for adult applicants. "
              "Children aged 6–11 pay EUR 40. Children under 6 are exempt.")
        q3 = f"How long does {cname} Schengen visa processing take?"
        a3 = ("Processing typically takes 15 working days. Apply at least 6 weeks before your travel date. "
              "You may apply up to 6 months in advance.")

    return (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n'
        f'  {{"@type":"Question","name":"{q1}","acceptedAnswer":{{"@type":"Answer","text":"{a1}"}}}},\n'
        f'  {{"@type":"Question","name":"{q2}","acceptedAnswer":{{"@type":"Answer","text":"{a2}"}}}},\n'
        f'  {{"@type":"Question","name":"{q3}","acceptedAnswer":{{"@type":"Answer","text":"{a3}"}}}}\n'
        ']}'
    )

def howto_json(nat_label, country_name, vi):
    cat = vi["category"]
    cname = country_name

    if cat == "eu_free":
        steps = [
            f'Ensure your {nat_label} passport or national ID card is valid for your trip to {cname}.',
            f'Book flights and accommodation — no visa or pre-travel authorisation is needed.',
            f'Travel to {cname} and present your EU passport or ID card at border control.',
        ]
        name = f"How to travel to {cname} as a {nat_label} citizen"
        desc = f"{nat_label} EU citizens do not need a visa to visit {cname}."
    elif cat == "etias":
        steps = [
            f'Gather your valid passport (must have at least 3 months validity beyond your planned stay).',
            'Visit travel-europe.europa.eu/etias and complete the online ETIAS application form.',
            'Pay the EUR 7 ETIAS fee by credit or debit card.',
            'Receive your ETIAS authorisation by email — usually within seconds to 96 hours.',
            f'Travel to {cname} with your approved ETIAS and valid passport.',
        ]
        name = f"How to get ETIAS for {cname} as a {nat_label} citizen"
        desc = f"{nat_label} citizens need ETIAS to visit {cname} visa-free."
    else:
        steps = [
            f'Contact the {cname} embassy or VFS Global in your country to book a visa appointment.',
            'Complete the Schengen visa application form (available on the embassy or VFS website).',
            f'Pay the EUR 80 visa fee at the time of appointment.',
            'Submit your documents: passport, photos, travel insurance, bank statements, itinerary.',
            'Attend the appointment; biometric data (fingerprints and photo) will be collected.',
            'Await a decision — typically 15 working days. Collect your passport with the visa sticker.',
        ]
        name = f"How to apply for a {cname} Schengen visa as a {nat_label} citizen"
        desc = f"{nat_label} citizens must apply for a Schengen visa to visit {cname}."

    steps_json = ",\n    ".join(
        f'{{"@type":"HowToStep","text":"{s}"}}'
        for s in steps
    )
    return (
        '{"@context":"https://schema.org","@type":"HowTo",\n'
        f' "name":"{name}",\n'
        f' "description":"{desc}",\n'
        f' "step":[\n    {steps_json}\n  ]}}'
    )

# ---------------------------------------------------------------------------
# Body content per category
# ---------------------------------------------------------------------------
def body_content(nat_slug, nat_label, country, vi):
    cname = country["name"]
    cat = vi["category"]
    nat_flag = [n[2] for n in NATIONALITIES if n[0] == nat_slug][0]
    nat_passport = [n[3] for n in NATIONALITIES if n[0] == nat_slug][0]

    if cat == "eu_free":
        h2_intro = f"EU Free Movement: {nat_label} Citizens in {cname}"
        p_intro = (
            f'<span class="fi fi-{nat_flag}"></span> <span class="fi fi-{country["flag"]}"></span> '
            f'{nat_passport} citizens are European Union nationals and enjoy the right to free movement across '
            f'all EU/EEA member states, including <strong>{cname}</strong>. No visa, no ETIAS, '
            f'and no prior authorisation is required.'
        )
        details_h2 = "What EU Free Movement Means"
        details_ul = (
            "<li>No visa required — enter with a valid EU passport or national ID card</li>\n"
            "<li>No ETIAS required</li>\n"
            f"<li>Unlimited stay in {cname} as an EU citizen</li>\n"
            "<li>Right to work, study, and reside</li>\n"
            "<li>No travel insurance requirement at border</li>"
        )
        apply_h2 = f"Travelling to {cname} as a {nat_label} Citizen"
        apply_steps = (
            f"<li>Ensure your {nat_passport} passport or national ID card is valid for your trip.</li>\n"
            f"<li>Book your flights and accommodation in {cname} — no pre-approval needed.</li>\n"
            f"<li>Present your EU document at the border. Entry is automatic for EU citizens.</li>"
        )
        docs_h2 = "Documents to Carry"
        docs_ul = (
            "<li>Valid EU passport or national identity card</li>\n"
            "<li>Proof of onward/return travel (recommended)</li>\n"
            "<li>Travel insurance (recommended but not mandatory)</li>"
        )
        eeat_url = country["embassy_url"]
        eeat_text = f"Always carry a valid EU travel document. For residency registration in {cname}, contact local municipal authorities."

    elif cat == "etias":
        h2_intro = f"Does a {nat_label} Citizen Need a Visa for {cname}?"
        p_intro = (
            f'<span class="fi fi-{nat_flag}"></span> <span class="fi fi-{country["flag"]}"></span> '
            f'{nat_passport} passport holders do <strong>not need a Schengen visa</strong> to visit '
            f'<strong>{cname}</strong>. However, since the ETIAS system launched, travellers must obtain '
            f'<strong>ETIAS</strong> (European Travel Information and Authorisation System) before boarding. '
            f'The fee is <strong>EUR 7</strong> and approval is usually instant.'
        )
        details_h2 = "ETIAS Key Details"
        details_ul = (
            "<li>Cost: <strong>EUR 7</strong></li>\n"
            "<li>Validity: 3 years (or until passport expiry, whichever comes first)</li>\n"
            "<li>Entries: Multiple</li>\n"
            f"<li>Stay: Up to 90 days in any 180-day period across the Schengen Area (including {cname})</li>\n"
            "<li>Processing: Usually instant; up to 96 hours in some cases</li>\n"
            "<li>Required: Before boarding — airlines check ETIAS at check-in</li>"
        )
        apply_h2 = "How to Apply for ETIAS"
        apply_steps = (
            "<li>Visit <a href='https://travel-europe.europa.eu/etias' target='_blank' rel='noopener'>travel-europe.europa.eu/etias</a>.</li>\n"
            "<li>Complete the online application form with your passport details.</li>\n"
            "<li>Pay the EUR 7 fee by credit or debit card.</li>\n"
            "<li>Receive your ETIAS authorisation by email (usually within minutes).</li>\n"
            f"<li>Travel to {cname} — present your passport at border control. ETIAS is electronically linked.</li>"
        )
        docs_h2 = "Documents Required for ETIAS"
        docs_ul = (
            "<li>Valid passport with at least 3 months validity beyond your intended stay</li>\n"
            "<li>Email address for ETIAS confirmation</li>\n"
            "<li>Credit or debit card for the EUR 7 fee</li>\n"
            "<li>Return or onward travel ticket (recommended)</li>\n"
            "<li>Travel/health insurance (recommended)</li>"
        )
        eeat_url = "https://travel-europe.europa.eu/etias"
        eeat_text = f"Always verify current ETIAS requirements before travel to {cname}."

    else:  # visa_required
        h2_intro = f"{nat_label} Citizens Visa Requirement for {cname}"
        p_intro = (
            f'<span class="fi fi-{nat_flag}"></span> <span class="fi fi-{country["flag"]}"></span> '
            f'{nat_passport} passport holders must obtain a <strong>Schengen Short-Stay Visa (Type C)</strong> '
            f'before travelling to <strong>{cname}</strong>. The visa fee is <strong>EUR 80</strong>, '
            f'processing takes <strong>15 working days</strong>, and applications are submitted through '
            f'<strong>VFS Global</strong> or the {cname} embassy in your country.'
        )
        details_h2 = "Schengen Visa Key Details"
        details_ul = (
            "<li>Fee: <strong>EUR 80</strong> (adults); EUR 40 (children 6–11); free (under 6)</li>\n"
            "<li>Processing time: 15 working days</li>\n"
            "<li>Max stay: 90 days in any 180-day period</li>\n"
            "<li>Valid across the entire Schengen Area (27 countries)</li>\n"
            "<li>Apply through: VFS Global or the {cname} embassy</li>\n"
            "<li>Biometrics: Required at appointment</li>".replace("{cname}", cname)
        )
        apply_h2 = f"How to Apply for a {cname} Schengen Visa"
        apply_steps = (
            f"<li>Book an appointment at <a href='{country['vfs_url']}' target='_blank' rel='noopener'>VFS Global</a> or the {cname} embassy in your country.</li>\n"
            "<li>Download and complete the Schengen visa application form.</li>\n"
            "<li>Pay the EUR 80 visa fee at the VFS centre or embassy.</li>\n"
            "<li>Attend your appointment and provide biometric data (fingerprints and photograph).</li>\n"
            "<li>Submit all supporting documents (see list below).</li>\n"
            "<li>Wait 15 working days for a decision. Collect your passport with visa sticker.</li>"
        )
        docs_h2 = "Required Documents"
        docs_ul = (
            "<li>Valid passport (at least 3 months validity beyond travel dates; 2 blank pages)</li>\n"
            "<li>Two recent passport-sized photos (ICAO standard)</li>\n"
            "<li>Completed Schengen visa application form</li>\n"
            "<li>Travel insurance (minimum EUR 30,000 cover) for the entire Schengen Area</li>\n"
            "<li>Bank statements (last 3–6 months)</li>\n"
            "<li>Proof of accommodation in {cname} (hotel bookings or invitation letter)</li>\n"
            "<li>Round-trip flight reservation</li>\n"
            "<li>Proof of employment, business registration, or student status</li>".replace("{cname}", cname)
        )
        eeat_url = country["vfs_url"]
        eeat_text = f"Verify current requirements at the {cname} embassy or VFS Global before applying."

    return (
        h2_intro, p_intro, details_h2, details_ul,
        apply_h2, apply_steps, docs_h2, docs_ul,
        eeat_url, eeat_text
    )

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
def build_page(nat_slug, nat_label, nat_flag_code, country):
    cname = country["name"]
    cflag = country["flag"]
    cslug = country["slug"]
    vi = visa_info(nat_slug, country)

    filename = f"{cslug}-visa-for-{nat_slug}-citizens.html"
    slug_no_ext = f"{cslug}-visa-for-{nat_slug}-citizens"

    title = f"{cname} Visa for {nat_label} Citizens 2026"
    cat = vi["category"]

    if cat == "eu_free":
        desc = (f"{nat_label} citizens (EU nationals) do not need a visa for {cname}. "
                f"EU free movement applies — unlimited stay. Updated March 2026.")
    elif cat == "etias":
        desc = (f"{nat_label} passport holders visiting {cname} in 2026: visa-free with ETIAS, "
                f"EUR 7, instant approval, 90 days. Updated March 2026.")
    else:
        desc = (f"{nat_label} passport holders visiting {cname} in 2026: Schengen visa required, "
                f"EUR 80, 15 working days, VFS Global. Updated March 2026.")

    (h2_intro, p_intro, details_h2, details_ul,
     apply_h2, apply_steps, docs_h2, docs_ul,
     eeat_url, eeat_text) = body_content(nat_slug, nat_label, country, vi)

    faq = faq_json(nat_label, cname, vi)
    howto = howto_json(nat_label, cname, vi)

    status_color = vi["status_color"]
    status_label = vi["status_label"]
    visa_type    = vi["visa_type"]
    fee          = vi["fee"]
    max_stay     = vi["max_stay"]
    processing   = vi["processing"]
    apply_at     = vi["apply_at"]

    html = f"""<!DOCTYPE html>
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
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug_no_ext}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug_no_ext}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug_no_ext}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {faq}
    </script>
    <script type="application/ld+json">
    {howto}
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
                        <a class="dropdown-item active" href="/en/{filename}"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{cflag}"></span> <span class="fi fi-{nat_flag_code}"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — {cname} for {nat_label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td><span style="color:{status_color};font-weight:600;">{status_label}</span></td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>{max_stay}</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
</tbody>
</table>

<h2>{h2_intro}</h2>
<p>{p_intro}</p>

<h2>{details_h2}</h2>
<ul>
{details_ul}
</ul>

<h2>{apply_h2}</h2>
<ol>
{apply_steps}
</ol>

<h2>{docs_h2}</h2>
<ul>
{docs_ul}
</ul>

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. {eeat_text} Always verify at <a href="{eeat_url}" target="_blank" rel="noopener">{eeat_url}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country['overview_url']}">{cname} Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country['req_url']}">{cname} Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country['fees_url']}">{cname} Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country['time_url']}">{cname} Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
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
    return filename, html

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for country in COUNTRIES:
        for nat_slug, nat_label, nat_flag_code, _nat_passport in NATIONALITIES:
            filename, html = build_page(nat_slug, nat_label, nat_flag_code, country)
            out_path = os.path.join(OUT_DIR, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  Created: {filename}")

    print(f"\nDone. {len(created)} files written to {OUT_DIR}")
    return created

if __name__ == "__main__":
    main()
