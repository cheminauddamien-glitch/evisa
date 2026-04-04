#!/usr/bin/env python3
"""SEO optimization: fix truncated meta descriptions & add keywords to expat guides."""
import os, re

EN_DIR = r"C:\Users\chemi\Documents\evisa\pacific-main\www\en"

# ── 1. Proper meta descriptions for visa pages with truncated content ──────────
VISA_DESCRIPTIONS = {
    "andorra": "Andorra visa requirements 2026. Enter via France or Spain (Schengen visa required). No border controls, no stamp. Visa-free for EU/Schengen citizens.",
    "bahamas": "Bahamas visa requirements 2026. Visa-free for most nationalities up to 8 months. Entry by air or cruise. No eVisa — stamp on arrival at Nassau or Freeport.",
    "bahrain": "Bahrain visa requirements 2026. eVisa available for 180+ nationalities. 14-day tourist visa or 1-month multiple-entry. Apply online at evisa.gov.bh.",
    "belize": "Belize visa requirements 2026. Visa-free for most nationalities for 30 days, extendable to 6 months. Entry via Philip Goldson International Airport, Belize City.",
    "bermuda": "Bermuda visa requirements 2026. Visa-free for most nationalities for 90 days. Entry by air or cruise ship only. No land border. British Overseas Territory.",
    "bhutan": "Bhutan visa requirements 2026. Sustainable Development Fee (SDF) $100/day for most nationalities. Visa required, apply through licensed Bhutanese tour operator.",
    "brunei": "Brunei visa requirements 2026. Visa-free for citizens of 60+ countries for 14–30 days. eVisa available for others at imigresen.gov.bn. Strict Islamic laws apply.",
    "bulgaria": "Bulgaria visa requirements 2026. EU member, not full Schengen. Visa-free for EU/EEA/US/UK/Canadian citizens. Others need a Bulgarian or Schengen visa.",
    "cape-verde": "Cape Verde visa requirements 2026. EASE digital pre-registration required for all visitors. Visa-on-arrival at all airports. €25 tourist fee. No pre-arranged visa needed.",
    "chile": "Chile visa requirements 2026. Visa-free for 90 days for citizens of 90+ countries. No eVisa system — stamp on arrival. PDI electronic declaration required at entry.",
    "cook-islands": "Cook Islands visa requirements 2026. Visa-free for all nationalities for up to 31 days, extendable to 6 months. Onward ticket required. Small Pacific paradise.",
    "cyprus": "Cyprus visa requirements 2026. EU member, not in Schengen. Visa-free for EU/EEA citizens. Others need a Cyprus visa. eVisa available at moi.gov.cy.",
    "ecuador": "Ecuador visa requirements 2026. Visa-free for citizens of 100+ countries for 90 days per 12-month period. Includes Galapagos Islands. No eVisa system.",
    "egypt": "Egypt visa requirements 2026. eVisa available online at visa2egypt.gov.eg ($25). Visa on arrival for most nationalities ($25). Sinai-only entry available for day trips.",
    "finland": "Finland visa requirements 2026. Schengen Area member. Visa-free for EU/EEA citizens. Others need a Schengen visa (up to 90 days/180). Finland eVisa not available.",
    "georgia": "Georgia visa requirements 2026. Visa-free for citizens of 95+ countries for 365 days. No eVisa needed for eligible nationalities. Apply for e-visa at evisa.gov.ge.",
    "guatemala": "Guatemala visa requirements 2026. Visa-free for citizens of 60+ countries for 90 days (extendable). Part of CA-4 region with Honduras, El Salvador, Nicaragua.",
    "iceland": "Iceland visa requirements 2026. Schengen Area member. Visa-free for EU/EEA/US/UK citizens. 90 days in any 180-day period. No Iceland eVisa — apply for Schengen visa.",
    "iran": "Iran visa requirements 2026. Most nationalities require a visa. eVisa (e-Visa) available at evisa.mfa.ir. Visa on arrival at Tehran IKA airport for eligible nationals.",
    "iraq": "Iraq visa requirements 2026. Most nationalities require a visa in advance. Kurdistan Region (Erbil, Sulaymaniyah) offers visa on arrival for 30+ nationalities.",
    "israel": "Israel visa requirements 2026. Visa-free for citizens of 100+ countries for 90 days. Entry requirements may change. No eVisa — stamp on arrival. ETA announced.",
    "kuwait": "Kuwait visa requirements 2026. eVisa available for eligible nationalities at evisa.moi.gov.kw. GCC residents may apply online. Visa on arrival not widely available.",
    "laos": "Laos visa requirements 2026. eVisa available at laoevisa.gov.la ($35). Visa on arrival at major border crossings ($35). 30-day single-entry for most nationalities.",
    "macau": "Macau visa requirements 2026. Separate visa policy from mainland China. Visa-free for most nationalities for 30–90 days. No visa needed from Zhuhai land border for most.",
    "moldova": "Moldova visa requirements 2026. Visa-free for EU/EEA, US, UK citizens for 90 days. eVisa available for other nationalities at evisa.gov.md. Part of Eastern Europe.",
    "nicaragua": "Nicaragua visa requirements 2026. Visa-free for citizens of Western countries for 90 days (CA-4 region). $10 tourist fee on arrival. Part of Central America-4 free movement zone.",
    "oman": "Oman visa requirements 2026. eVisa available for 70+ nationalities at evisa.rop.gov.om ($20). Visa on arrival for GCC holders. 10-day, 30-day and 1-year visa options.",
    "panama": "Panama visa requirements 2026. Visa-free for citizens of 60+ countries for 90 days. No eVisa system. Onward ticket and proof of funds required at entry.",
    "peru": "Peru visa requirements 2026. Visa-free for citizens of 80+ countries for 90–183 days. Home to Machu Picchu and Amazon. No eVisa — immigration card on arrival.",
    "samoa": "Samoa visa requirements 2026. Visa-free for most nationalities for 60 days. ETA (Entry Permit on Arrival) at Faleolo Airport. Extension possible to 90 days.",
    "saudi-arabia": "Saudi Arabia visa requirements 2026. Tourist eVisa at visa.visitsaudi.com ($122). Visa on arrival at major airports. Multiple-entry 1-year visa for tourism.",
    "south-korea": "South Korea visa requirements 2026. Visa-free for 100+ nationalities for 30–90 days. K-ETA required for visa-free travelers ($10). Apply at k-eta.go.kr.",
    "uruguay": "Uruguay visa requirements 2026. Visa-free for citizens of most countries for 90 days per 180-day period. No eVisa — stamp on arrival at Carrasco International Airport.",
    "venezuela": "Venezuela visa requirements 2026. Most nationalities require a visa in advance from a Venezuelan embassy. Political situation affects entry. Check travel advisories.",
}

# ── 2. Keywords for EN expat guide pages ──────────────────────────────────────
EXPAT_KEYWORDS = {
    "thailand": "expat guide thailand 2026, live in thailand, retire in thailand, thailand visa expat, cost of living thailand, thailand healthcare expat",
    "japan": "expat guide japan 2026, live in japan, retire in japan, japan visa expat, cost of living japan, japan healthcare expat",
    "vietnam": "expat guide vietnam 2026, live in vietnam, retire in vietnam, vietnam visa expat, cost of living vietnam, vietnam healthcare expat",
    "malaysia": "expat guide malaysia 2026, live in malaysia, retire in malaysia, malaysia visa expat, cost of living malaysia, MM2H visa",
    "cambodia": "expat guide cambodia 2026, live in cambodia, retire in cambodia, cambodia visa expat, cost of living cambodia, cambodia healthcare",
    "laos": "expat guide laos 2026, live in laos, retire in laos, laos visa expat, cost of living laos, vientiane expat",
    "georgia": "expat guide georgia 2026, live in georgia, retire in georgia, georgia visa expat, cost of living tbilisi, georgia digital nomad",
    "greece": "expat guide greece 2026, live in greece, retire in greece, greece golden visa, cost of living greece, digital nomad visa greece",
    "spain": "expat guide spain 2026, live in spain, retire in spain, spain digital nomad visa, cost of living spain, non lucrative visa spain",
    "portugal": "expat guide portugal 2026, live in portugal, retire in portugal, portugal d7 visa, NHR tax regime, cost of living lisbon",
    "mexico": "expat guide mexico 2026, live in mexico, retire in mexico, mexico temporary resident visa, cost of living mexico city, expat community mexico",
    "colombia": "expat guide colombia 2026, live in colombia, retire in colombia, colombia pensioner visa, cost of living medellin, digital nomad colombia",
    "costa-rica": "expat guide costa rica 2026, live in costa rica, retire in costa rica, pensionado visa costa rica, cost of living costa rica",
    "panama": "expat guide panama 2026, live in panama, retire in panama, pensionado visa panama, cost of living panama city, friendly nations visa",
    "paraguay": "expat guide paraguay 2026, live in paraguay, retire in paraguay, paraguay permanent residency, cost of living asuncion, tax benefits paraguay",
    "uae": "expat guide uae 2026, live in dubai, work in uae, uae golden visa, cost of living dubai, expat community dubai",
}

def fix_visa_descriptions():
    """Replace truncated meta descriptions in visa pages."""
    count = 0
    for country, new_desc in VISA_DESCRIPTIONS.items():
        fpath = os.path.join(EN_DIR, f"visa-{country}.html")
        if not os.path.exists(fpath):
            print(f"  SKIP: {fpath} not found")
            continue
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Replace truncated description
        new_html = re.sub(
            r'(<meta\s+(?:content|name)="description"[^>]*content="|<meta\s+name="description"\s+content=")[^"]*\.\.\."',
            lambda m: m.group(0).rsplit('"', 1)[0].replace(m.group(0).split('"')[-2 if m.group(0).count('"') > 2 else -1], '') + f'"{new_desc}"',
            html
        )
        # Simpler approach: direct regex replacement
        new_html = re.sub(
            r'(<meta[^>]*name="description"[^>]*content=")[^"]*\.\.\."',
            lambda m: m.group(1) + new_desc + '"',
            html
        )
        # Also update OG description
        new_html = re.sub(
            r'(<meta[^>]*property="og:description"[^>]*content=")[^"]*\.\.\."',
            lambda m: m.group(1) + new_desc + '"',
            new_html
        )

        if new_html != html:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_html)
            count += 1
            print(f"  OK visa-{country}.html")
    print(f"Fixed {count} visa page descriptions\n")

def add_expat_keywords():
    """Add keywords meta tag to EN expat guide pages."""
    count = 0
    for country, keywords in EXPAT_KEYWORDS.items():
        fpath = os.path.join(EN_DIR, f"expat-guide-{country}.html")
        if not os.path.exists(fpath):
            print(f"  SKIP: {fpath} not found")
            continue
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Skip if keywords already present
        if 'name="keywords"' in html:
            continue

        # Insert keywords after description meta tag
        keywords_tag = f'\n    <meta name="keywords" content="{keywords}"/>'
        new_html = re.sub(
            r'(<meta name="description"[^/]*/?>)',
            r'\1' + keywords_tag,
            html,
            count=1
        )

        if new_html != html:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_html)
            count += 1
            print(f"  OK expat-guide-{country}.html")
    print(f"Added keywords to {count} expat guide pages\n")

def add_robots_to_expat():
    """Add robots meta and Open Graph tags to expat guide pages that are missing them."""
    count = 0
    for country in EXPAT_KEYWORDS:
        fpath = os.path.join(EN_DIR, f"expat-guide-{country}.html")
        if not os.path.exists(fpath):
            continue
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()

        changed = False
        # Add robots meta if missing
        if 'name="robots"' not in html:
            robots_tag = '\n    <meta name="robots" content="index, follow"/>'
            new_html = re.sub(
                r'(<meta name="keywords"[^/]*/?>)',
                r'\1' + robots_tag,
                html, count=1
            )
            if new_html != html:
                html = new_html
                changed = True

        if changed:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
    print(f"Added robots meta to {count} expat guide pages\n")

if __name__ == "__main__":
    print("=== Fixing truncated visa meta descriptions ===")
    fix_visa_descriptions()

    print("=== Adding keywords to expat guide pages ===")
    add_expat_keywords()

    print("=== Adding robots meta to expat guides ===")
    add_robots_to_expat()

    print("SEO optimization complete.")
