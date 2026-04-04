#!/usr/bin/env python3
"""Add Open Graph tags to EN expat guide pages."""
import os, re

EN_DIR = r"C:\Users\chemi\Documents\evisa\pacific-main\www\en"

# Country-specific OG data
OG_DATA = {
    "thailand": {
        "title": "Complete Expat Guide Thailand 2026 — Live, Work & Retire in Thailand",
        "description": "Complete guide to living in Thailand as an expat in 2026. Visa options, residency, healthcare, supplementary insurance, bank accounts and property buying for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-thailand.html",
    },
    "japan": {
        "title": "Complete Expat Guide Japan 2026 — Live, Work & Retire in Japan",
        "description": "Complete guide to living in Japan as an expat in 2026. Visa options, residency, healthcare, insurance, bank accounts and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-japan.html",
    },
    "vietnam": {
        "title": "Complete Expat Guide Vietnam 2026 — Live, Work & Retire in Vietnam",
        "description": "Complete guide to living in Vietnam as an expat in 2026. Visa options, residency, healthcare, insurance, bank accounts and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-vietnam.html",
    },
    "malaysia": {
        "title": "Complete Expat Guide Malaysia 2026 — Live, Work & Retire in Malaysia",
        "description": "Complete guide to living in Malaysia as an expat in 2026. MM2H visa, residency, healthcare, insurance, bank accounts and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-malaysia.html",
    },
    "cambodia": {
        "title": "Complete Expat Guide Cambodia 2026 — Live, Work & Retire in Cambodia",
        "description": "Complete guide to living in Cambodia as an expat in 2026. Visa options, residency, healthcare, insurance, bank accounts and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-cambodia.html",
    },
    "laos": {
        "title": "Complete Expat Guide Laos 2026 — Live, Work & Retire in Laos",
        "description": "Complete guide to living in Laos as an expat in 2026. Visa options, residency, healthcare, insurance, bank accounts and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-laos.html",
    },
    "georgia": {
        "title": "Complete Expat Guide Georgia 2026 — Live, Work & Retire in Georgia",
        "description": "Complete guide to living in Georgia as an expat in 2026. Visa-free 365-day stay, residency, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-georgia.html",
    },
    "greece": {
        "title": "Complete Expat Guide Greece 2026 — Live, Work & Retire in Greece",
        "description": "Complete guide to living in Greece as an expat in 2026. Golden Visa, digital nomad visa, residency, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-greece.html",
    },
    "spain": {
        "title": "Complete Expat Guide Spain 2026 — Live, Work & Retire in Spain",
        "description": "Complete guide to living in Spain as an expat in 2026. Digital Nomad Visa, Non-Lucrative Visa, residency, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-spain.html",
    },
    "portugal": {
        "title": "Complete Expat Guide Portugal 2026 — Live, Work & Retire in Portugal",
        "description": "Complete guide to living in Portugal as an expat in 2026. D7 Visa, NHR tax benefits, residency, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-portugal.html",
    },
    "mexico": {
        "title": "Complete Expat Guide Mexico 2026 — Live, Work & Retire in Mexico",
        "description": "Complete guide to living in Mexico as an expat in 2026. Temporary Resident Visa, residency, healthcare, insurance, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-mexico.html",
    },
    "colombia": {
        "title": "Complete Expat Guide Colombia 2026 — Live, Work & Retire in Colombia",
        "description": "Complete guide to living in Colombia as an expat in 2026. Pensioner Visa, residency, healthcare, insurance, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-colombia.html",
    },
    "costa-rica": {
        "title": "Complete Expat Guide Costa Rica 2026 — Live, Work & Retire in Costa Rica",
        "description": "Complete guide to living in Costa Rica as an expat in 2026. Pensionado Visa, residency, healthcare, insurance, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-costa-rica.html",
    },
    "panama": {
        "title": "Complete Expat Guide Panama 2026 — Live, Work & Retire in Panama",
        "description": "Complete guide to living in Panama as an expat in 2026. Pensionado Visa, Friendly Nations Visa, residency, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-panama.html",
    },
    "paraguay": {
        "title": "Complete Expat Guide Paraguay 2026 — Live, Work & Retire in Paraguay",
        "description": "Complete guide to living in Paraguay as an expat in 2026. Permanent residency, tax benefits, healthcare, banking and property for foreigners.",
        "url": "https://www.evisa-card.com/en/expat-guide-paraguay.html",
    },
    "uae": {
        "title": "Complete Expat Guide UAE 2026 — Live, Work & Retire in Dubai & UAE",
        "description": "Complete guide to living in the UAE as an expat in 2026. Golden Visa, work permits, residency, healthcare, banking and property for foreigners in Dubai and Abu Dhabi.",
        "url": "https://www.evisa-card.com/en/expat-guide-uae.html",
    },
}

OG_IMAGE = "https://www.evisa-card.com/images/og-image.jpg"

count = 0
for country, data in OG_DATA.items():
    fpath = os.path.join(EN_DIR, f"expat-guide-{country}.html")
    if not os.path.exists(fpath):
        print(f"  SKIP: {fpath} not found")
        continue

    with open(fpath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    if "og:title" in html:
        continue  # already has OG tags

    og_tags = f"""
    <!-- Open Graph -->
    <meta property="og:title" content="{data['title']}"/>
    <meta property="og:description" content="{data['description']}"/>
    <meta property="og:type" content="article"/>
    <meta property="og:url" content="{data['url']}"/>
    <meta property="og:image" content="{OG_IMAGE}"/>"""

    # Insert before </head>
    new_html = html.replace("</head>", og_tags + "\n</head>", 1)

    if new_html != html:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)
        count += 1
        print(f"  OK expat-guide-{country}.html")

print(f"\nAdded OG tags to {count} expat guide pages.")
