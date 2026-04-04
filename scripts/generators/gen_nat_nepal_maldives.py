#!/usr/bin/env python3
"""
Generate 40 HTML pages:
  - nepal-visa-for-{nat}-citizens.html   (20 nationalities)
  - maldives-visa-for-{nat}-citizens.html (20 nationalities)
Output directory: www/en/
"""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "www", "en")

# ---------------------------------------------------------------------------
# Nationality data
# ---------------------------------------------------------------------------

NATIONALITIES = [
    # (slug, adjective, country-name, flag-code, demonym-for-title)
    ("us",           "American",       "the United States", "us",  "US"),
    ("uk",           "British",        "the United Kingdom", "gb",  "UK"),
    ("canadian",     "Canadian",       "Canada",             "ca",  "Canadian"),
    ("french",       "French",         "France",             "fr",  "French"),
    ("german",       "German",         "Germany",            "de",  "German"),
    ("japanese",     "Japanese",       "Japan",              "jp",  "Japanese"),
    ("australian",   "Australian",     "Australia",          "au",  "Australian"),
    ("indian",       "Indian",         "India",              "in",  "Indian"),
    ("chinese",      "Chinese",        "China",              "cn",  "Chinese"),
    ("russian",      "Russian",        "Russia",             "ru",  "Russian"),
    ("brazilian",    "Brazilian",      "Brazil",             "br",  "Brazilian"),
    ("mexican",      "Mexican",        "Mexico",             "mx",  "Mexican"),
    ("south-african","South African",  "South Africa",       "za",  "South African"),
    ("nigerian",     "Nigerian",       "Nigeria",            "ng",  "Nigerian"),
    ("korean",       "South Korean",   "South Korea",        "kr",  "Korean"),
    ("singaporean",  "Singaporean",    "Singapore",          "sg",  "Singaporean"),
    ("indonesian",   "Indonesian",     "Indonesia",          "id",  "Indonesian"),
    ("philippine",   "Philippine",     "the Philippines",    "ph",  "Philippine"),
    ("turkish",      "Turkish",        "Turkey",             "tr",  "Turkish"),
    ("argentinian",  "Argentinian",    "Argentina",          "ar",  "Argentinian"),
]

# ---------------------------------------------------------------------------
# Nepal visa status
# ---------------------------------------------------------------------------
# VoL + eVisa: everyone except indian
# indian: visa-free (SAARC)

NEPAL_VOL_NATS = {
    "us", "uk", "canadian", "french", "german", "japanese", "australian",
    "korean", "singaporean", "russian", "brazilian", "mexican",
    "south-african", "nigerian", "turkish", "argentinian",
    "chinese", "indonesian", "philippine",
}
NEPAL_FREE_NATS = {"indian"}

# ---------------------------------------------------------------------------
# Maldives: free 30-day on arrival for ALL
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def nav(current_file):
    return f"""<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
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
            <span class="fi fi-gb"></span> English</a>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
            <a class="dropdown-item active" href="/en/{current_file}"><span class="fi fi-gb"></span> English</a>
            <a class="dropdown-item" href="/destination.html"><span class="fi fi-fr"></span> Fran&#231;ais</a>
            <a class="dropdown-item" href="/destination.html"><span class="fi fi-es"></span> Espa&#241;ol</a>
            <a class="dropdown-item" href="/destination.html"><span class="fi fi-br"></span> Portugu&#234;s</a>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>"""


def footer():
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
        <p class="mt-4">&#169; 2026 eVisa-Card.com &#8212; Global eVisa &amp; Travel Information Platform</p>
      </div>
    </div>
  </div>
</footer>"""


def loader_and_scripts():
    return """<div class="show fullscreen" id="ftco-loader">
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
<script src="../js/main.js"></script>"""


# ---------------------------------------------------------------------------
# Nepal page builders
# ---------------------------------------------------------------------------

def nepal_vol_page(nat_slug, adj, country_name, flag_code, title_dem):
    """Visa on Arrival + eVisa page for Nepal."""
    filename = f"nepal-visa-for-{nat_slug}-citizens.html"
    canon_slug = filename[:-5]  # strip .html
    page_title = f"Nepal Visa for {title_dem} Citizens 2026"
    meta_desc = (
        f"{adj} passport holders visiting Nepal in 2026: Visa on Arrival (USD 30 / 50 / 125) "
        f"or eVisa at immigration.gov.np. Requirements, fees, and how to apply. Updated March 2026."
    )
    faq_json = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        f'{{"@type":"Question","name":"Do {adj} citizens need a visa for Nepal?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"{adj} passport holders can obtain a Nepal Visa on Arrival at Tribhuvan International Airport or major border crossings. Fees: USD 30 (15 days), USD 50 (30 days), USD 125 (90 days). eVisa is also available at immigration.gov.np."}}}},'
        f'{{"@type":"Question","name":"How much does a Nepal Visa on Arrival cost for {adj} citizens?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"USD 30 for 15 days, USD 50 for 30 days, or USD 125 for 90 days. Payment accepted in major currencies or by card at the airport."}}}},'
        f'{{"@type":"Question","name":"Can {adj} citizens apply for a Nepal eVisa?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"Yes. Apply online at immigration.gov.np before travel. The eVisa fee matches the VoA fee: USD 30 (15 days), USD 50 (30 days), USD 125 (90 days)."}}}}'
        ']}'
    )

    related = "\n      ".join([
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="maldives-visa-for-' + nat_slug + '-citizens.html">Maldives Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="thailand-visa-for-' + nat_slug + '-citizens.html">Thailand Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="vietnam-visa-for-' + nat_slug + '-citizens.html">Vietnam Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#x2192;</a>',
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <title>{page_title}</title>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canon_slug}"/>
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
{nav(filename)}

<section class="ftco-section">
  <div class="container">
    <article class="country-page">

      <h1><span class="fi fi-np mr-2"></span> {page_title}</h1>

      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &#8212; Nepal for {title_dem} Citizens</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td><span style="color:orange;font-weight:600;">Visa on Arrival / eVisa</span></td></tr>
          <tr><th>Visa Type</th><td>Tourist Visa on Arrival or eVisa</td></tr>
          <tr><th>Fee</th><td>USD 30 (15 days) &bull; USD 50 (30 days) &bull; USD 125 (90 days)</td></tr>
          <tr><th>Max Stay</th><td>Up to 90 days per visit</td></tr>
          <tr><th>Entries</th><td>Single (multiple-entry available on request)</td></tr>
          <tr><th>eVisa Portal</th><td><a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a></td></tr>
          <tr><th>Passport Validity</th><td>At least 6 months beyond stay</td></tr>
        </tbody>
      </table>

      <h2>Does a <span class="fi fi-{flag_code}"></span> {adj} Citizen Need a Visa for Nepal?</h2>
      <p>{adj} passport holders require a visa to visit Nepal. The easiest options are the <strong>Visa on Arrival (VoA)</strong> available at Tribhuvan International Airport (Kathmandu) and major land border crossings, or the <strong>Nepal eVisa</strong> applied for online at <a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a> before departure.</p>

      <h2>Nepal Visa Fees for {title_dem} Citizens</h2>
      <table class="table table-bordered table-sm mb-4">
        <thead><tr><th>Duration</th><th>Fee (USD)</th></tr></thead>
        <tbody>
          <tr><td>15 days</td><td><strong>USD 30</strong></td></tr>
          <tr><td>30 days</td><td><strong>USD 50</strong></td></tr>
          <tr><td>90 days</td><td><strong>USD 125</strong></td></tr>
        </tbody>
      </table>
      <p>Payment is accepted in US Dollars, Euros, British Pounds, and other major currencies, or by credit/debit card at the Visa on Arrival counter.</p>

      <h2>How to Apply &#8212; Nepal eVisa (Recommended)</h2>
      <ol>
        <li>Visit <a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a> and click <strong>Apply for Nepal Visa</strong>.</li>
        <li>Fill in your passport details, travel dates, and entry point.</li>
        <li>Upload a recent passport-size photo and the bio-data page of your passport.</li>
        <li>Pay the visa fee online (USD 30 / 50 / 125 depending on duration).</li>
        <li>Print or save the approval letter and present it on arrival.</li>
      </ol>

      <h2>Visa on Arrival &#8212; Step by Step</h2>
      <ol>
        <li>On arrival at Tribhuvan International Airport, proceed to the Visa on Arrival counters (before immigration).</li>
        <li>Fill in the arrival card and visa application form (available at the counter).</li>
        <li>Submit passport, photo, and fee payment.</li>
        <li>Collect your visa sticker and proceed to immigration.</li>
      </ol>

      <h2>Required Documents</h2>
      <ul>
        <li>Valid passport (minimum 6 months validity beyond your stay)</li>
        <li>One recent passport-size photograph (white background)</li>
        <li>Completed visa application form</li>
        <li>Visa fee payment (USD 30 / 50 / 125 in cash or card)</li>
        <li>Return or onward travel ticket</li>
        <li>Proof of accommodation in Nepal</li>
      </ul>

      <h2>Permitted Activities on a Nepal Tourist Visa</h2>
      <ul>
        <li>Trekking (Everest Base Camp, Annapurna Circuit, Langtang, etc.)</li>
        <li>Tourism and sightseeing (Kathmandu Valley, Pokhara, Chitwan)</li>
        <li>Mountaineering (separate climbing permit required)</li>
        <li>Short-term yoga or meditation courses</li>
      </ul>

      <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
        <div class="d-flex align-items-start">
          <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
          <div>
            <strong>Editorial Team &#8212; eVisa-Card.com</strong>
            <p class="mb-1 small text-muted">Last updated: <strong>March 2026</strong>.</p>
            <p class="mb-0 small"><strong>Important:</strong> Visa rules can change. Always verify current requirements at <a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a> or the Nepal Embassy in {country_name} before travel. This page is for informational purposes only.</p>
          </div>
        </div>
      </div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Visa Guides</h3>
      <div>
      {related}
      </div>
    </div>
  </div>
</section>

{footer()}

{loader_and_scripts()}
</body>
</html>
"""


def nepal_free_page(nat_slug, adj, country_name, flag_code, title_dem):
    """Visa-free (SAARC) page for Nepal &#8212; Indian citizens."""
    filename = f"nepal-visa-for-{nat_slug}-citizens.html"
    canon_slug = filename[:-5]
    page_title = f"Nepal Visa for {title_dem} Citizens 2026"
    meta_desc = (
        f"{adj} passport holders do not need a visa for Nepal. "
        f"Indian citizens can enter Nepal visa-free using a valid passport or national ID. "
        f"Complete guide updated March 2026."
    )
    faq_json = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        f'{{"@type":"Question","name":"Do {adj} citizens need a visa for Nepal?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"{adj} citizens do not need a visa for Nepal. India and Nepal share a special bilateral agreement under which Indian nationals can enter Nepal freely using a valid passport or Indian national identity card (Voter ID, Aadhaar, etc.)."}}}},'
        f'{{"@type":"Question","name":"Can {adj} citizens use a national ID to enter Nepal?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"Yes. Indian nationals may enter Nepal with a valid Indian passport OR an official government-issued photo ID such as a Voter ID card, Aadhaar card, or driving licence. A passport is recommended for a smoother experience."}}}},'
        f'{{"@type":"Question","name":"How long can {adj} citizens stay in Nepal?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"There is no fixed limit for Indian citizens. The Nepal-India Treaty of Peace and Friendship allows unrestricted stay, though registering with local authorities for long stays is advisable."}}}}'
        ']}'
    )

    related = "\n      ".join([
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="maldives-visa-for-' + nat_slug + '-citizens.html">Maldives Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="thailand-visa-for-' + nat_slug + '-citizens.html">Thailand Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="vietnam-visa-for-' + nat_slug + '-citizens.html">Vietnam Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#x2192;</a>',
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <title>{page_title}</title>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canon_slug}"/>
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
{nav(filename)}

<section class="ftco-section">
  <div class="container">
    <article class="country-page">

      <h1><span class="fi fi-np mr-2"></span> {page_title}</h1>

      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &#8212; Nepal for {title_dem} Citizens</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">&#10003; Visa-Free (SAARC)</span></td></tr>
          <tr><th>Allowed Stay</th><td>Unrestricted (bilateral treaty)</td></tr>
          <tr><th>Fee</th><td>Free</td></tr>
          <tr><th>Document Required</th><td>Valid Indian passport <em>or</em> national ID card</td></tr>
          <tr><th>Entry Points</th><td>All official border crossings and Tribhuvan Airport</td></tr>
          <tr><th>Treaty Basis</th><td>Nepal&#8211;India Treaty of Peace and Friendship 1950</td></tr>
        </tbody>
      </table>

      <h2>Do <span class="fi fi-{flag_code}"></span> Indian Citizens Need a Visa for Nepal?</h2>
      <p>Indian citizens do <strong>not</strong> need a visa to enter Nepal. Under the <strong>Nepal&#8211;India Treaty of Peace and Friendship (1950)</strong> and SAARC arrangements, Indian nationals enjoy unrestricted entry, residence, and the right to work in Nepal. No prior visa application is required.</p>

      <h2>What Documents Do Indian Citizens Need for Nepal?</h2>
      <p>Indian nationals may enter Nepal with <strong>either</strong> of the following documents:</p>
      <ul>
        <li><strong>Valid Indian Passport</strong> &#8212; recommended for the smoothest experience at immigration</li>
        <li><strong>Indian National ID Card</strong> &#8212; Voter ID (EPIC), Aadhaar card, driving licence, or other government-issued photo ID with name and photo</li>
      </ul>
      <p class="alert alert-info"><strong>Tip:</strong> A passport is strongly recommended if you plan to travel onward to Bhutan, Tibet, or other countries from Nepal. National IDs are only valid for entry into Nepal specifically.</p>

      <h2>Entry Points for Indian Citizens</h2>
      <ul>
        <li>Tribhuvan International Airport, Kathmandu (by air)</li>
        <li>Raxaul&#8211;Birgunj border crossing</li>
        <li>Sunauli&#8211;Bhairahawa border crossing</li>
        <li>Rupaidiha&#8211;Nautanwa border crossing</li>
        <li>Jogbani&#8211;Biratnagar border crossing</li>
        <li>All other official Nepal&#8211;India border crossings</li>
      </ul>

      <h2>Tips for Indian Travellers to Nepal</h2>
      <ul>
        <li>Indian currency (INR) is widely accepted in Nepal, but notes above INR 100 are not accepted &#8212; carry smaller denominations or use ATMs.</li>
        <li>Indian mobile SIM cards may not roam in Nepal &#8212; consider buying a local Nepali SIM on arrival.</li>
        <li>Nepal uses NPR (Nepali Rupee) &#8212; exchange rate is approximately NPR 1.60 per INR 1.</li>
        <li>Travel insurance is not mandatory but recommended for trekking activities.</li>
      </ul>

      <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
        <div class="d-flex align-items-start">
          <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
          <div>
            <strong>Editorial Team &#8212; eVisa-Card.com</strong>
            <p class="mb-1 small text-muted">Last updated: <strong>March 2026</strong>.</p>
            <p class="mb-0 small"><strong>Important:</strong> Visa rules can change. Always verify current requirements at <a href="https://immigration.gov.np" target="_blank" rel="noopener">immigration.gov.np</a> before travel. This page is for informational purposes only.</p>
          </div>
        </div>
      </div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Visa Guides</h3>
      <div>
      {related}
      </div>
    </div>
  </div>
</section>

{footer()}

{loader_and_scripts()}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Maldives page builder (free 30-day on arrival for all)
# ---------------------------------------------------------------------------

def maldives_free_page(nat_slug, adj, country_name, flag_code, title_dem):
    filename = f"maldives-visa-for-{nat_slug}-citizens.html"
    canon_slug = filename[:-5]
    page_title = f"Maldives Visa for {title_dem} Citizens 2026"
    meta_desc = (
        f"{adj} passport holders visiting the Maldives in 2026: free 30-day visa on arrival, "
        f"no prior application needed. Requirements and tips. Updated March 2026."
    )
    faq_json = (
        '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        f'{{"@type":"Question","name":"Do {adj} citizens need a visa for the Maldives?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"{adj} passport holders receive a free 30-day visa on arrival in the Maldives. No prior visa application is required. Simply arrive with a valid passport, onward ticket, and proof of accommodation."}}}},'
        f'{{"@type":"Question","name":"How long can {adj} citizens stay in the Maldives?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"Up to 30 days on arrival, free of charge. The stay can be extended to a total of 90 days by applying to the Maldives Immigration Department."}}}},'
        f'{{"@type":"Question","name":"What documents do {adj} citizens need for the Maldives?",'
        f'"acceptedAnswer":{{"@type":"Answer","text":"Valid passport (at least 1 month validity beyond stay), confirmed return or onward ticket, proof of accommodation (hotel booking or resort confirmation), and sufficient funds for the stay."}}}}'
        ']}'
    )

    related = "\n      ".join([
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="nepal-visa-for-' + nat_slug + '-citizens.html">Nepal Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="thailand-visa-for-' + nat_slug + '-citizens.html">Thailand Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="sri-lanka-visa-for-' + nat_slug + '-citizens.html">Sri Lanka Visa &mdash; ' + title_dem + ' Citizens</a>',
        '<a class="btn btn-primary btn-sm mb-2" href="../destination.html">All Destinations &#x2192;</a>',
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <title>{page_title}</title>
    <meta name="description" content="{meta_desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{canon_slug}"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{canon_slug}"/>
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
{nav(filename)}

<section class="ftco-section">
  <div class="container">
    <article class="country-page">

      <h1><span class="fi fi-mv mr-2"></span> {page_title}</h1>

      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">Key Facts &#8212; Maldives for {title_dem} Citizens</th></tr></thead>
        <tbody>
          <tr><th>Visa Required</th><td><span style="color:green;font-weight:600;">&#10003; Free Visa on Arrival</span></td></tr>
          <tr><th>Allowed Stay</th><td>30 days (extendable to 90 days)</td></tr>
          <tr><th>Fee</th><td>Free</td></tr>
          <tr><th>Processing Time</th><td>On arrival &#8212; immediate</td></tr>
          <tr><th>Entry Point</th><td>Velana International Airport (MLE) or any authorised port</td></tr>
          <tr><th>Passport Validity</th><td>At least 1 month beyond intended stay</td></tr>
        </tbody>
      </table>

      <h2>Do <span class="fi fi-{flag_code}"></span> {adj} Citizens Need a Visa for the Maldives?</h2>
      <p>{adj} passport holders do <strong>not</strong> need to apply for a visa before travelling to the Maldives. A <strong>free 30-day visa is granted on arrival</strong> to all nationalities at Velana International Airport and other authorised entry points. No prior application or approval is needed.</p>

      <h2>Entry Requirements for {title_dem} Citizens</h2>
      <ul>
        <li><strong>Valid passport</strong> &#8212; minimum 1 month validity beyond your intended departure date (6 months recommended)</li>
        <li><strong>Onward or return ticket</strong> &#8212; confirmed booking showing you will leave the Maldives</li>
        <li><strong>Proof of accommodation</strong> &#8212; hotel or resort confirmation, or a letter from a host</li>
        <li><strong>Sufficient funds</strong> &#8212; USD 100 per day (or equivalent) as a general guideline</li>
        <li>Immigration arrival/departure card (completed on the plane or at the airport)</li>
      </ul>

      <h2>Extending Your Stay Beyond 30 Days</h2>
      <p>The initial 30-day visa can be extended for a total maximum stay of <strong>90 days</strong>. To extend, apply at the <strong>Maldives Immigration Department</strong> (immi.gov.mv) before your current visa expires. An extension fee applies.</p>

      <h2>Tips for {title_dem} Travellers to the Maldives</h2>
      <ul>
        <li>The Maldives is an Islamic country &#8212; dress modestly when visiting inhabited local islands.</li>
        <li>Alcohol is only available at resort islands and licensed venues, not on local islands.</li>
        <li>The US Dollar (USD) is widely accepted alongside the Maldivian Rufiyaa (MVR).</li>
        <li>Book transfers from Velana Airport to your island resort in advance &#8212; speedboats and seaplanes fill up quickly.</li>
        <li>Travel insurance with water sports and medical evacuation coverage is strongly recommended.</li>
      </ul>

      <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
        <div class="d-flex align-items-start">
          <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
          <div>
            <strong>Editorial Team &#8212; eVisa-Card.com</strong>
            <p class="mb-1 small text-muted">Last updated: <strong>March 2026</strong>.</p>
            <p class="mb-0 small"><strong>Important:</strong> Visa rules can change. Always verify current requirements at <a href="https://immi.gov.mv" target="_blank" rel="noopener">immi.gov.mv</a> or the Maldives Embassy before travel. This page is for informational purposes only.</p>
          </div>
        </div>
      </div>

    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">Related Visa Guides</h3>
      <div>
      {related}
      </div>
    </div>
  </div>
</section>

{footer()}

{loader_and_scripts()}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    created = []

    for nat_slug, adj, country_name, flag_code, title_dem in NATIONALITIES:
        # --- Nepal ---
        if nat_slug in NEPAL_FREE_NATS:
            content = nepal_free_page(nat_slug, adj, country_name, flag_code, title_dem)
        else:
            content = nepal_vol_page(nat_slug, adj, country_name, flag_code, title_dem)

        nepal_path = os.path.join(OUT_DIR, f"nepal-visa-for-{nat_slug}-citizens.html")
        with open(nepal_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(nepal_path)

        # --- Maldives ---
        content = maldives_free_page(nat_slug, adj, country_name, flag_code, title_dem)
        maldives_path = os.path.join(OUT_DIR, f"maldives-visa-for-{nat_slug}-citizens.html")
        with open(maldives_path, "w", encoding="utf-8") as f:
            f.write(content)
        created.append(maldives_path)

    print(f"Generated {len(created)} files:")
    for p in created:
        print(f"  {os.path.basename(p)}")


if __name__ == "__main__":
    main()
