#!/usr/bin/env python3
"""
Spanish translations for the FAQ page (en/faq.html -> es/faq.html).
Contains all 7 category translations and all 47 Q&A pairs.
All internal links changed from /en/ to /es/.
"""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "Preguntas Generales sobre Visas",
    "Schengen & European Visas": "Visas Schengen y Europeas",
    "Documents & Application Process": "Documentos y Proceso de Solicitud",
    "Fees & Processing Times": "Tarifas y Tiempos de Procesamiento",
    "Extensions, Overstay & Refusal": "Extensiones, Estadia Excesiva y Rechazo",
    "Special Visa Types": "Tipos Especiales de Visa",
    "Embassy & Application Process": "Embajada y Proceso de Solicitud",
}

FAQ_TRANSLATIONS = [
    # =========================================================================
    # Category 1: General Visa Questions (7 questions)
    # =========================================================================
    {
        "category": "General Visa Questions",
        "q_en": "What is an eVisa?",
        "q_es": "¿Qué es una eVisa?",
        "a_es": 'Una eVisa (visa electrónica) es una autorización de viaje emitida digitalmente. Se solicita en línea, se paga la tarifa y se recibe la aprobación por correo electrónico. No es necesario visitar una embajada. Países como <a href="/es/visa-turkey.html">Turquía</a>, <a href="/es/visa-india.html">India</a>, <a href="/es/visa-vietnam.html">Vietnam</a>, <a href="/es/visa-cambodia.html">Camboya</a> y <a href="/es/visa-australia.html">Australia</a> ofrecen eVisas.',
    },
    {
        "category": "General Visa Questions",
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_es": "¿Cuál es la diferencia entre una visa y una eVisa?",
        "a_es": "Una visa tradicional requiere visitar una embajada o consulado, presentar documentos en papel y, en ocasiones, asistir a una entrevista. Una eVisa se solicita completamente en línea, se procesa más rápido (generalmente en 24-72 horas) y se envía electrónicamente a su correo electrónico.",
    },
    {
        "category": "General Visa Questions",
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_es": "¿Qué es una ETA (Autorización Electrónica de Viaje)?",
        "a_es": 'Una ETA es un control previo al viaje para ciudadanos de países exentos de visa. No es una visa, sino una autorización de viaje vinculada a su pasaporte. Países como <a href="/es/visa-australia.html">Australia</a>, Canadá, Nueva Zelanda y el Reino Unido utilizan sistemas ETA. El sistema ETIAS de la UE se lanza en 2026.',
    },
    {
        "category": "General Visa Questions",
        "q_en": "What is visa-free travel?",
        "q_es": "¿Qué es el viaje sin visa?",
        "a_es": "Viajar sin visa significa que puede ingresar a un país sin solicitar una visa con anticipación. Simplemente presenta su pasaporte en inmigración. La estancia permitida suele ser de 30 a 90 días. Los pasaportes más fuertes (Japón, Singapur, UE) ofrecen acceso sin visa a más de 190 países.",
    },
    {
        "category": "General Visa Questions",
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_es": "¿Qué es una visa a la llegada (VOA)?",
        "a_es": 'Una visa a la llegada se emite en el punto de entrada (aeropuerto o cruce fronterizo) sin solicitud previa. Presenta su pasaporte, completa un formulario, paga la tarifa y recibe el sello de visa. Países como <a href="/es/visa-indonesia.html">Indonesia</a>, <a href="/es/visa-nepal.html">Nepal</a> y <a href="/es/visa-jordan.html">Jordania</a> ofrecen VOA para muchas nacionalidades.',
    },
    {
        "category": "General Visa Questions",
        "q_en": "How do I check if I need a visa?",
        "q_es": "¿Cómo verifico si necesito una visa?",
        "a_es": 'Los requisitos de visa dependen de su nacionalidad y destino. Utilice nuestra <a href="../index.html">herramienta de búsqueda de visas</a> en la página principal o consulte la <a href="../destination.html">página del país</a> específico. En general, los ciudadanos de países con pasaportes fuertes (UE, EE. UU., Reino Unido, Japón) disfrutan de acceso sin visa a más de 150 países.',
    },
    {
        "category": "General Visa Questions",
        "q_en": "What is the strongest passport in the world?",
        "q_es": "¿Cuál es el pasaporte más fuerte del mundo?",
        "a_es": "En 2026, Japón, Singapur y varios pasaportes de la UE se clasifican constantemente como los más fuertes, ofreciendo acceso sin visa o con visa a la llegada a más de 190 países. El Índice de Pasaportes Henley y el índice Arton Capital clasifican los pasaportes trimestralmente según la libertad de viaje.",
    },
    # =========================================================================
    # Category 2: Schengen & European Visas (6 questions)
    # =========================================================================
    {
        "category": "Schengen & European Visas",
        "q_en": "What is a Schengen visa?",
        "q_es": "¿Qué es una visa Schengen?",
        "a_es": 'Una visa Schengen permite viajar a 27 países europeos con una sola visa. Es válida para estancias cortas de hasta 90 días en cualquier período de 180 días. Se solicita en la embajada del país que más visitará (o por el que entrará primero). Consulte nuestras páginas de visa de <a href="/es/visa-france.html">Francia</a>, <a href="/es/visa-germany.html">Alemania</a>, <a href="/es/visa-spain.html">España</a> e <a href="/es/visa-italy.html">Italia</a>.',
    },
    {
        "category": "Schengen & European Visas",
        "q_en": "How many countries are in the Schengen Area?",
        "q_es": "¿Cuántos países forman parte del Espacio Schengen?",
        "a_es": "En 2026, el Espacio Schengen incluye 27 países: Austria, Bélgica, Croacia, República Checa, Dinamarca, Estonia, Finlandia, Francia, Alemania, Grecia, Hungría, Islandia, Italia, Letonia, Liechtenstein, Lituania, Luxemburgo, Malta, Países Bajos, Noruega, Polonia, Portugal, Rumanía, Eslovaquia, Eslovenia, España, Suecia y Suiza.",
    },
    {
        "category": "Schengen & European Visas",
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_es": "¿Puedo visitar varios países Schengen con una sola visa?",
        "a_es": "Sí. Una visa Schengen permite la libre circulación por los 27 países Schengen durante su estancia autorizada (hasta 90 días en 180 días). Debe solicitar en la embajada de su destino principal o del país de primera entrada.",
    },
    {
        "category": "Schengen & European Visas",
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_es": "¿Qué es la regla 90/180 para Schengen?",
        "a_es": 'La regla 90/180 significa que puede permanecer en el Espacio Schengen un máximo de 90 días dentro de cualquier período de 180 días. Se calcula de forma continua. Una vez que haya utilizado 90 días, debe salir del Espacio Schengen y esperar hasta que suficientes días hayan "expirado" antes de volver a entrar.',
    },
    {
        "category": "Schengen & European Visas",
        "q_en": "What is ETIAS and when does it start?",
        "q_es": "¿Qué es ETIAS y cuándo comienza?",
        "a_es": "ETIAS (Sistema Europeo de Información y Autorización de Viajes) es una nueva autorización previa al viaje para viajeros exentos de visa que visitan el Espacio Schengen. Se lanza en 2026. Ciudadanos de más de 60 países (EE. UU., Reino Unido, Canadá, Australia, Japón) necesitarán la aprobación ETIAS (EUR 7, válida por 3 años) antes de viajar a Europa.",
    },
    {
        "category": "Schengen & European Visas",
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_es": "¿Puedo entrar a un país Schengen diferente al de mi visa?",
        "a_es": "Sí, pero su visa Schengen debe ser emitida por el país de su destino principal (estancia más larga). Si ingresa por un país diferente, inmigración puede cuestionar su itinerario. Si todas las estancias son iguales, solicite al país de primera entrada.",
    },
    # =========================================================================
    # Category 3: Documents & Application Process (9 questions)
    # =========================================================================
    {
        "category": "Documents & Application Process",
        "q_en": "What documents do I need for a visa application?",
        "q_es": "¿Qué documentos necesito para una solicitud de visa?",
        "a_es": 'Requisitos comunes: pasaporte válido (con más de 6 meses de vigencia), fotos de pasaporte, formulario de solicitud completo, itinerario de viaje, reserva de hotel, prueba de medios económicos (extractos bancarios), seguro de viaje y carta de invitación (si corresponde). Consulte nuestra <a href="/es/visa-documents-checklist.html">lista de documentos</a>.',
    },
    {
        "category": "Documents & Application Process",
        "q_en": "What size photo is needed for a visa?",
        "q_es": "¿Qué tamaño de foto se necesita para una visa?",
        "a_es": 'La mayoría de los países requieren fotos de 35x45 mm con fondo blanco. Estados Unidos requiere 51x51 mm (2x2 pulgadas). Las fotos deben ser recientes (de los últimos 6 meses), mostrar expresión neutra y cumplir requisitos específicos de iluminación. Consulte nuestra <a href="/es/visa-photo-requirements.html">guía de requisitos de foto para visa</a>.',
    },
    {
        "category": "Documents & Application Process",
        "q_en": "Do I need travel insurance for a visa?",
        "q_es": "¿Necesito un seguro de viaje para una visa?",
        "a_es": 'Sí, para visas Schengen debe tener un seguro de viaje con cobertura mínima de EUR 30.000. Muchos otros países también lo requieren o lo recomiendan encarecidamente. Consulte nuestra <a href="/es/travel-insurance-for-visa-applications.html">guía de seguros de viaje</a>.',
    },
    {
        "category": "Documents & Application Process",
        "q_en": "How long must my passport be valid for travel?",
        "q_es": "¿Cuánto tiempo debe ser válido mi pasaporte para viajar?",
        "a_es": "La mayoría de los países requieren que su pasaporte tenga al menos 6 meses de vigencia a partir de su estancia prevista. Los países Schengen exigen 3 meses de vigencia más allá de su fecha de salida, además de dos páginas en blanco. Verifique siempre los requisitos del país específico.",
    },
    {
        "category": "Documents & Application Process",
        "q_en": "What bank statement amount do I need for a visa?",
        "q_es": "¿Qué monto de extracto bancario necesito para una visa?",
        "a_es": "Para visas Schengen, demuestre EUR 50-100 por día de estancia. Para la visa B1/B2 de EE. UU., demuestre fondos suficientes (sin monto fijo). Para el Reino Unido, muestre 3-6 meses de ingresos constantes. En general, muestre un saldo bancario que cubra los costos del viaje más un 30-50% adicional.",
    },
    {
        "category": "Documents & Application Process",
        "q_en": "Is a hotel booking required for a visa application?",
        "q_es": "¿Se requiere una reserva de hotel para una solicitud de visa?",
        "a_es": "La mayoría de las solicitudes de visa requieren prueba de alojamiento para toda su estancia. Puede ser una reserva de hotel (no necesariamente prepagada), una reserva de Airbnb o una carta de su anfitrión. Para visas Schengen, todas las noches deben estar cubiertas.",
    },
    {
        "category": "Documents & Application Process",
        "q_en": "Do I need a return ticket to get a visa?",
        "q_es": "¿Necesito un boleto de regreso para obtener una visa?",
        "a_es": "La mayoría de los países exigen prueba de viaje de regreso o de continuación para las solicitudes de visa y en inmigración. Puede ser una reserva de vuelo confirmada, boleto de autobús o boleto de ferry que demuestre que planea salir antes de que expire su visa.",
    },
    {
        "category": "Documents & Application Process",
        "q_en": "What is an invitation letter for a visa?",
        "q_es": "¿Qué es una carta de invitación para una visa?",
        "a_es": "Una carta de invitación es un documento de una persona u organización en el país de destino que lo invita a visitar. Incluye los datos del anfitrión, su relación, el propósito y las fechas de la visita, los arreglos de alojamiento y la responsabilidad financiera. Es obligatoria para muchas solicitudes de visa Schengen y de negocios.",
    },
    {
        "category": "Documents & Application Process",
        "q_en": "What are biometrics for a visa?",
        "q_es": "¿Qué son los datos biométricos para una visa?",
        "a_es": "Los datos biométricos incluyen huellas dactilares y una fotografía digital recopilados durante su solicitud de visa. Los países Schengen, el Reino Unido, EE. UU., Canadá y muchos otros los exigen. Se almacenan para verificación de identidad y generalmente son válidos por 5 años.",
    },
    # =========================================================================
    # Category 4: Fees & Processing Times (6 questions)
    # =========================================================================
    {
        "category": "Fees & Processing Times",
        "q_en": "How much does a visa cost?",
        "q_es": "¿Cuánto cuesta una visa?",
        "a_es": 'Las tarifas de visa varían ampliamente. Ejemplos: visa Schengen EUR 80, visa B1/B2 de EE. UU. USD 185, eVisa de India USD 25-80, eVisa de Turquía USD 50, ETA de Australia AUD 20, eVisa de Camboya USD 36. Los niños y algunas nacionalidades pueden tener tarifas reducidas. Consulte nuestra página de <a href="/es/visa-processing-times.html">tiempos de procesamiento</a>.',
    },
    {
        "category": "Fees & Processing Times",
        "q_en": "How long does visa processing take?",
        "q_es": "¿Cuánto tiempo tarda el procesamiento de una visa?",
        "a_es": "Las eVisas suelen tardar 24-72 horas. Las visas Schengen tardan entre 15 y 45 días calendario. Las visas B1/B2 de EE. UU. pueden tardar semanas o meses según la embajada. Solicite siempre con suficiente antelación a su fecha de viaje.",
    },
    {
        "category": "Fees & Processing Times",
        "q_en": "How far in advance should I apply for a visa?",
        "q_es": "¿Con cuánta anticipación debo solicitar una visa?",
        "a_es": "Para eVisas: 1-2 semanas antes del viaje. Para visas Schengen: 3-6 meses de anticipación (como máximo 6 meses, mínimo 15 días antes de la salida). Para visas de EE. UU.: 3-6 meses o más por los largos tiempos de espera. Las temporadas altas pueden requerir solicitudes más tempranas.",
    },
    {
        "category": "Fees & Processing Times",
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_es": "¿Puedo obtener un reembolso si mi solicitud de visa es rechazada?",
        "a_es": "En la mayoría de los casos, las tarifas de visa no son reembolsables independientemente del resultado. La tarifa cubre el costo de procesamiento de su solicitud, no una garantía de aprobación.",
    },
    {
        "category": "Fees & Processing Times",
        "q_en": "How do I track my visa application status?",
        "q_es": "¿Cómo rastreo el estado de mi solicitud de visa?",
        "a_es": "La mayoría de las embajadas y oficinas de VFS Global ofrecen seguimiento en línea. Recibirá un número de referencia al presentar su solicitud. Ingrese este número en el sitio web de la embajada o de VFS. Algunos países también envían actualizaciones por correo electrónico o SMS en cada etapa del procesamiento.",
    },
    {
        "category": "Fees & Processing Times",
        "q_en": "What is VFS Global?",
        "q_es": "¿Qué es VFS Global?",
        "a_es": "VFS Global es una empresa privada que procesa solicitudes de visa en nombre de gobiernos. Operan centros de solicitud de visa (VAC) en todo el mundo. Usted presenta sus documentos en un centro VFS en lugar de directamente en la embajada. VFS cobra una tarifa de servicio adicional a la tarifa de visa.",
    },
    # =========================================================================
    # Category 5: Extensions, Overstay & Refusal (4 questions)
    # =========================================================================
    {
        "category": "Extensions, Overstay & Refusal",
        "q_en": "Can I extend my visa?",
        "q_es": "¿Puedo extender mi visa?",
        "a_es": 'Depende del país y tipo de visa. Algunos países permiten extensiones (por ejemplo, la VOA de Indonesia se puede extender 30 días, la visa de turista de Tailandia se puede extender 30 días). Las visas Schengen solo se pueden extender en circunstancias excepcionales. Consulte nuestra página de <a href="/es/visa-rejection-reasons.html">motivos de rechazo de visa</a> para información relacionada.',
    },
    {
        "category": "Extensions, Overstay & Refusal",
        "q_en": "What happens if my visa is refused?",
        "q_es": "¿Qué sucede si mi visa es rechazada?",
        "a_es": "Recibirá una notificación escrita con el motivo. Las razones comunes incluyen prueba financiera insuficiente, documentos incompletos o sospecha de intención migratoria. Generalmente puede apelar dentro de 1-3 meses o volver a solicitar con documentación mejorada.",
    },
    {
        "category": "Extensions, Overstay & Refusal",
        "q_en": "What is overstaying a visa?",
        "q_es": "¿Qué es exceder el tiempo de estadía de una visa?",
        "a_es": "Exceder la estadía significa permanecer más allá de su estancia autorizada. Las consecuencias incluyen multas (por ejemplo, Tailandia cobra 500 THB/día), deportación, detención, prohibiciones de entrada (1-10 años) y dificultades para obtener futuras visas. Respete siempre las fechas de vigencia de su visa.",
    },
    {
        "category": "Extensions, Overstay & Refusal",
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_es": "¿Qué sucede si pierdo mi pasaporte con una visa válida?",
        "a_es": "Contacte inmediatamente a la embajada más cercana de su país para obtener un documento de viaje de emergencia. Deberá solicitar una nueva visa, ya que las visas en pasaportes perdidos se consideran nulas. Presente una denuncia policial y conserve una copia para la nueva solicitud.",
    },
    # =========================================================================
    # Category 6: Special Visa Types (10 questions)
    # =========================================================================
    {
        "category": "Special Visa Types",
        "q_en": "What is a transit visa?",
        "q_es": "¿Qué es una visa de tránsito?",
        "a_es": "Una visa de tránsito le permite pasar por un país en camino a su destino final. Generalmente es válida por 24-72 horas. Algunos países requieren visa de tránsito incluso si no sale del aeropuerto.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "Can I work on a tourist visa?",
        "q_es": "¿Puedo trabajar con una visa de turista?",
        "a_es": "No. Las visas de turista generalmente no permiten empleo. Trabajar con una visa de turista es ilegal en la mayoría de los países y puede resultar en deportación, multas y denegaciones futuras de visa. Necesita una visa de trabajo o permiso de trabajo separado.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a digital nomad visa?",
        "q_es": "¿Qué es una visa para nómadas digitales?",
        "a_es": 'Una visa para nómadas digitales permite a los trabajadores remotos vivir en un país mientras trabajan para empleadores o clientes en el extranjero. Los países populares incluyen <a href="/es/visa-portugal.html">Portugal</a>, <a href="/es/visa-spain.html">España</a>, <a href="/es/visa-thailand.html">Tailandia</a>, <a href="/es/visa-colombia.html">Colombia</a> e <a href="/es/visa-indonesia.html">Indonesia</a>. Consulte nuestra <a href="/es/digital-nomad-visas-guide.html">guía de visas para nómadas digitales</a>.',
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a student visa?",
        "q_es": "¿Qué es una visa de estudiante?",
        "a_es": "Una visa de estudiante le permite estudiar en una institución educativa de otro país. Los requisitos incluyen una carta de aceptación, prueba de pago de matrícula o beca, medios económicos para gastos de manutención, seguro de salud y, en algunos casos, certificados de competencia lingüística.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a Working Holiday Visa?",
        "q_es": "¿Qué es una visa Working Holiday?",
        "a_es": 'Una visa Working Holiday (WHV) permite a jóvenes (generalmente de 18 a 30 o 18 a 35 años) viajar y trabajar en otro país durante 1-2 años. Los programas populares incluyen <a href="/es/visa-australia.html">Australia</a>, <a href="/es/visa-new-zealand.html">Nueva Zelanda</a>, <a href="/es/visa-canada.html">Canadá</a> y <a href="/es/visa-japan.html">Japón</a>.',
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a Golden Visa?",
        "q_es": "¿Qué es una Golden Visa?",
        "a_es": 'Una Golden Visa es un permiso de residencia otorgado a inversores que realizan una inversión financiera significativa (generalmente en bienes raíces o negocios). Existen programas populares en <a href="/es/visa-portugal.html">Portugal</a>, <a href="/es/visa-spain.html">España</a>, <a href="/es/visa-greece.html">Grecia</a> y los <a href="/es/visa-uae.html">EAU</a>. Las inversiones van desde EUR 250.000 hasta EUR 500.000 o más.',
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a long-stay visa (Type D)?",
        "q_es": "¿Qué es una visa de larga estancia (Tipo D)?",
        "a_es": "Una visa Tipo D (visa nacional) permite estancias superiores a 90 días en un país específico. A diferencia de la visa Schengen de corta estancia (Tipo C), una visa Tipo D es emitida por países individuales para fines como estudio, trabajo, reagrupación familiar o jubilación.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "What is a multiple-entry visa?",
        "q_es": "¿Qué es una visa de entradas múltiples?",
        "a_es": "Una visa de entradas múltiples le permite entrar y salir de un país varias veces durante la vigencia de la visa. Es útil para viajeros de negocios o personas que visitan países vecinos. Las visas de entrada única pierden validez una vez que sale del país.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "Do children need their own visa?",
        "q_es": "¿Los niños necesitan su propia visa?",
        "a_es": "Sí, los niños necesitan su propia visa en la mayoría de los casos, incluso los bebés. Algunos países ofrecen tarifas reducidas para niños menores de 6 o 12 años. Los niños deben tener su propio pasaporte para la mayoría de los viajes internacionales.",
    },
    {
        "category": "Special Visa Types",
        "q_en": "Can dual citizens use either passport for visas?",
        "q_es": "¿Pueden los ciudadanos con doble nacionalidad usar cualquiera de sus pasaportes para visas?",
        "a_es": "Sí, los ciudadanos con doble nacionalidad pueden elegir qué pasaporte utilizar. Use el que ofrezca mejores condiciones de visa. Siempre entre y salga de un país con el mismo pasaporte. Algunos países no reconocen la doble nacionalidad; verifique las leyes de ambos países.",
    },
    # =========================================================================
    # Category 7: Embassy & Application Process (5 questions)
    # =========================================================================
    {
        "category": "Embassy & Application Process",
        "q_en": "How do I apply for a visa at an embassy?",
        "q_es": "¿Cómo solicito una visa en una embajada?",
        "a_es": 'Pasos: 1) Verifique los requisitos en el sitio web de la embajada. 2) Reúna los documentos. 3) Reserve una cita. 4) Asista y presente los documentos. 5) Pague la tarifa. 6) Espere el procesamiento. 7) Recoja su pasaporte con la visa. Consulte nuestra <a href="/es/how-to-apply-evisa.html">guía de cómo solicitar</a>.',
    },
    {
        "category": "Embassy & Application Process",
        "q_en": "What is a visa interview?",
        "q_es": "¿Qué es una entrevista de visa?",
        "a_es": "Algunos países (principalmente EE. UU., Reino Unido y Canadá) requieren una entrevista personal en la embajada. El oficial consular le preguntará sobre sus planes de viaje, vínculos con su país de origen, situación financiera y propósito de la visita. Sea honesto y lleve documentos de respaldo.",
    },
    {
        "category": "Embassy & Application Process",
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_es": "¿Puedo solicitar una visa desde un país del que no soy ciudadano?",
        "a_es": "Sí, en muchos casos puede solicitar en la embajada del país donde tiene residencia legal. Necesitará prueba de residencia legal (permiso de residencia, visa de larga duración). Algunos países solo aceptan solicitudes de ciudadanos o residentes permanentes del país anfitrión.",
    },
    {
        "category": "Embassy & Application Process",
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_es": "¿Cuál es la diferencia entre una calcomanía de visa, un sello y una eVisa?",
        "a_es": "Una calcomanía de visa es una etiqueta física adherida a una página del pasaporte (Schengen, EE. UU., Reino Unido). Un sello de visa es una marca de entrada/salida estampada por inmigración. Una eVisa es una autorización digital vinculada a su número de pasaporte, sin necesidad de calcomanía o sello físico.",
    },
    {
        "category": "Embassy & Application Process",
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_es": "¿Puedo viajar con una visa en un pasaporte cancelado?",
        "a_es": "En algunos casos sí, si la visa aún es válida. Países como EE. UU. y el Reino Unido le permiten viajar con una visa válida en un pasaporte antiguo junto con su nuevo pasaporte. Consulte las reglas del país específico, ya que algunos exigen que la visa se transfiera al nuevo pasaporte.",
    },
]


if __name__ == "__main__":
    print(f"Total FAQ translations: {len(FAQ_TRANSLATIONS)}")
    print(f"Categories: {len(CATEGORY_TRANSLATIONS)}")
    for cat, cat_es in CATEGORY_TRANSLATIONS.items():
        count = sum(1 for f in FAQ_TRANSLATIONS if f.get("category") == cat)
        print(f"  {cat} -> {cat_es} ({count} questions)")
