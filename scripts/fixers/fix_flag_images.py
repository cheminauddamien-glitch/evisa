#!/usr/bin/env python3
"""
Replace generic destination-X.jpg background images with real country flag images
using flagcdn.com (free, no API key needed).
Format: https://flagcdn.com/w640/{iso}.png
"""
import re

FLAG_CODES = {
    "india": "in", "thailand": "th", "japan": "jp", "china": "cn",
    "indonesia": "id", "malaysia": "my", "singapore": "sg", "philippines": "ph",
    "vietnam": "vn", "cambodia": "kh", "sri-lanka": "lk", "maldives": "mv",
    "nepal": "np", "turkey": "tr", "uae": "ae",
    "france": "fr", "germany": "de", "spain": "es", "italy": "it",
    "united-kingdom": "gb", "netherlands": "nl", "belgium": "be",
    "portugal": "pt", "greece": "gr", "switzerland": "ch", "austria": "at",
    "croatia": "hr", "czech-republic": "cz", "poland": "pl", "hungary": "hu",
    "sweden": "se", "norway": "no", "denmark": "dk", "ireland": "ie",
    "romania": "ro",
    "usa": "us", "canada": "ca", "mexico": "mx", "brazil": "br",
    "argentina": "ar", "colombia": "co", "costa-rica": "cr",
    "jordan": "jo", "qatar": "qa", "australia": "au", "new-zealand": "nz",
    "hong-kong": "hk", "taiwan": "tw",
}

CDN = "https://flagcdn.com/w640/{iso}.png"

with open("C:/Users/chemi/Documents/evisa/pacific-main/www/destination.html", "r", encoding="utf-8") as f:
    html = f.read()

def replace_card_image(match):
    card_html = match.group(0)
    slug_m = re.search(r'/en/visa-([a-z0-9-]+)\.html', card_html)
    if not slug_m:
        return card_html
    slug = slug_m.group(1)
    iso = FLAG_CODES.get(slug)
    if not iso:
        return card_html

    flag_url = CDN.format(iso=iso)

    # Replace background-image url
    card_html = re.sub(
        r'background-image: url\([^)]+\)',
        f'background-image: url({flag_url})',
        card_html
    )
    # Replace src= on the hidden img tag
    card_html = re.sub(
        r'src="images/destination-\d\.jpg"',
        f'src="{flag_url}"',
        card_html
    )
    # Update alt to include flag reference
    return card_html

html_new = re.sub(
    r'<div class="col-md-3 col-sm-6 ftco-animate">.*?</div>\s*</div>\s*</div>',
    replace_card_image,
    html,
    flags=re.DOTALL
)

# Also add CSS to make flag images display properly (contain, not cover)
# Flags are wide (2:1 ratio), so use contain with a colored bg
flag_css = """
<style>
/* Country flag cards */
.project-wrap .img {
    background-size: contain !important;
    background-repeat: no-repeat !important;
    background-position: center center !important;
    background-color: #f0f2f5 !important;
}
</style>
"""

# Insert before </head>
html_new = html_new.replace("</head>", flag_css + "</head>", 1)

with open("C:/Users/chemi/Documents/evisa/pacific-main/www/destination.html", "w", encoding="utf-8") as f:
    f.write(html_new)

# Verify
flag_urls = re.findall(r'flagcdn\.com/w640/([a-z]+)\.png', html_new)
print(f"Cards updated with flag images: {len(set(flag_urls))}")
print("Countries:", sorted(set(flag_urls)))
