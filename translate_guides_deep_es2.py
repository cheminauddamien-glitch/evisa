#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep translation of ALL remaining English content in ES expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\es"

REPLACEMENTS = [
    # ── INTRO PARAGRAPHS ──────────────────────────────────────────────────────
    ("Thailand remains one of the world's most popular expat destinations, offering warm weather, affordable living, world-class cuisine and welcoming visa options for retirees, remote workers and families.",
     "Tailandia sigue siendo uno de los destinos de expatriados más populares del mundo, con clima cálido, coste de vida asequible, gastronomia de clase mundial y opciones de visa accesibles para jubilados, trabajadores remotos y familias."),

    # ── VISA TABLE CONTENT ────────────────────────────────────────────────────
    ("Requires proof of 800,000 THB in a Thai bank account OR 65,000 THB/month income. Valid 1 year, renewable. Allows multiple entries.",
     "Requiere prueba de 800.000 THB en una cuenta bancaria tailandesa O 65.000 THB/mes de ingresos. Válido 1 año, renovable. Permite entradas múltiples."),
    ("Valid 10 years. Allows working for overseas employers without a Thai work permit. Fast-track immigration.",
     "Válido 10 años. Permite trabajar para empleadores extranjeros sin permiso de trabajo tailandés. Inmigración acelerada."),
    ("5–20 year stay, VIP airport service. No income requirement. Purely residence-based.",
     "Estancia de 5 a 20 años, servicio VIP en aeropuerto. Sin requisito de ingresos. Puramente residencial."),
    ("Must be accompanied by a Thai Work Permit. Annual renewal.",
     "Debe ir acompañado de un permiso de trabajo tailandés. Renovación anual."),
    ("60 days (Tourist) or 30 days (visa-exempt). Can extend once at immigration. Many expats use border runs — now strictly monitored.",
     "60 días (turístico) o 30 días (exención de visa). Se puede ampliar una vez en inmigración. Muchos expatriados usan salidas de frontera — ahora estrictamente monitoreadas."),

    # ── STEP-BY-STEP ─────────────────────────────────────────────────────────
    ("retirement, LTR, Elite or business", "jubilación, LTR, Elite o negocios"),
    ("passport (6+ months), photos, bank statements, health insurance, medical certificate",
     "pasaporte (6+ meses de validez), fotos, extractos bancarios, seguro médico, certificado médico"),
    ("Thai embassy or consulate in your home country", "la embajada o consulado tailandés en tu país de origen"),
    ("TM.30 address notification within 24 hours", "la notificación de dirección TM.30 dentro de las 24 horas"),
    ("required for retirement visa deposit", "requerido para el depósito del visado de jubilación"),
    ("at the Immigration Bureau (online, by post or in person)", "en la Oficina de Inmigración (en línea, por correo o en persona)"),
    ("at your local Immigration office", "en tu oficina local de Inmigración"),

    # ── HEALTHCARE SECTION ────────────────────────────────────────────────────
    ("Thailand's public healthcare system (30-Baht Scheme) is available to Thai nationals and permanent residents only. As a non-resident expat, you cannot access public healthcare at subsidised rates.",
     "El sistema de salud pública tailandés (Programa 30 Baht) está disponible solo para ciudadanos tailandeses y residentes permanentes. Como expatriado no residente, no puede acceder a la atención médica pública a tarifas subsidiadas."),
    ("Private hospitals in Thailand (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
     "Los hospitales privados en Tailandia (Bangkok Hospital, Bumrungrad, Samitivej) son de primera clase y significativamente más baratos que los equivalentes occidentales. Una consulta cuesta 500–1.500 THB (~$14–42). Las cirugías mayores son 60–80% más baratas que en EE.UU. o Europa."),
    ("Most visa types (including LTR and Retirement OA) require proof of health insurance with minimum 40,000 THB outpatient / 400,000 THB inpatient coverage.",
     "La mayoría de los tipos de visa (incluyendo LTR y Jubilación OA) requieren prueba de seguro médico con cobertura mínima de 40.000 THB ambulatorio / 400.000 THB hospitalario."),

    # ── INSURANCE SECTION ─────────────────────────────────────────────────────
    ("for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
     "para visas de jubilación y LTR. Incluso con otros visados, se recomienda encarecidamente. Los hospitales privados tailandeses pueden ser caros para procedimientos mayores, y los costos de repatriación sin seguro pueden superar los $50.000."),
    ("Local insurer specialising in expats in Southeast Asia. Plans from ~$800/year. Good network of Thai private hospitals.",
     "Aseguradora local especializada en expatriados en el Sudeste Asiático. Planes desde ~$800/año. Buena red de hospitales privados tailandeses."),
    ("Strong regional network. Plans from ~$1,000/year. Well-regarded for cancer coverage.",
     "Sólida red regional. Planes desde ~$1.000/año. Reconocida por la cobertura de cáncer."),
    ("International coverage, ideal if you travel frequently or split time between countries. From ~$1,500/year.",
     "Cobertura internacional, ideal si viaja con frecuencia o divide el tiempo entre países. Desde ~$1.500/año."),
    ("Comprehensive plans with worldwide coverage. Particularly suited for high earners on LTR visas. From ~$1,800/year.",
     "Planes completos con cobertura mundial. Especialmente adecuado para altos ingresos con visa LTR. Desde ~$1.800/año."),
    ("Flexible modular plans. Can add dental, optical and maternity. From ~$1,200/year.",
     "Planes modulares flexibles. Se puede añadir dental, óptica y maternidad. Desde ~$1.200/año."),
    ("For the Retirement OA visa, your policy must be issued by a Thai-licensed insurer and must specifically state 40,000 / 400,000 THB minimum coverage. Pacific Cross and BUPA are the easiest to use for this purpose.",
     "Para el visado de Jubilación OA, su póliza debe ser emitida por una aseguradora con licencia tailandesa y debe indicar específicamente una cobertura mínima de 40.000 / 400.000 THB. Pacific Cross y BUPA son las más fáciles de usar para este propósito."),

    # ── BANK ACCOUNT SECTION ──────────────────────────────────────────────────
    ("it's required for the retirement visa deposit (800,000 THB), utility payments, rent transfers and daily transactions.",
     "se requiere para el depósito del visado de jubilación (800.000 THB), el pago de servicios, las transferencias de alquiler y las transacciones diarias."),
    ("Most expat-friendly bank. English-language app and staff in main branches. Fixed deposit accounts accepted for visa purposes.",
     "Banco más amigable con los expatriados. App y personal en inglés en las principales sucursales. Cuentas de depósito a plazo aceptadas para fines de visado."),
    ("Largest bank in Thailand. Strong international wire support. Commonly used for pension/income transfers.",
     "El banco más grande de Tailandia. Sólido soporte para transferencias internacionales. Comúnmente utilizado para transferencias de pensiones/ingresos."),
    ("Good English-language online banking. Competitive FX rates.",
     "Buena banca online en inglés. Tasas de cambio competitivas."),
    ("Easier account opening in some provinces. Partners with Mitsubishi UFJ.",
     "Apertura de cuenta más fácil en algunas provincias. Socio de Mitsubishi UFJ."),
    ("online opening not available for foreigners", "apertura en línea no disponible para extranjeros"),
    ("to the bank officer", "al funcionario del banco"),
    ("same day or within 5 business days", "el mismo día o dentro de 5 días hábiles"),
    ("may require Thai phone number", "puede requerir número de teléfono tailandés"),

    # ── REAL ESTATE SECTION ───────────────────────────────────────────────────
    ("Foreigners cannot own land in Thailand, but they can own condominium units freehold (up to 49% of a building's total floor area may be foreign-owned). Houses and land must be held through a Thai company, a 30-year leasehold or a Thai spouse.",
     "Los extranjeros no pueden ser propietarios de terrenos en Tailandia, pero pueden poseer unidades de condominio en pleno dominio (hasta el 49% de la superficie total de un edificio puede ser de propiedad extranjera). Las casas y los terrenos deben ser propiedad de una empresa tailandesa, un arrendamiento de 30 años o un cónyuge tailandés."),
    ("Full ownership permitted for foreigners. Must be paid from overseas in foreign currency (proof required). Most popular option.",
     "Propiedad plena permitida para extranjeros. Debe pagarse desde el extranjero en moneda extranjera (se requiere prueba). Opción más popular."),
    ("for 30 years, renewable twice (total 90 years in practice). Common for villas and townhouses.",
     "por 30 años, renovable dos veces (90 años en total en la práctica). Común para villas y casas adosadas."),
    ("A Thai limited company (min. 51% Thai shareholders) can hold land. Complex, legal fees $2,000–5,000. Requires ongoing compliance.",
     "Una empresa limitada tailandesa (mín. 51% de accionistas tailandeses) puede tener terrenos. Complejo, honorarios legales $2.000–5.000. Requiere cumplimiento continuo."),
    ("a Thai spouse's name. No legal protection in case of divorce. Not recommended.",
     "nombre de un cónyuge tailandés. Sin protección legal en caso de divorcio. No recomendado."),

    # ── PURCHASE PROCESS ──────────────────────────────────────────────────────
    ("Hire a reputable real estate lawyer (budget 30,000–80,000 THB)",
     "Contrate un abogado inmobiliario de reputación (presupuesto 30.000–80.000 THB)"),
    ("Verify the title deed (Chanote / Nor Sor 4 — the only fully secure title)",
     "Verifique la escritura de propiedad (Chanote / Nor Sor 4 — el único título completamente seguro)"),
    ("Sign a Reservation Agreement and pay deposit (50,000–100,000 THB)",
     "Firme un Acuerdo de Reserva y pague el depósito (50.000–100.000 THB)"),
    ("Due diligence: check no liens, correct zoning, building permits",
     "Diligencia debida: verificar ausencia de gravámenes, zonificación correcta, permisos de construcción"),
    ("Transfer funds from overseas bank to Thailand (keep FET form for proof)",
     "Transfiera fondos desde un banco extranjero a Tailandia (conserve el formulario FET como prueba)"),
    ("Sign Sale & Purchase Agreement (SPA)", "Firme el Contrato de Compraventa (SPA)"),
    ("Transfer at the Land Office — both parties must attend",
     "Transferencia en la Oficina de Tierras — ambas partes deben asistir"),
    ("Pay transfer fees (typically 2–3% of assessed value)",
     "Pague las tasas de transferencia (normalmente 2–3% del valor tasado)"),

    # ── COST TABLE ────────────────────────────────────────────────────────────
    ("Transfer fee", "Tasa de transferencia"),
    ("Stamp duty or specific business tax", "Impuesto de timbre o impuesto comercial específico"),
    ("Withholding tax", "Retención fiscal"),
    ("Lawyer fees", "Honorarios de abogado"),
    ("Agent commission", "Comisión del agente"),
    ("2% of the appraised value (split buyer/seller)", "2% del valor tasado (compartido comprador/vendedor)"),
    ("0.5% stamp duty OR 3.3% SBT if sold within 5 years", "0,5% impuesto de timbre O 3,3% SBT si se vende en 5 años"),
    ("1–3% (paid by seller)", "1–3% (pagado por el vendedor)"),
    ("3–5% (paid by seller)", "3–5% (pagado por el vendedor)"),

    # ── PRO TIPS ──────────────────────────────────────────────────────────────
    ("Always use a Chanote (NS4J) title deed. Avoid Nor Sor 3 or Sor Kor 1 titles — they offer less legal protection and cannot be mortgaged.",
     "Utilice siempre una escritura Chanote (NS4J). Evite los títulos Nor Sor 3 o Sor Kor 1 — ofrecen menos protección legal y no pueden hipotecarse."),
    ("The LTR Visa is the best option for remote workers — 10 years, no 90-day reports, and it exempts certain income from Thai tax.",
     "La Visa LTR es la mejor opción para trabajadores remotos — 10 años, sin informes de 90 días y exime ciertos ingresos del impuesto tailandés."),
    ("Kasikorn Bank's Asoke (Bangkok) or Nimman (Chiang Mai) branches are known for being particularly helpful to expats. Arrive early — queues can be long.",
     "Las sucursales Asoke (Bangkok) o Nimman (Chiang Mai) de Kasikorn Bank son conocidas por ser especialmente útiles para expatriados. Llegue temprano — las colas pueden ser largas."),

    # ── E-E-A-T ───────────────────────────────────────────────────────────────
    ("We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Nos esforzamos por mantener toda la información actualizada, pero las reglas de visa, los costos de atención médica y las regulaciones inmobiliarias cambian con frecuencia. Siempre verifique los requisitos actuales con fuentes gubernamentales oficiales y consulte a un profesional con licencia antes de tomar decisiones importantes."),
    ("This guide is researched and maintained by the editorial team at eVisa-Card.com.",
     "Esta guía es investigada y mantenida por el equipo editorial de eVisa-Card.com."),

    # ── GENERIC ───────────────────────────────────────────────────────────────
    ("Valid passport", "Pasaporte válido"),
    ("GP consultation (private)", "Consulta médico de cabecera (privado)"),
    ("Specialist consultation", "Consulta especialista"),
    ("Emergency room visit", "Visita a urgencias"),
    ("Hospitalisation (per night)", "Hospitalización (por noche)"),
    ("Dental cleaning", "Limpieza dental"),
    ("Eye exam + glasses", "Examen ocular + gafas"),
    ("Global eVisa & Travel Information Platform", "Plataforma Mundial de Información sobre eVisa y Viajes"),
    ("Follow eVisa-Card.com", "Siga eVisa-Card.com"),
    ("March 2026", "Marzo 2026"),
    ("Last updated:", "Última actualización:"),
]

def main():
    total_replacements = 0
    files_updated = 0
    for fname in sorted(os.listdir(BASE)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        original = html
        file_replacements = 0
        for eng, es in REPLACEMENTS:
            count = html.count(eng)
            if count > 0:
                html = html.replace(eng, es)
                file_replacements += count
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            files_updated += 1
            total_replacements += file_replacements
            print(f"  OK {fname}: {file_replacements} replacements")
    print(f"\nDone: {files_updated} files, {total_replacements} total replacements.")

if __name__ == "__main__":
    main()
