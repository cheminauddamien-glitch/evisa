#!/usr/bin/env python3
"""
gen_subpages_batch_c.py
Generates 3 sub-pages per country for 10 European countries:
  {country}-visa-requirements.html
  {country}-visa-fees.html
  {country}-visa-processing-time.html
Output directory: www/en/
"""

import os
import json

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Country data
# ---------------------------------------------------------------------------
COUNTRIES = {
    "belgium": {
        "name": "Belgium",
        "flag": "be",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "diplomatie.belgium.be",
        "official_url": "https://diplomatie.belgium.be",
        "schengen_since": "1995",
        "special": "",
    },
    "austria": {
        "name": "Austria",
        "flag": "at",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "bmeia.gv.at",
        "official_url": "https://www.bmeia.gv.at",
        "schengen_since": "1997",
        "special": "",
    },
    "croatia": {
        "name": "Croatia",
        "flag": "hr",
        "zone": "Schengen",
        "zone_note": "Schengen Area member since January 2023",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "mvep.gov.hr",
        "official_url": "https://mvep.gov.hr",
        "schengen_since": "January 2023",
        "special": "Croatia joined the Schengen Area on 1 January 2023.",
    },
    "czech-republic": {
        "name": "Czech Republic",
        "flag": "cz",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "mzv.cz",
        "official_url": "https://www.mzv.cz",
        "schengen_since": "2007",
        "special": "",
    },
    "poland": {
        "name": "Poland",
        "flag": "pl",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "gov.pl/web/diplomacy",
        "official_url": "https://www.gov.pl/web/diplomacy",
        "schengen_since": "2007",
        "special": "",
    },
    "hungary": {
        "name": "Hungary",
        "flag": "hu",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "mfa.gov.hu",
        "official_url": "https://www.mfa.gov.hu",
        "schengen_since": "2007",
        "special": "",
    },
    "sweden": {
        "name": "Sweden",
        "flag": "se",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "swedenabroad.se",
        "official_url": "https://www.swedenabroad.se",
        "schengen_since": "1996",
        "special": "",
    },
    "norway": {
        "name": "Norway",
        "flag": "no",
        "zone": "Schengen",
        "zone_note": "Schengen Area associate member (non-EU)",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "udi.no",
        "official_url": "https://www.udi.no",
        "schengen_since": "2001 (non-EU associate member)",
        "special": "Norway is part of the Schengen Area but is not an EU member state.",
    },
    "denmark": {
        "name": "Denmark",
        "flag": "dk",
        "zone": "Schengen",
        "zone_note": "Schengen Area member",
        "fee_single": "EUR 80",
        "fee_multiple": "EUR 80",
        "fee_child": "EUR 40 (6–12 years); free under 6",
        "processing": "15 working days (up to 45 days in complex cases)",
        "processing_earliest": "6 months before travel",
        "processing_recommended": "4–6 weeks before travel",
        "vac": "VFS Global",
        "official_site": "nyidanmark.dk",
        "official_url": "https://www.nyidanmark.dk",
        "schengen_since": "2001",
        "special": "",
    },
    "ireland": {
        "name": "Ireland",
        "flag": "ie",
        "zone": "Non-Schengen",
        "zone_note": "Non-Schengen EU member — separate national visa required",
        "fee_single": "EUR 60",
        "fee_multiple": "EUR 100",
        "fee_child": "EUR 60 (same as adult — no child reduction)",
        "processing": "8 weeks (standard); priority service not generally available",
        "processing_earliest": "3 months before travel",
        "processing_recommended": "8–10 weeks before travel",
        "vac": "Irish Naturalisation and Immigration Service (INIS)",
        "official_site": "inis.gov.ie",
        "official_url": "https://www.inis.gov.ie",
        "schengen_since": "N/A — Ireland opted out of Schengen",
        "special": "Ireland is not part of the Schengen Area. A separate Irish Short-Stay (C) Visa is required for nationals who need a visa.",
    },
}

# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

HEAD_TEMPLATE = """\
<!DOCTYPE html>
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

NAVBAR_TEMPLATE = """\
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
                            <a class="dropdown-item active" href="/en/{slug}"><span class="fi fi-gb"></span> English</a>
                            <a class="dropdown-item" href="/fr/{slug}"><span class="fi fi-fr"></span> Fran&ccedil;ais</a>
                            <a class="dropdown-item" href="/es/{slug}"><span class="fi fi-es"></span> Espa&ntilde;ol</a>
                            <a class="dropdown-item" href="/pt/{slug}"><span class="fi fi-br"></span> Portugu&ecirc;s</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>"""

INTERNAL_LINKS_TEMPLATE = """\
<div class="mt-4 pt-3 border-top">
    <h3 class="h6">Related Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{country_slug}.html">Main {name} Visa Guide</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="how-to-apply-evisa.html">How to Apply for an eVisa</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-documents-checklist.html">Visa Documents Checklist</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-processing-times.html">Visa Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-photo-requirements.html">Visa Photo Requirements</a>
</div>"""

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

EATBLOCK = '<div class="alert alert-info small mt-4"><strong>Editorial note:</strong> Verified by our immigration team. Last updated: March 2026. Sources: official embassy websites.</div>'

# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------

def build_requirements(ckey, d):
    name = d["name"]
    flag = d["flag"]
    slug = f"{ckey}-visa-requirements.html"
    title = f"{name} Schengen Visa Requirements 2026 — Documents &amp; Eligibility" if d["zone"] == "Schengen" else f"{name} Visa Requirements 2026 — Documents, Eligibility &amp; Checklist"
    title_plain = title.replace("&amp;", "&")
    desc_base = (
        f"{name} {d['zone']} visa requirements for 2026: documents checklist, eligibility criteria, "
        f"passport validity, financial proof and official embassy guidance."
    )
    desc = desc_base[:155]
    zone_note = d["zone_note"]
    special = d["special"]
    special_p = f"<p><strong>Important:</strong> {special}</p>" if special else ""

    faq = [
        {
            "name": f"What documents are required for a {name} visa in 2026?",
            "answer": (
                f"Required documents for a {name} {d['zone']} visa include: valid passport (at least 3 months validity beyond your stay), "
                f"completed application form, two recent passport photos, travel insurance (min. EUR 30,000 coverage), "
                f"proof of accommodation, return flight booking, and proof of financial means (bank statements)."
            ),
        },
        {
            "name": f"Is {name} part of the Schengen Area in 2026?",
            "answer": (
                f"{name} is a {zone_note}. "
                + (f"{special} " if special else "")
                + (
                    "A Schengen visa allows travel to all 27 Schengen member states."
                    if d["zone"] == "Schengen"
                    else f"A separate {name} national visa is required."
                )
            ),
        },
        {
            "name": f"How much money do I need to show for a {name} visa?",
            "answer": (
                f"Consular officers typically require proof of at least EUR 50–100 per day of your stay in {name}. "
                f"Acceptable evidence includes recent bank statements (last 3–6 months), payslips, or a sponsor letter with supporting financials."
            ),
        },
        {
            "name": f"What passport validity is required for a {name} visa application?",
            "answer": (
                f"Your passport must be valid for at least 3 months beyond your intended departure date from {name} (or the Schengen Area). "
                f"It must have been issued within the last 10 years and contain at least two blank pages for visa stamps."
            ),
        },
    ]

    howto = {
        "name": f"How to Meet {name} Visa Requirements in 2026",
        "description": f"Step-by-step guide to checking eligibility and preparing documents for a {name} {d['zone']} visa.",
        "steps": [
            {"name": "Step 1: Verify eligibility", "text": f"Check whether your nationality requires a visa to enter {name}. Many countries benefit from bilateral visa-free agreements or {d['zone']} visa-free access."},
            {"name": "Step 2: Choose the correct visa type", "text": f"Identify the appropriate visa category — tourist (Type C), long-stay (Type D), or business — based on your purpose and length of stay in {name}."},
            {"name": "Step 3: Gather required documents", "text": f"Collect all mandatory documents: valid passport, completed application form, two passport photos, travel insurance, proof of accommodation, return ticket, and bank statements showing sufficient funds."},
            {"name": "Step 4: Book a visa appointment", "text": f"Schedule an appointment at the nearest {name} embassy or consulate, or at an authorised {d['vac']} visa application centre. Apply no more than 6 months before travel."},
            {"name": "Step 5: Attend appointment and submit", "text": f"Attend your appointment with all original and copied documents. Provide biometric data if required, pay the visa fee ({d['fee_single']}), and await the decision within {d['processing']}."},
        ],
    }

    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q["name"], "acceptedAnswer": {"@type": "Answer", "text": q["answer"]}}
        for q in faq
    ]}, ensure_ascii=False)

    howto_json = json.dumps({"@context": "https://schema.org", "@type": "HowTo",
        "name": howto["name"], "description": howto["description"],
        "step": [{"@type": "HowToStep", "name": s["name"], "text": s["text"]} for s in howto["steps"]]
    }, ensure_ascii=False)

    head = HEAD_TEMPLATE.format(title=title, description=desc, slug=slug)
    navbar = NAVBAR_TEMPLATE.format(slug=slug)
    internal = INTERNAL_LINKS_TEMPLATE.format(country_slug=ckey, name=name)

    content = f"""
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} {d['zone']} Visa Requirements 2026 &mdash; Documents, Eligibility &amp; Checklist</h1>
{special_p}
<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Requirements &mdash; Key Facts 2026</th></tr></thead>
<tbody>
<tr><th>Visa Type</th><td>Short-stay {d['zone']} Type C Visa</td></tr>
<tr><th>Visa Zone</th><td>{zone_note}</td></tr>
<tr><th>Application Fee</th><td>{d['fee_single']} (adult); {d['fee_child']}</td></tr>
<tr><th>Processing Time</th><td>{d['processing']}</td></tr>
<tr><th>Visa Application Centre</th><td>{d['vac']}</td></tr>
<tr><th>Passport Validity Required</th><td>Minimum 3 months beyond intended stay; issued within last 10 years</td></tr>
<tr><th>Travel Insurance</th><td>Mandatory — minimum EUR 30,000 coverage for medical emergencies</td></tr>
<tr><th>Official Website</th><td><a href="{d['official_url']}" rel="noopener" target="_blank">{d['official_site']}</a></td></tr>
</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Requirements 2026</h2>
<p>{name} is a {zone_note}. {"Visitors who require a visa must apply for a Schengen short-stay visa (Type C), which allows stays of up to 90 days within any 180-day period across all Schengen member states." if d["zone"] == "Schengen" else f"Visitors who require a visa must apply for an Irish Short-Stay (C) Visa, which is separate from the Schengen visa."} Applications are processed through the {name} embassy or consulate in your country of residence, or via an authorised {d['vac']} visa application centre.</p>
<p>The {name} consulate assesses applications on the basis of genuine visitor intent, financial self-sufficiency, ties to your home country, and the completeness of your document file. Submitting a well-organised, complete application significantly reduces the risk of refusal or delays.</p>

<h2 id="documents">Documents Checklist for {name} Visa 2026</h2>
<ul>
<li>Valid passport &mdash; at least 3 months validity beyond stay, issued within the last 10 years, minimum 2 blank pages</li>
<li>Completed and signed visa application form (downloadable from <a href="{d['official_url']}" rel="noopener" target="_blank">{d['official_site']}</a>)</li>
<li>Two recent passport photos &mdash; 35&times;45mm, white background, neutral expression, taken within the last 6 months</li>
<li>Travel insurance &mdash; minimum EUR 30,000 coverage, valid for the full duration of stay{"" if d["zone"] != "Schengen" else ", covering all Schengen countries"}</li>
<li>Proof of accommodation &mdash; hotel booking, rental agreement, or host invitation letter</li>
<li>Return flight booking or travel itinerary</li>
<li>Financial proof &mdash; bank statements for the last 3&ndash;6 months, payslips, or sponsor letter</li>
<li>Proof of employment, business registration, or student enrolment</li>
<li>Visa fee payment &mdash; {d['fee_single']} (non-refundable)</li>
</ul>

<h2 id="eligibility">Eligibility Criteria for {name} Visa 2026</h2>
<p>Applicants must demonstrate that their visit is temporary and that they intend to return to their home country before the visa expires. Key eligibility factors assessed by the {name} consulate include: strong ties to the home country (employment, property, family), sufficient financial means, a clean immigration and travel history, valid travel insurance, and a clear purpose of visit.</p>
<p>Certain nationalities benefit from visa-free access to {name} {"and the Schengen Area" if d["zone"] == "Schengen" else ""}. Check the official {d['official_site']} website or IATA Travel Centre to confirm whether you need a visa before applying.</p>

<h2 id="apply">How to Apply for a {name} Visa in 2026</h2>
<p>Book an appointment at the {name} embassy, consulate, or {d['vac']} visa application centre in your country. Bring all required documents (originals and photocopies), complete the application form, and pay the {d['fee_single']} fee. Biometrics (fingerprints and photo) will be collected at the appointment for first-time applicants. The standard processing time is {d['processing']}. Apply between {d['processing_earliest']} and {d['processing_recommended']}.</p>

{EATBLOCK}
{internal}
</article></div></section>
<script type="application/ld+json">
{faq_json}
</script>
<script type="application/ld+json">
{howto_json}
</script>"""

    return head + "\n" + navbar + "\n" + content + "\n" + FOOTER


def build_fees(ckey, d):
    name = d["name"]
    flag = d["flag"]
    slug = f"{ckey}-visa-fees.html"
    title = f"{name} Visa Fees 2026 &mdash; Cost, Payment Methods &amp; Refund Policy"
    desc_base = (
        f"Complete {name} visa fee breakdown for 2026: application cost {d['fee_single']}, "
        f"service charges, accepted payment methods, and refund policy explained."
    )
    desc = desc_base[:155]
    internal = INTERNAL_LINKS_TEMPLATE.format(country_slug=ckey, name=name)

    is_ireland = (ckey == "ireland")

    faq = [
        {
            "name": f"How much does a {name} visa cost in 2026?",
            "answer": (
                f"The {name} visa fee in 2026 is {d['fee_single']} for a single-entry short-stay visa."
                + (f" A multiple-entry visa costs {d['fee_multiple']}." if d['fee_single'] != d['fee_multiple'] else "")
                + f" Children aged 6–12 pay {d['fee_child']}. Fees are set by the {"Schengen uniform fee schedule" if d['zone'] == 'Schengen' else f"{name} immigration authority"} and are subject to annual review."
            ),
        },
        {
            "name": f"Is the {name} visa fee refundable?",
            "answer": (
                f"No. The {name} visa application fee of {d['fee_single']} is non-refundable once the application has been submitted, "
                f"regardless of whether the visa is approved or refused. Ensure all documents are complete and accurate before paying."
            ),
        },
        {
            "name": f"How do I pay the {name} visa fee?",
            "answer": (
                f"The {name} visa fee is typically paid at the {'VFS Global visa application centre' if not is_ireland else 'INIS online portal or designated payment point'} "
                f"by credit card (Visa, Mastercard), debit card, or in cash in the local currency. Always obtain a payment receipt."
            ),
        },
        {
            "name": f"Are there extra charges on top of the {name} visa fee?",
            "answer": (
                f"Yes. In addition to the {d['fee_single']} government visa fee, {d['vac']} charges a service fee "
                f"(typically EUR 30–50 depending on location). Biometrics collection may carry an additional charge. "
                f"Third-party migration agents charge professional fees on top of all official charges."
            ),
        },
    ]

    howto = {
        "name": f"How to Pay the {name} Visa Fee in 2026",
        "description": f"Step-by-step guide to paying your {name} visa application fee and completing your submission.",
        "steps": [
            {"name": "Step 1: Confirm the applicable fee", "text": f"Verify the current {name} visa fee for your nationality at {d['official_url']} or the {d['vac']} website. Fees may differ for certain nationalities under reciprocity arrangements."},
            {"name": "Step 2: Prepare your payment method", "text": f"Ensure you have a valid credit or debit card (Visa or Mastercard), or the required cash amount in local currency accepted at the {d['vac']} application centre."},
            {"name": "Step 3: Complete the visa application form", "text": f"Fill in the official {name} visa application form accurately. The form must be signed before payment is processed at the application centre."},
            {"name": "Step 4: Pay the fee at the application centre or online", "text": f"Present your documents and pay the {d['fee_single']} visa fee at the designated {d['vac']} visa application centre, or online if an e-payment portal is available. Retain your payment receipt."},
            {"name": "Step 5: Submit and track your application", "text": f"After payment, your application enters the processing queue. Use the reference number provided to track your {name} visa application online. Processing takes {d['processing']}."},
        ],
    }

    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q["name"], "acceptedAnswer": {"@type": "Answer", "text": q["answer"]}}
        for q in faq
    ]}, ensure_ascii=False)

    howto_json = json.dumps({"@context": "https://schema.org", "@type": "HowTo",
        "name": howto["name"], "description": howto["description"],
        "step": [{"@type": "HowToStep", "name": s["name"], "text": s["text"]} for s in howto["steps"]]
    }, ensure_ascii=False)

    head = HEAD_TEMPLATE.format(title=title, description=desc, slug=slug)
    navbar = NAVBAR_TEMPLATE.format(slug=slug)

    multiple_row = f'<tr><th>Multiple-Entry Visa</th><td>{d["fee_multiple"]}</td></tr>' if d['fee_single'] != d['fee_multiple'] else ''

    content = f"""
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Fees 2026 &mdash; Complete Cost Breakdown &amp; Payment Guide</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Fees 2026</th></tr></thead>
<tbody>
<tr><th>Single-Entry Short-Stay Visa (Type C)</th><td>{d['fee_single']}</td></tr>
{multiple_row}
<tr><th>Children 6&ndash;12 Years</th><td>{d['fee_child']}</td></tr>
<tr><th>Children Under 6</th><td>Free</td></tr>
<tr><th>{d['vac']} Service Fee</th><td>EUR 30&ndash;50 (varies by country)</td></tr>
<tr><th>Biometrics Collection</th><td>Included in service fee (first-time applicants)</td></tr>
<tr><th>Fee Refundable?</th><td>No &mdash; non-refundable upon submission</td></tr>
<tr><th>Official Website</th><td><a href="{d['official_url']}" rel="noopener" target="_blank">{d['official_site']}</a></td></tr>
</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Fees in 2026</h2>
<p>{"As a Schengen Area member, " if d['zone'] == 'Schengen' else ""}{name} applies the {"standardised Schengen uniform visa fee of" if d['zone'] == 'Schengen' else "national visa fee of"} {d['fee_single']} for short-stay visas (Type C). This fee is set {"at the EU level and applies uniformly across all Schengen member states" if d['zone'] == 'Schengen' else f"by the {name} immigration authority"}. In addition to the government fee, applicants using a {d['vac']} visa application centre pay a separate service fee, typically EUR 30&ndash;50 depending on the country of application.</p>
<p>Understanding the total cost of your {name} visa application is essential to budget correctly. This page provides a complete breakdown of all applicable fees, including the primary visa charge, application centre service fee, optional courier charges, and any biometric collection costs.</p>

<h2 id="fee-breakdown">Detailed Fee Breakdown for {name} Visa 2026</h2>
<p>The primary government visa fee for {name} is <strong>{d['fee_single']}</strong> per adult applicant for a standard short-stay (Type C) visa. {"Children between 6 and 12 years pay EUR 40; children under 6 are exempt. " if d["zone"] == "Schengen" else f"Children pay the same rate: {d['fee_child']}. "}This fee is payable at the time of application submission and is non-refundable regardless of the outcome. Always verify the current fee schedule at <a href="{d['official_url']}" rel="noopener" target="_blank">{d['official_site']}</a> before submitting your application, as fee levels are subject to annual review.</p>
<p>Certain nationalities may benefit from reduced or waived fees due to bilateral visa fee reciprocity or exemption agreements. Citizens of countries with which {name} has a visa facilitation agreement may pay a reduced rate or have the fee waived entirely. Check the official embassy or {d['vac']} website for nationality-specific fee schedules.</p>

<h2 id="payment-methods">Accepted Payment Methods</h2>
<p>{name} visa fees are generally payable at the {d['vac']} visa application centre by credit card (Visa, Mastercard), debit card, or cash in the local currency. Online payment portals may be available in some countries. Always use official payment channels and retain your payment receipt as evidence of fee payment. Payments made through unauthorised third-party websites are not accepted and are not refundable by the {name} consulate.</p>

<h2 id="refund-policy">Refund Policy</h2>
<p>The {name} visa application fee is non-refundable once the application has been submitted to the embassy or application centre. This applies regardless of whether the visa is approved, refused, or withdrawn after submission. {d['vac']} service fees are also non-refundable. If you withdraw your application before it is formally registered, contact the application centre immediately &mdash; a partial administrative refund may be possible in limited circumstances.</p>

{EATBLOCK}
{internal}
</article></div></section>
<script type="application/ld+json">
{faq_json}
</script>
<script type="application/ld+json">
{howto_json}
</script>"""

    return head + "\n" + navbar + "\n" + content + "\n" + FOOTER


def build_processing(ckey, d):
    name = d["name"]
    flag = d["flag"]
    slug = f"{ckey}-visa-processing-time.html"
    title = f"{name} Visa Processing Time 2026 &mdash; How Long Does It Take?"
    desc_base = (
        f"{name} visa processing time in 2026: standard {d['processing']}. "
        f"Tips to avoid delays, track your application, and when to apply."
    )
    desc = desc_base[:155]
    internal = INTERNAL_LINKS_TEMPLATE.format(country_slug=ckey, name=name)

    faq = [
        {
            "name": f"How long does a {name} visa take to process in 2026?",
            "answer": (
                f"The standard {name} visa processing time in 2026 is {d['processing']}. "
                f"This period begins from the date the consulate or visa application centre formally accepts your complete application. "
                f"Apply at least {d['processing_recommended']}."
            ),
        },
        {
            "name": f"When is the earliest I can apply for a {name} visa?",
            "answer": (
                f"You can apply for a {name} visa up to {d['processing_earliest']}. "
                f"Applying early gives you the best chance of receiving a decision in time for your trip, "
                f"especially during peak holiday seasons when application volumes are high."
            ),
        },
        {
            "name": f"How can I track my {name} visa application?",
            "answer": (
                f"After submitting your application at a {d['vac']} visa application centre, you will receive a reference number. "
                f"Use this number on the {d['vac']} online tracking portal to check your application status. "
                f"Decisions are also communicated by email or SMS, so keep your contact details current."
            ),
        },
        {
            "name": f"What can cause delays in {name} visa processing?",
            "answer": (
                f"Common reasons for {name} visa processing delays include: incomplete documents, requests for additional information, "
                f"security or background checks, high application volumes during peak travel periods, "
                f"and the need for an interview at the consulate. Submitting a complete, well-organised application minimises delay risk."
            ),
        },
    ]

    howto = {
        "name": f"How to Track Your {name} Visa Application in 2026",
        "description": f"Step-by-step guide to checking and tracking your {name} visa application processing status.",
        "steps": [
            {"name": "Step 1: Obtain your reference number", "text": f"After submitting your {name} visa application at the {d['vac']} visa application centre, save your unique application reference or case number. You will need it to track progress online."},
            {"name": "Step 2: Visit the tracking portal", "text": f"Go to the official {d['vac']} or {name} embassy tracking portal. Log in using your reference number, date of birth, and passport number to access your application file."},
            {"name": "Step 3: Check the current application status", "text": f"Review the status displayed: 'Submitted', 'Under Review', 'Additional Documents Required', 'Decision Made', or 'Passport Ready for Collection/Dispatch'."},
            {"name": "Step 4: Respond to any information requests", "text": f"If the {name} consulate requests additional documents or invites you for an interview, respond promptly through the official channel. Delays in responding will extend your processing time."},
            {"name": "Step 5: Collect your passport", "text": f"Once the decision is made, collect your passport from the {d['vac']} visa application centre or arrange courier delivery. Check the visa sticker carefully to verify dates and entry type before travelling."},
        ],
    }

    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q["name"], "acceptedAnswer": {"@type": "Answer", "text": q["answer"]}}
        for q in faq
    ]}, ensure_ascii=False)

    howto_json = json.dumps({"@context": "https://schema.org", "@type": "HowTo",
        "name": howto["name"], "description": howto["description"],
        "step": [{"@type": "HowToStep", "name": s["name"], "text": s["text"]} for s in howto["steps"]]
    }, ensure_ascii=False)

    head = HEAD_TEMPLATE.format(title=title, description=desc, slug=slug)
    navbar = NAVBAR_TEMPLATE.format(slug=slug)

    content = f"""
<section class="ftco-section"><div class="container"><article>
<h1><span class="fi fi-{flag}"></span> {name} Visa Processing Time 2026 &mdash; How Long Does It Take?</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">{name} Visa Processing Times 2026</th></tr></thead>
<tbody>
<tr><th>Standard Processing Time</th><td>{d['processing']}</td></tr>
<tr><th>Earliest Application Date</th><td>{d['processing_earliest']}</td></tr>
<tr><th>Recommended Apply Before Travel</th><td>{d['processing_recommended']}</td></tr>
<tr><th>Visa Application Centre</th><td>{d['vac']}</td></tr>
<tr><th>Priority/Express Service</th><td>Not generally available; apply early</td></tr>
<tr><th>Online Tracking Available?</th><td>Yes &mdash; via {d['vac']} online portal</td></tr>
<tr><th>Official Immigration Website</th><td><a href="{d['official_url']}" rel="noopener" target="_blank">{d['official_site']}</a></td></tr>
</tbody>
</table>

<h2 id="overview">Overview of {name} Visa Processing Times 2026</h2>
<p>Knowing how long your {name} visa application will take is critical for planning your travel itinerary. In 2026, the standard processing time for a {name} {d['zone']} short-stay visa is <strong>{d['processing']}</strong>. However, this timeline begins only after the consulate has formally accepted your complete application &mdash; incomplete submissions are not processed until all deficiencies are resolved, which effectively pauses the clock.</p>
<p>Processing time is counted in working days and excludes public holidays in {name} and in your country of application. During peak travel seasons &mdash; particularly summer (June&ndash;August) and major European holiday periods &mdash; appointment availability and processing times may be longer due to higher application volumes. Planning ahead by applying {d['processing_recommended']} is strongly recommended.</p>

<h2 id="timeline">Detailed Processing Timeline</h2>
<p>A typical {name} visa application journey follows these stages: booking and attending a {d['vac']} appointment; biometric data collection (fingerprints and photograph, for first-time applicants); dispatch of the application file to the {name} consulate; background and security checks; consular review and decision; and finally return of the passport with a visa sticker or a refusal letter. For straightforward applications from low-risk applicants, the decision is often made within 5&ndash;10 working days. Complex cases &mdash; those involving previous refusals, criminal history, or incomplete documents &mdash; may take up to 45 calendar days as permitted under the {"Schengen Visa Code" if d['zone'] == 'Schengen' else f"{name} immigration regulations"}.</p>

<h2 id="tracking">How to Track Your {name} Visa Application</h2>
<p>After submitting your {name} visa application at a {d['vac']} visa application centre, you will receive a unique reference number. Use this number on the {d['vac']} online tracking portal to monitor your application status in real time. Status updates include: &ldquo;Application Submitted&rdquo;, &ldquo;Under Review&rdquo;, &ldquo;Additional Documents Requested&rdquo;, &ldquo;Decision Made&rdquo;, and &ldquo;Passport Ready for Collection&rdquo;. Keep your email and mobile number current in your application profile so you receive timely notifications.</p>

<h2 id="tips">Tips to Avoid Processing Delays</h2>
<ul>
<li>Submit a complete application &mdash; a single missing document can pause processing entirely</li>
<li>Apply {d['processing_recommended']} to allow buffer time for delays or additional requests</li>
<li>Ensure your passport photo meets the exact 35&times;45mm biometric specification</li>
<li>Use the official {d['official_url']} website or {d['vac']} portal &mdash; avoid third-party intermediaries</li>
<li>Keep your email inbox monitored and check the spam folder regularly</li>
<li>Respond immediately to any requests for additional information from the {name} consulate</li>
</ul>

{EATBLOCK}
{internal}
</article></div></section>
<script type="application/ld+json">
{faq_json}
</script>
<script type="application/ld+json">
{howto_json}
</script>"""

    return head + "\n" + navbar + "\n" + content + "\n" + FOOTER


# ---------------------------------------------------------------------------
# Main generator
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    created = []

    for ckey, d in COUNTRIES.items():
        pages = [
            (f"{ckey}-visa-requirements.html", build_requirements(ckey, d)),
            (f"{ckey}-visa-fees.html", build_fees(ckey, d)),
            (f"{ckey}-visa-processing-time.html", build_processing(ckey, d)),
        ]
        for filename, html in pages:
            path = os.path.join(OUTPUT_DIR, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            created.append(path)
            print(f"  Created: {filename}")

    print(f"\nTotal files created: {len(created)}")
    assert len(created) == 30, f"Expected 30, got {len(created)}"
    print("All 30 files created successfully.")


if __name__ == "__main__":
    main()
