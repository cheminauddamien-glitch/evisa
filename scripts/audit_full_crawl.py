#!/usr/bin/env python3
"""
audit_full_crawl.py
Full site crawl: check ALL internal links for 404s + SEO/geo audit.
"""
import os, re, glob, sys
from collections import defaultdict
from urllib.parse import urlparse, unquote

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
DOMAIN = "evisa-card.com"

# Build index of all existing files
def build_file_index():
    """Build a set of all existing file paths (relative to www/)."""
    index = set()
    for root, dirs, files in os.walk(BASE):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), BASE).replace("\\", "/")
            index.add(rel)
            # Also add without .html extension
            if rel.endswith(".html"):
                index.add(rel[:-5])
    return index


def resolve_link(href, current_file):
    """Resolve a relative or absolute link to a file path relative to www/."""
    if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
        return None
    if href.startswith("javascript:"):
        return None

    # External links
    if href.startswith("http://") or href.startswith("https://"):
        parsed = urlparse(href)
        if DOMAIN not in parsed.netloc:
            return None  # External link, skip
        # Internal absolute URL
        path = parsed.path.lstrip("/")
        return path if path else None

    # Absolute path
    if href.startswith("/"):
        return href.lstrip("/")

    # Relative path
    current_dir = os.path.dirname(current_file)
    resolved = os.path.normpath(os.path.join(current_dir, href)).replace("\\", "/")
    return resolved


def crawl_file(filepath, rel_path, file_index):
    """Crawl a single file. Return dict of issues."""
    issues = {
        "broken_links": [],
        "seo": [],
        "geo": [],
    }

    try:
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
    except Exception as e:
        issues["seo"].append(f"Cannot read file: {e}")
        return issues

    # Only check first 4096 bytes for noindex
    head = html[:4096]
    is_noindex = "noindex" in head

    # --- BROKEN LINKS ---
    # Find all href attributes
    hrefs = re.findall(r'href="([^"]*)"', html)
    for href in hrefs:
        href = href.split("#")[0].split("?")[0]  # Remove hash and query
        if not href:
            continue
        resolved = resolve_link(href, rel_path)
        if resolved is None:
            continue
        # Check if file exists
        if resolved not in file_index:
            # Try with .html extension
            if (resolved + ".html") not in file_index:
                # Skip common false positives
                if resolved.startswith("https://") or resolved.startswith("http://"):
                    continue
                if any(resolved.endswith(ext) for ext in [".css", ".js", ".png", ".jpg", ".svg", ".ico", ".xml", ".txt", ".json", ".woff", ".woff2", ".ttf", ".eot"]):
                    # Asset files - check separately
                    full_path = os.path.join(BASE, resolved)
                    if not os.path.isfile(full_path):
                        issues["broken_links"].append(f"Missing asset: {href}")
                    continue
                issues["broken_links"].append(href)

    # --- SEO AUDIT ---
    if not is_noindex:
        # Title
        if "<title>" not in html and "<title " not in html:
            issues["seo"].append("Missing <title>")
        else:
            title_match = re.search(r'<title>([^<]*)</title>', html)
            if title_match and len(title_match.group(1).strip()) < 10:
                issues["seo"].append(f"Title too short: '{title_match.group(1).strip()}'")

        # Meta description
        if 'name="description"' not in html:
            issues["seo"].append("Missing meta description")

        # Canonical
        if 'rel="canonical"' not in html:
            issues["seo"].append("Missing canonical URL")

        # H1
        if "<h1" not in html:
            issues["seo"].append("Missing H1 tag")

    # --- GEO/LANG AUDIT ---
    # Extract lang from directory
    parts = rel_path.split("/")
    if len(parts) >= 2 and parts[0] in ("en","fr","es","pt","zh","th","ru","ar","ja","ko"):
        expected_lang = parts[0]
        filename = parts[-1]

        # Check html lang attribute
        lang_match = re.search(r'<html\s+lang="([^"]*)"', html)
        if lang_match:
            actual_lang = lang_match.group(1)
            if actual_lang != expected_lang and not actual_lang.startswith(expected_lang):
                issues["geo"].append(f"Wrong html lang: expected '{expected_lang}', got '{actual_lang}'")
        else:
            if not is_noindex:
                issues["geo"].append("Missing html lang attribute")

        # Check canonical URL matches current language
        canon_match = re.search(r'rel="canonical"\s+href="([^"]*)"', html)
        if not canon_match:
            canon_match = re.search(r'href="([^"]*)"\s*rel="canonical"', html)
            if not canon_match:
                canon_match = re.search(r'rel="canonical"[^>]*href="([^"]*)"', html)
        if canon_match:
            canon_url = canon_match.group(1)
            if f"/{expected_lang}/" not in canon_url:
                issues["geo"].append(f"Canonical URL wrong lang: {canon_url}")

        # Check hreflang count
        hreflang_count = len(re.findall(r'hreflang="[a-z]', html))
        if hreflang_count > 0 and hreflang_count < 10 and not is_noindex:
            issues["geo"].append(f"Only {hreflang_count} hreflang tags (expected 10+)")

        # Check hreflang self-reference
        self_hreflang = f'hreflang="{expected_lang}"'
        if self_hreflang not in html and not is_noindex and hreflang_count > 0:
            issues["geo"].append(f"Missing self-referencing hreflang for '{expected_lang}'")

    return issues


def main():
    print("Building file index...")
    file_index = build_file_index()
    print(f"  {len(file_index)} entries in file index")

    print("Crawling all HTML files...")

    all_broken = defaultdict(list)
    all_seo = defaultdict(list)
    all_geo = defaultdict(list)

    total_files = 0
    files_with_issues = 0

    # Crawl all HTML files
    for root, dirs, files in os.walk(BASE):
        for f in files:
            if not f.endswith(".html"):
                continue

            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, BASE).replace("\\", "/")
            total_files += 1

            issues = crawl_file(filepath, rel_path, file_index)

            has_issues = False
            for link in issues["broken_links"]:
                all_broken[link].append(rel_path)
                has_issues = True
            for issue in issues["seo"]:
                all_seo[issue].append(rel_path)
                has_issues = True
            for issue in issues["geo"]:
                all_geo[issue].append(rel_path)
                has_issues = True

            if has_issues:
                files_with_issues += 1

            if total_files % 1000 == 0:
                print(f"  ...crawled {total_files} files")

    # --- REPORT ---
    print(f"\n{'='*60}")
    print(f"FULL CRAWL REPORT")
    print(f"{'='*60}")
    print(f"Total files crawled: {total_files}")
    print(f"Files with issues: {files_with_issues}")

    # BROKEN LINKS
    print(f"\n--- BROKEN LINKS (404) ---")
    if all_broken:
        # Sort by number of pages affected
        sorted_broken = sorted(all_broken.items(), key=lambda x: -len(x[1]))
        print(f"Total unique broken links: {len(sorted_broken)}")
        for link, pages in sorted_broken[:50]:  # Top 50
            print(f"  [{len(pages)} pages] {link}")
            if len(pages) <= 3:
                for p in pages:
                    print(f"    -> {p}")
        if len(sorted_broken) > 50:
            print(f"  ... and {len(sorted_broken) - 50} more")
    else:
        print("  No broken links found!")

    # SEO ISSUES
    print(f"\n--- SEO ISSUES ---")
    if all_seo:
        sorted_seo = sorted(all_seo.items(), key=lambda x: -len(x[1]))
        print(f"Total unique SEO issues: {len(sorted_seo)}")
        for issue, pages in sorted_seo:
            print(f"  [{len(pages)} pages] {issue}")
            if len(pages) <= 5:
                for p in pages:
                    print(f"    -> {p}")
    else:
        print("  No SEO issues found!")

    # GEO/LANG ISSUES
    print(f"\n--- GEO/LANG ISSUES ---")
    if all_geo:
        sorted_geo = sorted(all_geo.items(), key=lambda x: -len(x[1]))
        print(f"Total unique geo issues: {len(sorted_geo)}")
        for issue, pages in sorted_geo:
            count = len(pages)
            print(f"  [{count} pages] {issue}")
            if count <= 5:
                for p in pages:
                    print(f"    -> {p}")
    else:
        print("  No geo/lang issues found!")

    print(f"\n{'='*60}")
    print("DONE")


if __name__ == "__main__":
    main()
