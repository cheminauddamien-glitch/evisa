"""Generate localized variants of patagonia-visa-requirements.html for all 10 languages.
Mirrors the existing site pattern: en full English; fr/es/pt translate
title+H1+H2 partially; ar/ja/ko/ru/th/zh pure English duplicate.
"""
import re, os

SRC = 'www/en/patagonia-visa-requirements.html'
with open(SRC, encoding='utf-8') as f:
    base = f.read()

LANGS = {
    'fr': {'lang_attr':'fr','flag':'fi-fr','label':'Français',
           'title':'Patagonie conditions de visa 2026 — Argentine &amp; Chili règles d&rsquo;entrée pour voyageurs',
           'h1':'Patagonie conditions de visa 2026 — Argentine &amp; Chili règles d&rsquo;entrée',
           'meta':'Patagonie conditions de visa 2026 : Argentine et Chili règles d&rsquo;entrée, séjour touristique 90 jours, postes-frontière, documents pour Torres del Paine, El Calafate et Ushuaia.',
           'h2':{
               'Why Patagonia Visa Rules Cover Two Countries':'Pourquoi les règles de visa Patagonie concernent deux pays',
               'Argentina Entry Requirements for Patagonia 2026':'Argentine conditions d&rsquo;entrée pour la Patagonie 2026',
               'Chile Entry Requirements for Patagonia 2026':'Chili conditions d&rsquo;entrée pour la Patagonie 2026',
               'Border Crossings Between Argentine and Chilean Patagonia':'Postes-frontière entre Patagonie argentine et chilienne',
               'Documents for Torres del Paine, El Calafate and Ushuaia':'Documents pour Torres del Paine, El Calafate et Ushuaia',
               'Who Needs a Visa for Patagonia in 2026':'Qui a besoin d&rsquo;un visa pour la Patagonie en 2026',
           }},
    'es': {'lang_attr':'es','flag':'fi-es','label':'Español',
           'title':'Patagonia requisitos de visa 2026 — Argentina y Chile reglas de entrada para viajeros',
           'h1':'Patagonia requisitos de visa 2026 — Argentina y Chile reglas de entrada',
           'meta':'Patagonia requisitos de visa 2026: Argentina y Chile reglas de entrada, estancia turística 90 días, pasos fronterizos, documentos para Torres del Paine, El Calafate y Ushuaia.',
           'h2':{
               'Why Patagonia Visa Rules Cover Two Countries':'Por qué las reglas de visa de Patagonia cubren dos países',
               'Argentina Entry Requirements for Patagonia 2026':'Argentina requisitos de entrada para Patagonia 2026',
               'Chile Entry Requirements for Patagonia 2026':'Chile requisitos de entrada para Patagonia 2026',
               'Border Crossings Between Argentine and Chilean Patagonia':'Pasos fronterizos entre Patagonia argentina y chilena',
               'Documents for Torres del Paine, El Calafate and Ushuaia':'Documentos para Torres del Paine, El Calafate y Ushuaia',
               'Who Needs a Visa for Patagonia in 2026':'Quién necesita visa para Patagonia en 2026',
           }},
    'pt': {'lang_attr':'pt','flag':'fi-br','label':'Português',
           'title':'Patagônia requisitos de visto 2026 — Argentina e Chile regras de entrada para viajantes',
           'h1':'Patagônia requisitos de visto 2026 — Argentina e Chile regras de entrada',
           'meta':'Patagônia requisitos de visto 2026: Argentina e Chile regras de entrada, estadia turística de 90 dias, postos fronteiriços, documentos para Torres del Paine, El Calafate e Ushuaia.',
           'h2':{
               'Why Patagonia Visa Rules Cover Two Countries':'Por que as regras de visto da Patagônia cobrem dois países',
               'Argentina Entry Requirements for Patagonia 2026':'Argentina requisitos de entrada para Patagônia 2026',
               'Chile Entry Requirements for Patagonia 2026':'Chile requisitos de entrada para Patagônia 2026',
               'Border Crossings Between Argentine and Chilean Patagonia':'Postos fronteiriços entre Patagônia argentina e chilena',
               'Documents for Torres del Paine, El Calafate and Ushuaia':'Documentos para Torres del Paine, El Calafate e Ushuaia',
               'Who Needs a Visa for Patagonia in 2026':'Quem precisa de visto para Patagônia em 2026',
           }},
    'ar': {'lang_attr':'ar','flag':'fi-sa','label':'العربية','dir':'rtl'},
    'zh': {'lang_attr':'zh','flag':'fi-cn','label':'中文'},
    'th': {'lang_attr':'th','flag':'fi-th','label':'ไทย'},
    'ru': {'lang_attr':'ru','flag':'fi-ru','label':'Русский'},
    'ja': {'lang_attr':'ja','flag':'fi-jp','label':'日本語'},
    'ko': {'lang_attr':'ko','flag':'fi-kr','label':'한국어'},
}

def localize(html, lang, cfg):
    out = html
    out = re.sub(r'<html lang="en">', f'<html lang="{cfg["lang_attr"]}"' + (' dir="rtl"' if cfg.get("dir") == "rtl" else '') + '>', out, count=1)

    # Move active class on language dropdown
    out = re.sub(r'(<a class="dropdown-item) active(" href="/en/patagonia-visa-requirements\.html">)',
                 r'\1\2', out)
    out = re.sub(rf'(<a class="dropdown-item)(" href="/{cfg["lang_attr"]}/patagonia-visa-requirements\.html">)',
                 r'\1 active\2', out)

    if 'title' in cfg:
        out = re.sub(r'<title>[^<]*</title>', f'<title>{cfg["title"]}</title>', out, count=1)
        out = out.replace(
            '<meta content="Patagonia visa requirements 2026: Argentina and Chile entry rules, 90-day tourist stay, border crossings, documents needed for Torres del Paine, El Calafate and Ushuaia." name="description"/>',
            f'<meta content="{cfg["meta"]}" name="description"/>'
        )
        out = out.replace(
            '<meta content="Patagonia Visa Requirements 2026 &mdash; Argentina &amp; Chile Entry Rules for Travelers" property="og:title" />',
            f'<meta content="{cfg["title"]}" property="og:title" />'
        )
        out = out.replace(
            '<meta content="Patagonia visa requirements 2026: Argentina and Chile entry rules, 90-day tourist stay, border crossings, documents needed for Torres del Paine, El Calafate and Ushuaia." property="og:description" />',
            f'<meta content="{cfg["meta"]}" property="og:description" />'
        )
        out = re.sub(
            r'(<h1><span class="fi fi-ar"></span><span class="fi fi-cl"></span>) Patagonia Visa Requirements 2026 &mdash; Argentina &amp; Chile Entry Rules</h1>',
            r'\1 ' + cfg["h1"] + r'</h1>',
            out
        )
        for en_h2, tr_h2 in cfg['h2'].items():
            out = re.sub(
                rf'(<h2 id="[^"]+">){re.escape(en_h2)}(</h2>)',
                rf'\g<1>{tr_h2}\g<2>',
                out
            )
    return out

for lang, cfg in LANGS.items():
    out = localize(base, lang, cfg)
    target = f'www/{lang}/patagonia-visa-requirements.html'
    with open(target, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'OK {target}')
