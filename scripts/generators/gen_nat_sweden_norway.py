"""
gen_nat_sweden_norway.py
Generates 40 HTML pages in www/en/:
  sweden-visa-for-{nat}-citizens.html  (20 files)
  norway-visa-for-{nat}-citizens.html  (20 files)

Both Sweden and Norway are Schengen Area members.
Norway is not in the EU but is a full Schengen associate.
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATIONALITIES = {
    # slug: (adjective, flag-code, nationality-noun, country-of-passport)
    "us":           ("US",          "us", "US citizens",           "United States"),
    "uk":           ("British",     "gb", "British citizens",      "United Kingdom"),
    "canadian":     ("Canadian",    "ca", "Canadian citizens",     "Canada"),
    "french":       ("French",      "fr", "French citizens",       "France"),
    "german":       ("German",      "de", "German citizens",       "Germany"),
    "japanese":     ("Japanese",    "jp", "Japanese citizens",     "Japan"),
    "australian":   ("Australian",  "au", "Australian citizens",   "Australia"),
    "indian":       ("Indian",      "in", "Indian citizens",       "India"),
    "chinese":      ("Chinese",     "cn", "Chinese citizens",      "China"),
    "russian":      ("Russian",     "ru", "Russian citizens",      "Russia"),
    "brazilian":    ("Brazilian",   "br", "Brazilian citizens",    "Brazil"),
    "mexican":      ("Mexican",     "mx", "Mexican citizens",      "Mexico"),
    "south-african":("South African","za","South African citizens","South Africa"),
    "nigerian":     ("Nigerian",    "ng", "Nigerian citizens",     "Nigeria"),
    "korean":       ("Korean",      "kr", "Korean citizens",       "South Korea"),
    "singaporean":  ("Singaporean", "sg", "Singaporean citizens",  "Singapore"),
    "indonesian":   ("Indonesian",  "id", "Indonesian citizens",   "Indonesia"),
    "philippine":   ("Philippine",  "ph", "Philippine citizens",   "Philippines"),
    "turkish":      ("Turkish",     "tr", "Turkish citizens",      "Turkey"),
    "argentinian":  ("Argentinian", "ar", "Argentinian citizens",  "Argentina"),
}

# Visa status categories
ETIAS = {"us", "uk", "canadian", "japanese", "australian", "korean",
         "singaporean", "brazilian", "mexican", "argentinian"}
EU_EEA = {"french", "german"}
SCHENGEN_VISA = {"indian", "chinese", "russian", "indonesian", "philippine",
                 "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# Country-specific data
# ---------------------------------------------------------------------------
COUNTRIES = {
    "sweden": {
        "name": "Sweden",
        "flag": "se",
        "capital": "Stockholm",
        "embassy_url": "https://www.migrationsverket.se/English/Private-individuals/Visiting-Sweden.html",
        "vfs_url": "https://visa.vfsglobal.com/",
        "apply_url": "https://www.migrationsverket.se/English/Private-individuals/Visiting-Sweden.html",
        "etias_note": (
            "Sweden is in the Schengen Area. From mid-2025, "
            "ETIAS (European Travel Information and Authorisation System) "
            "is required for visa-free travellers. ETIAS costs EUR 7 and is "
            "valid for 3 years or until passport expiry."
        ),
        "eu_note": (
            "As EU citizens, French and German passport holders enjoy full "
            "freedom of movement within the EU/EEA and do <strong>not</strong> "
            "require any visa or ETIAS to enter Sweden."
        ),
        "visa_note": (
            "Sweden processes Schengen visas through the Swedish Migration Agency "
            "(Migrationsverket) and VFS Global application centres worldwide."
        ),
        "schengen_apply": "Swedish Migration Agency / VFS Global",
        "region": "Schengen Area / European Union",
    },
    "norway": {
        "name": "Norway",
        "flag": "no",
        "capital": "Oslo",
        "embassy_url": "https://www.udi.no/en/want-to-apply/visit/",
        "vfs_url": "https://visa.vfsglobal.com/",
        "apply_url": "https://www.udi.no/en/want-to-apply/visit/",
        "etias_note": (
            "Norway is not an EU member but is a full Schengen Area associate. "
            "From mid-2025, ETIAS is required for visa-free travellers. "
            "ETIAS costs EUR 7 and is valid for 3 years or until passport expiry."
        ),
        "eu_note": (
            "As EU citizens, French and German passport holders enjoy freedom of "
            "movement under the EEA Agreement and do <strong>not</strong> require "
            "any visa or ETIAS to enter Norway."
        ),
        "visa_note": (
            "Norway processes Schengen visas through the Norwegian Directorate of "
            "Immigration (UDI) and VFS Global application centres worldwide."
        ),
        "schengen_apply": "Norwegian Directorate of Immigration (UDI) / VFS Global",
        "region": "Schengen Area (non-EU EEA member)",
    },
}

# ---------------------------------------------------------------------------
# Helper: navbar language dropdown
# ---------------------------------------------------------------------------
def navbar(slug_file: str) -> str:
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
                        <a class="dropdown-item active" href="/en/{slug_file}"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Fran&ccedil;ais</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Espa&ntilde;ol</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Portugu&ecirc;s</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""


# ---------------------------------------------------------------------------
# HTML builder
# ---------------------------------------------------------------------------
def build_page(country_slug: str, nat_slug: str) -> str:
    cd = COUNTRIES[country_slug]
    adj, flag_code, nat_label, passport_country = NATIONALITIES[nat_slug]

    cname = cd["name"]
    slug_file = f"{country_slug}-visa-for-{nat_slug}-citizens.html"
    slug_canonical = f"{country_slug}-visa-for-{nat_slug}-citizens"
    page_title = f"{cname} Visa for {adj} Citizens 2026"

    # ---- Status block ----
    if nat_slug in EU_EEA:
        status = "free"
        status_badge = '<span style="color:green;font-weight:600;">No Visa Required — EU/EEA Free Movement</span>'
        visa_type_row = "EU/EEA Free Movement"
        fee_row = "Free"
        stay_row = "Unlimited (right of residence)"
        processing_row = "N/A"
        apply_row = "No application required"
        meta_desc = (
            f"{adj} passport holders do not need a visa for {cname} 2026. "
            f"As EU citizens they enjoy free movement within the EU/EEA. "
            f"Updated March 2026."
        )
    elif nat_slug in ETIAS:
        status = "etias"
        status_badge = '<span style="color:orange;font-weight:600;">ETIAS Required — EUR 7 (visa-free entry)</span>'
        visa_type_row = "ETIAS (European Travel Information and Authorisation System)"
        fee_row = "EUR 7"
        stay_row = "90 days in any 180-day period"
        processing_row = "Instant–72 hours (online)"
        apply_row = "travel-europe.eu/etias (official EU ETIAS portal)"
        meta_desc = (
            f"{adj} passport holders can visit {cname} visa-free in 2026 but need "
            f"ETIAS authorisation (EUR 7, valid 3 years). "
            f"Updated March 2026."
        )
    else:  # Schengen visa
        status = "visa"
        status_badge = '<span style="color:red;font-weight:600;">Schengen Visa Required — EUR 80</span>'
        visa_type_row = "Schengen Short-Stay Visa (Type C)"
        fee_row = "EUR 80 (adults); EUR 40 (children 6–11)"
        stay_row = "90 days in any 180-day period"
        processing_row = "15 working days (up to 45 in some cases)"
        apply_row = cd["schengen_apply"]
        meta_desc = (
            f"{adj} passport holders need a Schengen visa for {cname} 2026. "
            f"Fee EUR 80, processing 15 working days, apply at VFS Global or the {cname} embassy. "
            f"Updated March 2026."
        )

    # ---- FAQ schema ----
    if nat_slug in EU_EEA:
        faq_json = f"""[
      {{"@type":"Question","name":"Do {nat_label} need a visa for {cname}?","acceptedAnswer":{{"@type":"Answer","text":"{adj} passport holders are EU citizens and enjoy free movement within the EU/EEA. No visa or ETIAS is required to enter {cname}."}}}},
      {{"@type":"Question","name":"How long can {nat_label} stay in {cname}?","acceptedAnswer":{{"@type":"Answer","text":"EU/EEA citizens may reside in {cname} indefinitely under free movement rights. There is no maximum stay limit for tourism or short visits."}}}},
      {{"@type":"Question","name":"Do {nat_label} need to register in {cname}?","acceptedAnswer":{{"@type":"Answer","text":"EU citizens staying longer than 3 months in {cname} are encouraged to register with local authorities, but no registration is required for short visits."}}}}
    ]"""
    elif nat_slug in ETIAS:
        faq_json = f"""[
      {{"@type":"Question","name":"Do {nat_label} need a visa for {cname}?","acceptedAnswer":{{"@type":"Answer","text":"{adj} citizens do not need a visa for {cname} but must obtain ETIAS authorisation before travel. ETIAS costs EUR 7 and is valid for 3 years or until passport expiry."}}}},
      {{"@type":"Question","name":"What is ETIAS and how do I apply?","acceptedAnswer":{{"@type":"Answer","text":"ETIAS (European Travel Information and Authorisation System) is an electronic pre-travel authorisation for visa-exempt nationalities entering the Schengen Area. Apply online at the official ETIAS portal, pay EUR 7, and receive approval usually within minutes."}}}},
      {{"@type":"Question","name":"How long can {nat_label} stay in {cname} with ETIAS?","acceptedAnswer":{{"@type":"Answer","text":"Up to 90 days in any 180-day period across the entire Schengen Area, including {cname}."}}}}
    ]"""
    else:
        faq_json = f"""[
      {{"@type":"Question","name":"Do {nat_label} need a visa for {cname}?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {adj} passport holders must apply for a Schengen Short-Stay Visa (Type C) before travelling to {cname}. The fee is EUR 80 for adults."}}}},
      {{"@type":"Question","name":"How much does the {cname} Schengen visa cost?","acceptedAnswer":{{"@type":"Answer","text":"The standard Schengen visa fee is EUR 80 for adults and EUR 40 for children aged 6–11. Children under 6 are exempt from fees."}}}},
      {{"@type":"Question","name":"How long does {cname} visa processing take?","acceptedAnswer":{{"@type":"Answer","text":"Standard processing takes 15 working days. Allow up to 45 calendar days during peak periods. Apply at least 3 weeks before travel, and no earlier than 6 months before departure."}}}}
    ]"""

    # ---- Main content body ----
    if nat_slug in EU_EEA:
        body_content = f"""<h2>{cname} Entry for {adj} Citizens</h2>
<p>{adj} passport holders are EU citizens and benefit from the <strong>freedom of movement</strong> within the European Economic Area. No visa and no ETIAS is needed to enter {cname}.</p>
<p>{cd["eu_note"]}</p>

<h2>What {adj} Citizens Need</h2>
<ul>
<li>Valid passport or national identity card</li>
<li>No visa application required</li>
<li>No ETIAS required</li>
<li>Proof of onward travel or sufficient funds may be requested at border (rarely)</li>
</ul>

<h2>How Long Can You Stay?</h2>
<p>As EU citizens, {nat_label} may stay in {cname} for an unlimited period for tourism, work, or study. EU free movement rights apply fully.</p>

<h2>Practical Travel Tips</h2>
<ul>
<li>Carry a valid EU passport or national ID card</li>
<li>Health insurance (EHIC/EHIC successor) is recommended</li>
<li>No border formalities within the Schengen Area when arriving from another Schengen country</li>
<li>Passport control applies when arriving from outside the Schengen Area</li>
</ul>"""

    elif nat_slug in ETIAS:
        body_content = f"""<h2>{cname} Entry for {adj} Citizens — ETIAS</h2>
<p>{adj} passport holders can visit {cname} <strong>without a traditional visa</strong>, but must obtain an <strong>ETIAS authorisation</strong> before boarding. ETIAS is an electronic pre-travel check, not a visa. {cd["etias_note"]}</p>

<h2>ETIAS Key Details</h2>
<ul>
<li>Cost: <strong>EUR 7</strong> (applicants aged 18–70; free for under 18 and over 70)</li>
<li>Validity: <strong>3 years</strong> or until passport expiry (whichever is sooner)</li>
<li>Entries: Multiple</li>
<li>Stay per visit: Up to <strong>90 days in any 180-day period</strong> in the Schengen Area</li>
<li>Processing: Usually instant; up to 72 hours in some cases; up to 14 days in rare cases</li>
</ul>

<h2>How to Apply for ETIAS</h2>
<ol>
<li>Visit the official ETIAS website at <a href="https://travel-europe.eu/etias" target="_blank" rel="noopener">travel-europe.eu/etias</a>.</li>
<li>Complete the online application form with your passport details.</li>
<li>Pay the EUR 7 fee by card.</li>
<li>Receive ETIAS approval by email — usually within minutes.</li>
<li>ETIAS is linked electronically to your passport. No physical document is issued.</li>
</ol>

<h2>Required Documents for ETIAS</h2>
<ul>
<li>Valid passport (must be valid for the duration of your stay)</li>
<li>Email address</li>
<li>Credit or debit card for EUR 7 fee</li>
</ul>

<h2>ETIAS vs Schengen Visa</h2>
<p>ETIAS is <strong>not</strong> a visa. It is an automated security pre-screening tool for nationals who already enjoy visa-free access to the Schengen Area. {adj} citizens remain visa-free — ETIAS is simply a travel authorisation required before boarding.</p>"""

    else:  # Schengen visa
        body_content = f"""<h2>{cname} Schengen Visa for {adj} Citizens</h2>
<p>{adj} passport holders must apply for a <strong>Schengen Short-Stay Visa (Type C)</strong> to visit {cname}. The fee is <strong>EUR 80</strong> and processing takes approximately <strong>15 working days</strong>. {cd["visa_note"]}</p>

<h2>Schengen Visa Key Details</h2>
<ul>
<li>Cost: <strong>EUR 80</strong> (adults); EUR 40 (children 6–11); free (children under 6)</li>
<li>Stay: Up to <strong>90 days in any 180-day period</strong> in the Schengen Area</li>
<li>Processing: <strong>15 working days</strong> (standard); up to 45 calendar days peak period</li>
<li>Entries: Single, double, or multiple (as granted)</li>
<li>Apply: From <strong>6 months</strong> before travel, minimum <strong>15 working days</strong> before departure</li>
</ul>

<h2>How to Apply for the {cname} Schengen Visa</h2>
<ol>
<li>Book an appointment at the nearest <strong>VFS Global</strong> application centre or {cname} consulate/embassy.</li>
<li>Complete the Schengen visa application form (online via <a href="{cd['apply_url']}" target="_blank" rel="noopener">{cd['apply_url']}</a>).</li>
<li>Gather all required documents (see list below).</li>
<li>Attend your appointment, submit documents, pay EUR 80, and provide biometrics (fingerprints and photo) if not enrolled in the last 59 months.</li>
<li>Await the decision — typically 15 working days.</li>
<li>Collect your passport with visa sticker (or receive it by post if opted).</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (at least 3 months beyond intended stay; issued within the last 10 years)</li>
<li>Completed Schengen visa application form</li>
<li>Passport-size photos (35×45 mm, white background)</li>
<li>Travel itinerary and accommodation proof (hotel bookings or invitation letter)</li>
<li>Round-trip flight reservations</li>
<li>Travel insurance (min. EUR 30,000 coverage, valid across Schengen)</li>
<li>Bank statements (last 3 months, showing sufficient funds)</li>
<li>Proof of employment, business registration, or student enrollment</li>
<li>Leave approval letter (if employed)</li>
<li>Biometrics (fingerprints and photo) if not enrolled recently</li>
</ul>

<h2>Schengen Visa Fees Summary</h2>
<table class="table table-bordered table-sm mt-2 mb-3">
<thead><tr><th>Category</th><th>Fee</th></tr></thead>
<tbody>
<tr><td>Adults (12 and over)</td><td>EUR 80</td></tr>
<tr><td>Children aged 6–11</td><td>EUR 40</td></tr>
<tr><td>Children under 6</td><td>Free</td></tr>
</tbody>
</table>"""

    # ---- Related guides ----
    related = f"""<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{country_slug}.html">{cname} Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country_slug}-visa-requirements.html">{cname} Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country_slug}-visa-fees.html">{cname} Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{country_slug}-visa-processing-time.html">{cname} Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    # ---- Full page ----
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
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug_canonical}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug_canonical}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug_canonical}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
{navbar(slug_file)}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag_code}"></span> <span class="fi fi-{cd['flag']}"></span> {page_title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {cname} for {adj} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>{visa_type_row}</td></tr>
<tr><th>Fee</th><td>{fee_row}</td></tr>
<tr><th>Max Stay</th><td>{stay_row}</td></tr>
<tr><th>Processing</th><td>{processing_row}</td></tr>
<tr><th>Apply At</th><td>{apply_row}</td></tr>
</tbody>
</table>

{body_content}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{cd['apply_url']}" target="_blank" rel="noopener">{cd['apply_url']}</a> before travel.</p>
</div>

{related}

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
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    generated = []
    for country_slug in ("sweden", "norway"):
        for nat_slug in NATIONALITIES:
            html = build_page(country_slug, nat_slug)
            filename = f"{country_slug}-visa-for-{nat_slug}-citizens.html"
            filepath = os.path.join(OUT_DIR, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            generated.append(filename)
            print(f"  OK  {filename}")
    print(f"\nTotal files generated: {len(generated)}")


if __name__ == "__main__":
    main()
