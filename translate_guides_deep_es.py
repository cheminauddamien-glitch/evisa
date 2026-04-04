#!/usr/bin/env python3
"""Deep translation of ALL remaining English content in ES expat guide pages."""
import os, re

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\es"

# All English->Spanish replacements (ordered from longest to shortest to avoid partial matches)
REPLACEMENTS = [
    # =========================================================
    # META DESCRIPTIONS
    # =========================================================
    ("Complete guide to living in Tailandia as an expat in 2026. Visa options, residency, healthcare, supplementary insurance, bank accounts and property buying for foreigners.",
     "Guía completa para vivir en Tailandia como expatriado en 2026. Opciones de visa, residencia, sanidad, seguro complementario, cuentas bancarias y compra de propiedad para extranjeros."),
    ("Complete guide to living in Japón as an expat in 2026. Highly skilled professional visa, digital nomad visa, national health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en Japón como expatriado en 2026. Visa de profesional altamente cualificado, visa de nómada digital, seguro de salud nacional, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Vietnam as an expat in 2026. E-visa, residency, TRC, healthcare, health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en Vietnam como expatriado en 2026. E-visa, residencia, TRC, sanidad, seguro de salud, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living in Malasia as an expat in 2026. MM2H visa, DE Rantau nomad pass, healthcare, health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en Malasia como expatriado en 2026. Visa MM2H, pase nómada DE Rantau, sanidad, seguro de salud, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living in Camboya as an expat in 2026. E-visa, ordinary residence visa, business visa, healthcare, bank accounts and property for foreigners.",
     "Guía completa para vivir en Camboya como expatriado en 2026. E-visa, visa de residencia ordinaria, visa de negocios, sanidad, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Colombia as an expat in 2026. Digital nomad visa, pensionado visa, healthcare, health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en Colombia como expatriado en 2026. Visa de nómada digital, visa pensionado, sanidad, seguro de salud, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Costa Rica as an expat in 2026. Pensionado visa, rentista visa, healthcare, CAJA insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en Costa Rica como expatriado en 2026. Visa pensionado, visa rentista, sanidad, seguro CAJA, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Georgia (Caucasus) as an expat in 2026. Visa-free 365 days, residency by investment, flat 20% tax, healthcare, bank accounts and property for foreigners.",
     "Guía completa para vivir en Georgia (Cáucaso) como expatriado en 2026. Sin visa 365 días, residencia por inversión, impuesto fijo del 20%, sanidad, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living in Grecia as an expat in 2026. Financially independent person visa, Golden Visa, Greek Non-Dom tax, healthcare, bank accounts and property for foreigners.",
     "Guía completa para vivir en Grecia como expatriado en 2026. Visa de persona financieramente independiente, Visa Dorada, régimen fiscal no-dom griego, sanidad, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Laos as an expat in 2026. Laos visa, business visa, temporary residence, healthcare, bank accounts and property for foreigners.",
     "Guía completa para vivir en Laos como expatriado en 2026. Visa de Laos, visa de negocios, residencia temporal, sanidad, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living in M\u00e9xico as an expat in 2026. Temporary and permanent residency, IMSS healthcare, health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en México como expatriado en 2026. Residencia temporal y permanente, sanidad IMSS, seguro de salud, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living in Panam\u00e1 as an expat in 2026. Pensionado visa, residency, healthcare, health insurance, bank accounts and property buying for foreigners.",
     "Guía completa para vivir en Panamá como expatriado en 2026. Visa pensionado, residencia, sanidad, seguro de salud, cuentas bancarias y compra de propiedad para extranjeros."),
    ("Complete guide to living en Paraguay as an expat in 2026. Permanent residency, tax residency, territorial tax system, healthcare, bank accounts and property for foreigners.",
     "Guía completa para vivir en Paraguay como expatriado en 2026. Residencia permanente, residencia fiscal, sistema fiscal territorial, sanidad, cuentas bancarias y propiedad para extranjeros."),
    ("Complete guide to living en Portugal as an expat in 2026. D7 visa, Golden Visa, NHR tax status, healthcare, health insurance, bank accounts and property buying for foreigners.",
     "Guía completa para vivir en Portugal como expatriado en 2026. Visa D7, Visa Dorada, régimen fiscal NHR, sanidad, seguro de salud, cuentas bancarias y compra de propiedad para extranjeros."),
    ("Complete guide to living in Espa\u00f1a as an expat in 2026. Non-lucrative visa, digital nomad visa, healthcare, health insurance, bank accounts and property buying for foreigners.",
     "Guía completa para vivir en España como expatriado en 2026. Visa no lucrativa, visa de nómada digital, sanidad, seguro de salud, cuentas bancarias y compra de propiedad para extranjeros."),
    ("Complete guide to living in the EAU as an expat in 2026. Golden Visa, green visa, freelance permit, healthcare, health insurance, bank accounts and property for foreigners.",
     "Guía completa para vivir en los EAU como expatriado en 2026. Visa Dorada, visa verde, permiso de autónomo, sanidad, seguro de salud, cuentas bancarias y propiedad para extranjeros."),

    # =========================================================
    # INTRO PARAGRAPHS (country-specific)
    # =========================================================
    ("Thailand remains one of the world's most popular expat destinations, offering warm weather, affordable living, world-class cuisine and welcoming visa options for retirees, remote workers and families.",
     "Tailandia sigue siendo uno de los destinos de expatriados más populares del mundo, con clima cálido, coste de vida asequible, gastronomía de primera y opciones de visado atractivas para jubilados, teletrabajadores y familias."),

    ("Japan combines extraordinary safety, efficient infrastructure, unique culture and excellent healthcare. The 2024 Digital Nomad Visa and the Highly Skilled Professional (HSP) point system have made Japan more accessible than ever for skilled foreign workers.",
     "Japón combina una seguridad extraordinaria, infraestructuras eficientes, cultura única y una sanidad excelente. La Visa de Nómada Digital 2024 y el sistema de puntos para Profesionales Altamente Cualificados (HSP) han hecho Japón más accesible que nunca para trabajadores extranjeros cualificados."),

    ("Vietnam offers an unbeatable combination of ultra-low cost of living, delicious cuisine, dynamic cities and stunning natural scenery. Hanoi and Ho Chi Minh City have thriving expat communities, with fast internet and a growing remote worker scene.",
     "Vietnam ofrece una combinación inigualable de coste de vida ultrabarato, gastronomía deliciosa, ciudades dinámicas y paisajes naturales impresionantes. Hanói y Ciudad Ho Chi Minh cuentan con comunidades de expatriados prósperas, internet rápido y una creciente escena de trabajo remoto."),

    ("Malaysia is one of Asia's most underrated expat destinations — English is widely spoken, infrastructure is excellent, the food is extraordinary and the cost of living is among the lowest in the region for the quality on offer.",
     "Malasia es uno de los destinos para expatriados más infravalorados de Asia: el inglés se habla ampliamente, la infraestructura es excelente, la gastronomía es extraordinaria y el coste de vida se encuentra entre los más bajos de la región para la calidad ofrecida."),

    ("Cambodia is one of Southeast Asia's most accessible expat destinations — ultra-low cost of living, a fully dollarised economy (USD used everywhere), relatively straightforward residency via business or ordinary visa, and Phnom Penh and Siem Reap offer surprisingly vibrant expat communities.",
     "Camboya es uno de los destinos de expatriados más accesibles del Sudeste Asiático: coste de vida ultrabarato, una economía totalmente dolarizada (USD en todas partes), residencia relativamente sencilla mediante visado de negocios u ordinario, y Phnom Penh y Siem Reap ofrecen comunidades de expatriados sorprendentemente animadas."),

    ("Laos is Southeast Asia's most peaceful and unhurried country. Luang Prabang, Vang Vieng and Vientiane attract expats seeking a quiet lifestyle, stunning natural landscapes and ultra-low cost of living. Infrastructure is limited compared to Thailand or Vietnam, but for those seeking tranquillity, Laos is incomparable.",
     "Laos es el país más tranquilo y pausado del Sudeste Asiático. Luang Prabang, Vang Vieng y Vientiane atraen a expatriados que buscan un estilo de vida tranquilo, paisajes naturales impresionantes y un coste de vida ultrabarato. La infraestructura es limitada en comparación con Tailandia o Vietnam, pero para quienes buscan tranquilidad, Laos es incomparable."),

    ("Georgia (the Caucasus country) has emerged as one of the most popular destinations for digital nomads, entrepreneurs and expats worldwide. The reasons: 365-day visa-free entry for 95+ nationalities, a flat 20% income tax (1% for small businesses), ultra-low cost of living, fast internet and a young, cosmopolitan capital in Tbilisi.",
     "Georgia (el país del Cáucaso) se ha convertido en uno de los destinos más populares para nómadas digitales, emprendedores y expatriados de todo el mundo. Las razones: entrada sin visado de 365 días para más de 95 nacionalidades, impuesto sobre la renta fijo del 20% (1% para pequeñas empresas), coste de vida ultrabarato, internet rápido y una capital joven y cosmopolita en Tiflis."),

    ("Greece offers a compelling combination: Mediterranean lifestyle, ancient culture, excellent climate, affordable cost of living by EU standards, world-class cuisine and a strong expat community. The Financially Independent Person visa and a generous non-dom tax regime make it increasingly attractive to retirees and remote workers.",
     "Grecia ofrece una combinación atractiva: estilo de vida mediterráneo, cultura ancestral, clima excelente, coste de vida asequible para los estándares de la UE, gastronomía de primera y una sólida comunidad de expatriados. La visa de Persona Financieramente Independiente y un generoso régimen fiscal no-dom la hacen cada vez más atractiva para jubilados y teletrabajadores."),

    ("Spain offers year-round sunshine, rich culture, excellent food and one of Europe's best healthcare systems. With the Non-Lucrative Visa, Digital Nomad Visa and Golden Visa, Spain has become a top destination for expats from around the world.",
     "España ofrece sol durante todo el año, cultura rica, excelente gastronomía y uno de los mejores sistemas de salud de Europa. Con la Visa No Lucrativa, la Visa de Nómada Digital y la Visa Dorada, España se ha convertido en un destino de primer nivel para expatriados de todo el mundo."),

    ("Portugal consistently ranks as one of the best countries for expats — EU membership, mild climate, low crime, excellent healthcare and a growing expat community make it a top destination for retirees, remote workers and families.",
     "Portugal ocupa sistemáticamente uno de los primeros puestos entre los mejores países para expatriados: pertenencia a la UE, clima suave, baja criminalidad, excelente sanidad y una creciente comunidad de expatriados lo convierten en un destino de primer nivel para jubilados, teletrabajadores y familias."),

    ("Mexico offers stunning diversity — from the cosmopolitan energy of Mexico City to the beaches of Tulum and the colonial charm of Oaxaca. Affordable living, warm weather and straightforward residency make it a top expat destination in Latin America.",
     "México ofrece una diversidad impresionante: desde la energía cosmopolita de Ciudad de México hasta las playas de Tulum y el encanto colonial de Oaxaca. El coste de vida asequible, el clima cálido y la residencia sencilla lo convierten en uno de los principales destinos de expatriados en América Latina."),

    ("Colombia has transformed dramatically over the past decade — Medellín was named the world's most innovative city, and cities like Bogotá, Cartagena and Santa Marta offer a rich mix of culture, climate and affordability. Colombia's digital nomad visa and affordable EPS health system make it increasingly popular with expats.",
     "Colombia se ha transformado drásticamente en la última década: Medellín fue nombrada la ciudad más innovadora del mundo, y ciudades como Bogotá, Cartagena y Santa Marta ofrecen una rica mezcla de cultura, clima y accesibilidad económica. La visa de nómada digital de Colombia y el asequible sistema de salud EPS la hacen cada vez más popular entre los expatriados."),

    ("Costa Rica — Pura Vida — is a long-standing favourite of North American and European expats. Stable democracy, no standing army, excellent healthcare, lush biodiversity and a well-developed expat infrastructure make it one of the easiest countries in Latin America to settle in.",
     "Costa Rica — Pura Vida — es el favorito histórico de los expatriados norteamericanos y europeos. Democracia estable, sin ejército permanente, excelente sanidad, rica biodiversidad e infraestructura expatriada bien desarrollada la convierten en uno de los países más fáciles para establecerse en América Latina."),

    ("Panama offers a unique combination: a dollarised economy, excellent healthcare, zero taxes on foreign-source income, a tropical climate and one of the world's most famous retirement visa programmes — the Pensionado. It is consistently ranked as a top retirement destination in the Americas.",
     "Panamá ofrece una combinación única: economía dolarizada, excelente sanidad, cero impuestos sobre ingresos de fuente extranjera, clima tropical y uno de los programas de visado de jubilación más famosos del mundo: el Pensionado. Está sistemáticamente clasificado como uno de los mejores destinos de jubilación en las Américas."),

    ("Paraguay is Latin America's best-kept secret for expats seeking a low-tax, low-cost destination. The country operates on a territorial tax system (only local income is taxed), permanent residency is obtainable in 3 months, and the cost of living is among the lowest in South America. Asunción is a modern, safe capital with a growing expat community.",
     "Paraguay es el secreto mejor guardado de América Latina para los expatriados que buscan un destino de bajos impuestos y bajo coste. El país opera con un sistema fiscal territorial (solo se gravan los ingresos locales), la residencia permanente se obtiene en 3 meses y el coste de vida se encuentra entre los más bajos de América del Sur. Asunción es una capital moderna y segura con una creciente comunidad de expatriados."),

    ("The UAE — particularly Dubai — has positioned itself as the world's leading destination for high-net-worth expats and remote workers. Zero income tax, world-class infrastructure, modern healthcare and a cosmopolitan lifestyle make it uniquely attractive.",
     "Los EAU, en particular Dubái, se han posicionado como el principal destino mundial para expatriados de alto poder adquisitivo y teletrabajadores. Cero impuesto sobre la renta, infraestructuras de primera, sanidad moderna y un estilo de vida cosmopolita lo hacen especialmente atractivo."),

    # =========================================================
    # THAILAND VISA TABLE CONTENT
    # =========================================================
    ("Requires proof of 800,000 THB in a Thai bank account OR 65,000 THB/month income. Valid 1 year, renewable. Allows multiple entries.",
     "Requiere prueba de 800.000 THB en una cuenta bancaria tailandesa O 65.000 THB/mes de ingresos. Válida 1 año, renovable. Permite entradas múltiples."),
    ("Valid 10 years. Allows working for overseas employers without a Thai work permit. Fast-track immigration.",
     "Válida 10 años. Permite trabajar para empleadores extranjeros sin permiso de trabajo tailandés. Inmigración acelerada."),
    ("5–20 year stay, VIP airport service. No income requirement. Purely residence-based.",
     "Estancia de 5 a 20 años, servicio VIP en el aeropuerto. Sin requisito de ingresos. Puramente residencial."),
    ("Must be accompanied by a Thai Work Permit. Annual renewal.",
     "Debe ir acompañado de un permiso de trabajo tailandés. Renovación anual."),
    ("60 days (Tourist) or 30 days (visa-exempt). Can extend once at immigration. Many expats use border runs — now strictly monitored.",
     "60 días (turista) o 30 días (exención de visa). Se puede prorrogar una vez en inmigración. Muchos expatriados hacen salidas fronterizas, ahora estrictamente controladas."),

    # =========================================================
    # THAILAND STEP-BY-STEP
    # =========================================================
    ("retirement, LTR, Elite or business", "jubilación, LTR, Elite o negocios"),
    ("passport (6+ months), photos, bank statements, health insurance, medical certificate",
     "pasaporte (más de 6 meses de validez), fotos, extractos bancarios, seguro de salud, certificado médico"),
    ("Thai embassy or consulate in your home country", "la embajada o el consulado tailandés en su país de origen"),
    ("TM.30 address notification within 24 hours", "la notificación de domicilio TM.30 en un plazo de 24 horas"),
    ("required for retirement visa deposit", "necesario para el depósito del visado de jubilación"),
    ("at the Immigration Bureau (online, by post or in person)", "en la Oficina de Inmigración (en línea, por correo o en persona)"),
    ("at your local Immigration office", "en su oficina local de Inmigración"),

    # =========================================================
    # THAILAND HEALTHCARE
    # =========================================================
    ("Thailand's public healthcare system (30-Baht Scheme) is available to Thai nationals and permanent residents only. As a non-resident expat, you cannot access public healthcare at subsidised rates.",
     "El sistema de salud público de Tailandia (Programa de 30 Baht) está disponible únicamente para ciudadanos tailandeses y residentes permanentes. Como expatriado no residente, no puede acceder a la sanidad pública a tarifas subvencionadas."),
    ("Private hospitals in Thailand (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
     "Los hospitales privados en Tailandia (Bangkok Hospital, Bumrungrad, Samitivej) son de clase mundial y considerablemente más baratos que sus equivalentes occidentales. Una consulta cuesta entre 500 y 1.500 THB (~14–42 $). La cirugía mayor es entre un 60 y un 80% más barata que en Estados Unidos o Europa."),
    ("Most visa types (including LTR and Retirement OA) require proof of health insurance with minimum 40,000 THB outpatient / 400,000 THB inpatient coverage.",
     "La mayoría de los tipos de visado (incluidos LTR y Jubilación OA) requieren prueba de seguro de salud con una cobertura mínima de 40.000 THB ambulatoria / 400.000 THB hospitalaria."),
    ("Private hospitals en Tailandia (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
     "Los hospitales privados en Tailandia (Bangkok Hospital, Bumrungrad, Samitivej) son de clase mundial y considerablemente más baratos que sus equivalentes occidentales. Una consulta cuesta entre 500 y 1.500 THB (~14–42 $). La cirugía mayor es entre un 60 y un 80% más barata que en Estados Unidos o Europa."),

    # =========================================================
    # THAILAND INSURANCE SECTION
    # =========================================================
    ("International health insurance is mandatory for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
     "El seguro de salud internacional es obligatorio para los visados de jubilación y LTR. Incluso con otros visados, se recomienda encarecidamente. Los hospitales privados tailandeses pueden ser costosos para procedimientos mayores, y los gastos de repatriación sin seguro pueden superar los 50.000 $."),
    ("for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
     "para los visados de jubilación y LTR. Incluso con otros visados, se recomienda encarecidamente. Los hospitales privados tailandeses pueden ser costosos para procedimientos mayores, y los gastos de repatriación sin seguro pueden superar los 50.000 $."),
    ("Aseguradora local especializada en expatriados in Southeast Asia. Plans from ~$800/year. Good network of Thai private hospitals.",
     "Aseguradora local especializada en expatriados en el Sudeste Asiático. Planes desde ~800 $/año. Buena red de hospitales privados tailandeses."),
    ("Red regional sólida. Plans from ~$1,000/year. Well-regarded for cancer coverage.",
     "Red regional sólida. Planes desde ~1.000 $/año. Reconocida por la cobertura oncológica."),
    ("Cobertura internacional, ideal si viaja frecuentemente or split time between countries. From ~$1,500/year.",
     "Cobertura internacional, ideal si viaja frecuentemente o reparte su tiempo entre países. Desde ~1.500 $/año."),
    ("Planes integrales with worldwide coverage. Particularly suited for high earners on LTR visas. From ~$1,800/year.",
     "Planes integrales con cobertura mundial. Especialmente adecuado para altos ingresos con visa LTR. Desde ~1.800 $/año."),
    ("Planes modulares flexibles. Can add dental, optical and maternity. From ~$1,200/year.",
     "Planes modulares flexibles. Se puede añadir dental, óptica y maternidad. Desde ~1.200 $/año."),
    ("For the Retirement OA visa, your policy must be issued by a Thai-licensed insurer and must specifically state 40,000 / 400,000 THB minimum coverage. Pacific Cross and BUPA are the easiest to use for this purpose.",
     "Para el visado de Jubilación OA, su póliza debe ser emitida por una aseguradora con licencia tailandesa y debe indicar específicamente una cobertura mínima de 40.000 / 400.000 THB. Pacific Cross y BUPA son las más fáciles de usar para este fin."),

    # =========================================================
    # THAILAND BANK ACCOUNT
    # =========================================================
    ("A Thai bank account is practically essential for expats — it's required for the retirement visa deposit (800,000 THB), utility payments, rent transfers and daily transactions.",
     "Una cuenta bancaria tailandesa es prácticamente imprescindible para los expatriados: es necesaria para el depósito del visado de jubilación (800.000 THB), el pago de servicios, las transferencias de alquiler y las transacciones diarias."),
    ("Banco más amigable para expatriados. English-language app and staff in main branches. Fixed deposit accounts accepted for visa purposes.",
     "Banco más amigable para expatriados. Aplicación y personal en inglés en las principales sucursales. Cuentas de depósito fijo aceptadas para trámites de visado."),
    ("Banco más grande en Tailandia. Strong international wire support. Commonly used for pension/income transfers.",
     "Banco más grande de Tailandia. Excelente soporte para transferencias internacionales. Utilizado habitualmente para transferencias de pensiones e ingresos."),
    ("Good English-language online banking. Competitive FX rates.",
     "Banca en línea en inglés de calidad. Tasas de cambio competitivas."),
    ("Easier account opening in some provinces. Partners with Mitsubishi UFJ.",
     "Apertura de cuenta más sencilla en algunas provincias. Socio de Mitsubishi UFJ."),
    ("online opening not available for foreigners", "apertura en línea no disponible para extranjeros"),
    ("to the bank officer", "al empleado bancario"),
    ("same day or within 5 business days", "el mismo día o en un plazo de 5 días hábiles"),
    ("may require Thai phone number", "puede requerir un número de teléfono tailandés"),

    # =========================================================
    # THAILAND REAL ESTATE
    # =========================================================
    ("Foreigners cannot own land in Thailand, but they can own condominium units freehold (up to 49% of a building's total floor area may be foreign-owned). Houses and land must be held through a Thai company, a 30-year leasehold or a Thai spouse.",
     "Los extranjeros no pueden poseer terrenos en Tailandia, pero pueden poseer unidades de condominio en plena propiedad (hasta el 49% de la superficie total de un edificio puede ser propiedad de extranjeros). Las casas y los terrenos deben mantenerse a través de una empresa tailandesa, un arrendamiento de 30 años o un cónyuge tailandés."),
    ("Foreigners CANNOT own land en Camboya, but the law was amended in 2010 to allow foreigners to own condominium units on the 2nd floor and above (not ground floor or land). Workarounds include 50-year long-term leases and Cambodian company structures.",
     "Los extranjeros NO PUEDEN poseer terrenos en Camboya, pero la ley fue modificada en 2010 para permitir a los extranjeros poseer unidades de condominio a partir del segundo piso (no planta baja ni terrenos). Las alternativas incluyen arrendamientos a largo plazo de 50 años y estructuras de empresa camboyana."),
    ("Foreigners CANNOT own land in Laos. This is constitutionally prohibited. However, foreigners can lease land for up to 50 years (with possible renewal), hold ownership of structures (not land), and invest through a Lao company with local partners.",
     "Los extranjeros NO PUEDEN poseer terrenos en Laos. Esto está prohibido constitucionalmente. Sin embargo, los extranjeros pueden arrendar terrenos por hasta 50 años (con posible renovación), poseer estructuras (no terrenos) e invertir a través de una empresa laosiana con socios locales."),
    ("Full ownership permitted for foreigners. Must be paid from overseas in foreign currency (proof required). Most popular option.",
     "Propiedad plena permitida para extranjeros. Debe pagarse desde el extranjero en divisa extranjera (se requiere justificante). Opción más popular."),
    ("for 30 years, renewable twice (total 90 years in practice). Common for villas and townhouses.",
     "por 30 años, renovable dos veces (90 años en total en la práctica). Habitual para villas y casas adosadas."),
    ("A Thai limited company (min. 51% Thai shareholders) can hold land. Complex, legal fees $2,000–5,000. Requires ongoing compliance.",
     "Una empresa tailandesa de responsabilidad limitada (mín. 51% de accionistas tailandeses) puede poseer terrenos. Complejo, honorarios legales de 2.000–5.000 $. Requiere cumplimiento continuo."),
    ("a Thai spouse's name. No legal protection in case of divorce. Not recommended.",
     "a nombre de un cónyuge tailandés. Sin protección legal en caso de divorcio. No recomendado."),

    # =========================================================
    # THAILAND PURCHASE PROCESS
    # =========================================================
    ("Contrate un abogado inmobiliario de reputación (budget 30,000–80,000 THB)",
     "Contrate un abogado inmobiliario de reputación (presupuesto 30.000–80.000 THB)"),
    ("Verify the title deed (Chanote / Nor Sor 4 — the only fully secure title)",
     "Verifique la escritura de propiedad (Chanote / Nor Sor 4 — el único título completamente seguro)"),
    ("Sign a Reservation Agreement and pay deposit (50,000–100,000 THB)",
     "Firme un Acuerdo de Reserva y pague el depósito (50.000–100.000 THB)"),
    ("Due diligence: check no liens, correct zoning, building permits",
     "Diligencia debida: comprobar la ausencia de gravámenes, zonificación correcta y permisos de construcción"),
    ("Transfer funds from overseas bank to Thailand (keep FET form for proof)",
     "Transfiera fondos desde un banco extranjero a Tailandia (conserve el formulario FET como justificante)"),
    ("Sign Sale & Purchase Agreement (SPA)",
     "Firme el Contrato de Compraventa (SPA)"),
    ("Transfer at the Land Office — both parties must attend",
     "Transferencia en la Oficina de Tierras — ambas partes deben estar presentes"),
    ("Pay transfer fees (typically 2–3% of assessed value)",
     "Pague los gastos de transferencia (normalmente 2–3% del valor tasado)"),

    # =========================================================
    # THAILAND COST TABLE
    # =========================================================
    ("2% of the appraised value (split buyer/seller)", "2% del valor tasado (repartido entre comprador y vendedor)"),
    ("0.5% stamp duty OR 3.3% SBT if sold within 5 years", "0,5% de impuesto de timbre O 3,3% SBT si se vende antes de 5 años"),
    ("Impuesto de timbre or specific business tax", "Impuesto de timbre o impuesto comercial específico"),
    ("1–3% (paid by seller)", "1–3% (pagado por el vendedor)"),
    ("3–5% (paid by seller)", "3–5% (pagado por el vendedor)"),

    # =========================================================
    # THAILAND PRO TIPS
    # =========================================================
    ("Always use a Chanote (NS4J) title deed. Avoid Nor Sor 3 or Sor Kor 1 titles — they offer less legal protection and cannot be mortgaged.",
     "Utilice siempre una escritura Chanote (NS4J). Evite los títulos Nor Sor 3 o Sor Kor 1: ofrecen menor protección legal y no pueden hipotecarse."),
    ("The LTR Visa is the best option for remote workers — 10 years, no 90-day reports, and it exempts certain income from Thai tax.",
     "La Visa LTR es la mejor opción para los teletrabajadores: 10 años, sin informes de 90 días y exime ciertos ingresos del impuesto tailandés."),
    ("Kasikorn Bank's Asoke (Bangkok) or Nimman (Chiang Mai) branches are known for being particularly helpful to expats. Arrive early — queues can be long.",
     "Las sucursales de Kasikorn Bank en Asoke (Bangkok) o Nimman (Chiang Mai) son conocidas por ser especialmente útiles para los expatriados. Llegue temprano: las colas pueden ser largas."),

    # =========================================================
    # JAPAN VISA TABLE
    # =========================================================
    ("New 6-month visa for remote workers earning ¥10,000,000/year (~$65,000+). Single-entry, extendable for 6 months. Must have health insurance. Cannot work for Japanese companies.",
     "Nueva visa de 6 meses para teletrabajadores que ganen ¥10.000.000/año (~65.000 $+). Entrada única, prorrogable 6 meses. Debe tener seguro de salud. No puede trabajar para empresas japonesas."),
    ("Points-based system (70+ points). Points for education, income, age, Japanese ability. Allows fast-track to permanent residence (1–3 years vs standard 10).",
     "Sistema de puntos (70+ puntos). Puntos por educación, ingresos, edad y nivel de japonés. Permite acceso rápido a la residencia permanente (1–3 años frente a los 10 habituales)."),
    ("For IT, engineering and scientific professionals. Requires job offer from Japanese employer. 1–5 year renewable permit.",
     "Para profesionales de TI, ingeniería y ciencias. Requiere oferta de trabajo de un empleador japonés. Permiso renovable de 1 a 5 años."),
    ("For specified industries (hospitality, food service, care, construction). No degree required. Up to 5 years.",
     "Para industrias específicas (hostelería, restauración, cuidados, construcción). No se requiere título universitario. Hasta 5 años."),
    ("For spouses and dependent children of work visa holders or permanent residents. Allows certain types of employment.",
     "Para cónyuges e hijos dependientes de titulares de visado de trabajo o residentes permanentes. Permite ciertos tipos de empleo."),
    ("After 10 years continuous residence (or 1–3 years on HSP visa). No work restrictions. Highly desirable.",
     "Tras 10 años de residencia continua (o 1–3 años con visa HSP). Sin restricciones laborales. Muy deseable."),

    # =========================================================
    # JAPAN STEP-BY-STEP
    # =========================================================
    ("Secure a job offer from a Japanese employer OR qualify for the Digital Nomad Visa",
     "Consiga una oferta de trabajo de un empleador japonés O califique para la Visa de Nómada Digital"),
    ("Employer applies for Certificate of Eligibility (CoE) from the Japan Immigration Servicios Agency",
     "El empleador solicita el Certificado de Elegibilidad (CoE) a la Agencia de Servicios de Inmigración de Japón"),
    ("Apply for the visa at the Japanese embassy in your country using the CoE",
     "Solicite el visado en la embajada japonesa de su país usando el CoE"),
    ("Arrive en Japón and register at your ward/municipal office within 14 days",
     "Llegue a Japón y regístrese en su oficina municipal en un plazo de 14 días"),
    ("Obtain your Residence Card (在留カード) at the airport or municipal office",
     "Obtenga su Tarjeta de Residencia (在留カード) en el aeropuerto u oficina municipal"),
    ("Enrol in National Seguro de Salud (国民健康保険) at the municipal office",
     "Inscríbase en el Seguro Nacional de Salud (国民健康保険) en la oficina municipal"),
    ("Obtain a My Number Card (マイナンバーカード) — Japan's national ID",
     "Obtenga una Tarjeta My Number (マイナンバーカード), el documento de identidad nacional de Japón"),
    ("Open a bank account (requires Residence Card)", "Abra una cuenta bancaria (requiere Tarjeta de Residencia)"),
    ("The My Number Card has become increasingly important en Japón — it's needed for taxes, bank accounts, health insurance and government services. Apply for it at your local ward office as soon as possible.",
     "La Tarjeta My Number se ha vuelto cada vez más importante en Japón: es necesaria para impuestos, cuentas bancarias, seguro de salud y servicios gubernamentales. Solicítela en su oficina municipal lo antes posible."),

    # =========================================================
    # JAPAN HEALTHCARE
    # =========================================================
    ("Japan has a universal health insurance system. All residents (including foreigners with a Residence Card) must enrol in either National Seguro de Salud (国民健康保険, Kokumin Kenkou Hoken) for self-employed/unemployed, or company health insurance (社会保険) for employees. Patients pay 30% of medical costs; the insurance covers 70%.",
     "Japón tiene un sistema de seguro de salud universal. Todos los residentes (incluidos extranjeros con Tarjeta de Residencia) deben inscribirse en el Seguro Nacional de Salud (国民健康保険, Kokumin Kenkou Hoken) para autónomos/desempleados, o en el seguro médico empresarial (社会保険) para empleados. Los pacientes pagan el 30% de los costes médicos; el seguro cubre el 70%."),
    ("Japan's public hospitals are excellent — among the best in the world. Private clinics are common for routine care. International clinics in Tokyo (JICA, St. Luke's International, Tokyo Midtown Medical Center) offer English-language services.",
     "Los hospitales públicos de Japón son excelentes, entre los mejores del mundo. Las clínicas privadas son habituales para la atención rutinaria. Las clínicas internacionales en Tokio (JICA, St. Luke's International, Tokyo Midtown Medical Center) ofrecen servicios en inglés."),
    ("NHI monthly premium (employee, 30%)", "Prima mensual del NHI (empleado, 30%)"),
    ("Hospitalisation (30% co-pay, per day)", "Hospitalización (copago 30%, por día)"),
    ("Dental (partial coverage)", "Dental (cobertura parcial)"),
    ("Prescription medicines (30% co-pay)", "Medicamentos recetados (copago 30%)"),
    ("Enrol in the public health insurance system immediately upon registering your residence — it is mandatory and provides excellent value. You will also need a high-limit cost cap — Japan's system caps out-of-pocket costs at ¥80,100/month for average earners.",
     "Inscríbase en el sistema público de seguro de salud inmediatamente al registrar su residencia: es obligatorio y ofrece una excelente relación calidad-precio. También necesitará un límite de gasto máximo: el sistema japonés limita los gastos de bolsillo a ¥80.100/mes para ingresos medios."),

    # =========================================================
    # JAPAN INSURANCE
    # =========================================================
    ("Because Japan's National Seguro de Salud already covers 70% of medical costs, supplementary insurance is less critical than in other countries. However, international health insurance is useful for the period before NHI enrolment, for English-language hospitals, and for coverage during international travel.",
     "Dado que el Seguro Nacional de Salud de Japón ya cubre el 70% de los costes médicos, el seguro complementario es menos crítico que en otros países. Sin embargo, el seguro de salud internacional es útil durante el período previo a la inscripción en el NHI, para hospitales en inglés y para cobertura en viajes internacionales."),
    ("Japan's largest private insurer. Cancer and hospitalisation riders. For Japanese-speakers primarily.",
     "La mayor aseguradora privada de Japón. Complementos de cáncer y hospitalización. Principalmente para personas que hablan japonés."),
    ("Popular cancer and medical indemnity plans. Useful as a supplement to NHI. English support available.",
     "Populares planes de indemnización por cáncer y atención médica. Útil como complemento del NHI. Soporte en inglés disponible."),
    ("International plans for expats. Good English support. From ~¥15,000/month.",
     "Planes internacionales para expatriados. Buen soporte en inglés. Desde ~¥15.000/mes."),
    ("International plan for pre-arrival period and for coverage outside Japan. From ~$100/month.",
     "Plan internacional para el período previo a la llegada y para cobertura fuera de Japón. Desde ~100 $/mes."),
    ("Good for expats who travel frequently. Worldwide coverage including Japan. From ~$120/month.",
     "Ideal para expatriados que viajan con frecuencia. Cobertura mundial incluida Japón. Desde ~120 $/mes."),
    ("For most working expats en Japón, the mandatory NHI or company health insurance + a supplementary cancer/hospitalisation plan from a local insurer like Aflac is the most cost-effective setup.",
     "Para la mayoría de los expatriados que trabajan en Japón, el NHI obligatorio o el seguro médico de empresa + un plan complementario de cáncer/hospitalización de una aseguradora local como Aflac es la configuración más rentable."),

    # =========================================================
    # JAPAN BANK ACCOUNT
    # =========================================================
    ("A Japanese bank account is essential for receiving salary, paying rent, utilities and taxes. It has historically been difficult for new arrivals, but the process has improved significantly.",
     "Una cuenta bancaria japonesa es esencial para recibir el salario, pagar el alquiler, los servicios y los impuestos. Históricamente ha sido difícil para los recién llegados, pero el proceso ha mejorado significativamente."),
    ("Easiest bank to open for foreigners. Accepts residence cards from 6 months after arrival. No minimum balance. Largest ATM network en Japón.",
     "El banco más fácil de abrir para extranjeros. Acepta tarjetas de residencia a partir de 6 meses después de la llegada. Sin saldo mínimo. La red de cajeros automáticos más grande de Japón."),
    ("Largest megabank. Good international wire capabilities. English online banking available.",
     "El mayor megabanco. Buenas capacidades de transferencia internacional. Banca en línea en inglés disponible."),
    ("Online bank with the best FX rates en Japón. Excellent English interface. Requires Residence Card. Popular with expats.",
     "Banco en línea con las mejores tasas de cambio en Japón. Excelente interfaz en inglés. Requiere Tarjeta de Residencia. Popular entre expatriados."),
    ("English-language internet banking. No ATM fees at 7-Eleven. Good for international transfers.",
     "Banca por internet en inglés. Sin comisiones en cajeros de 7-Eleven. Ideal para transferencias internacionales."),
    ("Not a full bank but widely used by expats for international transfers and multi-currency transactions.",
     "No es un banco completo, pero es muy utilizado por expatriados para transferencias internacionales y transacciones multidivisa."),
    ("Residence Card (在留カード) — mandatory", "Tarjeta de Residencia (在留カード) — obligatoria"),
    ("My Number Card or My Number notification slip", "Tarjeta My Number o resguardo de notificación My Number"),
    ("Japanese phone number or smartphone", "Número de teléfono japonés o smartphone"),
    ("Some banks require 6 months of residence before opening", "Algunos bancos requieren 6 meses de residencia antes de abrir la cuenta"),
    ("Register your address at the ward office and obtain your Residence Card",
     "Registre su domicilio en la oficina municipal y obtenga su Tarjeta de Residencia"),
    ("Obtain My Number Card (apply at ward office, takes ~1 month)",
     "Obtenga la Tarjeta My Number (solicite en la oficina municipal, tarda ~1 mes)"),
    ("Visit Japan Post Bank or apply online at Sony Bank / Shinsei",
     "Visite Japan Post Bank o solicite en línea en Sony Bank / Shinsei"),
    ("Present Residence Card and My Number", "Presente la Tarjeta de Residencia y el My Number"),
    ("Receive bankbook and/or debit card within 1–2 weeks",
     "Reciba la libreta bancaria y/o tarjeta de débito en 1–2 semanas"),
    ("Japan Post Bank is the easiest to open immediately. Sony Bank has the best FX rates and English interface — open it once you've been resident for a few months.",
     "Japan Post Bank es el más fácil de abrir de inmediato. Sony Bank tiene las mejores tasas de cambio e interfaz en inglés: ábralo una vez que lleve unos meses como residente."),

    # =========================================================
    # JAPAN REAL ESTATE
    # =========================================================
    ("Japan has no restrictions on foreigners buying property — freehold ownership is fully permitted. Japan is unique in that properties (especially houses) can depreciate significantly over time, while land values are more stable. Prices outside Tokyo and major cities are remarkably low.",
     "Japón no tiene restricciones para que los extranjeros compren propiedades: la propiedad plena está totalmente permitida. Japón es único en que las propiedades (especialmente las casas) pueden depreciarse significativamente con el tiempo, mientras que los valores del terreno son más estables. Los precios fuera de Tokio y las grandes ciudades son notablemente bajos."),
    ("Full freehold ownership. Most expats buy condos in Tokyo, Osaka or Kyoto. Popular in international communities.",
     "Propiedad plena en régimen de propiedad absoluta. La mayoría de los expatriados compran apartamentos en Tokio, Osaka o Kioto. Popular en comunidades internacionales."),
    ("Full ownership of land and structure. Houses depreciate to near-zero after 20–30 years en Japón — land is the main value.",
     "Propiedad plena de terreno y estructura. Las casas se deprecian a casi cero después de 20–30 años en Japón: el terreno es el principal valor."),
    ("Vacant properties in rural areas, sometimes available for ¥1 (~$0.01) or very low prices. Renovation costs can be high.",
     "Propiedades vacantes en zonas rurales, a veces disponibles por ¥1 (~0,01 $) o precios muy bajos. Los costes de reforma pueden ser elevados."),
    ("Obtain a long-term residence visa (tourist visa insufficient for mortgage)",
     "Obtenga un visado de residencia de larga duración (el visado de turista es insuficiente para hipoteca)"),
    ("Hire a licensed real estate agent (宅地建物取引業者) — usually no buyer fee",
     "Contrate un agente inmobiliario con licencia (宅地建物取引業者): normalmente sin comisión para el comprador"),
    ("Identify properties via SUUMO, AtHome or an expat-specialist agency",
     "Identifique propiedades a través de SUUMO, AtHome o una agencia especializada en expatriados"),
    ("Make an offer and receive the Property Information Document (重要事項説明書)",
     "Haga una oferta y reciba el Documento de Información de la Propiedad (重要事項説明書)"),
    ("Sign the Purchase Agreement (売買契約書) — pay 10% deposit",
     "Firme el Contrato de Compraventa (売買契約書): pague el 10% de depósito"),
    ("Arrange mortgage (if applicable) or wire full payment",
     "Gestione la hipoteca (si procede) o realice el pago completo por transferencia"),
    ("Transfer at the notary / legal scrivener (司法書士) — title registered in land registry",
     "Transferencia ante notario / letrado judicial (司法書士): título registrado en el registro de la propiedad"),
    ("Real estate agent fee", "Comisión del agente inmobiliario"),
    ("3% + ¥60,000 + tax (paid by buyer and seller)", "3% + ¥60.000 + impuestos (pagado por comprador y vendedor)"),
    ("Registration and license tax", "Impuesto de registro y licencia"),
    ("0.1–2% of assessed value", "0,1–2% del valor tasado"),
    ("Property acquisition tax", "Impuesto de adquisición de propiedad"),
    ("3–4% of assessed value (one-time, 3–6 months after purchase)",
     "3–4% del valor tasado (único, 3–6 meses después de la compra)"),
    ("Judicial scrivener (registration)", "Letrado judicial (registro)"),
    ("Annual fixed asset tax", "Impuesto anual sobre activos fijos"),
    ("1.4% of assessed value (about 70% of market value)",
     "1,4% del valor tasado (aproximadamente el 70% del valor de mercado)"),
    ("Building inspection", "Inspección del edificio"),
    ("¥50,000–100,000 recommended", "¥50.000–100.000 recomendado"),
    ("In rural Japan, you can buy a fully habitable house for ¥2,000,000–5,000,000 (~$13,000–33,000). The Akiya Banks (空き家バンク) run by municipalities list vacant properties. The main cost is renovation, not purchase.",
     "En el Japón rural, puede comprar una casa totalmente habitable por ¥2.000.000–5.000.000 (~13.000–33.000 $). Los Akiya Banks (空き家バンク) gestionados por los municipios listan las propiedades vacantes. El principal coste es la reforma, no la compra."),

    # =========================================================
    # VIETNAM VISA TABLE
    # =========================================================
    ("Available online for citizens of 80+ countries. Single or multiple entry. Maximum 90 days, not renewable without leaving. Costo: $25.",
     "Disponible en línea para ciudadanos de más de 80 países. Entrada única o múltiple. Máximo 90 días, no renovable sin salir del país. Costo: 25 $."),
    ("For longer stays. Requires a sponsor (employer, Vietnamese spouse or an approved organisation). 1–2 year TRC, renewable. No specific income threshold.",
     "Para estancias más largas. Requiere un patrocinador (empleador, cónyuge vietnamita u organización aprobada). TRC de 1–2 años, renovable. Sin umbral de ingresos específico."),
    ("For business activities. 3–12 months, multiple entry. Requires invitation from a Vietnamese company.",
     "Para actividades empresariales. 3–12 meses, entrada múltiple. Requiere invitación de una empresa vietnamita."),
    ("Foreigners who invest in or direct a Vietnamese company can obtain a TRC through the company. Minimum investment ~$130,000.",
     "Los extranjeros que inviertan o dirijan una empresa vietnamita pueden obtener un TRC a través de la empresa. Inversión mínima ~130.000 $."),
    ("Vietnam has no formal retirement visa. Most long-term expats use repeated e-visas, business visas or obtain a TRC through employment/marriage.",
     "Vietnam no tiene visa de jubilación formal. La mayoría de los expatriados a largo plazo utilizan e-visas repetidas, visas de negocios u obtienen un TRC a través de empleo/matrimonio."),

    # =========================================================
    # VIETNAM STEP-BY-STEP
    # =========================================================
    ("Apply for an e-visa online at the official Vietnam Immigration Portal (evisa.xuatnhapcanh.gov.vn)",
     "Solicite una e-visa en línea en el Portal Oficial de Inmigración de Vietnam (evisa.xuatnhapcanh.gov.vn)"),
    ("Upon arrival, register your stay at the local police station or your accommodation does it",
     "A su llegada, registre su estancia en la comisaría local o su alojamiento lo hará automáticamente"),
    ("For long-term stay: find a sponsor (employer, school or Vietnamese partner)",
     "Para estancias largas: busque un patrocinador (empleador, escuela o socio vietnamita)"),
    ("Apply for a Temporary Residence Card (TRC) at the Immigration Department",
     "Solicite una Tarjeta de Residencia Temporal (TRC) en el Departamento de Inmigración"),
    ("Obtain a tax code at the local Tax Department if working",
     "Obtenga un código fiscal en el Departamento de Hacienda local si trabaja"),
    ("As of 2023, Vietnam e-visas allow 90 days multiple entry for most nationalities. This is sufficient for many long-term nomads who do a short trip to a neighbouring country every 3 months.",
     "Desde 2023, las e-visas de Vietnam permiten 90 días de entrada múltiple para la mayoría de nacionalidades. Esto es suficiente para muchos nómadas a largo plazo que hacen un viaje corto a un país vecino cada 3 meses."),

    # =========================================================
    # VIETNAM HEALTHCARE
    # =========================================================
    ("Public hospitals en Vietnam are overcrowded and language-challenged. Expats generally avoid them for all but emergencies. Foreigners registered with a Vietnamese employer can access the public health insurance system (BHYT).",
     "Los hospitales públicos en Vietnam están superpoblados y tienen barreras idiomáticas. Los expatriados generalmente los evitan excepto en emergencias. Los extranjeros registrados con un empleador vietnamita pueden acceder al sistema público de seguro de salud (BHYT)."),
    ("International private hospitals serve the expat community well in Hanoi and HCMC: Family Medical Practice, Vinmec International, Columbia Asia, FV Hospital (HCMC). Quality is good; costs are moderate.",
     "Los hospitales privados internacionales sirven bien a la comunidad expatriada en Hanói y Ciudad Ho Chi Minh: Family Medical Practice, Vinmec International, Columbia Asia, FV Hospital (HCMC). La calidad es buena; los costes son moderados."),
    ("Consulta médico general (private expat clinic)", "Consulta médico general (clínica privada para expatriados)"),
    ("Emergency room", "Urgencias"),
    ("Hospitalisation (international hospital, per night)", "Hospitalización (hospital internacional, por noche)"),
    ("Very cheap — 30–80% cheaper than Western prices", "Muy baratos: entre un 30 y un 80% más baratos que los precios occidentales"),
    ("Always use international hospitals if available. While local hospitals handle emergencies, language barriers and differing standards make private care preferable for expats.",
     "Utilice siempre hospitales internacionales si están disponibles. Aunque los hospitales locales atienden urgencias, las barreras idiomáticas y los diferentes estándares hacen preferible la atención privada para los expatriados."),

    # =========================================================
    # VIETNAM INSURANCE
    # =========================================================
    ("Health insurance is not legally required for most expat visa categories en Vietnam, but it is essential. Medical evacuation from Vietnam to Singapore or Thailand for serious cases can cost $20,000–50,000 without coverage.",
     "El seguro de salud no es legalmente obligatorio para la mayoría de las categorías de visado para expatriados en Vietnam, pero es esencial. La evacuación médica de Vietnam a Singapur o Tailandia para casos graves puede costar entre 20.000 y 50.000 $ sin cobertura."),
    ("Vietnam's largest insurer. Affordable local plans from ~$400/year. Limited English support.",
     "La mayor aseguradora de Vietnam. Planes locales asequibles desde ~400 $/año. Soporte en inglés limitado."),
    ("Popular among locally employed expats. From ~$500/year.",
     "Popular entre los expatriados con empleo local. Desde ~500 $/año."),
    ("International plan, widely accepted at expat clinics. From ~$1,000/year.",
     "Plan internacional, ampliamente aceptado en clínicas para expatriados. Desde ~1.000 $/año."),
    ("Comprehensive worldwide coverage. Good for frequent travellers. From ~$1,200/year.",
     "Cobertura mundial completa. Ideal para viajeros frecuentes. Desde ~1.200 $/año."),
    ("Premium plan, includes medical evacuation and repatriation. From ~$1,500/year.",
     "Plan premium, incluye evacuación médica y repatriación. Desde ~1.500 $/año."),
    ("Make sure your plan explicitly covers medical evacuation and repatriation — these are the most expensive emergencies for expats en Vietnam and are often excluded from basic plans.",
     "Asegúrese de que su plan cubra explícitamente la evacuación médica y la repatriación: estas son las emergencias más costosas para los expatriados en Vietnam y a menudo están excluidas de los planes básicos."),

    # =========================================================
    # VIETNAM BANK ACCOUNT
    # =========================================================
    ("A Vietnamese bank account simplifies daily life — cheaper rent payments, utility bills, local transfers and receiving salary. The process has become easier for foreigners holding TRCs.",
     "Una cuenta bancaria vietnamita simplifica la vida cotidiana: pagos de alquiler más baratos, facturas de servicios, transferencias locales y recepción de salario. El proceso se ha simplificado para los extranjeros que tienen TRC."),

    # =========================================================
    # MALAYSIA VISA TABLE
    # =========================================================
    ("Long-term residence programme for foreigners. Requirements since 2021: minimum 3-month fixed deposit of MYR 1,000,000, monthly offshore income of MYR 40,000, Malaysian health insurance. 5-year renewable visa. 60 days/year minimum stay.",
     "Programa de residencia a largo plazo para extranjeros. Requisitos desde 2021: depósito fijo mínimo de 3 meses de MYR 1.000.000, ingresos mensuales en el extranjero de MYR 40.000, seguro médico malayo. Visa renovable de 5 años. Estancia mínima de 60 días/año."),
    ("For digital nomads earning USD 24,000+/year. 3–12 month pass, renewable. Single or family options available. Fast online application.",
     "Para nómadas digitales que ganen más de 24.000 USD/año. Pase de 3 a 12 meses, renovable. Opciones disponibles para individuales o familias. Solicitud en línea rápida."),
    ("For foreign workers employed by Malaysian companies. Issued for 1–3 years. Requires employment contract with minimum salary MYR 5.000/month.",
     "Para trabajadores extranjeros empleados por empresas malasias. Emitido por 1–3 años. Requiere contrato de trabajo con salario mínimo de MYR 5.000/mes."),
    ("For highly skilled professionals. 10-year multiple-entry pass. No sponsorship needed. Requires degree and job offer or self-employment.",
     "Para profesionales altamente cualificados. Pase de entrada múltiple de 10 años. No requiere patrocinio. Requiere título universitario y oferta de trabajo o autoempleo."),
    ("Short-term professional activities, up to 12 months. Sponsored by a Malaysian company.",
     "Actividades profesionales a corto plazo, hasta 12 meses. Patrocinado por una empresa malasia."),

    # =========================================================
    # MALAYSIA STEP-BY-STEP
    # =========================================================
    ("Determine visa category (MM2H for retirees, DE Rantau for nomads, Employment Pass for workers)",
     "Determine la categoría de visado (MM2H para jubilados, DE Rantau para nómadas, Permiso de Empleo para trabajadores)"),
    ("Prepare documents: passport, income proof, health certificate, police clearance",
     "Prepare los documentos: pasaporte, prueba de ingresos, certificado médico, certificado de antecedentes penales"),
    ("For MM2H: apply via an approved MM2H agent (mandatory)",
     "Para MM2H: solicite a través de un agente MM2H aprobado (obligatorio)"),
    ("For DE Rantau: apply online via mdec.com.my",
     "Para DE Rantau: solicite en línea a través de mdec.com.my"),
    ("For Employment Pass: employer applies on your behalf via EzXpat system",
     "Para el Permiso de Empleo: el empleador solicita en su nombre a través del sistema EzXpat"),
    ("Upon approval, enter Malaysia and activate the visa",
     "Tras la aprobación, entre en Malasia y active el visado"),
    ("Register with LHDN (tax authority) if earning Malaysian-source income",
     "Regístrese en la LHDN (autoridad fiscal) si obtiene ingresos de fuente malasia"),
    ("The new MM2H requirements (2021) are significantly stricter than before. The DE Rantau Nomad Pass at USD 24,000/year is a much more accessible option for remote workers and is processed within 2–4 weeks.",
     "Los nuevos requisitos MM2H (2021) son significativamente más estrictos que antes. El Pase Nómada DE Rantau a 24.000 USD/año es una opción mucho más accesible para los teletrabajadores y se tramita en 2–4 semanas."),

    # =========================================================
    # MALAYSIA HEALTHCARE
    # =========================================================
    ("Malaysia has an excellent public healthcare system. Government hospitals charge a nominal fee for foreigners (RM 10–50 per consultation) but waiting times can be long. Non-residents pay more.  Emergency treatment is available to all.",
     "Malasia tiene un excelente sistema de salud público. Los hospitales del gobierno cobran una tarifa nominal a los extranjeros (RM 10–50 por consulta), pero los tiempos de espera pueden ser largos. Los no residentes pagan más. El tratamiento de urgencias está disponible para todos."),
    ("Private hospitals en Malasia are among the best in Southeast Asia and significantly cheaper than Singapore equivalents. KPJ Salud, Pantai Hospitals, Sunway Medical Centre and Prince Court (KL) are highly rated.",
     "Los hospitales privados en Malasia están entre los mejores del Sudeste Asiático y son considerablemente más baratos que los equivalentes de Singapur. KPJ Salud, Pantai Hospitals, Sunway Medical Centre y Prince Court (KL) tienen muy buena valoración."),
    ("Private Consulta médico general", "Consulta médico general (privada)"),
    ("Private specialist", "Especialista privado"),
    ("Emergency (private)", "Urgencias (privado)"),
    ("Hospitalisation (private, per night)", "Hospitalización (privado, por noche)"),
    ("MM2H requires proof of Malaysian health insurance. Even without this requirement, private health insurance is strongly recommended for expats due to the high cost of hospitalisation at private hospitals.",
     "MM2H requiere prueba de seguro médico malasio. Incluso sin este requisito, se recomienda encarecidamente el seguro médico privado para los expatriados debido al alto coste de la hospitalización en hospitales privados."),

    # =========================================================
    # MALAYSIA INSURANCE
    # =========================================================
    ("MM2H requires Malaysian health insurance coverage. Beyond the visa requirement, private insurance is strongly recommended to cover hospitalisation, specialist care and medical evacuation.",
     "MM2H requiere cobertura de seguro médico malasio. Más allá del requisito del visado, se recomienda encarecidamente el seguro privado para cubrir hospitalización, atención especializada y evacuación médica."),
    ("Malaysia's largest life insurer. Comprehensive health riders available. From ~RM 200/month.",
     "La mayor aseguradora de vida de Malasia. Complementos de salud completos disponibles. Desde ~RM 200/mes."),
    ("Strong private hospital network. Cobertura internacional option available. From ~RM 180/month.",
     "Sólida red de hospitales privados. Opción de cobertura internacional disponible. Desde ~RM 180/mes."),
    ("Good range of health plans. Widely accepted at private hospitals. From ~RM 190/month.",
     "Buena gama de planes de salud. Ampliamente aceptado en hospitales privados. Desde ~RM 190/mes."),
    ("International plan accepted for MM2H. Good for those who split time between countries. From ~$100/month.",
     "Plan internacional aceptado para MM2H. Ideal para quienes reparten su tiempo entre países. Desde ~100 $/mes."),
    ("Specialist expat insurer. Good value for SE Asia-based expats. From ~RM 150/month.",
     "Aseguradora especialista para expatriados. Buena relación calidad-precio para expatriados en el Sudeste Asiático. Desde ~RM 150/mes."),
    ("For MM2H specifically, the insurance must be issued by a Malaysian-licensed insurer and must be valid for the full duration of your stay. Great Eastern and AIA are the most commonly approved.",
     "Específicamente para MM2H, el seguro debe ser emitido por una aseguradora con licencia malasia y debe ser válido durante toda la duración de su estancia. Great Eastern y AIA son las más comúnmente aprobadas."),

    # =========================================================
    # CAMBODIA - VARIOUS
    # =========================================================
    ("Available online at evisa.gov.kh. 30 days, single entry, extendable once for 30 days. Costo: $30 + $6 processing fee.",
     "Disponible en línea en evisa.gov.kh. 30 días, entrada única, prorrogable una vez por 30 días. Costo: 30 $ + 6 $ de tasa de tramitación."),
    ("Available on arrival or online. 30 days, can be extended multiple times. The 'E' visa is the basis for most long-term stays. Extensions: 1 month, 3 months, 6 months, 1 year (multiple entry possible on 1-year extension).",
     "Disponible a la llegada o en línea. 30 días, puede prorrogarse múltiples veces. El visado 'E' es la base para la mayoría de las estancias largas. Prórrogas: 1 mes, 3 meses, 6 meses, 1 año (entrada múltiple posible con prórroga de 1 año)."),
    ("For those conducting business. Extendable for 1 year multiple entry. Popular with expat business owners and remote workers.",
     "Para quienes realizan actividades empresariales. Prorrogable por 1 año con entrada múltiple. Popular entre propietarios de empresas expatriados y teletrabajadores."),
    ("No specific retirement visa, but those 55+ can apply for a 1-year 'retirement' extension of their ordinary visa. Requires proof of $1,500/month income or $50,000 in bank.",
     "No existe visado de jubilación específico, pero los mayores de 55 años pueden solicitar una prórroga de 'jubilación' de 1 año de su visado ordinario. Requiere prueba de ingresos de 1.500 $/mes o 50.000 $ en el banco."),
    ("Specific category for foreign family members of Cambodian nationals.",
     "Categoría específica para familiares extranjeros de ciudadanos camboyanos."),
    ("Apply for E-Visa online before travel OR obtain visa on arrival at Phnom Penh / Siem Reap airports",
     "Solicite la E-Visa en línea antes del viaje O obtenga el visado a la llegada en los aeropuertos de Phnom Penh / Siem Reap"),
    ("For long-term stay: extend your E-class visa at an immigration agent or the Department of Immigration",
     "Para estancias largas: amplíe su visado de clase E en un agente de inmigración o en el Departamento de Inmigración"),
    ("Most expats use an immigration agent (~$200–350/year for 1-year multiple-entry EB extension)",
     "La mayoría de los expatriados utilizan un agente de inmigración (~200–350 $/año para prórroga EB de entrada múltiple de 1 año)"),
    ("Register your address at the local sangkat (commune) office",
     "Registre su domicilio en la oficina del sangkat local (comuna)"),
    ("Obtain a Tax Identification Number (TIN) at the General Department of Taxation if working",
     "Obtenga un Número de Identificación Fiscal (NIF) en el Departamento General de Tributación si trabaja"),
    ("Cambodia's visa system is very foreigner-friendly. A 1-year multiple-entry business extension (~$300 via an agent) is the de facto 'digital nomad visa'. No minimum stay requirement, no income proof needed at most immigration offices.",
     "El sistema de visados de Camboya es muy favorable para los extranjeros. Una prórroga de negocios de 1 año con entrada múltiple (~300 $ a través de un agente) es la 'visa de nómada digital' de facto. Sin requisito de estancia mínima, sin prueba de ingresos necesaria en la mayoría de las oficinas de inmigración."),
    ("Cambodia's public healthcare system is very limited. Most public hospitals lack basic equipment and medicines. Expats should use private hospitals for all care beyond minor issues.",
     "El sistema de salud público de Camboya es muy limitado. La mayoría de los hospitales públicos carecen de equipamiento básico y medicamentos. Los expatriados deben utilizar hospitales privados para toda atención más allá de problemas menores."),
    ("Private hospitals in Phnom Penh (Royal Rattanak Hospital, Sen Sok International University Hospital, Naga Clinic, Sunrise Japan Hospital) provide adequate to good care. Siem Reap has Royal Angkor International Hospital. For serious conditions, Bangkok is the standard evacuation destination (~1 hour by plane).",
     "Los hospitales privados de Phnom Penh (Royal Rattanak Hospital, Sen Sok International University Hospital, Naga Clinic, Sunrise Japan Hospital) ofrecen una atención adecuada a buena. Siem Reap cuenta con el Royal Angkor International Hospital. Para condiciones graves, Bangkok es el destino de evacuación estándar (~1 hora en avión)."),
    ("As with Laos, medical evacuation insurance is essential en Camboya. For anything beyond routine care, Bangkok's Bumrungrad or Samitivej hospitals are the standard destination.",
     "Al igual que en Laos, el seguro de evacuación médica es esencial en Camboya. Para cualquier cosa más allá de la atención rutinaria, los hospitales Bumrungrad o Samitivej de Bangkok son el destino estándar."),
    ("International health insurance is not required for any visa category en Camboya but is essential for safety. The combination of limited local facilities and proximity to excellent Thai hospitals makes evacuation coverage critical.",
     "El seguro de salud internacional no es obligatorio para ninguna categoría de visado en Camboya, pero es esencial por seguridad. La combinación de instalaciones locales limitadas y la proximidad a excelentes hospitales tailandeses hace que la cobertura de evacuación sea fundamental."),
    ("Local expat-focused insurer. Good network of Phnom Penh private hospitals. From ~$600/year.",
     "Aseguradora local especializada en expatriados. Buena red de hospitales privados de Phnom Penh. Desde ~600 $/año."),
    ("Strong medical evacuation and Thailand coverage. From ~$1,500/year.",
     "Sólida cobertura de evacuación médica y Tailandia. Desde ~1.500 $/año."),
    ("International plan with broad coverage. Good for frequent travellers. From ~$1,000/year.",
     "Plan internacional con amplia cobertura. Ideal para viajeros frecuentes. Desde ~1.000 $/año."),
    ("Comprehensive worldwide plan with repatriation. From ~$1,200/year.",
     "Plan mundial completo con repatriación. Desde ~1.200 $/año."),
    ("Budget nomad insurance. Covers evacuation. Popular in the expat community. From ~$45/month.",
     "Seguro económico para nómadas. Cubre evacuación. Popular en la comunidad expatriada. Desde ~45 $/mes."),
    ("Ensure your plan explicitly covers medical evacuation to Thailand. Pacific Cross Cambodia is a good local option and is widely accepted at Phnom Penh's private hospitals.",
     "Asegúrese de que su plan cubra explícitamente la evacuación médica a Tailandia. Pacific Cross Cambodia es una buena opción local y está ampliamente aceptada en los hospitales privados de Phnom Penh."),
    ("Cambodia's fully dollarised economy makes banking straightforward — USD accounts are the norm. Account opening is relatively easy for foreigners, even on tourist visa at some banks.",
     "La economía totalmente dolarizada de Camboya simplifica la banca: las cuentas en USD son la norma. La apertura de cuenta es relativamente fácil para extranjeros, incluso con visado turístico en algunos bancos."),
    ("Cambodia's most popular bank among expats. Excellent English app, ABA PAY digital payments, easy account opening. Most recommended.",
     "El banco más popular de Camboya entre los expatriados. Excelente aplicación en inglés, pagos digitales ABA PAY, fácil apertura de cuenta. El más recomendado."),
    ("Good for business accounts and larger transactions. English service available.",
     "Ideal para cuentas empresariales y transacciones de mayor cuantía. Servicio en inglés disponible."),
    ("Banco más grande by branches. Good for transfers withen Camboya and to Vietnam/Laos.",
     "El banco más grande por número de sucursales. Ideal para transferencias dentro de Camboya y a Vietnam/Laos."),
    ("State bank. Good for USD transfers. Strong relationship with Chinese banks.",
     "Banco estatal. Ideal para transferencias en USD. Sólida relación con bancos chinos."),
    ("Mobile money service (not a full bank) used for daily transactions. Very popular.",
     "Servicio de dinero móvil (no es un banco completo) utilizado para transacciones diarias. Muy popular."),
    ("Cambodian visa (tourist may be accepted at ABA Bank)",
     "Visado camboyano (el turístico puede aceptarse en ABA Bank)"),
    ("Comprobante de domicilio (guesthouse or rental contract)",
     "Comprobante de domicilio (hostal o contrato de alquiler)"),
    ("Cambodian phone number (for app)", "Número de teléfono camboyano (para la app)"),
    ("Depósito inicial ($100–500 for most account types)",
     "Depósito inicial (100–500 $ para la mayoría de los tipos de cuenta)"),
    ("Visit ABA Bank branch in Phnom Penh or Siem Reap",
     "Visite una sucursal de ABA Bank en Phnom Penh o Siem Reap"),
    ("Present passport and visa", "Presente el pasaporte y el visado"),
    ("Complete account opening form", "Rellene el formulario de apertura de cuenta"),
    ("Account opened same day in most cases", "Cuenta abierta el mismo día en la mayoría de los casos"),
    ("Download ABA Mobile app — one of the best banking apps in Southeast Asia",
     "Descargue la app ABA Mobile: una de las mejores apps bancarias del Sudeste Asiático"),
    ("ABA Bank is the unanimous favourite among Phnom Penh expats — the app is excellent, account opening is fast (sometimes with just a tourist visa), and the service is in English. Open a USD account as the primary account for daily use.",
     "ABA Bank es el favorito unánime entre los expatriados de Phnom Penh: la app es excelente, la apertura de cuenta es rápida (a veces solo con visado turístico) y el servicio es en inglés. Abra una cuenta en USD como cuenta principal para uso diario."),
    ("Foreign ownership permitted from the 2nd floor upward in approved condominium buildings. Growing inventory in Phnom Penh. Sihanoukville and Siem Reap also have options.",
     "Propiedad extranjera permitida desde el segundo piso hacia arriba en edificios de condominios aprobados. Inventario creciente en Phnom Penh. Sihanoukville y Siem Reap también tienen opciones."),
    ("Land and houses can be leased for 50 years, renewable for another 50. Common for villas and townhouses.",
     "Los terrenos y casas pueden arrendarse por 50 años, renovables por otros 50. Habitual para villas y casas adosadas."),
    ("Many foreigners form a Cambodian company (with a Cambodian nominee director holding 51% of shares on paper). Legal but carries risk if done improperly.",
     "Muchos extranjeros constituyen una empresa camboyana (con un director nominal camboyano que tiene el 51% de las acciones en papel). Legal, pero conlleva riesgos si se hace incorrectamente."),
    ("Land held in a Cambodian spouse's name. Common but risky without legal protections.",
     "Terreno registrado a nombre de un cónyuge camboyano. Habitual pero arriesgado sin protecciones legales."),
    ("Hire a reputable Cambodian real estate lawyer",
     "Contrate un abogado inmobiliario camboyano de reputación"),
    ("Verify the title (LMAP Title — the most secure type; avoid Soft Title)",
     "Verifique el título (Título LMAP, el tipo más seguro; evite el Título Blando)"),
    ("For condos: check building is registered with MLMUPC as foreigner-eligible",
     "Para condominios: compruebe que el edificio esté registrado en el MLMUPC como apto para extranjeros"),
    ("Sign a Memorandum of Understanding (MOU) and pay deposit",
     "Firme un Memorando de Entendimiento (MOU) y pague el depósito"),
    ("Lawyer conducts due diligence: title, permits, developer reputation",
     "El abogado realiza la diligencia debida: título, permisos, reputación del promotor"),
    ("Sign the Sale and Purchase Agreement (SPA)", "Firme el Contrato de Compraventa (SPA)"),
    ("Transfer at the relevant authority and receive your ownership certificate",
     "Realice la transferencia ante la autoridad competente y reciba su certificado de propiedad"),
    ("Transfer tax (registration fee)", "Impuesto de transferencia (tasa de registro)"),
    ("4% of property value", "4% del valor de la propiedad"),
    ("0.1% of registered value", "0,1% del valor registrado"),
    ("Notarisation", "Notarización"),
    ("Annual property tax", "Impuesto anual sobre bienes inmuebles"),
    ("0.1% of assessed value above $25,000", "0,1% del valor tasado por encima de 25.000 $"),
    ("Annual rental income tax (if renting out)", "Impuesto anual sobre ingresos de alquiler (si alquila)"),
    ("14% withholding tax", "Retención del 14%"),
    ("Only buy condos en Camboya — they are the only truly secure form of foreign property ownership under Cambodian law. Leasehold villas and company-held land carry significant legal risk. In Phnom Penh, Boeung Keng Kang (BKK1) and Tonle Bassac are the most expat-friendly neighbourhoods.",
     "Solo compre condominios en Camboya: son la única forma verdaderamente segura de propiedad extranjera bajo la ley camboyana. Las villas en arrendamiento y los terrenos de empresa conllevan un riesgo legal significativo. En Phnom Penh, Boeung Keng Kang (BKK1) y Tonle Bassac son los barrios más amigables para expatriados."),

    # =========================================================
    # E-E-A-T / ABOUT THIS GUIDE
    # =========================================================
    ("This guide is researched and maintained by the editorial team at eVisa-Card.com. Última actualización : <strong>March 2026</strong>. We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Esta guía es investigada y mantenida por el equipo editorial de eVisa-Card.com. Última actualización: <strong>Marzo 2026</strong>. Nos esforzamos por mantener toda la información actualizada, pero las normas de visado, los costes sanitarios y la normativa inmobiliaria cambian con frecuencia. Verifique siempre los requisitos actuales con fuentes gubernamentales oficiales y consulte a un profesional autorizado antes de tomar decisiones importantes."),
    ("This guide is researched and maintained by the editorial team at eVisa-Card.com.",
     "Esta guía es investigada y mantenida por el equipo editorial de eVisa-Card.com."),
    ("We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Nos esforzamos por mantener toda la información actualizada, pero las normas de visado, los costes sanitarios y la normativa inmobiliaria cambian con frecuencia. Verifique siempre los requisitos actuales con fuentes gubernamentales oficiales y consulte a un profesional autorizado antes de tomar decisiones importantes."),
    ("Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Verifique siempre los requisitos actuales con fuentes gubernamentales oficiales y consulte a un profesional autorizado antes de tomar decisiones importantes."),

    # =========================================================
    # GENERIC PATTERNS (apply across all country guides)
    # =========================================================
    ("Valid passport", "Pasaporte válido"),
    ("Proof of address in Thailand (rental contract or TM.30 confirmation)",
     "Comprobante de domicilio en Tailandia (contrato de alquiler o confirmación TM.30)"),
    ("Comprobante de domicilio en Tailandia (rental contract or TM.30 confirmation)",
     "Comprobante de domicilio en Tailandia (contrato de alquiler o confirmación TM.30)"),
    ("Thai SIM card or phone number", "Tarjeta SIM o número de teléfono tailandés"),
    ("Depósito inicial (typically 500–2,000 THB)", "Depósito inicial (normalmente 500–2.000 THB)"),
    ("Non-Immigrant visa (tourist visa may be refused at some branches)",
     "Visa No Inmigrante (el visado turístico puede denegarse en algunas sucursales)"),
    ("GP consultation (private)", "Consulta médico general (privada)"),
    ("Specialist consultation", "Consulta especialista"),
    ("Emergency room visit", "Visita a urgencias"),
    ("Hospitalisation (per night)", "Hospitalización (por noche)"),
    ("Dental cleaning", "Limpieza dental"),
    ("Eye exam + glasses", "Examen de vista + gafas"),
    ("Prescription medicines", "Medicamentos recetados"),
    ("Transfer fee", "Tasa de transferencia"),
    ("Stamp duty or specific business tax", "Impuesto de timbre o impuesto comercial específico"),
    ("Withholding tax", "Retención fiscal"),
    ("Lawyer fees", "Honorarios de abogado"),
    ("Agent commission", "Comisión del agente"),
    ("Proof of address", "Comprobante de domicilio"),
    ("rental contract", "contrato de alquiler"),
    ("utility bill", "factura de servicios"),
    ("Initial deposit", "Depósito inicial"),
    ("Step-by-Step Process", "Proceso Paso a Paso"),
    ("Required Documents", "Documentos Requeridos"),
    ("Recommended Banks", "Bancos Recomendados"),
    ("Top Providers for Expats", "Mejores Aseguradoras para Expatriados"),
    ("Options for Foreigners", "Opciones para Extranjeros"),
    ("Purchase Process", "Proceso de Compra"),
    ("Typical Costs", "Costos Típicos"),

    # =========================================================
    # FOOTER / DATE / MISC
    # =========================================================
    ("Global eVisa & Travel Information Platform", "Plataforma Global de Información eVisa y Viajes"),
    ("Follow eVisa-Card.com", "Sigue eVisa-Card.com"),
    ("March 2026", "Marzo 2026"),
    ("Last updated: March 2026", "Última actualización: Marzo 2026"),
    ("Last updated: <strong>March 2026</strong>", "Última actualización: <strong>Marzo 2026</strong>"),
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

        for eng, spa in REPLACEMENTS:
            count = html.count(eng)
            if count > 0:
                html = html.replace(eng, spa)
                file_replacements += count

        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            files_updated += 1
            total_replacements += file_replacements
            print(f"  OK {fname}: {file_replacements} replacements")
        else:
            print(f"  -- {fname}: no changes")

    print(f"\nDone: {files_updated} files updated, {total_replacements} total replacements.")


if __name__ == "__main__":
    main()
