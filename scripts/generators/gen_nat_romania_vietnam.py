"""
gen_nat_romania_vietnam.py
Generates 40 HTML files in www/en/:
  romania-visa-for-{nat}-citizens.html  (20 files)
  vietnam-visa-for-{nat}-citizens.html  (20 files)
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------
NATIONALITIES = [
    # slug           label            flag  demonym
    ("us",           "US",            "us", "US"),
    ("uk",           "UK",            "gb", "UK"),
    ("canadian",     "Canadian",      "ca", "Canadian"),
    ("french",       "French",        "fr", "French"),
    ("german",       "German",        "de", "German"),
    ("japanese",     "Japanese",      "jp", "Japanese"),
    ("australian",   "Australian",    "au", "Australian"),
    ("indian",       "Indian",        "in", "Indian"),
    ("chinese",      "Chinese",       "cn", "Chinese"),
    ("russian",      "Russian",       "ru", "Russian"),
    ("brazilian",    "Brazilian",     "br", "Brazilian"),
    ("mexican",      "Mexican",       "mx", "Mexican"),
    ("south-african","South African", "za", "South African"),
    ("nigerian",     "Nigerian",      "ng", "Nigerian"),
    ("korean",       "Korean",        "kr", "Korean"),
    ("singaporean",  "Singaporean",   "sg", "Singaporean"),
    ("indonesian",   "Indonesian",    "id", "Indonesian"),
    ("philippine",   "Philippine",    "ph", "Philippine"),
    ("turkish",      "Turkish",       "tr", "Turkish"),
    ("argentinian",  "Argentinian",   "ar", "Argentinian"),
]

# ---------------------------------------------------------------------------
# Romania visa status
# EU free movement (no visa, no limit): french, german
# Visa-free 90/180 days: us uk canadian japanese australian korean singaporean
#                        brazilian mexican argentinian
# Visa required EUR 65 (mae.ro): indian chinese russian indonesian philippine
#                                nigerian south-african turkish
# ---------------------------------------------------------------------------
ROMANIA_EU_FREE = {"french", "german"}
ROMANIA_VISA_FREE = {
    "us", "uk", "canadian", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian",
}
ROMANIA_VISA_REQUIRED = {
    "indian", "chinese", "russian", "indonesian",
    "philippine", "nigerian", "south-african", "turkish",
}

# ---------------------------------------------------------------------------
# Vietnam visa status
# Visa-free 45 days (EU15 agreement): french, german, uk
# Visa-free 30 days: japanese, korean, singaporean
# eVisa USD 25 (90 days, 3 business days): everyone else
# ---------------------------------------------------------------------------
VIETNAM_FREE_45 = {"french", "german", "uk"}
VIETNAM_FREE_30 = {"japanese", "korean", "singaporean"}
VIETNAM_EVISA = {
    "us", "canadian", "australian", "indian", "chinese", "russian",
    "brazilian", "mexican", "south-african", "nigerian", "indonesian",
    "philippine", "turkish", "argentinian",
}


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------
def head(title, description, canonical_slug, schema_json):
    return f"""<!DOCTYPE html>
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
    <link rel="canonical" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canonical_slug}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <script type="application/ld+json">
    {schema_json}
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


def navbar(current_slug):
    return f"""
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
                        <a class="dropdown-item active" href="/en/{current_slug}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""


def footer_scripts():
    return """
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


# ---------------------------------------------------------------------------
# Romania page generator
# ---------------------------------------------------------------------------
def romania_page(slug, label, flag, demonym):
    dest_flag = "ro"
    page_slug = f"romania-visa-for-{slug}-citizens"
    title = f"Romania Visa for {label} Citizens 2026"

    if slug in ROMANIA_EU_FREE:
        status_badge = '<span style="color:green;font-weight:600;">EU Free Movement — No Visa Required</span>'
        status_row = "EU Free Movement"
        meta_desc = (
            f"{label} passport holders enjoy free movement in Romania under EU rules. "
            f"No visa or entry permit required. Updated March 2026."
        )
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Romania for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Status</th><td>EU Free Movement</td></tr>
<tr><th>Max Stay</th><td>Unlimited (right of residence)</td></tr>
<tr><th>Entry</th><td>Valid national ID or passport</td></tr>
<tr><th>Apply At</th><td>N/A</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Romania Entry for {label} Citizens</h2>
<p>{demonym} nationals are EU citizens and enjoy <strong>free movement</strong> throughout Romania under EU Treaty rights. No visa, stamp, or prior authorisation is required.</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid national ID card <strong>or</strong> passport</li>
<li>No minimum validity period specified, but carry a document valid for the duration of your stay</li>
<li>No advance visa application needed</li>
</ul>
<h2>Longer Stays &amp; Residence</h2>
<p>For stays beyond 3 months, {demonym} nationals may register with local Romanian authorities, though this is generally a formality rather than a strict requirement.</p>"""
        faqs = [
            (f"Do {label} citizens need a visa for Romania?",
             f"No. {demonym} citizens benefit from EU free movement and may enter Romania without a visa using a valid national ID or passport."),
            ("Is Romania in the Schengen Area?",
             "Romania joined the Schengen Area for air and sea borders in March 2024, with land border integration continuing. EU citizens are unaffected either way."),
            (f"How long can {label} citizens stay in Romania?",
             f"As EU nationals, {demonym} citizens have the right to reside in Romania indefinitely, subject to registration formalities for stays over 3 months."),
        ]

    elif slug in ROMANIA_VISA_FREE:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 90 days / 180-day period</span>'
        meta_desc = (
            f"{label} passport holders can visit Romania visa-free for up to 90 days in any 180-day period. "
            f"No visa required. Updated March 2026."
        )
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Romania for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Max Stay</th><td>90 days / 180-day period</td></tr>
<tr><th>Purpose</th><td>Tourism, business, transit</td></tr>
<tr><th>Entry</th><td>Valid passport</td></tr>
<tr><th>Apply At</th><td>N/A — visa-free entry</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Visa-Free Entry to Romania for {label} Citizens</h2>
<p>{demonym} passport holders may enter Romania <strong>without a visa</strong> for up to <strong>90 days</strong> within any 180-day period for tourism, business, or transit.</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (recommended 6+ months validity beyond stay)</li>
<li>Proof of sufficient funds</li>
<li>Return or onward ticket</li>
<li>Accommodation proof (hotel booking or invitation letter)</li>
<li>Travel insurance (recommended)</li>
</ul>
<h2>Schengen &amp; Romania Note</h2>
<p>Romania joined the Schengen Area for air and sea borders in March 2024. For land crossings, check current border arrangements before travel. The 90/180-day visa-free rule applies to Romania separately from the Schengen Area calculation where applicable.</p>"""
        faqs = [
            (f"Do {label} citizens need a visa for Romania?",
             f"No. {demonym} passport holders can enter Romania visa-free for up to 90 days in any 180-day period."),
            ("Is Romania in Schengen?",
             "Romania joined Schengen for air and sea travel in March 2024. Land border integration is ongoing. Check current rules before travel."),
            (f"Can {label} citizens extend their stay in Romania?",
             f"{demonym} visitors on visa-free entry cannot extend beyond 90 days. For longer stays, a long-stay visa must be applied for before entry."),
        ]

    else:  # visa required
        status_badge = '<span style="color:red;font-weight:600;">Visa Required — EUR 65</span>'
        meta_desc = (
            f"{label} passport holders need a Romanian visa to visit Romania. "
            f"Fee EUR 65, apply at mae.ro. Updated March 2026."
        )
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Romania for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>Short-stay visa (C) or Long-stay visa (D)</td></tr>
<tr><th>Fee</th><td>EUR 65</td></tr>
<tr><th>Max Stay</th><td>90 days / 180-day period (short-stay)</td></tr>
<tr><th>Processing</th><td>10–30 business days</td></tr>
<tr><th>Apply At</th><td>mae.ro (Romanian Embassy)</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Romania Visa for {label} Citizens</h2>
<p>{demonym} passport holders must obtain a Romanian visa before travelling. The standard short-stay visa (type C) costs <strong>EUR 65</strong> and allows stays of up to <strong>90 days</strong> within a 180-day period.</p>
<h2>Visa Types</h2>
<ul>
<li><strong>Type C (Short-Stay)</strong>: Tourism, business, transit — up to 90 days / 180-day period</li>
<li><strong>Type D (Long-Stay)</strong>: Study, work, family reunification — over 90 days</li>
</ul>
<h2>How to Apply</h2>
<ol>
<li>Locate the nearest Romanian Embassy or Consulate.</li>
<li>Complete the online application form at <a href="https://evisa.mae.ro" target="_blank" rel="noopener">evisa.mae.ro</a>.</li>
<li>Pay the visa fee of EUR 65.</li>
<li>Submit required documents and attend an interview if requested.</li>
<li>Wait 10–30 business days for processing.</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid passport (6+ months validity, at least 2 blank pages)</li>
<li>Completed visa application form</li>
<li>Recent passport-size photographs (35×45 mm, white background)</li>
<li>Travel insurance (min EUR 30,000 coverage)</li>
<li>Proof of accommodation (hotel reservation or invitation)</li>
<li>Return/onward flight ticket</li>
<li>Proof of sufficient funds (bank statements, last 3 months)</li>
<li>Proof of purpose (employment letter, business invitation, etc.)</li>
</ul>"""
        faqs = [
            (f"Do {label} citizens need a visa for Romania?",
             f"Yes. {demonym} passport holders must apply for a Romanian visa at the nearest Romanian Embassy. The fee is EUR 65."),
            ("Where do I apply for a Romanian visa?",
             "Apply at your nearest Romanian Embassy or Consulate, or via the online portal at evisa.mae.ro. Processing takes 10–30 business days."),
            ("What is the Romanian visa fee?",
             "The standard short-stay visa (type C) fee is EUR 65. Fees may vary by country of application."),
        ]

    faq_schema = [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in faqs
    ]
    import json
    schema = json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema},
        ensure_ascii=False
    )

    faq_html = "\n".join(
        f"<h3>{q}</h3>\n<p>{a}</p>"
        for q, a in faqs
    )

    html = f"""{head(title, meta_desc, page_slug, schema)}
{navbar(page_slug)}
<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{dest_flag}" style="margin-right:8px;"></span>Romania Visa for <span class="fi fi-{flag}" style="margin-right:4px;"></span>{label} Citizens 2026</h1>

{key_table}

{body_content}

<h2>Frequently Asked Questions</h2>
{faq_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://evisa.mae.ro" target="_blank" rel="noopener">mae.ro</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-romania.html">Romania Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="romania-visa-requirements.html">Romania Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="romania-visa-fees.html">Romania Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="romania-visa-processing-time.html">Romania Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>
{footer_scripts()}"""
    return html


# ---------------------------------------------------------------------------
# Vietnam page generator
# ---------------------------------------------------------------------------
def vietnam_page(slug, label, flag, demonym):
    dest_flag = "vn"
    page_slug = f"vietnam-visa-for-{slug}-citizens"
    title = f"Vietnam Visa for {label} Citizens 2026"

    if slug in VIETNAM_FREE_45:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 45 days</span>'
        meta_desc = (
            f"{label} passport holders can visit Vietnam visa-free for up to 45 days under the EU15 agreement. "
            f"No eVisa needed. Updated March 2026."
        )
        stay = "45 days"
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Vietnam for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Max Stay</th><td>45 days per entry</td></tr>
<tr><th>Agreement</th><td>EU15 Visa-Free Agreement</td></tr>
<tr><th>Entries</th><td>Single or multiple (depending on your passport)</td></tr>
<tr><th>Apply At</th><td>N/A — visa-free entry</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Visa-Free Entry to Vietnam for {label} Citizens</h2>
<p>{demonym} passport holders benefit from a bilateral visa-free agreement allowing stays of up to <strong>45 days</strong> per entry without any visa or eVisa application.</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (6+ months validity recommended)</li>
<li>Return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details (hotel booking or host invitation)</li>
</ul>
<h2>Extending Your Stay</h2>
<p>If you wish to stay longer than 45 days, you must apply for a Vietnam eVisa (USD 25, 90-day stay) <em>before</em> your current permission expires, or exit and re-enter Vietnam.</p>"""
        faqs = [
            (f"Do {label} citizens need a visa for Vietnam?",
             f"No. {demonym} passport holders can enter Vietnam visa-free for up to 45 days under the EU15 agreement."),
            (f"Can {label} citizens get a Vietnam eVisa?",
             f"Yes, but it is not required for stays up to 45 days. For longer stays, apply for a 90-day eVisa at evisa.xuatnhapcanh.gov.vn for USD 25."),
            ("What are the entry requirements for Vietnam?",
             "A valid passport with at least 6 months validity, a return ticket, and proof of accommodation are the main requirements for visa-free entry."),
        ]

    elif slug in VIETNAM_FREE_30:
        status_badge = '<span style="color:green;font-weight:600;">Visa-Free — 30 days</span>'
        meta_desc = (
            f"{label} passport holders can visit Vietnam visa-free for up to 30 days. "
            f"No eVisa required. Updated March 2026."
        )
        stay = "30 days"
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Vietnam for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Max Stay</th><td>30 days per entry</td></tr>
<tr><th>Agreement</th><td>Bilateral visa-free agreement</td></tr>
<tr><th>Entries</th><td>Single (multiple possible with advance arrangement)</td></tr>
<tr><th>Apply At</th><td>N/A — visa-free entry</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Visa-Free Entry to Vietnam for {label} Citizens</h2>
<p>{demonym} passport holders may enter Vietnam <strong>without a visa</strong> for up to <strong>30 days</strong> per visit under a bilateral visa-free agreement.</p>
<h2>Entry Requirements</h2>
<ul>
<li>Valid passport (6+ months validity recommended)</li>
<li>Return or onward ticket</li>
<li>Proof of sufficient funds</li>
<li>Hotel booking or host invitation</li>
</ul>
<h2>Staying Longer Than 30 Days</h2>
<p>To stay beyond 30 days, apply for a <strong>Vietnam eVisa</strong> (90 days, USD 25) at <a href="https://evisa.xuatnhapcanh.gov.vn" target="_blank" rel="noopener">evisa.xuatnhapcanh.gov.vn</a> before arrival.</p>"""
        faqs = [
            (f"Do {label} citizens need a visa for Vietnam?",
             f"No. {demonym} passport holders can enter Vietnam visa-free for up to 30 days per visit."),
            ("What if I want to stay longer than 30 days?",
             "Apply for a Vietnam eVisa (USD 25, valid 90 days) at evisa.xuatnhapcanh.gov.vn. Processing takes approximately 3 business days."),
            ("Can I enter Vietnam multiple times on the visa-free arrangement?",
             "Typically single-entry per visa-free period. For multiple entries or extended stays, a Vietnam eVisa is recommended."),
        ]

    else:  # eVisa required
        status_badge = '<span style="color:orange;font-weight:600;">eVisa Required — USD 25 (90 days)</span>'
        meta_desc = (
            f"{label} passport holders need a Vietnam eVisa (USD 25, 90 days). "
            f"Apply online at evisa.xuatnhapcanh.gov.vn, 3 business days. Updated March 2026."
        )
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Vietnam for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_badge}</td></tr>
<tr><th>Visa Type</th><td>eVisa (Electronic Visa)</td></tr>
<tr><th>Fee</th><td>USD 25</td></tr>
<tr><th>Max Stay</th><td>90 days</td></tr>
<tr><th>Processing</th><td>~3 business days</td></tr>
<tr><th>Apply At</th><td>evisa.xuatnhapcanh.gov.vn</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Vietnam eVisa for {label} Citizens</h2>
<p>{demonym} passport holders must obtain a <strong>Vietnam eVisa</strong> before travelling. The eVisa costs <strong>USD 25</strong>, allows a stay of up to <strong>90 days</strong>, and is processed online in approximately <strong>3 business days</strong>.</p>
<h2>eVisa Key Details</h2>
<ul>
<li>Cost: <strong>USD 25</strong></li>
<li>Validity: 90 days from date of entry</li>
<li>Processing time: ~3 business days</li>
<li>Single or multiple entry (selected at application)</li>
<li>Apply entirely online — no embassy visit required</li>
</ul>
<h2>How to Apply</h2>
<ol>
<li>Visit the official portal: <a href="https://evisa.xuatnhapcanh.gov.vn" target="_blank" rel="noopener">evisa.xuatnhapcanh.gov.vn</a>.</li>
<li>Complete the online application form with passport details and travel information.</li>
<li>Upload a passport photo and passport biographical page scan.</li>
<li>Pay the USD 25 fee by credit/debit card.</li>
<li>Receive your eVisa by email within ~3 business days.</li>
<li>Print the eVisa and present it alongside your passport at the port of entry.</li>
</ol>
<h2>Required Documents</h2>
<ul>
<li>Valid passport (6+ months validity, at least 2 blank pages)</li>
<li>Digital passport-size photo (white background)</li>
<li>Scan of passport biographical page</li>
<li>Credit or debit card for USD 25 payment</li>
<li>Travel itinerary and accommodation details</li>
</ul>"""
        faqs = [
            (f"Do {label} citizens need a visa for Vietnam?",
             f"Yes. {demonym} passport holders must apply for a Vietnam eVisa (USD 25, 90 days) at evisa.xuatnhapcanh.gov.vn before travelling."),
            ("How long does the Vietnam eVisa take?",
             "Processing takes approximately 3 business days. Apply at least 5–7 days before your intended travel date."),
            ("Can I get a Vietnam eVisa on arrival?",
             "The official eVisa must be applied for online before arrival at evisa.xuatnhapcanh.gov.vn. Visa-on-arrival options exist but require prior approval letters; the eVisa is the easiest route."),
        ]

    faq_schema = [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in faqs
    ]
    import json
    schema = json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema},
        ensure_ascii=False
    )

    faq_html = "\n".join(
        f"<h3>{q}</h3>\n<p>{a}</p>"
        for q, a in faqs
    )

    html = f"""{head(title, meta_desc, page_slug, schema)}
{navbar(page_slug)}
<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{dest_flag}" style="margin-right:8px;"></span>Vietnam Visa for <span class="fi fi-{flag}" style="margin-right:4px;"></span>{label} Citizens 2026</h1>

{key_table}

{body_content}

<h2>Frequently Asked Questions</h2>
{faq_html}

<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team — eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="https://evisa.xuatnhapcanh.gov.vn" target="_blank" rel="noopener">evisa.xuatnhapcanh.gov.vn</a> before travel.</p>
</div>

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-vietnam.html">Vietnam Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="vietnam-visa-requirements.html">Vietnam Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="vietnam-visa-fees.html">Vietnam Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="vietnam-visa-processing-time.html">Vietnam Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>
{footer_scripts()}"""
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for slug, label, flag, demonym in NATIONALITIES:
        # Romania
        ro_filename = f"romania-visa-for-{slug}-citizens.html"
        ro_path = os.path.join(OUT_DIR, ro_filename)
        with open(ro_path, "w", encoding="utf-8") as f:
            f.write(romania_page(slug, label, flag, demonym))
        created.append(ro_filename)

        # Vietnam
        vn_filename = f"vietnam-visa-for-{slug}-citizens.html"
        vn_path = os.path.join(OUT_DIR, vn_filename)
        with open(vn_path, "w", encoding="utf-8") as f:
            f.write(vietnam_page(slug, label, flag, demonym))
        created.append(vn_filename)

    print(f"\nCreated {len(created)} files in {OUT_DIR}:\n")
    for i, fname in enumerate(created, 1):
        print(f"  {i:2d}. {fname}")
    print(f"\nDone — {len(created)} files generated.")


if __name__ == "__main__":
    main()
