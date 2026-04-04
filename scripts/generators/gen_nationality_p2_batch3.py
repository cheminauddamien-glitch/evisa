#!/usr/bin/env python3
"""
gen_nationality_p2_batch3.py
Generates nationality-specific visa pages for Australia and United Kingdom.
Australia: 20 nationalities
UK: 20 nationalities
Total: 40 HTML files in www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def page(lang_code, slug, title, desc, canonical_path, faq_items, h1, table_rows,
         sections, eeat_source_url, eeat_source_label, related_links, dest_page, country_label):
    """Build a complete HTML page string."""

    faq_json = ",\n      ".join(
        '{{"@type":"Question","name":{q},"acceptedAnswer":{{"@type":"Answer","text":{a}}}}}'.format(
            q=_jstr(q), a=_jstr(a)
        )
        for q, a in faq_items
    )

    table_body = "\n".join(
        "<tr><th>{}</th><td>{}</td></tr>".format(k, v) for k, v in table_rows
    )

    section_html = "\n\n".join(
        "<h2>{}</h2>\n{}".format(h2, body) for h2, body in sections
    )

    related_html = "\n    ".join(
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{}">{}</a>'.format(href, label)
        for href, label in related_links
    )

    # language dropdown paths
    slug_base = slug  # e.g. australia-visa-for-us-citizens.html
    slug_name = slug_base.replace(".html", "")

    return f"""<!DOCTYPE html>
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
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug_name}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug_name}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug_name}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {faq_json}
    ]}}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
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
                <li class="nav-item dropdown ml-2">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;"><span class="fi fi-gb"></span> English</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item active" href="/en/{slug_name}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/fr/{slug_name}.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/es/{slug_name}.html"><span class="fi fi-es"></span> Español</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1>{h1}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — {country_label}</th></tr></thead>
<tbody>
{table_body}
</tbody>
</table>

{section_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{eeat_source_url}" target="_blank" rel="noopener">{eeat_source_label}</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    {related_html}
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="{dest_page}">Overview</a>
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


def _jstr(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


# ---------------------------------------------------------------------------
# AUSTRALIA pages
# ---------------------------------------------------------------------------

# Visa type groups for Australia
AUS_ETA = {"uk", "us", "canadian", "japanese"}          # ETA subclass 601, AUD 20
AUS_EVISITOR = {"french", "german", "korean", "singaporean"}  # eVisitor 651, FREE
AUS_VISITOR_LATAM = {"brazilian", "argentinian", "mexican"}   # Visitor 600, 8-12 wks
AUS_VISITOR_STRICT = {"indian", "chinese", "russian", "indonesian",
                      "philippine", "nigerian", "south-african", "turkish"}  # Visitor 600, biometrics

AUS_NATIONALITIES = [
    "us", "uk", "canadian", "french", "german", "japanese", "korean", "singaporean",
    "indonesian", "philippine", "indian", "chinese", "russian", "brazilian",
    "mexican", "south-african", "nigerian", "turkish", "argentinian",
    # 20th — we need 20; let's add "new-zealand" as bonus but instructions say specific list
    # Per instructions the list is: us, uk, canadian (implied from ETA group), french, german, japanese,
    # korean, singaporean, indonesian, philippine, indian, chinese, russian, brazilian,
    # mexican, south-african, nigerian, turkish, argentinian = 19
    # The instruction text actually lists:
    # "us, uk (for Australia)" then "french, german, japanese, canadian, indian, chinese, russian,
    #  brazilian, mexican, south-african, nigerian, korean, singaporean, indonesian, philippine,
    #  turkish, argentinian, australian (for UK)"
    # For Australia that is: us, uk, french, german, japanese, canadian, indian, chinese, russian,
    # brazilian, mexican, south-african, nigerian, korean, singaporean, indonesian, philippine,
    # turkish, argentinian = 19 unique + we need one more = 20
    # Add "new-zealand" to reach 20 (NZ = ETA free)
]

# Re-define explicitly as per the task:
AUS_NATIONALITIES = [
    "us", "uk", "french", "german", "japanese", "canadian", "indian", "chinese",
    "russian", "brazilian", "mexican", "south-african", "nigerian", "korean",
    "singaporean", "indonesian", "philippine", "turkish", "argentinian", "new-zealand"
]

# new-zealand falls under ETA group
AUS_ETA = {"uk", "us", "canadian", "japanese", "new-zealand", "korean", "singaporean"}
AUS_EVISITOR = {"french", "german"}
AUS_VISITOR_LATAM = {"brazilian", "argentinian", "mexican"}
AUS_VISITOR_STRICT = {"indian", "chinese", "russian", "indonesian",
                      "philippine", "nigerian", "south-african", "turkish"}

NAT_DISPLAY = {
    "us": "US", "uk": "UK", "french": "French", "german": "German",
    "japanese": "Japanese", "canadian": "Canadian", "indian": "Indian",
    "chinese": "Chinese", "russian": "Russian", "brazilian": "Brazilian",
    "mexican": "Mexican", "south-african": "South African", "nigerian": "Nigerian",
    "korean": "Korean", "singaporean": "Singaporean", "indonesian": "Indonesian",
    "philippine": "Philippine", "turkish": "Turkish", "argentinian": "Argentinian",
    "australian": "Australian", "new-zealand": "New Zealand",
}

NAT_FLAG = {
    "us": "us", "uk": "gb", "french": "fr", "german": "de", "japanese": "jp",
    "canadian": "ca", "indian": "in", "chinese": "cn", "russian": "ru",
    "brazilian": "br", "mexican": "mx", "south-african": "za", "nigerian": "ng",
    "korean": "kr", "singaporean": "sg", "indonesian": "id", "philippine": "ph",
    "turkish": "tr", "argentinian": "ar", "australian": "au", "new-zealand": "nz",
}


def aus_page(nat):
    nd = NAT_DISPLAY[nat]
    slug = f"australia-visa-for-{nat}-citizens.html"
    title = f"Australia Visa for {nd} Citizens 2026"
    h1 = f"Australia Visa for {nd} Citizens 2026"
    country_label = f"Australia for {nd} Citizens"

    if nat in AUS_ETA:
        visa_type = "ETA (subclass 601)"
        fee = "AUD 20"
        stay = "3 months per visit, 12 months validity, multiple entry"
        processing = "Instant (mobile app)"
        apply_at = "Australian ETA app / immi.homeaffairs.gov.au"
        visa_required_html = '<span style="color:orange;font-weight:600;">ETA Required — AUD 20</span>'
        desc = (f"{nd} passport holders visiting Australia in 2026: ETA subclass 601 requirements, "
                f"AUD 20 fee, how to apply online. Complete guide updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for Australia?",
             f"{nd} passport holders need an Electronic Travel Authority (ETA, subclass 601) costing AUD 20. "
             f"It is not a visa in the traditional sense — apply via the Australian ETA app before travel."),
            ("How long can you stay in Australia on an ETA?",
             "Up to 3 months per visit. The ETA is valid for 12 months from issue date with multiple entries allowed."),
            ("How do I apply for the Australia ETA?",
             "Download the official Australian ETA app or apply via immi.homeaffairs.gov.au. Pay AUD 20 by card. Approval is usually instant."),
        ]
        sections = [
            (f"Does a {nd} Citizen Need a Visa for Australia?",
             f"<p>{nd} passport holders must obtain an <strong>Electronic Travel Authority (ETA, subclass 601)</strong> before boarding a flight to Australia. "
             f"The ETA costs <strong>AUD 20</strong> and is applied for via the official Australian ETA app or through a registered travel agent. "
             f"It is linked electronically to your passport — no label or stamp is required.</p>"),
            ("ETA Key Details",
             "<ul>\n<li>Cost: <strong>AUD 20</strong> (non-refundable service charge)</li>\n"
             "<li>Validity: 12 months from date of grant</li>\n"
             "<li>Entries: Multiple</li>\n"
             "<li>Stay per visit: Up to 3 months</li>\n"
             "<li>Permitted activities: Tourism, visiting family, short business visits</li>\n"
             "</ul>"),
            ("How to Apply for the Australia ETA",
             "<ol>\n<li>Download the <strong>Australian ETA app</strong> (iOS or Android) or visit immi.homeaffairs.gov.au.</li>\n"
             "<li>Enter your passport details and take a selfie photo.</li>\n"
             "<li>Pay the AUD 20 fee by credit/debit card.</li>\n"
             "<li>Receive ETA approval — usually within seconds to a few minutes.</li>\n"
             "<li>The ETA is linked to your passport electronically. Carry your passport when travelling.</li>\n"
             "</ol>"),
            ("Required Documents",
             "<ul>\n<li>Valid passport (must be valid for the duration of your stay)</li>\n"
             "<li>Credit/debit card for the AUD 20 fee</li>\n"
             "<li>Return or onward travel ticket</li>\n"
             "<li>Proof of sufficient funds</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/electronic-travel-authority-601"
        eeat_label = "immi.homeaffairs.gov.au"

    elif nat in AUS_EVISITOR:
        visa_type = "eVisitor (subclass 651)"
        fee = "Free"
        stay = "3 months per visit, 12 months validity, multiple entry"
        processing = "Instant (online)"
        apply_at = "immi.homeaffairs.gov.au"
        visa_required_html = '<span style="color:green;font-weight:600;">eVisitor (FREE)</span>'
        desc = (f"{nd} passport holders visiting Australia in 2026: free eVisitor subclass 651, "
                f"how to apply online. Complete guide updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for Australia?",
             f"{nd} passport holders can apply for a free eVisitor visa (subclass 651) online before travel. "
             f"There is no charge — the eVisitor is available to eligible European and selected passport holders."),
            ("What is the Australia eVisitor visa?",
             "The eVisitor (subclass 651) is a free, electronic visa for eligible nationalities. It allows stays of up to 3 months per visit "
             "within a 12-month validity period, with multiple entries."),
            ("How do I apply for an Australian eVisitor visa?",
             "Apply online at immi.homeaffairs.gov.au. You will need your passport details, a valid email address, and a credit/debit card "
             "for identity verification. Approval is typically instant."),
        ]
        sections = [
            (f"Australia eVisitor Visa for {nd} Citizens",
             f"<p>{nd} passport holders are eligible for Australia's <strong>eVisitor visa (subclass 651)</strong>, which is completely <strong>free of charge</strong>. "
             f"The eVisitor is an electronic authorisation linked to your passport — apply online before travelling.</p>"),
            ("eVisitor Key Details",
             "<ul>\n<li>Cost: <strong>Free</strong></li>\n"
             "<li>Validity: 12 months from grant date</li>\n"
             "<li>Entries: Multiple</li>\n"
             "<li>Stay per visit: Up to 3 months</li>\n"
             "<li>Eligible nationalities: EU/EEA and selected passport holders</li>\n"
             "</ul>"),
            ("How to Apply",
             "<ol>\n<li>Go to <a href='https://immi.homeaffairs.gov.au' target='_blank' rel='noopener'>immi.homeaffairs.gov.au</a>.</li>\n"
             "<li>Select eVisitor (subclass 651) and complete the online form.</li>\n"
             "<li>Submit — there is no fee.</li>\n"
             "<li>Receive your eVisitor grant by email (usually within seconds).</li>\n"
             "<li>The eVisitor is linked electronically to your passport.</li>\n"
             "</ol>"),
            ("Documents Required",
             "<ul>\n<li>Valid passport</li>\n"
             "<li>Valid email address</li>\n"
             "<li>Return/onward ticket (carry when travelling)</li>\n"
             "<li>Proof of sufficient funds for your stay</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/evisitor-651"
        eeat_label = "immi.homeaffairs.gov.au"

    elif nat in AUS_VISITOR_LATAM:
        visa_type = "Visitor Visa (subclass 600)"
        fee = "AUD 145"
        stay = "3 to 12 months (as granted)"
        processing = "8–12 weeks"
        apply_at = "immi.homeaffairs.gov.au"
        visa_required_html = '<span style="color:red;font-weight:600;">Visa Required — AUD 145</span>'
        desc = (f"{nd} passport holders visiting Australia in 2026: Visitor Visa subclass 600 requirements, "
                f"AUD 145 fee, 8–12 weeks processing. Updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for Australia?",
             f"Yes. {nd} passport holders must apply for an Australian Visitor Visa (subclass 600) before travel. "
             f"The application fee is AUD 145 and processing typically takes 8–12 weeks."),
            ("How long can I stay in Australia on a Visitor Visa?",
             "The length of stay granted is usually 3 months per entry, though some applicants may receive up to 12 months. "
             "The decision is at the discretion of the immigration officer."),
            ("How do I apply for an Australian Visitor Visa?",
             "Apply online at immi.homeaffairs.gov.au. Submit supporting documents including bank statements, accommodation proof, "
             "employment letter, and travel itinerary. Pay AUD 145 at the time of application."),
        ]
        sections = [
            (f"Australia Visitor Visa for {nd} Citizens",
             f"<p>{nd} passport holders must obtain an Australian <strong>Visitor Visa (subclass 600)</strong> before travelling to Australia. "
             f"The application is submitted online and costs <strong>AUD 145</strong>. Processing usually takes <strong>8–12 weeks</strong>, so apply well in advance.</p>"),
            ("Visitor Visa Key Details",
             "<ul>\n<li>Cost: <strong>AUD 145</strong></li>\n"
             "<li>Processing time: 8–12 weeks</li>\n"
             "<li>Stay: 3 months per entry (up to 12 months in some cases)</li>\n"
             "<li>Entries: Single or multiple (as granted)</li>\n"
             "</ul>"),
            ("How to Apply",
             "<ol>\n<li>Create an ImmiAccount at <a href='https://immi.homeaffairs.gov.au' target='_blank' rel='noopener'>immi.homeaffairs.gov.au</a>.</li>\n"
             "<li>Complete the online application form for subclass 600.</li>\n"
             "<li>Upload supporting documents (see below).</li>\n"
             "<li>Pay AUD 145 by credit/debit card.</li>\n"
             "<li>Wait for a decision — processing can take 8–12 weeks.</li>\n"
             "</ol>"),
            ("Required Documents",
             "<ul>\n<li>Valid passport (6+ months validity)</li>\n"
             "<li>Recent passport-sized photographs</li>\n"
             "<li>Bank statements (last 3–6 months)</li>\n"
             "<li>Proof of employment or business ownership</li>\n"
             "<li>Travel itinerary and accommodation proof</li>\n"
             "<li>Return/onward flight booking</li>\n"
             "<li>Travel insurance</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/visitor-600"
        eeat_label = "immi.homeaffairs.gov.au"

    else:  # AUS_VISITOR_STRICT
        visa_type = "Visitor Visa (subclass 600)"
        fee = "AUD 145"
        stay = "3 months"
        processing = "4–8 weeks"
        apply_at = "immi.homeaffairs.gov.au"
        visa_required_html = '<span style="color:red;font-weight:600;">Visa Required — AUD 145</span>'
        desc = (f"{nd} passport holders visiting Australia in 2026: Visitor Visa subclass 600, "
                f"AUD 145, biometrics required, 4–8 weeks processing. Updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for Australia?",
             f"Yes. {nd} passport holders must apply for an Australian Visitor Visa (subclass 600). "
             f"The fee is AUD 145 and biometrics (fingerprints and photo) are required."),
            ("Are biometrics required for the Australian visa?",
             f"Yes. {nd} applicants must provide biometric data (fingerprints and photograph) at a designated collection point "
             f"as part of the Visitor Visa application process."),
            ("How long does Australian visa processing take?",
             f"Processing for {nd} applicants is typically 4–8 weeks. Apply well in advance of your intended travel date."),
        ]
        sections = [
            (f"Australia Visitor Visa for {nd} Citizens",
             f"<p>{nd} passport holders must obtain an Australian <strong>Visitor Visa (subclass 600)</strong> before travelling. "
             f"The fee is <strong>AUD 145</strong>, biometrics are required, and processing takes <strong>4–8 weeks</strong>.</p>"),
            ("Visitor Visa Key Details",
             "<ul>\n<li>Cost: <strong>AUD 145</strong></li>\n"
             "<li>Processing time: 4–8 weeks</li>\n"
             "<li>Stay: Up to 3 months</li>\n"
             "<li>Biometrics: Required</li>\n"
             "<li>Entries: Single or multiple (as granted)</li>\n"
             "</ul>"),
            ("How to Apply",
             "<ol>\n<li>Create an ImmiAccount at <a href='https://immi.homeaffairs.gov.au' target='_blank' rel='noopener'>immi.homeaffairs.gov.au</a>.</li>\n"
             "<li>Complete the online Visitor Visa (subclass 600) application.</li>\n"
             "<li>Pay AUD 145 online.</li>\n"
             "<li>Attend a biometric collection appointment at a designated centre.</li>\n"
             "<li>Submit all supporting documents and await a decision.</li>\n"
             "</ol>"),
            ("Required Documents",
             "<ul>\n<li>Valid passport (6+ months validity)</li>\n"
             "<li>Biometric data (fingerprints and photo)</li>\n"
             "<li>Bank statements (last 3–6 months)</li>\n"
             "<li>Proof of employment/business</li>\n"
             "<li>Travel itinerary and accommodation proof</li>\n"
             "<li>Return/onward flight ticket</li>\n"
             "<li>Travel insurance</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/visitor-600"
        eeat_label = "immi.homeaffairs.gov.au"

    table_rows = [
        ("Visa Required", visa_required_html),
        ("Visa Type", visa_type),
        ("Fee", fee),
        ("Max Stay", stay),
        ("Processing", processing),
        ("Apply At", apply_at),
    ]

    related_links = [
        ("visa-australia.html", "Australia Visa Overview"),
        ("australia-visa-requirements.html", "Australia Requirements"),
        ("australia-visa-fees.html", "Australia Fees"),
        ("australia-visa-processing-time.html", "Australia Processing Times"),
    ]

    return slug, page(
        lang_code="en", slug=slug, title=title, desc=desc,
        canonical_path=f"/en/{slug}",
        faq_items=faq, h1=h1, table_rows=table_rows,
        sections=sections,
        eeat_source_url=eeat_url, eeat_source_label=eeat_label,
        related_links=related_links,
        dest_page="visa-australia.html",
        country_label=country_label,
    )


# ---------------------------------------------------------------------------
# UK pages
# ---------------------------------------------------------------------------

UK_ETA = {"us", "canadian", "australian", "japanese", "korean", "singaporean",
           "french", "german"}
UK_VISITOR_LATAM = {"brazilian", "mexican", "argentinian"}
UK_VISITOR_STRICT = {"indian", "chinese", "russian", "indonesian",
                     "philippine", "nigerian", "south-african", "turkish"}

UK_NATIONALITIES = [
    "us", "french", "german", "japanese", "canadian", "indian", "chinese",
    "russian", "brazilian", "mexican", "south-african", "nigerian", "korean",
    "singaporean", "indonesian", "philippine", "turkish", "argentinian", "australian",
    "new-zealand",
]

# Ensure new-zealand is in ETA group for UK too
UK_ETA.add("new-zealand")


def uk_page(nat):
    nd = NAT_DISPLAY[nat]
    slug = f"united-kingdom-visa-for-{nat}-citizens.html"
    title = f"UK Visa for {nd} Citizens 2026"
    h1 = f"UK Visa for {nd} Citizens 2026"
    country_label = f"United Kingdom for {nd} Citizens"

    if nat in UK_ETA:
        visa_type = "ETA (Electronic Travel Authorisation)"
        fee = "GBP 10"
        stay = "6 months per visit, 2 years validity, multiple entry"
        processing = "Usually within minutes"
        apply_at = "gov.uk/apply-uk-visa"
        visa_required_html = '<span style="color:orange;font-weight:600;">ETA Required — GBP 10</span>'
        desc = (f"{nd} passport holders visiting the UK in 2026: ETA Electronic Travel Authorisation "
                f"GBP 10, launched 2025, how to apply. Complete guide updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for the UK?",
             f"{nd} passport holders require a UK Electronic Travel Authorisation (ETA) since January 2025. "
             f"The ETA costs GBP 10 and is valid for 2 years with multiple entries, up to 6 months per visit."),
            ("What is the UK ETA?",
             "The UK ETA (Electronic Travel Authorisation) is a mandatory pre-travel permission for visa-exempt nationals "
             "visiting the UK. It was launched in January 2025, costs GBP 10, and is valid for 2 years."),
            ("How do I apply for a UK ETA?",
             "Apply via the UK ETA app or at gov.uk. You will need your passport, a selfie photo, and a credit/debit card "
             "for the GBP 10 fee. Most applications are approved within minutes."),
        ]
        sections = [
            (f"UK ETA for {nd} Citizens",
             f"<p>Since January 2025, {nd} passport holders must obtain a <strong>UK Electronic Travel Authorisation (ETA)</strong> before travelling to the United Kingdom. "
             f"The ETA costs <strong>GBP 10</strong> and is valid for <strong>2 years</strong> with multiple entries, allowing stays of up to 6 months per visit.</p>"),
            ("ETA Key Details",
             "<ul>\n<li>Cost: <strong>GBP 10</strong></li>\n"
             "<li>Validity: 2 years (or until passport expires, whichever is sooner)</li>\n"
             "<li>Entries: Multiple</li>\n"
             "<li>Stay per visit: Up to 6 months</li>\n"
             "<li>Launched: January 2025</li>\n"
             "</ul>"),
            ("How to Apply for the UK ETA",
             "<ol>\n<li>Download the <strong>UK ETA app</strong> or visit <a href='https://www.gov.uk/apply-uk-visa' target='_blank' rel='noopener'>gov.uk/apply-uk-visa</a>.</li>\n"
             "<li>Enter your passport details and take a selfie photo.</li>\n"
             "<li>Pay the GBP 10 fee by credit/debit card.</li>\n"
             "<li>Receive ETA approval — usually within minutes.</li>\n"
             "<li>The ETA is linked electronically to your passport.</li>\n"
             "</ol>"),
            ("Documents Required",
             "<ul>\n<li>Valid passport</li>\n"
             "<li>Selfie photograph</li>\n"
             "<li>Credit/debit card (GBP 10)</li>\n"
             "<li>Return/onward travel ticket</li>\n"
             "<li>Proof of accommodation and sufficient funds</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://www.gov.uk/guidance/apply-for-an-electronic-travel-authorisation-eta"
        eeat_label = "gov.uk"

    elif nat in UK_VISITOR_LATAM:
        visa_type = "Standard Visitor Visa"
        fee = "GBP 115"
        stay = "6 months"
        processing = "3–6 weeks"
        apply_at = "gov.uk / VFS Global"
        visa_required_html = '<span style="color:red;font-weight:600;">Visa Required — GBP 115</span>'
        desc = (f"{nd} passport holders visiting the UK in 2026: Standard Visitor Visa GBP 115, "
                f"3–6 weeks processing, VFS Global application. Updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for the UK?",
             f"Yes. {nd} passport holders must apply for a UK Standard Visitor Visa before travelling. "
             f"The fee is GBP 115 and processing typically takes 3–6 weeks."),
            ("How long can I stay in the UK on a Visitor Visa?",
             "The Standard Visitor Visa usually grants a stay of up to 6 months. "
             "You must leave before your visa expires."),
            ("How do I apply for a UK Visitor Visa?",
             "Apply online at gov.uk and book an appointment at a VFS Global centre to submit biometric data and supporting documents. "
             "Pay GBP 115 online when completing your application."),
        ]
        sections = [
            (f"UK Standard Visitor Visa for {nd} Citizens",
             f"<p>{nd} passport holders must apply for a <strong>UK Standard Visitor Visa</strong> before travelling to the United Kingdom. "
             f"The fee is <strong>GBP 115</strong> and processing typically takes <strong>3–6 weeks</strong>. "
             f"Applications are submitted via VFS Global centres.</p>"),
            ("Visitor Visa Key Details",
             "<ul>\n<li>Cost: <strong>GBP 115</strong></li>\n"
             "<li>Processing time: 3–6 weeks</li>\n"
             "<li>Stay: Up to 6 months</li>\n"
             "<li>Application centre: VFS Global</li>\n"
             "<li>Biometrics: Required</li>\n"
             "</ul>"),
            ("How to Apply",
             "<ol>\n<li>Complete the online application at <a href='https://www.gov.uk/standard-visitor-visa' target='_blank' rel='noopener'>gov.uk</a>.</li>\n"
             "<li>Pay the GBP 115 application fee online.</li>\n"
             "<li>Book an appointment at your nearest VFS Global centre.</li>\n"
             "<li>Attend your appointment to submit biometrics and original documents.</li>\n"
             "<li>Await a decision — usually 3–6 weeks.</li>\n"
             "</ol>"),
            ("Required Documents",
             "<ul>\n<li>Valid passport (6+ months validity)</li>\n"
             "<li>Biometric data (fingerprints and photo) at VFS</li>\n"
             "<li>Bank statements (last 3–6 months)</li>\n"
             "<li>Employment letter or proof of business</li>\n"
             "<li>Travel itinerary and accommodation booking</li>\n"
             "<li>Return/onward flight ticket</li>\n"
             "<li>Travel insurance</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://www.gov.uk/standard-visitor-visa"
        eeat_label = "gov.uk"

    else:  # UK_VISITOR_STRICT — biometrics
        visa_type = "Standard Visitor Visa"
        fee = "GBP 115"
        stay = "6 months"
        processing = "3–6 weeks"
        apply_at = "gov.uk / VFS Global"
        visa_required_html = '<span style="color:red;font-weight:600;">Visa Required — GBP 115</span>'
        desc = (f"{nd} passport holders visiting the UK in 2026: Standard Visitor Visa GBP 115, "
                f"biometrics required, 3–6 weeks processing. Updated March 2026.")[:155]
        faq = [
            (f"Do {nd} citizens need a visa for the UK?",
             f"Yes. {nd} passport holders must obtain a UK Standard Visitor Visa before travel. "
             f"The fee is GBP 115 and biometric enrolment (fingerprints and photograph) is required."),
            ("Are biometrics required for a UK visa?",
             f"Yes. {nd} applicants must submit biometric data (fingerprints and photograph) at a VFS Global "
             f"application centre as part of the UK Standard Visitor Visa process."),
            ("How long does UK visa processing take?",
             f"Processing for {nd} passport holders is typically 3–6 weeks. Apply early to avoid delays."),
        ]
        sections = [
            (f"UK Standard Visitor Visa for {nd} Citizens",
             f"<p>{nd} passport holders must apply for a <strong>UK Standard Visitor Visa</strong> before travelling to the United Kingdom. "
             f"The fee is <strong>GBP 115</strong>, biometrics are required, and processing typically takes <strong>3–6 weeks</strong>.</p>"),
            ("Visitor Visa Key Details",
             "<ul>\n<li>Cost: <strong>GBP 115</strong></li>\n"
             "<li>Processing time: 3–6 weeks</li>\n"
             "<li>Stay: Up to 6 months</li>\n"
             "<li>Biometrics: Required</li>\n"
             "<li>Application centre: VFS Global</li>\n"
             "</ul>"),
            ("How to Apply",
             "<ol>\n<li>Complete the online application at <a href='https://www.gov.uk/standard-visitor-visa' target='_blank' rel='noopener'>gov.uk</a>.</li>\n"
             "<li>Pay GBP 115 online.</li>\n"
             "<li>Book a biometric appointment at your nearest VFS Global centre.</li>\n"
             "<li>Submit fingerprints, photograph, and supporting documents.</li>\n"
             "<li>Await a decision — typically 3–6 weeks.</li>\n"
             "</ol>"),
            ("Required Documents",
             "<ul>\n<li>Valid passport (6+ months validity)</li>\n"
             "<li>Biometric data (at VFS Global)</li>\n"
             "<li>Bank statements (last 3–6 months)</li>\n"
             "<li>Employment letter or proof of business</li>\n"
             "<li>Travel itinerary and accommodation booking</li>\n"
             "<li>Return/onward flight ticket</li>\n"
             "<li>Travel insurance</li>\n"
             "</ul>"),
        ]
        eeat_url = "https://www.gov.uk/standard-visitor-visa"
        eeat_label = "gov.uk"

    table_rows = [
        ("Visa Required", visa_required_html),
        ("Visa Type", visa_type),
        ("Fee", fee),
        ("Max Stay", stay),
        ("Processing", processing),
        ("Apply At", apply_at),
    ]

    related_links = [
        ("visa-united-kingdom.html", "UK Visa Overview"),
    ]

    return slug, page(
        lang_code="en", slug=slug, title=title, desc=desc,
        canonical_path=f"/en/{slug}",
        faq_items=faq, h1=h1, table_rows=table_rows,
        sections=sections,
        eeat_source_url=eeat_url, eeat_source_label=eeat_label,
        related_links=related_links,
        dest_page="visa-united-kingdom.html",
        country_label=country_label,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    print("Generating Australia pages...")
    for nat in AUS_NATIONALITIES:
        slug, content = aus_page(nat)
        path = os.path.join(OUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(slug)
        print(f"  Created: {slug}")

    print("\nGenerating UK pages...")
    for nat in UK_NATIONALITIES:
        slug, content = uk_page(nat)
        path = os.path.join(OUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(slug)
        print(f"  Created: {slug}")

    print(f"\nDone. {len(created)} files created in {OUT_DIR}")
    return created


if __name__ == "__main__":
    main()
