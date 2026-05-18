"""LLM translation pipeline for evisa-card.com.

Translates the English content of non-EN HTML pages into the target language
using the Anthropic Claude API, then flips the page from noindex to index.

Usage:
    set ANTHROPIC_API_KEY=sk-ant-...
    python translate_pipeline.py --lang fr --limit 5      # test on 5 pages
    python translate_pipeline.py --lang fr                # whole language
    python translate_pipeline.py --all                    # all 9 languages

Design:
- One API call per page; all translatable segments sent together.
- Segments: <title>, meta description, og:title, og:description,
  the inner HTML of <article>, and JSON-LD FAQPage Q&A.
- HTML structure is preserved; only visible text is translated.
- Progress is tracked in .translation_progress/{lang}.json so the run resumes.
- Concurrency via ThreadPoolExecutor.
- After a page is translated, its robots meta is set back to index,follow.
"""
import os, re, sys, json, glob, time, argparse, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import anthropic
except ImportError:
    sys.exit('Run: pip install anthropic')

ROOT = r'C:\Users\chemi\Documents\evisa\pacific-main'
MODEL = os.environ.get('TRANSLATE_MODEL', 'claude-haiku-4-5')
WORKERS = int(os.environ.get('TRANSLATE_WORKERS', '8'))
PROGRESS_DIR = os.path.join(ROOT, '.translation_progress')

LANG_NAMES = {
    'fr': 'French', 'es': 'Spanish', 'pt': 'Portuguese (Brazil)',
    'zh': 'Simplified Chinese', 'th': 'Thai', 'ru': 'Russian',
    'ar': 'Arabic', 'ja': 'Japanese', 'ko': 'Korean',
}

SYSTEM_PROMPT = """You are a professional translator specialising in travel, \
visa and immigration content for a multilingual website (evisa-card.com).

You translate from English into {lang_name}.

RULES:
1. Translate ONLY visible human-readable text. Never translate or alter:
   - HTML tags, attributes, class names, IDs, inline styles
   - URLs, file paths, email addresses
   - Country/city proper nouns stay standard in the target language
   - Brand names: "eVisa-Card.com", "ETIAS", "eVisa", "Schengen"
   - Currency codes (USD, EUR), numbers, dates
2. Preserve every HTML tag exactly as-is, including <span class="fi fi-xx">
   flag icons and all attributes. Only the text BETWEEN tags changes.
3. Keep HTML entities valid (&amp; &mdash; &gt; etc.).
4. Use natural, fluent, SEO-friendly phrasing a native speaker would search.
5. Keep the same meaning and tone (informative, trustworthy).
6. For Arabic, produce correct right-to-left text (the page already has dir="rtl").
7. Return ONLY a valid JSON object, no commentary, no markdown fences.

You will receive a JSON object with keys to translate. Return a JSON object \
with the SAME keys, each value being the translated version. For "article_html" \
return the same HTML with only the visible text translated."""

client = None
_print_lock = threading.Lock()


def log(msg):
    with _print_lock:
        print(msg, flush=True)


def extract_segments(html):
    """Pull translatable segments out of a page. Returns (segments, anchors)."""
    seg = {}
    anchors = {}

    m = re.search(r'<title>(.*?)</title>', html, re.S | re.I)
    if m:
        seg['title'] = m.group(1).strip()
        anchors['title'] = m.group(0)

    m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*>', html, re.I)
    if not m:
        m = re.search(r'<meta[^>]*content=["\'][^"\']*["\'][^>]*name=["\']description["\'][^>]*>', html, re.I)
    if m:
        c = re.search(r'content=["\']([^"\']*)["\']', m.group(0))
        if c:
            seg['meta_description'] = c.group(1)
            anchors['meta_description'] = (m.group(0), c.group(1))

    for prop in ('og:title', 'og:description'):
        mm = re.search(rf'<meta[^>]*property=["\']{re.escape(prop)}["\'][^>]*>', html, re.I)
        if mm:
            c = re.search(r'content=["\']([^"\']*)["\']', mm.group(0))
            if c:
                key = prop.replace(':', '_')
                seg[key] = c.group(1)
                anchors[key] = (mm.group(0), c.group(1))

    m = re.search(r'<article[^>]*>(.*?)</article>', html, re.S | re.I)
    if m:
        seg['article_html'] = m.group(1).strip()
        anchors['article_html'] = m.group(0)
        anchors['article_open'] = m.group(0)[:m.group(0).index('>') + 1]

    # JSON-LD FAQPage
    faq_blocks = []
    for sm in re.finditer(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                          html, re.S | re.I):
        raw = sm.group(1).strip()
        try:
            data = json.loads(raw)
        except Exception:
            continue
        if isinstance(data, dict) and data.get('@type') == 'FAQPage':
            faq_blocks.append((sm.group(0), raw, data))
    if faq_blocks:
        seg['faq'] = []
        for _, _, data in faq_blocks:
            for q in data.get('mainEntity', []):
                seg['faq'].append({
                    'q': q.get('name', ''),
                    'a': q.get('acceptedAnswer', {}).get('text', ''),
                })
        anchors['faq'] = faq_blocks
    return seg, anchors


def translate_segments(seg, lang_code):
    """Call Claude to translate the segment dict. Returns translated dict."""
    payload = {k: v for k, v in seg.items()}
    user_msg = json.dumps(payload, ensure_ascii=False)
    system = SYSTEM_PROMPT.format(lang_name=LANG_NAMES[lang_code])

    for attempt in range(4):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=8192,
                system=[{'type': 'text', 'text': system,
                         'cache_control': {'type': 'ephemeral'}}],
                messages=[{'role': 'user',
                           'content': 'Translate this JSON object:\n' + user_msg}],
            )
            text = resp.content[0].text.strip()
            text = re.sub(r'^```(?:json)?\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            return json.loads(text)
        except (json.JSONDecodeError, anthropic.APIError, anthropic.APIStatusError) as e:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    return None


def apply_translation(html, anchors, tr):
    """Rebuild the HTML with translated segments and flip noindex -> index."""
    out = html

    if 'title' in anchors and 'title' in tr:
        out = out.replace(anchors['title'], f'<title>{tr["title"]}</title>', 1)

    if 'meta_description' in anchors and 'meta_description' in tr:
        orig_tag, orig_val = anchors['meta_description']
        new_tag = orig_tag.replace(orig_val, _attr_escape(tr['meta_description']))
        out = out.replace(orig_tag, new_tag, 1)

    for key in ('og_title', 'og_description'):
        if key in anchors and key in tr:
            orig_tag, orig_val = anchors[key]
            new_tag = orig_tag.replace(orig_val, _attr_escape(tr[key]))
            out = out.replace(orig_tag, new_tag, 1)

    if 'article_html' in anchors and 'article_html' in tr:
        open_tag = anchors.get('article_open', '<article>')
        out = out.replace(anchors['article_html'],
                          f'{open_tag}{tr["article_html"]}</article>', 1)

    if 'faq' in anchors and 'faq' in tr:
        flat = tr['faq']
        idx = 0
        for orig_block, raw, data in anchors['faq']:
            new_data = json.loads(raw)
            for q in new_data.get('mainEntity', []):
                if idx < len(flat):
                    q['name'] = flat[idx].get('q', q.get('name', ''))
                    q.setdefault('acceptedAnswer', {})['text'] = flat[idx].get('a', '')
                    idx += 1
            new_block = re.sub(
                r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>).*?(</script>)',
                lambda m: m.group(1) + '\n    ' + json.dumps(new_data, ensure_ascii=False) + '\n    ' + m.group(2),
                orig_block, count=1, flags=re.S)
            out = out.replace(orig_block, new_block, 1)

    # Flip noindex -> index (translation done)
    out = re.sub(r'(<meta[^>]*name=["\']robots["\'][^>]*content=["\'])noindex',
                 r'\1index', out, count=1, flags=re.I)
    out = re.sub(r'(<meta[^>]*content=["\'])noindex(,?\s*follow["\'][^>]*name=["\']robots["\'])',
                 r'\1index\2', out, count=1, flags=re.I)
    return out


def _attr_escape(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


def process_page(path, lang_code):
    with open(path, encoding='utf-8') as f:
        html = f.read()
    seg, anchors = extract_segments(html)
    if not seg:
        return 'skip-empty'
    tr = translate_segments(seg, lang_code)
    if not tr:
        return 'fail'
    new_html = apply_translation(html, anchors, tr)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    return 'ok'


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
    files = sorted(glob.glob(os.path.join(ROOT, 'www', lang, '*.html')))
    done = load_progress(lang)
    todo = [f for f in files if os.path.basename(f) not in done]
    if limit:
        todo = todo[:limit]
    log(f'[{lang}] {len(files)} pages total, {len(done)} done, processing {len(todo)}')

    ok = fail = 0
    done_lock = threading.Lock()
    counter = [0]

    def worker(path):
        nonlocal ok, fail
        try:
            res = process_page(path, lang)
        except Exception as e:
            res = f'error: {e}'
        with done_lock:
            counter[0] += 1
            if res == 'ok':
                ok += 1
                done.add(os.path.basename(path))
            else:
                fail += 1
                log(f'[{lang}] FAIL {os.path.basename(path)}: {res}')
            if counter[0] % 50 == 0:
                save_progress(lang, done)
                log(f'[{lang}] progress {counter[0]}/{len(todo)} (ok={ok} fail={fail})')

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        list(ex.map(worker, todo))

    save_progress(lang, done)
    log(f'[{lang}] DONE — ok={ok} fail={fail}')
    return ok, fail


def main():
    global client
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', help='language code (fr/es/pt/zh/th/ru/ar/ja/ko)')
    ap.add_argument('--all', action='store_true', help='all 9 languages')
    ap.add_argument('--limit', type=int, help='max pages (for testing)')
    args = ap.parse_args()

    key = os.environ.get('ANTHROPIC_API_KEY')
    if not key:
        sys.exit('ERROR: set ANTHROPIC_API_KEY environment variable')
    client = anthropic.Anthropic(api_key=key)

    if args.all:
        langs = list(LANG_NAMES)
    elif args.lang:
        langs = [args.lang]
    else:
        sys.exit('Specify --lang XX or --all')

    grand_ok = grand_fail = 0
    for lang in langs:
        o, f = run_language(lang, args.limit)
        grand_ok += o
        grand_fail += f
    log(f'\nALL DONE — ok={grand_ok} fail={grand_fail}')


if __name__ == '__main__':
    main()
