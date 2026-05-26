#!/usr/bin/env python3
"""
fix_seo_issues.py — Apply the safe, high-value technical SEO fixes found by the
attribute-order-independent audit (seo_audit.py v2):

  A. strip_html_descriptions : 266 meta descriptions contain raw HTML tags
     (<strong> etc.) inside content="" — invalid; Google ignores/truncates.
  B. fix_jsonld_escapes       : 2 FR JSON-LD blocks have invalid \\' escapes.
  C. add_og_tags              : 560 pages lack Open Graph tags; add
     og:title/description/type/url/image derived from existing title,
     meta description and canonical.

NOT a problem (false positive in v1): canonical tags — they exist with href,
just with attribute order <link href=... rel="canonical">.

Idempotent. Run: python fix_seo_issues.py [langs...]
"""
import re
import html as ihtml
from pathlib import Path

ROOT = Path(__file__).parent / "www"
LANGS = ["en", "fr", "es", "pt", "zh", "th", "ru", "ar", "ja", "ko"]
DEFAULT_OG_IMAGE = "https://www.evisa-card.com/images/og-image.jpg"

DESC_TAG = re.compile(r'(<meta\s+name="description"\s+content=")([^"]*)("\s*/?>)', re.I)
DESC_TAG_ALT = re.compile(r'(<meta\s+content=")([^"]*)("\s+name="description"\s*/?>)', re.I)
TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
CANON = re.compile(r'<link\b[^>]*rel="canonical"[^>]*>', re.I)
HREF = re.compile(r'href="([^"]*)"', re.I)
# Order-independent: an og: property may appear before OR after content=
OG_PROP = re.compile(r'property\s*=\s*["\']og:', re.I)
HEAD_END = re.compile(r"</head>", re.I)
REDIRECT = re.compile(r'window\.location|http-equiv=["\']refresh', re.I)
CJK = {"zh", "ja", "ko", "th"}


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = ihtml.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def truncate(s, limit):
    if len(s) <= limit:
        return s
    cut = s[:limit]
    for sep in (". ", "; ", ", ", " "):
        i = cut.rfind(sep)
        if i > limit * 0.6:
            return cut[: i + (1 if sep == ". " else 0)].rstrip(" ,;")
    return cut.rstrip()


def esc(s):
    return s.replace('"', "&quot;")


# ---------- Fix A ----------
def fix_descriptions(html_text, lang):
    changed = [False]

    def repl(m):
        content = m.group(2)
        if "<" not in content and "&lt;" not in content:
            return m.group(0)
        clean = strip_tags(content)
        clean = truncate(clean, 110 if lang in CJK else 158)
        if clean and clean[-1] not in ".!?。":
            clean += "."
        changed[0] = True
        return m.group(1) + esc(clean) + m.group(3)

    new = DESC_TAG.sub(repl, html_text, count=1)
    if not changed[0]:
        new = DESC_TAG_ALT.sub(
            lambda m: (m.group(1) + esc(truncate(strip_tags(m.group(2)), 110 if lang in CJK else 158)) + m.group(3))
            if ("<" in m.group(2) or "&lt;" in m.group(2)) else m.group(0),
            html_text, count=1,
        )
        if new != html_text:
            changed[0] = True
    return new, changed[0]


# ---------- Fix B ----------
def fix_jsonld(html_text):
    """Replace invalid JSON escapes (\\' -> ') inside ld+json blocks."""
    def repl(m):
        block = m.group(0)
        fixed = block.replace("\\'", "'")
        return fixed

    new = re.sub(
        r'<script[^>]*type="application/ld\+json"[^>]*>.*?</script>',
        repl, html_text, flags=re.S | re.I,
    )
    return new, (new != html_text)


# ---------- Fix C ----------
def add_og_tags(html_text):
    if OG_PROP.search(html_text):
        return html_text, False  # already has OG
    tm = TITLE.search(html_text)
    title = strip_tags(tm.group(1)) if tm else ""
    dm = DESC_TAG.search(html_text) or DESC_TAG_ALT.search(html_text)
    desc = dm.group(2) if dm else ""  # already escaped in file
    cm = CANON.search(html_text)
    url = ""
    if cm:
        hm = HREF.search(cm.group(0))
        if hm:
            url = hm.group(1)
    if not title:
        return html_text, False

    block = (
        f'    <meta property="og:title" content="{esc(title)}"/>\n'
        f'    <meta property="og:description" content="{desc}"/>\n'
        f'    <meta property="og:type" content="article"/>\n'
    )
    if url:
        block += f'    <meta property="og:url" content="{url}"/>\n'
    block += f'    <meta property="og:image" content="{DEFAULT_OG_IMAGE}"/>\n'

    new = HEAD_END.sub(block + "</head>", html_text, count=1)
    return new, (new != html_text)


def main():
    import sys
    langs = [a for a in sys.argv[1:] if not a.startswith("--")] or LANGS
    counts = {"desc": 0, "jsonld": 0, "og": 0}
    for lang in langs:
        d = ROOT / lang
        if not d.exists():
            continue
        for f in sorted(d.glob("*.html")):
            txt = f.read_text(encoding="utf-8", errors="replace")
            if REDIRECT.search(txt) and not TITLE.search(txt):
                continue
            orig = txt
            txt, c1 = fix_descriptions(txt, lang)
            txt, c2 = fix_jsonld(txt)
            txt, c3 = add_og_tags(txt)
            if txt != orig:
                f.write_text(txt, encoding="utf-8")
            counts["desc"] += int(c1)
            counts["jsonld"] += int(c2)
            counts["og"] += int(c3)
        print(f"[{lang}] done")
    print(f"Fixed: descriptions={counts['desc']}, jsonld={counts['jsonld']}, og={counts['og']}")


if __name__ == "__main__":
    main()
