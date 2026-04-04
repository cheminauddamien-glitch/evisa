#!/usr/bin/env python3
"""
1. Force navbar background navy blue on ALL pages (all languages)
2. Fix untranslated text in fr/es/pt/destination.html
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"
NAVY = '#0d2461'

# ── 1. Fix navbar background on ALL pages ────────────────────────────────────
# The ftco_navbar CSS class makes the navbar transparent by default.
# We inject an inline style to force the solid navy color.

NAV_PATTERN = re.compile(
    r'<nav\s+class="navbar[^"]*ftco_navbar[^"]*"([^>]*)>',
    re.DOTALL
)

def fix_navbar(html):
    def replacer(m):
        attrs = m.group(1)
        # Remove any existing background style to avoid duplication
        attrs = re.sub(r'\s*style="[^"]*background[^"]*"', '', attrs)
        return f'<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:{NAVY} !important;position:relative;z-index:10;">'
    return NAV_PATTERN.sub(replacer, html)

nav_fixed = nav_errors = 0

all_html = (
    glob.glob(os.path.join(WWW, "*.html")) +
    glob.glob(os.path.join(WWW, "en", "*.html")) +
    glob.glob(os.path.join(WWW, "fr", "*.html")) +
    glob.glob(os.path.join(WWW, "es", "*.html")) +
    glob.glob(os.path.join(WWW, "pt", "*.html"))
)

for fpath in all_html:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        new_html = fix_navbar(html)
        if new_html != html:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_html)
            nav_fixed += 1
    except Exception as e:
        print(f"ERR {fpath}: {e}")
        nav_errors += 1

print(f"Navbar fixed: {nav_fixed} pages | Errors: {nav_errors}")


# ── 2. Translate remaining English in fr/es/pt destination.html ──────────────

DEST_TRANSLATIONS = {
    "fr": {
        # Section descriptions
        "Find eVisa types, average durations, fees, official links and application tips for popular Asian destinations. Each country page includes requirements and quick steps to apply.":
            "Trouvez les types d'eVisa, durées moyennes, frais, liens officiels et conseils de demande pour les destinations asiatiques populaires. Chaque page pays inclut les conditions et les étapes rapides de demande.",
        "Overview of Schengen visas, national visitor visas and eVisa options for major European tourist countries. Find durations, fees, official links and quick application tips.":
            "Aperçu des visas Schengen, visas nationaux de touriste et options eVisa pour les principaux pays touristiques européens. Durées, frais, liens officiels et conseils de demande rapide.",
        "Discover visa requirements and eVisa options for popular destinations in North and South America. Includes fees, durations and official application links.":
            "Découvrez les conditions de visa et options eVisa pour les destinations populaires d'Amérique du Nord et du Sud. Frais, durées et liens officiels de demande inclus.",
        "Explore visa requirements for African destinations. Find eVisa options, visa on arrival information and entry requirements for major African countries.":
            "Explorez les conditions de visa pour les destinations africaines. Options eVisa, visa à l'arrivée et conditions d'entrée pour les principaux pays africains.",
        "Visa information for Middle Eastern destinations including eVisa options, visa on arrival and entry requirements for the region's top travel destinations.":
            "Informations sur les visas pour les destinations du Moyen-Orient, incluant les options eVisa, visa à l'arrivée et conditions d'entrée pour les meilleures destinations de la région.",
        # og:description
        "Find eVisa types, fees, requirements and official application links for 40+ countries in Asia and Europe.":
            "Trouvez les types d'eVisa, frais, conditions et liens officiels de demande pour 40+ pays en Asie et en Europe.",
        # Country names (h3)
        ">United Arab Emirates<": ">Émirats Arabes Unis<",
        ">United Kingdom<": ">Royaume-Uni<",
        ">Turkey<": ">Turquie<",
        ">Thailand<": ">Thaïlande<",
        ">Japan<": ">Japon<",
        ">China<": ">Chine<",
        ">South Korea<": ">Corée du Sud<",
        ">Malaysia<": ">Malaisie<",
        ">Philippines<": ">Philippines<",
        ">Cambodia<": ">Cambodge<",
        ">Sri Lanka<": ">Sri Lanka<",
        ">Nepal<": ">Népal<",
        ">Indonesia<": ">Indonésie<",
        ">Singapore<": ">Singapour<",
        ">Vietnam<": ">Viêt Nam<",
        ">Germany<": ">Allemagne<",
        ">Netherlands<": ">Pays-Bas<",
        ">Belgium<": ">Belgique<",
        ">Greece<": ">Grèce<",
        ">Switzerland<": ">Suisse<",
        ">Austria<": ">Autriche<",
        ">Sweden<": ">Suède<",
        ">Norway<": ">Norvège<",
        ">Denmark<": ">Danemark<",
        ">Ireland<": ">Irlande<",
        ">Mexico<": ">Mexique<",
        ">Brazil<": ">Brésil<",
        ">Argentina<": ">Argentine<",
        ">Peru<": ">Pérou<",
        ">Colombia<": ">Colombie<",
        ">Kenya<": ">Kenya<",
        ">Tanzania<": ">Tanzanie<",
        ">Egypt<": ">Égypte<",
        ">Morocco<": ">Maroc<",
        ">Ethiopia<": ">Éthiopie<",
        ">Qatar<": ">Qatar<",
        ">Bahrain<": ">Bahreïn<",
        ">Jordan<": ">Jordanie<",
        ">Oman<": ">Oman<",
        ">Saudi Arabia<": ">Arabie Saoudite<",
        ">New Zealand<": ">Nouvelle-Zélande<",
        ">Maldives<": ">Maldives<",
    },
    "es": {
        "Find eVisa types, average durations, fees, official links and application tips for popular Asian destinations. Each country page includes requirements and quick steps to apply.":
            "Encuentra los tipos de eVisa, duraciones promedio, tarifas, enlaces oficiales y consejos de solicitud para destinos asiáticos populares. Cada página de país incluye requisitos y pasos rápidos para aplicar.",
        "Overview of Schengen visas, national visitor visas and eVisa options for major European tourist countries. Find durations, fees, official links and quick application tips.":
            "Resumen de visas Schengen, visas de turista nacionales y opciones de eVisa para los principales países turísticos europeos. Duración, tarifas, enlaces oficiales y consejos rápidos de solicitud.",
        "Discover visa requirements and eVisa options for popular destinations in North and South America. Includes fees, durations and official application links.":
            "Descubre los requisitos de visa y opciones de eVisa para destinos populares en América del Norte y del Sur. Incluye tarifas, duraciones y enlaces oficiales de solicitud.",
        "Explore visa requirements for African destinations. Find eVisa options, visa on arrival information and entry requirements for major African countries.":
            "Explora los requisitos de visa para destinos africanos. Opciones de eVisa, visa a la llegada y requisitos de entrada para los principales países africanos.",
        "Visa information for Middle Eastern destinations including eVisa options, visa on arrival and entry requirements for the region's top travel destinations.":
            "Información de visa para destinos de Oriente Medio, incluidas opciones de eVisa, visa a la llegada y requisitos de entrada para los mejores destinos de viaje de la región.",
        "Find eVisa types, fees, requirements and official application links for 40+ countries in Asia and Europe.":
            "Encuentra tipos de eVisa, tarifas, requisitos y enlaces oficiales de solicitud para más de 40 países en Asia y Europa.",
        ">United Arab Emirates<": ">Emiratos Árabes Unidos<",
        ">United Kingdom<": ">Reino Unido<",
        ">Turkey<": ">Turquía<",
        ">Thailand<": ">Tailandia<",
        ">Japan<": ">Japón<",
        ">China<": ">China<",
        ">South Korea<": ">Corea del Sur<",
        ">Malaysia<": ">Malasia<",
        ">Cambodia<": ">Camboya<",
        ">Sri Lanka<": ">Sri Lanka<",
        ">Nepal<": ">Nepal<",
        ">Germany<": ">Alemania<",
        ">Netherlands<": ">Países Bajos<",
        ">Belgium<": ">Bélgica<",
        ">Greece<": ">Grecia<",
        ">Switzerland<": ">Suiza<",
        ">Austria<": ">Austria<",
        ">Sweden<": ">Suecia<",
        ">Norway<": ">Noruega<",
        ">Denmark<": ">Dinamarca<",
        ">Ireland<": ">Irlanda<",
        ">Mexico<": ">México<",
        ">Brazil<": ">Brasil<",
        ">Argentina<": ">Argentina<",
        ">Peru<": ">Perú<",
        ">Egypt<": ">Egipto<",
        ">Morocco<": ">Marruecos<",
        ">Ethiopia<": ">Etiopía<",
        ">Saudi Arabia<": ">Arabia Saudita<",
        ">New Zealand<": ">Nueva Zelanda<",
        ">Jordan<": ">Jordania<",
    },
    "pt": {
        "Find eVisa types, average durations, fees, official links and application tips for popular Asian destinations. Each country page includes requirements and quick steps to apply.":
            "Encontre os tipos de eVisa, durações médias, taxas, links oficiais e dicas de solicitação para destinos asiáticos populares. Cada página de país inclui requisitos e passos rápidos para aplicar.",
        "Overview of Schengen visas, national visitor visas and eVisa options for major European tourist countries. Find durations, fees, official links and quick application tips.":
            "Visão geral dos vistos Schengen, vistos de turista nacionais e opções de eVisa para os principais países turísticos europeus. Durações, taxas, links oficiais e dicas rápidas de solicitação.",
        "Discover visa requirements and eVisa options for popular destinations in North and South America. Includes fees, durations and official application links.":
            "Descubra os requisitos de visto e opções de eVisa para destinos populares na América do Norte e do Sul. Inclui taxas, durações e links oficiais de solicitação.",
        "Explore visa requirements for African destinations. Find eVisa options, visa on arrival information and entry requirements for major African countries.":
            "Explore os requisitos de visto para destinos africanos. Opções de eVisa, visto na chegada e requisitos de entrada para os principais países africanos.",
        "Visa information for Middle Eastern destinations including eVisa options, visa on arrival and entry requirements for the region's top travel destinations.":
            "Informações de visto para destinos do Oriente Médio, incluindo opções de eVisa, visto na chegada e requisitos de entrada para os melhores destinos de viagem da região.",
        "Find eVisa types, fees, requirements and official application links for 40+ countries in Asia and Europe.":
            "Encontre tipos de eVisa, taxas, requisitos e links oficiais de solicitação para mais de 40 países na Ásia e Europa.",
        ">United Arab Emirates<": ">Emirados Árabes Unidos<",
        ">United Kingdom<": ">Reino Unido<",
        ">Turkey<": ">Turquia<",
        ">Thailand<": ">Tailândia<",
        ">Japan<": ">Japão<",
        ">China<": ">China<",
        ">South Korea<": ">Coreia do Sul<",
        ">Malaysia<": ">Malásia<",
        ">Cambodia<": ">Camboja<",
        ">Sri Lanka<": ">Sri Lanka<",
        ">Nepal<": ">Nepal<",
        ">Germany<": ">Alemanha<",
        ">Netherlands<": ">Países Baixos<",
        ">Belgium<": ">Bélgica<",
        ">Greece<": ">Grécia<",
        ">Switzerland<": ">Suíça<",
        ">Austria<": ">Áustria<",
        ">Sweden<": ">Suécia<",
        ">Norway<": ">Noruega<",
        ">Denmark<": ">Dinamarca<",
        ">Ireland<": ">Irlanda<",
        ">Mexico<": ">México<",
        ">Brazil<": ">Brasil<",
        ">Argentina<": ">Argentina<",
        ">Peru<": ">Peru<",
        ">Egypt<": ">Egito<",
        ">Morocco<": ">Marrocos<",
        ">Ethiopia<": ">Etiópia<",
        ">Saudi Arabia<": ">Arábia Saudita<",
        ">New Zealand<": ">Nova Zelândia<",
        ">Jordan<": ">Jordânia<",
        ">Vietnam<": ">Vietnã<",
        ">Indonesia<": ">Indonésia<",
        ">Colombia<": ">Colômbia<",
    },
}

dest_fixed = 0
for lang, translations in DEST_TRANSLATIONS.items():
    fpath = os.path.join(WWW, lang, "destination.html")
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        for en_text, translated in translations.items():
            html = html.replace(en_text, translated)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        dest_fixed += 1
        print(f"destination.html translated: {lang}")
    except Exception as e:
        print(f"ERR {lang}/destination.html: {e}")

print(f"\nDestination pages translated: {dest_fixed}")
print("DONE")
