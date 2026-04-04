#!/usr/bin/env python3
"""
Generate 40 HTML files:
  poland-visa-for-{nat}-citizens.html   (20 nationalities)
  hungary-visa-for-{nat}-citizens.html  (20 nationalities)
Output dir: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ── nationality metadata ──────────────────────────────────────────────────────
NAT_META = {
    "us":           {"label": "US",            "adj": "American",      "fi": "us", "passport": "US passport"},
    "uk":           {"label": "UK",            "adj": "British",       "fi": "gb", "passport": "British passport"},
    "canadian":     {"label": "Canadian",      "adj": "Canadian",      "fi": "ca", "passport": "Canadian passport"},
    "french":       {"label": "French",        "adj": "French",        "fi": "fr", "passport": "French passport"},
    "german":       {"label": "German",        "adj": "German",        "fi": "de", "passport": "German passport"},
    "japanese":     {"label": "Japanese",      "adj": "Japanese",      "fi": "jp", "passport": "Japanese passport"},
    "australian":   {"label": "Australian",    "adj": "Australian",    "fi": "au", "passport": "Australian passport"},
    "indian":       {"label": "Indian",        "adj": "Indian",        "fi": "in", "passport": "Indian passport"},
    "chinese":      {"label": "Chinese",       "adj": "Chinese",       "fi": "cn", "passport": "Chinese passport"},
    "russian":      {"label": "Russian",       "adj": "Russian",       "fi": "ru", "passport": "Russian passport"},
    "brazilian":    {"label": "Brazilian",     "adj": "Brazilian",     "fi": "br", "passport": "Brazilian passport"},
    "mexican":      {"label": "Mexican",       "adj": "Mexican",       "fi": "mx", "passport": "Mexican passport"},
    "south-african":{"label": "South African", "adj": "South African", "fi": "za", "passport": "South African passport"},
    "nigerian":     {"label": "Nigerian",      "adj": "Nigerian",      "fi": "ng", "passport": "Nigerian passport"},
    "korean":       {"label": "Korean",        "adj": "South Korean",  "fi": "kr", "passport": "South Korean passport"},
    "singaporean":  {"label": "Singaporean",   "adj": "Singaporean",   "fi": "sg", "passport": "Singaporean passport"},
    "indonesian":   {"label": "Indonesian",    "adj": "Indonesian",    "fi": "id", "passport": "Indonesian passport"},
    "philippine":   {"label": "Philippine",    "adj": "Filipino",      "fi": "ph", "passport": "Philippine passport"},
    "turkish":      {"label": "Turkish",       "adj": "Turkish",       "fi": "tr", "passport": "Turkish passport"},
    "argentinian":  {"label": "Argentinian",   "adj": "Argentinian",   "fi": "ar", "passport": "Argentinian passport"},
}

# ── visa-status groups ────────────────────────────────────────────────────────
VISA_FREE_ETIAS   = {"us","uk","canadian","japanese","australian","korean","singaporean","brazilian","mexican","argentinian"}
EU_FREE_MOVEMENT  = {"french","german"}
SCHENGEN_VISA     = {"indian","chinese","russian","indonesian","philippine","nigerian","south-african","turkish"}

# ── destination metadata ──────────────────────────────────────────────────────
DEST = {
    "poland": {
        "name": "Poland",
        "fi":   "pl",
        "capital": "Warsaw",
        "embassy_url": "https://www.gov.pl/web/dyplomacja-en",
        "vfs_url":     "https://www.vfsglobal.com/poland/",
        "currency":    "PLN (Polish Złoty)",
        "schengen":    True,
    },
    "hungary": {
        "name": "Hungary",
        "fi":   "hu",
        "capital": "Budapest",
        "embassy_url": "https://konzuliszolgalat.kormany.hu/en",
        "vfs_url":     "https://www.vfsglobal.com/hungary/",
        "currency":    "HUF (Hungarian Forint)",
        "schengen":    True,
    },
}

# ── FAQ helpers ───────────────────────────────────────────────────────────────

def faq_etias(dest_name, nat_adj):
    return [
        (f"Do {nat_adj} citizens need a visa for {dest_name}?",
         f"No. {nat_adj} passport holders can enter {dest_name} visa-free for up to 90 days in any 180-day period. "
         f"However, from mid-2025 the EU ETIAS (European Travel Information and Authorisation System) is required before travel. "
         f"ETIAS costs EUR 7 and is valid for 3 years."),
        ("What is ETIAS?",
         "ETIAS is the EU's electronic travel authorisation for nationals of visa-exempt countries. "
         "It is not a visa — it is a pre-travel check linked to your passport. "
         "It is valid for 3 years or until your passport expires, and costs EUR 7."),
        (f"How long can {nat_adj} citizens stay in {dest_name}?",
         f"{nat_adj} passport holders may stay up to 90 days in any 180-day period across the entire Schengen Area, "
         f"including {dest_name}."),
    ]

def faq_eu(dest_name, nat_adj):
    return [
        (f"Do {nat_adj} citizens need a visa for {dest_name}?",
         f"No. As EU citizens, {nat_adj} passport holders enjoy free movement rights and can live, work and travel "
         f"in {dest_name} indefinitely without a visa or ETIAS."),
        ("Do EU citizens need ETIAS?",
         "No. ETIAS applies only to non-EU nationals from visa-exempt countries. EU citizens are exempt."),
        (f"Can {nat_adj} citizens work in {dest_name}?",
         f"Yes. {nat_adj} citizens have the right to work, study and reside in {dest_name} under EU free-movement rules."),
    ]

def faq_schengen(dest_name, nat_adj, embassy_url):
    return [
        (f"Do {nat_adj} citizens need a visa for {dest_name}?",
         f"Yes. {nat_adj} passport holders must obtain a Schengen visa before travelling to {dest_name}. "
         f"The standard fee is EUR 80 and processing takes approximately 15 working days through VFS Global."),
        ("How do I apply for the Schengen visa?",
         f"Submit your application through VFS Global in your home country. You will need a valid passport, completed application form, "
         f"2 photos, travel insurance, bank statements, proof of accommodation and a round-trip ticket."),
        (f"How long can {nat_adj} citizens stay in {dest_name} on a Schengen visa?",
         "A standard short-stay Schengen visa allows up to 90 days within any 180-day period across all Schengen member states."),
    ]

# ── status block builder ──────────────────────────────────────────────────────

def status_block(nat_key, dest):
    dest_name = dest["name"]
    nat = NAT_META[nat_key]
    nat_adj = nat["adj"]
    nat_label = nat["label"]

    if nat_key in EU_FREE_MOVEMENT:
        status_badge = '<span style="color:green;font-weight:700;">✓ EU Free Movement — No Visa Required</span>'
        visa_type_row = "<tr><th>Visa Type</th><td>EU Free Movement</td></tr>"
        fee_row = "<tr><th>Fee</th><td>None</td></tr>"
        max_stay_row = "<tr><th>Max Stay</th><td>Unlimited</td></tr>"
        processing_row = "<tr><th>Processing</th><td>N/A</td></tr>"
        apply_row = f"<tr><th>More Info</th><td><a href='{dest['embassy_url']}' target='_blank' rel='noopener'>{dest_name} official site</a></td></tr>"

        intro = (
            f"As EU citizens, <strong>{nat_adj} passport holders</strong> enjoy full free-movement rights within the European Union. "
            f"No visa, no ETIAS, and no restriction on length of stay in <strong>{dest_name}</strong>."
        )
        details_heading = "EU Free Movement — What It Means"
        details_body = f"""
<p>{nat_adj} citizens may enter, reside, work and study in {dest_name} without any prior authorisation.
Simply present your valid {nat["passport"]} or EU national identity card at the border.</p>
<ul>
<li>No visa required</li>
<li>No ETIAS required</li>
<li>No maximum stay limit</li>
<li>Right to work and study</li>
<li>Access to healthcare and social benefits under EU rules</li>
</ul>
"""
        how_to = f"""
<p>No application is required. Travel to {dest_name} with your valid {nat["passport"]} or EU national ID card.</p>
<ol>
<li>Ensure your passport or national ID card is valid.</li>
<li>Travel freely — no visa or prior authorisation needed.</li>
<li>For long-term residence (&gt;3 months), register with local authorities in {dest_name}.</li>
</ol>
"""
        docs = """
<ul>
<li>Valid EU passport or national identity card</li>
</ul>
"""
        faqs = faq_eu(dest_name, nat_adj)

    elif nat_key in VISA_FREE_ETIAS:
        status_badge = '<span style="color:#e67e00;font-weight:700;">✓ Visa-Free — ETIAS Required (from 2025)</span>'
        visa_type_row = "<tr><th>Visa Type</th><td>ETIAS (Travel Authorisation)</td></tr>"
        fee_row = "<tr><th>Fee</th><td>EUR 7</td></tr>"
        max_stay_row = "<tr><th>Max Stay</th><td>90 days / 180-day period</td></tr>"
        processing_row = "<tr><th>Processing</th><td>Minutes to 4 days</td></tr>"
        apply_row = "<tr><th>Apply At</th><td>travel-europe.europa.eu/etias</td></tr>"

        intro = (
            f"<strong>{nat_adj} passport holders</strong> can visit <strong>{dest_name}</strong> visa-free for up to "
            f"<strong>90 days</strong> in any 180-day period. From 2025, an ETIAS travel authorisation (EUR 7, valid 3 years) "
            f"is required before entry."
        )
        details_heading = "ETIAS — Key Details"
        details_body = f"""
<p>ETIAS (European Travel Information and Authorisation System) is the EU's mandatory pre-travel check for visa-exempt travellers.
It is <strong>not a visa</strong> — it is linked to your passport electronically.</p>
<ul>
<li>Cost: <strong>EUR 7</strong></li>
<li>Validity: 3 years or until passport expiry</li>
<li>Covers all Schengen Area countries including {dest_name}</li>
<li>Processing: usually within minutes; up to 4 days</li>
<li>Multiple entries permitted</li>
<li>Apply online at: <a href="https://travel-europe.europa.eu/etias_en" target="_blank" rel="noopener">travel-europe.europa.eu/etias</a></li>
</ul>
"""
        how_to = f"""
<ol>
<li>Apply online for ETIAS at <a href="https://travel-europe.europa.eu/etias_en" target="_blank" rel="noopener">travel-europe.europa.eu/etias</a>.</li>
<li>Pay the EUR 7 fee (under 18 and over 70 are exempt).</li>
<li>Wait for your authorisation (usually within minutes).</li>
<li>Travel to {dest_name} — ETIAS is checked electronically at the border.</li>
</ol>
"""
        docs = """
<ul>
<li>Valid passport (6+ months validity recommended)</li>
<li>Valid ETIAS authorisation linked to your passport</li>
<li>Proof of sufficient funds</li>
<li>Return/onward travel ticket (may be requested)</li>
</ul>
"""
        faqs = faq_etias(dest_name, nat_adj)

    else:  # SCHENGEN_VISA
        status_badge = '<span style="color:red;font-weight:700;">Visa Required — EUR 80 Schengen Visa</span>'
        visa_type_row = "<tr><th>Visa Type</th><td>Schengen Short-Stay Visa (Type C)</td></tr>"
        fee_row = "<tr><th>Fee</th><td>EUR 80</td></tr>"
        max_stay_row = "<tr><th>Max Stay</th><td>90 days / 180-day period</td></tr>"
        processing_row = "<tr><th>Processing</th><td>15 working days</td></tr>"
        apply_row = f"<tr><th>Apply Via</th><td><a href='{dest['vfs_url']}' target='_blank' rel='noopener'>VFS Global</a></td></tr>"

        intro = (
            f"<strong>{nat_adj} passport holders</strong> must obtain a <strong>Schengen visa (Type C)</strong> before travelling "
            f"to <strong>{dest_name}</strong>. The standard fee is <strong>EUR 80</strong> and processing takes approximately "
            f"<strong>15 working days</strong> through VFS Global."
        )
        details_heading = "Schengen Visa — Key Details"
        details_body = f"""
<p>A Schengen short-stay visa (Type C) allows {nat_adj} passport holders to visit {dest_name} and the entire Schengen Area
for up to <strong>90 days</strong> in any 180-day period.</p>
<ul>
<li>Fee: <strong>EUR 80</strong></li>
<li>Processing time: approximately <strong>15 working days</strong></li>
<li>Apply through: <a href="{dest['vfs_url']}" target="_blank" rel="noopener">VFS Global</a></li>
<li>Valid for: Schengen Area (26 countries)</li>
<li>Maximum stay: 90 days / 180-day period</li>
</ul>
"""
        how_to = f"""
<ol>
<li>Book an appointment at your nearest <a href="{dest['vfs_url']}" target="_blank" rel="noopener">VFS Global</a> application centre.</li>
<li>Complete the Schengen visa application form.</li>
<li>Pay the EUR 80 visa fee at the centre.</li>
<li>Submit all required documents (see list below).</li>
<li>Provide biometric data (fingerprints and photo) at the centre.</li>
<li>Wait approximately 15 working days for a decision.</li>
<li>Collect your passport with the visa sticker.</li>
</ol>
"""
        docs = """
<ul>
<li>Valid passport (issued within the last 10 years, valid for 3+ months beyond intended stay)</li>
<li>2 recent passport-size photos (35×45 mm, white background)</li>
<li>Completed Schengen visa application form</li>
<li>Travel insurance (min. EUR 30,000 medical cover for the entire Schengen Area)</li>
<li>Bank statements (last 3–6 months, showing sufficient funds)</li>
<li>Proof of accommodation (hotel bookings or invitation letter)</li>
<li>Return/round-trip flight ticket or itinerary</li>
<li>Proof of employment (employment letter, payslips, or business registration)</li>
<li>If employed: employer's leave approval letter</li>
</ul>
"""
        faqs = faq_schengen(dest_name, nat_adj, dest["embassy_url"])

    return {
        "status_badge": status_badge,
        "visa_type_row": visa_type_row,
        "fee_row": fee_row,
        "max_stay_row": max_stay_row,
        "processing_row": processing_row,
        "apply_row": apply_row,
        "intro": intro,
        "details_heading": details_heading,
        "details_body": details_body,
        "how_to": how_to,
        "docs": docs,
        "faqs": faqs,
    }

# ── FAQ JSON-LD builder ───────────────────────────────────────────────────────

def faq_jsonld(faqs):
    items = []
    for q, a in faqs:
        # escape quotes
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"')
        items.append(
            f'{{"@type":"Question","name":"{q_esc}",'
            f'"acceptedAnswer":{{"@type":"Answer","text":"{a_esc}"}}}}'
        )
    inner = ",\n      ".join(items)
    return (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n      '
        + inner
        + "\n    ]}"
    )

# ── FAQ HTML builder ──────────────────────────────────────────────────────────

def faq_html(faqs):
    parts = ['<div class="faq-section mt-5"><h2>Frequently Asked Questions</h2>']
    for q, a in faqs:
        parts.append(f"<h3>{q}</h3><p>{a}</p>")
    parts.append("</div>")
    return "\n".join(parts)

# ── main page builder ─────────────────────────────────────────────────────────

def build_page(dest_key, nat_key):
    dest = DEST[dest_key]
    nat  = NAT_META[nat_key]
    sb   = status_block(nat_key, dest)

    dest_name  = dest["name"]
    dest_fi    = dest["fi"]
    nat_label  = nat["label"]
    nat_adj    = nat["adj"]
    nat_fi     = nat["fi"]

    title        = f"{dest_name} Visa for {nat_label} Citizens 2026"
    slug         = f"{dest_key}-visa-for-{nat_key}-citizens"
    canonical    = f"https://www.evisa-card.com/en/{slug}"
    description  = (
        f"{nat_adj} passport holders visiting {dest_name} in 2026: "
        + (
            "EU free movement, no visa required. Updated March 2026."
            if nat_key in EU_FREE_MOVEMENT else
            "Visa-free with ETIAS (EUR 7, 3 years). Up to 90 days. Updated March 2026."
            if nat_key in VISA_FREE_ETIAS else
            f"Schengen visa required, EUR 80, 15 working days via VFS Global. Updated March 2026."
        )
    )

    table_key_fact = f"Key Facts — {dest_name} for {nat_label} Citizens"
    faq_ld = faq_jsonld(sb["faqs"])
    faq_section = faq_html(sb["faqs"])

    html = f"""<!DOCTYPE html>
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
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {faq_ld}
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
                        <a class="dropdown-item active" href="/en/{slug}.html"><span class="fi fi-gb"></span> English</a>
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

<h1><span class="fi fi-{dest_fi}" style="margin-right:8px;"></span><span class="fi fi-{nat_fi}" style="margin-right:8px;"></span>{title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{table_key_fact}</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{sb["status_badge"]}</td></tr>
{sb["visa_type_row"]}
{sb["fee_row"]}
{sb["max_stay_row"]}
{sb["processing_row"]}
{sb["apply_row"]}
</tbody>
</table>

<h2>{dest_name} for {nat_label} Citizens — Overview</h2>
<p>{sb["intro"]}</p>

<h2>{sb["details_heading"]}</h2>
{sb["details_body"]}

<h2>How to Travel to {dest_name}</h2>
{sb["how_to"]}

<h2>Required Documents</h2>
{sb["docs"]}

{faq_section}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current entry requirements at the official <a href="{dest["embassy_url"]}" target="_blank" rel="noopener">{dest_name} government website</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{dest_key}.html">{dest_name} Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_key}-visa-requirements.html">{dest_name} Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_key}-visa-fees.html">{dest_name} Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_key}-visa-processing-time.html">{dest_name} Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations →</a>
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
    return html

# ── runner ────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []
    for dest_key in ("poland", "hungary"):
        for nat_key in NAT_META:
            filename = f"{dest_key}-visa-for-{nat_key}-citizens.html"
            filepath = os.path.join(OUT_DIR, filename)
            html = build_page(dest_key, nat_key)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  created: {filename}")
    print(f"\nDone — {len(created)} files written to {OUT_DIR}")

if __name__ == "__main__":
    main()
