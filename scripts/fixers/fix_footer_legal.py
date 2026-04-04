#!/usr/bin/env python3
"""
1. Add Legal Notice + Disclaimer links to footer on all pages
2. Create legal-notice.html and disclaimer.html pages
"""
import os, re, glob

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# Footer links per language
LEGAL_LINKS = {
    "en": ('Legal Notice', '/en/legal-notice.html', 'Disclaimer', '/en/disclaimer.html'),
    "fr": ('Mentions légales', '/fr/mentions-legales.html', 'Disclaimer', '/fr/disclaimer.html'),
    "es": ('Aviso Legal', '/es/aviso-legal.html', 'Disclaimer', '/es/disclaimer.html'),
    "pt": ('Aviso Legal', '/pt/aviso-legal.html', 'Disclaimer', '/pt/disclaimer.html'),
    "root": ('Legal Notice', '/en/legal-notice.html', 'Disclaimer', '/en/disclaimer.html'),
}

COPYRIGHT = {
    "en": "© 2026 eVisa-Card.com — Global eVisa & Travel Information Platform",
    "fr": "© 2026 eVisa-Card.com — Plateforme mondiale d'information sur les eVisas",
    "es": "© 2026 eVisa-Card.com — Plataforma global de información sobre eVisas",
    "pt": "© 2026 eVisa-Card.com — Plataforma global de informações sobre eVisas",
    "root": "© 2026 eVisa-Card.com — Global eVisa & Travel Information Platform",
}

def new_footer_p(lang, img_prefix):
    l1, u1, l2, u2 = LEGAL_LINKS[lang]
    copy = COPYRIGHT[lang]
    return f'''<p class="mt-4">{copy}</p>
                    <p class="mt-2" style="font-size:13px;">
                        <a href="{u1}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l1}</a>
                        &nbsp;|&nbsp;
                        <a href="{u2}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{l2}</a>
                    </p>'''

def fix_footer(html, lang, img_prefix):
    # Replace copyright line + add legal links
    # Pattern: <p class="mt-4">© ...</p>
    old_p = re.search(r'<p class="mt-4"[^>]*>.*?©.*?</p>', html, re.DOTALL)
    if old_p:
        # Replace old copyright with new copyright + legal links
        html = html[:old_p.start()] + new_footer_p(lang, img_prefix) + html[old_p.end():]
    else:
        # Insert before </footer>
        insert = new_footer_p(lang, img_prefix)
        html = html.replace('</footer>', insert + '\n    </footer>', 1)
    return html

# Fix all pages
fixed = 0
errors = 0
for lang in ["en", "fr", "es", "pt"]:
    for fpath in glob.glob(os.path.join(WWW, lang, "*.html")):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                html = f.read()
            # Skip if already has legal links
            if 'legal-notice' in html or 'mentions-legales' in html or 'aviso-legal' in html:
                continue
            html = fix_footer(html, lang, "../")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            fixed += 1
        except Exception as e:
            print(f"ERR {fpath}: {e}")
            errors += 1

# Fix root pages
for fpath in glob.glob(os.path.join(WWW, "*.html")):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        if 'legal-notice' in html or 'mentions-legales' in html:
            continue
        html = fix_footer(html, "root", "")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        fixed += 1
    except Exception as e:
        print(f"ERR {fpath}: {e}")
        errors += 1

print(f"Footer fixed: {fixed} pages | Errors: {errors}")


# ── Create Legal Notice page ─────────────────────────────────────────────
legal_notice = '''<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>Legal Notice | eVisa-Card.com</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="robots" content="noindex, follow"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/legal-notice.html"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">Guides</a></li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container" style="max-width:860px;margin:60px auto;padding:0 20px;">
    <h1 style="margin-bottom:30px;">Legal Notice</h1>

    <h2>Website Publisher</h2>
    <p>eVisa-Card.com is an independent informational website providing travel visa guidance for international travelers.</p>
    <ul>
        <li><strong>Website:</strong> https://www.evisa-card.com</li>
        <li><strong>Contact:</strong> <a href="mailto:contact@evisa-card.com">contact@evisa-card.com</a></li>
    </ul>

    <h2>Hosting</h2>
    <p>This website is hosted by a third-party hosting provider. For hosting details, contact us at the email above.</p>

    <h2>Intellectual Property</h2>
    <p>All content published on eVisa-Card.com — including text, graphics, logos, and data — is the exclusive property of eVisa-Card.com or its content partners, and is protected by applicable intellectual property laws.</p>
    <p>Reproduction, distribution, or use of any content without prior written permission is strictly prohibited.</p>

    <h2>Data & Privacy</h2>
    <p>eVisa-Card.com uses Google Analytics (GA4) to collect anonymous traffic statistics. No personal data is sold or shared with third parties for marketing purposes. For more details, refer to <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google's Privacy Policy</a>.</p>
    <p>This site uses Google AdSense to display advertisements. AdSense may use cookies to show relevant ads based on your browsing history.</p>

    <h2>External Links</h2>
    <p>eVisa-Card.com may contain links to external websites. We are not responsible for the content or privacy practices of those sites.</p>

    <h2>Applicable Law</h2>
    <p>This legal notice is governed by applicable law. Any disputes shall be subject to the exclusive jurisdiction of the competent courts.</p>

    <p style="color:#999;font-size:13px;margin-top:40px;">Last updated: March 2026</p>
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">© 2026 eVisa-Card.com — Global eVisa & Travel Information Platform</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/en/legal-notice.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/en/disclaimer.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>'''

with open(os.path.join(WWW, "en", "legal-notice.html"), "w", encoding="utf-8") as f:
    f.write(legal_notice)
print("Created: en/legal-notice.html")


# ── Create Disclaimer page ───────────────────────────────────────────────
disclaimer = '''<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>Disclaimer | eVisa-Card.com</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="robots" content="noindex, follow"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link rel="canonical" href="https://www.evisa-card.com/en/disclaimer.html"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="../index.html">eVisa-Card<span>.com</span></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">Destinations</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/retirement-visa-guide.html">Guides</a></li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container" style="max-width:860px;margin:60px auto;padding:0 20px;">
    <h1 style="margin-bottom:30px;">Disclaimer</h1>

    <h2>Informational Purpose Only</h2>
    <p>The information provided on eVisa-Card.com is for <strong>general informational purposes only</strong>. It does not constitute legal advice, immigration advice, or any other professional advice.</p>

    <h2>Accuracy of Information</h2>
    <p>While we strive to keep all visa and travel information accurate and up to date, <strong>visa regulations, fees, and entry requirements change frequently</strong>. eVisa-Card.com cannot guarantee the completeness, accuracy, or timeliness of the information provided.</p>
    <p>Always verify the latest requirements with:</p>
    <ul>
        <li>The official embassy or consulate of your destination country</li>
        <li>The official government immigration portal of the destination country</li>
        <li>Your airline or travel agent</li>
    </ul>

    <h2>No Liability</h2>
    <p>eVisa-Card.com shall not be held liable for any loss, damage, or inconvenience arising from reliance on information published on this website. Use of this site is entirely at your own risk.</p>

    <h2>Affiliate & Advertising Disclosure</h2>
    <p>This website displays advertisements via Google AdSense. Some links may be affiliate links. We may receive compensation if you click on certain links or make purchases through them. This does not influence our editorial content.</p>

    <h2>No Visa Application Service</h2>
    <p>eVisa-Card.com does <strong>not</strong> process visa applications, issue visas, or act as a travel agency. All official visa applications must be submitted through the relevant government authority.</p>

    <p style="color:#999;font-size:13px;margin-top:40px;">Last updated: March 2026</p>
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">© 2026 eVisa-Card.com — Global eVisa & Travel Information Platform</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/en/legal-notice.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Legal Notice</a>
                    &nbsp;|&nbsp;
                    <a href="/en/disclaimer.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>'''

with open(os.path.join(WWW, "en", "disclaimer.html"), "w", encoding="utf-8") as f:
    f.write(disclaimer)
print("Created: en/disclaimer.html")
