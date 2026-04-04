#!/usr/bin/env python3
"""
gen_nat_multilang.py
Generates FR / ES / PT nationality pages from EN sources.
Reads key facts from each EN page, fills translated templates.
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW   = "C:/Users/chemi/Documents/evisa/pacific-main/www"
BASE  = "https://www.evisa-card.com"

# ── Country names ────────────────────────────────────────────────────────────
CNAMES = {
    "fr": {
        "argentina":"l'Argentine","australia":"l'Australie","austria":"l'Autriche",
        "belgium":"la Belgique","brazil":"le Brésil","cambodia":"le Cambodge",
        "canada":"le Canada","china":"la Chine","colombia":"la Colombie",
        "costa-rica":"le Costa Rica","croatia":"la Croatie",
        "czech-republic":"la République tchèque","denmark":"le Danemark",
        "france":"la France","germany":"l'Allemagne","greece":"la Grèce",
        "hong-kong":"Hong Kong","hungary":"la Hongrie","india":"l'Inde",
        "indonesia":"l'Indonésie","ireland":"l'Irlande","italy":"l'Italie",
        "japan":"le Japon","jordan":"la Jordanie","malaysia":"la Malaisie",
        "maldives":"les Maldives","mexico":"le Mexique","nepal":"le Népal",
        "netherlands":"les Pays-Bas","new-zealand":"la Nouvelle-Zélande",
        "norway":"la Norvège","philippines":"les Philippines","poland":"la Pologne",
        "portugal":"le Portugal","qatar":"le Qatar","romania":"la Roumanie",
        "singapore":"Singapour","spain":"l'Espagne","sri-lanka":"le Sri Lanka",
        "sweden":"la Suède","switzerland":"la Suisse","taiwan":"Taïwan",
        "thailand":"la Thaïlande","turkey":"la Turquie",
        "uae":"les Émirats Arabes Unis","united-kingdom":"le Royaume-Uni",
        "usa":"les États-Unis","vietnam":"le Viêt Nam",
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

# ── Nationality labels: (adj singular, adj plural, demonym) ─────────────────
NAT_LABELS = {
    "fr": {
        "us":            ("américain(e)",   "américains",    "les Américains"),
        "uk":            ("britannique",    "britanniques",  "les Britanniques"),
        "canadian":      ("canadien(ne)",   "canadiens",     "les Canadiens"),
        "french":        ("français(e)",    "français",      "les Français"),
        "german":        ("allemand(e)",    "allemands",     "les Allemands"),
        "japanese":      ("japonais(e)",    "japonais",      "les Japonais"),
        "australian":    ("australien(ne)", "australiens",   "les Australiens"),
        "indian":        ("indien(ne)",     "indiens",       "les Indiens"),
        "chinese":       ("chinois(e)",     "chinois",       "les Chinois"),
        "russian":       ("russe",          "russes",        "les Russes"),
        "brazilian":     ("brésilien(ne)",  "brésiliens",    "les Brésiliens"),
        "mexican":       ("mexicain(e)",    "mexicains",     "les Mexicains"),
        "south-african": ("sud-africain(e)","sud-africains", "les Sud-Africains"),
        "nigerian":      ("nigérian(e)",    "nigérians",     "les Nigérians"),
        "korean":        ("coréen(ne)",     "coréens",       "les Coréens"),
        "singaporean":   ("singapourien(ne)","singapouriens","les Singapouriens"),
        "indonesian":    ("indonésien(ne)", "indonésiens",   "les Indonésiens"),
        "philippine":    ("philippin(e)",   "philippins",    "les Philippins"),
        "turkish":       ("turc/turque",    "turcs",         "les Turcs"),
        "argentinian":   ("argentin(e)",    "argentins",     "les Argentins"),
        "bangladeshi":   ("bangladais(e)",  "bangladais",    "les Bangladais"),
        "pakistani":     ("pakistanais(e)", "pakistanais",   "les Pakistanais"),
    },
    "es": {
        "us":            ("estadounidense",  "estadounidenses", "los estadounidenses"),
        "uk":            ("británico/a",     "británicos",      "los británicos"),
        "canadian":      ("canadiense",      "canadienses",     "los canadienses"),
        "french":        ("francés/francesa","franceses",       "los franceses"),
        "german":        ("alemán/alemana",  "alemanes",        "los alemanes"),
        "japanese":      ("japonés/japonesa","japoneses",       "los japoneses"),
        "australian":    ("australiano/a",   "australianos",    "los australianos"),
        "indian":        ("indio/a",         "indios",          "los indios"),
        "chinese":       ("chino/a",         "chinos",          "los chinos"),
        "russian":       ("ruso/a",          "rusos",           "los rusos"),
        "brazilian":     ("brasileño/a",     "brasileños",      "los brasileños"),
        "mexican":       ("mexicano/a",      "mexicanos",       "los mexicanos"),
        "south-african": ("sudafricano/a",   "sudafricanos",    "los sudafricanos"),
        "nigerian":      ("nigeriano/a",     "nigerianos",      "los nigerianos"),
        "korean":        ("coreano/a",       "coreanos",        "los coreanos"),
        "singaporean":   ("singapurense",    "singapurenses",   "los singapurenses"),
        "indonesian":    ("indonesio/a",     "indonesios",      "los indonesios"),
        "philippine":    ("filipino/a",      "filipinos",       "los filipinos"),
        "turkish":       ("turco/a",         "turcos",          "los turcos"),
        "argentinian":   ("argentino/a",     "argentinos",      "los argentinos"),
        "bangladeshi":   ("bangladesí",      "bangladesíes",    "los bangladesíes"),
        "pakistani":     ("pakistaní",       "pakistaníes",     "los pakistaníes"),
    },
    "pt": {
        "us":            ("americano/a",    "americanos",    "os americanos"),
        "uk":            ("britânico/a",    "britânicos",    "os britânicos"),
        "canadian":      ("canadense",      "canadenses",    "os canadenses"),
        "french":        ("francês/francesa","franceses",    "os franceses"),
        "german":        ("alemão/alemã",   "alemães",       "os alemães"),
        "japanese":      ("japonês/japonesa","japoneses",    "os japoneses"),
        "australian":    ("australiano/a",  "australianos",  "os australianos"),
        "indian":        ("indiano/a",      "indianos",      "os indianos"),
        "chinese":       ("chinês/chinesa", "chineses",      "os chineses"),
        "russian":       ("russo/a",        "russos",        "os russos"),
        "brazilian":     ("brasileiro/a",   "brasileiros",   "os brasileiros"),
        "mexican":       ("mexicano/a",     "mexicanos",     "os mexicanos"),
        "south-african": ("sul-africano/a", "sul-africanos", "os sul-africanos"),
        "nigerian":      ("nigeriano/a",    "nigerianos",    "os nigerianos"),
        "korean":        ("coreano/a",      "coreanos",      "os coreanos"),
        "singaporean":   ("singapurense",   "singapurenses", "os singapurenses"),
        "indonesian":    ("indonésio/a",    "indonésios",    "os indonésios"),
        "philippine":    ("filipino/a",     "filipinos",     "os filipinos"),
        "turkish":       ("turco/a",        "turcos",        "os turcos"),
        "argentinian":   ("argentino/a",    "argentinos",    "os argentinos"),
        "bangladeshi":   ("bangladeshiano/a","bangladeshianos","os bangladeshianos"),
        "pakistani":     ("paquistanês/esa","paquistaneses", "os paquistaneses"),
    },
}

# ── UI strings ────────────────────────────────────────────────────────────────
UI = {
    "fr": {
        "home":"Accueil","destinations":"Destinations","about":"À propos",
        "blog":"Blog","guides":"Guides","lang_label":"Français",
        "flag":"fi-fr","flag_gb":"fi-gb",
        "table_key":"Informations clés","visa_req_hdr":"Visa requis",
        "allowed_stay":"Durée autorisée","fee":"Frais",
        "proc_time":"Délai de traitement","evisa_avail":"eVisa disponible",
        "passport_val":"Validité passeport requise",
        "visa_free_val":"Non — Sans visa","evisa_val":"Oui — eVisa",
        "voa_val":"Oui — Visa à l'arrivée","visa_req_val":"Oui — Visa requis",
        "free":"Gratuit","not_needed":"Non requis","na":"N/A",
        "how_to_apply":"Comment postuler",
        "eeat_updated":"Dernière mise à jour\u00a0: <strong>mars\u00a02026</strong>.",
        "eeat_important":"<strong>Important\u00a0:</strong>",
        "eeat_suffix":"pour les informations officielles avant de réserver.",
        "related":"Guides connexes",
        "all_dest":"Toutes les destinations \u2192",
        "legal_label":"Mentions légales","disclaimer_label":"Avertissement",
        "footer_copy":"\u00a9 2026 eVisa-Card.com \u2014 Plateforme mondiale d'information eVisa & Voyage",
        "h2_need":"Les citoyens {nat} ont-ils besoin d'un visa pour {country}\u00a0?",
        "h2_tips":"Conseils pour les voyageurs {nat}",
        "tips_generic":[
            "Assurez-vous que votre passeport est valide pour au moins 6 mois au-delà de votre séjour prévu.",
            "Conservez un billet aller-retour ou de continuation — les agents d'immigration peuvent le demander.",
            "Une assurance voyage est fortement recommandée.",
            "Vérifiez les conditions d'entrée auprès de l'ambassade ou du consulat avant le départ.",
        ],
        "p_visa_free":"Les citoyens {nat} ne nécessitent <strong>pas de visa</strong> pour visiter {country}. L'entrée sans visa est accordée pour une durée pouvant aller jusqu'à <strong>{stay}</strong>. Aucune autorisation préalable n'est requise — arrivez simplement avec un passeport valide.",
        "p_visa_free_apply":"Aucune demande n'est nécessaire pour les séjours jusqu'à {stay}. À l'arrivée, présentez votre passeport valide (6+ mois de validité), un billet de retour ou de continuation, et une preuve d'hébergement.",
        "p_evisa":"Les citoyens {nat} doivent obtenir un <strong>eVisa</strong> avant de voyager vers {country}. Le coût est de <strong>{fee}</strong> et le délai de traitement est d'environ <strong>{proc}</strong>. Faites votre demande sur le site officiel avant le départ.",
        "p_evisa_apply":"Rendez-vous sur le portail officiel d'immigration de {country}, créez un compte, remplissez le formulaire de demande en ligne et téléchargez les documents requis (passeport, photo, itinéraire). Payez les frais en ligne. L'eVisa est envoyé par courriel.",
        "p_voa":"Les citoyens {nat} peuvent obtenir un <strong>visa à l'arrivée</strong> à {country}. Les frais sont de <strong>{fee}</strong> et la durée maximale de séjour est de <strong>{stay}</strong>. Apportez des formulaires remplis et les frais en espèces.",
        "p_voa_apply":"À l'arrivée à l'aéroport international, rendez-vous au guichet Visa à l'arrivée. Remplissez le formulaire de demande, présentez votre passeport et payez les frais requis ({fee}) en espèces ou par carte.",
        "p_visa_req":"Les citoyens {nat} ont besoin d'un <strong>visa</strong> pour visiter {country}. Il faut contacter l'ambassade ou le consulat de {country} pour déposer une demande de visa touristique.",
        "p_visa_req_apply":"Contactez l'ambassade ou le consulat de {country} le plus proche. Préparez votre dossier\u00a0: passeport valide, photos d'identité, justificatif de séjour, preuve de ressources financières et billet d'avion aller-retour.",
        "eeat_visit":"Consultez le site officiel de l'immigration de {country}",
        "dest_page":"/fr/destination.html",
    },
    "es": {
        "home":"Inicio","destinations":"Destinos","about":"Acerca de",
        "blog":"Blog","guides":"Guías","lang_label":"Español",
        "flag":"fi-es","flag_gb":"fi-gb",
        "table_key":"Datos clave","visa_req_hdr":"Visa requerida",
        "allowed_stay":"Estadía permitida","fee":"Tarifa",
        "proc_time":"Tiempo de procesamiento","evisa_avail":"eVisa disponible",
        "passport_val":"Validez de pasaporte requerida",
        "visa_free_val":"No — Sin visa","evisa_val":"Sí — eVisa",
        "voa_val":"Sí — Visa a la llegada","visa_req_val":"Sí — Visa requerida",
        "free":"Gratuito","not_needed":"No requerido","na":"N/A",
        "how_to_apply":"Cómo solicitar",
        "eeat_updated":"Última actualización: <strong>marzo de 2026</strong>.",
        "eeat_important":"<strong>Importante:</strong>",
        "eeat_suffix":"para información oficial antes de reservar.",
        "related":"Guías relacionadas",
        "all_dest":"Todos los destinos \u2192",
        "legal_label":"Aviso legal","disclaimer_label":"Descargo",
        "footer_copy":"\u00a9 2026 eVisa-Card.com \u2014 Plataforma global de información eVisa y viajes",
        "h2_need":"¿Los ciudadanos {nat} necesitan visa para {country}?",
        "h2_tips":"Consejos para viajeros {nat}",
        "tips_generic":[
            "Asegúrese de que su pasaporte tenga vigencia mínima de 6 meses más allá de su estadía prevista.",
            "Lleve un boleto de regreso o de conexión — los agentes de inmigración pueden solicitarlo.",
            "Se recomienda encarecidamente contratar un seguro de viaje.",
            "Verifique los requisitos de entrada en la embajada o consulado antes de partir.",
        ],
        "p_visa_free":"Los ciudadanos {nat} <strong>no necesitan visa</strong> para visitar {country}. Se concede entrada sin visa por hasta <strong>{stay}</strong>. No se requiere autorización previa — simplemente llegue con un pasaporte válido.",
        "p_visa_free_apply":"No se requiere solicitud para estadías de hasta {stay}. A la llegada, presente su pasaporte válido (validez de 6+ meses), un boleto de regreso o de conexión, y prueba de alojamiento.",
        "p_evisa":"Los ciudadanos {nat} deben obtener un <strong>eVisa</strong> antes de viajar a {country}. El costo es de <strong>{fee}</strong> y el tiempo de procesamiento es de aproximadamente <strong>{proc}</strong>. Solicítelo en el portal oficial antes de viajar.",
        "p_evisa_apply":"Acceda al portal oficial de inmigración de {country}, cree una cuenta, complete el formulario de solicitud en línea y cargue los documentos requeridos (pasaporte, foto, itinerario). Pague la tarifa en línea. El eVisa se envía por correo electrónico.",
        "p_voa":"Los ciudadanos {nat} pueden obtener <strong>visa a la llegada</strong> en {country}. La tarifa es de <strong>{fee}</strong> y la estadía máxima es de <strong>{stay}</strong>. Traiga formularios completados y efectivo para el pago.",
        "p_voa_apply":"Al llegar al aeropuerto internacional, diríjase al mostrador de Visa a la llegada. Complete el formulario de solicitud, presente su pasaporte y pague la tarifa requerida ({fee}) en efectivo o con tarjeta.",
        "p_visa_req":"Los ciudadanos {nat} necesitan <strong>visa</strong> para visitar {country}. Es necesario contactar a la embajada o consulado de {country} para presentar una solicitud de visa turística.",
        "p_visa_req_apply":"Contacte la embajada o consulado de {country} más cercano. Prepare su expediente: pasaporte válido, fotos de identidad, justificante de estadía, prueba de solvencia económica y billete de avión de ida y vuelta.",
        "eeat_visit":"Consulte el sitio oficial de inmigración de {country}",
        "dest_page":"/es/destination.html",
    },
    "pt": {
        "home":"Início","destinations":"Destinos","about":"Sobre",
        "blog":"Blog","guides":"Guias","lang_label":"Português",
        "flag":"fi-br","flag_gb":"fi-gb",
        "table_key":"Informações principais","visa_req_hdr":"Visto necessário",
        "allowed_stay":"Permanência permitida","fee":"Taxa",
        "proc_time":"Tempo de processamento","evisa_avail":"eVisa disponível",
        "passport_val":"Validade do passaporte necessária",
        "visa_free_val":"Não — Sem visto","evisa_val":"Sim — eVisa",
        "voa_val":"Sim — Visto na chegada","visa_req_val":"Sim — Visto necessário",
        "free":"Gratuito","not_needed":"Não necessário","na":"N/A",
        "how_to_apply":"Como solicitar",
        "eeat_updated":"Última atualização: <strong>março de 2026</strong>.",
        "eeat_important":"<strong>Importante:</strong>",
        "eeat_suffix":"para informações oficiais antes de reservar.",
        "related":"Guias relacionados",
        "all_dest":"Todos os destinos \u2192",
        "legal_label":"Aviso legal","disclaimer_label":"Isenção",
        "footer_copy":"\u00a9 2026 eVisa-Card.com \u2014 Plataforma global de informações eVisa e viagens",
        "h2_need":"Os cidadãos {nat} precisam de visto para {country}?",
        "h2_tips":"Dicas para viajantes {nat}",
        "tips_generic":[
            "Certifique-se de que seu passaporte seja válido por pelo menos 6 meses além da sua estadia prevista.",
            "Leve uma passagem de retorno ou de conexão — os agentes de imigração podem solicitá-la.",
            "O seguro viagem é altamente recomendado.",
            "Verifique os requisitos de entrada na embaixada ou consulado antes da viagem.",
        ],
        "p_visa_free":"Os cidadãos {nat} <strong>não precisam de visto</strong> para visitar {country}. A entrada sem visto é concedida por até <strong>{stay}</strong>. Nenhuma autorização prévia é necessária — basta chegar com um passaporte válido.",
        "p_visa_free_apply":"Nenhuma solicitação é necessária para estadias de até {stay}. Na chegada, apresente seu passaporte válido (validade de 6+ meses), passagem de volta ou de conexão, e comprovante de hospedagem.",
        "p_evisa":"Os cidadãos {nat} devem obter um <strong>eVisa</strong> antes de viajar para {country}. O custo é de <strong>{fee}</strong> e o tempo de processamento é de aproximadamente <strong>{proc}</strong>. Solicite no portal oficial antes da viagem.",
        "p_evisa_apply":"Acesse o portal oficial de imigração de {country}, crie uma conta, preencha o formulário de solicitação online e envie os documentos necessários (passaporte, foto, itinerário). Pague a taxa online. O eVisa é enviado por e-mail.",
        "p_voa":"Os cidadãos {nat} podem obter <strong>visto na chegada</strong> em {country}. A taxa é de <strong>{fee}</strong> e a permanência máxima é de <strong>{stay}</strong>. Traga formulários preenchidos e dinheiro em espécie para pagamento.",
        "p_voa_apply":"Ao chegar no aeroporto internacional, dirija-se ao balcão de Visto na chegada. Preencha o formulário de solicitação, apresente seu passaporte e pague a taxa exigida ({fee}) em dinheiro ou cartão.",
        "p_visa_req":"Os cidadãos {nat} precisam de <strong>visto</strong> para visitar {country}. É necessário entrar em contato com a embaixada ou consulado de {country} para solicitar um visto de turismo.",
        "p_visa_req_apply":"Entre em contato com a embaixada ou consulado de {country} mais próximo. Prepare sua documentação: passaporte válido, fotos de identidade, comprovante de hospedagem, prova de recursos financeiros e passagem aérea de ida e volta.",
        "eeat_visit":"Consulte o site oficial de imigração de {country}",
        "dest_page":"/pt/destination.html",
    },
}

# ── Extract key facts from EN table ─────────────────────────────────────────
def extract_facts(html):
    """Return dict with visa_status, stay, fee, proc, official_url."""
    facts = {}
    # visa required cell
    m = re.search(r'<tr><th>Visa Required</th><td>(.*?)</td></tr>', html, re.S)
    if not m:
        m = re.search(r'<tr><th>e-Tourist Visa</th>', html, re.S)
    cell = m.group(1) if m else ""
    cell_clean = re.sub(r'<[^>]+>', '', cell).strip()

    if re.search(r'No\s*[—\-]', cell_clean) or re.search(r'Visa.Free', cell_clean, re.I) or "without a visa" in html.lower():
        facts["status"] = "visa_free"
    elif re.search(r'eVisa|e-Tourist', cell_clean, re.I):
        facts["status"] = "evisa"
    elif re.search(r'Arrival', cell_clean, re.I):
        facts["status"] = "voa"
    else:
        facts["status"] = "visa_req"

    # stay
    m2 = re.search(r'<tr><th>(?:Allowed Stay|Max Stay|Stay)</th><td>(.*?)</td></tr>', html, re.S)
    facts["stay"] = re.sub(r'<[^>]+>','', m2.group(1)).strip() if m2 else "as granted"

    # fee
    m3 = re.search(r'<tr><th>(?:Fee|30-Day Fee)</th><td>(.*?)</td></tr>', html, re.S)
    facts["fee"] = re.sub(r'<[^>]+>','', m3.group(1)).strip() if m3 else "varies"

    # processing
    m4 = re.search(r'<tr><th>Processing Time</th><td>(.*?)</td></tr>', html, re.S)
    facts["proc"] = re.sub(r'<[^>]+>','', m4.group(1)).strip() if m4 else "varies"

    # official URL (first external link in body)
    m5 = re.search(r'href="(https?://(?:(?!evisa-card\.com)[^"]+))"', html)
    facts["url"] = m5.group(1) if m5 else "#"

    return facts


# ── Page template ─────────────────────────────────────────────────────────────
def make_page(lang, country_slug, nat_slug, facts, country_name_en, nat_adj_en):
    u   = UI[lang]
    cn  = CNAMES[lang].get(country_slug, country_name_en)
    nat_labels = NAT_LABELS[lang].get(nat_slug, (nat_adj_en, nat_adj_en+"s", nat_adj_en+"s"))
    nat_adj    = nat_labels[0]
    nat_plural = nat_labels[1]
    nat_dem    = nat_labels[2]

    slug_base = f"{country_slug}-visa-for-{nat_slug}-citizens"
    canonical = f"{BASE}/{lang}/{slug_base}"

    # title + description
    if lang == "fr":
        title = f"Visa {cn.replace('l\'','').replace('la ','').replace('le ','').replace('les ','')} pour citoyens {nat_adj} 2026 &#8212; Exigences &amp; Comment postuler"
        desc  = f"Citoyens {nat_adj} qui voyagent vers {cn} en 2026 : conditions de visa, frais et comment postuler. Guide complet mis à jour mars 2026."
        h2_title = f"Visa {cn} pour citoyens {nat_plural}"
    elif lang == "es":
        title = f"Visa {cn} para ciudadanos {nat_adj} 2026 &#8212; Requisitos &amp; Cómo solicitar"
        desc  = f"Ciudadanos {nat_adj} que viajan a {cn} en 2026: requisitos de visa, tarifas y cómo solicitar. Guía completa actualizada marzo 2026."
        h2_title = f"Visa {cn} para ciudadanos {nat_plural}"
    else:
        title = f"Visto {cn} para cidadãos {nat_adj} 2026 &#8212; Requisitos &amp; Como solicitar"
        desc  = f"Cidadãos {nat_adj} que viajam para {cn} em 2026: requisitos de visto, taxas e como solicitar. Guia completo atualizado março de 2026."
        h2_title = f"Visto {cn} para cidadãos {nat_plural}"

    # visa status row value
    status_map = {"visa_free": u["visa_free_val"], "evisa": u["evisa_val"],
                  "voa": u["voa_val"], "visa_req": u["visa_req_val"]}
    visa_val = status_map.get(facts["status"], u["visa_req_val"])

    fee_disp  = u["free"] if facts["fee"].lower() in ("free","gratuit","gratuito") else facts["fee"]
    proc_disp = u["not_needed"] if facts["proc"].lower() in ("n/a","no visa needed","not needed") else facts["proc"]
    stay_disp = u["na"] if facts["stay"] in ("N/A","n/a") else facts["stay"]

    # content paragraphs
    def fmt(tpl): return tpl.format(nat=nat_plural, country=cn, stay=stay_disp, fee=facts["fee"], proc=facts["proc"])
    if facts["status"] == "visa_free":
        p_intro = fmt(u["p_visa_free"])
        p_apply = fmt(u["p_visa_free_apply"])
    elif facts["status"] == "evisa":
        p_intro = fmt(u["p_evisa"])
        p_apply = fmt(u["p_evisa_apply"])
    elif facts["status"] == "voa":
        p_intro = fmt(u["p_voa"])
        p_apply = fmt(u["p_voa_apply"])
    else:
        p_intro = fmt(u["p_visa_req"])
        p_apply = fmt(u["p_visa_req_apply"])

    h2_need  = u["h2_need"].format(nat=nat_plural, country=cn)
    h2_tips  = u["h2_tips"].format(nat=nat_plural)
    tips_li  = "\n".join(f"        <li>{t}</li>" for t in u["tips_generic"])

    # Destination page link
    dest_href = u["dest_page"]

    # Related links (adapt for language)
    related_visa  = f"visa-{country_slug}.html" if lang == "en" else f"visa-{country_slug}.html"
    # Use country name in English for guide links (page files are same slug)
    country_disp_en = country_name_en

    # official link text
    if lang == "fr":
        official_txt = f"site officiel de {cn}"
    elif lang == "es":
        official_txt = f"sitio oficial de {cn}"
    else:
        official_txt = f"site oficial de {cn}"

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport"/>
    <title>{title}</title>
    <meta name="description" content="{desc}"/>
    <meta name="robots" content="index, follow"/>
    <link rel="canonical" href="{canonical}"/>
    <link rel="alternate" hreflang="en" href="{BASE}/en/{slug_base}"/>
    <link rel="alternate" hreflang="fr" href="{BASE}/fr/{slug_base}"/>
    <link rel="alternate" hreflang="es" href="{BASE}/es/{slug_base}"/>
    <link rel="alternate" hreflang="pt" href="{BASE}/pt/{slug_base}"/>
    <link rel="alternate" hreflang="x-default" href="{BASE}/en/{slug_base}"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/owl.carousel.min.css" rel="stylesheet"/>
    <link href="../css/owl.theme.default.min.css" rel="stylesheet"/>
    <link href="../css/magnific-popup.css" rel="stylesheet"/>
    <link href="../css/flaticon.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png"/>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light" id="ftco-navbar" style="background-color:#0d2461 !important;position:relative;z-index:10;">
    <div class="container">
        <a class="navbar-brand" href="../index.html" style="padding:4px 0;"><img src="../images/logo.png" alt="eVisa-Card.com" style="height:44px;width:auto;vertical-align:middle;"></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="ftco-nav">
            <ul class="navbar-nav align-items-center">
                <li class="nav-item"><a class="nav-link" href="../index.html">{u["home"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="{dest_href}">{u["destinations"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">{u["about"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">{u["blog"]}</a></li>
                <li class="nav-item"><a class="nav-link" href="/{lang}/expat-guides.html">{u["guides"]}</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {u['flag']}"></span> {u["lang_label"]}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item" href="/en/{slug_base}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item {'active' if lang=='fr' else ''}" href="/fr/{slug_base}.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item {'active' if lang=='es' else ''}" href="/es/{slug_base}.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item {'active' if lang=='pt' else ''}" href="/pt/{slug_base}.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
  <div class="container">
    <article class="country-page">
      <h1>{h2_title} 2026</h1>

      <table class="table table-bordered table-sm mt-3 mb-4">
        <thead><tr><th colspan="2" class="table-dark">{u["table_key"]} &#8212; {nat_plural} &amp; {cn}</th></tr></thead>
        <tbody>
          <tr><th>{u["visa_req_hdr"]}</th><td>{visa_val}</td></tr>
          <tr><th>{u["allowed_stay"]}</th><td>{stay_disp}</td></tr>
          <tr><th>{u["fee"]}</th><td>{fee_disp}</td></tr>
          <tr><th>{u["proc_time"]}</th><td>{proc_disp}</td></tr>
          <tr><th>{u["passport_val"]}</th><td>6+ mois / months</td></tr>
        </tbody>
      </table>

      <h2>{h2_need}</h2>
      <p>{p_intro}</p>

      <h2>{u["how_to_apply"]}</h2>
      <p>{p_apply}</p>

      <h2>{h2_tips}</h2>
      <ul>
{tips_li}
      </ul>

      <div class="eeat-section mt-4 p-3 bg-light rounded border-left border-info">
        <div class="d-flex align-items-start">
          <div class="mr-3"><span class="fa fa-shield fa-2x text-info"></span></div>
          <div>
            <strong>Editorial Team &#8212; eVisa-Card.com</strong>
            <p class="mb-1 small text-muted">{u["eeat_updated"]}</p>
            <p class="mb-0 small">{u["eeat_important"]} {u["eeat_visit"].format(country=cn)} (<a href="{facts['url']}" target="_blank" rel="noopener">{facts['url']}</a>) {u["eeat_suffix"]}</p>
          </div>
        </div>
      </div>
    </article>

    <div class="related-guides mt-5 pt-4 border-top">
      <h3 class="h5 mb-3">{u["related"]}</h3>
      <div>
        <a class="btn btn-outline-secondary btn-sm mr-2 mb-2" href="visa-{country_slug}.html">{country_disp_en} Visa Guide</a>
        <a class="btn btn-primary btn-sm mb-2" href="{dest_href}">{u["all_dest"]}</a>
      </div>
    </div>
  </div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">{u["footer_copy"]}</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="/{lang}/{('mentions-legales' if lang=='fr' else 'aviso-legal')}.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">{u["legal_label"]}</a>
                    &nbsp;|&nbsp;
                    <a href="/{lang}/disclaimer.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">{u["disclaimer_label"]}</a>
                </p>
            </div>
        </div>
    </div>
</footer>

<div class="show fullscreen" id="ftco-loader">
  <svg class="circular" height="48px" width="48px">
    <circle class="path-bg" cx="24" cy="24" fill="none" r="22" stroke="#eeeeee" stroke-width="4"></circle>
    <circle class="path" cx="24" cy="24" fill="none" r="22" stroke="#F96D00" stroke-miterlimit="10" stroke-width="4"></circle>
  </svg>
</div>
<script src="../js/jquery.min.js"></script>
<script src="../js/jquery-migrate-3.0.1.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/jquery.easing.1.3.js"></script>
<script src="../js/jquery.waypoints.min.js"></script>
<script src="../js/jquery.stellar.min.js"></script>
<script src="../js/owl.carousel.min.js"></script>
<script src="../js/jquery.magnific-popup.min.js"></script>
<script src="../js/jquery.animateNumber.min.js"></script>
<script src="../js/scrollax.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""
    return html


# ── Main: iterate EN pages ────────────────────────────────────────────────────
en_pages = glob.glob(os.path.join(WWW, "en", "*-visa-for-*-citizens.html"))
created = {"fr": 0, "es": 0, "pt": 0}
errors  = 0

for en_path in en_pages:
    fname = os.path.basename(en_path)
    # parse filename: {country}-visa-for-{nat}-citizens.html
    m = re.match(r'^(.+)-visa-for-(.+)-citizens\.html$', fname)
    if not m:
        continue
    country_slug = m.group(1)
    nat_slug     = m.group(2)

    try:
        with open(en_path, "r", encoding="utf-8") as f:
            en_html = f.read()
    except Exception as e:
        print(f"ERR reading {fname}: {e}")
        errors += 1
        continue

    # Extract EN title h1 to get display names
    h1m = re.search(r'<h1>([^<]+)</h1>', en_html)
    h1  = h1m.group(1) if h1m else ""
    # "Thailand Visa for US Citizens 2026" → country_name_en="Thailand", nat_adj_en="US"
    pm = re.match(r'^(.+?) Visa for (.+?) Citizens', h1)
    country_name_en = pm.group(1) if pm else country_slug.replace("-", " ").title()
    nat_adj_en      = pm.group(2) if pm else nat_slug.replace("-", " ").title()

    facts = extract_facts(en_html)

    for lang in ("fr", "es", "pt"):
        out_dir  = os.path.join(WWW, lang)
        out_path = os.path.join(out_dir, fname)
        if os.path.exists(out_path):
            continue   # skip if already generated
        try:
            page_html = make_page(lang, country_slug, nat_slug, facts, country_name_en, nat_adj_en)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            created[lang] += 1
        except Exception as e:
            print(f"ERR {lang}/{fname}: {e}")
            errors += 1

print(f"Created FR: {created['fr']} | ES: {created['es']} | PT: {created['pt']} | Errors: {errors}")
print("DONE")
