#!/usr/bin/env python3
"""
add_tax_exile_block.py
Add a Tax & Fiscal Exile block to all 16 x 10 = 160 expat guide pages.
Links to taxes-crypto.eu simulator with language-specific URLs.
"""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# taxes-crypto.eu simulator path per language
SIMULATOR_PATHS = {
    "fr": "simulateur-exil-fiscal",
    "en": "fiscal-exile-simulator",
    "es": "simulador-exilio-fiscal",
    "pt": "simulador-exilio-fiscal",
    # fallback to EN for unsupported languages
    "zh": "fiscal-exile-simulator",
    "th": "fiscal-exile-simulator",
    "ru": "fiscal-exile-simulator",
    "ar": "fiscal-exile-simulator",
    "ja": "fiscal-exile-simulator",
    "ko": "fiscal-exile-simulator",
}

# taxes-crypto.eu language prefix
SIMULATOR_LANG = {
    "fr": "fr", "en": "en", "es": "es", "pt": "pt",
    "zh": "en", "th": "en", "ru": "en", "ar": "en", "ja": "en", "ko": "en",
}

# Country slugs on taxes-crypto.eu (only those that have a dedicated page)
EXILE_SLUGS = {
    "thailand":   "thailand",
    "portugal":   "portugal",
    "spain":      "spain",
    "malaysia":   "malaysia",
    "uae":        "uae",
    "panama":     "panama",
    "greece":     "greece",
    "georgia":    "georgia",
    "paraguay":   "paraguay",
}

# Countries NOT in the simulator -> link to general simulator page
NO_EXILE_PAGE = ["mexico", "vietnam", "japan", "colombia", "costa-rica", "laos", "cambodia"]

# Tax data per country
TAX_DATA = {
    "thailand": {
        "tax_rate": "15%",
        "tax_label": "15% on crypto gains (since Jan 2024)",
        "crypto_score": "7/10",
        "regime": "Territorial",
        "exit_tax": "No",
        "highlights": [
            "15% flat tax on capital gains realized in Thailand",
            "No tax on gains from assets held before moving to Thailand",
            "LTR Visa holders: 17% flat income tax rate",
            "No inheritance tax under 100M THB",
        ],
    },
    "portugal": {
        "tax_rate": "28%",
        "tax_label": "28% CGT (0% if held > 365 days)",
        "crypto_score": "8/10",
        "regime": "NHR/IFICI",
        "exit_tax": "No",
        "highlights": [
            "0% capital gains tax if crypto held over 365 days",
            "NHR/IFICI regime: 20% flat tax on Portuguese-source income",
            "No exit tax on unrealized gains",
            "EU residency with full Schengen access",
        ],
    },
    "spain": {
        "tax_rate": "19-28%",
        "tax_label": "19-28% progressive CGT",
        "crypto_score": "5/10",
        "regime": "Beckham Law",
        "exit_tax": "Yes (> 4 years residency, > 4M assets)",
        "highlights": [
            "Beckham Law: 24% flat tax for first 6 years",
            "Progressive CGT: 19% (0-6k), 21% (6-50k), 23% (50-200k), 28% (200k+)",
            "Exit tax applies if resident > 4 years with > 4M in assets",
            "Modelo 720: mandatory declaration of foreign assets > 50k",
        ],
    },
    "mexico": {
        "tax_rate": "10-35%",
        "tax_label": "10% CGT (residents) or up to 35% income tax",
        "crypto_score": "5/10",
        "regime": "Territorial (partial)",
        "exit_tax": "No",
        "highlights": [
            "10% capital gains tax for tax residents",
            "No specific crypto regulation yet (treated as property)",
            "Double taxation treaties with 50+ countries",
            "No exit tax on unrealized capital gains",
        ],
    },
    "vietnam": {
        "tax_rate": "N/A",
        "tax_label": "Crypto legally unregulated (no tax framework)",
        "crypto_score": "4/10",
        "regime": "Undefined",
        "exit_tax": "No",
        "highlights": [
            "Crypto is not recognized as legal tender or asset",
            "No specific tax framework for cryptocurrency gains",
            "Government studying regulation (expected 2026-2027)",
            "Income tax up to 35% could theoretically apply",
        ],
    },
    "malaysia": {
        "tax_rate": "0%",
        "tax_label": "0% capital gains tax on crypto",
        "crypto_score": "8/10",
        "regime": "Territorial",
        "exit_tax": "No",
        "highlights": [
            "No capital gains tax on cryptocurrency",
            "Territorial tax system: foreign income not taxed",
            "MM2H visa provides long-term residency",
            "Well-regulated crypto market (Securities Commission)",
        ],
    },
    "japan": {
        "tax_rate": "15-55%",
        "tax_label": "15-55% (misc. income, progressive)",
        "crypto_score": "3/10",
        "regime": "Worldwide",
        "exit_tax": "Yes (> 100M JPY in assets)",
        "highlights": [
            "Crypto taxed as miscellaneous income (up to 55%)",
            "One of the highest crypto tax rates globally",
            "Exit tax on unrealized gains if assets > 100M JPY",
            "Reform discussions ongoing for flat 20% CGT on crypto",
        ],
    },
    "uae": {
        "tax_rate": "0%",
        "tax_label": "0% personal income tax, 0% CGT",
        "crypto_score": "10/10",
        "regime": "Zero tax",
        "exit_tax": "No",
        "highlights": [
            "Zero personal income tax and capital gains tax",
            "Dubai: VARA-regulated crypto hub",
            "Golden Visa: 10-year residency with property or investment",
            "Free zones with 100% foreign ownership",
        ],
    },
    "colombia": {
        "tax_rate": "10-15%",
        "tax_label": "10-15% CGT on crypto gains",
        "crypto_score": "5/10",
        "regime": "Worldwide",
        "exit_tax": "No",
        "highlights": [
            "10% CGT on gains up to 1,090 UVT, 15% above",
            "Crypto legally classified as intangible asset",
            "No exit tax on unrealized gains",
            "Digital nomad visa with favorable tax treatment",
        ],
    },
    "panama": {
        "tax_rate": "0%",
        "tax_label": "0% on foreign-source income (territorial)",
        "crypto_score": "9/10",
        "regime": "Territorial",
        "exit_tax": "No",
        "highlights": [
            "Territorial tax: 0% on foreign-source income",
            "Crypto gains from foreign exchanges are tax-free",
            "Pensionado visa: easy residency with $1,000/month pension",
            "Friendly Nations visa for 50+ qualifying countries",
        ],
    },
    "costa-rica": {
        "tax_rate": "0%",
        "tax_label": "0% on foreign-source income (territorial)",
        "crypto_score": "7/10",
        "regime": "Territorial",
        "exit_tax": "No",
        "highlights": [
            "Territorial tax: no tax on income earned outside Costa Rica",
            "Crypto gains from foreign platforms are tax-free",
            "No exit tax",
            "Stable democracy with strong rule of law",
        ],
    },
    "greece": {
        "tax_rate": "15%",
        "tax_label": "15% flat CGT on crypto",
        "crypto_score": "6/10",
        "regime": "Non-Dom available",
        "exit_tax": "No (proposed)",
        "highlights": [
            "15% flat capital gains tax on crypto",
            "Non-Dom regime: 100,000 EUR flat tax on worldwide income",
            "Golden Visa: residency with 250k-800k property investment",
            "EU/Schengen residency",
        ],
    },
    "georgia": {
        "tax_rate": "0%",
        "tax_label": "0% CGT for individuals",
        "crypto_score": "9/10",
        "regime": "Territorial + Small Business",
        "exit_tax": "No",
        "highlights": [
            "0% capital gains tax for individuals",
            "1% turnover tax for small businesses (< 500k GEL)",
            "Virtual Zone (IT): 0% corporate tax on foreign income",
            "365-day visa-free stay for 90+ nationalities",
        ],
    },
    "paraguay": {
        "tax_rate": "0%",
        "tax_label": "0% on foreign-source income (territorial)",
        "crypto_score": "8/10",
        "regime": "Territorial",
        "exit_tax": "No",
        "highlights": [
            "Territorial tax: 0% on foreign-source income",
            "Permanent residency with only $5,500 bank deposit",
            "10% flat tax on local income only",
            "Low cost of living and easy banking",
        ],
    },
    "laos": {
        "tax_rate": "N/A",
        "tax_label": "No crypto framework (income tax up to 25%)",
        "crypto_score": "2/10",
        "regime": "Undefined",
        "exit_tax": "No",
        "highlights": [
            "No specific cryptocurrency tax legislation",
            "General income tax rates: 0-25% progressive",
            "Limited banking and financial infrastructure",
            "Government exploring digital currency regulation",
        ],
    },
    "cambodia": {
        "tax_rate": "0-20%",
        "tax_label": "0-20% (limited enforcement on crypto)",
        "crypto_score": "5/10",
        "regime": "Territorial (de facto)",
        "exit_tax": "No",
        "highlights": [
            "USD-based economy, low tax enforcement on crypto",
            "20% capital gains tax exists but rarely enforced for crypto",
            "KHR and USD dual currency system",
            "Growing fintech ecosystem",
        ],
    },
}

# UI translations for the tax block
UI = {
    "en": {
        "section_title": "Tax & Fiscal Exile",
        "tax_overview": "Tax Overview",
        "tax_rate": "Capital Gains Tax",
        "regime": "Tax Regime",
        "crypto_score": "Crypto-Friendliness",
        "exit_tax": "Exit Tax",
        "key_points": "Key Tax Points",
        "cta_text": "Simulate Your Tax Savings",
        "cta_sub": "Use our free tax exile simulator to compare your tax savings in",
        "powered_by": "Powered by",
        "compare_text": "Compare tax rates across 27+ countries with our interactive simulator",
        "disclaimer": "Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.",
    },
    "fr": {
        "section_title": "Fiscalit\u00e9 & Exil Fiscal",
        "tax_overview": "Aper\u00e7u Fiscal",
        "tax_rate": "Imp\u00f4t sur les plus-values",
        "regime": "R\u00e9gime fiscal",
        "crypto_score": "Crypto-compatibilit\u00e9",
        "exit_tax": "Exit Tax",
        "key_points": "Points cl\u00e9s",
        "cta_text": "Simulez vos \u00e9conomies d'imp\u00f4ts",
        "cta_sub": "Utilisez notre simulateur gratuit d'exil fiscal pour comparer vos \u00e9conomies en",
        "powered_by": "Propuls\u00e9 par",
        "compare_text": "Comparez les taux d'imposition de 27+ pays avec notre simulateur interactif",
        "disclaimer": "Informations fiscales fournies \u00e0 titre indicatif uniquement. Consultez un conseiller fiscal qualifi\u00e9 avant toute d\u00e9cision de relocalisation.",
    },
    "es": {
        "section_title": "Fiscalidad & Exilio Fiscal",
        "tax_overview": "Resumen Fiscal",
        "tax_rate": "Impuesto sobre ganancias",
        "regime": "R\u00e9gimen fiscal",
        "crypto_score": "Cripto-compatibilidad",
        "exit_tax": "Exit Tax",
        "key_points": "Puntos clave",
        "cta_text": "Simule sus ahorros fiscales",
        "cta_sub": "Use nuestro simulador gratuito de exilio fiscal para comparar sus ahorros en",
        "powered_by": "Desarrollado por",
        "compare_text": "Compare tasas impositivas de 27+ pa\u00edses con nuestro simulador interactivo",
        "disclaimer": "Informaci\u00f3n fiscal proporcionada solo como orientaci\u00f3n general. Consulte a un asesor fiscal cualificado.",
    },
    "pt": {
        "section_title": "Fiscalidade & Ex\u00edlio Fiscal",
        "tax_overview": "Resumo Fiscal",
        "tax_rate": "Imposto sobre ganhos",
        "regime": "Regime fiscal",
        "crypto_score": "Cripto-compatibilidade",
        "exit_tax": "Exit Tax",
        "key_points": "Pontos-chave",
        "cta_text": "Simule suas economias fiscais",
        "cta_sub": "Use nosso simulador gratuito de ex\u00edlio fiscal para comparar suas economias em",
        "powered_by": "Desenvolvido por",
        "compare_text": "Compare taxas de impostos de 27+ pa\u00edses com nosso simulador interativo",
        "disclaimer": "Informa\u00e7\u00f5es fiscais fornecidas apenas como orienta\u00e7\u00e3o geral. Consulte um consultor fiscal qualificado.",
    },
}

# Fallback to EN for CJK/Arabic/etc
for lang in ["zh", "th", "ru", "ar", "ja", "ko"]:
    UI[lang] = UI["en"].copy()

# Country display names per language
COUNTRY_NAMES_I18N = {
    "en": {
        "thailand": "Thailand", "portugal": "Portugal", "spain": "Spain",
        "mexico": "Mexico", "vietnam": "Vietnam", "malaysia": "Malaysia",
        "japan": "Japan", "uae": "the UAE", "colombia": "Colombia",
        "panama": "Panama", "costa-rica": "Costa Rica", "greece": "Greece",
        "georgia": "Georgia", "paraguay": "Paraguay", "laos": "Laos",
        "cambodia": "Cambodia",
    },
    "fr": {
        "thailand": "Tha\u00eflande", "portugal": "Portugal", "spain": "Espagne",
        "mexico": "Mexique", "vietnam": "Vietnam", "malaysia": "Malaisie",
        "japan": "Japon", "uae": "les \u00c9mirats arabes unis", "colombia": "Colombie",
        "panama": "Panama", "costa-rica": "Costa Rica", "greece": "Gr\u00e8ce",
        "georgia": "G\u00e9orgie", "paraguay": "Paraguay", "laos": "Laos",
        "cambodia": "Cambodge",
    },
    "es": {
        "thailand": "Tailandia", "portugal": "Portugal", "spain": "Espa\u00f1a",
        "mexico": "M\u00e9xico", "vietnam": "Vietnam", "malaysia": "Malasia",
        "japan": "Jap\u00f3n", "uae": "los EAU", "colombia": "Colombia",
        "panama": "Panam\u00e1", "costa-rica": "Costa Rica", "greece": "Grecia",
        "georgia": "Georgia", "paraguay": "Paraguay", "laos": "Laos",
        "cambodia": "Camboya",
    },
    "pt": {
        "thailand": "Tail\u00e2ndia", "portugal": "Portugal", "spain": "Espanha",
        "mexico": "M\u00e9xico", "vietnam": "Vietn\u00e3", "malaysia": "Mal\u00e1sia",
        "japan": "Jap\u00e3o", "uae": "os EAU", "colombia": "Col\u00f4mbia",
        "panama": "Panam\u00e1", "costa-rica": "Costa Rica", "greece": "Gr\u00e9cia",
        "georgia": "Ge\u00f3rgia", "paraguay": "Paraguai", "laos": "Laos",
        "cambodia": "Camboja",
    },
}

# Fallback to EN
for lang in ["zh", "th", "ru", "ar", "ja", "ko"]:
    COUNTRY_NAMES_I18N[lang] = COUNTRY_NAMES_I18N["en"].copy()


def build_simulator_url(lang, country_slug):
    """Build the taxes-crypto.eu simulator URL for a given language and country."""
    tc_lang = SIMULATOR_LANG[lang]
    path = SIMULATOR_PATHS[lang]

    if country_slug in EXILE_SLUGS:
        return f"https://taxes-crypto.eu/{tc_lang}/{path}/{EXILE_SLUGS[country_slug]}"
    else:
        # General simulator page for countries not in the simulator
        return f"https://taxes-crypto.eu/{tc_lang}/{path}"


def build_tax_block(lang, country_slug):
    """Generate the HTML block for the tax/fiscal exile section."""
    ui = UI[lang]
    td = TAX_DATA[country_slug]
    country_name = COUNTRY_NAMES_I18N[lang].get(country_slug, country_slug.title())
    sim_url = build_simulator_url(lang, country_slug)
    has_dedicated = country_slug in EXILE_SLUGS

    # Tax rate color
    rate = td["tax_rate"]
    if rate in ("0%", "N/A"):
        rate_color = "#28a745"  # green
    elif rate.startswith("0-") or rate.startswith("10"):
        rate_color = "#7cb342"  # light green
    elif "15" in rate or "19" in rate:
        rate_color = "#ffc107"  # yellow
    else:
        rate_color = "#dc3545"  # red

    # Crypto score color
    score_num = int(td["crypto_score"].split("/")[0])
    if score_num >= 8:
        score_color = "#28a745"
    elif score_num >= 5:
        score_color = "#ffc107"
    else:
        score_color = "#dc3545"

    highlights_html = ""
    for h in td["highlights"]:
        highlights_html += f'<li style="margin-bottom:6px;">{h}</li>'

    block = f'''
    <!-- Section: Tax & Fiscal Exile -->
    <div class="row mb-5" id="tax">
        <div class="col-md-12">
            <h2 style="font-size:26px;color:#1d2d50;border-bottom:3px solid #f15d30;padding-bottom:10px;margin-bottom:24px;">
                &#128176; {ui["section_title"]}
            </h2>

            <!-- Tax Overview Cards -->
            <div class="row mb-4">
                <div class="col-md-3 col-6 mb-3">
                    <div style="background:#f8f9fc;border-radius:8px;padding:16px;text-align:center;height:100%;">
                        <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">{ui["tax_rate"]}</div>
                        <div style="font-size:24px;font-weight:700;color:{rate_color};">{rate}</div>
                    </div>
                </div>
                <div class="col-md-3 col-6 mb-3">
                    <div style="background:#f8f9fc;border-radius:8px;padding:16px;text-align:center;height:100%;">
                        <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">{ui["regime"]}</div>
                        <div style="font-size:16px;font-weight:600;color:#1d2d50;">{td["regime"]}</div>
                    </div>
                </div>
                <div class="col-md-3 col-6 mb-3">
                    <div style="background:#f8f9fc;border-radius:8px;padding:16px;text-align:center;height:100%;">
                        <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">{ui["crypto_score"]}</div>
                        <div style="font-size:24px;font-weight:700;color:{score_color};">{td["crypto_score"]}</div>
                    </div>
                </div>
                <div class="col-md-3 col-6 mb-3">
                    <div style="background:#f8f9fc;border-radius:8px;padding:16px;text-align:center;height:100%;">
                        <div style="font-size:11px;color:#888;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">{ui["exit_tax"]}</div>
                        <div style="font-size:16px;font-weight:600;color:{"#dc3545" if td["exit_tax"] != "No" else "#28a745"};">{td["exit_tax"]}</div>
                    </div>
                </div>
            </div>

            <!-- Tax label -->
            <p style="font-size:.95rem;color:#444;margin-bottom:16px;"><strong>{ui["tax_rate"]}:</strong> {td["tax_label"]}</p>

            <!-- Key Points -->
            <h3 style="font-size:17px;color:#1d2d50;margin-bottom:12px;">{ui["key_points"]}</h3>
            <ul style="font-size:.93rem;line-height:1.8;padding-left:20px;color:#444;">
                {highlights_html}
            </ul>

            <!-- CTA Block -->
            <div style="background:linear-gradient(135deg,#1d2d50 0%,#2a4a7f 100%);border-radius:10px;padding:28px 32px;margin-top:24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
                <div style="flex:1;min-width:200px;">
                    <h3 style="font-size:18px;color:#fff;margin:0 0 8px;">{ui["cta_text"]}</h3>
                    <p style="font-size:.9rem;color:rgba(255,255,255,0.8);margin:0;">
                        {ui["cta_sub"]} {country_name}.
                        {ui["compare_text"] if not has_dedicated else ""}
                    </p>
                </div>
                <a href="{sim_url}" target="_blank" rel="noopener noreferrer"
                   style="display:inline-block;background:#f15d30;color:#fff;font-weight:600;font-size:15px;padding:14px 28px;border-radius:6px;text-decoration:none;text-align:center;white-space:nowrap;">
                    &#128640; {ui["cta_text"]} &rarr;
                </a>
            </div>
            <p style="font-size:.78rem;color:#aaa;margin-top:10px;text-align:right;">
                {ui["powered_by"]} <a href="https://taxes-crypto.eu" target="_blank" rel="noopener" style="color:#f15d30;text-decoration:underline;">Taxes-Crypto.eu</a>
            </p>

            <!-- Disclaimer -->
            <div style="background:#fff8e1;border-left:4px solid #ffc107;padding:12px 16px;border-radius:4px;margin-top:12px;">
                <p style="font-size:.82rem;color:#888;margin:0;"><em>{ui["disclaimer"]}</em></p>
            </div>
        </div>
    </div>
'''
    return block


def add_block_to_file(filepath, lang, country_slug):
    """Insert the tax block into an expat guide page."""
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # Skip if already has the tax block
    if 'id="tax"' in html or "taxes-crypto.eu" in html:
        return False

    block = build_tax_block(lang, country_slug)

    # Also add #tax to the Table of Contents if it exists
    toc_item_en = '<li><a href="#tax" style="color:#f15d30;">Tax &amp; Fiscal Exile</a></li>'
    toc_item_fr = '<li><a href="#tax" style="color:#f15d30;">Fiscalit&eacute; &amp; Exil Fiscal</a></li>'
    toc_item_es = '<li><a href="#tax" style="color:#f15d30;">Fiscalidad &amp; Exilio Fiscal</a></li>'
    toc_item_pt = '<li><a href="#tax" style="color:#f15d30;">Fiscalidade &amp; Ex&iacute;lio Fiscal</a></li>'

    toc_items = {
        "en": toc_item_en, "fr": toc_item_fr, "es": toc_item_es, "pt": toc_item_pt,
        "zh": toc_item_en, "th": toc_item_en, "ru": toc_item_en,
        "ar": toc_item_en, "ja": toc_item_en, "ko": toc_item_en,
    }

    # Insert TOC item after "Buying Property" / "realestate" entry
    toc_entry = toc_items.get(lang, toc_item_en)
    # Find the last </li> in the TOC <ol> that contains #realestate
    toc_pattern = r'(<li><a href="#realestate"[^<]*</a></li>)'
    if re.search(toc_pattern, html):
        html = re.sub(toc_pattern, r'\1\n                    ' + toc_entry, html, count=1)

    # Insert block before author/sources or before related guides
    inserted = False

    # Try to insert before "Official Sources"
    if "Official Sources" in html:
        html = html.replace("<!-- Author + Sources -->", block + "\n    <!-- Author + Sources -->", 1)
        inserted = True

    # Try to insert before "Related Guides"
    if not inserted and "<!-- Related Guides -->" in html:
        html = html.replace("<!-- Related Guides -->", block + "\n    <!-- Related Guides -->", 1)
        inserted = True

    # Try to insert before E-E-A-T block
    if not inserted and "<!-- E-E-A-T -->" in html:
        html = html.replace("<!-- E-E-A-T -->", block + "\n    <!-- E-E-A-T -->", 1)
        inserted = True

    # Fallback: insert before closing </div></section>
    if not inserted:
        # Find the last </div>\n</section> before footer
        idx = html.rfind("</div>\n</section>")
        if idx > 0:
            html = html[:idx] + block + "\n" + html[idx:]
            inserted = True

    if inserted:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    langs = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
    countries = list(TAX_DATA.keys())

    total = 0
    updated = 0

    for lang in langs:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue
        for slug in countries:
            filename = f"expat-guide-{slug}.html"
            filepath = os.path.join(lang_dir, filename)
            if not os.path.isfile(filepath):
                continue
            total += 1
            if add_block_to_file(filepath, lang, slug):
                updated += 1
                print(f"  OK {lang}/{filename}")

    print(f"\nDone: {updated}/{total} files updated with tax exile block.")


if __name__ == "__main__":
    main()
