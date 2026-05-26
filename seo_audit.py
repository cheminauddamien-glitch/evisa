#!/usr/bin/env python3
"""
seo_audit.py — Full on-page/technical SEO audit across all languages.
v2: attribute-order-independent tag parsing (v1 had false positives because
it assumed a fixed attribute order, e.g. rel before href in <link>).

Scans www/{lang}/*.html and reports issue counts per type and per language.
Writes SEO_AUDIT_REPORT.md.
"""
import re
import json as _json
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).parent / "www"
LANGS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
CJK = {"zh", "ja", "ko", "th"}  # char-count thresholds don't apply the same way

TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
H1 = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.S | re.I)
JSONLD = re.compile(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)
IMG = re.compile(r"<img\b[^>]*>", re.I)
REDIRECT = re.compile(r'window\.location|http-equiv=["\']refresh', re.I)
TAG = re.compile(r"<(meta|link)\b([^>]*)>", re.I)
ATTR = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"', re.I)


def clean(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def parse_tags(html):
    """Return list of (tagname, {attr:val}) for all meta/link tags, order-independent."""
    out = []
    for m in TAG.finditer(html):
        name = m.group(1).lower()
        attrs = {k.lower(): v for k, v in ATTR.findall(m.group(2))}
        out.append((name, attrs))
    return out


def audit():
    issues = defaultdict(lambda: defaultdict(int))
    examples = defaultdict(list)
    titles_by_lang = defaultdict(Counter)
    total_pages = content_pages = redirects = 0

    for lang in LANGS:
        d = ROOT / lang
        if not d.exists():
            continue
        for f in sorted(d.glob("*.html")):
            total_pages += 1
            html = f.read_text(encoding="utf-8", errors="replace")
            rel = f"{lang}/{f.name}"

            if REDIRECT.search(html) and not TITLE.search(html):
                redirects += 1
                continue
            content_pages += 1

            tags = parse_tags(html)
            metas = [a for n, a in tags if n == "meta"]
            links = [a for n, a in tags if n == "link"]

            def has_meta_name(v):
                return any(a.get("name", "").lower() == v for a in metas)

            def get_meta_name(v):
                for a in metas:
                    if a.get("name", "").lower() == v:
                        return a.get("content", "")
                return None

            def has_meta_prop(v):
                return any(a.get("property", "").lower() == v for a in metas)

            def link_rel(v):
                for a in links:
                    if a.get("rel", "").lower() == v:
                        return a
                return None

            def add(key):
                issues[key][lang] += 1
                if len(examples[key]) < 8:
                    examples[key].append(rel)

            # Title
            tm = TITLE.search(html)
            t = clean(tm.group(1)) if tm else ""
            if not t:
                add("title_missing")
            else:
                titles_by_lang[lang][t] += 1
                # CJK: a char carries more; use a higher char budget
                hi = 40 if lang in CJK else 65
                lo = 12 if lang in CJK else 30
                if len(t) > hi:
                    add("title_too_long")
                elif len(t) < lo:
                    add("title_too_short")

            # Description
            desc = get_meta_name("description")
            if not desc or not desc.strip():
                add("desc_missing")
            else:
                hi = 110 if lang in CJK else 170
                lo = 30 if lang in CJK else 70
                if len(desc) > hi:
                    add("desc_too_long")
                elif len(desc) < lo:
                    add("desc_too_short")

            # H1
            nonempty_h1 = [h for h in H1.findall(html) if clean(h)]
            if len(nonempty_h1) == 0:
                add("h1_missing")
            elif len(nonempty_h1) > 1:
                add("h1_multiple")

            # Canonical (order-independent)
            can = link_rel("canonical")
            if not can or not can.get("href", "").strip():
                add("canonical_missing")

            # robots noindex
            rob = get_meta_name("robots")
            if rob and "noindex" in rob.lower():
                add("robots_noindex")

            # viewport
            if not has_meta_name("viewport"):
                add("viewport_missing")

            # Open Graph
            if not has_meta_prop("og:title"):
                add("og_title_missing")
            if not has_meta_prop("og:description"):
                add("og_desc_missing")
            if not has_meta_prop("og:image"):
                add("og_image_missing")

            # hreflang
            if not any(a.get("hreflang") for a in links):
                add("hreflang_missing")

            # JSON-LD
            ld = JSONLD.findall(html)
            if not ld:
                add("jsonld_missing")
            else:
                for block in ld:
                    try:
                        _json.loads(block.strip())
                    except Exception:
                        add("jsonld_broken")
                        break

            # Images missing alt
            no_alt = sum(1 for tag in IMG.findall(html) if "alt=" not in tag.lower())
            if no_alt:
                issues["img_no_alt"][lang] += no_alt
                if len(examples["img_no_alt"]) < 8:
                    examples["img_no_alt"].append(f"{rel} ({no_alt})")

    dup_titles = defaultdict(int)
    dup_examples = []
    for lang, ctr in titles_by_lang.items():
        for title, n in ctr.items():
            if n > 1:
                dup_titles[lang] += n
                if len(dup_examples) < 15:
                    dup_examples.append(f"{lang}: x{n} — {title[:55]}")

    return dict(total_pages=total_pages, content_pages=content_pages,
                redirects=redirects, issues=issues, examples=examples,
                dup_titles=dup_titles, dup_examples=dup_examples)


SEVERITY = {
    "title_missing": "CRITICAL", "h1_missing": "CRITICAL", "desc_missing": "CRITICAL",
    "robots_noindex": "CRITICAL", "jsonld_broken": "CRITICAL",
    "canonical_missing": "WARNING", "title_too_long": "WARNING", "title_too_short": "WARNING",
    "desc_too_long": "WARNING", "desc_too_short": "WARNING", "h1_multiple": "WARNING",
    "og_desc_missing": "WARNING", "og_image_missing": "WARNING", "og_title_missing": "WARNING",
    "img_no_alt": "WARNING", "viewport_missing": "WARNING", "dup_titles": "WARNING",
    "hreflang_missing": "OPPORTUNITY", "jsonld_missing": "OPPORTUNITY",
}


def main():
    r = audit()
    sev_order = {"CRITICAL": 0, "WARNING": 1, "OPPORTUNITY": 2}
    rows = []
    for key, perlang in r["issues"].items():
        total = sum(perlang.values())
        rows.append((sev_order.get(SEVERITY.get(key, "WARNING"), 1), -total, key, total, dict(perlang)))
    dt_total = sum(r["dup_titles"].values())
    if dt_total:
        rows.append((1, -dt_total, "dup_titles", dt_total, dict(r["dup_titles"])))
    rows.sort()

    out = ["# SEO Audit Report v2 — eVisa-Card.com\n",
           f"**Pages scanned**: {r['total_pages']} ({r['content_pages']} content, {r['redirects']} redirect stubs)\n",
           f"**Languages**: {', '.join(LANGS)}\n",
           "\n## Issues by type\n",
           "| Severity | Issue | Total | Per-language |", "|---|---|---:|---|"]
    for _, _, key, total, perlang in rows:
        pl = ", ".join(f"{l}:{c}" for l, c in sorted(perlang.items()))
        out.append(f"| {SEVERITY.get(key,'WARNING')} | {key} | {total} | {pl} |")
    out.append("\n## Examples\n")
    for _, _, key, total, _ in rows:
        ex = r["examples"].get(key, [])
        if ex:
            out.append(f"- **{key}**: {', '.join(ex[:6])}")
    if r["dup_examples"]:
        out.append("\n## Duplicate title examples\n")
        for e in r["dup_examples"]:
            out.append(f"- {e}")
    Path("SEO_AUDIT_REPORT.md").write_text("\n".join(out), encoding="utf-8")

    print(f"Pages: {r['total_pages']} ({r['content_pages']} content, {r['redirects']} redirects)")
    for _, _, key, total, _ in rows:
        print(f"  {SEVERITY.get(key,'WARNING'):11} {key:20} {total}")
    print("Report -> SEO_AUDIT_REPORT.md")


if __name__ == "__main__":
    main()
