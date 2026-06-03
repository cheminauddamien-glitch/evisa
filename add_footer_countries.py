# -*- coding: utf-8 -*-
"""Add a "Most Requested Visas" links block to the global footer of every page
(action-visas-style internal-linking footer for crawlability).

Localized heading per language; country links are language-relative
(/{lang}/visa-{slug}). Idempotent via id="footer-top-visas".
PROD ONLY (www, absolute paths).
"""
import glob, os

WWW = r'C:\Users\chemi\Documents\evisa\pacific-main\www'
ANCHOR = '<div class="row mb-5 justify-content-center">'

HEADING = {
 'en':'Most Requested Visas','fr':'Visas les plus demandés','es':'Visas más solicitados',
 'pt':'Vistos mais solicitados','zh':'最热门签证','th':'วีซ่าที่ขอมากที่สุด',
 'ru':'Самые востребованные визы','ar':'التأشيرات الأكثر طلبًا','ja':'人気のビザ','ko':'인기 비자',
}
# (slug, English label) — labels are proper nouns, kept across languages
TOP = [
 ('thailand','Thailand'),('vietnam','Vietnam'),('india','India'),('turkey','Turkey'),
 ('japan','Japan'),('china','China'),('indonesia','Indonesia'),('malaysia','Malaysia'),
 ('taiwan','Taiwan'),('uae','UAE'),('maldives','Maldives'),('sri-lanka','Sri Lanka'),
 ('colombia','Colombia'),('egypt','Egypt'),('jordan','Jordan'),('usa','USA'),
 ('canada','Canada'),('australia','Australia'),
]
SPECIAL = ('schengen-visa-guide-2026','Schengen Visa')


def block(lang):
    h = HEADING.get(lang, HEADING['en'])
    links = ''.join(
        f'<a href="/{lang}/visa-{slug}" style="color:#cfd8e3;text-decoration:none;font-size:13px;margin:0 8px 6px 0;display:inline-block;">{label}</a>'
        for slug, label in TOP)
    links += (f'<a href="/{lang}/{SPECIAL[0]}" style="color:#cfd8e3;text-decoration:none;'
              f'font-size:13px;margin:0 8px 6px 0;display:inline-block;">{SPECIAL[1]}</a>')
    return (f'<div class="row justify-content-center" id="footer-top-visas">'
            f'<div class="col-md-10 text-center" style="margin-bottom:28px;">'
            f'<h3 style="font-size:15px;color:#fff;margin-bottom:12px;letter-spacing:.5px;">{h}</h3>'
            f'<div style="line-height:1.9;">{links}</div></div></div>\n')


n = 0
for f in glob.glob(os.path.join(WWW, '*', '*.html')):
    lang = f.replace('\\', '/').split('/')[-2]
    if lang not in HEADING:
        continue
    h = open(f, encoding='utf-8', errors='replace').read()
    if 'footer-top-visas' in h or ANCHOR not in h:
        continue
    h = h.replace(ANCHOR, block(lang) + ANCHOR, 1)
    open(f, 'w', encoding='utf-8').write(h)
    n += 1

print('footers updated:', n)
