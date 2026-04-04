#!/usr/bin/env python
"""
add_prearrival_registrations.py
Adds mandatory pre-arrival digital registration info to visa country pages in www/en/.
Idempotent — skips pages that already have the registration alert.
"""

import os
import re

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "en")

# ──────────────────────────────────────────────────────────────────
# Pre-arrival registration data
# ──────────────────────────────────────────────────────────────────
PREARRIVAL = {
    # AMERICAS
    "usa": {
        "name": "ESTA (Electronic System for Travel Authorization)",
        "short_name": "ESTA",
        "mandatory_for": "All VWP country nationals (42 countries including EU, UK, Australia, Japan)",
        "url": "https://esta.cbp.dhs.gov",
        "details": "Must be approved BEFORE boarding flight to USA. $21 fee. Valid 2 years. Required even for transit.",
        "timing": "Apply at least 72 hours before departure",
    },
    "canada": {
        "name": "eTA (Electronic Travel Authorization)",
        "short_name": "eTA",
        "mandatory_for": "All visa-exempt foreign nationals flying to Canada (except US citizens)",
        "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html",
        "details": "Required before boarding flight to Canada. CAD $7 fee. Valid 5 years or until passport expires.",
        "timing": "Apply before booking flight — usually approved within minutes",
    },
    "cuba": {
        "name": "D'Viajeros Health Declaration",
        "short_name": "D'Viajeros",
        "mandatory_for": "All travelers",
        "url": "https://www.dviajeros.mitrans.gob.cu",
        "details": "Online health and customs declaration. Free. Must be completed before arrival.",
        "timing": "Within 72 hours before arrival",
    },

    # EUROPE
    "united-kingdom": {
        "name": "UK Electronic Travel Authorisation (ETA)",
        "short_name": "UK ETA",
        "mandatory_for": "Non-visa nationals from Gulf states, Jordan, and expanding to all visa-exempt nationals in 2025-2026",
        "url": "https://www.gov.uk/guidance/apply-for-an-electronic-travel-authorisation-eta",
        "details": "\u00a310 fee. Valid 2 years. Required before travel. Linked to passport biometrically.",
        "timing": "Apply before travel — processing within 3 working days",
    },

    # ASIA-PACIFIC
    "australia": {
        "name": "ETA (Electronic Travel Authority) / eVisitor",
        "short_name": "ETA / eVisitor",
        "mandatory_for": "All visitors — ETA for eligible passport holders, eVisitor for EU/EEA nationals",
        "url": "https://www.eta.homeaffairs.gov.au",
        "details": "ETA: AUD $20 via app. eVisitor: free. Both valid 12 months, 90-day stays. Must be approved before travel.",
        "timing": "Apply before travel — usually approved within 12 hours",
    },
    "new-zealand": {
        "name": "NZeTA (New Zealand Electronic Travel Authority)",
        "short_name": "NZeTA",
        "mandatory_for": "All visa-waiver travelers and cruise ship passengers",
        "url": "https://www.immigration.govt.nz/new-zealand-visas/visas/visa/nzeta",
        "details": "NZD $17 (app) or $23 (web) + IVL levy $35. Valid 2 years. Required before boarding.",
        "timing": "Apply at least 72 hours before departure",
    },
    "india": {
        "name": "e-Visa (Electronic Visa)",
        "short_name": "e-Visa",
        "mandatory_for": "Citizens of 160+ countries — must apply online before travel (no visa on arrival)",
        "url": "https://indianvisaonline.gov.in",
        "details": "e-Tourist: $10-25 (30 days) or $25-40 (1-5 years). Processing 72 hours. Print ETA confirmation.",
        "timing": "Apply at least 4 days before travel",
    },
    "sri-lanka": {
        "name": "ETA (Electronic Travel Authorization)",
        "short_name": "Sri Lanka ETA",
        "mandatory_for": "All visitors except citizens of Singapore, Maldives, and Seychelles",
        "url": "https://www.srilankaevisa.lk",
        "details": "Free for tourism (since 2024). Must be approved before arrival. Valid 30 days, extendable to 90.",
        "timing": "Apply before travel — processed within 24-48 hours",
    },
    "cambodia": {
        "name": "e-Visa",
        "short_name": "Cambodia e-Visa",
        "mandatory_for": "Most nationalities (alternative to Visa on Arrival at airport only)",
        "url": "https://www.evisa.gov.kh",
        "details": "$36 fee (eVisa) vs $30 (VOA at airport). eVisa valid for single entry, 30 days. Recommended to avoid queues.",
        "timing": "Apply at least 3 business days before travel",
    },
    "myanmar": {
        "name": "e-Visa",
        "short_name": "Myanmar e-Visa",
        "mandatory_for": "Most nationalities — no visa on arrival for most",
        "url": "https://evisa.moip.gov.mm",
        "details": "$50 tourist eVisa. 28 days. Must be approved before travel. Print approval letter.",
        "timing": "Apply at least 5 business days before departure",
    },
    "singapore": {
        "name": "SG Arrival Card (SGAC)",
        "short_name": "SG Arrival Card",
        "mandatory_for": "All foreign travelers entering Singapore",
        "url": "https://eservices.ica.gov.sg/sgarrivalcard",
        "details": "Free. Electronic arrival card replacing paper form. Must submit within 3 days before arrival.",
        "timing": "Submit within 3 days before arrival",
    },
    "south-korea": {
        "name": "K-ETA (Korea Electronic Travel Authorization)",
        "short_name": "K-ETA",
        "mandatory_for": "Currently SUSPENDED for 22 countries until Dec 2025. Check before travel.",
        "url": "https://www.k-eta.go.kr",
        "details": "When active: KRW 10,000 (~$7). Valid 2 years. Currently suspended for most visa-free nationals.",
        "timing": "When required: apply at least 24 hours before departure",
    },
    "japan": {
        "name": "Visit Japan Web",
        "short_name": "Visit Japan Web",
        "mandatory_for": "All travelers — online customs and immigration declaration",
        "url": "https://www.vjw.digital.go.jp",
        "details": "Free. Combines immigration, customs and quarantine forms. Optional but strongly recommended — speeds up arrival.",
        "timing": "Complete before arrival for faster processing",
    },
    "malaysia": {
        "name": "MDAC (Malaysia Digital Arrival Card)",
        "short_name": "MDAC",
        "mandatory_for": "All foreign travelers entering Malaysia",
        "url": "https://imigresen-online.imi.gov.my/mdac/main",
        "details": "Free. Digital arrival card replacing paper form. Must be completed before arrival.",
        "timing": "Submit within 3 days before arrival",
    },

    # MIDDLE EAST & AFRICA
    "turkey": {
        "name": "e-Visa",
        "short_name": "Turkey e-Visa",
        "mandatory_for": "Citizens of 100+ countries — must apply online or at embassy",
        "url": "https://www.evisa.gov.tr",
        "details": "$50 for most nationalities. Single/multiple entry. 30-90 days depending on nationality. Instant approval.",
        "timing": "Apply before travel — instant processing online",
    },
    "uae": {
        "name": "ICP Smart Services (Entry Permit / e-Visa)",
        "short_name": "UAE e-Visa",
        "mandatory_for": "Nationalities not eligible for visa-free or visa-on-arrival entry",
        "url": "https://smartservices.icp.gov.ae",
        "details": "Various e-visa types. Tourist visa AED 300 (~$82). 30-60 days. Many nationalities get visa-free entry.",
        "timing": "Apply before travel if visa required",
    },
    "qatar": {
        "name": "Hayya Card / eVisa",
        "short_name": "Qatar eVisa",
        "mandatory_for": "Nationalities not eligible for visa-free entry (80+ countries are visa-free)",
        "url": "https://www.moi.gov.qa",
        "details": "Visa-free for 80+ countries (30 days). Others need eVisa via MOI portal or Hayya platform.",
        "timing": "Apply before travel",
    },
    "jordan": {
        "name": "Jordan Pass (recommended) / eVisa",
        "short_name": "Jordan Pass",
        "mandatory_for": "Most nationalities need visa — Jordan Pass includes visa + attractions",
        "url": "https://www.jordanpass.jo",
        "details": "Jordan Pass: JOD 70-80 (~$99-113) includes visa fee + Petra entry + 40 attractions. VOA also available at airport ($56).",
        "timing": "Purchase Jordan Pass before travel for best value",
    },
    "kenya": {
        "name": "eTA (Electronic Travel Authorization)",
        "short_name": "Kenya eTA",
        "mandatory_for": "All visitors — eTA replaced eVisa in 2024",
        "url": "https://www.etakenya.go.ke",
        "details": "$30 fee. Valid for 90 days. Single entry. Replaced previous eVisa system in January 2024.",
        "timing": "Apply at least 72 hours before travel",
    },
    "ethiopia": {
        "name": "e-Visa",
        "short_name": "Ethiopia e-Visa",
        "mandatory_for": "All visitors",
        "url": "https://www.evisa.gov.et",
        "details": "$82 single entry (30 days) or $102 (90 days). Must be approved before arrival.",
        "timing": "Apply at least 3 business days before travel",
    },

    # ISLAND NATIONS
    "maldives": {
        "name": "Traveller Declaration (IMUGA)",
        "short_name": "IMUGA Declaration",
        "mandatory_for": "All travelers entering or departing Maldives",
        "url": "https://imuga.immigration.gov.mv",
        "details": "Free. Online health and travel declaration. Visa-free for all nationalities (30 days) but IMUGA is mandatory.",
        "timing": "Submit within 96 hours before arrival",
    },
}

# Schengen/EU countries that should get the ETIAS informational note
SCHENGEN_COUNTRIES = [
    "austria", "belgium", "bulgaria", "croatia", "czech-republic",
    "denmark", "finland", "france", "germany", "greece", "hungary",
    "iceland", "italy", "liechtenstein", "luxembourg", "netherlands",
    "norway", "poland", "portugal", "romania", "slovakia", "slovenia",
    "spain", "sweden", "switzerland",
]

# Countries to SKIP (already done manually)
SKIP_COUNTRIES = {"thailand"}


def build_alert_html(info):
    """Build the orange mandatory alert block."""
    return (
        '<div class="visa-alert visa-alert-mandatory" style="background:#fff3e0;border-left:4px solid #ff9800;padding:16px 20px;border-radius:8px;margin:16px 0 12px;">\n'
        '    <div style="display:flex;align-items:center;gap:12px;">\n'
        '        <span style="font-size:28px;">\u26a0\ufe0f</span>\n'
        '        <div>\n'
        f'            <strong style="font-size:16px;color:#e65100;">Mandatory: {info["name"]}</strong>\n'
        f'            <p style="margin:4px 0 0;font-size:14px;color:#333;">{info["details"]} Required for: {info["mandatory_for"]}.</p>\n'
        f'            <p style="margin:4px 0 0;font-size:13px;color:#666;"><strong>When:</strong> {info["timing"]}</p>\n'
        f'            <a href="{info["url"]}" target="_blank" rel="noopener" style="display:inline-block;margin-top:6px;color:#e65100;font-weight:600;text-decoration:underline;font-size:14px;">Register Now \u2192</a>\n'
        '        </div>\n'
        '    </div>\n'
        '</div>\n'
    )


def build_etias_info_html():
    """Build the blue informational ETIAS note for Schengen/EU pages."""
    return (
        '<div class="visa-alert visa-alert-info-etias" style="background:#e3f2fd;border-left:4px solid #2196f3;padding:16px 20px;border-radius:8px;margin:16px 0 12px;">\n'
        '    <div style="display:flex;align-items:center;gap:12px;">\n'
        '        <span style="font-size:28px;">\u2139\ufe0f</span>\n'
        '        <div>\n'
        '            <strong style="font-size:16px;color:#0d47a1;">Upcoming: ETIAS (European Travel Information and Authorisation System)</strong>\n'
        '            <p style="margin:4px 0 0;font-size:14px;color:#333;">ETIAS will be required for visa-exempt non-EU nationals visiting Schengen countries (expected 2025-2026). \u20ac7 fee, valid 3 years. Not yet mandatory — check <a href="https://travel-europe.europa.eu/etias_en" target="_blank" rel="noopener" style="color:#0d47a1;font-weight:600;">official ETIAS site</a> for launch date.</p>\n'
        '            <p style="margin:4px 0 0;font-size:13px;color:#666;"><strong>Status:</strong> Not yet in effect. No action required at this time.</p>\n'
        '        </div>\n'
        '    </div>\n'
        '</div>\n'
    )


def build_table_row(info):
    """Build the Key Facts table row."""
    short = info.get("short_name", info["name"])
    return (
        f'<tr style="background:#fff3e0;"><th>\u26a0\ufe0f {short}</th>'
        f'<td><strong>Mandatory</strong> \u2014 {info["timing"]}. '
        f'<a href="{info["url"]}" target="_blank" rel="noopener">Register here</a></td></tr>\n'
    )


def build_etias_table_row():
    """Build the ETIAS informational Key Facts table row."""
    return (
        '<tr style="background:#e3f2fd;"><th>\u2139\ufe0f ETIAS (upcoming)</th>'
        '<td><strong>Not yet mandatory</strong> \u2014 Expected 2025-2026 for visa-exempt non-EU nationals. '
        '<a href="https://travel-europe.europa.eu/etias_en" target="_blank" rel="noopener">Check status</a></td></tr>\n'
    )


def find_insertion_point_after_h1_and_alerts(content):
    """
    Find the position right after the <h1>...</h1> tag and any subsequent
    visa-alert blocks. We insert our new alert after all existing alerts.
    """
    # Find the closing </h1> or end of h1 line
    # The h1 may be on a single line or span multiple lines
    h1_match = re.search(r'<h1[^>]*>.*?</h1>', content, re.DOTALL)
    if not h1_match:
        return None

    pos = h1_match.end()

    # Now skip past any existing visa-alert blocks that follow
    # Look for consecutive visa-alert divs after the h1
    while True:
        # Skip whitespace/newlines
        remaining = content[pos:]
        ws_match = re.match(r'\s*', remaining)
        if ws_match:
            check_pos = pos + ws_match.end()
        else:
            check_pos = pos

        # Check if next thing is a visa-alert div
        remaining = content[check_pos:]
        if remaining.startswith('<div class="visa-alert'):
            # Find the end of this div block — need to handle nested divs
            depth = 0
            i = 0
            while i < len(remaining):
                if remaining[i:].startswith('<div'):
                    depth += 1
                    i += 4
                elif remaining[i:].startswith('</div>'):
                    depth -= 1
                    i += 6
                    if depth == 0:
                        pos = check_pos + i
                        break
                else:
                    i += 1
            else:
                # Couldn't find matching close — bail
                break
        else:
            # No more visa-alert blocks
            pos = check_pos
            break

    return pos


def find_tbody_insertion_point(content):
    """
    Find the position right after the first <tbody> in the Key Facts table.
    Returns the position right after '<tbody>' (or '<tbody>\n').
    """
    # Find the Key Facts table header first
    key_facts_match = re.search(r'Key Facts', content)
    if not key_facts_match:
        return None

    # Find the <tbody> after the Key Facts header
    tbody_match = re.search(r'<tbody>\s*\n?', content[key_facts_match.start():])
    if not tbody_match:
        return None

    return key_facts_match.start() + tbody_match.end()


def process_country(country_key, info):
    """Process a single country page. Returns (status, message)."""
    filename = f"visa-{country_key}.html"
    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.isfile(filepath):
        return "skipped", f"{filename} not found"

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Idempotency check — look for our specific alert class or the registration name
    if 'visa-alert-mandatory' in content and info["name"] in content:
        return "already_present", f"{filename}: '{info['name']}' already present"

    # For the specific registration name check (looser match)
    short = info.get("short_name", info["name"])
    if f'visa-alert-mandatory' in content and short in content:
        return "already_present", f"{filename}: '{short}' already present"

    modified = False
    alert_html = build_alert_html(info)
    table_row = build_table_row(info)

    # ── Insert alert block after h1 and existing alerts ──
    insertion_pos = find_insertion_point_after_h1_and_alerts(content)
    if insertion_pos is not None:
        # Add a newline before if needed
        prefix = "\n" if content[insertion_pos - 1:insertion_pos] != "\n" else ""
        content = content[:insertion_pos] + prefix + alert_html + content[insertion_pos:]
        modified = True
    else:
        return "error", f"{filename}: could not find <h1> tag"

    # ── Insert table row as first row in Key Facts tbody ──
    tbody_pos = find_tbody_insertion_point(content)
    if tbody_pos is not None:
        content = content[:tbody_pos] + table_row + content[tbody_pos:]
        modified = True
    else:
        # Some pages (like Myanmar compact pages) don't have a Key Facts table — that's OK
        pass

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return "updated", f"{filename}: added '{info['name']}'"

    return "no_change", f"{filename}: no changes made"


def process_etias_country(country_key):
    """Add ETIAS informational note to a Schengen/EU country page."""
    filename = f"visa-{country_key}.html"
    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.isfile(filepath):
        return "skipped", f"{filename} not found"

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Idempotency check
    if 'visa-alert-info-etias' in content:
        return "already_present", f"{filename}: ETIAS note already present"

    modified = False
    etias_html = build_etias_info_html()
    etias_row = build_etias_table_row()

    # ── Insert ETIAS info block after h1 and existing alerts ──
    insertion_pos = find_insertion_point_after_h1_and_alerts(content)
    if insertion_pos is not None:
        prefix = "\n" if content[insertion_pos - 1:insertion_pos] != "\n" else ""
        content = content[:insertion_pos] + prefix + etias_html + content[insertion_pos:]
        modified = True
    else:
        return "error", f"{filename}: could not find <h1> tag"

    # ── Insert ETIAS table row as first row in Key Facts tbody ──
    tbody_pos = find_tbody_insertion_point(content)
    if tbody_pos is not None:
        content = content[:tbody_pos] + etias_row + content[tbody_pos:]
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return "updated", f"{filename}: added ETIAS informational note"

    return "no_change", f"{filename}: no changes made"


def main():
    print("=" * 70)
    print("Pre-Arrival Digital Registration — Bulk Updater")
    print("=" * 70)
    print(f"Base directory: {BASE_DIR}\n")

    stats = {"updated": 0, "skipped": 0, "already_present": 0, "error": 0}

    # ── Process mandatory pre-arrival countries ──
    print("--- Mandatory Pre-Arrival Registrations ---\n")
    for country_key, info in PREARRIVAL.items():
        if country_key in SKIP_COUNTRIES:
            print(f"  SKIP     {country_key}: already done manually")
            stats["skipped"] += 1
            continue

        status, msg = process_country(country_key, info)
        label = status.upper().ljust(10)
        print(f"  {label} {msg}")
        stats[status] = stats.get(status, 0) + 1

    # ── Process Schengen/EU countries for ETIAS note ──
    print("\n--- ETIAS Informational Notes (Schengen/EU) ---\n")
    for country_key in SCHENGEN_COUNTRIES:
        status, msg = process_etias_country(country_key)
        label = status.upper().ljust(10)
        print(f"  {label} {msg}")
        stats[status] = stats.get(status, 0) + 1

    # ── Summary ──
    print("\n" + "=" * 70)
    print("Summary:")
    print(f"  Updated:         {stats.get('updated', 0)}")
    print(f"  Already present: {stats.get('already_present', 0)}")
    print(f"  Skipped:         {stats.get('skipped', 0)}")
    print(f"  Errors:          {stats.get('error', 0)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
