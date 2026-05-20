#!/usr/bin/env python3
"""
update_visa_pages_2026.py — Inject 2026 visa update banner + Important Update
alert into individual visa pages (~3080 files across 10 languages).

Reuses COUNTRIES + LANG data from update_visa_2026.py.

Insertion logic per file:
  1. If a "Last updated" paragraph exists (style="...small text-muted"),
     replace it with the new banner and insert the alert box right after.
  2. Otherwise insert <banner+alert> immediately after the opening
     <div class="container" style="max-width:960px;">.

Source of truth: VISA_AUDIT_2026.md
Date: 2026-05-20
"""
import re
from pathlib import Path

# Reuse country data + lang labels (build_alert is reimplemented below
# with the visa-page style, but COUNTRIES/LANG are imported as-is).
from update_visa_2026 import COUNTRIES, LANG

ROOT = Path(__file__).parent / "www"

# Per-language "Last updated" line found on visa-* pages (mb-1 small text-muted style).
# Format is more relaxed than the expat-guide top banner — it's a one-liner.
INPAGE_PATTERNS = {
    "en": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?Last updated:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "fr": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?Dernière mise à jour:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "es": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?Última actualización:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "pt": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?(Última atualização|Última actualização):?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "zh": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?最后更新:?\s*<strong>[^<]*</strong>。?\.?</p>'
    ),
    "th": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?(อัปเดตล่าสุด|ปรับปรุงล่าสุด):?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "ru": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?Последнее обновление:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "ar": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?آخر تحديث:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "ja": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?最終更新(日)?:?\s*<strong>[^<]*</strong>\.?</p>'
    ),
    "ko": re.compile(
        r'<p class="mb-1 small text-muted">[^<]*?(마지막 업데이트|최근 업데이트):?\s*<strong>[^<]*</strong>\.?</p>'
    ),
}

# Universal content-area anchor — matches all 3 visa-page templates:
#  - Template A: <div class="container" style="max-width:960px;">  (e.g. *-evisa pages)
#  - Template B: <article class="country-page">                    (e.g. *-visa-for-*-citizens, *-visa-extension)
#  - Template C: <section class="ftco-section"><div class="container"><article>  (e.g. *-visa-fees, *-visa-requirements)
CONTAINER_RE = re.compile(
    r'(<div class="container" style="max-width:960px;">'
    r'|<article class="country-page">'
    r'|<section class="ftco-section"><div class="container"><article>)'
)

# We must only inject once per file (idempotency marker)
MARKER = "<!-- visa-2026-update -->"


def build_inpage_banner(lang_code):
    L = LANG[lang_code]
    return (
        f'{MARKER}\n    <p class="mb-1 small text-muted">'
        f'{L["updated"]}: <strong>{L["date_label"]}</strong>.</p>'
    )


def build_inpage_alert(lang_code, country):
    L = LANG[lang_code]
    c = COUNTRIES[country]
    if c["status"] == "current":
        return ""
    bg = "#fff5f0" if c["status"] == "major" else "#f0f6ff"
    border = "#f15d30" if c["status"] == "major" else "#1d2d50"
    icon = "⚠️" if c["status"] == "major" else "ℹ️"

    return (
        f'\n    <div style="background:{bg};border-left:4px solid {border};'
        f'padding:14px 18px;border-radius:4px;margin:8px 0 24px;">\n'
        f'        <p style="margin:0 0 6px;font-weight:600;color:#1d2d50;'
        f'font-size:.98rem;">{icon} {L["important"]} — {c["title"]}</p>\n'
        f'        <p style="margin:0 0 6px;font-size:.9rem;color:#444;'
        f'line-height:1.55;">{c["summary"]}</p>\n'
        f'        <p style="margin:6px 0 0;font-size:.85rem;color:#444;">'
        f'<strong>{L["effective"]}:</strong> {c["effective"]}</p>\n'
        f'        <p style="margin:8px 0 0;font-size:.82rem;color:#666;">'
        f'<strong>{L["source"]}:</strong> '
        f'<a href="{c["source_url"]}" rel="nofollow noopener" target="_blank" '
        f'style="color:#1d2d50;">{c["source_label"]}</a></p>\n'
        f'    </div>'
    )


def visa_pages_for(country, lang_dir):
    """All visa-* pages where this country is the destination."""
    out = []
    for f in lang_dir.glob(f'{country}-*.html'):
        if 'expat-guide' in f.name:
            continue
        out.append(f)
    p = lang_dir / f'visa-{country}.html'
    if p.exists():
        out.append(p)
    return sorted(set(out))


def update_file(path: Path, lang_code: str, country: str):
    html = path.read_text(encoding="utf-8")

    # Idempotency: skip if already injected
    if MARKER in html:
        return f"  [SKIP] {lang_code}/{path.name} - already updated"

    banner = build_inpage_banner(lang_code)
    alert = build_inpage_alert(lang_code, country)
    block = banner + alert

    # Always insert at the top via the universal container anchor.
    # This guarantees visibility (above the page content) regardless of
    # whether the page has an Editorial-Team / Last-updated block lower down.
    new_html, n2 = CONTAINER_RE.subn(
        r'\1\n    ' + block.replace("\n", "\n    "), html, count=1
    )
    if n2 == 0:
        return f"  [FAIL] {lang_code}/{path.name} - container not found"

    # Separately: update any inline "Last updated" date string lower in the page
    # (e.g. Editorial Team footer) without disturbing its surrounding structure.
    # Just refresh the date string from March 2026 → 20 May 2026 in the local language.
    pat = INPAGE_PATTERNS[lang_code]
    L = LANG[lang_code]
    refreshed_line = (
        f'<p class="mb-1 small text-muted">{L["updated"]}: '
        f'<strong>{L["date_label"]}</strong>.</p>'
    )
    new_html = pat.sub(refreshed_line, new_html, count=1)

    path.write_text(new_html, encoding="utf-8")
    return f"  [OK]   {lang_code}/{path.name}"


def main():
    print(f"=== Visa pages update — 2026-05-20 ===\n")
    total_ok = 0
    total_skip = 0
    total_fail = 0

    for lang_code in LANG:
        lang_dir = ROOT / lang_code
        if not lang_dir.exists():
            continue
        lang_ok = 0
        lang_skip = 0
        lang_fail = 0
        for country in COUNTRIES:
            for path in visa_pages_for(country, lang_dir):
                msg = update_file(path, lang_code, country)
                if "[OK]" in msg:
                    lang_ok += 1
                elif "[SKIP]" in msg:
                    lang_skip += 1
                else:
                    lang_fail += 1
                    print(msg)
        print(f"[{lang_code}] OK={lang_ok}  SKIP={lang_skip}  FAIL={lang_fail}")
        total_ok += lang_ok
        total_skip += lang_skip
        total_fail += lang_fail

    print(f"\n=== Done: {total_ok} updated, {total_skip} skipped, {total_fail} failed ===")


if __name__ == "__main__":
    main()
