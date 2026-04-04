#!/usr/bin/env python3
"""
gen_cluster_multilang.py
Generates FR/ES/PT versions of:
  - {country}-visa-requirements.html (49 pages)
  - {country}-visa-processing-time.html (49 pages)
  - visa-free-countries-{passport}-passport.html (10 pages)
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW  = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE = "https://www.evisa-card.com"

# ── Country names in each language ─────────────────────────────────────────
CNAMES = {
    "fr": {
        "argentina":"Argentine","australia":"Australie","austria":"Autriche",
        "belgium":"Belgique","brazil":"Brésil","cambodia":"Cambodge",
        "canada":"Canada","china":"Chine","colombia":"Colombie",
        "costa-rica":"Costa Rica","croatia":"Croatie",
        "czech-republic":"République tchèque","denmark":"Danemark",
        "france":"France","germany":"Allemagne","greece":"Grèce",
        "hong-kong":"Hong Kong","hungary":"Hongrie","india":"Inde",
        "indonesia":"Indonésie","ireland":"Irlande","italy":"Italie",
        "japan":"Japon","jordan":"Jordanie","malaysia":"Malaisie",
        "maldives":"Maldives","mexico":"Mexique","nepal":"Népal",
        "netherlands":"Pays-Bas","new-zealand":"Nouvelle-Zélande",
        "norway":"Norvège","philippines":"Philippines","poland":"Pologne",
        "portugal":"Portugal","qatar":"Qatar","romania":"Roumanie",
        "singapore":"Singapour","spain":"Espagne","sri-lanka":"Sri Lanka",
        "sweden":"Suède","switzerland":"Suisse","taiwan":"Taïwan",
        "thailand":"Thaïlande","turkey":"Turquie",
        "uae":"Émirats Arabes Unis","united-kingdom":"Royaume-Uni",
        "usa":"États-Unis","vietnam":"Viêt Nam",
    },
    "es": {
        "argentina":"Argentina","australia":"Australia","austria":"Austria",
        "belgium":"Bélgica","brazil":"Brasil","cambodia":"Camboya",
        "canada":"Canadá","china":"China","colombia":"Colombia",
        "costa-rica":"Costa Rica","croatia":"Croacia",
        "czech-republic":"República Checa","denmark":"Dinamarca",
        "france":"Francia","germany":"Alemania","greece":"Grecia",
        "hong-kong":"Hong Kong","hungary":"Hungría","india":"India",
        "indonesia":"Indonesia","ireland":"Irlanda","italy":"Italia",
        "japan":"Japón","jordan":"Jordania","malaysia":"Malasia",
        "maldives":"Maldivas","mexico":"México","nepal":"Nepal",
        "netherlands":"Países Bajos","new-zealand":"Nueva Zelanda",
        "norway":"Noruega","philippines":"Filipinas","poland":"Polonia",
        "portugal":"Portugal","qatar":"Catar","romania":"Rumania",
        "singapore":"Singapur","spain":"España","sri-lanka":"Sri Lanka",
        "sweden":"Suecia","switzerland":"Suiza","taiwan":"Taiwán",
        "thailand":"Tailandia","turkey":"Turquía",
        "uae":"Emiratos Árabes Unidos","united-kingdom":"Reino Unido",
        "usa":"Estados Unidos","vietnam":"Vietnam",
    },
    "pt": {
        "argentina":"Argentina","australia":"Austrália","austria":"Áustria",
        "belgium":"Bélgica","brazil":"Brasil","cambodia":"Camboja",
        "canada":"Canadá","china":"China","colombia":"Colômbia",
        "costa-rica":"Costa Rica","croatia":"Croácia",
        "czech-republic":"República Tcheca","denmark":"Dinamarca",
        "france":"França","germany":"Alemanha","greece":"Grécia",
        "hong-kong":"Hong Kong","hungary":"Hungria","india":"Índia",
        "indonesia":"Indonésia","ireland":"Irlanda","italy":"Itália",
        "japan":"Japão","jordan":"Jordânia","malaysia":"Malásia",
        "maldives":"Maldivas","mexico":"México","nepal":"Nepal",
        "netherlands":"Países Baixos","new-zealand":"Nova Zelândia",
        "norway":"Noruega","philippines":"Filipinas","poland":"Polônia",
        "portugal":"Portugal","qatar":"Catar","romania":"Romênia",
        "singapore":"Singapura","spain":"Espanha","sri-lanka":"Sri Lanka",
        "sweden":"Suécia","switzerland":"Suíça","taiwan":"Taiwan",
        "thailand":"Tailândia","turkey":"Turquia",
        "uae":"Emirados Árabes Unidos","united-kingdom":"Reino Unido",
        "usa":"Estados Unidos","vietnam":"Vietnã",
    },
}

# Passport holder labels for visa-free pages
PASSPORT_LABELS = {
    "fr": {
        "us": "passeport américain", "uk": "passeport britannique",
        "canada": "passeport canadien", "france": "passeport français",
        "germany": "passeport allemand", "australia": "passeport australien",
        "brazil": "passeport brésilien", "japan": "passeport japonais",
        "china": "passeport chinois", "eu": "passeport européen",
    },
    "es": {
        "us": "pasaporte estadounidense", "uk": "pasaporte británico",
        "canada": "pasaporte canadiense", "france": "pasaporte francés",
        "germany": "pasaporte alemán", "australia": "pasaporte australiano",
        "brazil": "pasaporte brasileño", "japan": "pasaporte japonés",
        "china": "pasaporte chino", "eu": "pasaporte europeo",
    },
    "pt": {
        "us": "passaporte americano", "uk": "passaporte britânico",
        "canada": "passaporte canadense", "france": "passaporte francês",
        "germany": "passaporte alemão", "australia": "passaporte australiano",
        "brazil": "passaporte brasileiro", "japan": "passaporte japonês",
        "china": "passaporte chinês", "eu": "passaporte europeu",
    },
}

# ── Text substitutions applied to ALL pages ───────────────────────────────
def get_subs(lang):
    if lang == "fr":
        return [
            # html lang
            ('<html lang="en">', '<html lang="fr">'),
            # navbar
            ('">Home</a>', '">Accueil</a>'),
            ('">Destinations</a>', '">Destinations</a>'),
            ('">About</a>', '">À propos</a>'),
            ('">Guides</a>', '">Guides</a>'),
            ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-fr"></span> Français</a>'),
            # footer
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
             '© 2026 eVisa-Card.com — Plateforme mondiale d\'information eVisa &amp; Voyage'),
            ('Legal Notice', 'Mentions légales'),
            ('Disclaimer', 'Avertissement'),
            # section headings
            ('Documents Checklist', 'Liste des documents requis'),
            ('Eligibility Criteria', 'Critères d\'éligibilité'),
            ('How to Apply', 'Comment postuler'),
            ('Tips to Avoid Processing Delays', 'Conseils pour éviter les retards'),
            ('How to Track Your Application', 'Suivi de votre demande'),
            ('Related Guides', 'Guides connexes'),
            ('Main ', 'Guide principal '),
            ('How to Apply for an eVisa', 'Comment postuler pour un eVisa'),
            ('Visa Documents Checklist', 'Liste des documents visa'),
            ('Visa Processing Times', 'Délais de traitement visa'),
            ('Visa Photo Requirements', 'Exigences photo visa'),
            ('All Destinations', 'Toutes les destinations'),
            # table headers
            ('Visa-Free Entry', 'Entrée sans visa'),
            ('Passport Validity Required', 'Validité passeport requise'),
            ('Travel Insurance', 'Assurance voyage'),
            ('Onward Ticket Required', 'Billet de continuation requis'),
            ('Blank Pages Required', 'Pages vierges requises'),
            # common values
            ('Recommended but not mandatory', 'Recommandée mais non obligatoire'),
            ('At least 1 blank page', 'Au moins 1 page vierge'),
            # overview
            ('Overview of ', 'Aperçu des '),
            ('Entry Requirements', 'conditions d\'entrée'),
            ('Visa Requirements', 'conditions de visa'),
            ('Processing Times', 'délais de traitement'),
            ('Detailed Processing Timeline', 'Calendrier détaillé de traitement'),
            ('Top Visa-Free Destinations', 'Meilleures destinations sans visa'),
            ('Countries Requiring a Visa', 'Pays nécessitant un visa'),
            # alert editorial
            ('Editorial note:', 'Note éditoriale :'),
            ('Verified by our immigration team.', 'Vérifié par notre équipe immigration.'),
            ('Last updated: March 2026.', 'Dernière mise à jour : mars 2026.'),
            ('Sources: official embassy websites.', 'Sources : sites officiels des ambassades.'),
            # Requirements page headings
            ('Requirements 2026 — Documents, Eligibility &amp; Checklist',
             'Conditions 2026 — Documents, Éligibilité &amp; Liste de contrôle'),
            ('Requirements 2026', 'Conditions 2026'),
            ('Processing Time 2026 — How Long Does It Take?',
             'Délai de traitement 2026 — Combien de temps faut-il ?'),
            ('Visa Free Countries 2026', 'Pays sans visa 2026'),
            # key facts
            ('Key Facts', 'Informations clés'),
        ]
    elif lang == "es":
        return [
            ('<html lang="en">', '<html lang="es">'),
            ('">Home</a>', '">Inicio</a>'),
            ('">About</a>', '">Acerca de</a>'),
            ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-es"></span> Español</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
             '© 2026 eVisa-Card.com — Plataforma global de información eVisa y viajes'),
            ('Legal Notice', 'Aviso legal'),
            ('Disclaimer', 'Descargo'),
            ('Documents Checklist', 'Lista de documentos requeridos'),
            ('Eligibility Criteria', 'Criterios de elegibilidad'),
            ('How to Apply', 'Cómo solicitar'),
            ('Tips to Avoid Processing Delays', 'Consejos para evitar retrasos'),
            ('How to Track Your Application', 'Seguimiento de su solicitud'),
            ('Related Guides', 'Guías relacionadas'),
            ('How to Apply for an eVisa', 'Cómo solicitar un eVisa'),
            ('Visa Documents Checklist', 'Lista de documentos de visa'),
            ('Visa Processing Times', 'Tiempos de procesamiento de visa'),
            ('Visa Photo Requirements', 'Requisitos de foto de visa'),
            ('All Destinations', 'Todos los destinos'),
            ('Visa-Free Entry', 'Entrada sin visa'),
            ('Passport Validity Required', 'Validez de pasaporte requerida'),
            ('Travel Insurance', 'Seguro de viaje'),
            ('Onward Ticket Required', 'Boleto de conexión requerido'),
            ('Blank Pages Required', 'Páginas en blanco requeridas'),
            ('Recommended but not mandatory', 'Recomendado pero no obligatorio'),
            ('At least 1 blank page', 'Al menos 1 página en blanco'),
            ('Overview of ', 'Descripción general de '),
            ('Entry Requirements', 'requisitos de entrada'),
            ('Visa Requirements', 'requisitos de visa'),
            ('Processing Times', 'tiempos de procesamiento'),
            ('Detailed Processing Timeline', 'Cronograma detallado de procesamiento'),
            ('Top Visa-Free Destinations', 'Mejores destinos sin visa'),
            ('Countries Requiring a Visa', 'Países que requieren visa'),
            ('Editorial note:', 'Nota editorial:'),
            ('Verified by our immigration team.', 'Verificado por nuestro equipo de inmigración.'),
            ('Last updated: March 2026.', 'Última actualización: marzo de 2026.'),
            ('Sources: official embassy websites.', 'Fuentes: sitios web oficiales de embajadas.'),
            ('Requirements 2026 — Documents, Eligibility &amp; Checklist',
             'Requisitos 2026 — Documentos, Elegibilidad &amp; Lista de verificación'),
            ('Requirements 2026', 'Requisitos 2026'),
            ('Processing Time 2026 — How Long Does It Take?',
             'Tiempo de procesamiento 2026 — ¿Cuánto tarda?'),
            ('Visa Free Countries 2026', 'Países sin visa 2026'),
            ('Key Facts', 'Datos clave'),
        ]
    else:  # pt
        return [
            ('<html lang="en">', '<html lang="pt">'),
            ('">Home</a>', '">Início</a>'),
            ('">About</a>', '">Sobre</a>'),
            ('<span class="fi fi-gb"></span> English</a>', '<span class="fi fi-br"></span> Português</a>'),
            ('© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
             '© 2026 eVisa-Card.com — Plataforma global de informações eVisa e viagens'),
            ('Legal Notice', 'Aviso legal'),
            ('Disclaimer', 'Isenção'),
            ('Documents Checklist', 'Lista de documentos necessários'),
            ('Eligibility Criteria', 'Critérios de elegibilidade'),
            ('How to Apply', 'Como solicitar'),
            ('Tips to Avoid Processing Delays', 'Dicas para evitar atrasos'),
            ('How to Track Your Application', 'Acompanhamento da sua solicitação'),
            ('Related Guides', 'Guias relacionados'),
            ('How to Apply for an eVisa', 'Como solicitar um eVisa'),
            ('Visa Documents Checklist', 'Lista de documentos para visto'),
            ('Visa Processing Times', 'Prazos de processamento de visto'),
            ('Visa Photo Requirements', 'Requisitos de foto para visto'),
            ('All Destinations', 'Todos os destinos'),
            ('Visa-Free Entry', 'Entrada sem visto'),
            ('Passport Validity Required', 'Validade do passaporte necessária'),
            ('Travel Insurance', 'Seguro viagem'),
            ('Onward Ticket Required', 'Passagem de conexão necessária'),
            ('Blank Pages Required', 'Páginas em branco necessárias'),
            ('Recommended but not mandatory', 'Recomendado mas não obrigatório'),
            ('At least 1 blank page', 'Pelo menos 1 página em branco'),
            ('Overview of ', 'Visão geral das '),
            ('Entry Requirements', 'requisitos de entrada'),
            ('Visa Requirements', 'requisitos de visto'),
            ('Processing Times', 'prazos de processamento'),
            ('Detailed Processing Timeline', 'Cronograma detalhado de processamento'),
            ('Top Visa-Free Destinations', 'Melhores destinos sem visto'),
            ('Countries Requiring a Visa', 'Países que exigem visto'),
            ('Editorial note:', 'Nota editorial:'),
            ('Verified by our immigration team.', 'Verificado pela nossa equipe de imigração.'),
            ('Last updated: March 2026.', 'Última atualização: março de 2026.'),
            ('Sources: official embassy websites.', 'Fontes: sites oficiais de embaixadas.'),
            ('Requirements 2026 — Documents, Eligibility &amp; Checklist',
             'Requisitos 2026 — Documentos, Elegibilidade &amp; Lista de verificação'),
            ('Requirements 2026', 'Requisitos 2026'),
            ('Processing Time 2026 — How Long Does It Take?',
             'Prazo de processamento 2026 — Quanto tempo leva?'),
            ('Visa Free Countries 2026', 'Países sem visto 2026'),
            ('Key Facts', 'Informações principais'),
        ]


def fix_lang_urls(html, lang, fname):
    """Fix canonical, og:url, hreflang to use correct lang."""
    slug = fname.replace(".html", "")
    # canonical
    html = re.sub(
        r'<link href="https://www\.evisa-card\.com/en/([^"]+)" rel="canonical"',
        f'<link href="{BASE}/{lang}/{slug}" rel="canonical"',
        html
    )
    html = re.sub(
        r'<link rel="canonical" href="https://www\.evisa-card\.com/en/([^"]+)"',
        f'<link rel="canonical" href="{BASE}/{lang}/{slug}"',
        html
    )
    # og:url
    html = re.sub(
        r'content="https://www\.evisa-card\.com/en/[^"]+\.html" property="og:url"',
        f'content="{BASE}/{lang}/{slug}.html" property="og:url"',
        html
    )
    html = re.sub(
        r'property="og:url" content="https://www\.evisa-card\.com/en/[^"]+\.html"',
        f'property="og:url" content="{BASE}/{lang}/{slug}.html"',
        html
    )
    # legal footer links
    if lang == "fr":
        html = html.replace('/en/legal-notice.html', '/fr/mentions-legales.html')
        html = html.replace('/en/disclaimer.html', '/fr/disclaimer.html')
        html = html.replace('href="../destination.html"', 'href="/fr/destination.html"')
        html = html.replace('href="/en/expat-guides.html"', 'href="/fr/expat-guides.html"')
        # dropdown active state
        html = html.replace(
            '<a class="dropdown-item active" href="/en/',
            '<a class="dropdown-item" href="/en/'
        )
        html = html.replace(
            f'<a class="dropdown-item" href="/fr/{slug}.html">',
            f'<a class="dropdown-item active" href="/fr/{slug}.html">'
        )
    elif lang == "es":
        html = html.replace('/en/legal-notice.html', '/es/aviso-legal.html')
        html = html.replace('/en/disclaimer.html', '/es/disclaimer.html')
        html = html.replace('href="../destination.html"', 'href="/es/destination.html"')
        html = html.replace('href="/en/expat-guides.html"', 'href="/es/expat-guides.html"')
        html = html.replace(
            '<a class="dropdown-item active" href="/en/',
            '<a class="dropdown-item" href="/en/'
        )
        html = html.replace(
            f'<a class="dropdown-item" href="/es/{slug}.html">',
            f'<a class="dropdown-item active" href="/es/{slug}.html">'
        )
    else:  # pt
        html = html.replace('/en/legal-notice.html', '/pt/aviso-legal.html')
        html = html.replace('/en/disclaimer.html', '/pt/disclaimer.html')
        html = html.replace('href="../destination.html"', 'href="/pt/destination.html"')
        html = html.replace('href="/en/expat-guides.html"', 'href="/pt/expat-guides.html"')
        html = html.replace(
            '<a class="dropdown-item active" href="/en/',
            '<a class="dropdown-item" href="/en/'
        )
        html = html.replace(
            f'<a class="dropdown-item" href="/pt/{slug}.html">',
            f'<a class="dropdown-item active" href="/pt/{slug}.html">'
        )
    return html


def translate_country_name(html, lang, country_slug):
    """Replace country name in titles and headings."""
    country_en  = country_slug.replace("-", " ").title()
    country_loc = CNAMES[lang].get(country_slug, country_en)
    if country_loc != country_en:
        # Replace in title, h1, h2 only (avoid breaking JS/CSS)
        html = re.sub(
            rf'(<(?:title|h1|h2|h3)[^>]*>.*?){re.escape(country_en)}(.*?</(?:title|h1|h2|h3)>)',
            rf'\g<1>{country_loc}\g<2>',
            html, flags=re.S
        )
        # og:title, og:description
        html = re.sub(
            rf'(content="[^"]*){re.escape(country_en)}([^"]*")',
            rf'\g<1>{country_loc}\g<2>',
            html
        )
    return html


def process_file(en_path, lang, country_slug=None):
    fname = os.path.basename(en_path)
    out_path = os.path.join(WWW, lang, fname)
    if os.path.exists(out_path):
        return False  # skip existing

    with open(en_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Apply generic text substitutions
    for old, new in get_subs(lang):
        html = html.replace(old, new)

    # Fix URLs
    html = fix_lang_urls(html, lang, fname.replace(".html",""))

    # Translate country name in headings
    if country_slug:
        html = translate_country_name(html, lang, country_slug)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return True


# ── Process requirements pages ───────────────────────────────────────────────
req_pages = glob.glob(os.path.join(WWW, "en", "*-visa-requirements.html"))
proc_pages = glob.glob(os.path.join(WWW, "en", "*-visa-processing-time.html"))
vf_pages   = glob.glob(os.path.join(WWW, "en", "visa-free-countries-*-passport.html"))

created = 0
errors  = 0

for en_path in req_pages + proc_pages:
    fname = os.path.basename(en_path)
    # extract country slug
    m = re.match(r'^(.+)-visa-(?:requirements|processing-time)\.html$', fname)
    country_slug = m.group(1) if m else None
    for lang in ("fr","es","pt"):
        try:
            if process_file(en_path, lang, country_slug):
                created += 1
        except Exception as e:
            print(f"ERR {lang}/{fname}: {e}")
            errors += 1

for en_path in vf_pages:
    fname = os.path.basename(en_path)
    for lang in ("fr","es","pt"):
        try:
            if process_file(en_path, lang):
                created += 1
        except Exception as e:
            print(f"ERR {lang}/{fname}: {e}")
            errors += 1

print(f"Cluster pages created: {created} | Errors: {errors}")
print("DONE")
