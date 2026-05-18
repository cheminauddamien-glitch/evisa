"""FREE offline translation pipeline for evisa-card.com using Argos Translate.

No API key, no cost, no limits. Translates the English content of each page
into the target language, preserving all HTML structure.

Usage:
    python translate_argos.py --lang fr --limit 5      # test on 5 pages
    python translate_argos.py --lang fr                # whole language
    python translate_argos.py --all                    # all 9 languages

How it works:
- Source of truth = www/en/<file>. Translated text is written into
  www/<lang>/<file>, preserving that file's lang attr, hreflang, canonical,
  og:url and language-dropdown state.
- HTML structure is preserved: an HTMLParser walks the markup and translates
  only visible text nodes (never tags, attributes, scripts, styles).
- A per-language on-disk cache (.translation_cache/<lang>.json) means every
  unique English string is translated only once — massive speed-up on the
  heavily-templated page set.
- Resumable: .translation_progress/<lang>.json tracks completed files.
- After a page is translated its robots meta is flipped noindex -> index.
"""
import os, re, sys, json, glob, time, argparse
from html.parser import HTMLParser

import argostranslate.translate as argt

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'
PROGRESS_DIR = os.path.join(ROOT, '.translation_progress')
CACHE_DIR = os.path.join(ROOT, '.translation_cache')

LANG_NAMES = {
    'fr': 'French', 'es': 'Spanish', 'pt': 'Portuguese', 'zh': 'Chinese',
    'th': 'Thai', 'ru': 'Russian', 'ar': 'Arabic', 'ja': 'Japanese', 'ko': 'Korean',
}

# Strings that must never be translated (brand, codes).
DO_NOT_TRANSLATE = {
    'eVisa-Card.com', 'evisa-card.com', 'ETIAS', 'eVisa', 'Schengen',
    'English', 'Français', 'Español', 'Português', '中文', 'ไทย',
    'Русский', 'العربية', '日本語', '한국어', 'Menu',
}

SKIP_TAGS = {'script', 'style'}
VOID_TAGS = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'area', 'col', 'base'}


class _Cache:
    def __init__(self, lang):
        self.lang = lang
        self.path = os.path.join(CACHE_DIR, f'{lang}.json')
        self.data = {}
        self.dirty = 0
        if os.path.exists(self.path):
            try:
                with open(self.path, encoding='utf-8') as f:
                    self.data = json.load(f)
            except Exception:
                self.data = {}

    def translate(self, text):
        key = text.strip()
        if not key:
            return text
        if key in DO_NOT_TRANSLATE:
            return text
        # Pure number / code — skip
        if re.fullmatch(r'[\d\W]+', key):
            return text
        if key in self.data:
            return self.data[key]
        try:
            out = argt.translate(key, 'en', self.lang)
        except Exception:
            out = key
        self.data[key] = out
        self.dirty += 1
        if self.dirty >= 200:
            self.save()
        return out

    def save(self):
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)
        self.dirty = 0


class HTMLTextTranslator(HTMLParser):
    """Walks HTML, translating visible text nodes only."""
    def __init__(self, translate_fn):
        super().__init__(convert_charrefs=False)
        self.tr = translate_fn
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        self.out.append(self.get_starttag_text())
        if tag in SKIP_TAGS:
            self.skip += 1

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag not in VOID_TAGS:
            self.out.append(f'</{tag}>')
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if self.skip or not data.strip():
            self.out.append(data)
            return
        lead = data[:len(data) - len(data.lstrip())]
        trail = data[len(data.rstrip()):]
        self.out.append(lead + self.tr(data.strip()) + trail)

    def handle_entityref(self, name):
        self.out.append(f'&{name};')

    def handle_charref(self, name):
        self.out.append(f'&#{name};')

    def handle_comment(self, data):
        self.out.append(f'<!--{data}-->')

    def handle_decl(self, decl):
        self.out.append(f'<!{decl}>')

    def result(self):
        return ''.join(self.out)


def translate_html_fragment(fragment, cache):
    p = HTMLTextTranslator(cache.translate)
    p.feed(fragment)
    p.close()
    return p.result()


def attr_escape(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


# ---- segment extraction (English source) ----------------------------------

def extract(html):
    seg, anch = {}, {}
    m = re.search(r'<title>(.*?)</title>', html, re.S | re.I)
    if m:
        seg['title'] = m.group(1)
        anch['title'] = m.group(0)

    m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', html, re.I)
    if m:
        c = re.search(r'content=["\']([^"\']*)["\']', m.group(0))
        if c:
            seg['meta'] = c.group(1)
            anch['meta'] = (m.group(0), c.group(1))

    for prop in ('og:title', 'og:description'):
        mm = re.search(rf'<meta[^>]*property=["\']{re.escape(prop)}["\'][^>]*>', html, re.I)
        if mm:
            c = re.search(r'content=["\']([^"\']*)["\']', mm.group(0))
            if c:
                seg[prop] = c.group(1)
                anch[prop] = (mm.group(0), c.group(1))

    m = re.search(r'(<article[^>]*>)(.*?)(</article>)', html, re.S | re.I)
    if m:
        seg['article'] = m.group(2)
        anch['article'] = (m.group(1), m.group(2), m.group(3))
    else:
        # Fallback for pages with no <article>: translate the main content
        # region between </nav> and <footer>.
        fm = re.search(r'(</nav>)(.*?)(<footer)', html, re.S | re.I)
        if fm and fm.group(2).strip():
            seg['body'] = fm.group(2)
            anch['body'] = fm.group(2)
    return seg, anch


def faq_blocks(html):
    blocks = []
    for sm in re.finditer(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                          html, re.S | re.I):
        raw = sm.group(1).strip()
        try:
            data = json.loads(raw)
        except Exception:
            continue
        if isinstance(data, dict) and data.get('@type') == 'FAQPage':
            blocks.append((sm.group(0), data))
    return blocks


def apply_to_target(target_html, en_seg, en_anch, en_html, cache):
    """Translate English segments, write them into the target-language file."""
    out = target_html

    # title
    if 'title' in en_seg:
        tt = translate_html_fragment(en_seg['title'], cache)
        m = re.search(r'<title>.*?</title>', out, re.S | re.I)
        if m:
            out = out.replace(m.group(0), f'<title>{tt}</title>', 1)

    # meta description
    if 'meta' in en_seg:
        tv = cache.translate(en_seg['meta'])
        m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', out, re.I)
        if m:
            c = re.search(r'(content=["\'])([^"\']*)(["\'])', m.group(0))
            if c:
                newtag = m.group(0).replace(c.group(0),
                                            c.group(1) + attr_escape(tv) + c.group(3))
                out = out.replace(m.group(0), newtag, 1)

    # og tags
    for prop in ('og:title', 'og:description'):
        if prop in en_seg:
            tv = cache.translate(en_seg[prop])
            m = re.search(rf'<meta[^>]*property=["\']{re.escape(prop)}["\'][^>]*>', out, re.I)
            if m:
                c = re.search(r'(content=["\'])([^"\']*)(["\'])', m.group(0))
                if c:
                    newtag = m.group(0).replace(c.group(0),
                                                c.group(1) + attr_escape(tv) + c.group(3))
                    out = out.replace(m.group(0), newtag, 1)

    # article body
    if 'article' in en_seg:
        translated = translate_html_fragment(en_seg['article'], cache)
        m = re.search(r'(<article[^>]*>)(.*?)(</article>)', out, re.S | re.I)
        if m:
            out = out.replace(m.group(0), m.group(1) + translated + m.group(3), 1)

    # body fallback (pages without <article>)
    if 'body' in en_seg:
        translated = translate_html_fragment(en_seg['body'], cache)
        m = re.search(r'(</nav>)(.*?)(<footer)', out, re.S | re.I)
        if m:
            out = out.replace(m.group(0), m.group(1) + translated + m.group(3), 1)

    # JSON-LD FAQ
    en_faq = faq_blocks(en_html)
    tgt_faq = faq_blocks(out)
    if en_faq and tgt_faq:
        for (en_block, en_data), (tg_block, _) in zip(en_faq, tgt_faq):
            new_data = json.loads(json.dumps(en_data))  # deep copy
            for q in new_data.get('mainEntity', []):
                if 'name' in q:
                    q['name'] = cache.translate(q['name'])
                aa = q.get('acceptedAnswer', {})
                if 'text' in aa:
                    aa['text'] = cache.translate(aa['text'])
            new_block = re.sub(
                r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>).*?(</script>)',
                lambda mm: mm.group(1) + '\n    ' + json.dumps(new_data, ensure_ascii=False)
                           + '\n    ' + mm.group(2),
                tg_block, count=1, flags=re.S)
            out = out.replace(tg_block, new_block, 1)

    # flip noindex -> index
    out = re.sub(r'(name=["\']robots["\'][^>]*content=["\'])noindex',
                 r'\1index', out, count=1, flags=re.I)
    out = re.sub(r'(content=["\'])noindex(\s*,?\s*follow["\'][^>]*name=["\']robots["\'])',
                 r'\1index\2', out, count=1, flags=re.I)
    return out


def load_progress(lang):
    p = os.path.join(PROGRESS_DIR, f'{lang}.json')
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            return set(json.load(f))
    return set()


def save_progress(lang, done):
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    with open(os.path.join(PROGRESS_DIR, f'{lang}.json'), 'w', encoding='utf-8') as f:
        json.dump(sorted(done), f)


def run_language(lang, limit=None):
    cache = _Cache(lang)
    done = load_progress(lang)
    tgt_files = sorted(glob.glob(os.path.join(ROOT, 'www', lang, '*.html')))
    todo = [f for f in tgt_files if os.path.basename(f) not in done]
    if limit:
        todo = todo[:limit]
    print(f'[{lang}] {len(tgt_files)} pages, {len(done)} done, processing {len(todo)}', flush=True)

    ok = fail = 0
    t0 = time.time()
    for i, tgt in enumerate(todo, 1):
        bn = os.path.basename(tgt)
        en_path = os.path.join(ROOT, 'www', 'en', bn)
        try:
            with open(tgt, encoding='utf-8') as f:
                tgt_html = f.read()
            src_path = en_path if os.path.exists(en_path) else tgt
            with open(src_path, encoding='utf-8') as f:
                en_html = f.read()
            en_seg, en_anch = extract(en_html)
            new_html = apply_to_target(tgt_html, en_seg, en_anch, en_html, cache)
            with open(tgt, 'w', encoding='utf-8') as f:
                f.write(new_html)
            done.add(bn)
            ok += 1
        except Exception as e:
            fail += 1
            print(f'[{lang}] FAIL {bn}: {e}', flush=True)
        if i % 25 == 0:
            cache.save()
            save_progress(lang, done)
            rate = i / (time.time() - t0)
            eta = (len(todo) - i) / rate / 60 if rate else 0
            print(f'[{lang}] {i}/{len(todo)} ok={ok} fail={fail} '
                  f'cache={len(cache.data)} {rate:.1f}p/s ETA {eta:.0f}min', flush=True)

    cache.save()
    save_progress(lang, done)
    print(f'[{lang}] DONE ok={ok} fail={fail} cache_size={len(cache.data)}', flush=True)
    return ok, fail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--limit', type=int)
    args = ap.parse_args()

    langs = list(LANG_NAMES) if args.all else ([args.lang] if args.lang else None)
    if not langs:
        sys.exit('Specify --lang XX or --all')

    go = gf = 0
    for lang in langs:
        if lang not in LANG_NAMES:
            print(f'skip unknown lang {lang}'); continue
        o, f = run_language(lang, args.limit)
        go += o; gf += f
    print(f'\nALL DONE ok={go} fail={gf}', flush=True)


if __name__ == '__main__':
    main()
