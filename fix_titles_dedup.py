#!/usr/bin/env python3
"""
fix_titles_dedup.py — De-duplicate <title> on combinatorial visa pages in
zh/ko/ja, where translation dropped the DESTINATION and left only the
nationality, so many "{dest}-visa-for-{nat}-citizens" pages share one title.

Fix: prepend the localized destination name (self-sourced from the site's own
visa-{dest}.html H1) to titles that are duplicated and don't already contain it.
This uses the site's existing translations (not new machine translation) and
only touches pages whose title currently collides with another page.

Arabic is intentionally skipped: its source titles are too corrupted
(nonsense/partial-English) for a safe automated prepend — flagged for manual
review in the strategy report instead.

Idempotent. Run: python fix_titles_dedup.py
"""
import re
import html as ihtml
import collections
from pathlib import Path

ROOT = Path(__file__).parent / "www"
LANGS = ["zh", "ko", "ja"]

TITLE = re.compile(r"(<title>)(.*?)(</title>)", re.S | re.I)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)

# Markers that follow the destination name in a visa-{dest}.html H1, per the
# observed pattern "{DestName}eVisa & Travel info (2026)" localized.
NAME_CUTS = ["eVisa", "电子签证", "电子簽證", "e비자", "電子ビザ", "の電子", "&amp;",
             "&", "(2026", "（2026", " 2026", "旅行", "여행", "旅行情報",
             "Visa", "비자", "ビザ", "签证"]


def clean(s):
    return re.sub(r"\s+", " ", ihtml.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def localized_dest_name(lang, dest):
    p = ROOT / lang / f"visa-{dest}.html"
    if not p.exists():
        return None
    m = H1.search(p.read_text(encoding="utf-8", errors="replace"))
    if not m:
        return None
    name = clean(m.group(1))
    # cut at the first marker
    cut_at = len(name)
    for mk in NAME_CUTS:
        i = name.find(mk)
        if 0 < i < cut_at:
            cut_at = i
    name = name[:cut_at].strip(" ：:·-—　")
    # sanity: must be short and non-empty
    if 1 <= len(name) <= 16:
        return name
    return None


def build_dest_maps():
    dests = set()
    for f in (ROOT / "en").glob("*-visa-for-*-citizens.html"):
        m = re.match(r"(.+?)-visa-for-.+-citizens\.html", f.name)
        if m:
            dests.add(m.group(1))
    maps = {}
    for lang in LANGS:
        maps[lang] = {}
        for d in dests:
            n = localized_dest_name(lang, d)
            if n:
                maps[lang][d] = n
    return maps


def main():
    maps = build_dest_maps()
    total_fixed = 0
    report = []
    for lang in LANGS:
        files = sorted((ROOT / lang).glob("*-visa-for-*-citizens.html"))
        # find duplicate titles
        by_title = collections.defaultdict(list)
        cache = {}
        for f in files:
            h = f.read_text(encoding="utf-8", errors="replace")
            cache[f] = h
            tm = TITLE.search(h)
            t = clean(tm.group(2)) if tm else ""
            by_title[t].append(f)
        dup_titles = {t for t, fs in by_title.items() if len(fs) > 1 and t}

        fixed = 0
        for f in files:
            h = cache[f]
            tm = TITLE.search(h)
            if not tm:
                continue
            cur = clean(tm.group(2))
            if cur not in dup_titles:
                continue
            m = re.match(r"(.+?)-visa-for-.+-citizens\.html", f.name)
            dest = m.group(1) if m else None
            dn = maps[lang].get(dest)
            if not dn:
                continue
            if dn in cur:
                continue  # destination already present
            new_title = f"{dn} {tm.group(2).strip()}"
            new_h = h[:tm.start()] + tm.group(1) + new_title + tm.group(3) + h[tm.end():]
            f.write_text(new_h, encoding="utf-8")
            fixed += 1
        report.append(f"[{lang}] dest_map={len(maps[lang])}/49, dup-title pages fixed={fixed}")
        total_fixed += fixed
    for line in report:
        print(line)
    print(f"TOTAL titles de-duplicated: {total_fixed}")


if __name__ == "__main__":
    main()
