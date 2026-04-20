#!/usr/bin/env python3
"""Apply full translations to FAQ pages for all non-EN languages.

Reads translation files from scripts/faq_translations_{lang}.py,
then rewrites each www/{lang}/faq.html with translated questions, answers,
and category headings while preserving the HTML structure.
"""
import os, re, sys, importlib.util

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
WWW = os.path.join(os.path.dirname(SCRIPTS_DIR), "www")

LANGS = ["fr", "es", "pt", "ar", "ja", "ko", "ru", "th", "zh"]


def load_translations(lang):
    """Dynamically load translation module for a language."""
    mod_path = os.path.join(SCRIPTS_DIR, f"faq_translations_{lang}.py")
    if not os.path.exists(mod_path):
        print(f"  SKIP {lang}: translation file not found")
        return None, None
    spec = importlib.util.spec_from_file_location(f"faq_translations_{lang}", mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CATEGORY_TRANSLATIONS, mod.FAQ_TRANSLATIONS


def apply_translations(lang):
    """Apply translations to a single language FAQ page."""
    cat_trans, faq_trans = load_translations(lang)
    if cat_trans is None:
        return False

    faq_path = os.path.join(WWW, lang, "faq.html")
    if not os.path.exists(faq_path):
        print(f"  SKIP {lang}: faq.html not found")
        return False

    with open(faq_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build lookup: English question -> translated question + answer
    q_key = f"q_{lang}"
    a_key = f"a_{lang}"
    trans_map = {}
    for item in faq_trans:
        q_en = item["q_en"]
        q_translated = item.get(q_key, q_en)
        a_translated = item.get(a_key, "")
        trans_map[q_en] = (q_translated, a_translated)

    # Replace category headings
    for en_cat, translated_cat in cat_trans.items():
        content = content.replace(f">{en_cat}<", f">{translated_cat}<")

    # Replace questions and answers
    # Pattern: button text (question) followed by card-body div (answer)
    for q_en, (q_translated, a_translated) in trans_map.items():
        # Escape special regex chars in q_en for matching
        q_escaped = re.escape(q_en)

        # Replace question text in button
        # Match: >Question text</button>
        pattern_q = f">{q_escaped}</button>"
        replacement_q = f">{q_translated}</button>"
        content = content.replace(f">{q_en}</button>", f">{q_translated}</button>")

        # Replace answer text in card-body
        # This is trickier - find the answer div that follows this question
        # Strategy: find the question, then replace the next card-body content
        if a_translated:
            # Find the card-body that follows this question's collapse div
            # We look for the pattern: question button ... <div class="card-body">ANSWER</div>
            # Since questions are unique, we can use them as anchors
            q_pattern = re.escape(q_translated)
            # Match: q_translated</button></h3></div>\n        <div id="..." class="collapse..." ...><div class="card-body">CONTENT</div></div>
            card_body_pattern = (
                f'{q_pattern}</button></h3></div>'
                r'\s*<div id="[^"]*" class="collapse[^"]*"[^>]*>'
                r'<div class="card-body">(.*?)</div></div>'
            )
            match = re.search(card_body_pattern, content, re.DOTALL)
            if match:
                old_answer = match.group(1)
                content = content.replace(
                    f'<div class="card-body">{old_answer}</div></div>',
                    f'<div class="card-body">{a_translated}</div></div>',
                    1
                )

    # Also update the FAQPage schema JSON-LD with translated Q&A
    # Find the FAQPage script block and replace Q&A
    schema_pattern = r'("@type":"FAQPage","mainEntity":\[)(.*?)(\])'
    schema_match = re.search(schema_pattern, content, re.DOTALL)
    if schema_match and faq_trans:
        schema_items = []
        for item in faq_trans:
            q = item.get(q_key, item["q_en"]).replace('"', '\\"')
            a = item.get(a_key, "").replace('"', '\\"').replace('\n', ' ')
            # Strip HTML tags from answer for schema
            a_clean = re.sub(r'<[^>]+>', '', a)
            schema_items.append(
                f'{{"@type":"Question","name":"{q}",'
                f'"acceptedAnswer":{{"@type":"Answer","text":"{a_clean}"}}}}'
            )
        new_schema = schema_match.group(1) + "\n      " + ",\n      ".join(schema_items) + "\n    " + schema_match.group(3)
        content = content[:schema_match.start()] + new_schema + content[schema_match.end():]

    with open(faq_path, "w", encoding="utf-8") as f:
        f.write(content)

    translated_count = sum(1 for q_en, (q_t, a_t) in trans_map.items() if q_t != q_en)
    print(f"  {lang}: {translated_count} questions translated")
    return True


def main():
    count = 0
    for lang in LANGS:
        try:
            if apply_translations(lang):
                count += 1
        except Exception as e:
            print(f"  ERROR {lang}: {e}")
            import traceback
            traceback.print_exc()

    print(f"\nDone: {count} languages processed")


if __name__ == "__main__":
    main()
