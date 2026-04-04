#!/usr/bin/env python3
"""
Generate FR/ES/PT versions of all *-visa-extension.html pages from EN sources.
Uses text substitution approach (like gen_cluster_multilang.py).
"""
import os, re, glob

BASE = r"C:/Users/chemi/Documents/evisa/pacific-main/www"
EN_DIR = os.path.join(BASE, "en")

FLAG_MAP = {"fr":"fr","es":"es","pt":"br"}

def get_subs(lang):
    if lang == "fr":
        return [
            ("How to Extend Your", "Comment prolonger votre"),
            ("Visa Extension 2026", "Prolongation de visa 2026"),
            ("visa-extension.html", "visa-extension.html"),
            ("Extension at a Glance", "Aperçu de la prolongation"),
            ("Can You Extend Your", "Pouvez-vous prolonger votre"),
            ("Requirements &amp; Documents", "Conditions et documents"),
            ("Step-by-Step Extension Process", "Processus de prolongation étape par étape"),
            ("Overstay Consequences", "Conséquences du dépassement"),
            ("Related", "Guides associés"),
            ("Visa Guides", "sur le visa"),
            ("Visa Overview", "Aperçu du visa"),
            ("Visa Requirements", "Conditions de visa"),
            ("Visa Fees", "Frais de visa"),
            ("All Destinations", "Toutes les destinations"),
            ("How to Apply for a", "Comment demander une"),
            ("Visa Extension", "Prolongation de visa"),
            ("Step 1: Gather documents", "Étape 1 : Rassembler les documents"),
            ("Step 2: Apply at", "Étape 2 : Déposer la demande à"),
            ("Step 3: Pay the fee", "Étape 3 : Payer les frais"),
            ("Step 4: Wait for processing", "Étape 4 : Attendre le traitement"),
            ("Step 5: Receive your extension", "Étape 5 : Recevoir la prolongation"),
            ("Gather your documents", "Rassemblez vos documents"),
            ("Prepare passport, bank statements", "Préparez le passeport, les relevés bancaires"),
            ("Submit your extension application", "Déposez votre demande de prolongation"),
            ("Payment is required at the time", "Le paiement est requis au moment"),
            ("Processing typically takes", "Le traitement prend généralement"),
            ("Your new authorised stay", "Votre nouveau séjour autorisé"),
            ("Can I extend my", "Puis-je prolonger mon"),
            ("How long does a", "Combien de temps dure une"),
            ("What is the fee for a", "Quel est le tarif pour une"),
            ("What happens if I overstay", "Que se passe-t-il si je dépasse"),
            ("in 2026", "en 2026"),
            ("how to extend your stay, fees, required documents and overstay consequences. Complete guide.", "comment prolonger votre séjour, frais, documents requis et conséquences du dépassement. Guide complet."),
            ("how to extend your stay, fees, required documents and overstay consequences.", "comment prolonger votre séjour, frais, documents requis et conséquences du dépassement."),
            ("Editorial Team", "Équipe éditoriale"),
            ("This guide is maintained by our visa research team.", "Ce guide est maintenu par notre équipe de recherche sur les visas."),
            ("Last updated:", "Dernière mise à jour :"),
            ("Important:", "Important :"),
            ("Visa extension rules change frequently.", "Les règles de prolongation de visa changent fréquemment."),
            ("Always verify current requirements at", "Vérifiez toujours les exigences actuelles sur"),
            ("before making travel plans.", "avant de planifier votre voyage."),
            ("This page is for informational purposes only.", "Cette page est fournie à titre informatif uniquement."),
            ("Warning:", "Avertissement :"),
            ("Overstaying your visa or authorised stay in", "Dépasser votre visa ou séjour autorisé en"),
            ("can have serious consequences.", "peut avoir de graves conséquences."),
            ("Apply <strong>before your current visa expires</strong>", "Faites votre demande <strong>avant l'expiration de votre visa actuel</strong>"),
            ("to remain in legal status throughout the process.", "pour rester en situation régulière tout au long du processus."),
            ("Extension Type", "Type de prolongation"),
            ("Duration", "Durée"),
            ("Where to Apply", "Où faire la demande"),
            ("Processing Time", "Délai de traitement"),
            (" Visa in 2026", " en 2026"),
            ("requires applying through the official immigration authority before your current visa or permitted stay expires.", "nécessite de faire une demande auprès de l'autorité d'immigration officielle avant l'expiration de votre visa ou séjour autorisé."),
            ("This guide covers the extension process, fees, documents required and the consequences of overstaying.", "Ce guide couvre le processus de prolongation, les frais, les documents requis et les conséquences du dépassement."),
            ("Yes, in most cases tourists can request a stay extension through", "Oui, dans la plupart des cas, les touristes peuvent demander une prolongation de séjour via"),
            ("Extensions are typically processed within", "Les prolongations sont généralement traitées en"),
            ("The standard fee is", "Le tarif standard est"),
            ("You must apply before your current authorised stay expires", "Vous devez faire la demande avant l'expiration de votre séjour autorisé"),
            ("applying in time ensures you remain in lawful status during processing.", "faire la demande dans les délais vous garantit de rester en situation régulière pendant le traitement."),
            ("Valid passport (minimum 6 months validity beyond requested stay)", "Passeport valide (minimum 6 mois de validité au-delà du séjour demandé)"),
            ("Completed extension application form", "Formulaire de demande de prolongation rempli"),
            ("Proof of sufficient funds (recent bank statement)", "Preuve de fonds suffisants (relevé bancaire récent)"),
            ("Proof of accommodation", "Preuve d'hébergement"),
            ("Onward or return travel booking", "Réservation de voyage aller ou retour"),
            ("Proof of reason for extension (if required)", "Justificatif du motif de prolongation (si requis)"),
            ("Application fee:", "Frais de dossier :"),
            ("© 2026 eVisa-Card.com", "© 2026 eVisa-Card.com"),
            ("Global eVisa &amp; Travel Information Platform", "Plateforme mondiale d'information sur les eVisas et les voyages"),
            ("Home", "Accueil"),
            ("Destinations", "Destinations"),
            ("About", "À propos"),
            ("Guides", "Guides"),
            ("English", "English"),
            ("Toggle navigation", "Basculer la navigation"),
            ("Menu", "Menu"),
        ]
    elif lang == "es":
        return [
            ("How to Extend Your", "Cómo prorrogar tu"),
            ("Visa Extension 2026", "Prórroga de visado 2026"),
            ("Extension at a Glance", "Prórroga de un vistazo"),
            ("Can You Extend Your", "¿Puedes prorrogar tu"),
            ("Requirements &amp; Documents", "Requisitos y documentos"),
            ("Step-by-Step Extension Process", "Proceso de prórroga paso a paso"),
            ("Overstay Consequences", "Consecuencias de la estancia excesiva"),
            ("Related", "Guías relacionadas"),
            ("Visa Guides", "sobre el visado"),
            ("Visa Overview", "Resumen del visado"),
            ("Visa Requirements", "Requisitos de visado"),
            ("Visa Fees", "Tasas de visado"),
            ("All Destinations", "Todos los destinos"),
            ("How to Apply for a", "Cómo solicitar una"),
            ("Visa Extension", "Prórroga de visado"),
            ("Step 1: Gather documents", "Paso 1: Reunir documentos"),
            ("Step 2: Apply at", "Paso 2: Solicitar en"),
            ("Step 3: Pay the fee", "Paso 3: Pagar la tasa"),
            ("Step 4: Wait for processing", "Paso 4: Esperar la tramitación"),
            ("Step 5: Receive your extension", "Paso 5: Recibir la prórroga"),
            ("Gather your documents", "Reúne tus documentos"),
            ("Prepare passport, bank statements", "Prepara el pasaporte, extractos bancarios"),
            ("Submit your extension application", "Presenta tu solicitud de prórroga"),
            ("Payment is required at the time", "El pago es requerido en el momento"),
            ("Processing typically takes", "La tramitación suele tardar"),
            ("Your new authorised stay", "Tu nueva estancia autorizada"),
            ("Can I extend my", "¿Puedo prorrogar mi"),
            ("How long does a", "¿Cuánto tarda una"),
            ("What is the fee for a", "¿Cuál es la tasa de una"),
            ("What happens if I overstay", "¿Qué pasa si supero"),
            ("in 2026", "en 2026"),
            ("how to extend your stay, fees, required documents and overstay consequences. Complete guide.", "cómo prorrogar tu estancia, tasas, documentos requeridos y consecuencias de la estancia excesiva. Guía completa."),
            ("how to extend your stay, fees, required documents and overstay consequences.", "cómo prorrogar tu estancia, tasas, documentos requeridos y consecuencias de la estancia excesiva."),
            ("Editorial Team", "Equipo editorial"),
            ("This guide is maintained by our visa research team.", "Esta guía es mantenida por nuestro equipo de investigación de visados."),
            ("Last updated:", "Última actualización:"),
            ("Important:", "Importante:"),
            ("Visa extension rules change frequently.", "Las normas de prórroga de visado cambian con frecuencia."),
            ("Always verify current requirements at", "Verifica siempre los requisitos actuales en"),
            ("before making travel plans.", "antes de planificar tu viaje."),
            ("This page is for informational purposes only.", "Esta página es solo para fines informativos."),
            ("Warning:", "Advertencia:"),
            ("Overstaying your visa or authorised stay in", "Superar tu visado o estancia autorizada en"),
            ("can have serious consequences.", "puede tener graves consecuencias."),
            ("Apply <strong>before your current visa expires</strong>", "Solicita <strong>antes de que expire tu visado actual</strong>"),
            ("to remain in legal status throughout the process.", "para mantener tu situación regular durante todo el proceso."),
            ("Extension Type", "Tipo de prórroga"),
            ("Duration", "Duración"),
            ("Where to Apply", "Dónde solicitar"),
            ("Processing Time", "Tiempo de tramitación"),
            ("requires applying through the official immigration authority before your current visa or permitted stay expires.", "requiere solicitar a través de la autoridad de inmigración oficial antes de que expire tu visado o estancia autorizada."),
            ("This guide covers the extension process, fees, documents required and the consequences of overstaying.", "Esta guía cubre el proceso de prórroga, tasas, documentos requeridos y las consecuencias de la estancia excesiva."),
            ("Yes, in most cases tourists can request a stay extension through", "Sí, en la mayoría de los casos los turistas pueden solicitar una prórroga de estancia a través de"),
            ("Extensions are typically processed within", "Las prórrogas se tramitan normalmente en"),
            ("The standard fee is", "La tasa estándar es"),
            ("You must apply before your current authorised stay expires", "Debes solicitar antes de que expire tu estancia autorizada"),
            ("Valid passport (minimum 6 months validity beyond requested stay)", "Pasaporte válido (mínimo 6 meses de validez más allá de la estancia solicitada)"),
            ("Completed extension application form", "Formulario de solicitud de prórroga cumplimentado"),
            ("Proof of sufficient funds (recent bank statement)", "Prueba de fondos suficientes (extracto bancario reciente)"),
            ("Proof of accommodation", "Prueba de alojamiento"),
            ("Onward or return travel booking", "Reserva de viaje de ida o de regreso"),
            ("Proof of reason for extension (if required)", "Justificante del motivo de prórroga (si es necesario)"),
            ("Application fee:", "Tasa de solicitud:"),
            ("Global eVisa &amp; Travel Information Platform", "Plataforma global de información sobre eVisas y viajes"),
            ("Home", "Inicio"),
            ("Destinations", "Destinos"),
            ("About", "Acerca de"),
            ("English", "English"),
            ("Toggle navigation", "Activar navegación"),
            ("Menu", "Menú"),
        ]
    elif lang == "pt":
        return [
            ("How to Extend Your", "Como prorrogar o seu"),
            ("Visa Extension 2026", "Prorrogação de visto 2026"),
            ("Extension at a Glance", "Prorrogação em resumo"),
            ("Can You Extend Your", "Pode prorrogar o seu"),
            ("Requirements &amp; Documents", "Requisitos e documentos"),
            ("Step-by-Step Extension Process", "Processo de prorrogação passo a passo"),
            ("Overstay Consequences", "Consequências da permanência excessiva"),
            ("Related", "Guias relacionados"),
            ("Visa Guides", "sobre o visto"),
            ("Visa Overview", "Visão geral do visto"),
            ("Visa Requirements", "Requisitos de visto"),
            ("Visa Fees", "Taxas de visto"),
            ("All Destinations", "Todos os destinos"),
            ("How to Apply for a", "Como solicitar uma"),
            ("Visa Extension", "Prorrogação de visto"),
            ("Step 1: Gather documents", "Passo 1: Recolher documentos"),
            ("Step 2: Apply at", "Passo 2: Candidatar em"),
            ("Step 3: Pay the fee", "Passo 3: Pagar a taxa"),
            ("Step 4: Wait for processing", "Passo 4: Aguardar o processamento"),
            ("Step 5: Receive your extension", "Passo 5: Receber a prorrogação"),
            ("Gather your documents", "Recolha os seus documentos"),
            ("Prepare passport, bank statements", "Prepare o passaporte, extratos bancários"),
            ("Submit your extension application", "Submeta o seu pedido de prorrogação"),
            ("Payment is required at the time", "O pagamento é necessário no momento"),
            ("Processing typically takes", "O processamento demora normalmente"),
            ("Your new authorised stay", "A sua nova estadia autorizada"),
            ("Can I extend my", "Posso prorrogar o meu"),
            ("How long does a", "Quanto tempo demora uma"),
            ("What is the fee for a", "Qual é a taxa de uma"),
            ("What happens if I overstay", "O que acontece se ficar além do prazo"),
            ("in 2026", "em 2026"),
            ("how to extend your stay, fees, required documents and overstay consequences. Complete guide.", "como prorrogar a sua estadia, taxas, documentos necessários e consequências da permanência excessiva. Guia completo."),
            ("how to extend your stay, fees, required documents and overstay consequences.", "como prorrogar a sua estadia, taxas, documentos necessários e consequências da permanência excessiva."),
            ("Editorial Team", "Equipa editorial"),
            ("This guide is maintained by our visa research team.", "Este guia é mantido pela nossa equipa de investigação de vistos."),
            ("Last updated:", "Última atualização:"),
            ("Important:", "Importante:"),
            ("Visa extension rules change frequently.", "As regras de prorrogação de visto mudam frequentemente."),
            ("Always verify current requirements at", "Verifique sempre os requisitos atuais em"),
            ("before making travel plans.", "antes de planear a sua viagem."),
            ("This page is for informational purposes only.", "Esta página destina-se apenas a fins informativos."),
            ("Warning:", "Aviso:"),
            ("Overstaying your visa or authorised stay in", "Exceder o seu visto ou estadia autorizada em"),
            ("can have serious consequences.", "pode ter consequências graves."),
            ("Apply <strong>before your current visa expires</strong>", "Candidate-se <strong>antes de o seu visto atual expirar</strong>"),
            ("to remain in legal status throughout the process.", "para permanecer em situação legal durante todo o processo."),
            ("Extension Type", "Tipo de prorrogação"),
            ("Duration", "Duração"),
            ("Where to Apply", "Onde candidatar"),
            ("Processing Time", "Tempo de processamento"),
            ("requires applying through the official immigration authority before your current visa or permitted stay expires.", "requer a candidatura junto da autoridade de imigração oficial antes de o seu visto ou estadia autorizada expirar."),
            ("This guide covers the extension process, fees, documents required and the consequences of overstaying.", "Este guia aborda o processo de prorrogação, taxas, documentos necessários e as consequências da permanência excessiva."),
            ("Yes, in most cases tourists can request a stay extension through", "Sim, na maioria dos casos os turistas podem solicitar uma prorrogação de estadia através de"),
            ("Extensions are typically processed within", "As prorrogações são normalmente processadas em"),
            ("The standard fee is", "A taxa padrão é"),
            ("You must apply before your current authorised stay expires", "Deve candidatar-se antes de a sua estadia autorizada expirar"),
            ("Valid passport (minimum 6 months validity beyond requested stay)", "Passaporte válido (mínimo 6 meses de validade além da estadia solicitada)"),
            ("Completed extension application form", "Formulário de pedido de prorrogação preenchido"),
            ("Proof of sufficient funds (recent bank statement)", "Prova de fundos suficientes (extrato bancário recente)"),
            ("Proof of accommodation", "Prova de alojamento"),
            ("Onward or return travel booking", "Reserva de viagem de ida ou regresso"),
            ("Proof of reason for extension (if required)", "Justificativo do motivo da prorrogação (se necessário)"),
            ("Application fee:", "Taxa de candidatura:"),
            ("Global eVisa &amp; Travel Information Platform", "Plataforma global de informação sobre eVisas e viagens"),
            ("Home", "Início"),
            ("Destinations", "Destinos"),
            ("About", "Sobre"),
            ("English", "English"),
            ("Toggle navigation", "Alternar navegação"),
            ("Menu", "Menu"),
        ]
    return []

def fix_lang_meta(html, lang, slug, flag):
    """Fix html lang, canonical, og:url, hreflang, active dropdown, footer links."""
    # html lang
    html = re.sub(r'<html lang="en">', f'<html lang="{lang}">', html)
    # canonical + og:url
    html = html.replace(
        f'https://www.evisa-card.com/en/{slug}-visa-extension.html',
        f'https://www.evisa-card.com/{lang}/{slug}-visa-extension.html'
    )
    # active dropdown
    html = html.replace(
        f'href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>',
        f'href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>'
    )
    # navbar brand / JS paths already use ../
    # Footer legal links
    html = html.replace('href="/en/legal-notice.html"', f'href="/{lang}/legal-notice.html"')
    html = html.replace('href="/en/disclaimer.html"', f'href="/{lang}/disclaimer.html"')
    # Navbar links
    html = html.replace('href="/en/expat-guides.html"', f'href="/{lang}/expat-guides.html"')
    # Active dropdown item
    html = html.replace(
        f'<a class="dropdown-item active" href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>',
        f'<a class="dropdown-item" href="/en/{slug}-visa-extension.html"><span class="fi fi-gb"></span> English</a>'
    )
    # Add active to correct lang
    lang_names = {"fr":"Français","es":"Español","pt":"Português"}
    flag_codes = {"fr":"fr","es":"es","pt":"br"}
    lname = lang_names.get(lang, lang)
    lflag = flag_codes.get(lang, lang)
    html = html.replace(
        f'<a class="dropdown-item" href="/{lang}/{slug}-visa-extension.html"><span class="fi fi-{lflag}"></span> {lname}</a>',
        f'<a class="dropdown-item active" href="/{lang}/{slug}-visa-extension.html"><span class="fi fi-{lflag}"></span> {lname}</a>'
    )
    # lang switcher: fr/es/pt point to their own extension page
    for l2 in ["fr","es","pt"]:
        fn2 = {"fr":"fr","es":"es","pt":"br"}[l2]
        ln2 = {"fr":"Français","es":"Español","pt":"Português"}[l2]
        html = html.replace(
            f'href="/{l2}/destination.html"><span class="fi fi-{fn2}"></span> {ln2}</a>',
            f'href="/{l2}/{slug}-visa-extension.html"><span class="fi fi-{fn2}"></span> {ln2}</a>'
        )
    # hreflang
    html = re.sub(r'[ \t]*<link[^>]+hreflang[^>]+/?>\n?', '', html)
    hreflang_block = f'''    <link rel="alternate" hreflang="en" href="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>
    <link rel="alternate" hreflang="fr" href="https://www.evisa-card.com/fr/{slug}-visa-extension.html"/>
    <link rel="alternate" hreflang="es" href="https://www.evisa-card.com/es/{slug}-visa-extension.html"/>
    <link rel="alternate" hreflang="pt" href="https://www.evisa-card.com/pt/{slug}-visa-extension.html"/>
    <link rel="alternate" hreflang="x-default" href="https://www.evisa-card.com/en/{slug}-visa-extension.html"/>'''
    html = html.replace('</head>', hreflang_block + '\n</head>', 1)
    return html

created = 0

# Find all EN extension pages
en_dir = os.path.join(BASE, "en")
for fname in os.listdir(en_dir):
    if not fname.endswith("-visa-extension.html"):
        continue
    slug = fname.replace("-visa-extension.html", "")
    en_path = os.path.join(en_dir, fname)
    with open(en_path, "r", encoding="utf-8") as f:
        en_html = f.read()

    for lang in ["fr","es","pt"]:
        out_dir = os.path.join(BASE, lang)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, fname)
        if os.path.exists(out_path):
            continue  # skip if already exists

        html = en_html
        # Apply text substitutions
        for old, new in get_subs(lang):
            html = html.replace(old, new)
        # Fix meta/lang/hreflang
        html = fix_lang_meta(html, lang, slug, FLAG_MAP[lang])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        created += 1

print(f"DONE — {created} extension pages created (FR/ES/PT)")

FLAG_MAP = {"fr":"fr","es":"es","pt":"br"}
