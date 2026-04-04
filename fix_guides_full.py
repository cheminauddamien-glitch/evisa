#!/usr/bin/env python3
"""
fix_guides_full.py
1. Fix Guides nav link on root pages (retirement-visa-guide -> expat-guides)
2. Translate body content of FR/ES/PT expat guide pages (headings, labels, footer)
3. Fix title, h1, meta for all non-EN guide pages
"""
import os, re, glob

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"

# ============================================================
# PART 1: Fix root pages Guides nav link
# ============================================================
def fix_root_pages():
    root_files = ["index.html", "destination.html", "about.html", "blog.html",
                  "contact.html", "blog-single.html", "404.html"]
    fixed = 0
    for fname in root_files:
        fp = os.path.join(BASE, fname)
        if not os.path.isfile(fp):
            continue
        with open(fp, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        orig = html
        html = html.replace(
            'href="/en/retirement-visa-guide.html">Guides',
            'href="/en/expat-guides.html">Guides'
        )
        if html != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html)
            fixed += 1
            print(f"  ROOT OK: {fname}")
    return fixed

# ============================================================
# PART 2: Translate FR/ES/PT guide body content
# ============================================================

# Translation maps for section headings, labels, UI text
TRANSLATIONS = {
    "fr": {
        # Title patterns
        ("Complete Expat Guide", "Guide Complet Expatriation"),
        ("Live, Work & Retire in", "Vivre, Travailler & S'installer en"),
        ("Live, Work & Retire in the", "Vivre, Travailler & S'installer aux"),
        # H1
        ("Expat Guide: Living in", "Guide Expatriation :"),
        # Section headings
        ("Visa & Residency Options", "Visa & Options de R\u00e9sidence"),
        ("Visa &amp; Residency Options", "Visa &amp; Options de R\u00e9sidence"),
        ("Healthcare System", "Syst\u00e8me de Sant\u00e9"),
        ("Health Insurance", "Assurance Sant\u00e9"),
        ("Supplementary Health Insurance", "Assurance Sant\u00e9 Compl\u00e9mentaire"),
        ("Opening a Bank Account", "Ouvrir un Compte Bancaire"),
        ("Buying Property", "Acheter un Bien Immobilier"),
        ("Tax & Fiscal Exile", "Fiscalit\u00e9 & Exil Fiscal"),
        # Sub-headings
        ("Available Visa Types", "Types de Visa Disponibles"),
        ("Step-by-Step Residency Process", "\u00c9tapes pour Obtenir la R\u00e9sidence"),
        ("Step-by-Step: How to Move to", "\u00c9tape par \u00c9tape : S'installer en"),
        ("Typical Healthcare Costs", "Co\u00fbts de Sant\u00e9 Typiques"),
        ("Top Providers for Expats", "Meilleurs Assureurs pour Expatri\u00e9s"),
        ("Recommended Banks", "Banques Recommand\u00e9es"),
        ("Required Documents", "Documents Requis"),
        ("Step-by-Step Process", "Processus \u00c9tape par \u00c9tape"),
        ("Ownership Options for Foreigners", "Options de Propri\u00e9t\u00e9 pour les \u00c9trangers"),
        ("Purchase Process", "Processus d'Achat"),
        ("Typical Purchase Costs", "Co\u00fbts d'Achat Typiques"),
        ("Related Expat Guides", "Guides Expatriation Associ\u00e9s"),
        ("Frequently Asked Questions", "Questions Fr\u00e9quentes"),
        # Table headers
        ("Visa Type", "Type de Visa"),
        ("Details", "D\u00e9tails"),
        ("Service", "Service"),
        ("Estimated Cost", "Co\u00fbt Estim\u00e9"),
        ("Item", "\u00c9l\u00e9ment"),
        ("Cost", "Co\u00fbt"),
        # Labels
        ("Table of Contents", "Sommaire"),
        ("Public Healthcare", "Sant\u00e9 Publique"),
        ("Private Healthcare", "Sant\u00e9 Priv\u00e9e"),
        ("at a Glance", "en Bref"),
        ("Capital", "Capitale"),
        ("Currency", "Monnaie"),
        ("Language", "Langue"),
        ("Monthly cost", "Co\u00fbt mensuel"),
        ("Cost of Living", "Co\u00fbt de la Vie"),
        ("Pro Tip:", "Conseil Pro :"),
        ("Recommended:", "Recommand\u00e9 :"),
        ("Last updated:", "Derni\u00e8re mise \u00e0 jour :"),
        ("Editorial Team", "\u00c9quipe \u00c9ditoriale"),
        # Footer
        ("Follow eVisa-Card.com", "Suivez eVisa-Card.com"),
        ("Legal Notice", "Mentions L\u00e9gales"),
        ("Disclaimer", "Avertissement"),
        ("All Expat Guides", "Tous les Guides"),
        ("Retirement Visa Guide", "Guide Visa Retraite"),
        ("Digital Nomad Visas", "Visas Nomades Num\u00e9riques"),
        ("Read the Guide", "Lire le Guide"),
        # Hero breadcrumbs
        (">Home <", ">Accueil <"),
        (">Expat Guides <", ">Guides Expatriation <"),
        # Author box
        ("Official Sources &amp; References", "Sources Officielles &amp; R\u00e9f\u00e9rences"),
        ("Expat guides written by travel experts", "Guides \u00e9crits par des experts en voyage"),
        ("immigration specialists and expats with first-hand experience in", "sp\u00e9cialistes en immigration et expatri\u00e9s avec une exp\u00e9rience directe en"),
        ("Verified information", "Informations v\u00e9rifi\u00e9es"),
        ("Updated March 2026", "Mis \u00e0 jour Mars 2026"),
        ("Official sources cited", "Sources officielles cit\u00e9es"),
    },
    "es": {
        ("Complete Expat Guide", "Gu\u00eda Completa Expatriaci\u00f3n"),
        ("Live, Work & Retire in", "Vivir, Trabajar & Jubilarse en"),
        ("Live, Work & Retire in the", "Vivir, Trabajar & Jubilarse en"),
        ("Expat Guide: Living in", "Gu\u00eda Expatriaci\u00f3n:"),
        ("Visa & Residency Options", "Visa & Opciones de Residencia"),
        ("Visa &amp; Residency Options", "Visa &amp; Opciones de Residencia"),
        ("Healthcare System", "Sistema de Salud"),
        ("Health Insurance", "Seguro de Salud"),
        ("Supplementary Health Insurance", "Seguro de Salud Complementario"),
        ("Opening a Bank Account", "Abrir una Cuenta Bancaria"),
        ("Buying Property", "Comprar Propiedad"),
        ("Tax & Fiscal Exile", "Fiscalidad & Exilio Fiscal"),
        ("Available Visa Types", "Tipos de Visa Disponibles"),
        ("Step-by-Step Residency Process", "Proceso de Residencia Paso a Paso"),
        ("Step-by-Step: How to Move to", "Paso a Paso: C\u00f3mo Mudarse a"),
        ("Typical Healthcare Costs", "Costos de Salud T\u00edpicos"),
        ("Top Providers for Expats", "Mejores Aseguradoras para Expatriados"),
        ("Recommended Banks", "Bancos Recomendados"),
        ("Required Documents", "Documentos Requeridos"),
        ("Step-by-Step Process", "Proceso Paso a Paso"),
        ("Ownership Options for Foreigners", "Opciones de Propiedad para Extranjeros"),
        ("Purchase Process", "Proceso de Compra"),
        ("Typical Purchase Costs", "Costos de Compra T\u00edpicos"),
        ("Related Expat Guides", "Gu\u00edas de Expatriaci\u00f3n Relacionadas"),
        ("Frequently Asked Questions", "Preguntas Frecuentes"),
        ("Visa Type", "Tipo de Visa"),
        ("Details", "Detalles"),
        ("Service", "Servicio"),
        ("Estimated Cost", "Costo Estimado"),
        ("Item", "Concepto"),
        ("Cost", "Costo"),
        ("Table of Contents", "\u00cdndice"),
        ("Public Healthcare", "Salud P\u00fablica"),
        ("Private Healthcare", "Salud Privada"),
        ("at a Glance", "de un Vistazo"),
        ("Capital", "Capital"),
        ("Currency", "Moneda"),
        ("Language", "Idioma"),
        ("Monthly cost", "Costo mensual"),
        ("Cost of Living", "Costo de Vida"),
        ("Pro Tip:", "Consejo Pro:"),
        ("Recommended:", "Recomendado:"),
        ("Last updated:", "\u00daltima actualizaci\u00f3n:"),
        ("Editorial Team", "Equipo Editorial"),
        ("Follow eVisa-Card.com", "Sigue eVisa-Card.com"),
        ("Legal Notice", "Aviso Legal"),
        ("Disclaimer", "Descargo de Responsabilidad"),
        ("All Expat Guides", "Todas las Gu\u00edas"),
        ("Retirement Visa Guide", "Gu\u00eda Visa Jubilaci\u00f3n"),
        ("Digital Nomad Visas", "Visas N\u00f3madas Digitales"),
        ("Read the Guide", "Leer la Gu\u00eda"),
        (">Home <", ">Inicio <"),
        (">Expat Guides <", ">Gu\u00edas Expatriaci\u00f3n <"),
        ("Official Sources &amp; References", "Fuentes Oficiales &amp; Referencias"),
        ("Expat guides written by travel experts", "Gu\u00edas escritas por expertos en viajes"),
        ("immigration specialists and expats with first-hand experience in", "especialistas en inmigraci\u00f3n y expatriados con experiencia directa en"),
        ("Verified information", "Informaci\u00f3n verificada"),
        ("Updated March 2026", "Actualizado Marzo 2026"),
        ("Official sources cited", "Fuentes oficiales citadas"),
    },
    "pt": {
        ("Complete Expat Guide", "Guia Completo Expatria\u00e7\u00e3o"),
        ("Live, Work & Retire in", "Viver, Trabalhar & Aposentar-se em"),
        ("Live, Work & Retire in the", "Viver, Trabalhar & Aposentar-se nos"),
        ("Expat Guide: Living in", "Guia Expatria\u00e7\u00e3o:"),
        ("Visa & Residency Options", "Visa & Op\u00e7\u00f5es de Resid\u00eancia"),
        ("Visa &amp; Residency Options", "Visa &amp; Op\u00e7\u00f5es de Resid\u00eancia"),
        ("Healthcare System", "Sistema de Sa\u00fade"),
        ("Health Insurance", "Seguro de Sa\u00fade"),
        ("Supplementary Health Insurance", "Seguro de Sa\u00fade Complementar"),
        ("Opening a Bank Account", "Abrir uma Conta Banc\u00e1ria"),
        ("Buying Property", "Comprar Im\u00f3vel"),
        ("Tax & Fiscal Exile", "Fiscalidade & Ex\u00edlio Fiscal"),
        ("Available Visa Types", "Tipos de Visto Dispon\u00edveis"),
        ("Step-by-Step Residency Process", "Processo de Resid\u00eancia Passo a Passo"),
        ("Step-by-Step: How to Move to", "Passo a Passo: Como Mudar-se para"),
        ("Typical Healthcare Costs", "Custos de Sa\u00fade T\u00edpicos"),
        ("Top Providers for Expats", "Melhores Seguradoras para Expatriados"),
        ("Recommended Banks", "Bancos Recomendados"),
        ("Required Documents", "Documentos Necess\u00e1rios"),
        ("Step-by-Step Process", "Processo Passo a Passo"),
        ("Ownership Options for Foreigners", "Op\u00e7\u00f5es de Propriedade para Estrangeiros"),
        ("Purchase Process", "Processo de Compra"),
        ("Typical Purchase Costs", "Custos de Compra T\u00edpicos"),
        ("Related Expat Guides", "Guias de Expatria\u00e7\u00e3o Relacionados"),
        ("Frequently Asked Questions", "Perguntas Frequentes"),
        ("Visa Type", "Tipo de Visto"),
        ("Details", "Detalhes"),
        ("Service", "Servi\u00e7o"),
        ("Estimated Cost", "Custo Estimado"),
        ("Item", "Item"),
        ("Cost", "Custo"),
        ("Table of Contents", "\u00cdndice"),
        ("Public Healthcare", "Sa\u00fade P\u00fablica"),
        ("Private Healthcare", "Sa\u00fade Privada"),
        ("at a Glance", "em Resumo"),
        ("Capital", "Capital"),
        ("Currency", "Moeda"),
        ("Language", "L\u00edngua"),
        ("Monthly cost", "Custo mensal"),
        ("Cost of Living", "Custo de Vida"),
        ("Pro Tip:", "Dica Pro:"),
        ("Recommended:", "Recomendado:"),
        ("Last updated:", "\u00daltima atualiza\u00e7\u00e3o:"),
        ("Editorial Team", "Equipe Editorial"),
        ("Follow eVisa-Card.com", "Siga eVisa-Card.com"),
        ("Legal Notice", "Aviso Legal"),
        ("Disclaimer", "Aviso de Responsabilidade"),
        ("All Expat Guides", "Todos os Guias"),
        ("Retirement Visa Guide", "Guia Visto Aposentadoria"),
        ("Digital Nomad Visas", "Vistos N\u00f4mades Digitais"),
        ("Read the Guide", "Ler o Guia"),
        (">Home <", ">In\u00edcio <"),
        (">Expat Guides <", ">Guias Expatria\u00e7\u00e3o <"),
        ("Official Sources &amp; References", "Fontes Oficiais &amp; Refer\u00eancias"),
        ("Expat guides written by travel experts", "Guias escritos por especialistas em viagens"),
        ("immigration specialists and expats with first-hand experience in", "especialistas em imigra\u00e7\u00e3o e expatriados com experi\u00eancia direta em"),
        ("Verified information", "Informa\u00e7\u00e3o verificada"),
        ("Updated March 2026", "Atualizado Mar\u00e7o 2026"),
        ("Official sources cited", "Fontes oficiais citadas"),
    },
}

# Country names in each language for title/h1 translations
COUNTRY_NAMES = {
    "fr": {
        "Thailand": "Tha\u00eflande", "Portugal": "Portugal", "Spain": "Espagne",
        "Mexico": "Mexique", "Vietnam": "Vietnam", "Malaysia": "Malaisie",
        "Japan": "Japon", "UAE": "\u00c9mirats Arabes Unis", "Colombia": "Colombie",
        "Panama": "Panama", "Costa Rica": "Costa Rica", "Greece": "Gr\u00e8ce",
        "Georgia": "G\u00e9orgie", "Paraguay": "Paraguay", "Laos": "Laos",
        "Cambodia": "Cambodge",
    },
    "es": {
        "Thailand": "Tailandia", "Portugal": "Portugal", "Spain": "Espa\u00f1a",
        "Mexico": "M\u00e9xico", "Vietnam": "Vietnam", "Malaysia": "Malasia",
        "Japan": "Jap\u00f3n", "UAE": "EAU", "Colombia": "Colombia",
        "Panama": "Panam\u00e1", "Costa Rica": "Costa Rica", "Greece": "Grecia",
        "Georgia": "Georgia", "Paraguay": "Paraguay", "Laos": "Laos",
        "Cambodia": "Camboya",
    },
    "pt": {
        "Thailand": "Tail\u00e2ndia", "Portugal": "Portugal", "Spain": "Espanha",
        "Mexico": "M\u00e9xico", "Vietnam": "Vietn\u00e3", "Malaysia": "Mal\u00e1sia",
        "Japan": "Jap\u00e3o", "UAE": "EAU", "Colombia": "Col\u00f4mbia",
        "Panama": "Panam\u00e1", "Costa Rica": "Costa Rica", "Greece": "Gr\u00e9cia",
        "Georgia": "Ge\u00f3rgia", "Paraguay": "Paraguai", "Laos": "Laos",
        "Cambodia": "Camboja",
    },
}

COUNTRIES = [
    "thailand", "portugal", "spain", "mexico", "vietnam", "malaysia",
    "japan", "uae", "colombia", "panama", "costa-rica", "greece",
    "georgia", "paraguay", "laos", "cambodia"
]

COUNTRY_DISPLAY = {
    "thailand": "Thailand", "portugal": "Portugal", "spain": "Spain",
    "mexico": "Mexico", "vietnam": "Vietnam", "malaysia": "Malaysia",
    "japan": "Japan", "uae": "UAE", "colombia": "Colombia",
    "panama": "Panama", "costa-rica": "Costa Rica", "greece": "Greece",
    "georgia": "Georgia", "paraguay": "Paraguay", "laos": "Laos",
    "cambodia": "Cambodia",
}


def translate_guide_page(filepath, lang, country_slug):
    """Apply translations to a guide page."""
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        html = f.read()

    orig = html
    translations = TRANSLATIONS.get(lang)
    if not translations:
        return False

    country_en = COUNTRY_DISPLAY[country_slug]
    country_local = COUNTRY_NAMES.get(lang, {}).get(country_en, country_en)

    # Apply all text substitutions
    for en_text, local_text in translations:
        html = html.replace(en_text, local_text)

    # Translate country name in title, h1, meta
    if lang in COUNTRY_NAMES and country_en in COUNTRY_NAMES[lang]:
        # Only replace in specific patterns to avoid breaking content
        # Title
        html = re.sub(
            rf'(<title>[^<]*){country_en}([^<]*</title>)',
            rf'\g<1>{country_local}\g<2>',
            html
        )
        # H1
        html = re.sub(
            rf'(<h1[^>]*>[^<]*){country_en}([^<]*</h1>)',
            rf'\g<1>{country_local}\g<2>',
            html
        )
        # Meta description
        html = re.sub(
            rf'(content="[^"]*){country_en}([^"]*"[^>]*/>)',
            lambda m: m.group(0).replace(country_en, country_local, 1),
            html, count=1
        )
        # "at a Glance" / "en Bref" heading with country
        for en_g, loc_g in [("at a Glance", COUNTRY_NAMES.get(lang, {}).get("at a Glance", "at a Glance"))]:
            pass  # Already handled by the general translations

    # Healthcare emoji headings
    html = html.replace(
        f"Healthcare in {country_en}",
        {"fr": f"Sant\u00e9 en {country_local}",
         "es": f"Salud en {country_local}",
         "pt": f"Sa\u00fade em {country_local}"}.get(lang, f"Healthcare in {country_en}")
    )

    # Bank account heading with country
    html = html.replace(
        f"Opening a Bank Account in {country_en}",
        {"fr": f"Ouvrir un Compte Bancaire en {country_local}",
         "es": f"Abrir una Cuenta Bancaria en {country_local}",
         "pt": f"Abrir uma Conta Banc\u00e1ria em {country_local}"}.get(lang, f"Opening a Bank Account in {country_en}")
    )

    # Property heading with country
    html = html.replace(
        f"Buying Property in {country_en}",
        {"fr": f"Acheter un Bien Immobilier en {country_local}",
         "es": f"Comprar Propiedad en {country_local}",
         "pt": f"Comprar Im\u00f3vel em {country_local}"}.get(lang, f"Buying Property in {country_en}")
    )

    if html != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


def main():
    print("=" * 60)
    print("PART 1: Fix root pages Guides nav link")
    print("=" * 60)
    root_fixed = fix_root_pages()
    print(f"  Fixed {root_fixed} root pages\n")

    print("=" * 60)
    print("PART 2: Translate FR/ES/PT guide page content")
    print("=" * 60)
    translated = 0
    for lang in ["fr", "es", "pt"]:
        lang_dir = os.path.join(BASE, lang)
        if not os.path.isdir(lang_dir):
            continue
        for slug in COUNTRIES:
            fp = os.path.join(lang_dir, f"expat-guide-{slug}.html")
            if not os.path.isfile(fp):
                continue
            if translate_guide_page(fp, lang, slug):
                translated += 1
                print(f"  OK {lang}/expat-guide-{slug}.html")

    print(f"\n  Translated {translated} guide pages\n")

    # Also translate expat-guides.html index pages
    print("=" * 60)
    print("PART 3: Translate expat-guides.html index pages")
    print("=" * 60)
    idx_fixed = 0
    for lang in ["fr", "es", "pt"]:
        fp = os.path.join(BASE, lang, "expat-guides.html")
        if not os.path.isfile(fp):
            continue
        with open(fp, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        orig = html
        translations = TRANSLATIONS.get(lang, set())
        for en_text, local_text in translations:
            html = html.replace(en_text, local_text)
        if html != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(html)
            idx_fixed += 1
            print(f"  OK {lang}/expat-guides.html")

    print(f"\n  Fixed {idx_fixed} index pages")
    print(f"\nTOTAL: {root_fixed} root + {translated} guide + {idx_fixed} index pages fixed")


if __name__ == "__main__":
    main()
