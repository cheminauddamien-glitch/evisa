#!/usr/bin/env python3
"""
Translate English content in all 16 Spanish expat guide pages to Spanish.
Uses string replace() for each translation pair.
"""

import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "es")

COUNTRIES = [
    "thailand", "portugal", "spain", "mexico", "vietnam", "malaysia",
    "japan", "uae", "colombia", "panama", "costa-rica", "greece",
    "georgia", "paraguay", "laos", "cambodia"
]

# Country name translations for "in {Country}" patterns
COUNTRY_IN_TRANSLATIONS = {
    "in Thailand": "en Tailandia",
    "in Portugal": "en Portugal",
    "in Spain": "en España",
    "in Mexico": "en México",
    "in Vietnam": "en Vietnam",
    "in Malaysia": "en Malasia",
    "in Japan": "en Japón",
    "in UAE": "en EAU",
    "in Colombia": "en Colombia",
    "in Panama": "en Panamá",
    "in Costa Rica": "en Costa Rica",
    "in Costoa Rica": "en Costa Rica",
    "in Greece": "en Grecia",
    "in Georgia": "en Georgia",
    "in Paraguay": "en Paraguay",
    "in Laos": "en Laos",
    "in Cambodia": "en Camboya",
}

# All translation pairs (English -> Spanish)
TRANSLATIONS = [
    # --- H2/H3 titles ---
    ("Supplementary", "Complementario"),

    # --- Table headers ---
    ("Visa Type", "Tipo de Visa"),
    ("Details", "Detalles"),
    ("Estimated Cout", "Costo Estimado"),
    ("Estimated Cost", "Costo Estimado"),
    ("Costoo Estimado", "Costo Estimado"),
    (">Item<", ">Elemento<"),
    (">Cost<", ">Costo<"),
    (">Service<", ">Servicio<"),

    # --- Visa section ---
    ("Available Visa Types", "Tipos de Visa Disponibles"),
    ("Available Type de Visas", "Tipos de Visa Disponibles"),
    ("Step-by-Step Residency Process", "Proceso de Residencia Paso a Paso"),
    ("For expats 50+", "Para expatriados de 50 años o más"),
    ("For remote workers earning", "Para trabajadores remotos que ganan"),
    ("Membership programme", "Programa de membresía"),
    ("Required if working for", "Requerido si trabaja para"),
    ("Determine your visa category", "Determine su categoría de visa"),
    ("Gather documents:", "Reúna los documentos:"),
    ("Apply at the nearest", "Solicite en la más cercana"),
    ("Upon arrival, file", "A su llegada, presente"),
    ("Report every 90 days", "Reporte cada 90 días"),
    ("Renew annually", "Renovación anual"),
    ("Valid passport", "Pasaporte válido"),
    ("Proof of address", "Comprobante de domicilio"),
    ("Initial deposit", "Depósito inicial"),

    # --- Healthcare ---
    ("Public Healthcare", "Salud Pública"),
    ("Private Healthcare", "Salud Privada"),
    ("Typical Healthcare Costs", "Costos de Salud Típicos"),
    ("Typical Healthcare Costos", "Costos de Salud Típicos"),
    ("GP consultation", "Consulta médico general"),
    ("Specialist consultation", "Consulta especialista"),
    ("Emergency room visit", "Visita a urgencias"),
    ("Hospitalisation (per night)", "Hospitalización (por noche)"),
    ("Dental cleaning", "Limpieza dental"),
    ("Eye exam + glasses", "Examen de vista + gafas"),

    # --- Insurance ---
    ("Top Providers for Expats", "Mejores Aseguradoras para Expatriados"),
    ("Local insurer specialising in expats", "Aseguradora local especializada en expatriados"),
    ("Strong regional network", "Red regional sólida"),
    ("International coverage", "Cobertura internacional"),
    ("Comprehensive plans", "Planes integrales"),
    ("Flexible modular plans", "Planes modulares flexibles"),
    ("ideal if you travel frequently", "ideal si viaja frecuentemente"),

    # --- Bank ---
    ("Recommended Banks", "Bancos Recomendados"),
    ("Required Documents", "Documentos Requeridos"),
    ("Step-by-Step Process", "Proceso Paso a Paso"),
    ("Visit the bank branch in person", "Visite la sucursal bancaria en persona"),
    ("Request a savings account", "Solicite una cuenta de ahorro"),
    ("Present all documents", "Presente todos los documentos"),
    ("Receive debit card", "Reciba su tarjeta de débito"),
    ("Activate online/mobile banking", "Active la banca en línea/móvil"),
    ("Most expat-friendly bank", "Banco más amigable para expatriados"),
    ("Largest bank", "Banco más grande"),

    # --- Real Estate ---
    ("Ownership Options for Foreigners", "Opciones de Propiedad para Extranjeros"),
    ("Options for Foreigners", "Opciones de Propiedad para Extranjeros"),
    ("Purchase Process", "Proceso de Compra"),
    ("Typical Purchase Costs", "Costos de Compra Típicos"),
    ("Typical Purchase Costos", "Costos de Compra Típicos"),
    ("Typical Costos", "Costos Típicos"),
    ("Full ownership permitted for foreigners", "Propiedad plena permitida para extranjeros"),
    ("Hire a reputable real estate lawyer", "Contrate un abogado inmobiliario de reputación"),
    ("Transfer fee", "Tasa de transferencia"),
    ("Stamp duty", "Impuesto de timbre"),
    ("Withholding tax", "Retención fiscal"),
    ("Lawyer fees", "Honorarios del abogado"),
    ("Agent commission", "Comisión del agente"),

    # --- Common ---
    ("Pro Tip:", "Consejo Pro:"),
    ("Recommended:", "Recomendado:"),
    ("About This Guide", "Acerca de esta Guía"),
    ("Related Expat Guides", "Guías de Expatriación Relacionadas"),
    ("All Expat Guides", "Todas las Guías de Expatriación"),
    ("Retirement Visa Guide", "Guía de Visa de Jubilación"),
    ("Digital Nomad Visas", "Visas para Nómadas Digitales"),
    ("Global eVisa &amp; Travel Information Platform", "Plataforma Global de Información eVisa y Viajes"),

    # --- TOC entries (short-format files) ---
    ("Visa &amp; Residency", "Visa &amp; Residencia"),
    ("Healthcare", "Salud"),
    ("Bank Account", "Cuenta Bancaria"),
    ("Cheapest Countries to Retire", "Países más Baratos para Jubilarse"),
]


def translate_file(filepath, country):
    """Read file, apply all translations, write back."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Apply country-specific "in {Country}" translations
    for eng, esp in COUNTRY_IN_TRANSLATIONS.items():
        content = content.replace(eng, esp)

    # Apply all general translations
    for eng, esp in TRANSLATIONS:
        content = content.replace(eng, esp)

    # Fix links: replace href="/en/ with href="/es/ in Related Guides section
    # We need to be careful: the language dropdown English links should stay as /en/
    # The links to fix are specifically:
    #   - /en/expat-guides.html  (nav and related guides)
    #   - /en/retirement-visa-guide.html
    #   - /en/digital-nomad-visas-guide.html
    #   - /en/cheapest-countries-to-retire-abroad-2026.html
    # But NOT the language dropdown links like /en/expat-guide-{country}.html (those point to English version intentionally)

    # Fix the nav link to guides hub
    content = content.replace(
        'href="/en/expat-guides.html">Guías</a>',
        'href="/es/expat-guides.html">Guías</a>'
    )

    # Fix Related Guides section links
    content = content.replace(
        'href="/en/expat-guides.html" class="btn',
        'href="/es/expat-guides.html" class="btn'
    )
    content = content.replace(
        'href="/en/retirement-visa-guide.html"',
        'href="/es/retirement-visa-guide.html"'
    )
    content = content.replace(
        'href="/en/digital-nomad-visas-guide.html"',
        'href="/es/digital-nomad-visas-guide.html"'
    )
    content = content.replace(
        'href="/en/cheapest-countries-to-retire-abroad-2026.html"',
        'href="/es/cheapest-countries-to-retire-abroad-2026.html"'
    )

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        changes = sum(1 for a, b in zip(original, content) if a != b)
        print(f"  [UPDATED] {os.path.basename(filepath)} — content changed")
    else:
        print(f"  [NO CHANGE] {os.path.basename(filepath)}")


def main():
    print("=" * 60)
    print("Translating English content in Spanish expat guides...")
    print("=" * 60)

    processed = 0
    missing = []

    for country in COUNTRIES:
        filename = f"expat-guide-{country}.html"
        filepath = os.path.join(BASE_DIR, filename)

        if not os.path.exists(filepath):
            print(f"  [MISSING] {filename}")
            missing.append(filename)
            continue

        translate_file(filepath, country)
        processed += 1

    print()
    print(f"Processed: {processed} files")
    if missing:
        print(f"Missing:   {len(missing)} files — {', '.join(missing)}")
    print("Done.")


if __name__ == "__main__":
    main()
