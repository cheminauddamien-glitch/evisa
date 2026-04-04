"""
gen_nat_nz_hk.py
Generates 40 HTML files in www/en/:
  new-zealand-visa-for-{nat}-citizens.html   (20 files)
  hong-kong-visa-for-{nat}-citizens.html     (20 files)
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# --- Nationality metadata ---
# (slug, label, flag-icon code, adjective for prose)
NATIONALITIES = [
    ("us",           "US",           "us",  "US"),
    ("uk",           "UK",           "gb",  "UK"),
    ("canadian",     "Canadian",     "ca",  "Canadian"),
    ("french",       "French",       "fr",  "French"),
    ("german",       "German",       "de",  "German"),
    ("japanese",     "Japanese",     "jp",  "Japanese"),
    ("australian",   "Australian",   "au",  "Australian"),
    ("indian",       "Indian",       "in",  "Indian"),
    ("chinese",      "Chinese",      "cn",  "Chinese"),
    ("russian",      "Russian",      "ru",  "Russian"),
    ("brazilian",    "Brazilian",    "br",  "Brazilian"),
    ("mexican",      "Mexican",      "mx",  "Mexican"),
    ("south-african","South African","za",  "South African"),
    ("nigerian",     "Nigerian",     "ng",  "Nigerian"),
    ("korean",       "Korean",       "kr",  "Korean"),
    ("singaporean",  "Singaporean",  "sg",  "Singaporean"),
    ("indonesian",   "Indonesian",   "id",  "Indonesian"),
    ("philippine",   "Philippine",   "ph",  "Philippine"),
    ("turkish",      "Turkish",      "tr",  "Turkish"),
    ("argentinian",  "Argentinian",  "ar",  "Argentinian"),
]

# --- New Zealand visa status ---
# NZeTA nationalities (mobile NZD 17 / web NZD 23 + IVL NZD 35)
NZ_NZETA = {
    "uk", "us", "canadian", "french", "german", "japanese",
    "korean", "singaporean", "brazilian", "mexican", "argentinian"
}
# Trans-Tasman (no NZeTA)
NZ_TRANSTASMAN = {"australian"}
# Visitor Visa (NZD 211, 3 months processing)
NZ_VISAREQUIRED = {
    "indian", "chinese", "russian", "indonesian",
    "philippine", "nigerian", "south-african", "turkish"
}

# --- Hong Kong visa status ---
# Visa-free 90 days
HK_FREE90 = {
    "us", "uk", "canadian", "french", "german", "japanese",
    "australian", "korean", "singaporean", "brazilian", "mexican",
    "argentinian", "russian"
}
# Visa-free 30 days
HK_FREE30 = {"indonesian", "philippine"}
# Visa required (immd.gov.hk)
HK_VISAREQUIRED = {"indian", "nigerian", "south-african", "turkish"}
# Chinese mainland — Home Return Permit (separate system)
HK_HOMERETURN = {"chinese"}


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def head(title, description, canonical_slug, flag_code):
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
    <link href="../css/style.css" rel="stylesheet"/>"""


def favicon_and_close_head():
    return """    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>"""


def navbar(current_slug):
    return f"""<body>
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


def footer_and_scripts():
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
<script src="../js/main.js"></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# New Zealand page builder
# ---------------------------------------------------------------------------

def build_nz_page(slug, label, flag_code, adj):
    filename = f"new-zealand-visa-for-{slug}-citizens.html"
    canonical = f"new-zealand-visa-for-{slug}-citizens"
    title = f"New Zealand Visa for {label} Citizens 2026"

    if slug in NZ_TRANSTASMAN:
        # Australian — Trans-Tasman, no NZeTA
        description = (
            f"Australian citizens do not need a visa or NZeTA to enter New Zealand. "
            f"Trans-Tasman Travel Arrangement allows unlimited stays. Updated March 2026."
        )
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — Trans-Tasman</span>'
        faq = f"""[{{"@type":"Question","name":"Do Australian citizens need a visa for New Zealand?","acceptedAnswer":{{"@type":"Answer","text":"No. Australian citizens can enter New Zealand freely under the Trans-Tasman Travel Arrangement. No visa or NZeTA is required and there is no limit on the length of stay."}}}},
      {{"@type":"Question","name":"Is the NZeTA required for Australians?","acceptedAnswer":{{"@type":"Answer","text":"No. Australian passport holders are exempt from both the NZeTA and the International Visitor Levy (IVL)."}}}},
      {{"@type":"Question","name":"Can Australians live and work in New Zealand?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Under the Trans-Tasman Travel Arrangement, Australian citizens may live, work, and study in New Zealand indefinitely."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — New Zealand for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Entry Requirement</th><td>{status_cell}</td></tr>
<tr><th>Arrangement</th><td>Trans-Tasman Travel Arrangement</td></tr>
<tr><th>Fee</th><td>None</td></tr>
<tr><th>Max Stay</th><td>Unlimited</td></tr>
<tr><th>NZeTA Required</th><td>No</td></tr>
<tr><th>IVL Required</th><td>No</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>New Zealand Entry for Australian Citizens</h2>
<p>Australian citizens enjoy unrestricted entry to New Zealand under the <strong>Trans-Tasman Travel Arrangement</strong>. No visa, NZeTA, or International Visitor Levy (IVL) is required. Australians may live, work, and study in New Zealand without any immigration approval.</p>

<h2>What You Need to Travel</h2>
<ul>
<li>Valid Australian passport (or a valid New Zealand permanent resident visa in an Australian passport)</li>
<li>No NZeTA needed</li>
<li>No IVL payment needed</li>
</ul>

<h2>Trans-Tasman Arrangement Details</h2>
<p>The Trans-Tasman Travel Arrangement between Australia and New Zealand is one of the most open bilateral travel agreements in the world. {label} citizens arriving in New Zealand are processed quickly at immigration and have the right to remain indefinitely.</p>"""
        eeat_link = "https://www.immigration.govt.nz/new-zealand-visas/pages/visa-decision-tree"
        related = f"""<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-new-zealand.html">New Zealand Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-requirements.html">NZ Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-fees.html">NZ Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-processing-time.html">NZ Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    elif slug in NZ_NZETA:
        # NZeTA required
        description = (
            f"{label} passport holders visiting New Zealand in 2026 need an NZeTA "
            f"(NZD 17 mobile / NZD 23 web) plus IVL NZD 35. Updated March 2026."
        )
        status_cell = '<span style="color:orange;font-weight:600;">NZeTA Required — NZD 17 (mobile) / NZD 23 (web) + IVL NZD 35</span>'
        faq = f"""[{{"@type":"Question","name":"Do {label} citizens need a visa for New Zealand?","acceptedAnswer":{{"@type":"Answer","text":"{label} passport holders do not need a traditional visa but must obtain an NZeTA before travel. The NZeTA costs NZD 17 via mobile app or NZD 23 online, plus an International Visitor Levy (IVL) of NZD 35."}}}},
      {{"@type":"Question","name":"What is the NZeTA?","acceptedAnswer":{{"@type":"Answer","text":"The New Zealand Electronic Travel Authority (NZeTA) is a pre-travel authorisation required for visa-waiver countries. It is linked electronically to your passport and is valid for multiple trips over 2 years or until your passport expires."}}}},
      {{"@type":"Question","name":"How long can {label} citizens stay in New Zealand?","acceptedAnswer":{{"@type":"Answer","text":"{label} citizens with an NZeTA can stay up to 90 days per visit as a visitor."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — New Zealand for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Entry Requirement</th><td>{status_cell}</td></tr>
<tr><th>NZeTA Fee (mobile app)</th><td>NZD 17</td></tr>
<tr><th>NZeTA Fee (web)</th><td>NZD 23</td></tr>
<tr><th>IVL (International Visitor Levy)</th><td>NZD 35</td></tr>
<tr><th>Max Stay</th><td>Up to 90 days per visit</td></tr>
<tr><th>NZeTA Validity</th><td>2 years or until passport expiry</td></tr>
<tr><th>Apply At</th><td>nzeta.immigration.govt.nz</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>NZeTA for {label} Citizens</h2>
<p>{label} passport holders do not need a traditional visa but must obtain a <strong>New Zealand Electronic Travel Authority (NZeTA)</strong> before boarding any flight or cruise to New Zealand. The NZeTA costs <strong>NZD 17</strong> via the official mobile app or <strong>NZD 23</strong> online, plus the <strong>International Visitor Levy (IVL) of NZD 35</strong> (paid at the same time).</p>

<h2>NZeTA Key Details</h2>
<ul>
<li>Mobile app fee: <strong>NZD 17</strong> + IVL NZD 35</li>
<li>Web application fee: <strong>NZD 23</strong> + IVL NZD 35</li>
<li>Validity: 2 years or until passport expiry (whichever is sooner)</li>
<li>Multiple trips allowed during validity period</li>
<li>Max stay per visit: <strong>90 days</strong></li>
<li>Processing: Usually within 72 hours (apply early)</li>
</ul>

<h2>How to Apply for the NZeTA</h2>
<ol>
<li>Download the official NZeTA app (iOS/Android) or visit <a href='https://nzeta.immigration.govt.nz' target='_blank' rel='noopener'>nzeta.immigration.govt.nz</a>.</li>
<li>Upload a passport photo and photo of your passport data page.</li>
<li>Answer eligibility questions.</li>
<li>Pay NZD 17 (app) or NZD 23 (web) + IVL NZD 35 by credit/debit card.</li>
<li>Receive your NZeTA decision — usually within 72 hours.</li>
</ol>

<h2>What Documents to Carry</h2>
<ul>
<li>Valid {label} passport (6+ months validity recommended)</li>
<li>NZeTA approval (linked to passport — no printout required)</li>
<li>Return/onward travel ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details</li>
</ul>"""
        eeat_link = "https://nzeta.immigration.govt.nz"
        related = f"""<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-new-zealand.html">New Zealand Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-requirements.html">NZ Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-fees.html">NZ Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-processing-time.html">NZ Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    else:
        # Visitor Visa required
        description = (
            f"{label} passport holders visiting New Zealand in 2026 must obtain a Visitor Visa "
            f"(NZD 211, up to 3 months processing). Updated March 2026."
        )
        status_cell = '<span style="color:red;font-weight:600;">Visitor Visa Required — NZD 211</span>'
        faq = f"""[{{"@type":"Question","name":"Do {label} citizens need a visa for New Zealand?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {label} passport holders must apply for a New Zealand Visitor Visa before travelling. The visa fee is NZD 211 and processing can take up to 3 months."}}}},
      {{"@type":"Question","name":"How much does the New Zealand Visitor Visa cost for {label} citizens?","acceptedAnswer":{{"@type":"Answer","text":"The New Zealand Visitor Visa fee for {label} passport holders is NZD 211, paid at the time of application."}}}},
      {{"@type":"Question","name":"How long does NZ Visitor Visa processing take?","acceptedAnswer":{{"@type":"Answer","text":"Processing for {label} applicants can take up to 3 months. Apply as early as possible before your intended travel date."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — New Zealand for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Visa Type</th><td>Visitor Visa</td></tr>
<tr><th>Fee</th><td>NZD 211</td></tr>
<tr><th>Max Stay</th><td>Up to 9 months</td></tr>
<tr><th>Processing</th><td>Up to 3 months</td></tr>
<tr><th>Apply At</th><td>immigration.govt.nz</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>New Zealand Visitor Visa for {label} Citizens</h2>
<p>{label} passport holders must obtain a <strong>New Zealand Visitor Visa</strong> before travelling. The application is submitted online through Immigration New Zealand. The fee is <strong>NZD 211</strong> and processing can take <strong>up to 3 months</strong> — apply well in advance.</p>

<h2>Visitor Visa Key Details</h2>
<ul>
<li>Fee: <strong>NZD 211</strong></li>
<li>Processing time: Up to 3 months</li>
<li>Stay: Up to 9 months</li>
<li>Entries: Single or multiple (as granted)</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Create an account at <a href='https://www.immigration.govt.nz' target='_blank' rel='noopener'>immigration.govt.nz</a>.</li>
<li>Complete the online Visitor Visa application form.</li>
<li>Upload supporting documents (see below).</li>
<li>Pay NZD 211 by credit/debit card.</li>
<li>Await a decision — processing can take up to 3 months.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid passport (3+ months beyond intended stay)</li>
<li>Recent passport-sized photographs</li>
<li>Bank statements (last 3–6 months)</li>
<li>Proof of employment or business ownership</li>
<li>Travel itinerary and accommodation proof</li>
<li>Return/onward flight booking</li>
<li>Travel insurance</li>
</ul>"""
        eeat_link = "https://www.immigration.govt.nz/new-zealand-visas/apply-for-a-visa/about-visa/visitor-visa"
        related = f"""<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-new-zealand.html">New Zealand Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-requirements.html">NZ Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-fees.html">NZ Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="new-zealand-visa-processing-time.html">NZ Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    faq_json = f"""    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq}}}
    </script>"""

    html = "\n".join([
        head(title, description, canonical, flag_code),
        faq_json,
        favicon_and_close_head(),
        navbar(canonical),
        "",
        "<section class=\"ftco-section\">",
        "<div class=\"container\">",
        "<article class=\"country-page\">",
        "",
        f"<h1>{title}</h1>",
        "",
        key_table,
        "",
        body_content,
        "",
        f"""<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{eeat_link}" target="_blank" rel="noopener">immigration.govt.nz</a> before travel.</p>
</div>""",
        "",
        related,
        "",
        "</article>",
        "</div>",
        "</section>",
        "",
        footer_and_scripts(),
    ])
    return filename, html


# ---------------------------------------------------------------------------
# Hong Kong page builder
# ---------------------------------------------------------------------------

def build_hk_page(slug, label, flag_code, adj):
    filename = f"hong-kong-visa-for-{slug}-citizens.html"
    canonical = f"hong-kong-visa-for-{slug}-citizens"
    title = f"Hong Kong Visa for {label} Citizens 2026"

    if slug in HK_HOMERETURN:
        # Chinese mainland — Home Return Permit
        description = (
            "Chinese mainland citizens visiting Hong Kong in 2026 use the Home Return Permit "
            "(回乡证), not a standard visa. Updated March 2026."
        )
        status_cell = '<span style="color:blue;font-weight:600;">Home Return Permit (回乡证) — Separate System</span>'
        faq = """[{"@type":"Question","name":"Do Chinese mainland citizens need a visa for Hong Kong?","acceptedAnswer":{"@type":"Answer","text":"Chinese mainland citizens do not use a standard visa to visit Hong Kong. Instead they must hold a valid Home Return Permit (Huixiang Zheng / 回乡证), which is issued by mainland authorities."}},
      {"@type":"Question","name":"Where do Chinese citizens apply for the Home Return Permit?","acceptedAnswer":{"@type":"Answer","text":"The Home Return Permit is issued by mainland public security bureaux. It is not processed through the Hong Kong Immigration Department (IMMD)."}},
      {"@type":"Question","name":"How long can mainland Chinese citizens stay in Hong Kong?","acceptedAnswer":{"@type":"Answer","text":"Holders of a Home Return Permit may generally stay up to 7 days per visit for tourism and up to 3 months for other purposes, subject to conditions endorsed on the permit."}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Hong Kong for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Entry Requirement</th><td>{status_cell}</td></tr>
<tr><th>Document</th><td>Home Return Permit (回乡证 / Huixiang Zheng)</td></tr>
<tr><th>Issued By</th><td>Mainland public security bureaux (not IMMD)</td></tr>
<tr><th>Stay Allowed</th><td>Up to 7 days (tourism) / Up to 3 months (other)</td></tr>
<tr><th>Note</th><td>Hong Kong is a separate immigration territory from mainland China</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Chinese Mainland Citizens and Hong Kong Entry</h2>
<p>Hong Kong is a <strong>Special Administrative Region (SAR)</strong> of China with its own immigration controls, separate from the mainland. Chinese mainland citizens do <strong>not</strong> use a standard tourist visa to visit Hong Kong. Instead, they must hold a valid <strong>Home Return Permit</strong> (<em>Huixiang Zheng</em> / 回乡证).</p>

<h2>Home Return Permit Details</h2>
<ul>
<li>Also known as: <strong>Mainland Travel Permit for Hong Kong and Macao Residents</strong> (港澳居民来往内地通行证) for HK/Macao residents, or <em>Home Return Permit</em> for mainland citizens</li>
<li>Issued by: Mainland public security authorities</li>
<li>Not processed through Hong Kong Immigration Department (IMMD)</li>
<li>Stay: Up to 7 days per visit for tourism; up to 3 months for other permitted purposes</li>
</ul>

<h2>Important Note on Hong Kong's Immigration System</h2>
<p>Because Hong Kong operates under the "One Country, Two Systems" principle, it maintains a completely separate immigration system from mainland China. Mainland citizens must comply with Hong Kong's immigration requirements independently of any mainland travel documents.</p>"""
        eeat_link = "https://www.immd.gov.hk/eng/services/index.html"
        eeat_text = "immd.gov.hk"

    elif slug in HK_FREE90:
        # Visa-free 90 days
        description = (
            f"{label} passport holders can visit Hong Kong visa-free for up to 90 days in 2026. "
            f"No prior application required. Updated March 2026."
        )
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — Up to 90 Days</span>'
        faq = f"""[{{"@type":"Question","name":"Do {label} citizens need a visa for Hong Kong?","acceptedAnswer":{{"@type":"Answer","text":"No. {label} passport holders can visit Hong Kong for tourism, business, or transit for up to 90 days without a visa. No prior application is required."}}}},
      {{"@type":"Question","name":"Can {label} citizens work in Hong Kong visa-free?","acceptedAnswer":{{"@type":"Answer","text":"No. The visa-free arrangement covers tourism, business visits, and transit only. {label} citizens who wish to work in Hong Kong must obtain the appropriate work visa before starting employment."}}}},
      {{"@type":"Question","name":"Is there any pre-travel application needed?","acceptedAnswer":{{"@type":"Answer","text":"No. {label} citizens simply present their valid passport on arrival at any Hong Kong immigration control point. No eTA or pre-registration is required."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Hong Kong for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Max Stay</th><td>90 days per visit</td></tr>
<tr><th>Pre-Application</th><td>Not required</td></tr>
<tr><th>Permitted Activities</th><td>Tourism, business visits, transit</td></tr>
<tr><th>Work Allowed</th><td>No</td></tr>
<tr><th>Entry Point</th><td>Any Hong Kong immigration control point</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Visa-Free Entry to Hong Kong for {label} Citizens</h2>
<p>{label} passport holders can enter Hong Kong <strong>visa-free for up to 90 days</strong> per visit. No prior application, eTA, or registration is required. Simply present your valid passport at any Hong Kong immigration control point on arrival.</p>

<h2>Visa-Free Stay Details</h2>
<ul>
<li>Stay allowed: <strong>Up to 90 days per visit</strong></li>
<li>Permitted activities: Tourism, business meetings, transit</li>
<li>Work: Not permitted under visa-free entry</li>
<li>No eTA or pre-registration required</li>
</ul>

<h2>What to Carry on Arrival</h2>
<ul>
<li>Valid {label} passport (valid for the full duration of your stay)</li>
<li>Return or onward travel ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details</li>
</ul>

<h2>Extending Your Stay</h2>
<p>If you wish to stay longer than 90 days, you must apply for an extension through the Hong Kong Immigration Department at <a href="https://www.immd.gov.hk" target="_blank" rel="noopener">immd.gov.hk</a> before your permitted period expires.</p>"""
        eeat_link = "https://www.immd.gov.hk/eng/services/visas/visit-transit/visit-visa-entry-permit.html"
        eeat_text = "immd.gov.hk"

    elif slug in HK_FREE30:
        # Visa-free 30 days
        description = (
            f"{label} passport holders can visit Hong Kong visa-free for up to 30 days in 2026. "
            f"No prior application required. Updated March 2026."
        )
        status_cell = '<span style="color:green;font-weight:600;">Visa-Free — Up to 30 Days</span>'
        faq = f"""[{{"@type":"Question","name":"Do {label} citizens need a visa for Hong Kong?","acceptedAnswer":{{"@type":"Answer","text":"No. {label} passport holders can visit Hong Kong for up to 30 days without a visa. No prior application is required."}}}},
      {{"@type":"Question","name":"Can {label} citizens extend their stay in Hong Kong?","acceptedAnswer":{{"@type":"Answer","text":"Extensions beyond 30 days are possible but must be applied for at the Hong Kong Immigration Department (immd.gov.hk) before the permitted period expires."}}}},
      {{"@type":"Question","name":"What can {label} citizens do in Hong Kong visa-free?","acceptedAnswer":{{"@type":"Answer","text":"{label} citizens may visit for tourism, business meetings, and transit. Working in Hong Kong requires a separate work visa."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Hong Kong for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Max Stay</th><td>30 days per visit</td></tr>
<tr><th>Pre-Application</th><td>Not required</td></tr>
<tr><th>Permitted Activities</th><td>Tourism, business visits, transit</td></tr>
<tr><th>Work Allowed</th><td>No</td></tr>
<tr><th>Entry Point</th><td>Any Hong Kong immigration control point</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Visa-Free Entry to Hong Kong for {label} Citizens</h2>
<p>{label} passport holders can enter Hong Kong <strong>visa-free for up to 30 days</strong> per visit. No prior application is required — simply present your valid passport on arrival at any Hong Kong immigration control point.</p>

<h2>Visa-Free Stay Details</h2>
<ul>
<li>Stay allowed: <strong>Up to 30 days per visit</strong></li>
<li>Permitted activities: Tourism, business meetings, transit</li>
<li>Work: Not permitted under visa-free entry</li>
<li>No eTA or pre-registration required</li>
</ul>

<h2>What to Carry on Arrival</h2>
<ul>
<li>Valid {label} passport (valid for the full duration of your stay)</li>
<li>Return or onward travel ticket</li>
<li>Proof of sufficient funds</li>
<li>Accommodation details</li>
</ul>

<h2>Extending Your Stay</h2>
<p>If you wish to stay longer than 30 days, you must apply for an extension at the Hong Kong Immigration Department (<a href="https://www.immd.gov.hk" target="_blank" rel="noopener">immd.gov.hk</a>) before your permitted period expires.</p>"""
        eeat_link = "https://www.immd.gov.hk/eng/services/visas/visit-transit/visit-visa-entry-permit.html"
        eeat_text = "immd.gov.hk"

    else:
        # Visa required (immd.gov.hk)
        description = (
            f"{label} passport holders need a visa to enter Hong Kong in 2026. "
            f"Apply through immd.gov.hk. Updated March 2026."
        )
        status_cell = '<span style="color:red;font-weight:600;">Visa Required</span>'
        faq = f"""[{{"@type":"Question","name":"Do {label} citizens need a visa for Hong Kong?","acceptedAnswer":{{"@type":"Answer","text":"Yes. {label} passport holders must obtain a Hong Kong visit visa before travelling. Applications are made through the Hong Kong Immigration Department at immd.gov.hk."}}}},
      {{"@type":"Question","name":"How do {label} citizens apply for a Hong Kong visa?","acceptedAnswer":{{"@type":"Answer","text":"{label} citizens should apply for a Hong Kong visit visa through the Hong Kong Immigration Department online portal at immd.gov.hk, or through the nearest Chinese consulate or visa office."}}}},
      {{"@type":"Question","name":"How long does Hong Kong visa processing take?","acceptedAnswer":{{"@type":"Answer","text":"Processing times vary. Applying online through immd.gov.hk typically takes several weeks. Apply well in advance of your travel date."}}}}]"""
        key_table = f"""<table class="table table-bordered table-sm mt-3 mb-4">
<thead><tr><th colspan="2" class="table-dark">Key Facts — Hong Kong for {label} Citizens</th></tr></thead>
<tbody>
<tr><th>Visa Required</th><td>{status_cell}</td></tr>
<tr><th>Visa Type</th><td>Hong Kong Visit Visa</td></tr>
<tr><th>Apply At</th><td>immd.gov.hk</td></tr>
<tr><th>Max Stay</th><td>As endorsed on visa</td></tr>
<tr><th>Processing</th><td>Several weeks (apply early)</td></tr>
</tbody>
</table>"""
        body_content = f"""<h2>Hong Kong Visa for {label} Citizens</h2>
<p>{label} passport holders must obtain a <strong>Hong Kong visit visa</strong> before travelling. Applications are handled by the Hong Kong Immigration Department (IMMD). Apply through the online portal at <a href="https://www.immd.gov.hk" target="_blank" rel="noopener">immd.gov.hk</a> or through the nearest Chinese diplomatic mission.</p>

<h2>Visa Application Details</h2>
<ul>
<li>Apply at: <a href="https://www.immd.gov.hk/eng/services/visas/visit-transit/visit-visa-entry-permit.html" target="_blank" rel="noopener">immd.gov.hk</a></li>
<li>Processing: Several weeks — apply early</li>
<li>Stay: As endorsed on visa</li>
<li>Alternatively apply at the nearest Chinese consulate/visa office</li>
</ul>

<h2>How to Apply</h2>
<ol>
<li>Visit <a href="https://www.immd.gov.hk" target="_blank" rel="noopener">immd.gov.hk</a> and navigate to the visit visa/entry permit section.</li>
<li>Complete the application form (ID 1000A or online equivalent).</li>
<li>Prepare supporting documents (see below).</li>
<li>Submit application and pay the visa fee.</li>
<li>Await approval — processing takes several weeks.</li>
</ol>

<h2>Required Documents</h2>
<ul>
<li>Valid {label} passport (6+ months validity)</li>
<li>Completed visa application form</li>
<li>Recent passport-sized photographs</li>
<li>Proof of accommodation in Hong Kong</li>
<li>Return/onward travel ticket</li>
<li>Bank statements showing sufficient funds</li>
<li>Travel itinerary</li>
<li>Employment letter or business registration (if applicable)</li>
</ul>"""
        eeat_link = "https://www.immd.gov.hk/eng/services/visas/visit-transit/visit-visa-entry-permit.html"
        eeat_text = "immd.gov.hk"

    faq_json = f"""    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq}}}
    </script>"""

    related = f"""<div class="related-guides mt-5 pt-4 border-top">
    <h3 class="h5 mb-3">Related Visa Guides</h3>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-hong-kong.html">Hong Kong Visa Overview</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="hong-kong-visa-requirements.html">HK Requirements</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="hong-kong-visa-fees.html">HK Fees</a>
    <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="hong-kong-visa-processing-time.html">HK Processing Times</a>
    <a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &rarr;</a>
</div>"""

    html = "\n".join([
        head(title, description, canonical, flag_code),
        faq_json,
        favicon_and_close_head(),
        navbar(canonical),
        "",
        "<section class=\"ftco-section\">",
        "<div class=\"container\">",
        "<article class=\"country-page\">",
        "",
        f"<h1>{title}</h1>",
        "",
        key_table,
        "",
        body_content,
        "",
        f"""<div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
    <strong>Editorial Team &mdash; eVisa-Card.com</strong>
    <p class="mb-0 small">Last updated: <strong>March 2026</strong>. Always verify current requirements at <a href="{eeat_link}" target="_blank" rel="noopener">{eeat_text}</a> before travel.</p>
</div>""",
        "",
        related,
        "",
        "</article>",
        "</div>",
        "</section>",
        "",
        footer_and_scripts(),
    ])
    return filename, html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for slug, label, flag_code, adj in NATIONALITIES:
        # New Zealand
        nz_filename, nz_html = build_nz_page(slug, label, flag_code, adj)
        nz_path = os.path.join(OUT_DIR, nz_filename)
        with open(nz_path, "w", encoding="utf-8") as f:
            f.write(nz_html)
        created.append(nz_filename)
        print(f"  Created: {nz_filename}")

        # Hong Kong
        hk_filename, hk_html = build_hk_page(slug, label, flag_code, adj)
        hk_path = os.path.join(OUT_DIR, hk_filename)
        with open(hk_path, "w", encoding="utf-8") as f:
            f.write(hk_html)
        created.append(hk_filename)
        print(f"  Created: {hk_filename}")

    print(f"\nDone. {len(created)} files created in {OUT_DIR}")
    return created


if __name__ == "__main__":
    main()
