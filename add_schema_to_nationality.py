"""Add schema.org FAQPage JSON-LD to nationality pages without any structured data.
Uses the title and a generic FAQ template based on the page topic.
"""
import os, re, glob, json

LANGS = ['en','fr','es','pt','zh','th','ru','ar','ja','ko']
TOTAL = ADDED = SKIPPED = ERRORS = 0


def has_jsonld(html):
    return bool(re.search(r'<script[^>]*type=["\']application/ld\+json["\']', html, re.I))


def extract_country_nat(filename):
    """visa pattern: {country}-visa-for-{nat}-citizens.html"""
    bn = os.path.basename(filename).replace('.html','')
    m = re.match(r'^([a-z-]+)-visa-for-([a-z-]+)-citizens$', bn)
    if not m: return None, None
    country = m.group(1).replace('-', ' ').title()
    nat = m.group(2).replace('-', ' ').title()
    return country, nat


# Lang-specific Q/A templates
TEMPLATES = {
    'en': {
        'q1': 'Do {nat} citizens need a visa for {country}?',
        'a1': 'Visa requirements for {nat} citizens visiting {country} depend on the bilateral agreement and length of stay. Check the official immigration portal of {country} for the latest rules.',
        'q2': 'How long can {nat} citizens stay in {country}?',
        'a2': 'Maximum stay varies by visa type and nationality. Tourist stays are commonly 30 to 90 days. Always confirm the allowed duration before booking flights.',
        'q3': 'What documents are needed for {nat} travelers entering {country}?',
        'a3': 'Standard documents include a valid passport (6+ months validity), return ticket, proof of accommodation, sufficient funds, and a completed arrival card. Some nationalities also need a visa or eVisa approval.',
    },
    'fr': {
        'q1': 'Les citoyens {nat} ont-ils besoin d\'un visa pour {country} ?',
        'a1': 'Les conditions de visa pour les citoyens {nat} se rendant en {country} dépendent de l\'accord bilatéral et de la durée du séjour. Consultez le portail officiel d\'immigration de {country} pour les règles à jour.',
        'q2': 'Combien de temps les citoyens {nat} peuvent-ils séjourner en {country} ?',
        'a2': 'La durée maximale varie selon le type de visa et la nationalité. Les séjours touristiques sont généralement de 30 à 90 jours. Vérifiez toujours la durée autorisée avant de réserver vos vols.',
        'q3': 'Quels documents sont nécessaires pour les voyageurs {nat} entrant en {country} ?',
        'a3': 'Les documents standards comprennent : passeport valide (6+ mois), billet retour, preuve d\'hébergement, fonds suffisants et carte d\'arrivée. Certaines nationalités ont aussi besoin d\'un visa ou e-Visa.',
    },
    'es': {
        'q1': '¿Los ciudadanos {nat} necesitan visa para {country}?',
        'a1': 'Los requisitos de visa para ciudadanos {nat} que visitan {country} dependen del acuerdo bilateral y la duración de la estancia. Consulte el portal oficial de inmigración de {country} para reglas actualizadas.',
        'q2': '¿Cuánto tiempo pueden quedarse los ciudadanos {nat} en {country}?',
        'a2': 'La estancia máxima varía según el tipo de visa y la nacionalidad. Las estancias turísticas suelen ser de 30 a 90 días. Confirme siempre la duración permitida antes de reservar vuelos.',
        'q3': '¿Qué documentos necesitan los viajeros {nat} para entrar a {country}?',
        'a3': 'Los documentos estándar incluyen pasaporte válido (6+ meses), boleto de regreso, prueba de alojamiento, fondos suficientes y tarjeta de llegada. Algunas nacionalidades también necesitan visa o eVisa.',
    },
    'pt': {
        'q1': 'Os cidadãos {nat} precisam de visto para {country}?',
        'a1': 'Os requisitos de visto para cidadãos {nat} visitando {country} dependem do acordo bilateral e da duração da estadia. Consulte o portal oficial de imigração de {country} para regras atualizadas.',
        'q2': 'Quanto tempo os cidadãos {nat} podem permanecer em {country}?',
        'a2': 'A estadia máxima varia conforme o tipo de visto e a nacionalidade. As estadias turísticas geralmente são de 30 a 90 dias. Sempre confirme a duração permitida antes de reservar voos.',
        'q3': 'Quais documentos são necessários para viajantes {nat} entrarem em {country}?',
        'a3': 'Os documentos padrão incluem passaporte válido (6+ meses), passagem de volta, prova de hospedagem, fundos suficientes e cartão de chegada. Algumas nacionalidades também precisam de visto ou eVisa.',
    },
}
# For non-Latin langs use English templates (matches existing site pattern)
for k in ('zh','th','ru','ar','ja','ko'):
    TEMPLATES[k] = TEMPLATES['en']


def build_jsonld(country, nat, lang):
    t = TEMPLATES.get(lang, TEMPLATES['en'])
    qa = []
    for i in (1, 2, 3):
        q = t[f'q{i}'].format(nat=nat, country=country)
        a = t[f'a{i}'].format(nat=nat, country=country)
        qa.append({'@type': 'Question', 'name': q,
                   'acceptedAnswer': {'@type': 'Answer', 'text': a}})
    payload = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': qa}
    return ('    <script type="application/ld+json">\n    '
            + json.dumps(payload, ensure_ascii=False)
            + '\n    </script>\n')


def process_file(path, lang):
    global TOTAL, ADDED, SKIPPED, ERRORS
    TOTAL += 1
    try:
        with open(path, encoding='utf-8') as f:
            html = f.read()
    except Exception:
        ERRORS += 1
        return
    if has_jsonld(html):
        SKIPPED += 1
        return
    country, nat = extract_country_nat(path)
    if not country:
        ERRORS += 1
        return
    snippet = build_jsonld(country, nat, lang)

    # Insert right after the canonical line, before any other content
    new = re.sub(
        r'(<link[^>]*rel=["\']canonical["\'][^>]*/>\s*\n)',
        r'\1' + snippet,
        html, count=1
    )
    if new == html:
        new = re.sub(
            r'(<link[^>]*href=["\'][^"\']+["\'][^>]*rel=["\']canonical["\'][^>]*/>\s*\n)',
            r'\1' + snippet,
            html, count=1
        )
    if new == html:
        # Insert before </head>
        new = html.replace('</head>', snippet + '</head>', 1)
    if new == html:
        ERRORS += 1
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    ADDED += 1


def main():
    for lang in LANGS:
        files = glob.glob(f'www/{lang}/*-visa-for-*-citizens.html')
        before = ADDED
        for f in files:
            process_file(f, lang)
        added_lang = ADDED - before
        print(f'  {lang}: {len(files)} files | added: {added_lang} | total ADDED: {ADDED}')
    print(f'\nFINAL: total={TOTAL}, added={ADDED}, skipped={SKIPPED}, errors={ERRORS}')


if __name__ == '__main__':
    main()
