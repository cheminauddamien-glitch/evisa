#!/usr/bin/env python3
"""
gen_nat_colombia_costarica.py
Generates 40 HTML files in www/en/:
  colombia-visa-for-{nat}-citizens.html   (20 files)
  costa-rica-visa-for-{nat}-citizens.html (20 files)
for 20 nationalities.
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NATIONALITIES = [
    # (slug,           label,          adj,             fi_code, related_nat_slugs)
    ("us",            "US",           "American",       "us",   ["canadian", "uk", "australian"]),
    ("uk",            "UK",           "British",        "gb",   ["canadian", "australian", "french"]),
    ("canadian",      "Canadian",     "Canadian",       "ca",   ["us", "uk", "australian"]),
    ("french",        "French",       "French",         "fr",   ["german", "uk", "argentinian"]),
    ("german",        "German",       "German",         "de",   ["french", "uk", "argentinian"]),
    ("japanese",      "Japanese",     "Japanese",       "jp",   ["korean", "singaporean", "chinese"]),
    ("australian",    "Australian",   "Australian",     "au",   ["us", "uk", "canadian"]),
    ("indian",        "Indian",       "Indian",         "in",   ["chinese", "philippine", "indonesian"]),
    ("chinese",       "Chinese",      "Chinese",        "cn",   ["japanese", "korean", "russian"]),
    ("russian",       "Russian",      "Russian",        "ru",   ["chinese", "turkish", "south-african"]),
    ("brazilian",     "Brazilian",    "Brazilian",      "br",   ["argentinian", "mexican", "us"]),
    ("mexican",       "Mexican",      "Mexican",        "mx",   ["brazilian", "argentinian", "us"]),
    ("south-african", "South African","South African",  "za",   ["nigerian", "turkish", "russian"]),
    ("nigerian",      "Nigerian",     "Nigerian",       "ng",   ["south-african", "turkish", "indonesian"]),
    ("korean",        "Korean",       "Korean",         "kr",   ["japanese", "singaporean", "chinese"]),
    ("singaporean",   "Singaporean",  "Singaporean",    "sg",   ["korean", "indonesian", "japanese"]),
    ("indonesian",    "Indonesian",   "Indonesian",     "id",   ["philippine", "singaporean", "indian"]),
    ("philippine",    "Philippine",   "Philippine",     "ph",   ["indonesian", "singaporean", "indian"]),
    ("turkish",       "Turkish",      "Turkish",        "tr",   ["russian", "south-african", "nigerian"]),
    ("argentinian",   "Argentinian",  "Argentinian",    "ar",   ["brazilian", "mexican", "french"]),
]

# ---------------------------------------------------------------------------
# Colombia visa classification
# ---------------------------------------------------------------------------
# Visa-free 90 days: us, uk, canadian, french, german, japanese, australian,
#                    korean, singaporean, brazilian, mexican, argentinian, russian, turkish
COLOMBIA_VISAFREE = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian", "russian", "turkish"
}
# Visa required (Colombian visa via cancilleria.gov.co, USD 52):
#   indian, chinese, indonesian, philippine, nigerian, south-african
COLOMBIA_REQUIRED = {"indian", "chinese", "indonesian", "philippine", "nigerian", "south-african"}

# ---------------------------------------------------------------------------
# Costa Rica visa classification
# ---------------------------------------------------------------------------
# Visa-free 90 days: us, uk, canadian, french, german, japanese, australian,
#                    korean, singaporean, brazilian, mexican, argentinian, russian
COSTA_RICA_VISAFREE = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian", "russian"
}
# Visa required: indian, chinese, indonesian, philippine, nigerian, south-african, turkish
COSTA_RICA_REQUIRED = {"indian", "chinese", "indonesian", "philippine", "nigerian", "south-african", "turkish"}


# ---------------------------------------------------------------------------
# Colombia data builder
# ---------------------------------------------------------------------------
def colombia_data(nat_slug, adj):
    country = "Colombia"
    country_slug = "colombia"

    if nat_slug in COLOMBIA_REQUIRED:
        visa_required = '<span style="color:red;font-weight:600;">Visa Required — USD 52</span>'
        max_stay = "Up to 90 days"
        fee = "USD 52"
        processing = "5–15 business days"
        apply_at = "cancilleria.gov.co"
        status_heading = f"Do {adj} Citizens Need a Visa for Colombia?"
        status_body = (
            f"{adj} passport holders must obtain a <strong>Colombian visa</strong> before travelling to Colombia. "
            f"Applications are submitted online via the Cancillería (Ministry of Foreign Affairs) portal at "
            f"<a href='https://www.cancilleria.gov.co/tramites_servicios/visas' target='_blank' rel='noopener'>cancilleria.gov.co</a>. "
            f"The standard visitor visa fee is <strong>USD 52</strong> and processing typically takes "
            f"<strong>5–15 business days</strong>."
        )
        req_items = [
            "Valid passport (at least 6 months validity beyond the planned entry date; at least 2 blank pages)",
            "Completed online visa application form (cancilleria.gov.co)",
            "Recent passport-size photograph (3×4 cm, white background, taken within the last 6 months)",
            "Bank statements for the last 3–6 months demonstrating sufficient funds",
            "Round-trip flight itinerary or confirmed bookings",
            "Proof of accommodation (hotel reservations, rental agreement, or host invitation letter)",
            "Employment letter, proof of self-employment, or proof of student enrolment",
            "Visa fee payment receipt (USD 52, paid via the Cancillería online portal)",
            "Travel health insurance valid for the duration of stay in Colombia",
        ]
        how_to = (
            "<ol>"
            "<li><strong>Create an account</strong> on the Colombian Cancillería visa portal at "
            "<a href='https://www.cancilleria.gov.co/tramites_servicios/visas' target='_blank' rel='noopener'>cancilleria.gov.co</a>.</li>"
            "<li><strong>Complete the application form</strong> — select the appropriate visa category (usually Visitor / Turismo).</li>"
            "<li><strong>Upload supporting documents</strong> — scan all required documents listed above.</li>"
            "<li><strong>Pay the fee</strong> — USD 52 via the online payment system (credit/debit card accepted).</li>"
            "<li><strong>Submit and await decision</strong> — processing takes 5–15 business days. "
            "Check your email for updates or log in to the portal.</li>"
            "<li><strong>Receive your visa</strong> — if approved, the electronic visa (digital sticker) is sent by email. Print it and carry it when travelling.</li>"
            "</ol>"
            "<p>Official portal: <a href='https://www.cancilleria.gov.co/tramites_servicios/visas' target='_blank' rel='noopener'>cancilleria.gov.co</a></p>"
        )
        tips = [
            "Apply at least 3–4 weeks before your travel date; processing can be slower during public holidays.",
            "Ensure your travel insurance policy explicitly covers Colombia for the full duration of your stay.",
            "Bank statements should reflect a minimum of USD 30–45 per day for the length of your trip.",
            "The digital visa (sticker) is sent by email — download and print it before departure.",
            "Colombian immigration officers may ask for proof of onward travel and accommodation at the border.",
        ]
        faq = [
            {
                "q": f"How much does a Colombian visa cost for {adj} citizens?",
                "a": f"The Colombian visitor visa fee for {adj} passport holders is USD 52, payable online via the Cancillería portal."
            },
            {
                "q": f"How long does Colombian visa processing take for {adj} applicants?",
                "a": "Processing typically takes 5–15 business days after successful submission of the complete application."
            },
            {
                "q": f"Can {adj} citizens apply for a Colombia visa online?",
                "a": "Yes. Colombia operates a fully online visa application system via cancilleria.gov.co. No visit to a consulate is required."
            },
        ]
    else:
        # Visa-free 90 days
        visa_required = '<span style="color:green;font-weight:600;">Visa-Free — 90 Days</span>'
        max_stay = "90 days (extendable up to 180 days/year)"
        fee = "Free"
        processing = "N/A — no application required"
        apply_at = "Migraciones Colombia at port of entry"
        status_heading = f"Do {adj} Citizens Need a Visa for Colombia?"
        status_body = (
            f"{adj} passport holders enjoy <strong>visa-free access to Colombia</strong>. "
            f"You may stay for up to <strong>90 days</strong> per entry (extendable once for another 90 days, "
            f"up to a maximum of 180 days per year) for tourism or short business visits. "
            f"No advance visa or pre-travel authorisation is required — simply arrive with a valid passport."
        )
        req_items = [
            "Valid passport (6+ months validity recommended beyond your planned return date)",
            "Return or onward travel ticket",
            "Proof of accommodation (hotel booking or host address)",
            "Proof of sufficient funds for your stay (credit card or equivalent cash)",
            "Travel health insurance (recommended; yellow fever vaccination recommended if visiting Amazon region)",
        ]
        how_to = (
            "<p>No visa application is required for stays up to 90 days.</p>"
            "<ol>"
            "<li><strong>Book flights and accommodation</strong> — ensure your passport is valid for the duration of your trip.</li>"
            "<li><strong>Complete the Check-Mig form</strong> — Colombia requires travellers to fill out the online <strong>Check-Mig</strong> migration form before arrival at "
            "<a href='https://apps.migracioncolombia.gov.co/pre-registro' target='_blank' rel='noopener'>apps.migracioncolombia.gov.co</a>.</li>"
            "<li><strong>Arrive at a Colombian port of entry</strong> — present your passport and Check-Mig confirmation to the immigration officer.</li>"
            "<li><strong>Receive your entry stamp</strong> — the officer will stamp your passport with the permitted stay (up to 90 days).</li>"
            "</ol>"
            "<p>To extend your stay beyond 90 days, visit a Migraciones Colombia office before your initial period expires.</p>"
        )
        tips = [
            "Complete the Check-Mig form online before your flight — it is mandatory for most arrivals.",
            "The 90-day entry stamp is at the discretion of the immigration officer; carry proof of sufficient funds.",
            "Colombia operates on COP (Colombian Peso); carry some local cash for areas outside major cities.",
            "If you plan to visit the Amazon or certain rural regions, a yellow fever vaccination is strongly recommended.",
            "Extensions (prórrogas) of up to 90 additional days can be requested at any Migraciones Colombia office.",
        ]
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for Colombia?",
                "a": f"No. {adj} passport holders can enter Colombia visa-free for up to 90 days for tourism or short business visits."
            },
            {
                "q": f"How long can {adj} citizens stay in Colombia without a visa?",
                "a": "Up to 90 days per entry. This can be extended once for another 90 days, for a maximum of 180 days per calendar year."
            },
            {
                "q": "What is the Check-Mig form and is it required?",
                "a": "The Check-Mig is Colombia's online pre-registration form for travellers. It must be completed before arrival and is required for most international travellers entering Colombia."
            },
        ]

    return {
        "country": country,
        "country_slug": country_slug,
        "visa_required": visa_required,
        "max_stay": max_stay,
        "fee": fee,
        "processing": processing,
        "apply_at": apply_at,
        "status_heading": status_heading,
        "status_body": status_body,
        "req_items": req_items,
        "how_to": how_to,
        "tips": tips,
        "faq": faq,
        "official_page": "colombia-visa-requirements.html",
        "official_label": "Colombia Visa Requirements",
        "fees_page": "colombia-visa-fees.html",
        "processing_page": "colombia-visa-processing-time.html",
        "flag_code": "co",
    }


# ---------------------------------------------------------------------------
# Costa Rica data builder
# ---------------------------------------------------------------------------
def costa_rica_data(nat_slug, adj):
    country = "Costa Rica"
    country_slug = "costa-rica"

    if nat_slug in COSTA_RICA_REQUIRED:
        visa_required = '<span style="color:red;font-weight:600;">Visa Required</span>'
        max_stay = "Up to 90 days (if visa granted)"
        fee = "USD 30–100 (varies by consulate)"
        processing = "5–15 business days"
        apply_at = "Costa Rican Embassy / Consulate"
        status_heading = f"Do {adj} Citizens Need a Visa for Costa Rica?"
        status_body = (
            f"{adj} passport holders require a <strong>Costa Rican visa</strong> to enter the country. "
            f"Applications must be submitted in person or by mail at the nearest Costa Rican Embassy or Consulate. "
            f"Fees vary by consulate but are typically in the range of <strong>USD 30–100</strong>. "
            f"Processing usually takes <strong>5–15 business days</strong>. "
            f"Check the official Costa Rican Ministry of Foreign Affairs website at "
            f"<a href='https://www.rree.go.cr' target='_blank' rel='noopener'>rree.go.cr</a> for the consulate nearest you."
        )
        req_items = [
            "Valid passport (at least 6 months validity beyond the intended stay; at least 2 blank pages)",
            "Completed and signed Costa Rica visa application form",
            "Recent passport-size photograph (white background)",
            "Bank statements for the last 3–6 months (proof of sufficient funds, approximately USD 100/week)",
            "Round-trip flight itinerary",
            "Proof of accommodation (hotel reservation or host invitation letter)",
            "Employment letter, proof of business ownership, or proof of student enrolment",
            "Visa fee (amount varies by consulate; ask your nearest Costa Rican mission for details)",
            "Travel health insurance covering the duration of stay in Costa Rica",
        ]
        how_to = (
            "<ol>"
            "<li><strong>Locate the nearest Costa Rican Embassy or Consulate</strong> via "
            "<a href='https://www.rree.go.cr' target='_blank' rel='noopener'>rree.go.cr</a>.</li>"
            "<li><strong>Download the visa application form</strong> from the consulate's website or collect it in person.</li>"
            "<li><strong>Gather all required documents</strong> — see the list above.</li>"
            "<li><strong>Submit the application</strong> — in person or by mail (check with your consulate for accepted methods).</li>"
            "<li><strong>Pay the visa fee</strong> — amount varies by consulate, typically USD 30–100.</li>"
            "<li><strong>Wait for the decision</strong> — processing takes 5–15 business days. The consulate will contact you.</li>"
            "<li><strong>Receive your visa</strong> — if approved, the visa sticker is affixed to your passport and returned to you.</li>"
            "</ol>"
            "<p>Official website: <a href='https://www.rree.go.cr' target='_blank' rel='noopener'>rree.go.cr</a></p>"
        )
        tips = [
            "Contact your nearest Costa Rican consulate well in advance — processing times can vary significantly.",
            "Ensure your travel insurance policy explicitly covers Costa Rica.",
            "Costa Rica requires proof of onward/return travel — carry your return ticket confirmation.",
            "The official currency is CRC (Costa Rican Colón); USD is widely accepted but carry local currency for rural areas.",
            "Vaccinations for Hepatitis A and Typhoid are recommended for Costa Rica travellers.",
        ]
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for Costa Rica?",
                "a": f"Yes. {adj} passport holders must obtain a Costa Rican visa from the nearest Embassy or Consulate before travelling."
            },
            {
                "q": f"How much does a Costa Rica visa cost for {adj} citizens?",
                "a": "Visa fees vary by consulate but are typically in the range of USD 30–100. Contact your nearest Costa Rican mission for the exact fee."
            },
            {
                "q": f"How long does Costa Rica visa processing take for {adj} applicants?",
                "a": "Processing typically takes 5–15 business days, though times may vary by consulate and season."
            },
        ]
    else:
        # Visa-free 90 days
        visa_required = '<span style="color:green;font-weight:600;">Visa-Free — 90 Days</span>'
        max_stay = "90 days"
        fee = "Free"
        processing = "N/A — no application required"
        apply_at = "Immigration at port of entry"
        status_heading = f"Do {adj} Citizens Need a Visa for Costa Rica?"
        status_body = (
            f"{adj} passport holders enjoy <strong>visa-free access to Costa Rica</strong>. "
            f"Stays of up to <strong>90 days</strong> for tourism or business require no advance visa or "
            f"pre-travel authorisation. Simply arrive with a valid passport and onward/return travel."
        )
        req_items = [
            "Valid passport (6+ months validity recommended beyond your planned departure from Costa Rica)",
            "Return or onward travel ticket out of Costa Rica (immigration may ask for this)",
            "Proof of accommodation (hotel reservation or host address)",
            "Proof of sufficient funds (approximately USD 100 per week; credit card or cash)",
            "Travel health insurance (strongly recommended)",
        ]
        how_to = (
            "<p>No visa application is required for stays up to 90 days.</p>"
            "<ol>"
            "<li><strong>Book your trip</strong> — ensure your passport will be valid for the duration of your stay.</li>"
            "<li><strong>Purchase a return or onward ticket</strong> — Costa Rican immigration may deny entry without proof of departure.</li>"
            "<li><strong>Arrive at a Costa Rican port of entry</strong> — present your passport, return ticket, and proof of accommodation to the immigration officer.</li>"
            "<li><strong>Receive your entry stamp</strong> — the officer will stamp your passport with up to 90 days.</li>"
            "</ol>"
            "<p>For stays beyond 90 days, you must leave Costa Rica (even briefly) or apply for a longer-term residency. "
            "Contact the Dirección General de Migración y Extranjería at "
            "<a href='https://www.migracion.go.cr' target='_blank' rel='noopener'>migracion.go.cr</a> for details.</p>"
        )
        tips = [
            "Always carry a printed or digital return ticket — Costa Rican immigration officers regularly request it.",
            "Costa Rica is part of the CA-4 agreement (with Nicaragua, Honduras, El Salvador, Guatemala) — time in those countries may count toward your 90-day limit.",
            "Travel insurance covering medical evacuation is strongly recommended given Costa Rica's active volcano and jungle terrain.",
            "The official currency is CRC (Costa Rican Colón); USD is widely accepted in tourist areas.",
            "Driving in Costa Rica requires an International Driving Permit (IDP) alongside your national driving licence.",
        ]
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for Costa Rica?",
                "a": f"No. {adj} passport holders can enter Costa Rica visa-free for up to 90 days for tourism or business."
            },
            {
                "q": f"How long can {adj} citizens stay in Costa Rica without a visa?",
                "a": "Up to 90 days per entry. For longer stays, you must leave the country or apply for a residency permit."
            },
            {
                "q": "Is a return ticket required to enter Costa Rica visa-free?",
                "a": "Yes. Costa Rican immigration routinely requires proof of onward or return travel. Ensure you have a confirmed return or connecting ticket before arrival."
            },
        ]

    return {
        "country": country,
        "country_slug": country_slug,
        "visa_required": visa_required,
        "max_stay": max_stay,
        "fee": fee,
        "processing": processing,
        "apply_at": apply_at,
        "status_heading": status_heading,
        "status_body": status_body,
        "req_items": req_items,
        "how_to": how_to,
        "tips": tips,
        "faq": faq,
        "official_page": "costa-rica-visa-requirements.html",
        "official_label": "Costa Rica Visa Requirements",
        "fees_page": "costa-rica-visa-fees.html",
        "processing_page": "costa-rica-visa-processing-time.html",
        "flag_code": "cr",
    }


# ---------------------------------------------------------------------------
# HTML builder
# ---------------------------------------------------------------------------
def build_page(data, nat_slug, nat_label, nat_adj, nat_fi, related_slugs):
    country = data["country"]
    country_slug = data["country_slug"]
    slug = f"{country_slug}-visa-for-{nat_slug}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    title = f"{country} Visa for {nat_label} Citizens 2026 — Requirements, Fees &amp; How to Apply"
    country_fi = data["flag_code"]

    # Meta description
    if nat_slug in COLOMBIA_REQUIRED and country_slug == "colombia":
        desc = (f"{nat_adj} citizens need a Colombian visa in 2026. "
                f"USD 52 fee, apply online at cancilleria.gov.co. Requirements, processing time and tips.")
    elif country_slug == "colombia":
        desc = (f"{nat_adj} citizens travel to Colombia visa-free for 90 days in 2026. "
                f"Complete guide: Check-Mig form, entry requirements, extension tips.")
    elif nat_slug in COSTA_RICA_REQUIRED and country_slug == "costa-rica":
        desc = (f"{nat_adj} citizens need a visa for Costa Rica in 2026. "
                f"Apply at the Costa Rican Consulate. Requirements, fees and processing times.")
    else:
        desc = (f"{nat_adj} citizens enjoy visa-free entry to Costa Rica for 90 days in 2026. "
                f"Entry requirements, return ticket rules, CA-4 travel tips and what to prepare.")
    desc = desc[:155]

    # JSON-LD FAQ
    faq_items = []
    for item in data["faq"]:
        q_escaped = item["q"].replace('"', '&quot;')
        a_escaped = item["a"].replace('"', '&quot;')
        faq_items.append(
            f'{{"@type":"Question","name":"{q_escaped}","acceptedAnswer":{{"@type":"Answer","text":"{a_escaped}"}}}}'
        )
    faq_json = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(faq_items) + "]}"

    # Requirements list
    req_html = "<ul>\n" + "".join(f"          <li>{r}</li>\n" for r in data["req_items"]) + "        </ul>"

    # Tips list
    tips_html = "<ul>\n" + "".join(f"          <li>{t}</li>\n" for t in data["tips"]) + "        </ul>"

    # Related nationality links (same country)
    related_links = ""
    for rslug in related_slugs:
        rlabel = rslug.replace("-", " ").title()
        rfile = f"{country_slug}-visa-for-{rslug}-citizens.html"
        related_links += (
            f'        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{rfile}">'
            f'{country} Visa &mdash; {rlabel} Citizens</a>\n'
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
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{canonical}"/>
    <link rel="alternate" hreflang="x-default" href="{canonical}"/>
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
    {faq_json}
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
            <span class="fi fi-gb"></span> English
          </a>
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
</nav>

<section class="ftco-section">
  <div class="container">
    <article class="country-page">

      <h1><span class="fi fi-{nat_fi} mr-2"></span><span class="fi fi-{country_fi} mr-2"></span>{country} Visa for {nat_label} Citizens 2026</h1>

      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; {nat_label} Citizens &amp; {country}</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td>{data["visa_required"]}</td></tr>
          <tr><th>Max Stay</th><td>{data["max_stay"]}</td></tr>
          <tr><th>Fee</th><td>{data["fee"]}</td></tr>
          <tr><th>Processing Time</th><td>{data["processing"]}</td></tr>
          <tr><th>Apply At</th><td>{data["apply_at"]}</td></tr>
        </tbody>
      </table>

      <h2>{data["status_heading"]}</h2>
      <p>{data["status_body"]}</p>

      <h2>Requirements for {nat_adj} Citizens</h2>
        {req_html}

      <h2>How to Apply</h2>
      {data["how_to"]}

      <h2>Tips for {nat_adj} Travellers to {country}</h2>
        {tips_html}

      <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
        <strong>Editorial Team &mdash; eVisa-Card.com</strong>
        <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at the official government source before travel.</p>
      </div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Guides</h3>
      <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{data["official_page"]}">{data["official_label"]}</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{data["fees_page"]}">{country} Visa Fees</a>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{data["processing_page"]}">{country} Processing Times</a>
{related_links}        <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#x2192;</a>
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
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    for nat_slug, nat_label, nat_adj, nat_fi, related_slugs in NATIONALITIES:
        for country_fn in (colombia_data, costa_rica_data):
            data = country_fn(nat_slug, nat_adj)
            country_slug = data["country_slug"]
            filename = f"{country_slug}-visa-for-{nat_slug}-citizens.html"
            filepath = os.path.join(OUTPUT_DIR, filename)
            html = build_page(data, nat_slug, nat_label, nat_adj, nat_fi, related_slugs)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  Created: {filename}")

    print(f"\nDone. {len(created)} files created.")
    return created


if __name__ == "__main__":
    main()
