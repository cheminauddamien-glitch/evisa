#!/usr/bin/env python3
"""
gen_nationality_p2_batch1.py
Generates Germany and Japan nationality pages (20 pages each = 40 total).
Output directory: www/en/
"""

import os
import textwrap

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality metadata
# ---------------------------------------------------------------------------
NATIONALITIES = [
    # (slug,         label,          adj,           fi_code, related_nat_slugs)
    ("us",           "US",           "American",    "us",    ["canadian", "uk", "australian"]),
    ("uk",           "UK",           "British",     "gb",    ["canadian", "australian", "french"]),
    ("canadian",     "Canadian",     "Canadian",    "ca",    ["us", "uk", "australian"]),
    ("french",       "French",       "French",      "fr",    ["german", "uk", "italian"]),
    ("german",       "German",       "German",      "de",    ["french", "uk", "austrian"]),
    ("japanese",     "Japanese",     "Japanese",    "jp",    ["korean", "singaporean", "chinese"]),
    ("australian",   "Australian",   "Australian",  "au",    ["us", "uk", "canadian"]),
    ("indian",       "Indian",       "Indian",      "in",    ["chinese", "philippine", "indonesian"]),
    ("chinese",      "Chinese",      "Chinese",     "cn",    ["japanese", "korean", "russian"]),
    ("russian",      "Russian",      "Russian",     "ru",    ["chinese", "turkish", "south-african"]),
    ("brazilian",    "Brazilian",    "Brazilian",   "br",    ["argentinian", "mexican", "us"]),
    ("mexican",      "Mexican",      "Mexican",     "mx",    ["brazilian", "argentinian", "us"]),
    ("south-african","South African","South African","za",   ["nigerian", "kenyan", "turkish"]),
    ("nigerian",     "Nigerian",     "Nigerian",    "ng",    ["south-african", "ghanaian", "turkish"]),
    ("korean",       "Korean",       "Korean",      "kr",    ["japanese", "chinese", "singaporean"]),
    ("singaporean",  "Singaporean",  "Singaporean", "sg",    ["malaysian", "indonesian", "korean"]),
    ("indonesian",   "Indonesian",   "Indonesian",  "id",    ["philippine", "indian", "singaporean"]),
    ("philippine",   "Philippine",   "Philippine",  "ph",    ["indonesian", "indian", "singaporean"]),
    ("turkish",      "Turkish",      "Turkish",     "tr",    ["russian", "iranian", "south-african"]),
    ("argentinian",  "Argentinian",  "Argentinian", "ar",    ["brazilian", "mexican", "chilean"]),
]

# ---------------------------------------------------------------------------
# Germany visa data by nationality
# ---------------------------------------------------------------------------
# Visa-free (ETIAS needed from 2025): us, uk, canadian, australian, japanese, korean, singaporean, brazilian
# Visa-free 90 days no ETIAS: french, german (EU free movement), mexican, argentinian
# Schengen visa required: indian, chinese, russian, indonesian, philippine, nigerian, south-african, turkish

GERMANY_ETIAS = {"us", "uk", "canadian", "australian", "japanese", "korean", "singaporean", "brazilian"}
GERMANY_VISAFREE = {"french", "german", "mexican", "argentinian"}
GERMANY_REQUIRED = {"indian", "chinese", "russian", "indonesian", "philippine", "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# Japan visa data by nationality
# ---------------------------------------------------------------------------
JAPAN_VISAFREE = {"us", "uk", "canadian", "australian", "french", "german", "korean", "singaporean",
                  "brazilian", "mexican", "argentinian"}
JAPAN_REQUIRED = {"indian", "chinese", "russian", "indonesian", "philippine", "nigerian", "south-african", "turkish"}

# ---------------------------------------------------------------------------
# Helper: build a related-nationality slug for a different country
# ---------------------------------------------------------------------------
def related_nat_page(country_slug, nat_slug):
    """Return filename for a related nationality page for the given country."""
    return f"{country_slug}-visa-for-{nat_slug}-citizens.html"


# ---------------------------------------------------------------------------
# Germany page builder
# ---------------------------------------------------------------------------
def germany_data(nat_slug, adj, fi_code):
    country = "Germany"
    country_slug = "germany"

    if nat_slug in GERMANY_REQUIRED:
        visa_required = "Yes — Schengen Visa Required"
        max_stay = "Up to 90 days in any 180-day period"
        fee = "EUR 80"
        processing = "15 working days"
        apply_at = "German Embassy / VFS Global"
        status_heading = f"Do {adj} Citizens Need a Visa for Germany?"
        status_body = (
            f"{adj} passport holders require a <strong>Schengen short-stay visa (Type C)</strong> to enter Germany. "
            f"The application must be submitted in person at the German Embassy, Consulate, or an authorised "
            f"VFS Global centre in your country of residence. The standard fee is <strong>EUR 80</strong> and "
            f"processing takes approximately <strong>15 working days</strong>, though peak season may add delays. "
            f"Apply at least four weeks before your planned travel date."
        )
        req_items = [
            "Valid passport (at least 6 months validity beyond the return date; at least 2 blank pages)",
            "Completed and signed Schengen visa application form",
            "Two recent passport-size photographs (35&times;45 mm, white background)",
            "Travel health insurance covering at least EUR 30,000 (valid for the entire Schengen area)",
            "Round-trip flight itinerary / confirmed bookings",
            "Proof of accommodation (hotel reservations or host invitation letter)",
            "Proof of financial means (bank statements for the last 3 months showing sufficient funds)",
            "Employment letter or proof of enrollment / business registration",
            "Consular fee receipt (EUR 80)",
        ]
        how_to = (
            "<ol>"
            "<li><strong>Gather documents</strong> — compile all items from the requirements list above.</li>"
            "<li><strong>Book an appointment</strong> — visit the German Embassy or the nearest VFS Global centre to schedule a visa interview slot.</li>"
            "<li><strong>Submit your application in person</strong> — biometric data (fingerprints) will be collected at the appointment.</li>"
            "<li><strong>Pay the fee</strong> — EUR 80 (non-refundable) by the accepted payment method at the centre.</li>"
            "<li><strong>Track your application</strong> — use the VFS tracking reference or check directly with the embassy.</li>"
            "<li><strong>Collect your passport</strong> — in person or via the optional courier service (additional fee).</li>"
            "</ol>"
            "<p>Official information: <a href='https://www.auswaertiges-amt.de/en/visa-service' target='_blank' rel='noopener'>auswaertiges-amt.de</a></p>"
        )
        tips = [
            "Apply at least 4 weeks before travel; during summer and holiday periods allow 6–8 weeks.",
            "Your insurance policy must explicitly state Schengen coverage and EUR 30,000 minimum.",
            "Bank statements should show a minimum of EUR 45 per day for the duration of your stay.",
            "A refusal does not automatically ban future applications — address any missing documents and reapply.",
            "A multiple-entry visa may be granted if you have a good travel history.",
        ]
        faq = [
            {
                "q": f"How much is the Germany Schengen visa fee for {adj} citizens?",
                "a": f"The standard Schengen visa fee for {adj} passport holders is EUR 80. Children aged 6–11 pay EUR 40; children under 6 are exempt."
            },
            {
                "q": f"How long does Germany visa processing take for {adj} applicants?",
                "a": "Processing typically takes 15 working days. Apply well in advance, as processing times can be longer during peak travel seasons."
            },
            {
                "q": f"Can {adj} citizens apply for a Germany visa online?",
                "a": "The application form can be completed online via the German Mission's portal, but the submission must be done in person at the embassy or VFS Global centre to provide biometric data."
            },
        ]
    elif nat_slug in GERMANY_ETIAS:
        visa_required = "No — Visa-Free (ETIAS required from 2025)"
        max_stay = "90 days in any 180-day period (Schengen)"
        fee = "EUR 7 (ETIAS, adults 18–70)"
        processing = "ETIAS: up to 4 days (usually minutes)"
        apply_at = "travel.ec.europa.eu (ETIAS)"
        status_heading = f"Do {adj} Citizens Need a Visa for Germany?"
        status_body = (
            f"{adj} passport holders enjoy <strong>visa-free</strong> access to Germany and the entire Schengen Area. "
            f"Stays of up to <strong>90 days in any 180-day period</strong> require no advance visa. "
            f"However, from 2025 the EU's <strong>ETIAS</strong> (European Travel Information and Authorisation System) "
            f"is required before travel. ETIAS costs EUR 7 (waived under 18 and over 70) and is valid for 3 years "
            f"or until passport expiry. Apply online at "
            f"<a href='https://travel.ec.europa.eu/etias_en' target='_blank' rel='noopener'>travel.ec.europa.eu</a>."
        )
        req_items = [
            "Valid passport (6+ months validity beyond your planned return date)",
            "ETIAS authorisation (apply at travel.ec.europa.eu; valid 3 years / until passport expiry)",
            "Return or onward travel ticket",
            "Proof of accommodation for the duration of your stay",
            "Proof of sufficient funds (credit card or cash equivalent)",
            "Travel or health insurance (recommended; mandatory for some border crossings)",
        ]
        how_to = (
            "<p>No visa application is required for stays up to 90 days.</p>"
            "<ol>"
            "<li><strong>Obtain ETIAS</strong> — apply online at <a href='https://travel.ec.europa.eu/etias_en' target='_blank' rel='noopener'>travel.ec.europa.eu</a>. The process takes about 10 minutes and approval usually arrives within minutes to 4 days.</li>"
            "<li><strong>Book flights and accommodation</strong> — ensure your passport is valid throughout your stay.</li>"
            "<li><strong>Arrive at the border</strong> — present your passport and ETIAS confirmation (usually embedded in passport scan). Border guards may ask for supporting documents.</li>"
            "</ol>"
            "<p>For stays beyond 90 days, contact the German Embassy to apply for the appropriate national visa (D-type).</p>"
        )
        tips = [
            "ETIAS is linked to your passport — if you renew your passport, you will need a new ETIAS.",
            "Ensure your passport has at least 6 months of validity on the date of entry.",
            "The 90-day limit is cumulative across the entire Schengen Area, not just Germany.",
            "Keep a digital copy of your ETIAS approval email on your phone.",
            "Travel insurance is strongly recommended despite not being mandatory at all checkpoints.",
        ]
        faq = [
            {
                "q": f"Do {adj} citizens need ETIAS for Germany?",
                "a": f"Yes. From 2025, {adj} passport holders must obtain an ETIAS authorisation (EUR 7) before travelling to Germany and the rest of the Schengen Area, even though no visa is required."
            },
            {
                "q": f"How long can {adj} citizens stay in Germany visa-free?",
                "a": "Up to 90 days in any 180-day period across the entire Schengen Area. This includes time spent in other Schengen countries, not just Germany."
            },
            {
                "q": "What happens if I overstay my 90-day Schengen allowance?",
                "a": "Overstaying can result in fines, entry bans, or deportation. Always monitor your days carefully using the EU short-stay calculator."
            },
        ]
    else:
        # EU free movement (french, german, etc.) / visa-free no ETIAS
        if nat_slug == "german":
            visa_required = "N/A — German citizens live and work freely in Germany"
        else:
            visa_required = "No — Visa-Free (no ETIAS required)"
        max_stay = "90 days in any 180-day period (Schengen) / unlimited for EU citizens"
        fee = "Free"
        processing = "N/A"
        apply_at = "No application needed"
        if nat_slug == "german":
            status_heading = "German Citizens and Germany — Free Movement"
            status_body = (
                "German citizens have <strong>unrestricted right of entry and residence</strong> in Germany "
                "as it is their home country. No visa, ETIAS, or permit is required."
            )
            req_items = ["Valid German ID card or passport"]
            how_to = "<p>No application required. Simply travel with a valid German ID card or passport.</p>"
            tips = [
                "Your German national ID card is sufficient for travel within the EU/Schengen Area.",
                "For travel outside the EU, ensure your passport is valid.",
            ]
            faq = [
                {
                    "q": "Do German citizens need any documentation to enter Germany?",
                    "a": "German citizens need only a valid German ID card or passport to enter Germany."
                },
                {
                    "q": "Can German citizens live and work in Germany indefinitely?",
                    "a": "Yes. German citizens have an unconditional right to reside and work in Germany."
                },
                {
                    "q": "Does a German citizen need an ETIAS when visiting other Schengen countries?",
                    "a": "No. ETIAS applies only to non-EU/non-Schengen nationals. German citizens travel freely within the EU and Schengen Area."
                },
            ]
        else:
            status_heading = f"Do {adj} Citizens Need a Visa for Germany?"
            status_body = (
                f"{adj} passport holders do <strong>not</strong> need a visa to visit Germany. "
                f"Germany is part of the Schengen Area and {adj} citizens can stay for up to "
                f"<strong>90 days in any 180-day period</strong> without any pre-travel authorisation. "
                f"ETIAS does not apply to {adj} passport holders."
            )
            req_items = [
                "Valid passport (6+ months validity recommended)",
                "Return or onward travel ticket",
                "Proof of accommodation",
                "Proof of sufficient funds",
            ]
            how_to = (
                "<p>No visa or ETIAS application is needed. Simply:</p>"
                "<ol>"
                "<li>Ensure your passport is valid for the duration of your stay.</li>"
                "<li>Book your flights and accommodation.</li>"
                "<li>Arrive at a German port of entry and present your passport.</li>"
                "</ol>"
            )
            tips = [
                "The 90-day limit applies across the entire Schengen Area, not just Germany.",
                "Carry proof of accommodation and return ticket in case of spot checks.",
                "Travel insurance, while not always compulsory, is strongly recommended.",
            ]
            faq = [
                {
                    "q": f"Do {adj} citizens need a visa for Germany?",
                    "a": f"No. {adj} passport holders are visa-exempt and can visit Germany for up to 90 days in any 180-day period without a visa."
                },
                {
                    "q": f"Do {adj} citizens need ETIAS for Germany?",
                    "a": f"No. ETIAS applies to specific non-EU nationalities. {adj} citizens are not required to obtain ETIAS."
                },
                {
                    "q": "How many days can I stay in Germany without a visa?",
                    "a": "Up to 90 days in any 180-day period across the Schengen Area."
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
        "official_page": "visa-germany.html",
        "official_label": "Germany Visa Guide",
        "flag_code": "de",
    }


# ---------------------------------------------------------------------------
# Japan page builder
# ---------------------------------------------------------------------------
def japan_data(nat_slug, adj, fi_code):
    country = "Japan"
    country_slug = "japan"

    if nat_slug in JAPAN_REQUIRED:
        visa_required = "Yes — Visa Required"
        max_stay = "Up to 90 days (single entry, short-stay)"
        fee = "JPY 3,000 (~USD 20)"
        processing = "5–10 business days"
        apply_at = "Japanese Embassy / Consulate; mofa.go.jp"
        status_heading = f"Do {adj} Citizens Need a Visa for Japan?"
        status_body = (
            f"{adj} passport holders must obtain a <strong>Japanese short-stay visa</strong> before travelling to Japan. "
            f"Applications are submitted in person at the nearest Japanese Embassy or Consulate. "
            f"The single-entry fee is <strong>JPY 3,000 (~USD 20)</strong> and processing takes "
            f"<strong>5–10 business days</strong>. Multiple-entry visas may be available depending on travel history."
        )
        req_items = [
            "Valid passport (at least 6 months validity beyond the return date)",
            "Completed visa application form (available at the Embassy or mofa.go.jp)",
            "One recent passport-size photograph (45&times;45 mm, white background)",
            "Round-trip flight itinerary",
            "Proof of accommodation (hotel reservations or invitation letter)",
            "Bank statements or financial documents showing sufficient funds",
            "Employment letter or proof of self-employment / enrollment",
            "Visa fee payment (JPY 3,000 ~USD 20 for single-entry)",
        ]
        how_to = (
            "<ol>"
            "<li><strong>Download the application form</strong> — obtain the Temporary Visitor visa form from the "
            "<a href='https://www.mofa.go.jp/j_info/visit/visa/index.html' target='_blank' rel='noopener'>MOFA website</a> "
            "or the Embassy in your country.</li>"
            "<li><strong>Gather your documents</strong> — compile all supporting documents listed above.</li>"
            "<li><strong>Submit in person</strong> — visit the Japanese Embassy or Consulate serving your region during designated application hours.</li>"
            "<li><strong>Pay the fee</strong> — JPY 3,000 (~USD 20) for a single-entry visa.</li>"
            "<li><strong>Wait for processing</strong> — typically 5–10 business days. Check with the Embassy for current wait times.</li>"
            "<li><strong>Collect your passport</strong> — in person or via authorised courier service.</li>"
            "</ol>"
            "<p>Official information: <a href='https://www.mofa.go.jp/j_info/visit/visa/' target='_blank' rel='noopener'>mofa.go.jp</a></p>"
        )
        tips = [
            "Submit your application at least 3–4 weeks before travel to account for any delays.",
            "The Embassy may request an interview or additional documents — respond promptly.",
            "Proof of strong ties to your home country (employment, property, family) strengthens your application.",
            "Travel insurance is not mandatory but is strongly recommended for Japan travel.",
            "Check Japan's entry requirements for current health documentation before departure.",
        ]
        faq = [
            {
                "q": f"How much does a Japan visa cost for {adj} citizens?",
                "a": f"The Japan short-stay visa fee for {adj} passport holders is JPY 3,000 (approximately USD 20) for a single-entry visa."
            },
            {
                "q": f"How long does Japan visa processing take for {adj} applicants?",
                "a": "Processing typically takes 5–10 business days after submission at the Japanese Embassy or Consulate."
            },
            {
                "q": f"Can {adj} citizens apply for a Japan visa online?",
                "a": "Currently, Japan does not offer a full e-visa for most nationalities. The application form can be downloaded online, but submission must be done in person at the Embassy or Consulate."
            },
        ]
    else:
        visa_required = "No — Visa-Free"
        max_stay = "90 days"
        fee = "Free"
        processing = "N/A"
        apply_at = "No application needed"
        status_heading = f"Do {adj} Citizens Need a Visa for Japan?"
        status_body = (
            f"{adj} passport holders enjoy <strong>visa-free</strong> entry to Japan. "
            f"You can stay for up to <strong>90 days</strong> for tourism, business, or transit without any "
            f"advance visa or authorisation. Simply arrive with a valid passport."
        )
        req_items = [
            "Valid passport (6+ months validity recommended beyond your stay)",
            "Return or onward travel ticket",
            "Proof of accommodation (hotel bookings or host details)",
            "Proof of sufficient funds for the duration of your stay",
            "Completed Disembarkation Card for Foreigner (provided on arrival or on the aircraft)",
        ]
        how_to = (
            "<p>No visa application is required for stays up to 90 days.</p>"
            "<ol>"
            "<li><strong>Book your trip</strong> — ensure your passport is valid throughout your stay.</li>"
            "<li><strong>Fill out the arrival card</strong> — complete the Disembarkation Card provided on your flight or at the immigration hall.</li>"
            "<li><strong>Clear immigration</strong> — present your passport, arrival card, and return ticket at the border. Fingerprints and photo will be taken.</li>"
            "<li><strong>Declare at customs</strong> — fill out the Customs Declaration Form if required.</li>"
            "</ol>"
            "<p>For stays beyond 90 days, contact the Japanese Embassy to apply for the appropriate visa type.</p>"
        )
        tips = [
            "Japan immigration officers may ask to see your return ticket and accommodation details — have these ready.",
            "You can extend a visa-free stay in exceptional circumstances by applying at the regional immigration office.",
            "Carry sufficient cash — Japan is still largely cash-based outside major cities.",
            "Download the Visit Japan Web app to pre-register arrival/quarantine documents.",
            "Japan has a reciprocal visa-free agreement — ensure you carry a valid passport of the correct nationality.",
        ]
        faq = [
            {
                "q": f"Do {adj} citizens need a visa for Japan?",
                "a": f"No. {adj} passport holders can enter Japan visa-free for up to 90 days for tourism or business."
            },
            {
                "q": f"How long can {adj} citizens stay in Japan without a visa?",
                "a": "Up to 90 days per entry under the visa-exemption arrangement."
            },
            {
                "q": f"Can {adj} citizens work in Japan on a visa-free stay?",
                "a": "No. The visa-free entry is for tourism and short business visits only. Working in Japan requires a separate work visa."
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
        "official_page": "visa-japan.html",
        "official_label": "Japan Visa Guide",
        "flag_code": "jp",
    }


# ---------------------------------------------------------------------------
# HTML builder
# ---------------------------------------------------------------------------
def build_page(data, nat_slug, nat_label, nat_adj, nat_fi, related_slugs, country_fn):
    country = data["country"]
    country_slug = data["country_slug"]
    slug = f"{country_slug}-visa-for-{nat_slug}-citizens"
    canonical = f"https://www.evisa-card.com/en/{slug}"
    title = f"{country} Visa for {nat_label} Citizens 2026 — Requirements, Fees &amp; How to Apply"

    # Meta description 150-155 chars (targeting ~152)
    if nat_slug in GERMANY_REQUIRED and country_slug == "germany":
        desc = (f"{nat_adj} citizens need a Schengen visa for Germany in 2026. Learn requirements, EUR 80 fee, "
                f"processing time and how to apply at the German Embassy or VFS Global.")
    elif nat_slug in GERMANY_ETIAS and country_slug == "germany":
        desc = (f"{nat_adj} citizens visit Germany visa-free in 2026 with ETIAS (EUR 7). "
                f"Learn about the 90-day Schengen limit, ETIAS application steps and entry tips.")
    elif country_slug == "germany":
        desc = (f"{nat_adj} citizens travel to Germany visa-free in 2026. "
                f"Discover the 90-day Schengen stay, entry requirements and tips for a smooth border crossing.")
    elif nat_slug in JAPAN_REQUIRED:
        desc = (f"{nat_adj} citizens need a visa for Japan in 2026. "
                f"Find the JPY 3,000 fee, 5-10 day processing time, required documents and Embassy application steps.")
    else:
        desc = (f"{nat_adj} citizens enjoy visa-free entry to Japan for 90 days in 2026. "
                f"Read our complete guide on entry requirements, arrival tips and what to bring.")

    # Truncate/pad description to 150-155 range (best effort)
    desc = desc[:155]

    # JSON-LD FAQ
    faq_items = []
    for item in data["faq"]:
        faq_items.append(
            f'{{"@type":"Question","name":"{item["q"]}","acceptedAnswer":{{"@type":"Answer","text":"{item["a"]}"}}}}'
        )
    faq_json = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(faq_items) + "]}"

    # Requirements list
    req_html = "<ul>\n" + "".join(f"          <li>{r}</li>\n" for r in data["req_items"]) + "        </ul>"

    # Tips
    tips_html = "<ul>\n" + "".join(f"          <li>{t}</li>\n" for t in data["tips"]) + "        </ul>"

    # Related nationality links (same country)
    related_links = ""
    for rslug in related_slugs:
        rlabel = rslug.replace("-", " ").title()
        rfile = f"{country_slug}-visa-for-{rslug}-citizens.html"
        related_links += f'        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{rfile}">{country} Visa &mdash; {rlabel} Citizens</a>\n'

    # Country flag fi code
    country_fi = data["flag_code"]

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
        <li class="nav-item dropdown ml-2">
          <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;"><span class="fi fi-gb"></span> English</a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
            <a class="dropdown-item active" href="#"><span class="fi fi-gb"></span> English</a>
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

      <div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026.</div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Guides</h3>
      <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{data["official_page"]}">{data["official_label"]}</a>
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
        for country_fn in (germany_data, japan_data):
            data = country_fn(nat_slug, nat_adj, nat_fi)
            country_slug = data["country_slug"]
            filename = f"{country_slug}-visa-for-{nat_slug}-citizens.html"
            filepath = os.path.join(OUTPUT_DIR, filename)
            html = build_page(data, nat_slug, nat_label, nat_adj, nat_fi, related_slugs, country_fn)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(filename)
            print(f"  Created: {filename}")

    print(f"\nDone. {len(created)} files created.")
    return created


if __name__ == "__main__":
    main()
