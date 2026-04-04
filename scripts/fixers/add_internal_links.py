#!/usr/bin/env python3
"""
add_internal_links.py

Adds a "Related {Country} Visa Pages" internal-linking block to every visa
page in www/en/ and propagates the same block (with adjusted href paths)
to all other language directories.

Usage:  python add_internal_links.py          (dry-run by default)
        python add_internal_links.py --apply  (actually modify files)
"""

import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent / "www"
EN_DIR = BASE_DIR / "en"
LANG_DIRS = ["fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]

# Regex patterns that identify a visa page and capture the country slug.
# Order matters: more specific patterns must come first so that the first
# match wins and we extract the right slug.
VISA_PAGE_PATTERNS = [
    # {country}-visa-for-{nationality}-citizens.html
    re.compile(r"^(?P<country>.+?)-visa-for-.+-citizens\.html$"),
    # {country}-visa-extension.html
    re.compile(r"^(?P<country>.+?)-visa-extension\.html$"),
    # {country}-visa-fees.html
    re.compile(r"^(?P<country>.+?)-visa-fees\.html$"),
    # {country}-visa-requirements.html
    re.compile(r"^(?P<country>.+?)-visa-requirements\.html$"),
    # {country}-visa-processing-time.html
    re.compile(r"^(?P<country>.+?)-visa-processing-time\.html$"),
    # visa-{country}.html  (main overview page)
    re.compile(r"^visa-(?P<country>.+?)\.html$"),
]

# Generic / non-country pages whose slugs should be skipped
SLUG_BLACKLIST = {
    "documents-checklist",
    "photo-requirements",
    "processing-times",
    "types",
    "policy",
    "on-arrival",
}

# Also skip any slug that starts with these prefixes
SLUG_PREFIX_BLACKLIST = [
    "free-countries-",
]

# Duplicate-detection: skip files that already contain one of these markers
ALREADY_DONE_RE = re.compile(r"Related\s.*Visa Pages|related-links", re.IGNORECASE)

# The footer tag we insert before
FOOTER_RE = re.compile(r"(<footer\b)", re.IGNORECASE)

# Button inline style (matches the site's btn-outline-primary look)
BTN_STYLE = (
    "display:inline-block;padding:6px 14px;border:1px solid #3b82f6;"
    "border-radius:6px;color:#3b82f6;text-decoration:none;font-size:13px;"
    "font-weight:500;transition:background .2s,color .2s;"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slug_to_name(slug: str) -> str:
    """Convert a URL slug to a capitalised country name.

    Examples:
        'thailand'    -> 'Thailand'
        'costa-rica'  -> 'Costa Rica'
        'new-zealand' -> 'New Zealand'
        'uae'         -> 'UAE'
        'uk'          -> 'UK'
        'us'          -> 'US'
    """
    # Fully-uppercase abbreviations
    upper_words = {"uae", "uk", "us", "usa"}
    parts = slug.split("-")
    titled = []
    for part in parts:
        if part.lower() in upper_words:
            titled.append(part.upper())
        else:
            titled.append(part.capitalize())
    return " ".join(titled)


def extract_country_slug(filename: str) -> str | None:
    """Return the country slug from a visa-page filename, or None."""
    for pattern in VISA_PAGE_PATTERNS:
        m = pattern.match(filename)
        if m:
            slug = m.group("country")
            if slug in SLUG_BLACKLIST:
                return None
            for prefix in SLUG_PREFIX_BLACKLIST:
                if slug.startswith(prefix):
                    return None
            return slug
    return None


def discover_related_pages(country_slug: str, en_dir: Path) -> list[tuple[str, str]]:
    """Return a list of (filename, label) for related pages that exist on disk.

    The order is deterministic and matches the spec.
    """
    candidates = [
        (f"visa-{country_slug}.html", "Main Overview"),
        (f"{country_slug}-visa-requirements.html", "Requirements"),
        (f"{country_slug}-visa-fees.html", "Fees & Cost"),
        (f"{country_slug}-visa-extension.html", "Extension"),
        (f"{country_slug}-visa-processing-time.html", "Processing Time"),
    ]

    # eVisa / ETA / eVOA variants
    for suffix, label in [
        ("eta", "ETA"),
        ("evisa", "eVisa"),
        ("evoa", "eVOA"),
    ]:
        fname = f"{country_slug}-{suffix}.html"
        if (en_dir / fname).is_file():
            candidates.append((fname, label))

    # Expat guide
    expat = f"expat-guide-{country_slug}.html"
    if (en_dir / expat).is_file():
        candidates.append((expat, "Expat Guide"))

    # Keep only files that actually exist
    result = []
    for fname, label in candidates:
        if (en_dir / fname).is_file():
            result.append((fname, label))
    return result


def build_html_block(
    country_slug: str,
    related: list[tuple[str, str]],
    lang: str,
    current_filename: str,
) -> str:
    """Build the styled Related Pages HTML block.

    The link to the *current* page is excluded so we don't link to ourselves.
    If only one link remains (or zero), return an empty string — no point
    showing a block with a single self-referential link.
    """
    country_name = slug_to_name(country_slug)

    # Filter out the current page
    links = [(fname, label) for fname, label in related if fname != current_filename]

    if len(links) < 1:
        return ""

    link_html_parts = []
    for fname, label in links:
        href = f"/{lang}/{fname}"
        link_html_parts.append(
            f'        <a href="{href}" style="{BTN_STYLE}" '
            f'class="btn btn-outline-primary btn-sm">{label}</a>'
        )

    links_joined = "\n".join(link_html_parts)

    block = (
        f"<!-- Related Pages -->\n"
        f'<div style="background:#f8f9fc;border-radius:8px;padding:20px 24px;'
        f'margin:0 auto 30px;max-width:960px;">\n'
        f'    <h3 style="font-size:16px;color:#1d2d50;margin-bottom:14px;">'
        f"Related {country_name} Visa Pages</h3>\n"
        f'    <div style="display:flex;flex-wrap:wrap;gap:8px;">\n'
        f"{links_joined}\n"
        f"    </div>\n"
        f"</div>\n"
    )
    return block


def inject_block(html: str, block: str) -> str | None:
    """Insert *block* immediately before the first <footer ...> tag.

    Returns the modified HTML, or None if no footer was found.
    """
    m = FOOTER_RE.search(html)
    if not m:
        return None
    insert_pos = m.start()
    return html[:insert_pos] + block + html[insert_pos:]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    apply = "--apply" in sys.argv
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== add_internal_links.py [{mode}] ===\n")

    if not EN_DIR.is_dir():
        print(f"ERROR: English directory not found: {EN_DIR}")
        sys.exit(1)

    # 1. Collect all en/ visa-page filenames and their country slugs
    en_files = sorted(EN_DIR.iterdir())
    slug_files: dict[str, list[str]] = {}  # slug -> [filenames]
    for fpath in en_files:
        if not fpath.is_file() or fpath.suffix != ".html":
            continue
        slug = extract_country_slug(fpath.name)
        if slug is not None:
            slug_files.setdefault(slug, []).append(fpath.name)

    print(f"Found {len(slug_files)} country slugs across "
          f"{sum(len(v) for v in slug_files.values())} visa pages in en/\n")

    # 2. For each country, discover related pages once
    related_cache: dict[str, list[tuple[str, str]]] = {}
    for slug in slug_files:
        related_cache[slug] = discover_related_pages(slug, EN_DIR)

    # 3. Process each language directory (en + others)
    all_langs = ["en"] + LANG_DIRS
    total_modified = 0
    total_skipped_existing = 0
    total_skipped_no_footer = 0
    total_skipped_no_links = 0

    for lang in all_langs:
        lang_dir = BASE_DIR / lang
        if not lang_dir.is_dir():
            print(f"  SKIP language dir (not found): {lang_dir}")
            continue

        lang_modified = 0

        for slug, filenames in slug_files.items():
            related = related_cache[slug]

            for filename in filenames:
                fpath = lang_dir / filename
                if not fpath.is_file():
                    continue

                html = fpath.read_text(encoding="utf-8", errors="replace")

                # Skip if already has a related-links section
                if ALREADY_DONE_RE.search(html):
                    total_skipped_existing += 1
                    continue

                # Build the block
                block = build_html_block(slug, related, lang, filename)
                if not block:
                    total_skipped_no_links += 1
                    continue

                # Inject before <footer>
                new_html = inject_block(html, block)
                if new_html is None:
                    total_skipped_no_footer += 1
                    continue

                if apply:
                    fpath.write_text(new_html, encoding="utf-8")

                lang_modified += 1

        print(f"  [{lang}] {lang_modified} files {'modified' if apply else 'would be modified'}")
        total_modified += lang_modified

    print(f"\n--- Summary ---")
    print(f"  Total files {'modified' if apply else 'to modify'}:  {total_modified}")
    print(f"  Skipped (already has section):    {total_skipped_existing}")
    print(f"  Skipped (no <footer> found):      {total_skipped_no_footer}")
    print(f"  Skipped (no related links):       {total_skipped_no_links}")

    if not apply:
        print(f"\nThis was a dry run. Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
