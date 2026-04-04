#!/usr/bin/env python3
"""
Generate 40 nationality pages for Switzerland and Austria:
  www/en/switzerland-visa-for-{nat}-citizens.html
  www/en/austria-visa-for-{nat}-citizens.html
for 20 nationalities.

Visa status (both are Schengen):
  - EU/CH free movement : french, german
  - Visa-free + ETIAS   : us, uk, canadian, japanese, australian, korean,
                          singaporean, brazilian, mexican, argentinian
  - Schengen visa EUR 80: indian, chinese, russian, indonesian, philippine,
                          nigerian, south-african, turkish
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NATIONALITIES = {
    # slug        : (Adjective,     flag-iso2, passport_label,   status)
    "us"          : ("US",          "us",  "US passport holders",            "etias"),
    "uk"          : ("UK",          "gb",  "UK passport holders",            "etias"),
    "canadian"    : ("Canadian",    "ca",  "Canadian passport holders",      "etias"),
    "french"      : ("French",      "fr",  "French passport holders",        "eu_free"),
    "german"      : ("German",      "de",  "German passport holders",        "eu_free"),
    "japanese"    : ("Japanese",    "jp",  "Japanese passport holders",      "etias"),
    "australian"  : ("Australian",  "au",  "Australian passport holders",    "etias"),
    "indian"      : ("Indian",      "in",  "Indian passport holders",        "visa"),
    "chinese"     : ("Chinese",     "cn",  "Chinese passport holders",       "visa"),
    "russian"     : ("Russian",     "ru",  "Russian passport holders",       "visa"),
    "brazilian"   : ("Brazilian",   "br",  "Brazilian passport holders",     "etias"),
    "mexican"     : ("Mexican",     "mx",  "Mexican passport holders",       "etias"),
    "south-african":("South African","za", "South African passport holders", "visa"),
    "nigerian"    : ("Nigerian",    "ng",  "Nigerian passport holders",      "visa"),
    "korean"      : ("Korean",      "kr",  "Korean passport holders",        "etias"),
    "singaporean" : ("Singaporean", "sg",  "Singaporean passport holders",   "etias"),
    "indonesian"  : ("Indonesian",  "id",  "Indonesian passport holders",    "visa"),
    "philippine"  : ("Philippine",  "ph",  "Philippine passport holders",    "visa"),
    "turkish"     : ("Turkish",     "tr",  "Turkish passport holders",       "visa"),
    "argentinian" : ("Argentinian", "ar",  "Argentinian passport holders",   "etias"),
}

# ---------------------------------------------------------------------------
# Destination metadata
# ---------------------------------------------------------------------------
DESTINATIONS = {
    "switzerland": {
        "title_name"   : "Switzerland",
        "flag_iso2"    : "ch",
        "official_url" : "https://www.sem.admin.ch/sem/en/home/themen/einreise.html",
        "official_label": "sem.admin.ch",
        "fees_page"    : "switzerland-visa-fees.html",
        "req_page"     : "switzerland-visa-requirements.html",
        "proc_page"    : "switzerland-visa-processing-time.html",
        "overview_page": "visa-switzerland.html",
        "note_schengen": (
            "Switzerland is not an EU member but is a full <strong>Schengen Area</strong> associate. "
            "A Schengen visa issued by Switzerland is valid across all 27 Schengen countries, and vice versa."
        ),
        "embassy_note" : "Swiss Embassy / VFS Global",
    },
    "austria": {
        "title_name"   : "Austria",
        "flag_iso2"    : "at",
        "official_url" : "https://www.bmeia.gv.at/en/travel-stay/entry-and-residence-in-austria/",
        "official_label": "bmeia.gv.at",
        "fees_page"    : "austria-visa-fees.html",
        "req_page"     : "austria-visa-requirements.html",
        "proc_page"    : "austria-visa-processing-time.html",
        "overview_page": "visa-austria.html",
        "note_schengen": (
            "Austria is a full <strong>EU and Schengen Area</strong> member. "
            "A Schengen visa issued by Austria is valid across all 27 Schengen countries, and vice versa."
        ),
        "embassy_note" : "Austrian Embassy / VFS Global",
    },
}

# ---------------------------------------------------------------------------
# HTML generator
# ---------------------------------------------------------------------------

def nav_html(slug, dest_slug):
    filename = f"{dest_slug}-visa-for-{slug}-citizens.html"
    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
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
</nav>"""


def footer_html():
    return """<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
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


def build_page(dest_slug, nat_slug):
    d  = DESTINATIONS[dest_slug]
    n  = NATIONALITIES[nat_slug]
    adj, flag_nat, passport_label, status = n
    dest_name   = d["title_name"]
    dest_flag   = d["flag_iso2"]
    filename    = f"{dest_slug}-visa-for-{nat_slug}-citizens.html"
    canonical   = f"https://www.evisa-card.com/en/{dest_slug}-visa-for-{nat_slug}-citizens"
    page_title  = f"{dest_name} Visa for {adj} Citizens 2026"

    # -----------------------------------------------------------------------
    # Per-status content
    # -----------------------------------------------------------------------
    if status == "eu_free":
        # French / German — EU free movement (also covers Switzerland via bilateral)
        meta_desc = (
            f"{passport_label} visiting {dest_name} in 2026: EU/Schengen free movement, "
            f"no visa or ETIAS required. Complete guide updated March 2026."
        )
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for {dest_name}?",
                "a": (
                    f"No. {passport_label} enjoy full freedom of movement as EU citizens. "
                    f"No visa, no ETIAS, and no prior authorisation is required."
                ),
            },
            {
                "q": f"How long can {adj} citizens stay in {dest_name}?",
                "a": (
                    f"Indefinitely — EU citizens have the right to live, work, and stay in {dest_name} "
                    f"without any time restriction."
                ),
            },
            {
                "q": f"What documents does a {adj} citizen need to enter {dest_name}?",
                "a": (
                    "A valid EU national ID card or passport is sufficient for entry. "
                    "No additional documents are required for tourism."
                ),
            },
        ]
        status_cell = '<span style="color:green;font-weight:600;">No Visa — EU Free Movement</span>'
        max_stay_cell = "Unlimited (EU freedom of movement)"
        fee_cell = "Free"
        processing_cell = "N/A"
        apply_at_cell = "N/A"
        h1_text = f"{dest_name} for {adj} Citizens 2026 — EU Free Movement"
        intro_para = (
            f"<p>As EU citizens, {passport_label} enjoy <strong>freedom of movement</strong> throughout the "
            f"Schengen Area and the European Union. Entry into {dest_name} requires no visa, no ETIAS "
            f"authorisation, and no prior appointment at a consulate. A valid national ID card or passport is all "
            f"that is needed at the border.</p>"
            f"<p>{d['note_schengen']}</p>"
        )
        main_sections = f"""
<h2>Entry Requirements for {adj} Citizens</h2>
{intro_para}

<h2>What Documents to Carry</h2>
<ul>
<li>Valid EU national ID card <em>or</em> passport</li>
<li>Proof of accommodation for stays beyond a few days (recommended)</li>
<li>Return or onward travel ticket (recommended for short visits)</li>
</ul>

<h2>Living and Working in {dest_name}</h2>
<p>EU citizens wishing to reside in {dest_name} for more than three months must register with the local authorities. {passport_label} do not need a work permit — the right to work is inherent in EU free movement rights.</p>

<h2>ETIAS — Does It Apply?</h2>
<p>No. ETIAS (European Travel Information and Authorisation System) applies to <em>non-EU</em> visa-exempt nationals only. {adj} citizens are exempt from ETIAS entirely.</p>
"""
        related_nats = [n2 for n2 in ["us", "uk", "canadian", "japanese", "indian"] if n2 != nat_slug]

    elif status == "etias":
        meta_desc = (
            f"{passport_label} visiting {dest_name} in 2026: visa-free access, ETIAS required from 2025, "
            f"90 days Schengen stay. Complete guide updated March 2026."
        )
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for {dest_name}?",
                "a": (
                    f"No visa is required. {passport_label} can visit {dest_name} visa-free for up to "
                    f"90 days in any 180-day period. From 2025 an ETIAS pre-travel authorisation (€7) is required."
                ),
            },
            {
                "q": "What is ETIAS and how do I apply?",
                "a": (
                    "ETIAS is a mandatory online travel authorisation for visa-exempt visitors to the Schengen Area. "
                    "Apply at etias.com, pay €7, and receive approval by email — usually within minutes."
                ),
            },
            {
                "q": f"How long can {adj} citizens stay in {dest_name}?",
                "a": (
                    "Up to 90 days in any 180-day period across the entire Schengen Zone. "
                    "Days spent in other Schengen countries count toward this limit."
                ),
            },
        ]
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — ETIAS Required</span>'
        max_stay_cell = "90 days in any 180-day period"
        fee_cell = "Free (ETIAS €7)"
        processing_cell = "Instant (ETIAS online)"
        apply_at_cell = "etias.com"
        h1_text = f"{dest_name} Visa for {adj} Citizens 2026 — Visa-Free + ETIAS"
        main_sections = f"""
<h2>Do {adj} Citizens Need a Visa for {dest_name}?</h2>
<p>No. {passport_label} can enter {dest_name} and the entire Schengen Area without a visa for up to <strong>90 days in any 180-day period</strong>. No consulate appointment is required.</p>
<p>{d['note_schengen']}</p>
<p>From 2025, travellers must obtain <strong>ETIAS</strong> (European Travel Information and Authorisation System) before departure. The application is entirely online, costs €7, and is valid for 3 years.</p>

<h2>ETIAS — How to Apply</h2>
<ol>
<li>Visit <a href="https://travel-europe.europa.eu/etias_en" target="_blank" rel="noopener">etias.com</a> and complete the online application form.</li>
<li>Pay the €7 fee by credit or debit card.</li>
<li>Receive ETIAS authorisation by email — usually within minutes to hours.</li>
<li>ETIAS is electronically linked to your passport. Carry your passport when travelling.</li>
</ol>

<h2>Documents Required at the Border</h2>
<ul>
<li>Valid {adj} passport (valid for the full duration of your stay)</li>
<li>ETIAS authorisation (from 2025)</li>
<li>Return or onward travel ticket</li>
<li>Proof of accommodation (hotel booking or host invitation)</li>
<li>Travel/health insurance covering at least €30,000 in the Schengen Area</li>
<li>Proof of sufficient funds (~€120 per day of stay)</li>
</ul>

<h2>Schengen 90/180-Day Rule</h2>
<p>The 90-day limit applies across the <em>entire</em> Schengen Zone, not just {dest_name}. Days spent in France, Germany, Spain, or any other Schengen country count against your {dest_name} allowance. Plan accordingly to avoid overstaying.</p>
"""
        related_nats = [n2 for n2 in ["indian", "chinese", "russian", "turkish"] if n2 != nat_slug]

    else:  # status == "visa"
        meta_desc = (
            f"{passport_label} visiting {dest_name} in 2026: Schengen visa required, €80 fee, "
            f"15 working days processing. Complete guide updated March 2026."
        )
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for {dest_name}?",
                "a": (
                    f"Yes. {passport_label} must obtain a Schengen Type C visa before travelling to {dest_name}. "
                    f"Apply at the {d['embassy_note']} in your country."
                ),
            },
            {
                "q": f"How much does a {dest_name} Schengen visa cost for {adj} citizens?",
                "a": (
                    "The Schengen visa fee is €80 for adults (aged 12+) and €40 for children aged 6–12. "
                    "Children under 6 are free. All fees are non-refundable."
                ),
            },
            {
                "q": f"How long does {dest_name} visa processing take for {adj} applicants?",
                "a": (
                    "Standard processing is 15 working days from the date of biometric appointment. "
                    "Apply at least 3–4 weeks before your intended departure date."
                ),
            },
        ]
        status_cell = '<span style="color:red;font-weight:600;">Yes — Schengen Visa Required</span>'
        max_stay_cell = "90 days in any 180-day period"
        fee_cell = "€80 (adults), €40 (children 6–12), free (under 6)"
        processing_cell = "15 working days"
        apply_at_cell = d["embassy_note"]
        h1_text = f"{dest_name} Schengen Visa for {adj} Citizens 2026"
        main_sections = f"""
<h2>Do {adj} Citizens Need a Visa for {dest_name}?</h2>
<p>Yes. {passport_label} must obtain a <strong>Schengen Type C visa</strong> before travelling to {dest_name}. There is no eVisa — applications must be submitted in person with biometrics (fingerprints and photograph) at the {d['embassy_note']}.</p>
<p>{d['note_schengen']}</p>

<h2>Schengen Visa Fee and Validity</h2>
<p>The standard adult fee is <strong>€80</strong> (non-refundable). The visa allows stays of up to <strong>90 days in any 180-day period</strong> across all 27 Schengen countries. It is typically issued as a single or double-entry visa; multi-entry visas are granted to frequent travellers.</p>

<h2>How to Apply for a {dest_name} Schengen Visa</h2>
<ol>
<li>Complete the Schengen visa application form (available from the {d['embassy_note']}).</li>
<li>Book a biometric appointment at the {d['embassy_note']} in your country.</li>
<li>Attend in person, submit all documents, and provide fingerprints and a photo.</li>
<li>Pay the €80 non-refundable application fee.</li>
<li>Track your application online. Collect your passport with the visa sticker once approved.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid {adj} passport (min. 2 blank pages; issued within the last 10 years; valid at least 3 months beyond intended departure)</li>
<li>Two recent colour passport photos (35 &times; 45 mm, white background)</li>
<li>Completed Schengen visa application form</li>
<li>Bank statements — last 3 months (min. ~€120 per day of stay)</li>
<li>Travel insurance — min. €30,000 coverage valid across the Schengen Area</li>
<li>Confirmed return flight itinerary</li>
<li>Proof of accommodation (hotel booking or host invitation letter)</li>
<li>Employment letter / payslips / proof of business registration</li>
<li>Evidence of ties to home country (property, family, employment)</li>
</ul>

<h2>Processing Time</h2>
<p>Standard processing is <strong>15 working days</strong> from the biometric appointment date. Consulates may take up to 45 calendar days during peak travel season (June–August). Apply well in advance.</p>
"""
        related_nats = [n2 for n2 in ["indian", "chinese", "russian", "turkish", "nigerian", "philippine"]
                        if n2 != nat_slug]

    # -----------------------------------------------------------------------
    # Related pages links for the destination
    # -----------------------------------------------------------------------
    related_nat_links = "\n    ".join(
        f'<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_slug}-visa-for-{rn}-citizens.html">'
        f'{dest_name} for {NATIONALITIES[rn][0]} Citizens</a>'
        for rn in related_nats[:4]
    )

    # -----------------------------------------------------------------------
    # FAQ JSON-LD
    # -----------------------------------------------------------------------
    faq_items = ",\n      ".join(
        f'{{"@type":"Question","name":"{item["q"]}","acceptedAnswer":{{"@type":"Answer","text":"{item["a"]}"}}}}'
        for item in faq
    )
    faq_jsonld = (
        f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n      {faq_items}\n    ]}}'
    )

    # -----------------------------------------------------------------------
    # Full page
    # -----------------------------------------------------------------------
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{page_title}</title>
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
    {faq_jsonld}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{nav_html(nat_slug, dest_slug)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{h1_text}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {dest_name} for {adj} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Max Stay</th><td>{max_stay_cell}</td></tr>
<tr><th>Visa Fee</th><td>{fee_cell}</td></tr>
<tr><th>Processing Time</th><td>{processing_cell}</td></tr>
<tr><th>Apply At</th><td>{apply_at_cell}</td></tr>
</tbody>
</table>

{main_sections}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{d['official_url']}" target="_blank" rel="noopener">{d['official_label']}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{d['overview_page']}">{dest_name} Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{d['req_page']}">{dest_name} Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{d['fees_page']}">{dest_name} Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{d['proc_page']}">{dest_name} Processing Times</a>
    {related_nat_links}
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{footer_html()}
</body>
</html>
"""
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    count = 0
    for dest_slug in ("switzerland", "austria"):
        for nat_slug in NATIONALITIES:
            filename = f"{dest_slug}-visa-for-{nat_slug}-citizens.html"
            filepath = os.path.join(OUT_DIR, filename)
            content  = build_page(dest_slug, nat_slug)
            with open(filepath, "w", encoding="utf-8") as fh:
                fh.write(content)
            count += 1
            print(f"  Created: {filename}")
    print(f"\nDone — {count} files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
