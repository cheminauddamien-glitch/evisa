#!/usr/bin/env python3
"""
1. Add country flag to each card in destination.html
2. Fix navbar mobile grey -> dark navy
3. Fix scrolled navbar grey -> dark navy
"""
import re

# --- Country flag ISO codes ---
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

# --- 1. Fix destination.html cards ---
with open("C:/Users/chemi/Documents/evisa/pacific-main/www/destination.html", "r", encoding="utf-8") as f:
    html = f.read()

def add_flag_to_card(match):
    card_html = match.group(0)
    # Get slug from href
    slug_m = re.search(r'/en/visa-([a-z0-9-]+)\.html', card_html)
    if not slug_m:
        return card_html
    slug = slug_m.group(1)
    iso = FLAG_CODES.get(slug)
    if not iso:
        return card_html
    # Already has flag?
    if f'fi fi-{iso}' in card_html:
        return card_html
    # Add flag before country name in h3
    flag_span = f'<span class="fi fi-{iso}" style="margin-right:5px;"></span>'
    card_html = re.sub(
        r'(<h3><a href="[^"]+">)([^<]+)(</a></h3>)',
        lambda m: m.group(1) + flag_span + m.group(2) + m.group(3),
        card_html
    )
    return card_html

html_new = re.sub(
    r'<div class="col-md-3 col-sm-6 ftco-animate">.*?</div>\s*</div>\s*</div>',
    add_flag_to_card,
    html,
    flags=re.DOTALL
)

with open("C:/Users/chemi/Documents/evisa/pacific-main/www/destination.html", "w", encoding="utf-8") as f:
    f.write(html_new)

# Verify flags added
flags_in_cards = re.findall(r'fi fi-[a-z]{2}', html_new)
# Remove lang switcher flags (gb, fr, es, br appear multiple times in nav)
print(f"Flags in destination.html: {len(flags_in_cards)}")
print("Sample:", flags_in_cards[:10])


# --- 2. Fix style.css navbar colors ---
with open("C:/Users/chemi/Documents/evisa/pacific-main/www/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

DARK_NAV = "#1d2d50"  # dark navy
WHITE = "#ffffff"

# Append overrides at end of CSS
overrides = f"""

/* ========== NAVBAR MOBILE & SCROLL FIX ========== */

/* Mobile navbar: dark navy instead of grey */
@media (max-width: 991.98px) {{
  .ftco-navbar-light {{
    background: {DARK_NAV} !important;
  }}
  .ftco-navbar-light .navbar-brand {{
    color: {WHITE} !important;
  }}
  .ftco-navbar-light .navbar-nav > .nav-item > .nav-link {{
    color: {WHITE} !important;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-top: 10px !important;
    padding-bottom: 10px !important;
  }}
  .ftco-navbar-light .navbar-nav > .nav-item > .nav-link:hover {{
    color: #f15d30 !important;
  }}
  .ftco-navbar-light .navbar-toggler {{
    border-color: rgba(255,255,255,0.5) !important;
    color: {WHITE} !important;
  }}
  .ftco-navbar-light .navbar-toggler-icon {{
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(255,255,255,0.8)' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e") !important;
  }}
  .ftco-navbar-light .navbar-collapse {{
    background: {DARK_NAV};
    padding: 0 15px 15px;
  }}
  .ftco-navbar-light .dropdown-menu {{
    background: #162040 !important;
    border: none;
  }}
  .ftco-navbar-light .dropdown-item {{
    color: {WHITE} !important;
  }}
  .ftco-navbar-light .dropdown-item:hover {{
    background: rgba(255,255,255,0.1) !important;
  }}
}}

/* Scrolled navbar: dark navy instead of grey */
.ftco_navbar.scrolled {{
  background: {DARK_NAV} !important;
}}
.ftco_navbar.scrolled .ftco-navbar-light,
.ftco-navbar-light.scrolled {{
  background: {DARK_NAV} !important;
}}
.ftco-navbar-light.scrolled .navbar-nav > .nav-item > .nav-link {{
  color: {WHITE} !important;
}}
.ftco-navbar-light.scrolled .navbar-brand {{
  color: {WHITE} !important;
}}
.ftco-navbar-light.scrolled .navbar-nav > .nav-item.active > a {{
  color: #f15d30 !important;
}}

/* Destination card flags */
.col-md-3 .project-wrap h3 .fi {{
  vertical-align: middle;
  font-size: 13px !important;
  margin-right: 4px;
}}
"""

# Check if we already added this fix to avoid duplicating
if "NAVBAR MOBILE & SCROLL FIX" in css:
    # Remove old block and replace
    css = re.sub(r'/\* ={10,} NAVBAR MOBILE & SCROLL FIX.*', '', css, flags=re.DOTALL)

css_new = css + overrides

with open("C:/Users/chemi/Documents/evisa/pacific-main/www/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_new)

print("CSS navbar fixes applied.")
print("Done!")
