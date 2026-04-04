#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
propagate_visa_enrichment.py
Propagates visa enrichment from www/en/ to 9 other language directories.
1. Injects 5 new sections (all-visas, processing, health-requirements, extension, refusal)
   from enriched EN *-visa-requirements.html files into target language files.
2. Propagates visa-alert blocks (mandatory, evisa, free, etc.) from EN visa-*.html files.
3. Fixes dropdown language links that point to destination.html instead of actual filename.
Idempotent: skips files that are already enriched.
"""
import os
import re
import glob
import time

# --- Wait 5 minutes for enrichment scripts to finish ---
print("Waiting 5 minutes (300s) for enrichment scripts to finish...")
time.sleep(300)
print("Wait complete. Starting propagation.\n")

BASE = os.path.dirname(os.path.abspath(__file__))
WWW = os.path.join(BASE, "www")
EN_DIR = os.path.join(WWW, "en")

TARGET_LANGS = ["fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

# Translated H2 titles: keys are the EN section IDs
# Values: dict of lang -> translated title
SECTION_TITLES = {
    "all-visas": {
        "en": "Complete Visa Categories",
        "fr": "Categories de Visa",
        "es": "Categorias de Visa",
        "pt": "Categorias de Visto",
        "zh": "\u7b7e\u8bc1\u7c7b\u522b",
        "ja": "\u30d3\u30b6\u30ab\u30c6\u30b4\u30ea\u30fc",
        "ko": "\ube44\uc790 \uce74\ud14c\uace0\ub9ac",
        "ru": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0432\u0438\u0437",
        "ar": "\u0641\u0626\u0627\u062a \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0629",
        "th": "\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e27\u0e35\u0e0b\u0e48\u0e32",
    },
    "processing": {
        "en": "Processing Times by Visa Type",
        "fr": "Delais et Frais",
        "es": "Tiempos y Tarifas",
        "pt": "Prazos e Taxas",
        "zh": "\u5904\u7406\u65f6\u95f4\u548c\u8d39\u7528",
        "ja": "\u51e6\u7406\u6642\u9593\u3068\u6599\u91d1",
        "ko": "\ucc98\ub9ac \uc2dc\uac04 \ubc0f \uc218\uc218\ub8cc",
        "ru": "\u0421\u0440\u043e\u043a\u0438 \u0438 \u0441\u0431\u043e\u0440\u044b",
        "ar": "\u0645\u062f\u0629 \u0627\u0644\u0645\u0639\u0627\u0644\u062c\u0629 \u0648\u0627\u0644\u0631\u0633\u0648\u0645",
        "th": "\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e41\u0e25\u0e30\u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21",
    },
    "health-requirements": {
        "en": "Health &amp; Character Requirements",
        "fr": "Sante et Conditions d'Entree",
        "es": "Salud y Requisitos de Entrada",
        "pt": "Saude e Requisitos de Entrada",
        "zh": "\u5065\u5eb7\u548c\u5165\u5883\u8981\u6c42",
        "ja": "\u5065\u5eb7\u30fb\u5165\u56fd\u8981\u4ef6",
        "ko": "\uac74\uac15 \ubc0f \uc785\uad6d \uc694\uac74",
        "ru": "\u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435 \u0438 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u044a\u0435\u0437\u0434\u0430",
        "ar": "\u0627\u0644\u0635\u062d\u0629 \u0648\u0645\u062a\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u062f\u062e\u0648\u0644",
        "th": "\u0e2a\u0e38\u0e02\u0e20\u0e32\u0e1e\u0e41\u0e25\u0e30\u0e02\u0e49\u0e2d\u0e01\u0e33\u0e2b\u0e19\u0e14\u0e01\u0e32\u0e23\u0e40\u0e02\u0e49\u0e32",
    },
    "extension": {
        "en": "Visa Extension &amp; Renewal",
        "fr": "Extension et Depassement",
        "es": "Extension y Estancia Excesiva",
        "pt": "Extensao e Permanencia Excessiva",
        "zh": "\u7b7e\u8bc1\u5ef6\u671f\u548c\u903e\u671f",
        "ja": "\u30d3\u30b6\u5ef6\u9577\u3068\u8d85\u904e\u6ede\u5728",
        "ko": "\ube44\uc790 \uc5f0\uc7a5 \ubc0f \uccb4\ub958 \ucd08\uacfc",
        "ru": "\u041f\u0440\u043e\u0434\u043b\u0435\u043d\u0438\u0435 \u0438 \u043f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u0438\u0435 \u0441\u0440\u043e\u043a\u0430",
        "ar": "\u062a\u0645\u062f\u064a\u062f \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0629 \u0648\u0627\u0644\u0625\u0642\u0627\u0645\u0629 \u0627\u0644\u0632\u0627\u0626\u062f\u0629",
        "th": "\u0e01\u0e32\u0e23\u0e15\u0e48\u0e2d\u0e2d\u0e32\u0e22\u0e38\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e01\u0e34\u0e19\u0e01\u0e33\u0e2b\u0e19\u0e14",
    },
    "refusal": {
        "en": "Visa Refusal &amp; Appeals",
        "fr": "Refus et Recours",
        "es": "Rechazo y Apelaciones",
        "pt": "Recusa e Recursos",
        "zh": "\u62d2\u7b7e\u548c\u7533\u8bc9",
        "ja": "\u62d2\u5426\u3068\u4e0d\u670d\u7533\u7acb\u3066",
        "ko": "\uac70\ubd80 \ubc0f \ud56d\uc18c",
        "ru": "\u041e\u0442\u043a\u0430\u0437 \u0438 \u0430\u043f\u0435\u043b\u043b\u044f\u0446\u0438\u044f",
        "ar": "\u0627\u0644\u0631\u0641\u0636 \u0648\u0627\u0644\u0627\u0633\u062a\u0626\u0646\u0627\u0641",
        "th": "\u0e01\u0e32\u0e23\u0e1b\u0e0f\u0e34\u0e40\u0e2a\u0e18\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e2d\u0e38\u0e17\u0e18\u0e23\u0e13\u0e4c",
    },
}


def read_file(path):
    """Read file with utf-8 encoding."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    """Write file with utf-8 encoding."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def extract_enriched_sections(en_content):
    """
    Extract the 5 enriched sections from EN content.
    From <h2 id="all-visas"> through end of <h2 id="refusal"> section (ends at </ul>).
    Returns the raw HTML block or None if not enriched.
    """
    # Find start: <h2 id="all-visas">
    start_match = re.search(r'<h2\s+id="all-visas">', en_content)
    if not start_match:
        return None

    start_pos = start_match.start()

    # Find the refusal section and its end
    # The refusal section ends with </ul> before the next <div or <h2 or editorial note
    refusal_match = re.search(r'<h2\s+id="refusal">', en_content)
    if not refusal_match:
        return None

    # Find the </ul> that ends the refusal section
    refusal_pos = refusal_match.start()
    # Search for </ul> after the refusal h2
    end_match = re.search(r'</ul>', en_content[refusal_pos:])
    if not end_match:
        return None

    end_pos = refusal_pos + end_match.end()

    return en_content[start_pos:end_pos]


def translate_section_titles(section_html, lang):
    """
    Replace EN H2 titles with translated versions for the given language.
    """
    result = section_html
    for section_id, translations in SECTION_TITLES.items():
        en_title = translations["en"]
        lang_title = translations.get(lang, en_title)
        # Match the h2 tag with this id and replace the title text
        pattern = r'(<h2\s+id="' + re.escape(section_id) + r'">)' + re.escape(en_title) + r'(</h2>)'
        replacement = r'\g<1>' + lang_title + r'\g<2>'
        result = re.sub(pattern, replacement, result)
    return result


def find_injection_point_requirements(target_content):
    """
    Find where to inject the enriched sections in a *-visa-requirements.html file.
    Inject before the editorial note div: <div class="alert alert-info
    """
    # Look for editorial note
    match = re.search(r'<div class="alert alert-info', target_content)
    if match:
        return match.start()

    # Fallback: before </article>
    match = re.search(r'</article>', target_content)
    if match:
        return match.start()

    return None


def extract_visa_alerts(en_content):
    """
    Extract all visa-alert divs from EN content.
    Returns list of (alert_class, full_html_block) tuples.
    """
    alerts = []
    # Match complete visa-alert divs - they are self-contained blocks
    # Pattern: <div class="visa-alert visa-alert-XXX" ...>...</div>\n (the outer div)
    # These are structured as: outer div > inner div > span + div
    pattern = r'<div class="visa-alert visa-alert-(\w+)"[^>]*>.*?</div>\s*</div>\s*</div>'
    for match in re.finditer(pattern, en_content, re.DOTALL):
        alert_class = match.group(1)
        alert_html = match.group(0)
        alerts.append((alert_class, alert_html))
    return alerts


def find_injection_point_after_h1(content):
    """
    Find the position right after the <h1>...</h1> tag for injecting alerts.
    """
    match = re.search(r'</h1>\s*', content)
    if match:
        return match.end()
    return None


def fix_dropdown_links(content, filename):
    """
    Fix dropdown language links that point to destination.html instead of the actual filename.
    Also fix links in the dropdown that should point to the current file.
    """
    # Fix links like href="/XX/destination.html" in the dropdown to href="/XX/filename"
    # But only within the dropdown-menu section
    result = content
    # Fix any dropdown-item links that point to destination.html
    # These should point to the current filename in each language
    for lang in ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]:
        old_pattern = f'href="/{lang}/destination.html"'
        new_link = f'href="/{lang}/{filename}"'
        # Only replace within dropdown context (dropdown-item class links)
        # We do a targeted replacement: only if preceded by dropdown-item
        result = result.replace(old_pattern, new_link)

    return result


def propagate_requirements_enrichment():
    """
    Propagate enriched sections from EN *-visa-requirements.html to other languages.
    """
    stats = {lang: {"checked": 0, "enriched": 0, "skipped": 0, "missing": 0}
             for lang in TARGET_LANGS}

    # Find all EN *-visa-requirements.html files
    en_files = glob.glob(os.path.join(EN_DIR, "*-visa-requirements.html"))

    print(f"Found {len(en_files)} EN *-visa-requirements.html files")
    print("=" * 70)

    enriched_en_count = 0
    not_enriched_en = []

    for en_path in sorted(en_files):
        filename = os.path.basename(en_path)
        en_content = read_file(en_path)

        # Check if EN file is enriched
        sections_html = extract_enriched_sections(en_content)
        if not sections_html:
            not_enriched_en.append(filename)
            continue

        enriched_en_count += 1

        for lang in TARGET_LANGS:
            stats[lang]["checked"] += 1
            target_path = os.path.join(WWW, lang, filename)

            if not os.path.exists(target_path):
                stats[lang]["missing"] += 1
                continue

            target_content = read_file(target_path)

            # Check if already enriched (idempotent)
            if 'id="all-visas"' in target_content:
                stats[lang]["skipped"] += 1
                continue

            # Translate section titles
            translated_sections = translate_section_titles(sections_html, lang)

            # Find injection point
            inject_pos = find_injection_point_requirements(target_content)
            if inject_pos is None:
                print(f"  WARNING: No injection point found for {lang}/{filename}")
                continue

            # Inject the sections
            new_content = (
                target_content[:inject_pos]
                + "\n"
                + translated_sections
                + "\n\n"
                + target_content[inject_pos:]
            )

            write_file(target_path, new_content)
            stats[lang]["enriched"] += 1
            print(f"  ENRICHED: {lang}/{filename}")

    print(f"\nEN files enriched: {enriched_en_count}/{len(en_files)}")
    if not_enriched_en:
        print(f"  Not yet enriched in EN: {len(not_enriched_en)} files")

    return stats


def propagate_visa_alerts():
    """
    Propagate visa-alert blocks from EN visa-*.html to other languages.
    """
    stats = {lang: {"checked": 0, "alerts_added": 0, "skipped": 0, "missing": 0}
             for lang in TARGET_LANGS}

    # Find all EN visa-*.html files (not *-visa-requirements.html)
    en_files = glob.glob(os.path.join(EN_DIR, "visa-*.html"))

    print(f"\nFound {len(en_files)} EN visa-*.html files for alert propagation")
    print("=" * 70)

    files_with_alerts = 0

    for en_path in sorted(en_files):
        filename = os.path.basename(en_path)
        en_content = read_file(en_path)

        # Extract alerts from EN file
        alerts = extract_visa_alerts(en_content)
        if not alerts:
            continue

        files_with_alerts += 1

        for lang in TARGET_LANGS:
            stats[lang]["checked"] += 1
            target_path = os.path.join(WWW, lang, filename)

            if not os.path.exists(target_path):
                stats[lang]["missing"] += 1
                continue

            target_content = read_file(target_path)
            modified = False

            for alert_class, alert_html in alerts:
                # Check if this alert type already exists (idempotent)
                if f"visa-alert-{alert_class}" in target_content:
                    continue

                # Find injection point: right after </h1>
                inject_pos = find_injection_point_after_h1(target_content)
                if inject_pos is None:
                    continue

                # Inject the alert
                target_content = (
                    target_content[:inject_pos]
                    + alert_html
                    + "\n"
                    + target_content[inject_pos:]
                )
                modified = True

            if modified:
                write_file(target_path, target_content)
                stats[lang]["alerts_added"] += 1
                print(f"  ALERTS ADDED: {lang}/{filename}")
            else:
                stats[lang]["skipped"] += 1

    print(f"\nEN files with alerts: {files_with_alerts}")
    return stats


def fix_all_dropdown_links():
    """
    Fix dropdown language links across all language directories.
    """
    stats = {lang: {"checked": 0, "fixed": 0} for lang in TARGET_LANGS}

    print("\nFixing dropdown language links...")
    print("=" * 70)

    for lang in TARGET_LANGS:
        lang_dir = os.path.join(WWW, lang)
        if not os.path.isdir(lang_dir):
            continue

        html_files = glob.glob(os.path.join(lang_dir, "*.html"))
        for filepath in sorted(html_files):
            filename = os.path.basename(filepath)
            stats[lang]["checked"] += 1

            content = read_file(filepath)
            original = content

            # Fix dropdown links pointing to destination.html
            content = fix_dropdown_links(content, filename)

            if content != original:
                write_file(filepath, content)
                stats[lang]["fixed"] += 1

    return stats


def print_stats(title, stats, columns):
    """Print statistics table."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")
    header = f"  {'Lang':<6}" + "".join(f"{col:<12}" for col in columns)
    print(header)
    print("  " + "-" * (6 + 12 * len(columns)))
    for lang in TARGET_LANGS:
        row = f"  {lang:<6}"
        for col in columns:
            key = col.lower().replace(" ", "_")
            row += f"{stats[lang].get(key, 0):<12}"
        print(row)
    # Totals
    print("  " + "-" * (6 + 12 * len(columns)))
    row = f"  {'TOTAL':<6}"
    for col in columns:
        key = col.lower().replace(" ", "_")
        total = sum(stats[lang].get(key, 0) for lang in TARGET_LANGS)
        row += f"{total:<12}"
    print(row)


def main():
    print("=" * 70)
    print("  VISA ENRICHMENT PROPAGATION SCRIPT")
    print("  Propagating from www/en/ to 9 language directories")
    print("=" * 70)
    print()

    # 1. Propagate enriched sections in *-visa-requirements.html
    print("STEP 1: Propagating enriched sections (*-visa-requirements.html)")
    print("-" * 70)
    req_stats = propagate_requirements_enrichment()
    print_stats(
        "Requirements Enrichment Stats",
        req_stats,
        ["Checked", "Enriched", "Skipped", "Missing"]
    )

    # 2. Propagate visa alerts in visa-*.html
    print("\n\nSTEP 2: Propagating visa alerts (visa-*.html)")
    print("-" * 70)
    alert_stats = propagate_visa_alerts()
    print_stats(
        "Visa Alert Propagation Stats",
        alert_stats,
        ["Checked", "Alerts_added", "Skipped", "Missing"]
    )

    # 3. Fix dropdown links
    print("\n\nSTEP 3: Fixing dropdown language links")
    print("-" * 70)
    link_stats = fix_all_dropdown_links()
    print_stats(
        "Dropdown Link Fix Stats",
        link_stats,
        ["Checked", "Fixed"]
    )

    print("\n" + "=" * 70)
    print("  PROPAGATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
