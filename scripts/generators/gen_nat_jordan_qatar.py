#!/usr/bin/env python3
"""
Generate 40 HTML files for Jordan and Qatar nationality-specific visa pages.
Output: www/en/jordan-visa-for-{nat}-citizens.html  (20 files)
        www/en/qatar-visa-for-{nat}-citizens.html   (20 files)
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# --- nationality meta data ---------------------------------------------------
# slug -> (display_name, flag_code, adjective_for_passport_holders)
NATS = {
    "us":           ("American",        "us",  "US (American)"),
    "uk":           ("British",         "gb",  "British"),
    "canadian":     ("Canadian",        "ca",  "Canadian"),
    "french":       ("French",          "fr",  "French"),
    "german":       ("German",          "de",  "German"),
    "japanese":     ("Japanese",        "jp",  "Japanese"),
    "australian":   ("Australian",      "au",  "Australian"),
    "indian":       ("Indian",          "in",  "Indian"),
    "chinese":      ("Chinese",         "cn",  "Chinese"),
    "russian":      ("Russian",         "ru",  "Russian"),
    "brazilian":    ("Brazilian",       "br",  "Brazilian"),
    "mexican":      ("Mexican",         "mx",  "Mexican"),
    "south-african":("South African",   "za",  "South African"),
    "nigerian":     ("Nigerian",        "ng",  "Nigerian"),
    "korean":       ("South Korean",    "kr",  "South Korean"),
    "singaporean":  ("Singaporean",     "sg",  "Singaporean"),
    "indonesian":   ("Indonesian",      "id",  "Indonesian"),
    "philippine":   ("Philippine",      "ph",  "Philippine"),
    "turkish":      ("Turkish",         "tr",  "Turkish"),
    "argentinian":  ("Argentinian",     "ar",  "Argentinian"),
}

# --- Jordan visa status per nationality -------------------------------------
# VoA + eVisa group (JOD 40, moi.gov.jo)
JORDAN_VOA = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "russian", "brazilian", "mexican", "argentinian",
    "turkish", "south-african", "indonesian", "philippine",
}
# Must apply at consulate / eVisa restricted
JORDAN_EVISA_CONSULAR = {"indian", "chinese", "nigerian"}

# --- Qatar visa status per nationality --------------------------------------
QATAR_VISAFREE = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "brazilian", "mexican", "argentinian", "russian",
}
QATAR_EVISA = {
    "indian", "chinese", "indonesian", "philippine",
    "south-african", "nigerian", "turkish",
}

# ---------------------------------------------------------------------------
# HTML template helpers
# ---------------------------------------------------------------------------

HEAD_TMPL = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}"/>
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

NAV_TMPL = """\
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
                        <a class="dropdown-item active" href="/en/{page_file}"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>"""

FOOTER_TMPL = """\
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

EEAT_TMPL = """\
<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at the official immigration authority before travel.</p>
</div>"""

# ---------------------------------------------------------------------------
# Jordan page builder
# ---------------------------------------------------------------------------

def build_jordan(nat_slug):
    disp, flag, adj = NATS[nat_slug]
    page_file = f"jordan-visa-for-{nat_slug}-citizens.html"
    slug_noext = f"jordan-visa-for-{nat_slug}-citizens"
    title = f"Jordan Visa for {disp} Citizens 2026"
    country_dest = "Jordan"

    if nat_slug in JORDAN_VOA:
        status_label = '<span style="color:#e67e00;font-weight:600;">Visa on Arrival / eVisa — JOD 40</span>'
        visa_type = "Visa on Arrival (VoA) or eVisa"
        fee = "JOD 40 (~USD 56)"
        apply_at = "evisa.moi.gov.jo or on arrival at AMM"
        processing = "On arrival or 48 hours (eVisa)"
        meta_desc = (
            f"{disp} passport holders visiting Jordan in 2026: Visa on Arrival or eVisa, "
            f"JOD 40, 30-day stay. Jordan Pass (from JOD 70) includes visa fee. Updated March 2026."
        )
        faq_q1 = f"Do {disp} citizens need a visa for Jordan?"
        faq_a1 = (
            f"{disp} passport holders can obtain a Visa on Arrival (JOD 40) at Queen Alia International "
            f"Airport (AMM) or apply for an eVisa in advance at evisa.moi.gov.jo. "
            f"The Jordan Pass (from JOD 70) also includes the visa fee waiver if staying 3+ nights."
        )
        faq_q2 = "What is the Jordan Pass and is it worth it?"
        faq_a2 = (
            "The Jordan Pass (jordanpass.jo) combines the visa fee waiver with entry to 40+ attractions "
            "including Petra. Starting from JOD 70, it is excellent value for tourists visiting Petra and "
            "staying at least 3 consecutive nights in Jordan."
        )
        faq_q3 = "How long can I stay in Jordan?"
        faq_a3 = (
            "The standard tourist visa/VoA permits 30 days. Extensions up to 3 months are free and "
            "processed at local PSDSS offices or police stations."
        )
        body_section = f"""
<h2>Visa on Arrival for {disp} Citizens</h2>
<p>{disp} passport holders may obtain a <strong>Visa on Arrival (JOD 40, ~USD 56)</strong> on arrival at Queen Alia International Airport (AMM), the Aqaba border crossing, or other designated entry points. Alternatively, apply online via the Jordan eVisa portal before travelling to skip airport queues.</p>

<h2>Jordan Pass — Best Value Option</h2>
<p>The <strong>Jordan Pass</strong> (from JOD 70 at <a href="https://www.jordanpass.jo" target="_blank" rel="noopener">jordanpass.jo</a>) includes the visa fee waiver and entry to over 40 attractions, including Petra (normally JOD 50/day). It is the recommended option for tourists planning to visit Petra and staying at least 3 consecutive nights.</p>

<h2>How to Apply — eVisa Option</h2>
<ol>
<li>Visit <a href="https://evisa.moi.gov.jo" target="_blank" rel="noopener">evisa.moi.gov.jo</a>.</li>
<li>Complete the online application form with your passport details.</li>
<li>Pay JOD 40 online (card payment accepted).</li>
<li>Receive eVisa approval by email within 48 hours.</li>
<li>Print or save the eVisa and present at immigration on arrival.</li>
</ol>

<h2>How to Apply — Visa on Arrival</h2>
<ol>
<li>Arrive at a designated Jordanian entry point (e.g., AMM airport).</li>
<li>Proceed to the Visa on Arrival counter before passport control.</li>
<li>Pay JOD 40 in cash (JOD, USD, or EUR accepted).</li>
<li>Receive visa sticker and proceed to immigration.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond stay)</li>
<li>Return or onward flight ticket</li>
<li>Accommodation confirmation</li>
<li>Proof of sufficient funds</li>
<li>Jordan Pass printout or eVisa approval (if applicable)</li>
<li>Travel insurance (recommended)</li>
</ul>

<h2>Stay Duration &amp; Extension</h2>
<p>The visa on arrival and eVisa permit a <strong>30-day stay</strong>. Extensions up to 3 months total are available free of charge at local PSDSS offices or police stations. Overstaying without extension incurs fines.</p>
"""
    else:
        # eVisa or consular (indian, chinese, nigerian)
        status_label = '<span style="color:red;font-weight:600;">eVisa or Consular Visa Required</span>'
        visa_type = "eVisa or Embassy/Consulate Visa"
        fee = "JOD 40 (eVisa) — consulate fees vary"
        apply_at = "evisa.moi.gov.jo or Jordanian Embassy"
        processing = "1–5 business days (eVisa); 5–15 days (consulate)"
        meta_desc = (
            f"{disp} passport holders visiting Jordan in 2026 must apply for an eVisa or consular visa. "
            f"eVisa JOD 40, apply at evisa.moi.gov.jo. Updated March 2026."
        )
        faq_q1 = f"Do {disp} citizens need a visa for Jordan?"
        faq_a1 = (
            f"{disp} passport holders are required to obtain a visa before travelling to Jordan. "
            f"The eVisa (JOD 40) is available at evisa.moi.gov.jo. Alternatively, apply at the nearest "
            f"Jordanian embassy or consulate."
        )
        faq_q2 = "How long does Jordan visa processing take?"
        faq_a2 = (
            "The Jordan eVisa is typically processed within 1–5 business days. "
            "Consular applications may take 5–15 business days. Apply well in advance of your travel date."
        )
        faq_q3 = "What documents are required for the Jordan visa?"
        faq_a3 = (
            "Required documents include a valid passport (6+ months validity), passport-size photos, "
            "bank statements, return flight ticket, hotel/accommodation confirmation, and travel insurance."
        )
        body_section = f"""
<h2>Jordan eVisa for {disp} Citizens</h2>
<p>{disp} passport holders must obtain a visa before travelling to Jordan. The most convenient option is the <strong>Jordan eVisa</strong> (JOD 40), applied online at <a href="https://evisa.moi.gov.jo" target="_blank" rel="noopener">evisa.moi.gov.jo</a>. Alternatively, a visa may be obtained from the nearest Jordanian embassy or consulate.</p>

<h2>Jordan Pass — Best Value Option</h2>
<p>The <strong>Jordan Pass</strong> (from JOD 70 at <a href="https://www.jordanpass.jo" target="_blank" rel="noopener">jordanpass.jo</a>) includes the visa fee waiver and entry to over 40 tourist sites including Petra (normally JOD 50/day). Highly recommended for tourists staying 3+ nights and visiting major sites.</p>

<h2>How to Apply — eVisa</h2>
<ol>
<li>Visit <a href="https://evisa.moi.gov.jo" target="_blank" rel="noopener">evisa.moi.gov.jo</a>.</li>
<li>Create an account and complete the application form.</li>
<li>Upload required documents (passport scan, photo, supporting documents).</li>
<li>Pay JOD 40 online.</li>
<li>Receive approval by email within 1–5 business days.</li>
<li>Print the eVisa and present at the port of entry.</li>
</ol>

<h2>How to Apply — Consular Visa</h2>
<ol>
<li>Locate the nearest Jordanian embassy or consulate.</li>
<li>Download and complete the visa application form.</li>
<li>Gather all required documents.</li>
<li>Submit in person or by post with the consulate fee.</li>
<li>Allow 5–15 business days for processing.</li>
<li>Collect passport with visa sticker.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity)</li>
<li>Recent passport-size photograph</li>
<li>Bank statements (last 3 months)</li>
<li>Return or onward flight ticket</li>
<li>Hotel/accommodation confirmation</li>
<li>Travel insurance</li>
<li>Proof of employment or business (if applicable)</li>
</ul>

<h2>Stay Duration &amp; Extension</h2>
<p>Approved visas typically permit a <strong>30-day stay</strong>. Extensions are available at PSDSS offices. Overstaying without extension incurs fines.</p>
"""

    schema_json = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{{"@type":"Question","name":"{q1}","acceptedAnswer":{{"@type":"Answer","text":"{a1}"}}}},'
        '{{"@type":"Question","name":"{q2}","acceptedAnswer":{{"@type":"Answer","text":"{a2}"}}}},'
        '{{"@type":"Question","name":"{q3}","acceptedAnswer":{{"@type":"Answer","text":"{a3}"}}}}'
        ']}}'
    ).format(
        q1=faq_q1.replace('"', '&quot;'), a1=faq_a1.replace('"', '&quot;'),
        q2=faq_q2.replace('"', '&quot;'), a2=faq_a2.replace('"', '&quot;'),
        q3=faq_q3.replace('"', '&quot;'), a3=faq_a3.replace('"', '&quot;'),
    )

    head = HEAD_TMPL.format(
        title=title, meta_desc=meta_desc,
        slug=slug_noext, schema_json=schema_json,
    )
    nav = NAV_TMPL.format(page_file=page_file)

    html = f"""{head}
{nav}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Jordan for {disp} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Status</th><td>{status_label}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>30 days (extendable to 3 months)</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
<tr><th>Jordan Pass</th><td>From JOD 70 &mdash; includes visa &amp; 40+ attractions (jordanpass.jo)</td></tr>
</tbody>
</table>

{body_section}

{EEAT_TMPL}

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Jordan Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-jordan.html">Jordan Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="jordan-visa-requirements.html">Jordan Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="jordan-visa-fees.html">Jordan Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="jordan-visa-processing-time.html">Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="qatar-visa-for-{nat_slug}-citizens.html">Qatar Visa for {disp}</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER_TMPL}"""
    return html, page_file


# ---------------------------------------------------------------------------
# Qatar page builder
# ---------------------------------------------------------------------------

def build_qatar(nat_slug):
    disp, flag, adj = NATS[nat_slug]
    page_file = f"qatar-visa-for-{nat_slug}-citizens.html"
    slug_noext = f"qatar-visa-for-{nat_slug}-citizens"
    title = f"Qatar Visa for {disp} Citizens 2026"

    if nat_slug in QATAR_VISAFREE:
        status_label = '<span style="color:green;font-weight:600;">Visa-Free &mdash; 30 Days</span>'
        visa_type = "Visa-Free Entry"
        fee = "Free"
        apply_at = "No advance application required"
        processing = "On arrival — no application needed"
        meta_desc = (
            f"{disp} passport holders can enter Qatar visa-free for up to 30 days in 2026. "
            f"No advance application required. Updated March 2026."
        )
        faq_q1 = f"Do {disp} citizens need a visa for Qatar?"
        faq_a1 = (
            f"{disp} passport holders enjoy visa-free entry to Qatar for stays of up to 30 days. "
            f"No advance application or fee is required. Simply present your passport at Hamad International Airport (DOH)."
        )
        faq_q2 = "How long can I stay in Qatar visa-free?"
        faq_a2 = (
            "The standard visa-free period is 30 days, extendable for a further 30 days via the "
            "Ministry of Interior portal (portal.moi.gov.qa) for a fee of QAR 100."
        )
        faq_q3 = "Can I extend my visa-free stay in Qatar?"
        faq_a3 = (
            "Yes. You may apply online at portal.moi.gov.qa to extend your stay for an additional 30 days "
            "by paying QAR 100 (~USD 27). Apply before your initial 30-day period expires."
        )
        body_section = f"""
<h2>Visa-Free Entry for {disp} Citizens</h2>
<p>{disp} passport holders enjoy <strong>visa-free access to Qatar for up to 30 days</strong>. No advance application or fee is required. Present your valid passport at immigration upon arrival at Hamad International Airport (DOH) or any official land/sea border.</p>

<h2>Entry Requirements</h2>
<ul>
<li>Valid passport with at least 6 months validity beyond your intended stay</li>
<li>Return or onward flight ticket</li>
<li>Proof of accommodation (hotel booking or host invitation)</li>
<li>Sufficient funds for the duration of stay</li>
<li>Travel insurance (recommended)</li>
</ul>

<h2>Extending Your Stay</h2>
<p>If you wish to stay beyond 30 days, you can apply for a 30-day extension via the Qatar Ministry of Interior portal at <a href="https://portal.moi.gov.qa" target="_blank" rel="noopener">portal.moi.gov.qa</a>. The extension fee is <strong>QAR 100 (~USD 27)</strong>. Apply before your initial 30-day period expires to avoid fines.</p>

<h2>Useful Tips</h2>
<ul>
<li>Qatar is a Muslim country — dress modestly in public areas outside of hotels and beaches.</li>
<li>Alcohol is available in licensed hotels and restaurants.</li>
<li>The Hayya Card (if applicable for events) may affect entry requirements during major events — check visit.qatar.com.</li>
<li>Keep a printed copy of your accommodation booking for border control.</li>
</ul>
"""
    else:
        # eVisa required
        status_label = '<span style="color:#e67e00;font-weight:600;">eVisa Required &mdash; QAR 100 (~USD 27)</span>'
        visa_type = "eVisa"
        fee = "QAR 100 (~USD 27)"
        apply_at = "portal.moi.gov.qa"
        processing = "Instant to 72 hours"
        meta_desc = (
            f"{disp} passport holders need an eVisa for Qatar in 2026. "
            f"Apply online at portal.moi.gov.qa, fee QAR 100 (~USD 27), processed within 72 hours. Updated March 2026."
        )
        faq_q1 = f"Do {disp} citizens need a visa for Qatar?"
        faq_a1 = (
            f"{disp} passport holders must obtain a Qatar eVisa before or on arrival. "
            f"Apply online at portal.moi.gov.qa. The fee is QAR 100 (~USD 27) and processing typically takes "
            f"up to 72 hours."
        )
        faq_q2 = "How do I apply for a Qatar eVisa?"
        faq_a2 = (
            "Visit portal.moi.gov.qa, create an account, fill in the application with your passport details, "
            "upload a passport-size photo and passport scan, pay QAR 100 online, and receive your eVisa by email."
        )
        faq_q3 = "How long does Qatar eVisa processing take?"
        faq_a3 = (
            "Most Qatar eVisa applications are approved within a few minutes to 72 hours. "
            "Apply at least 3–5 days before travel to allow sufficient processing time."
        )
        body_section = f"""
<h2>Qatar eVisa for {disp} Citizens</h2>
<p>{disp} passport holders must obtain a <strong>Qatar eVisa</strong> before travelling. Apply online at <a href="https://portal.moi.gov.qa" target="_blank" rel="noopener">portal.moi.gov.qa</a>. The fee is <strong>QAR 100 (~USD 27)</strong> and processing is typically completed within 72 hours.</p>

<h2>Qatar eVisa Key Details</h2>
<ul>
<li>Fee: <strong>QAR 100 (~USD 27)</strong></li>
<li>Processing time: Minutes to 72 hours</li>
<li>Stay: Up to 30 days (extendable by 30 more days)</li>
<li>Entry: Single entry</li>
<li>Apply at: <a href="https://portal.moi.gov.qa" target="_blank" rel="noopener">portal.moi.gov.qa</a></li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Go to <a href="https://portal.moi.gov.qa" target="_blank" rel="noopener">portal.moi.gov.qa</a>.</li>
<li>Register or log in to create an eVisa application.</li>
<li>Enter your passport details and personal information.</li>
<li>Upload a passport-size photo (white background) and passport bio-data page scan.</li>
<li>Pay QAR 100 using a credit or debit card.</li>
<li>Receive eVisa approval by email.</li>
<li>Print or save the eVisa and present it at the port of entry.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (minimum 6 months validity beyond stay)</li>
<li>Passport-size photograph (white background)</li>
<li>Scanned copy of passport bio-data page</li>
<li>Return or onward flight ticket</li>
<li>Hotel or accommodation booking confirmation</li>
<li>Proof of sufficient funds</li>
<li>Travel insurance (recommended)</li>
</ul>

<h2>Extending Your eVisa Stay</h2>
<p>You can extend your Qatar eVisa for a further 30 days via <a href="https://portal.moi.gov.qa" target="_blank" rel="noopener">portal.moi.gov.qa</a> by paying an additional QAR 100. Apply before your initial visa period expires.</p>
"""

    schema_json = (
        '{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        '{{"@type":"Question","name":"{q1}","acceptedAnswer":{{"@type":"Answer","text":"{a1}"}}}},'
        '{{"@type":"Question","name":"{q2}","acceptedAnswer":{{"@type":"Answer","text":"{a2}"}}}},'
        '{{"@type":"Question","name":"{q3}","acceptedAnswer":{{"@type":"Answer","text":"{a3}"}}}}'
        ']}}'
    ).format(
        q1=faq_q1.replace('"', '&quot;'), a1=faq_a1.replace('"', '&quot;'),
        q2=faq_q2.replace('"', '&quot;'), a2=faq_a2.replace('"', '&quot;'),
        q3=faq_q3.replace('"', '&quot;'), a3=faq_a3.replace('"', '&quot;'),
    )

    head = HEAD_TMPL.format(
        title=title, meta_desc=meta_desc,
        slug=slug_noext, schema_json=schema_json,
    )
    nav = NAV_TMPL.format(page_file=page_file)

    html = f"""{head}
{nav}

<section class="ftco-section">
<div class="container">
<article class="country-page">

<h1><span class="fi fi-{flag}"></span> {title}</h1>

<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts &mdash; Qatar for {disp} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Status</th><td>{status_label}</td></tr>
<tr><th>Visa Type</th><td>{visa_type}</td></tr>
<tr><th>Fee</th><td>{fee}</td></tr>
<tr><th>Max Stay</th><td>30 days (extendable 30 more days)</td></tr>
<tr><th>Processing</th><td>{processing}</td></tr>
<tr><th>Apply At</th><td>{apply_at}</td></tr>
</tbody>
</table>

{body_section}

{EEAT_TMPL}

<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Qatar Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-qatar.html">Qatar Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="qatar-visa-requirements.html">Qatar Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="qatar-visa-fees.html">Qatar Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="qatar-visa-processing-time.html">Processing Times</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="jordan-visa-for-{nat_slug}-citizens.html">Jordan Visa for {disp}</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>

</article>
</div>
</section>

{FOOTER_TMPL}"""
    return html, page_file


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for nat_slug in NATS:
        # Jordan
        html, fname = build_jordan(nat_slug)
        path = os.path.join(OUT_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(fname)

        # Qatar
        html, fname = build_qatar(nat_slug)
        path = os.path.join(OUT_DIR, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(fname)

    print(f"\nCreated {len(created)} files in {OUT_DIR}:\n")
    for fn in sorted(created):
        print(f"  {fn}")
    print(f"\nTotal: {len(created)}")


if __name__ == "__main__":
    main()
