#!/usr/bin/env python3
"""
Translate English content in all 16 Portuguese expat guide pages to Portuguese.
Uses string replace() for each known English phrase.
"""

import os
import glob

# Directory containing the Portuguese expat guide files
PT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www", "pt")

# All 16 countries
COUNTRIES = [
    "thailand", "portugal", "spain", "mexico", "vietnam", "malaysia",
    "japan", "uae", "colombia", "panama", "costa-rica", "greece",
    "georgia", "paraguay", "laos", "cambodia"
]

# Translation pairs: (English, Portuguese)
TRANSLATIONS = [
    # === Table headers ===
    # Note: "Visa Type" -> "Tipo de Visto" and "Details" -> "Detalhes" are already translated in the files
    # "Estimated Cost" and "Estimated Cout" variants
    ("Estimated Cost", "Custo Estimado"),
    ("Estimated Cout", "Custo Estimado"),
    # "Estimated Custo" is a half-translated form found in files
    ("Estimated Custo", "Custo Estimado"),

    # === Visa Section ===
    ("Available Visa Types", "Tipos de Visto Disponíveis"),
    ("Available Type de Visas", "Tipos de Visto Disponíveis"),
    ("Available Tipo de Vistos", "Tipos de Visto Disponíveis"),
    ("Step-by-Step Residency Process", "Processo de Residência Passo a Passo"),
    ("For expats 50+", "Para expatriados com 50 anos ou mais"),
    ("For remote workers earning", "Para trabalhadores remotos que ganham"),
    ("Determine your visa category", "Determine sua categoria de visto"),
    ("Gather documents:", "Reúna os documentos:"),
    ("Apply at the nearest", "Solicite na mais próxima"),
    ("Valid passport", "Passaporte válido"),
    ("Proof of address", "Comprovante de endereço"),
    ("Initial deposit", "Depósito inicial"),

    # === Healthcare Section ===
    ("Public Healthcare", "Saúde Pública"),
    ("Private Healthcare", "Saúde Privada"),
    ("Typical Healthcare Costs", "Custos de Saúde Típicos"),
    ("Typical Healthcare Custos", "Custos de Saúde Típicos"),
    ("GP consultation", "Consulta clínico geral"),
    ("Specialist consultation", "Consulta especialista"),
    ("Emergency room visit", "Visita ao pronto-socorro"),
    ("Hospitalisation (per night)", "Hospitalização (por noite)"),
    ("Dental cleaning", "Limpeza dentária"),
    ("Eye exam + glasses", "Exame de vista + óculos"),

    # === Insurance Section ===
    ("Top Providers for Expats", "Melhores Seguradoras para Expatriados"),
    ("Local insurer specialising in expats", "Seguradora local especializada em expatriados"),
    ("Strong regional network", "Rede regional sólida"),
    ("International coverage", "Cobertura internacional"),
    ("Comprehensive plans", "Planos abrangentes"),
    ("Flexible modular plans", "Planos modulares flexíveis"),

    # === Bank Section ===
    ("Recommended Banks", "Bancos Recomendados"),
    ("Required Documents", "Documentos Necessários"),
    ("Step-by-Step Process", "Processo Passo a Passo"),
    ("Visit the bank branch in person", "Visite a agência bancária pessoalmente"),
    ("Request a savings account", "Solicite uma conta poupança"),
    ("Present all documents", "Apresente todos os documentos"),
    ("Receive debit card", "Receba seu cartão de débito"),
    ("Activate online/mobile banking", "Ative o banco online/mobile"),

    # === Real Estate Section ===
    ("Ownership Options for Foreigners", "Opções de Propriedade para Estrangeiros"),
    ("Purchase Process", "Processo de Compra"),
    ("Typical Purchase Costs", "Custos de Compra Típicos"),
    ("Full ownership permitted for foreigners", "Propriedade plena permitida para estrangeiros"),
    ("Transfer fee", "Taxa de transferência"),
    ("Stamp duty", "Imposto de selo"),
    ("Withholding tax", "Imposto retido na fonte"),
    ("Lawyer fees", "Honorários do advogado"),
    ("Agent commission", "Comissão do agente"),

    # === Common / Footer ===
    ("Pro Tip:", "Dica Pro:"),
    ("Recommended:", "Recomendado:"),
    ("About This Guide", "Sobre este Guia"),
    ("Related Expat Guides", "Guias de Expatriação Relacionados"),
    ("All Expat Guides", "Todos os Guias"),
    ("Retirement Visa Guide", "Guia de Visto de Aposentadoria"),
    ("Digital Nomad Visas", "Vistos para Nômades Digitais"),
    ("Global eVisa &amp; Travel Information Platform", "Plataforma Global de Informação eVisa e Viagens"),
    ("Supplementary", "Complementar"),
]

# Fix links: replace href="/en/ with href="/pt/ in Related Guides section
# But we must NOT change the language dropdown links (those /en/ links are correct for the English version)
# The language dropdown links point to /en/expat-guide-{country}.html which is correct
# The related guides links at the bottom use /en/ which should be /pt/
LINK_REPLACEMENTS = [
    ('href="/en/expat-guides.html"', 'href="/pt/expat-guides.html"'),
    ('href="/en/retirement-visa-guide.html"', 'href="/pt/retirement-visa-guide.html"'),
    ('href="/en/digital-nomad-visas-guide.html"', 'href="/pt/digital-nomad-visas-guide.html"'),
    ('href="/en/cheapest-countries-to-retire-abroad-2026.html"', 'href="/pt/cheapest-countries-to-retire-abroad-2026.html"'),
]


def translate_file(filepath):
    """Apply all translations to a single file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = 0

    # Apply text translations
    for english, portuguese in TRANSLATIONS:
        if english in content:
            count = content.count(english)
            content = content.replace(english, portuguese)
            changes += count

    # Apply link fixes
    for old_link, new_link in LINK_REPLACEMENTS:
        if old_link in content:
            count = content.count(old_link)
            content = content.replace(old_link, new_link)
            changes += count

    # Write back only if changes were made
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def main():
    total_changes = 0
    files_changed = 0

    for country in COUNTRIES:
        filename = f"expat-guide-{country}.html"
        filepath = os.path.join(PT_DIR, filename)

        if not os.path.exists(filepath):
            print(f"  [SKIP] {filename} — file not found")
            continue

        changes = translate_file(filepath)
        total_changes += changes

        if changes > 0:
            files_changed += 1
            print(f"  [OK]   {filename} — {changes} replacements")
        else:
            print(f"  [--]   {filename} — no changes needed")

    print(f"\nDone: {files_changed} files modified, {total_changes} total replacements.")


if __name__ == "__main__":
    main()
