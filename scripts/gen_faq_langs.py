#!/usr/bin/env python3
"""Generate FAQ pages for all non-EN languages by copying EN FAQ and updating metadata."""
import os, re

WWW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "www")
SRC = os.path.join(WWW, "en", "faq.html")

LANGS = {
    "fr": {"html_lang": "fr", "title": "FAQ Visa 2026 — Questions Fr\u00e9quentes sur les Visas et eVisas",
           "desc": "R\u00e9ponses \u00e0 50+ questions fr\u00e9quentes sur les visas, eVisas, Schengen, frais, d\u00e9lais, extensions et refus en 2026.",
           "h1": "FAQ Visa &mdash; Questions Fr\u00e9quentes",
           "intro": "Retrouvez les r\u00e9ponses aux questions les plus courantes sur les visas, eVisas, voyages Schengen, documents, d\u00e9lais de traitement, extensions et plus. Mis \u00e0 jour pour 2026.",
           "cta_title": "Encore des questions ?", "cta_text": "Parcourez nos guides par destination pour les conditions de visa sp\u00e9cifiques.",
           "btn_dest": "Voir les Destinations", "btn_checklist": "Liste des Documents"},
    "es": {"html_lang": "es", "title": "FAQ Visa 2026 — Preguntas Frecuentes sobre Visas y eVisas",
           "desc": "Respuestas a 50+ preguntas frecuentes sobre visas, eVisas, Schengen, tasas, tiempos, extensiones y rechazos en 2026.",
           "h1": "FAQ Visa &mdash; Preguntas Frecuentes",
           "intro": "Encuentre respuestas a las preguntas m\u00e1s comunes sobre visas, eVisas, viajes Schengen, documentos, tiempos de procesamiento, extensiones y m\u00e1s. Actualizado para 2026.",
           "cta_title": "\u00bfA\u00fan tiene preguntas?", "cta_text": "Explore nuestras gu\u00edas por destino para requisitos espec\u00edficos.",
           "btn_dest": "Ver Destinos", "btn_checklist": "Lista de Documentos"},
    "pt": {"html_lang": "pt", "title": "FAQ Visto 2026 — Perguntas Frequentes sobre Vistos e eVisas",
           "desc": "Respostas a 50+ perguntas frequentes sobre vistos, eVisas, Schengen, taxas, prazos, extens\u00f5es e recusas em 2026.",
           "h1": "FAQ Visto &mdash; Perguntas Frequentes",
           "intro": "Encontre respostas para as perguntas mais comuns sobre vistos, eVisas, viagens Schengen, documentos, prazos de processamento, extens\u00f5es e mais. Atualizado para 2026.",
           "cta_title": "Ainda tem d\u00favidas?", "cta_text": "Explore nossos guias por destino para requisitos espec\u00edficos.",
           "btn_dest": "Ver Destinos", "btn_checklist": "Lista de Documentos"},
    "ar": {"html_lang": "ar", "title": "\u0623\u0633\u0626\u0644\u0629 \u0634\u0627\u0626\u0639\u0629 \u062d\u0648\u0644 \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0627\u062a 2026 — \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0627\u062a \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a\u0629 \u0648\u0634\u0646\u063a\u0646",
           "desc": "\u0625\u062c\u0627\u0628\u0627\u062a \u0639\u0644\u0649 \u0623\u0643\u062b\u0631 \u0645\u0646 50 \u0633\u0624\u0627\u0644\u0627\u064b \u0634\u0627\u0626\u0639\u0627\u064b \u062d\u0648\u0644 \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0627\u062a \u0648\u0634\u0646\u063a\u0646 \u0648\u0627\u0644\u0631\u0633\u0648\u0645 \u0648\u0627\u0644\u0645\u0648\u0627\u0639\u064a\u062f \u0641\u064a 2026.",
           "h1": "\u0623\u0633\u0626\u0644\u0629 \u0634\u0627\u0626\u0639\u0629 &mdash; \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0627\u062a \u0648\u0627\u0644\u0633\u0641\u0631",
           "intro": "\u0627\u0639\u062b\u0631 \u0639\u0644\u0649 \u0625\u062c\u0627\u0628\u0627\u062a \u0644\u0623\u0643\u062b\u0631 \u0627\u0644\u0623\u0633\u0626\u0644\u0629 \u0634\u064a\u0648\u0639\u0627\u064b \u062d\u0648\u0644 \u0627\u0644\u062a\u0623\u0634\u064a\u0631\u0627\u062a. \u0645\u062d\u062f\u0651\u062b \u0644\u0639\u0627\u0645 2026.",
           "cta_title": "\u0644\u0627 \u062a\u0632\u0627\u0644 \u0644\u062f\u064a\u0643 \u0623\u0633\u0626\u0644\u0629\u061f", "cta_text": "\u062a\u0635\u0641\u062d \u0623\u062f\u0644\u0629 \u0627\u0644\u0648\u062c\u0647\u0627\u062a.",
           "btn_dest": "\u0627\u0644\u0648\u062c\u0647\u0627\u062a", "btn_checklist": "\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u0633\u062a\u0646\u062f\u0627\u062a"},
    "ja": {"html_lang": "ja", "title": "\u30d3\u30b6FAQ 2026 \u2014 \u30d3\u30b6\u30fbeVisa\u306b\u95a2\u3059\u308b\u3088\u304f\u3042\u308b\u8cea\u554f",
           "desc": "\u30d3\u30b6\u3001eVisa\u3001\u30b7\u30a7\u30f3\u30b2\u30f3\u3001\u624b\u6570\u6599\u3001\u51e6\u7406\u6642\u9593\u306b\u95a2\u305950\u4ee5\u4e0a\u306e\u3088\u304f\u3042\u308b\u8cea\u554f\u3078\u306e\u56de\u7b54\u30022026\u5e74\u7248\u3002",
           "h1": "\u30d3\u30b6FAQ &mdash; \u3088\u304f\u3042\u308b\u8cea\u554f",
           "intro": "\u30d3\u30b6\u3001eVisa\u3001\u30b7\u30a7\u30f3\u30b2\u30f3\u65c5\u884c\u3001\u5fc5\u8981\u66f8\u985e\u3001\u51e6\u7406\u6642\u9593\u306a\u3069\u306b\u95a2\u3059\u308b\u3088\u304f\u3042\u308b\u8cea\u554f\u3078\u306e\u56de\u7b54\u30022026\u5e74\u66f4\u65b0\u3002",
           "cta_title": "\u307e\u3060\u8cea\u554f\u304c\u3042\u308a\u307e\u3059\u304b\uff1f", "cta_text": "\u56fd\u5225\u306e\u30d3\u30b6\u8981\u4ef6\u306f\u30c7\u30b9\u30c6\u30a3\u30cd\u30fc\u30b7\u30e7\u30f3\u30ac\u30a4\u30c9\u3092\u3054\u89a7\u304f\u3060\u3055\u3044\u3002",
           "btn_dest": "\u76ee\u7684\u5730\u4e00\u89a7", "btn_checklist": "\u66f8\u985e\u30c1\u30a7\u30c3\u30af\u30ea\u30b9\u30c8"},
    "ko": {"html_lang": "ko", "title": "\ube44\uc790 FAQ 2026 \u2014 \ube44\uc790 \ubc0f eVisa \uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38",
           "desc": "\ube44\uc790, eVisa, \uc194\uac90, \uc218\uc218\ub8cc, \ucc98\ub9ac \uc2dc\uac04\uc5d0 \ub300\ud55c 50\uac1c \uc774\uc0c1\uc758 \uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38. 2026\ub144 \uc5c5\ub370\uc774\ud2b8.",
           "h1": "\ube44\uc790 FAQ &mdash; \uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38",
           "intro": "\ube44\uc790, eVisa, \uc194\uac90 \uc5ec\ud589, \ud544\uc694 \uc11c\ub958, \ucc98\ub9ac \uc2dc\uac04 \ub4f1\uc5d0 \ub300\ud55c \uc790\uc8fc \ubb3b\ub294 \uc9c8\ubb38\uc5d0 \ub300\ud55c \ub2f5\ubcc0. 2026\ub144 \uc5c5\ub370\uc774\ud2b8.",
           "cta_title": "\uc544\uc9c1 \uad81\uae08\ud55c \uc810\uc774 \uc788\uc73c\uc2e0\uac00\uc694?", "cta_text": "\uad6d\uac00\ubcc4 \ube44\uc790 \uc694\uac74\uc740 \ubaa9\uc801\uc9c0 \uac00\uc774\ub4dc\ub97c \ucc38\uc870\ud558\uc138\uc694.",
           "btn_dest": "\ubaa9\uc801\uc9c0", "btn_checklist": "\uc11c\ub958 \uccb4\ud06c\ub9ac\uc2a4\ud2b8"},
    "ru": {"html_lang": "ru", "title": "\u0427\u0430\u0412\u041e \u043e \u0432\u0438\u0437\u0430\u0445 2026 \u2014 \u0427\u0430\u0441\u0442\u043e \u0437\u0430\u0434\u0430\u0432\u0430\u0435\u043c\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b",
           "desc": "\u041e\u0442\u0432\u0435\u0442\u044b \u043d\u0430 50+ \u0447\u0430\u0441\u0442\u043e \u0437\u0430\u0434\u0430\u0432\u0430\u0435\u043c\u044b\u0445 \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432 \u043e \u0432\u0438\u0437\u0430\u0445, eVisa, \u0428\u0435\u043d\u0433\u0435\u043d\u0435, \u0441\u0431\u043e\u0440\u0430\u0445 \u0438 \u0441\u0440\u043e\u043a\u0430\u0445 \u0432 2026.",
           "h1": "\u0427\u0430\u0412\u041e &mdash; \u0427\u0430\u0441\u0442\u043e \u0437\u0430\u0434\u0430\u0432\u0430\u0435\u043c\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b",
           "intro": "\u041e\u0442\u0432\u0435\u0442\u044b \u043d\u0430 \u0441\u0430\u043c\u044b\u0435 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0451\u043d\u043d\u044b\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043e \u0432\u0438\u0437\u0430\u0445, eVisa, \u0448\u0435\u043d\u0433\u0435\u043d\u0441\u043a\u0438\u0445 \u043f\u043e\u0435\u0437\u0434\u043a\u0430\u0445 \u0438 \u043f\u0440\u043e\u0447\u0435\u043c. \u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e \u043d\u0430 2026 \u0433\u043e\u0434.",
           "cta_title": "\u0415\u0449\u0451 \u0435\u0441\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441\u044b?", "cta_text": "\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0438\u0442\u0435 \u043d\u0430\u0448\u0438 \u0433\u0438\u0434\u044b \u043f\u043e \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u043c.",
           "btn_dest": "\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", "btn_checklist": "\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432"},
    "th": {"html_lang": "th", "title": "\u0e04\u0e33\u0e16\u0e32\u0e21\u0e17\u0e35\u0e48\u0e1e\u0e1a\u0e1a\u0e48\u0e2d\u0e22\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e27\u0e35\u0e0b\u0e48\u0e32 2026",
           "desc": "\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e33\u0e16\u0e32\u0e21\u0e17\u0e35\u0e48\u0e1e\u0e1a\u0e1a\u0e48\u0e2d\u0e22\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e27\u0e35\u0e0b\u0e48\u0e32 eVisa \u0e40\u0e0a\u0e07\u0e40\u0e01\u0e49\u0e19 \u0e04\u0e48\u0e32\u0e18\u0e23\u0e23\u0e21\u0e40\u0e19\u0e35\u0e22\u0e21 \u0e41\u0e25\u0e30\u0e23\u0e30\u0e22\u0e30\u0e40\u0e27\u0e25\u0e32\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e01\u0e32\u0e23 2026",
           "h1": "\u0e04\u0e33\u0e16\u0e32\u0e21\u0e17\u0e35\u0e48\u0e1e\u0e1a\u0e1a\u0e48\u0e2d\u0e22 &mdash; \u0e27\u0e35\u0e0b\u0e48\u0e32\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e40\u0e14\u0e34\u0e19\u0e17\u0e32\u0e07",
           "intro": "\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e04\u0e33\u0e15\u0e2d\u0e1a\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e04\u0e33\u0e16\u0e32\u0e21\u0e17\u0e35\u0e48\u0e1e\u0e1a\u0e1a\u0e48\u0e2d\u0e22\u0e17\u0e35\u0e48\u0e2a\u0e38\u0e14\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e27\u0e35\u0e0b\u0e48\u0e32 \u0e2d\u0e31\u0e1e\u0e40\u0e14\u0e15 2026",
           "cta_title": "\u0e22\u0e31\u0e07\u0e21\u0e35\u0e04\u0e33\u0e16\u0e32\u0e21\u0e2d\u0e22\u0e39\u0e48?", "cta_text": "\u0e40\u0e23\u0e35\u0e22\u0e01\u0e14\u0e39\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e15\u0e32\u0e21\u0e08\u0e38\u0e14\u0e2b\u0e21\u0e32\u0e22",
           "btn_dest": "\u0e08\u0e38\u0e14\u0e2b\u0e21\u0e32\u0e22", "btn_checklist": "\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e2d\u0e01\u0e2a\u0e32\u0e23"},
    "zh": {"html_lang": "zh", "title": "\u7b7e\u8bc1\u5e38\u89c1\u95ee\u9898 2026 \u2014 \u7535\u5b50\u7b7e\u8bc1\u3001\u7533\u6839\u7b7e\u8bc1\u95ee\u7b54",
           "desc": "\u5173\u4e8e\u7b7e\u8bc1\u3001\u7535\u5b50\u7b7e\u8bc1\u3001\u7533\u6839\u3001\u8d39\u7528\u3001\u5904\u7406\u65f6\u95f4\u7b4950\u591a\u4e2a\u5e38\u89c1\u95ee\u9898\u7684\u89e3\u7b54\u30022026\u5e74\u66f4\u65b0\u3002",
           "h1": "\u7b7e\u8bc1\u5e38\u89c1\u95ee\u9898 &mdash; FAQ",
           "intro": "\u67e5\u627e\u5173\u4e8e\u7b7e\u8bc1\u3001\u7535\u5b50\u7b7e\u8bc1\u3001\u7533\u6839\u65c5\u884c\u3001\u6240\u9700\u6587\u4ef6\u3001\u5904\u7406\u65f6\u95f4\u7b49\u6700\u5e38\u89c1\u95ee\u9898\u7684\u89e3\u7b54\u30022026\u5e74\u66f4\u65b0\u3002",
           "cta_title": "\u8fd8\u6709\u95ee\u9898\uff1f", "cta_text": "\u6d4f\u89c8\u6211\u4eec\u7684\u76ee\u7684\u5730\u6307\u5357\u4e86\u89e3\u5404\u56fd\u7b7e\u8bc1\u8981\u6c42\u3002",
           "btn_dest": "\u76ee\u7684\u5730", "btn_checklist": "\u6587\u4ef6\u6e05\u5355"},
}

with open(SRC, "r", encoding="utf-8") as f:
    src_content = f.read()

count = 0
for lang, meta in LANGS.items():
    content = src_content

    # Update html lang
    content = content.replace('lang="en"', f'lang="{lang}"', 1)

    # Update title
    content = re.sub(r'<title>[^<]+</title>',
                     f'<title>{meta["title"]}</title>', content, count=1)

    # Update meta description
    content = re.sub(r'<meta name="description" content="[^"]+"/>',
                     f'<meta name="description" content="{meta["desc"]}"/>', content, count=1)

    # Update OG title
    content = re.sub(r'<meta property="og:title" content="[^"]+"/>',
                     f'<meta property="og:title" content="{meta["title"]}"/>', content, count=1)

    # Update OG description
    content = re.sub(r'<meta property="og:description" content="[^"]+"/>',
                     f'<meta property="og:description" content="{meta["desc"]}"/>', content, count=1)

    # Update canonical
    content = content.replace(
        'href="https://www.evisa-card.com/en/faq.html" rel="canonical"',
        f'href="https://www.evisa-card.com/{lang}/faq.html" rel="canonical"')

    # Update OG URL
    content = content.replace(
        '"https://www.evisa-card.com/en/faq.html" property="og:url"',
        f'"https://www.evisa-card.com/{lang}/faq.html" property="og:url"')

    # Update internal links from /en/ to /{lang}/
    content = content.replace('href="/en/', f'href="/{lang}/')

    # Update H1
    content = re.sub(r'<h1 class="mb-3 bread">[^<]+</h1>',
                     f'<h1 class="mb-3 bread">{meta["h1"]}</h1>', content, count=1)

    # Update intro text
    content = re.sub(r'Find answers to the most common questions.*?Updated for 2026\.',
                     meta["intro"], content, count=1)

    # Update CTA
    content = content.replace('Still have questions?', meta["cta_title"])
    content = content.replace('Browse our destination guides for country-specific visa requirements.', meta["cta_text"])
    content = content.replace('>Browse Destinations<', f'>{meta["btn_dest"]}<')
    content = content.replace('>Documents Checklist<', f'>{meta["btn_checklist"]}<')

    # Update active lang in dropdown
    content = content.replace(
        f'<a class="dropdown-item active" href="/en/faq.html">English</a>',
        f'<a class="dropdown-item" href="/en/faq.html">English</a>')
    content = content.replace(
        f'<a class="dropdown-item" href="/{lang}/faq.html">',
        f'<a class="dropdown-item active" href="/{lang}/faq.html">')

    # Update breadcrumb in schema
    content = content.replace(
        '"https://www.evisa-card.com/en/"',
        f'"https://www.evisa-card.com/{lang}/"')
    content = content.replace(
        '"https://www.evisa-card.com/en/faq.html"',
        f'"https://www.evisa-card.com/{lang}/faq.html"')

    # Write
    outpath = os.path.join(WWW, lang, "faq.html")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Done: {count} FAQ pages generated")
