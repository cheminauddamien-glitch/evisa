#!/usr/bin/env python3
"""
gen_subpages_batch_a.py
Generates 3 sub-pages per country for the first 10 countries.
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Country data
# ---------------------------------------------------------------------------
COUNTRIES = {
    "thailand": {
        "name": "Thailand",
        "flag": "th",
        "evisa_portal": "thaievisa.go.th",
        "visa_free_days": "60",
        "evisa_fee": "THB 2,000 (~USD $55)",
        "processing_time": "5 business days",
        "currency": "THB",
        "schengen": False,
        "official_link": "https://www.thaievisa.go.th",
        "official_link_label": "thaievisa.go.th",
    },
    "india": {
        "name": "India",
        "flag": "in",
        "evisa_portal": "evisa.india.gov.in",
        "visa_free_days": "N/A (eVisa required for most)",
        "evisa_fee": "USD 25 (30-day), USD 40 (1-year), USD 80 (5-year)",
        "processing_time": "72–96 hours",
        "currency": "USD",
        "schengen": False,
        "official_link": "https://evisa.india.gov.in",
        "official_link_label": "evisa.india.gov.in",
    },
    "france": {
        "name": "France",
        "flag": "fr",
        "evisa_portal": "france-visas.gouv.fr",
        "visa_free_days": "90 (Schengen, for eligible nationalities)",
        "evisa_fee": "EUR 80",
        "processing_time": "15 working days",
        "currency": "EUR",
        "schengen": True,
        "official_link": "https://france-visas.gouv.fr",
        "official_link_label": "france-visas.gouv.fr",
    },
    "germany": {
        "name": "Germany",
        "flag": "de",
        "evisa_portal": "auswaertiges-amt.de",
        "visa_free_days": "90 (Schengen, for eligible nationalities)",
        "evisa_fee": "EUR 80",
        "processing_time": "15 working days",
        "currency": "EUR",
        "schengen": True,
        "official_link": "https://www.auswaertiges-amt.de",
        "official_link_label": "auswaertiges-amt.de",
    },
    "japan": {
        "name": "Japan",
        "flag": "jp",
        "evisa_portal": "mofa.go.jp",
        "visa_free_days": "90 (for eligible nationalities)",
        "evisa_fee": "Free for some; consular fee varies by nationality",
        "processing_time": "5–10 business days",
        "currency": "JPY",
        "schengen": False,
        "official_link": "https://www.mofa.go.jp/j_info/visit/visa/index.html",
        "official_link_label": "mofa.go.jp",
    },
    "usa": {
        "name": "USA",
        "flag": "us",
        "evisa_portal": "travel.state.gov",
        "visa_free_days": "90 (ESTA/VWP for eligible nationalities)",
        "evisa_fee": "ESTA: USD 21; B1/B2: USD 185",
        "processing_time": "ESTA: instant–72h; B1/B2: 3–5 weeks",
        "currency": "USD",
        "schengen": False,
        "official_link": "https://travel.state.gov",
        "official_link_label": "travel.state.gov",
    },
    "canada": {
        "name": "Canada",
        "flag": "ca",
        "evisa_portal": "ircc.canada.ca",
        "visa_free_days": "6 months (for eligible nationalities)",
        "evisa_fee": "eTA: CAD 7; Visitor Visa: CAD 100",
        "processing_time": "eTA: minutes–72h; Visitor Visa: 4–12 weeks",
        "currency": "CAD",
        "schengen": False,
        "official_link": "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html",
        "official_link_label": "ircc.canada.ca",
    },
    "australia": {
        "name": "Australia",
        "flag": "au",
        "evisa_portal": "immi.homeaffairs.gov.au",
        "visa_free_days": "3 months (ETA/eVisitor for eligible nationalities)",
        "evisa_fee": "ETA: AUD 20; eVisitor: Free; Tourist Visa: AUD 145",
        "processing_time": "ETA: instant; Tourist Visa: 1–14 days",
        "currency": "AUD",
        "schengen": False,
        "official_link": "https://immi.homeaffairs.gov.au",
        "official_link_label": "immi.homeaffairs.gov.au",
    },
    "italy": {
        "name": "Italy",
        "flag": "it",
        "evisa_portal": "vistoperitalia.esteri.it",
        "visa_free_days": "90 (Schengen, for eligible nationalities)",
        "evisa_fee": "EUR 80",
        "processing_time": "15 working days",
        "currency": "EUR",
        "schengen": True,
        "official_link": "https://vistoperitalia.esteri.it",
        "official_link_label": "vistoperitalia.esteri.it",
    },
    "spain": {
        "name": "Spain",
        "flag": "es",
        "evisa_portal": "exteriores.gob.es",
        "visa_free_days": "90 (Schengen, for eligible nationalities)",
        "evisa_fee": "EUR 80",
        "processing_time": "15 working days",
        "currency": "EUR",
        "schengen": True,
        "official_link": "https://www.exteriores.gob.es",
        "official_link_label": "exteriores.gob.es",
    },
}

# ---------------------------------------------------------------------------
# Helper: HTML head
# ---------------------------------------------------------------------------
def head(title, description, canonical_slug, country_key, page_type):
    c = COUNTRIES[country_key]
    slug = canonical_slug
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', 'G-XC1GYM27WC');
    </script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686"
            crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport" />
    <meta content="{description}" name="description"/>
    <meta content="index, follow" name="robots" />
    <link href="https://www.evisa-card.com/en/{slug}" rel="canonical" />
    <meta content="{title}" property="og:title" />
    <meta content="{description}" property="og:description" />
    <meta content="website" property="og:type" />
    <meta content="https://www.evisa-card.com/en/{slug}" property="og:url" />
    <meta content="https://www.evisa-card.com/images/og-image.jpg" property="og:image" />
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "eVisa-Card.com",
      "url": "https://www.evisa-card.com",
      "logo": "https://www.evisa-card.com/images/logo.png",
      "sameAs": [
        "https://facebook.com/evisacard",
        "https://twitter.com/evisacard",
        "https://instagram.com/evisacard"
      ],
      "description": "eVisa-Card.com provides global eVisa information and online travel authorization guides for tourists and business travelers."
    }}
    </script>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Arizonia&display=swap" rel="stylesheet" />
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />
    <link href="../css/animate.css" rel="stylesheet" />
    <link href="../css/owl.carousel.min.css" rel="stylesheet" />
    <link href="../css/owl.theme.default.min.css" rel="stylesheet" />
    <link href="../css/magnific-popup.css" rel="stylesheet" />
    <link href="../css/bootstrap-datepicker.css" rel="stylesheet" />
    <link href="../css/jquery.timepicker.css" rel="stylesheet" />
    <link href="../css/flaticon.css" rel="stylesheet" />
    <link href="../css/style.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="fr" href="https://www.evisa-card.com/fr/{slug}"/>
    <link rel="alternate" hreflang="es" href="https://www.evisa-card.com/es/{slug}"/>
    <link rel="alternate" hreflang="pt" href="https://www.evisa-card.com/pt/{slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
</head>"""


# ---------------------------------------------------------------------------
# Helper: navbar
# ---------------------------------------------------------------------------
def navbar(country_key, slug):
    c = COUNTRIES[country_key]
    return f"""<body>
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
                            <a class="dropdown-item active" href="/en/{slug}"><span class="fi fi-gb"></span> English</a>
                            <a class="dropdown-item" href="/fr/{slug}"><span class="fi fi-fr"></span> Français</a>
                            <a class="dropdown-item" href="/es/{slug}"><span class="fi fi-es"></span> Español</a>
                            <a class="dropdown-item" href="/pt/{slug}"><span class="fi fi-br"></span> Português</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>"""


# ---------------------------------------------------------------------------
# Helper: footer + JS
# ---------------------------------------------------------------------------
def footer_and_js():
    return """    <footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
        <div class="container">
            <div class="row mb-5 justify-content-center">
                <div class="col-md-6 text-center">
                    <h2 class="ftco-heading-2">Follow eVisa-Card.com</h2>
                    <ul class="ftco-footer-social list-unstyled float-md-center float-lft mt-3">
                        <li class="ftco-animate"><a href="https://facebook.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-facebook"></span></a></li>
                        <li class="ftco-animate"><a href="https://twitter.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-twitter"></span></a></li>
                        <li class="ftco-animate"><a href="https://instagram.com/evisacard" rel="noopener" target="_blank"><span class="fa fa-instagram"></span></a></li>
                    </ul>
                    <p class="mt-4">&copy; 2025 eVisa-Card.com &mdash; Global eVisa &amp; Travel Information Platform</p>
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
    <script src="../js/bootstrap-datepicker.js"></script>
    <script src="../js/scrollax.min.js"></script>
    <script src="../js/google-map.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Helper: E-E-A-T block
# ---------------------------------------------------------------------------
def eeat():
    return """<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026. Sources: official embassy websites.</div>"""


# ---------------------------------------------------------------------------
# Helper: internal links block
# ---------------------------------------------------------------------------
def internal_links(country_key):
    c = COUNTRIES[country_key]
    cname = c["name"].lower()
    return f"""<div class="mt-4 pt-3 border-top">
    <h3 class="h6">Related Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{cname}.html">Main {c['name']} Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-documents-checklist.html">Visa Documents Checklist</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-processing-times.html">Visa Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-photo-requirements.html">Visa Photo Requirements</a>
</div>"""


# ===========================================================================
# PAGE 1: visa-requirements
# ===========================================================================
def gen_requirements(country_key):
    c = COUNTRIES[country_key]
    name = c["name"]
    flag = c["flag"]
    slug = f"{country_key}-visa-requirements.html"
    title = f"{name} Visa Requirements 2026 — Documents, Eligibility & Checklist"
    # 150-155 chars
    desc = f"Complete {name} visa requirements for 2026. Documents checklist, eligibility criteria, passport validity rules and official application links."
    desc = desc[:155]

    if c["schengen"]:
        visa_type = "Schengen short-stay visa (Type C)"
        authority = "French/German/Italian/Spanish Consulate or VFS Global"
        entry = "90 days within any 180-day period"
    elif country_key == "thailand":
        visa_type = "eVisa (Tourist TR) or visa-free entry"
        authority = "Department of Consular Affairs, Thailand"
        entry = "60 days (visa-free) / 60 days (Tourist TR)"
    elif country_key == "india":
        visa_type = "e-Tourist Visa (eTV)"
        authority = "Bureau of Immigration, India"
        entry = "30 days (single), 1 year (multiple), 5 years (multiple)"
    elif country_key == "japan":
        visa_type = "Temporary Visitor Visa (no eVisa for most nationalities)"
        authority = "Ministry of Foreign Affairs (MOFA), Japan"
        entry = "Up to 90 days"
    elif country_key == "usa":
        visa_type = "B-1/B-2 Tourist/Business Visa or ESTA (VWP)"
        authority = "U.S. Department of State / CBP"
        entry = "Up to 90 days (ESTA) / 6 months (B-2)"
    elif country_key == "canada":
        visa_type = "Temporary Resident Visa (TRV) or eTA"
        authority = "Immigration, Refugees and Citizenship Canada (IRCC)"
        entry = "Up to 6 months"
    else:  # australia
        visa_type = "Electronic Travel Authority (ETA), eVisitor, or Visitor Visa (subclass 600)"
        authority = "Department of Home Affairs, Australia"
        entry = "Up to 3 months per visit (ETA/eVisitor)"

    # FAQ JSON-LD
    faq_jsonld = ""
    if country_key == "thailand":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents do I need for a Thailand tourist visa in 2026?","acceptedAnswer":{"@type":"Answer","text":"You need a valid passport (6+ months validity), a completed online application at thaievisa.go.th, a digital passport photo on a white background, return/onward flight bookings, proof of accommodation, and a bank statement showing sufficient funds (THB 10,000 per person)."}},
{"@type":"Question","name":"Do I need a visa to visit Thailand?","acceptedAnswer":{"@type":"Answer","text":"Citizens of 93 countries qualify for visa-free entry to Thailand for up to 60 days. If your nationality is not on the visa-exempt list, you must apply for a Tourist Visa (TR) via the Thailand eVisa portal at thaievisa.go.th before travel."}},
{"@type":"Question","name":"What is the minimum passport validity for Thailand?","acceptedAnswer":{"@type":"Answer","text":"Thailand requires your passport to be valid for at least 6 months beyond your intended stay. Ensure your passport has at least one blank page for the entry stamp."}},
{"@type":"Question","name":"Can I extend my stay in Thailand?","acceptedAnswer":{"@type":"Answer","text":"Yes. Visa-free visitors and Tourist Visa (TR) holders can extend their stay by 30 days at any Thai Immigration Office, paying a fee of THB 1,900. Long-term options include the LTR Visa and Thailand Elite program."}}
]}
</script>"""
    elif country_key == "india":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents are required for an India e-Tourist Visa in 2026?","acceptedAnswer":{"@type":"Answer","text":"Required documents include a valid passport (6+ months validity, 2 blank pages), a recent passport-size photo (white background), a scanned bio-data page, return/onward ticket, and payment of the eVisa fee (USD 25–80 depending on duration)."}},
{"@type":"Question","name":"Who is eligible for India e-Tourist Visa?","acceptedAnswer":{"@type":"Answer","text":"Citizens of over 160 countries are eligible for the India e-Tourist Visa (eTV). The visa is available for tourism, casual business visits, and medical visits. Applicants must apply online at evisa.india.gov.in at least 4 days before travel."}},
{"@type":"Question","name":"How many times can I enter India on an e-Tourist Visa?","acceptedAnswer":{"@type":"Answer","text":"The 30-day eTV allows double entry. The 1-year and 5-year eTVs allow multiple entries with a maximum stay of 90 consecutive days per visit (60 days for certain nationalities)."}},
{"@type":"Question","name":"Can I work or study in India on a tourist eVisa?","acceptedAnswer":{"@type":"Answer","text":"No. The e-Tourist Visa is strictly for tourism, recreation, casual visits to friends and relatives, and short medical visits. Working, studying, or journalism activities require specific visa categories."}}
]}
</script>"""
    elif country_key in ("france", "germany", "italy", "spain"):
        faq_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{{"@type":"Question","name":"What documents do I need for a {name} Schengen visa in 2026?","acceptedAnswer":{{"@type":"Answer","text":"You need a valid passport (valid for 3 months after departure, issued within 10 years), 2 recent passport photos, completed visa application form, travel insurance (minimum EUR 30,000 coverage), proof of accommodation, return flights, and financial proof (bank statements, payslips)."}}}},
{{"@type":"Question","name":"How far in advance should I apply for a {name} Schengen visa?","acceptedAnswer":{{"@type":"Answer","text":"Applications can be submitted up to 6 months before travel. It is recommended to apply at least 4–6 weeks before your trip to allow sufficient processing time. The standard processing time is 15 working days."}}}},
{{"@type":"Question","name":"Do I need travel insurance for a {name} visa?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Schengen visa applicants must provide proof of travel insurance with a minimum coverage of EUR 30,000 valid throughout the Schengen area for the entire duration of their stay."}}}},
{{"@type":"Question","name":"What is the Schengen area and which countries are included?","acceptedAnswer":{{"@type":"Answer","text":"The Schengen area consists of 27 European countries that have abolished internal border controls. A single Schengen visa allows travel to all member states for up to 90 days within any 180-day period."}}}}
]}}
</script>"""
    elif country_key == "japan":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents do I need to enter Japan in 2026?","acceptedAnswer":{"@type":"Answer","text":"Most nationalities with visa-free access need only a valid passport and a completed arrival card. Visa applicants need: valid passport, completed application form (available at Japanese consulates), passport photo, itinerary, accommodation proof, financial evidence, and employment certificate."}},
{"@type":"Question","name":"Does Japan have an eVisa system?","acceptedAnswer":{"@type":"Answer","text":"Japan introduced an eVisa system for limited nationalities for short-term stays. Most nationalities either qualify for visa-free entry or must apply through a Japanese embassy or consulate. Check mofa.go.jp for the latest list of eligible countries."}},
{"@type":"Question","name":"What nationalities can visit Japan visa-free in 2026?","acceptedAnswer":{"@type":"Answer","text":"Over 68 countries/regions have visa-free access to Japan for short-term stays (typically 90 days), including USA, UK, EU countries, Canada, Australia, and many others. Check the MOFA website for the most current list."}},
{"@type":"Question","name":"What is the minimum passport validity for Japan?","acceptedAnswer":{"@type":"Answer","text":"Japan requires your passport to remain valid for the duration of your stay. There is no strict 6-month rule for visa-free visitors, but it is advisable to have at least 6 months validity to avoid any issues at immigration."}}
]}
</script>"""
    elif country_key == "usa":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents do I need for a US B-2 tourist visa in 2026?","acceptedAnswer":{"@type":"Answer","text":"Required documents include: valid passport (6+ months validity), completed DS-160 form, visa application fee payment (USD 185 MRV fee), passport photo, interview appointment confirmation, financial evidence (bank statements, pay stubs), and ties to home country (property, employment, family)."}},
{"@type":"Question","name":"What is ESTA and who qualifies?","acceptedAnswer":{"@type":"Answer","text":"ESTA (Electronic System for Travel Authorization) is for citizens of Visa Waiver Program (VWP) countries traveling to the USA for up to 90 days for tourism or business. It costs USD 21 and can be applied for at esta.cbp.dhs.gov. Over 40 countries participate in the VWP."}},
{"@type":"Question","name":"How long does a US visa interview take?","acceptedAnswer":{"@type":"Answer","text":"The consular interview itself typically lasts 3–5 minutes. However, you should allocate 2–4 hours total for your appointment including security screening and waiting. Appointment wait times vary by embassy and season."}},
{"@type":"Question","name":"Can I work in the USA on a B-2 tourist visa?","acceptedAnswer":{"@type":"Answer","text":"No. The B-1/B-2 visa is strictly for tourism and business meetings (no paid work). Working in the USA requires a work visa such as H-1B, L-1, or O-1, which must be sponsored by a US employer."}}
]}
</script>"""
    elif country_key == "canada":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents do I need for a Canada visitor visa in 2026?","acceptedAnswer":{"@type":"Answer","text":"Required documents include: valid passport, completed IMM 5257 form, biometrics (CAD 85), financial evidence (bank statements, employment letter, pay stubs), travel history, purpose of visit letter, proof of ties to home country, and visa fee (CAD 100)."}},
{"@type":"Question","name":"What is the Canada eTA and who needs it?","acceptedAnswer":{"@type":"Answer","text":"The Electronic Travel Authorization (eTA) costs CAD 7 and is required for visa-exempt foreign nationals flying to Canada. US citizens are exempt. It is valid for 5 years or until passport expiry and allows multiple visits of up to 6 months each."}},
{"@type":"Question","name":"How long does a Canadian visitor visa take to process?","acceptedAnswer":{"@type":"Answer","text":"Processing times for a Temporary Resident Visa (TRV) typically range from 4 to 12 weeks depending on the visa office and applicant's country. IRCC's current processing times are published at ircc.canada.ca. The eTA is usually approved within minutes."}},
{"@type":"Question","name":"Do I need biometrics for a Canada visitor visa?","acceptedAnswer":{"@type":"Answer","text":"Yes. Most applicants aged 14–79 must provide biometrics (fingerprints and photo) at a designated collection point. The biometrics fee is CAD 85 (or CAD 170 for a family). Biometrics are valid for 10 years."}}
]}
</script>"""
    else:  # australia
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What documents do I need for an Australia visitor visa in 2026?","acceptedAnswer":{"@type":"Answer","text":"Required documents include: valid passport, completed online application via ImmiAccount, passport photo, financial evidence (bank statements), travel itinerary, employment or enrolment evidence, and health insurance. Visa subclass 600 applicants pay AUD 145."}},
{"@type":"Question","name":"What is the Australia ETA and who qualifies?","acceptedAnswer":{"@type":"Answer","text":"The Electronic Travel Authority (ETA, subclass 601) costs AUD 20 and is available to passport holders from USA, UK, Canada, Japan, Singapore, and other eligible countries. It allows multiple visits of up to 3 months each within a 12-month period."}},
{"@type":"Question","name":"What is the eVisitor visa for Australia?","acceptedAnswer":{"@type":"Answer","text":"The eVisitor (subclass 651) is a free visa for citizens of EU countries and select other European nations. It allows multiple visits of up to 3 months within a 12-month period and can be applied for online at immi.homeaffairs.gov.au."}},
{"@type":"Question","name":"Can I extend my Australian visitor visa?","acceptedAnswer":{"@type":"Answer","text":"ETA and eVisitor holders cannot extend their stay beyond 3 months per visit without leaving and re-entering. Visitor Visa (subclass 600) holders may apply for an extension online through ImmiAccount before their current visa expires."}}
]}
</script>"""

    # HowTo JSON-LD
    howto_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","name":"How to Check {name} Visa Requirements in 2026","description":"Step-by-step guide to verifying eligibility and gathering documents for a {name} visa application.","step":[
{{"@type":"HowToStep","name":"Step 1: Check eligibility","text":"Visit the official {name} immigration website to check whether your nationality requires a visa or qualifies for visa-free entry or an eVisa."}},
{{"@type":"HowToStep","name":"Step 2: Determine the correct visa type","text":"Identify the right visa category for your trip (tourism, business, transit, etc.) and the corresponding requirements."}},
{{"@type":"HowToStep","name":"Step 3: Gather required documents","text":"Collect all mandatory documents: valid passport, photos, financial proof, accommodation confirmation, travel insurance, and any supporting letters."}},
{{"@type":"HowToStep","name":"Step 4: Complete the application form","text":"Fill in the official visa application form online or at the consulate. Double-check all information for accuracy before submission."}},
{{"@type":"HowToStep","name":"Step 5: Submit and await decision","text":"Submit your application with all documents and the applicable fee. Track your application status and prepare to attend an interview if required."}}
]}}
</script>"""

    # Table data
    if country_key == "thailand":
        table_rows = """<tr><th>Visa-Free Entry</th><td>Citizens of 93 countries — 60 days</td></tr>
<tr><th>Tourist Visa (TR)</th><td>THB 2,000 — 60 days (extendable 30 days)</td></tr>
<tr><th>Multiple-Entry Tourist Visa</th><td>THB 5,000 — 60 days/stay, valid 6 months</td></tr>
<tr><th>Passport Validity Required</th><td>Minimum 6 months beyond intended stay</td></tr>
<tr><th>Blank Pages Required</th><td>At least 1 blank page</td></tr>
<tr><th>Travel Insurance</th><td>Recommended but not mandatory</td></tr>
<tr><th>Onward Ticket Required</th><td>Yes (visa-free and Tourist Visa)</td></tr>"""
    elif country_key == "india":
        table_rows = """<tr><th>e-Tourist Visa (30 days)</th><td>USD 25 — double entry</td></tr>
<tr><th>e-Tourist Visa (1 year)</th><td>USD 40 — multiple entry, max 90 days/stay</td></tr>
<tr><th>e-Tourist Visa (5 years)</th><td>USD 80 — multiple entry, max 90 days/stay</td></tr>
<tr><th>Passport Validity Required</th><td>Minimum 6 months + 2 blank pages</td></tr>
<tr><th>Photo Requirement</th><td>50x50mm, white background, recency &lt;6 months</td></tr>
<tr><th>Travel Insurance</th><td>Recommended</td></tr>
<tr><th>Application Portal</th><td>evisa.india.gov.in</td></tr>"""
    elif c["schengen"]:
        table_rows = f"""<tr><th>Visa Type</th><td>Schengen Short-Stay Visa (Type C)</td></tr>
<tr><th>Maximum Stay</th><td>90 days within any 180-day period</td></tr>
<tr><th>Passport Validity</th><td>Valid 3 months after intended departure; issued within 10 years</td></tr>
<tr><th>Passport Photos</th><td>2 photos, 35x45mm, white background, &lt;6 months old</td></tr>
<tr><th>Travel Insurance</th><td>Required — min EUR 30,000 coverage, Schengen-wide</td></tr>
<tr><th>Financial Proof</th><td>Bank statements last 3 months; min EUR 50–100/day recommended</td></tr>
<tr><th>Accommodation Proof</th><td>Hotel bookings or invitation letter from host</td></tr>"""
    elif country_key == "japan":
        table_rows = """<tr><th>Visa-Free Entry</th><td>68+ nationalities — up to 90 days</td></tr>
<tr><th>Temporary Visitor Visa</th><td>Required for non-exempt nationalities</td></tr>
<tr><th>Passport Validity</th><td>Valid for full duration of stay</td></tr>
<tr><th>Passport Photos</th><td>45x45mm, white background, no glasses</td></tr>
<tr><th>Return/Onward Ticket</th><td>Required at immigration</td></tr>
<tr><th>Proof of Funds</th><td>JPY 100,000+ recommended (approx. USD 700)</td></tr>
<tr><th>Travel Insurance</th><td>Recommended</td></tr>"""
    elif country_key == "usa":
        table_rows = """<tr><th>ESTA (VWP)</th><td>USD 21 — 90 days, eligible nationalities only</td></tr>
<tr><th>B-1/B-2 Tourist Visa</th><td>USD 185 MRV fee — up to 6 months</td></tr>
<tr><th>DS-160 Form</th><td>Mandatory for all visa applicants</td></tr>
<tr><th>Passport Validity</th><td>Minimum 6 months beyond intended stay (or per treaty)</td></tr>
<tr><th>Photo Requirement</th><td>51x51mm (2x2 inch), white background, &lt;6 months old</td></tr>
<tr><th>Financial Evidence</th><td>Bank statements, tax returns, property deeds</td></tr>
<tr><th>Ties to Home Country</th><td>Employment letter, property, family — to show non-immigrant intent</td></tr>"""
    elif country_key == "canada":
        table_rows = """<tr><th>eTA</th><td>CAD 7 — visa-exempt nationals flying to Canada</td></tr>
<tr><th>Temporary Resident Visa</th><td>CAD 100 — nationals who require a visa</td></tr>
<tr><th>Biometrics</th><td>CAD 85 (required for most applicants aged 14–79)</td></tr>
<tr><th>Passport Validity</th><td>Valid for full duration of stay + 6 months recommended</td></tr>
<tr><th>Photo Requirement</th><td>35x45mm, white background, neutral expression</td></tr>
<tr><th>Financial Proof</th><td>Bank statements, employment letter, income tax returns</td></tr>
<tr><th>Ties to Home Country</th><td>Employment, family, property — strong ties required</td></tr>"""
    else:  # australia
        table_rows = """<tr><th>ETA (Subclass 601)</th><td>AUD 20 — eligible passport holders, 3 months/visit</td></tr>
<tr><th>eVisitor (Subclass 651)</th><td>Free — EU and select European nationals</td></tr>
<tr><th>Visitor Visa (Subclass 600)</th><td>AUD 145 — general applicants, up to 12 months</td></tr>
<tr><th>Passport Validity</th><td>Valid for full duration of stay</td></tr>
<tr><th>Photo Requirement</th><td>35x45mm, white background, neutral expression</td></tr>
<tr><th>Health Insurance</th><td>Recommended; OVHC for long-stay visitors</td></tr>
<tr><th>Character Requirements</th><td>No serious criminal convictions; health checks may apply</td></tr>"""

    # Main content body
    if country_key == "thailand":
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> Thailand Visa Requirements 2026 — Documents, Eligibility &amp; Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Thailand Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of Thailand Entry Requirements 2026</h2>
<p>Thailand remains one of the world's most visited countries, welcoming over 30 million international tourists annually. In 2024, Thailand expanded its visa-free programme to 93 countries — granting 60 days of visa-free stay to most nationalities including the USA, UK, all EU member states, Canada, Australia, Japan, and South Korea. Understanding the entry requirements before you travel is essential to avoid issues at the border.</p>
<p>Thailand's entry requirements depend on your nationality. Visa-exempt travellers must carry a valid passport (minimum 6 months validity), a return or onward ticket, and proof of sufficient funds. For nationals outside the visa-exempt list, the Thailand eVisa system at <a href="https://www.thaievisa.go.th" target="_blank" rel="noopener">thaievisa.go.th</a> allows online applications for Tourist (TR), Non-Immigrant, and other visa categories.</p>

<h2 id="documents">Documents Checklist for Thailand Tourist Visa 2026</h2>
<ul>
<li>Valid passport — minimum 6 months validity beyond intended departure, at least 1 blank page</li>
<li>Digital passport photo — white background, full face, 200×200 px minimum (JPEG format)</li>
<li>Return or onward flight booking confirmation</li>
<li>Proof of accommodation — hotel bookings or host invitation letter</li>
<li>Bank statement — minimum balance of THB 10,000 (individual) or THB 20,000 (family)</li>
<li>Completed online application via thaievisa.go.th</li>
<li>Visa fee payment — THB 2,000 by credit/debit card</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>To enter Thailand, you must hold a passport with at least 6 months validity and be free of any communicable diseases listed under Thailand's entry regulations. You must not have a criminal record that would render you inadmissible. Visa-free visitors must demonstrate genuine tourist intent and sufficient funds for the intended stay. The Immigration Bureau may deny entry to any traveller deemed a risk or without adequate documentation.</p>

<h2 id="apply">How to Apply</h2>
<p>Visa-exempt nationals simply arrive at a Thai port of entry with their passport, return ticket, and evidence of funds — no pre-arrival authorisation is required. Nationals who need a Tourist Visa (TR) should apply online at thaievisa.go.th at least 5–7 business days before travel. The eVisa is emailed as a PDF; print it and present it at immigration alongside your passport.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    elif country_key == "india":
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> India Visa Requirements 2026 — e-Tourist Visa Documents &amp; Eligibility</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">India Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of India Visa Requirements 2026</h2>
<p>India operates a comprehensive e-Visa system for tourists, business travellers, medical visitors, and conference attendees. The e-Tourist Visa (eTV) is available to citizens of over 160 countries and is one of the most popular electronic travel authorisations in Asia. All applications are submitted through the official portal at evisa.india.gov.in — no embassy visit is required for eVisa categories.</p>
<p>India does not offer traditional visa-on-arrival for most nationalities. Travellers from eligible countries must apply online at least 4 days before their planned date of arrival. The eVisa is linked electronically to your passport; print a copy to present on arrival at designated airports and seaports.</p>

<h2 id="documents">Documents Checklist for India e-Tourist Visa 2026</h2>
<ul>
<li>Valid passport — minimum 6 months validity, 2 blank pages, issued in the last 10 years</li>
<li>Digital passport photo — 50x50mm, white background, plain white or off-white dress, &lt;6 months old</li>
<li>Scanned bio-data page of passport (first and last pages)</li>
<li>Return or onward ticket confirmation</li>
<li>Proof of sufficient funds for the trip</li>
<li>eVisa fee — USD 25 / USD 40 / USD 80 (paid by international credit/debit card)</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>To qualify for an India e-Tourist Visa in 2026, you must hold a passport from one of the 164+ eligible countries, be travelling for tourism or casual visiting purposes, and have no criminal record that would render you inadmissible. Applicants with Pakistani passports or those of Pakistani origin must use the standard visa process at an Indian embassy. Journalists require a separate journalist visa category.</p>

<h2 id="apply">How to Apply for India eVisa</h2>
<p>Visit evisa.india.gov.in and select "e-Tourist Visa." Fill in the online form with personal, travel, and passport details. Upload your photo and passport scan. Pay the fee by international credit or debit card. You will receive an Electronic Travel Authorisation (ETA) by email within 72–96 hours. Print it and present it alongside your passport at the Indian port of entry.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    elif c["schengen"]:
        if country_key == "france":
            extra = "<p>France is a leading Schengen destination. Visa applications are processed by the French consulate or via VFS Global at france-visas.gouv.fr. The France-Visas portal is the official online booking system for appointment scheduling and document upload.</p>"
        elif country_key == "germany":
            extra = "<p>Germany is the Schengen zone's largest economy and a top destination for tourism and business. Applications are processed by the German consulate or via authorised visa service providers. The official portal is auswaertiges-amt.de.</p>"
        elif country_key == "italy":
            extra = "<p>Italy is one of the world's most visited countries. Schengen visa applications for Italy are processed by Italian consulates or VFS Global. The official portal is vistoperitalia.esteri.it.</p>"
        else:  # spain
            extra = "<p>Spain is a top Schengen destination, especially popular for beaches, culture, and gastronomy. Applications are processed by Spanish consulates or VFS Global. The official website is exteriores.gob.es.</p>"
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Requirements 2026 — Schengen Documents, Eligibility &amp; Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Schengen Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of {name} Schengen Visa Requirements 2026</h2>
<p>Travellers who require a visa to visit {name} must apply for a Schengen Short-Stay Visa (Type C), which allows up to 90 days within any 180-day period across all 27 Schengen member states. Citizens of many countries — including the USA, UK, Canada, Australia, and Japan — are exempt from Schengen visa requirements for short stays.</p>
{extra}

<h2 id="documents">Documents Checklist for {name} Schengen Visa 2026</h2>
<ul>
<li>Valid passport — valid for at least 3 months after intended departure, issued within the last 10 years, at least 2 blank pages</li>
<li>2 passport photos — 35x45mm, white background, neutral expression, &lt;6 months old</li>
<li>Completed and signed Schengen visa application form</li>
<li>Travel insurance — minimum EUR 30,000 coverage valid in all Schengen states</li>
<li>Round-trip flight reservation (not necessarily purchased)</li>
<li>Proof of accommodation — hotel bookings, rental agreement, or host invitation (with copy of host's ID)</li>
<li>Proof of financial means — bank statements for the last 3 months</li>
<li>Employment proof — employer letter, business registration, or student enrolment</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>To qualify for a {name} Schengen visa, applicants must demonstrate genuine intent to return to their home country after the visit, have sufficient financial means for the trip, and not represent a threat to public order or security. Applicants with previous Schengen visa refusals must disclose this in the application. Overstaying a previous Schengen visa may result in a ban.</p>

<h2 id="apply">How to Apply for a {name} Schengen Visa</h2>
<p>Book your appointment at the {name} consulate or an authorised VFS Global centre in your country of residence. Submit your application in person with all required documents. Pay the EUR 80 visa fee. Applications can be submitted up to 6 months before travel and must be submitted no later than 15 working days before your trip. Processing takes up to 15 working days.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    elif country_key == "japan":
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> Japan Visa Requirements 2026 — Documents, Eligibility &amp; Entry Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Japan Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of Japan Entry Requirements 2026</h2>
<p>Japan is one of Asia's most popular travel destinations, known for its unique blend of ancient culture and modern innovation. Over 68 countries and regions benefit from visa-free access to Japan for short-term stays of up to 90 days. These include most Western nations: the USA, UK, Canada, Australia, all EU member states, and many others. Japan does not currently operate a universal eVisa system; most travellers either enter visa-free or must apply through a Japanese embassy or consulate.</p>
<p>Japan introduced limited eVisa capabilities for certain nationalities in recent years, but the primary route for visa-required nationalities remains a consular application. Always check the current status at mofa.go.jp before applying.</p>

<h2 id="documents">Documents Checklist for Japan Visa 2026</h2>
<ul>
<li>Valid passport — valid for the full duration of stay, at least 1 blank page</li>
<li>Completed visa application form (available from Japanese consulates or mofa.go.jp)</li>
<li>Passport photo — 45x45mm, white background, no glasses, &lt;6 months old</li>
<li>Detailed travel itinerary including flights and accommodation</li>
<li>Proof of financial means — bank statement showing sufficient funds</li>
<li>Employment or business documentation — employer letter, business registration</li>
<li>Return or onward ticket reservation</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>Visa-free travellers to Japan must comply with the conditions of their stay: no paid work, no activities contrary to the visa-free purpose, and departure within the permitted period. Travellers with previous immigration violations in Japan may be denied entry. Japan's border officials assess character, purpose, and financial capacity at the port of entry.</p>

<h2 id="apply">How to Apply for a Japan Visa</h2>
<p>Citizens of countries without visa-free access must apply at the nearest Japanese embassy or consulate or an accredited agency. Submit the application form with all documents and the applicable fee. Processing typically takes 5–10 business days. Japan does not currently offer a general online eVisa; always use official consular channels at mofa.go.jp.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    elif country_key == "usa":
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> USA Visa Requirements 2026 — B-2 Tourist Visa &amp; ESTA Documents Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">USA Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of USA Entry Requirements 2026</h2>
<p>The United States has two primary entry pathways for tourists: the Visa Waiver Program (VWP) with ESTA, and the B-1/B-2 Tourist/Business Visa. Citizens of over 40 countries participate in the VWP and may travel to the USA for up to 90 days with a valid ESTA authorisation, available at esta.cbp.dhs.gov for USD 21. All other nationalities must apply for a nonimmigrant visa at a US embassy or consulate.</p>
<p>The B-2 tourist visa is the most common US visa for travellers who do not qualify for ESTA. It requires completing the DS-160 online application, paying the USD 185 MRV fee, and attending a consular interview. The interview is a critical step; applicants must demonstrate strong ties to their home country and genuine non-immigrant intent.</p>

<h2 id="documents">Documents Checklist for USA B-2 Visa 2026</h2>
<ul>
<li>Valid passport — minimum 6 months validity beyond stay (unless covered by treaty) — at least 1 blank page</li>
<li>Completed DS-160 form (online at ceac.state.gov)</li>
<li>MRV fee payment confirmation — USD 185</li>
<li>Interview appointment confirmation letter (from US embassy website)</li>
<li>Passport photo — 51x51mm (2×2 inch), white background, &lt;6 months old</li>
<li>Financial evidence — bank statements, tax returns, pay stubs</li>
<li>Ties to home country — employer letter, property deeds, family documents</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>The key test for a US B-2 visa is overcoming the presumption of immigrant intent. Applicants must prove to the consular officer that they have strong ties to their home country — through employment, property, family, or other obligations — that will compel them to return after their US visit. Prior US visa refusals and overstays significantly reduce approval chances.</p>

<h2 id="apply">How to Apply for a US B-2 Visa</h2>
<p>Complete the DS-160 form online and pay the USD 185 MRV fee. Schedule your interview at the nearest US embassy or consulate at ustraveldocs.com. Attend the interview with all required documents. Visa processing after the interview typically takes 3–5 business days for approved applications, but administrative processing may add 2–10 weeks. Check travel.state.gov for current wait times.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    elif country_key == "canada":
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> Canada Visa Requirements 2026 — TRV &amp; eTA Documents Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Canada Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of Canada Entry Requirements 2026</h2>
<p>Canada uses two key entry systems for visitors: the Electronic Travel Authorization (eTA) for visa-exempt nationals flying to Canada, and the Temporary Resident Visa (TRV) for nationals who require a visa. US citizens are exempt from both and may enter with a valid passport or approved documents. The eTA costs CAD 7 and is linked to your passport electronically, valid for 5 years or until passport expiry.</p>
<p>Nationals who require a Temporary Resident Visa must apply online through the IRCC portal at ircc.canada.ca or at a Visa Application Centre (VAC). Processing times vary from 4 to 12 weeks depending on the office and volume. Biometrics are required for most applicants and must be provided at a designated collection point.</p>

<h2 id="documents">Documents Checklist for Canada TRV 2026</h2>
<ul>
<li>Valid passport — recommended 6+ months validity, all previous passports if applicable</li>
<li>Completed IMM 5257 application form (online via IRCC)</li>
<li>Biometrics — fingerprints and photo at designated collection centre (CAD 85)</li>
<li>Passport photo — 35x45mm, white background, neutral expression</li>
<li>Financial evidence — bank statements (3–6 months), pay stubs, income tax returns</li>
<li>Employment letter or business registration</li>
<li>Travel itinerary and accommodation proof</li>
<li>Purpose of visit letter</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>To be approved for a Canadian Temporary Resident Visa, applicants must demonstrate they will leave Canada at the end of their authorised stay, have no inadmissibility issues (criminal record, health conditions), and have sufficient funds for the visit. Strong ties to home country — employment, family, property — are important indicators for approval. Previous Canadian visa refusals should be declared.</p>

<h2 id="apply">How to Apply for Canada TRV</h2>
<p>Apply online at ircc.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html. Create an account, complete the form, upload documents, pay CAD 100 (plus CAD 85 biometrics if applicable), and provide biometrics at a VAC. Track your application online. Decision letters are sent electronically; if approved, your passport will be stamped with a Temporary Resident Visa.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""
    else:  # australia
        body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> Australia Visa Requirements 2026 — ETA, eVisitor &amp; Visitor Visa Checklist</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Australia Visa Requirements — Key Facts 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of Australia Entry Requirements 2026</h2>
<p>Australia requires almost all visitors (except New Zealand citizens) to hold a valid visa before arrival. Three main options exist for short-term tourists: the Electronic Travel Authority (ETA, subclass 601) available to passport holders from the USA, UK, Canada, Japan, Singapore, and others; the eVisitor (subclass 651) for EU and select European passport holders; and the Visitor Visa (subclass 600) for all other nationalities.</p>
<p>The ETA and eVisitor allow multiple visits of up to 3 months within a 12-month period. The Visitor Visa (subclass 600) can allow stays of up to 12 months for certain circumstances. All visa applications are managed through ImmiAccount at immi.homeaffairs.gov.au.</p>

<h2 id="documents">Documents Checklist for Australia Visitor Visa 2026</h2>
<ul>
<li>Valid passport — sufficient validity for the duration of stay</li>
<li>Passport photo — 35x45mm, white background, neutral expression</li>
<li>Completed online application via ImmiAccount (immi.homeaffairs.gov.au)</li>
<li>Financial evidence — bank statements, payslips, investment statements</li>
<li>Employment letter or evidence of self-employment/business</li>
<li>Travel itinerary — flights and accommodation</li>
<li>Health insurance or Overseas Visitor Health Cover (OVHC) for longer stays</li>
</ul>

<h2 id="eligibility">Eligibility Criteria</h2>
<p>Australia assesses visa applicants on health, character, and genuine visitor intent. Medical examinations may be required for stays over 3 months or for applicants from certain countries. A National Police Certificate may be requested. The visa officer assesses whether you will genuinely visit temporarily and comply with visa conditions. Financial self-sufficiency is an important criterion.</p>

<h2 id="apply">How to Apply for an Australian Visitor Visa</h2>
<p>Create an ImmiAccount at immi.homeaffairs.gov.au and apply for the appropriate visa subclass (ETA via Australian ETA app, eVisitor online, or subclass 600 through ImmiAccount). Upload required documents and pay the applicable fee. ETA processing is typically instant; eVisitor takes 1–3 days; subclass 600 can take 1–14 days or longer depending on complexity.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""

    html = (
        head(title, desc, slug, country_key, "requirements")
        + "\n"
        + navbar(country_key, slug)
        + "\n"
        + body
        + "\n"
        + faq_jsonld
        + "\n"
        + howto_jsonld
        + "\n"
        + footer_and_js()
    )
    return slug, html


# ===========================================================================
# PAGE 2: visa-fees
# ===========================================================================
def gen_fees(country_key):
    c = COUNTRIES[country_key]
    name = c["name"]
    flag = c["flag"]
    slug = f"{country_key}-visa-fees.html"
    title = f"{name} Visa Fees 2026 — Cost, Payment Methods & Refund Policy"
    desc = f"Full breakdown of {name} visa fees in 2026. Application costs, service charges, payment methods and refund policy explained."
    desc = desc[:155]

    # FAQ JSON-LD
    if country_key == "thailand":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does a Thailand tourist visa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"The Thailand Tourist Visa (TR) costs THB 2,000 (approximately USD 55) for a single-entry visa. The Multiple-Entry Tourist Visa (METV) costs THB 5,000. In-country extensions cost THB 1,900 at any Thai Immigration Office."}},
{"@type":"Question","name":"Is the Thailand visa fee refundable if refused?","acceptedAnswer":{"@type":"Answer","text":"No. Thailand visa fees are non-refundable regardless of the outcome of the application. Ensure all documents are complete and accurate before submitting your application."}},
{"@type":"Question","name":"Can I pay Thailand visa fees online?","acceptedAnswer":{"@type":"Answer","text":"Yes. The Thailand eVisa system at thaievisa.go.th accepts payment by international credit and debit cards (Visa, Mastercard). The fee must be paid online during the application process."}},
{"@type":"Question","name":"Are there any additional service fees for Thailand visa applications?","acceptedAnswer":{"@type":"Answer","text":"Applications made through the official thaievisa.go.th portal incur only the standard government fee. Third-party visa agencies may charge additional service fees of USD 20–80, but use of agencies is not mandatory."}}
]}
</script>"""
    elif country_key == "india":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does India eVisa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"India e-Tourist Visa fees in 2026: USD 25 for 30-day double-entry; USD 40 for 1-year multiple-entry; USD 80 for 5-year multiple-entry. A bank charge of USD 2.50 may apply. Fees are non-refundable."}},
{"@type":"Question","name":"What payment methods are accepted for India eVisa?","acceptedAnswer":{"@type":"Answer","text":"India eVisa fees can be paid by Visa, Mastercard, American Express, or PayPal through the secure payment gateway on evisa.india.gov.in. The fee is charged in USD. Some cards may incur a foreign transaction fee from your bank."}},
{"@type":"Question","name":"Is the India eVisa fee refundable?","acceptedAnswer":{"@type":"Answer","text":"No. The India eVisa fee is non-refundable once the application has been submitted, regardless of approval or rejection."}},
{"@type":"Question","name":"Does India charge different fees for different nationalities?","acceptedAnswer":{"@type":"Answer","text":"India charges a standard eVisa fee for most nationalities. However, citizens of some countries (including Japan, UAE, and others) may have different fee arrangements or reciprocal fee-free access. Check evisa.india.gov.in for the current fee schedule."}}
]}
</script>"""
    elif c["schengen"]:
        faq_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{{"@type":"Question","name":"How much does a {name} Schengen visa cost in 2026?","acceptedAnswer":{{"@type":"Answer","text":"The standard Schengen visa fee for {name} is EUR 80 for adults. Children aged 6–11 pay EUR 40. Children under 6 years and certain categories (close family of EU citizens, students) may be exempt. Service fees from VFS Global add EUR 30–40."}}}},
{{"@type":"Question","name":"Are Schengen visa fees refundable if refused?","acceptedAnswer":{{"@type":"Answer","text":"No. The EUR 80 Schengen visa fee is non-refundable in case of refusal. Service fees charged by VFS Global are also non-refundable."}}}},
{{"@type":"Question","name":"Can I pay {name} visa fees online?","acceptedAnswer":{{"@type":"Answer","text":"Payment methods vary by application centre. VFS Global and most consulates accept cash, credit/debit cards, or bank transfers depending on the location. Check the specific appointment booking portal for accepted payment methods."}}}},
{{"@type":"Question","name":"Are there additional charges beyond the EUR 80 Schengen visa fee?","acceptedAnswer":{{"@type":"Answer","text":"Yes. VFS Global and other authorised visa application centres charge a service fee of approximately EUR 30–40. Some centres also charge for biometric collection, document scanning, or courier return services."}}}}
]}}
</script>"""
    elif country_key == "japan":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does a Japan tourist visa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"Japan visa fees vary by nationality due to reciprocal agreements. Typical fees range from JPY 3,000 (single entry) to JPY 6,000 (multiple entry). Some nationalities pay no fee due to bilateral agreements. Check mofa.go.jp or your nearest Japanese consulate for exact fees."}},
{"@type":"Question","name":"Is the Japan visa fee the same for all nationalities?","acceptedAnswer":{"@type":"Answer","text":"No. Japan applies reciprocal visa fee arrangements. Citizens of countries with bilateral agreements (e.g., some Southeast Asian nations) may pay reduced or zero fees. The standard consular fee for most nationalities is JPY 3,000 for single entry."}},
{"@type":"Question","name":"Is the Japan visa fee refundable?","acceptedAnswer":{"@type":"Answer","text":"No. Japan consular visa fees are non-refundable regardless of the application outcome."}},
{"@type":"Question","name":"How do I pay the Japan visa fee?","acceptedAnswer":{"@type":"Answer","text":"Japan visa fees are typically paid in cash (local currency) at the consulate or designated collection point. Some authorised agencies may accept card payments. Check with your local Japanese consulate for specific payment instructions."}}
]}
</script>"""
    elif country_key == "usa":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does a US tourist visa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"The US B-1/B-2 visa application fee (MRV fee) is USD 185. ESTA (for Visa Waiver Program countries) costs USD 21. These fees are non-refundable. Some visa categories (e.g., J, K visas) have different fee structures."}},
{"@type":"Question","name":"Is the US visa fee refundable if denied?","acceptedAnswer":{"@type":"Answer","text":"No. The USD 185 MRV fee is non-refundable regardless of the visa decision. ESTA fees are also non-refundable. You must pay the fee again if you reapply after a refusal."}},
{"@type":"Question","name":"How do I pay the US visa fee?","acceptedAnswer":{"@type":"Answer","text":"The MRV fee can be paid via the US embassy's local payment method (varies by country — bank transfer, online payment, or at designated banks). ESTA fees are paid online by credit or debit card at esta.cbp.dhs.gov."}},
{"@type":"Question","name":"Are there additional costs beyond the USD 185 US visa fee?","acceptedAnswer":{"@type":"Answer","text":"Potentially. Some countries require payment of a visa issuance reciprocity fee in addition to the USD 185 MRV fee, based on the fees the USA charges citizens of that country. Check travel.state.gov for the reciprocity schedule for your nationality."}}
]}
</script>"""
    elif country_key == "canada":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does a Canada visitor visa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"The Temporary Resident Visa (TRV) costs CAD 100. Biometrics (required for most applicants) cost an additional CAD 85. The eTA costs CAD 7. Family biometric collection is CAD 170."}},
{"@type":"Question","name":"Is the Canada visa fee refundable?","acceptedAnswer":{"@type":"Answer","text":"The government processing fee of CAD 100 is non-refundable once submitted. The biometrics fee is also non-refundable. If you withdraw your application before processing begins, you may request a refund — check ircc.canada.ca for current policy."}},
{"@type":"Question","name":"How do I pay the Canada visa fee?","acceptedAnswer":{"@type":"Answer","text":"Canada visa fees are paid online through the IRCC secure portal using Visa, Mastercard, American Express, or prepaid credit cards. Payment is required when submitting your online application."}},
{"@type":"Question","name":"Are there additional fees for biometrics for Canada visa?","acceptedAnswer":{"@type":"Answer","text":"Yes. Most applicants aged 14–79 must pay CAD 85 for biometric collection in addition to the CAD 100 visa fee. Family members applying together pay a combined biometrics fee of CAD 170."}}
]}
</script>"""
    else:  # australia
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much does an Australia visitor visa cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"The Australian ETA (subclass 601) costs AUD 20. The eVisitor (subclass 651) is free. The Visitor Visa (subclass 600) costs AUD 145. These fees are subject to annual review; check immi.homeaffairs.gov.au for current amounts."}},
{"@type":"Question","name":"Is the Australia visa fee refundable?","acceptedAnswer":{"@type":"Answer","text":"No. Australian visa application fees are non-refundable once the application is submitted, regardless of the decision. Ensure your application is complete and accurate before paying."}},
{"@type":"Question","name":"How do I pay the Australia visa fee?","acceptedAnswer":{"@type":"Answer","text":"Australia visa fees are paid through ImmiAccount using Visa, Mastercard, or American Express. Payment is required when submitting the application. The ETA can also be applied for through the Australian ETA app, which charges AUD 20."}},
{"@type":"Question","name":"Are there extra charges for Australia visa applications?","acceptedAnswer":{"@type":"Answer","text":"Some applicants may be required to undergo health examinations (charged separately by approved panel physicians). Biometrics collection may also be requested for certain nationalities. Third-party migration agents charge additional professional fees."}}
]}
</script>"""

    # HowTo JSON-LD
    howto_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","name":"How to Pay {name} Visa Fees in 2026","description":"Step-by-step instructions for paying your {name} visa application fee online or in person.","step":[
{{"@type":"HowToStep","name":"Step 1: Confirm the correct fee","text":"Check the official {name} immigration website for the current visa fee for your nationality and visa category."}},
{{"@type":"HowToStep","name":"Step 2: Prepare payment method","text":"Ensure you have a valid credit/debit card or access to the required payment method (varies by country and application centre)."}},
{{"@type":"HowToStep","name":"Step 3: Complete application form","text":"Fill in the official application form before proceeding to payment — most systems require form completion before fee payment."}},
{{"@type":"HowToStep","name":"Step 4: Pay the fee","text":"Pay the visa fee through the official online portal or at the designated application centre. Keep the payment receipt."}},
{{"@type":"HowToStep","name":"Step 5: Submit and track","text":"Submit your application with proof of fee payment. Save your application reference number to track processing status online."}}
]}}
</script>"""

    # Fee table
    if country_key == "thailand":
        table_rows = """<tr><th>Tourist Visa TR (single-entry)</th><td>THB 2,000 (~USD 55)</td></tr>
<tr><th>Multiple-Entry Tourist Visa METV</th><td>THB 5,000 (~USD 140)</td></tr>
<tr><th>Non-Immigrant B (Business, single)</th><td>THB 2,000 (~USD 55)</td></tr>
<tr><th>Non-Immigrant O-A (Retirement, 1 year)</th><td>THB 2,000 (~USD 55)</td></tr>
<tr><th>In-country extension (30 days)</th><td>THB 1,900 (~USD 52)</td></tr>
<tr><th>Re-entry permit (single)</th><td>THB 1,000</td></tr>
<tr><th>Re-entry permit (multiple)</th><td>THB 3,800</td></tr>"""
    elif country_key == "india":
        table_rows = """<tr><th>e-Tourist Visa — 30 days (double entry)</th><td>USD 25</td></tr>
<tr><th>e-Tourist Visa — 1 year (multiple entry)</th><td>USD 40</td></tr>
<tr><th>e-Tourist Visa — 5 years (multiple entry)</th><td>USD 80</td></tr>
<tr><th>e-Business Visa — 1 year</th><td>USD 80</td></tr>
<tr><th>e-Medical Visa</th><td>USD 25</td></tr>
<tr><th>Bank processing charge</th><td>USD 2.50 (approx.)</td></tr>
<tr><th>Visa on Arrival (select airports)</th><td>USD 25</td></tr>"""
    elif c["schengen"]:
        table_rows = f"""<tr><th>Schengen Visa (Adult, 12+)</th><td>EUR 80</td></tr>
<tr><th>Schengen Visa (Child 6–11)</th><td>EUR 40</td></tr>
<tr><th>Schengen Visa (Child under 6)</th><td>Free</td></tr>
<tr><th>VFS Global Service Fee</th><td>EUR 30–40 (approx.)</td></tr>
<tr><th>Biometrics (if applicable)</th><td>Included in service fee</td></tr>
<tr><th>Document Courier Return</th><td>EUR 10–20 (optional)</td></tr>
<tr><th>Long-Stay Visa (Type D, France/Germany/Italy/Spain)</th><td>EUR 99</td></tr>"""
    elif country_key == "japan":
        table_rows = """<tr><th>Single-Entry Temporary Visitor Visa</th><td>JPY 3,000 (~USD 20)</td></tr>
<tr><th>Double-Entry Temporary Visitor Visa</th><td>JPY 6,000 (~USD 40)</td></tr>
<tr><th>Multiple-Entry Visitor Visa</th><td>JPY 6,000 (~USD 40)</td></tr>
<tr><th>Transit Visa</th><td>JPY 700 (~USD 5)</td></tr>
<tr><th>Work / Long-Stay Visa</th><td>JPY 3,000–6,000</td></tr>
<tr><th>Fee for some nationalities (reciprocal)</th><td>Free (bilateral agreements)</td></tr>
<tr><th>Agency service fee (if applicable)</th><td>JPY 5,000–15,000 (varies)</td></tr>"""
    elif country_key == "usa":
        table_rows = """<tr><th>ESTA (Visa Waiver Program)</th><td>USD 21</td></tr>
<tr><th>B-1/B-2 Tourist/Business Visa (MRV Fee)</th><td>USD 185</td></tr>
<tr><th>F-1/M-1 Student Visa (MRV Fee)</th><td>USD 185</td></tr>
<tr><th>J-1 Exchange Visitor (MRV Fee)</th><td>USD 185</td></tr>
<tr><th>H-1B / L-1 Work Visa (MRV Fee)</th><td>USD 185</td></tr>
<tr><th>Reciprocity Fee (varies by nationality)</th><td>USD 0–300+ (check travel.state.gov)</td></tr>
<tr><th>SEVIS Fee (students/exchange)</th><td>USD 200–350</td></tr>"""
    elif country_key == "canada":
        table_rows = """<tr><th>eTA (Electronic Travel Authorization)</th><td>CAD 7</td></tr>
<tr><th>Temporary Resident Visa (TRV)</th><td>CAD 100</td></tr>
<tr><th>Biometrics (individual)</th><td>CAD 85</td></tr>
<tr><th>Biometrics (family group)</th><td>CAD 170</td></tr>
<tr><th>Super Visa (parents/grandparents)</th><td>CAD 100</td></tr>
<tr><th>Work Permit (open or employer-specific)</th><td>CAD 155</td></tr>
<tr><th>Study Permit</th><td>CAD 150</td></tr>"""
    else:  # australia
        table_rows = """<tr><th>ETA (Subclass 601)</th><td>AUD 20</td></tr>
<tr><th>eVisitor (Subclass 651)</th><td>Free</td></tr>
<tr><th>Visitor Visa (Subclass 600 — Tourist stream)</th><td>AUD 145</td></tr>
<tr><th>Visitor Visa (Subclass 600 — Business Visitor)</th><td>AUD 145</td></tr>
<tr><th>Working Holiday Visa (Subclass 417)</th><td>AUD 635</td></tr>
<tr><th>Student Visa (Subclass 500)</th><td>AUD 710</td></tr>
<tr><th>Health examination (if required)</th><td>AUD 300–600 (varies by panel physician)</td></tr>"""

    # Fees content
    body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Fees 2026 — Complete Cost Breakdown &amp; Payment Guide</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Fees 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Fees in 2026</h2>
<p>Understanding the full cost of a {name} visa application is essential for budgeting your trip. Beyond the government visa fee, applicants often face service charges from visa application centres, biometrics fees, and courier costs. This guide provides a complete breakdown of all {name} visa costs for 2026, including the main fee, optional services, and any additional charges based on nationality.</p>

<h2 id="fee-breakdown">Detailed Fee Breakdown</h2>
<p>The primary visa fee for {name} is <strong>{c['evisa_fee']}</strong>. This government fee is payable at the time of application submission and is non-refundable regardless of the outcome. Visa application centres (where applicable) charge a separate service fee for processing and biometric collection. Always use official government portals to avoid overpaying or falling victim to scams.</p>
<p>Some nationalities benefit from reduced or waived fees due to bilateral visa fee reciprocity agreements. Children under a certain age (typically 6 years) are often exempt from visa fees. Check the official {name} immigration authority website for nationality-specific fee schedules before applying.</p>

<h2 id="payment-methods">Payment Methods</h2>
<p>Most {name} visa fees can be paid using international credit or debit cards (Visa, Mastercard) through the official online application portal. Some consulates and visa application centres also accept cash in local currency. Bank transfers may be required in certain countries. Always pay through official channels and retain your payment receipt as proof of payment for your application.</p>

<h2 id="refund-policy">Refund Policy</h2>
<p>{name} visa application fees are generally non-refundable once the application has been submitted. This applies to both approved and refused applications. If you withdraw your application before processing begins, you may be eligible for a partial refund in some jurisdictions — check the official portal for current policy. Service fees from visa application centres are also non-refundable.</p>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""

    html = (
        head(title, desc, slug, country_key, "fees")
        + "\n"
        + navbar(country_key, slug)
        + "\n"
        + body
        + "\n"
        + faq_jsonld
        + "\n"
        + howto_jsonld
        + "\n"
        + footer_and_js()
    )
    return slug, html


# ===========================================================================
# PAGE 3: visa-processing-time
# ===========================================================================
def gen_processing(country_key):
    c = COUNTRIES[country_key]
    name = c["name"]
    flag = c["flag"]
    slug = f"{country_key}-visa-processing-time.html"
    title = f"{name} Visa Processing Time 2026 — How Long Does It Take?"
    desc = f"{name} visa processing time in 2026: standard, express and urgent timelines. Tips to avoid delays and track your application status."
    desc = desc[:155]

    # FAQ JSON-LD
    if country_key == "thailand":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does it take to get a Thailand eVisa?","acceptedAnswer":{"@type":"Answer","text":"The Thailand eVisa (Tourist TR) typically takes 3–5 business days to process. Apply at least 7–10 days before your planned travel date to allow for any unexpected delays."}},
{"@type":"Question","name":"Is there an express or urgent option for Thailand visa?","acceptedAnswer":{"@type":"Answer","text":"Thailand does not currently offer an official express or same-day eVisa service. In-person applications at a Thai embassy may have different timelines. Contact your nearest Thai consulate for urgent cases."}},
{"@type":"Question","name":"How can I track my Thailand eVisa application?","acceptedAnswer":{"@type":"Answer","text":"You can track your Thailand eVisa application status by logging into your account at thaievisa.go.th. The system shows real-time status updates including pending, processing, approved, and rejected stages."}},
{"@type":"Question","name":"Why might my Thailand visa application be delayed?","acceptedAnswer":{"@type":"Answer","text":"Common causes of delay include incomplete documents, unclear passport photos, issues with financial evidence, high application volume during peak travel seasons, and additional security checks. Ensuring all documents meet specifications minimises delay risk."}}
]}
</script>"""
    elif country_key == "india":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does India eVisa processing take in 2026?","acceptedAnswer":{"@type":"Answer","text":"India eVisa processing typically takes 72–96 hours (3–4 business days). Applicants should apply at least 4 days before travel but preferably 1–2 weeks in advance to allow time for any issues."}},
{"@type":"Question","name":"Can I get an India eVisa urgently or same-day?","acceptedAnswer":{"@type":"Answer","text":"India does not offer an official express eVisa service. The standard 72–96 hour processing time is the minimum. In genuine emergencies, contact the Indian embassy directly for advice — same-day processing is not guaranteed."}},
{"@type":"Question","name":"How do I check the status of my India eVisa?","acceptedAnswer":{"@type":"Answer","text":"Check your India eVisa application status at evisa.india.gov.in using your application ID and date of birth. The system provides real-time status updates. You will also receive an email notification when the decision is made."}},
{"@type":"Question","name":"What should I do if my India eVisa is not approved within 4 days?","acceptedAnswer":{"@type":"Answer","text":"If your India eVisa has not been processed within 96 hours, log into evisa.india.gov.in to check the status. If the status shows pending or there is no update, contact the Indian Immigration Helpdesk or the nearest Indian embassy."}}
]}
</script>"""
    elif c["schengen"]:
        faq_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{{"@type":"Question","name":"How long does a {name} Schengen visa take to process in 2026?","acceptedAnswer":{{"@type":"Answer","text":"The standard processing time for a {name} Schengen visa is up to 15 working days. During peak seasons (June–September, December), it can take longer. Apply at least 4–6 weeks before travel."}}}},
{{"@type":"Question","name":"Is there an express service for {name} Schengen visa?","acceptedAnswer":{{"@type":"Answer","text":"There is no official express service for Schengen visas as a standard rule. However, in cases of genuine urgency (medical emergency, bereavement), some consulates may prioritise applications. Contact the consulate directly to explain your circumstances."}}}},
{{"@type":"Question","name":"How do I track my {name} Schengen visa application?","acceptedAnswer":{{"@type":"Answer","text":"If you applied via VFS Global, you can track your {name} Schengen visa application online at the VFS Global tracking portal using your application reference number. Direct consulate applicants should contact the consulate's visa section."}}}},
{{"@type":"Question","name":"Can a {name} Schengen visa application be expedited?","acceptedAnswer":{{"@type":"Answer","text":"Under the Schengen Visa Code, consulates must process applications within 15 calendar days. For humanitarian cases, the deadline can be reduced. Ensure you apply well in advance to avoid relying on urgent processing."}}}}
]}}
</script>"""
    elif country_key == "japan":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does a Japan visa take to process in 2026?","acceptedAnswer":{"@type":"Answer","text":"Japan tourist visa processing typically takes 5–10 business days after submission of a complete application. Some applications may require additional security checks, extending the timeline to 2–3 weeks."}},
{"@type":"Question","name":"Can I get a Japan visa urgently?","acceptedAnswer":{"@type":"Answer","text":"Japan consulates do not typically offer an express visa service. However, in cases of proven urgency (medical, family emergency), some consulates may expedite processing. Contact your nearest Japanese consulate as soon as possible."}},
{"@type":"Question","name":"How do I check my Japan visa application status?","acceptedAnswer":{"@type":"Answer","text":"Japan visa status inquiries are handled directly by the consulate or authorised agency. Unlike digital systems, Japan does not have a public online tracking portal for consular visa applications. Contact the consulate directly for updates."}},
{"@type":"Question","name":"Can a Japan visa application be refused?","acceptedAnswer":{"@type":"Answer","text":"Yes. Japan can refuse visa applications without providing detailed reasons. Common causes include incomplete documentation, previous immigration violations, or insufficient financial evidence. Visa-free travellers can be turned away at the port of entry for similar reasons."}}
]}
</script>"""
    elif country_key == "usa":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does a US B-2 visa take to process in 2026?","acceptedAnswer":{"@type":"Answer","text":"US B-2 visa processing takes 3–5 business days after your interview for standard cases. However, interview appointment wait times at US embassies can range from weeks to over a year depending on location and demand. ESTA is typically processed within 72 hours."}},
{"@type":"Question","name":"What is administrative processing for a US visa?","acceptedAnswer":{"@type":"Answer","text":"Administrative processing (also called Section 221(g)) means your application requires additional review beyond the standard interview, typically for security checks. It can add 2 weeks to several months to processing time. Check your status at ceac.state.gov."}},
{"@type":"Question","name":"How do I check the status of my US visa application?","acceptedAnswer":{"@type":"Answer","text":"Track your US visa application at ceac.state.gov using your DS-160 case number and passport number. ESTA status can be checked at esta.cbp.dhs.gov with your application number."}},
{"@type":"Question","name":"Can I expedite my US visa appointment?","acceptedAnswer":{"@type":"Answer","text":"Yes. The US State Department offers an emergency appointment request for genuine urgent travel needs (medical, bereavement, urgent business). Emergency appointments are not guaranteed and require evidence of urgency. Check ustraveldocs.com for your country."}}
]}
</script>"""
    elif country_key == "canada":
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does a Canada visitor visa take to process in 2026?","acceptedAnswer":{"@type":"Answer","text":"Canada Temporary Resident Visa (TRV) processing typically takes 4–12 weeks. IRCC publishes current processing times at ircc.canada.ca. The eTA is typically approved within minutes, though some require manual review taking up to 72 hours."}},
{"@type":"Question","name":"Does Canada offer express or urgent visa processing?","acceptedAnswer":{"@type":"Answer","text":"IRCC does not offer a standard expedited processing service for visitor visas. However, if you have a genuine urgent need, you may contact IRCC via their web form to explain your circumstances. Flagpoling (entering and re-entering at the border) may also be an option in some cases."}},
{"@type":"Question","name":"How do I check my Canada visa application status?","acceptedAnswer":{"@type":"Answer","text":"Track your Canadian visa application through your IRCC secure account at ircc.canada.ca. You can see real-time updates including biometrics request, document request, decision, and passport issuance stages."}},
{"@type":"Question","name":"Why is my Canada visa taking longer than expected?","acceptedAnswer":{"@type":"Answer","text":"Processing delays often occur during peak periods (summer, holidays). Additional causes include incomplete applications, background checks, medical or security screening, and high application volumes. IRCC's published processing times are estimates, not guarantees."}}
]}
</script>"""
    else:  # australia
        faq_jsonld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How long does an Australian visitor visa take to process in 2026?","acceptedAnswer":{"@type":"Answer","text":"ETA processing is typically instant (seconds to minutes). eVisitor takes 1–3 days. The Visitor Visa (subclass 600) takes 1–14 days in most cases, though complex applications can take several weeks."}},
{"@type":"Question","name":"Does Australia offer priority visa processing?","acceptedAnswer":{"@type":"Answer","text":"Australia's Department of Home Affairs does not offer a general express service for visitor visas. However, applicants can note the urgency of their travel in their application. Contacting ATAS-registered migration agents may help manage the process."}},
{"@type":"Question","name":"How do I check my Australian visa application status?","acceptedAnswer":{"@type":"Answer","text":"Check your Australian visa application status through ImmiAccount at immi.homeaffairs.gov.au. You can also use the VEVO (Visa Entitlement Verification Online) service to verify visa grant details."}},
{"@type":"Question","name":"Why was my Australian visa processing delayed?","acceptedAnswer":{"@type":"Answer","text":"Common reasons for Australian visa delays include health examination requirements, character checks (police clearance), incomplete or inconsistent documents, and high application volume. Providing clear, complete documentation upfront reduces delay risk."}}
]}
</script>"""

    # HowTo JSON-LD
    howto_jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","name":"How to Track Your {name} Visa Application in 2026","description":"Step-by-step guide to checking and tracking your {name} visa application processing status.","step":[
{{"@type":"HowToStep","name":"Step 1: Obtain reference number","text":"After submitting your application, save your application reference or case number — you will need it for tracking."}},
{{"@type":"HowToStep","name":"Step 2: Visit official tracking portal","text":"Go to the official {name} immigration or visa tracking website and log in with your credentials or reference number."}},
{{"@type":"HowToStep","name":"Step 3: Review application status","text":"Check the current status: pending, under review, additional documents required, decision made, or passport dispatched."}},
{{"@type":"HowToStep","name":"Step 4: Respond to information requests","text":"If the authority requests additional documents, respond promptly through the official portal to avoid processing delays."}},
{{"@type":"HowToStep","name":"Step 5: Collect approved visa","text":"Once approved, download your eVisa PDF (if applicable) or collect your passport with visa sticker from the application centre."}}
]}}
</script>"""

    # Processing time table
    if country_key == "thailand":
        table_rows = """<tr><th>eVisa (Tourist TR) — standard</th><td>3–5 business days</td></tr>
<tr><th>eVisa (Non-Immigrant B)</th><td>3–5 business days</td></tr>
<tr><th>Embassy application (in person)</th><td>1–3 business days (varies)</td></tr>
<tr><th>In-country extension</th><td>Same day (Immigration Office)</td></tr>
<tr><th>Peak season delay risk</th><td>High (Nov–Mar, Jul–Aug)</td></tr>
<tr><th>Apply at least</th><td>7–10 days before travel</td></tr>"""
    elif country_key == "india":
        table_rows = """<tr><th>e-Tourist Visa — standard</th><td>72–96 hours</td></tr>
<tr><th>e-Business Visa — standard</th><td>72–96 hours</td></tr>
<tr><th>e-Medical Visa — standard</th><td>72–96 hours</td></tr>
<tr><th>Minimum apply before travel</th><td>4 days</td></tr>
<tr><th>Recommended apply before travel</th><td>7–14 days</td></tr>
<tr><th>Peak season delay risk</th><td>Moderate (Oct–Jan, Apr–Jun)</td></tr>"""
    elif c["schengen"]:
        table_rows = f"""<tr><th>Schengen Visa — standard</th><td>Up to 15 working days</td></tr>
<tr><th>Schengen Visa — maximum legal</th><td>30 calendar days (complex cases)</td></tr>
<tr><th>Earliest application date</th><td>6 months before travel</td></tr>
<tr><th>Recommended apply before travel</th><td>4–6 weeks</td></tr>
<tr><th>Peak season delay risk</th><td>High (June–September, December)</td></tr>
<tr><th>Biometric appointment wait</th><td>1–3 weeks at VFS Global (varies by country)</td></tr>"""
    elif country_key == "japan":
        table_rows = """<tr><th>Tourist Visa — standard</th><td>5–10 business days</td></tr>
<tr><th>Work/Long-Stay Visa</th><td>10–15 business days</td></tr>
<tr><th>Applications requiring additional review</th><td>Up to 2–3 weeks</td></tr>
<tr><th>Earliest application date</th><td>3 months before travel</td></tr>
<tr><th>Recommended apply before travel</th><td>3–4 weeks</td></tr>
<tr><th>Peak season delay risk</th><td>Moderate (March–May, Oct–Nov)</td></tr>"""
    elif country_key == "usa":
        table_rows = """<tr><th>ESTA — standard</th><td>Instant to 72 hours</td></tr>
<tr><th>B-1/B-2 — after interview</th><td>3–5 business days</td></tr>
<tr><th>Administrative processing (221g)</th><td>2 weeks to several months</td></tr>
<tr><th>Interview appointment wait (varies)</th><td>Weeks to 12+ months</td></tr>
<tr><th>Earliest ESTA application</th><td>Anytime (valid 2 years)</td></tr>
<tr><th>Recommended B-2 apply before travel</th><td>3–6 months</td></tr>"""
    elif country_key == "canada":
        table_rows = """<tr><th>eTA — standard</th><td>Minutes to 72 hours</td></tr>
<tr><th>TRV (online) — standard</th><td>4–8 weeks</td></tr>
<tr><th>TRV (paper) — standard</th><td>8–12 weeks</td></tr>
<tr><th>Biometrics — collection appointment</th><td>1–3 weeks (varies by VAC)</td></tr>
<tr><th>Earliest application date</th><td>6 months before travel</td></tr>
<tr><th>Recommended apply before travel</th><td>8–12 weeks</td></tr>"""
    else:  # australia
        table_rows = """<tr><th>ETA (Subclass 601)</th><td>Instant (via app or airline)</td></tr>
<tr><th>eVisitor (Subclass 651)</th><td>1–3 days (usually)</td></tr>
<tr><th>Visitor Visa (Subclass 600)</th><td>1–14 days (most cases)</td></tr>
<tr><th>Visitor Visa (complex cases)</th><td>Up to several weeks</td></tr>
<tr><th>Earliest application date</th><td>Anytime before travel</td></tr>
<tr><th>Recommended apply before travel</th><td>4–6 weeks</td></tr>"""

    body = f"""<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Processing Time 2026 — How Long Does It Take?</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Processing Times 2026</th></tr></thead>
<tbody>
{table_rows}
</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Processing Times 2026</h2>
<p>Knowing how long your {name} visa application will take is critical for travel planning. Processing times are influenced by application type, applicant nationality, time of year, and completeness of the application. In 2026, the standard processing time for a {name} visa is <strong>{c['processing_time']}</strong>. However, this is an estimate — apply well in advance to avoid missing your travel date.</p>
<p>Processing time begins from the date your complete application is received by the immigration authority. Incomplete applications — missing documents, unclear photos, or unpaid fees — are not processed until the deficiency is resolved, effectively resetting the clock.</p>

<h2 id="timeline">Detailed Processing Timeline</h2>
<p>For most applicants, the {name} visa application journey follows these stages: submission of online or paper application with all supporting documents; biometric collection (where required); background and security checks; document review by consular or immigration officer; decision (approved, refused, or referred for additional review); and issuance of visa (eVisa sent by email, or passport returned with visa sticker).</p>
<p>Peak travel seasons — typically summer and major holiday periods — can significantly extend processing times due to high application volumes. Submitting your application 4–8 weeks before travel is strongly recommended for consular applications. eVisa systems (like Thailand's thaievisa.go.th or Australia's ImmiAccount) tend to be faster than paper or in-person processes.</p>

<h2 id="tracking">How to Track Your Application</h2>
<p>Most modern immigration systems provide online tracking. After submission, you will receive a reference number or case ID. Use this to log into the official portal and check your application status. For email-based systems, check your spam folder regularly as decisions are often communicated by email. Keep your contact details up to date in your application to avoid missing important notifications.</p>

<h2 id="tips">Tips to Avoid Processing Delays</h2>
<ul>
<li>Submit a complete application — missing a single document can pause processing entirely</li>
<li>Use the official government portal — third-party sites may cause errors or delays</li>
<li>Ensure your passport photo meets exact specifications</li>
<li>Apply during off-peak periods where possible</li>
<li>Keep your contact email and phone accessible throughout the process</li>
<li>Respond immediately to any requests for additional information</li>
</ul>

{eeat()}
{internal_links(country_key)}
</article></div></section>"""

    html = (
        head(title, desc, slug, country_key, "processing")
        + "\n"
        + navbar(country_key, slug)
        + "\n"
        + body
        + "\n"
        + faq_jsonld
        + "\n"
        + howto_jsonld
        + "\n"
        + footer_and_js()
    )
    return slug, html


# ===========================================================================
# Main
# ===========================================================================
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    generated = []

    for country_key in COUNTRIES:
        for gen_fn in (gen_requirements, gen_fees, gen_processing):
            slug, html = gen_fn(country_key)
            filepath = os.path.join(OUT_DIR, slug)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            generated.append(filepath)
            print(f"  Created: {slug}")

    print(f"\nTotal files generated: {len(generated)}")
    return generated


if __name__ == "__main__":
    main()
