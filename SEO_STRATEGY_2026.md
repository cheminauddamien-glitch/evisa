# SEO Strategy & Audit Summary — eVisa-Card.com (May 2026)

Date: 2026-05-26
Scope: 13,198 pages × 10 languages. Triggered by Google Search Console data
(90 days) showing 1.1M impressions / 2,258 clicks → **0.20% CTR** at avg
position ~14.

---

## 1. Root-cause diagnosis (GSC)

The problem was **not ranking** (many pages sit on page 1) — it was **CTR**.
Pages ranked but earned ~0 clicks because they had no usable snippet.

Worst offenders (page-1 rank, near-zero clicks):
| Query | Impressions | Pos | Clicks |
|---|---:|---:|---:|
| cappadocia visa requirements | 36,291 | 8.4 | 1 |
| machu picchu visa requirements | 19,745 | 7.5 | 0 |
| taipei visa requirements | 7,292 | 11.2 | 0 |
| patagonia visa requirements | 3,681 | 6.4 | 0 |

~132k impressions sat on pages with no meta description.

---

## 2. Fixes applied (committed)

| Fix | Pages | Commit |
|---|---:|---|
| Meta descriptions added (derived from real page content, per language) | 2,185 | 575fa5fc6 |
| Stripped raw HTML (`<strong>`) from meta descriptions | 266 | 9f8d1da0b |
| Fixed broken JSON-LD (invalid `\'` escapes, FR) | 2 | 9f8d1da0b |
| Added Open Graph tags (og:title/description/type/url/image) | 560 | 9f8d1da0b |
| De-duplicated `<title>` by restoring destination name (zh/ko/ja) | 210 | (this commit) |
| Sitemap `<lastmod>` refreshed for changed pages | 2,175+ | 72d8b22f1 + this |
| 2026 visa-rule update banners + alerts (16 countries) | 3,240 | 082474d87 |

### Audit method note
The first audit pass produced **false positives** (2,166 "missing canonical",
a bad OG pass) because its regexes were **attribute-order sensitive** — the
site's tags use `href`-before-`rel` and `content`-before-`property`. Detection
was rewritten order-independently (`seo_audit.py` v2). Lesson: always parse
attributes order-independently on this codebase.

---

## 3. Alignment with Google core-update / helpful-content guidance

Ref: https://developers.google.com/search/docs/appearance/core-updates

Google rewards **people-first, helpful, reliable** content + **E-E-A-T**
(Experience, Expertise, Authoritativeness, Trustworthiness). For a visa site
(YMYL-adjacent), reliability and freshness matter most.

**Aligned / strengths**
- "Last updated" dates + "Editorial Team" blocks → authorship/trust signals.
- Official-source links and 2026 freshness banners → accuracy/trust.
- Per-nationality pages carry genuinely different info (visa-free vs e-visa vs
  visa-required differs by nationality). Measured ~65% token overlap between
  same-destination pages → ~35% is legitimately unique. Only 43/968 EN
  combinatorial pages are thin (<1,500 chars body). **The combinatorial model
  is defensible**, not doorway spam — provided the per-nationality facts are
  correct.

**Risks to address**
- **Translation quality** in zh/ko/ja/ar (see §4). Garbled/duplicate titles
  read as "made for search engines" and undermine trust — the exact signal
  Google's helpful-content system penalizes.
- **Thin tail**: 43 EN pages (+ equivalents) with <1,500 chars should be
  enriched or consolidated.

---

## 4. Remaining work (NOT auto-fixed — needs judgement / human review)

### a) Duplicate titles still present
- **ko**: ~102 pages — destination is present but the **nationality** collapsed
  in translation (e.g. all `uae-visa-for-*-citizens` → "UAE 비자 2026...").
- **ja**: ~7 pages — same nationality-collapse pattern.
- **ar**: ~223 pages — titles are **corrupted at the source** (e.g. 64 pages
  share a nonsense title `&apos; ٢ &apos; & كيفية التطبيق`; others are
  partial-English). These need a proper Arabic re-translation, not an
  automated prepend — doing so blindly would worsen quality.
- **Recommendation**: rebuild these titles from a curated, human-verified
  localized template `{destination} visa for {nationality} citizens 2026`,
  using proper per-language destination + nationality name tables. Do NOT
  mass-generate unverified machine translations (Google penalizes this).

### b) Title length
- ~1,065 EN titles exceed ~65 chars and get truncated in SERP. This is
  cosmetic (they still rank); shortening risks dropping keywords. Low priority.
  If done, trim the boilerplate suffix "— Requirements, Cost & How to Apply"
  only on the highest-impression pages.

### c) Content depth (helpful-content)
- Enrich the 43 thinnest EN combinatorial pages with nationality-specific
  detail (embassy locations, typical approval rates, document specifics).
- Ensure every page answers the searcher's exact question better than
  competitors (Google's core self-assessment question).

### d) Minor
- 76 utility/legal pages lack JSON-LD (low value — optional).
- 1 zh page missing H1 (zh/destination.html).
- 2 EN pages intentionally noindex (disclaimer, legal-notice) — correct.

---

## 5. Expected impact

Fixing descriptions on ~132k description-less impressions: even a conservative
2% CTR ≈ **+2,600 clicks/month** — more than the site's current total. Title
de-duplication improves crawl clarity and avoids same-title cannibalisation in
zh/ko/ja. Monitor GSC ~1 week after Google re-crawls (lastmod bumped), and
allow several weeks for core-update effects to settle.

## 6. Reusable tooling
- `seo_audit.py` — order-independent technical/on-page audit → SEO_AUDIT_REPORT.md
- `seo_meta_descriptions.py` — content-derived meta descriptions (idempotent)
- `fix_seo_issues.py` — strip-HTML descriptions, JSON-LD escapes, OG tags
- `fix_titles_dedup.py` — restore destination name in zh/ko/ja titles
- `bump_sitemap_lastmod.py` — targeted lastmod refresh
