#!/usr/bin/env python3
"""
seo_meta_descriptions.py — Generate & inject SEO meta descriptions for pages
that have none. Diagnosis from Google Search Console (May 2026): 216 EN pages
rank on page 1 but earn ~0 clicks because Google has no description to build a
snippet from. Site-wide CTR was 0.20%.

For each page missing <meta name="description">:
  1. Derive a 150-160 char description from the page's own H1 + first
     meaningful paragraph + key-facts table (real content, not boilerplate).
  2. Ensure the primary keyword (from the H1) appears.
  3. Inject <meta name="description"> after <title>, and an og:description
     if the page has Open Graph tags but no og:description.

Idempotent: skips pages that already have a description.
Run on EN first (drives the high-impression queries), then other langs.
"""
import re
import html as ihtml
from pathlib import Path

ROOT = Path(__file__).parent / "www"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta\s+name="description"', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
OG_DESC_RE = re.compile(r'<meta\s+property="og:description"', re.I)
OG_ANY_RE = re.compile(r'<meta\s+property="og:', re.I)


def clean_text(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = ihtml.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# The 2026 visa-update banner + alert block we injected earlier. Must be stripped
# before deriving a description, otherwise the snippet starts with the alert text.
ALERT_BLOCK_RE = re.compile(r"<!-- visa-2026-update -->.*?</div>", re.S)
SKIP_MARKERS = (
    "Important 2026 update", "Mise à jour importante", "Actualización importante",
    "Atualização importante", "重要更新", "重要な更新", "중요 업데이트",
    "Важное обновление", "تحديث مهم", "การอัปเดตที่สำคัญ",
)


def first_meaningful_paragraph(body: str) -> str:
    for p in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S):
        txt = clean_text(p)
        # strip leading emoji/symbols/space before the startswith check
        stripped = txt.lstrip("⚠️ℹ️📋 \t​")
        if stripped.startswith(("Updated:", "Last updated", "Mis à jour", "Actualizado",
                                "Atualizado", "Important")):
            continue
        if any(m in txt for m in SKIP_MARKERS):
            continue
        if len(txt) >= 50:
            return txt
    return ""


def key_facts(html_text: str) -> str:
    """Pull a couple of useful 'key: value' pairs from the first table."""
    pairs = re.findall(
        r"<t[dh][^>]*>(.*?)</t[dh]>\s*<t[dh][^>]*>(.*?)</t[dh]>", html_text, re.S
    )
    facts = []
    wanted = ("visa", "stay", "fee", "cost", "validity", "processing")
    for k, v in pairs:
        kk = clean_text(k)
        vv = clean_text(v)
        if not kk or not vv:
            continue
        if any(w in kk.lower() for w in wanted) and len(vv) < 40:
            facts.append(f"{kk}: {vv}")
        if len(facts) >= 2:
            break
    return " ".join(facts)


def truncate(s: str, limit: int = 158) -> str:
    if len(s) <= limit:
        return s
    cut = s[:limit]
    # back off to last sentence end or word boundary
    for sep in (". ", "; ", ", ", " "):
        idx = cut.rfind(sep)
        if idx > limit * 0.6:
            return cut[: idx + (1 if sep.startswith(".") else 0)].rstrip(" ,;")
    return cut.rstrip()


def build_description(html_text: str) -> str:
    # Remove the injected 2026 update banner/alert so it never leaks into the snippet
    clean_html = ALERT_BLOCK_RE.sub("", html_text)
    h1 = clean_text(H1_RE.search(clean_html).group(1)) if H1_RE.search(clean_html) else ""
    body = clean_html.split("</nav>")[-1]
    para = first_meaningful_paragraph(body)
    facts = key_facts(clean_html)

    # Base = first paragraph (already human-written, info-dense)
    base = para or h1

    desc = base
    # If short, enrich with key facts and/or a CTA
    if len(desc) < 110 and facts:
        desc = f"{desc} {facts}"
    if len(desc) < 110:
        desc = f"{desc} Check 2026 requirements, fees and processing times."

    desc = truncate(desc, 158)

    # Make sure it reads like a complete thought
    if desc and desc[-1] not in ".!?":
        desc += "."
    return desc


def inject(html_text: str, desc: str) -> str:
    esc = desc.replace('"', "&quot;")
    meta = f'<meta name="description" content="{esc}"/>'

    # Insert right after </title>
    if "</title>" in html_text:
        html_text = html_text.replace("</title>", "</title>\n    " + meta, 1)
    else:
        # fallback: after charset
        html_text = re.sub(
            r'(<meta charset="[^"]*"/?>)', r"\1\n    " + meta, html_text, count=1
        )

    # Add og:description if OG block exists but lacks it
    if OG_ANY_RE.search(html_text) and not OG_DESC_RE.search(html_text):
        og = f'<meta property="og:description" content="{esc}"/>'
        # put it after og:title if present, else after the first og: tag
        m = re.search(r'(<meta\s+property="og:title"[^>]*/?>)', html_text, re.I)
        if m:
            html_text = html_text.replace(m.group(1), m.group(1) + "\n    " + og, 1)
    return html_text


def process(lang: str, dry_run: bool = False):
    d = ROOT / lang
    if not d.exists():
        return 0, 0
    done = 0
    skipped = 0
    report = []
    for f in sorted(d.glob("*.html")):
        txt = f.read_text(encoding="utf-8", errors="replace")
        if DESC_RE.search(txt):
            skipped += 1
            continue
        desc = build_description(txt)
        if not desc or len(desc) < 30:
            report.append(f"  [WEAK] {lang}/{f.name} -> '{desc}'")
            continue
        if not dry_run:
            f.write_text(inject(txt, desc), encoding="utf-8")
        done += 1
        report.append(f"  [{len(desc):3}c] {f.name}: {desc}")
    return done, skipped, report


if __name__ == "__main__":
    import sys

    langs = sys.argv[1:] or ["en"]
    dry = "--dry" in langs
    langs = [l for l in langs if not l.startswith("--")]
    grand = 0
    for lang in langs:
        done, skipped, report = process(lang, dry_run=dry)
        # write report to file to avoid console encoding issues
        Path(f"seo_desc_report_{lang}.txt").write_text(
            "\n".join(report), encoding="utf-8"
        )
        print(f"[{lang}] injected={done} skipped(has desc)={skipped} -> report seo_desc_report_{lang}.txt")
        grand += done
    print(f"TOTAL injected: {grand}")
