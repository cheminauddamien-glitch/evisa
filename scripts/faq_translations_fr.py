"""
French translations for all 48 FAQ questions and 7 category headings.
Used by gen_faq_langs.py or similar scripts to generate /fr/faq.html.
"""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "Questions g\u00e9n\u00e9rales sur les visas",
    "Schengen & European Visas": "Visas Schengen et europ\u00e9ens",
    "Documents & Application Process": "Documents et proc\u00e9dure de demande",
    "Fees & Processing Times": "Frais et d\u00e9lais de traitement",
    "Extensions, Overstay & Refusal": "Prolongations, d\u00e9passement de s\u00e9jour et refus",
    "Special Visa Types": "Types de visas sp\u00e9ciaux",
    "Embassy & Application Process": "Ambassade et proc\u00e9dure de demande",
}

FAQ_TRANSLATIONS = [
    # ── Category 1: General Visa Questions (7 questions) ──
    {
        "q_en": "What is an eVisa?",
        "q_fr": "Qu'est-ce qu'un eVisa ?",
        "a_fr": (
            "Un eVisa (visa \u00e9lectronique) est une autorisation de voyage d\u00e9livr\u00e9e "
            "num\u00e9riquement. Vous faites la demande en ligne, payez les frais et recevez "
            "l'approbation par e-mail. Aucune visite \u00e0 l'ambassade n'est n\u00e9cessaire. "
            "Des pays comme la <a href=\"/fr/visa-turkey.html\">Turquie</a>, "
            "l'<a href=\"/fr/visa-india.html\">Inde</a>, le "
            "<a href=\"/fr/visa-vietnam.html\">Vietnam</a>, le "
            "<a href=\"/fr/visa-cambodia.html\">Cambodge</a> et "
            "l'<a href=\"/fr/visa-australia.html\">Australie</a> proposent des eVisas."
        ),
    },
    {
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_fr": "Quelle est la diff\u00e9rence entre un visa et un eVisa ?",
        "a_fr": (
            "Un visa traditionnel n\u00e9cessite de se rendre \u00e0 une ambassade ou un consulat, "
            "de soumettre des documents papier et parfois de passer un entretien. Un eVisa "
            "se demande enti\u00e8rement en ligne, est trait\u00e9 plus rapidement (souvent en "
            "24 \u00e0 72 heures) et vous est envoy\u00e9 \u00e9lectroniquement par e-mail."
        ),
    },
    {
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_fr": "Qu'est-ce qu'une ETA (autorisation de voyage \u00e9lectronique) ?",
        "a_fr": (
            "Une ETA est un contr\u00f4le pr\u00e9alable au voyage pour les ressortissants "
            "de pays exempt\u00e9s de visa. Ce n'est pas un visa, mais une autorisation de "
            "voyage li\u00e9e \u00e0 votre passeport. Des pays comme "
            "l'<a href=\"/fr/visa-australia.html\">Australie</a>, le Canada, la "
            "Nouvelle-Z\u00e9lande et le Royaume-Uni utilisent le syst\u00e8me ETA. "
            "Le syst\u00e8me ETIAS de l'UE entre en vigueur en 2026."
        ),
    },
    {
        "q_en": "What is visa-free travel?",
        "q_fr": "Qu'est-ce que le voyage sans visa ?",
        "a_fr": (
            "Le voyage sans visa signifie que vous pouvez entrer dans un pays sans demander "
            "de visa au pr\u00e9alable. Vous pr\u00e9sentez simplement votre passeport \u00e0 "
            "l'immigration. La dur\u00e9e de s\u00e9jour autoris\u00e9e est g\u00e9n\u00e9ralement "
            "de 30 \u00e0 90 jours. Les passeports les plus puissants (Japon, Singapour, UE) "
            "offrent un acc\u00e8s sans visa \u00e0 plus de 190 pays."
        ),
    },
    {
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_fr": "Qu'est-ce qu'un visa \u00e0 l'arriv\u00e9e (VOA) ?",
        "a_fr": (
            "Un visa \u00e0 l'arriv\u00e9e est d\u00e9livr\u00e9 au point d'entr\u00e9e "
            "(a\u00e9roport ou poste fronti\u00e8re) sans demande pr\u00e9alable. Vous "
            "pr\u00e9sentez votre passeport, remplissez un formulaire, payez les frais et "
            "recevez le tampon de visa. Des pays comme "
            "l'<a href=\"/fr/visa-indonesia.html\">Indon\u00e9sie</a>, le "
            "<a href=\"/fr/visa-nepal.html\">N\u00e9pal</a> et la "
            "<a href=\"/fr/visa-jordan.html\">Jordanie</a> proposent le VOA pour de "
            "nombreuses nationalit\u00e9s."
        ),
    },
    {
        "q_en": "How do I check if I need a visa?",
        "q_fr": "Comment savoir si j'ai besoin d'un visa ?",
        "a_fr": (
            "Les exigences en mati\u00e8re de visa d\u00e9pendent de votre nationalit\u00e9 "
            "et de votre destination. Utilisez notre <a href=\"/fr/index.html\">outil de "
            "recherche de visas</a> sur la page d'accueil ou consultez la "
            "<a href=\"/fr/destination.html\">page du pays</a> concern\u00e9. En g\u00e9n\u00e9ral, "
            "les citoyens des pays \u00e0 passeport fort (UE, \u00c9tats-Unis, Royaume-Uni, "
            "Japon) b\u00e9n\u00e9ficient d'un acc\u00e8s sans visa dans plus de 150 pays."
        ),
    },
    {
        "q_en": "What is the strongest passport in the world?",
        "q_fr": "Quel est le passeport le plus puissant au monde ?",
        "a_fr": (
            "En 2026, le Japon, Singapour et plusieurs passeports europ\u00e9ens se classent "
            "r\u00e9guli\u00e8rement parmi les plus puissants, offrant un acc\u00e8s sans visa "
            "ou avec visa \u00e0 l'arriv\u00e9e dans plus de 190 pays. Le Henley Passport Index "
            "et l'Arton Capital Index classent les passeports chaque trimestre en fonction de "
            "la libert\u00e9 de d\u00e9placement."
        ),
    },
    # ── Category 2: Schengen & European Visas (6 questions) ──
    {
        "q_en": "What is a Schengen visa?",
        "q_fr": "Qu'est-ce qu'un visa Schengen ?",
        "a_fr": (
            "Un visa Schengen permet de voyager dans 27 pays europ\u00e9ens avec un seul visa. "
            "Il est valable pour des s\u00e9jours de courte dur\u00e9e de 90 jours maximum sur "
            "toute p\u00e9riode de 180 jours. Vous devez d\u00e9poser votre demande aupr\u00e8s de "
            "l'ambassade du pays o\u00f9 vous s\u00e9journerez le plus longtemps (ou du premier "
            "pays d'entr\u00e9e). Consultez nos pages visas pour la "
            "<a href=\"/fr/visa-france.html\">France</a>, "
            "l'<a href=\"/fr/visa-germany.html\">Allemagne</a>, "
            "l'<a href=\"/fr/visa-spain.html\">Espagne</a> et "
            "l'<a href=\"/fr/visa-italy.html\">Italie</a>."
        ),
    },
    {
        "q_en": "How many countries are in the Schengen Area?",
        "q_fr": "Combien de pays font partie de l'espace Schengen ?",
        "a_fr": (
            "En 2026, l'espace Schengen comprend 27 pays\u00a0: Autriche, Belgique, Croatie, "
            "R\u00e9publique tch\u00e8que, Danemark, Estonie, Finlande, France, Allemagne, "
            "Gr\u00e8ce, Hongrie, Islande, Italie, Lettonie, Liechtenstein, Lituanie, "
            "Luxembourg, Malte, Pays-Bas, Norv\u00e8ge, Pologne, Portugal, Roumanie, "
            "Slovaquie, Slov\u00e9nie, Espagne, Su\u00e8de et Suisse."
        ),
    },
    {
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_fr": "Puis-je visiter plusieurs pays Schengen avec un seul visa ?",
        "a_fr": (
            "Oui. Un visa Schengen permet la libre circulation dans les 27 pays Schengen "
            "pendant votre s\u00e9jour autoris\u00e9 (jusqu'\u00e0 90 jours sur 180 jours). "
            "Vous devez d\u00e9poser votre demande aupr\u00e8s de l'ambassade de votre "
            "destination principale ou du premier pays d'entr\u00e9e."
        ),
    },
    {
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_fr": "Qu'est-ce que la r\u00e8gle des 90/180 jours pour Schengen ?",
        "a_fr": (
            "La r\u00e8gle 90/180 signifie que vous pouvez s\u00e9journer dans l'espace "
            "Schengen pendant 90 jours maximum sur toute p\u00e9riode de 180 jours. Ce "
            "calcul se fait sur une base glissante. Une fois vos 90 jours utilis\u00e9s, "
            "vous devez quitter l'espace Schengen et attendre que suffisamment de jours "
            "aient \u00ab\u00a0expir\u00e9\u00a0\u00bb avant de pouvoir y revenir."
        ),
    },
    {
        "q_en": "What is ETIAS and when does it start?",
        "q_fr": "Qu'est-ce que l'ETIAS et quand entre-t-il en vigueur ?",
        "a_fr": (
            "L'ETIAS (syst\u00e8me europ\u00e9en d'information et d'autorisation de voyage) "
            "est une nouvelle autorisation pr\u00e9alable au voyage pour les voyageurs "
            "exempt\u00e9s de visa se rendant dans l'espace Schengen. Il entre en vigueur "
            "en 2026. Les citoyens de plus de 60 pays (\u00c9tats-Unis, Royaume-Uni, Canada, "
            "Australie, Japon) devront obtenir une autorisation ETIAS (7\u00a0EUR, valable "
            "3\u00a0ans) avant de voyager en Europe."
        ),
    },
    {
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_fr": "Puis-je entrer dans un pays Schengen diff\u00e9rent de celui qui a d\u00e9livr\u00e9 mon visa ?",
        "a_fr": (
            "Oui, mais votre visa Schengen doit \u00eatre d\u00e9livr\u00e9 par le pays de "
            "votre destination principale (s\u00e9jour le plus long). Si vous entrez par un "
            "autre pays, l'immigration peut vous interroger sur votre itin\u00e9raire. Si "
            "tous les s\u00e9jours sont \u00e9gaux, d\u00e9posez votre demande aupr\u00e8s du "
            "pays de premi\u00e8re entr\u00e9e."
        ),
    },
    # ── Category 3: Documents & Application Process (9 questions) ──
    {
        "q_en": "What documents do I need for a visa application?",
        "q_fr": "Quels documents faut-il pour une demande de visa ?",
        "a_fr": (
            "Les documents couramment demand\u00e9s sont\u00a0: passeport valide (6\u00a0mois "
            "minimum), photos d'identit\u00e9, formulaire de demande rempli, itin\u00e9raire "
            "de voyage, r\u00e9servation d'h\u00f4tel, justificatifs de moyens financiers "
            "(relev\u00e9s bancaires), assurance voyage et lettre d'invitation (le cas "
            "\u00e9ch\u00e9ant). Consultez notre <a href=\"/fr/visa-documents-checklist.html\">"
            "liste de documents</a>."
        ),
    },
    {
        "q_en": "What size photo is needed for a visa?",
        "q_fr": "Quel format de photo est requis pour un visa ?",
        "a_fr": (
            "La plupart des pays exigent des photos de 35\u00d745\u00a0mm sur fond blanc. "
            "Les \u00c9tats-Unis exigent 51\u00d751\u00a0mm (2\u00d72\u00a0pouces). Les photos "
            "doivent \u00eatre r\u00e9centes (moins de 6\u00a0mois), avec une expression "
            "neutre et r\u00e9pondre \u00e0 des exigences pr\u00e9cises d'\u00e9clairage. "
            "Consultez notre <a href=\"/fr/visa-photo-requirements.html\">guide des "
            "exigences photo</a>."
        ),
    },
    {
        "q_en": "Do I need travel insurance for a visa?",
        "q_fr": "Ai-je besoin d'une assurance voyage pour un visa ?",
        "a_fr": (
            "Oui, pour les visas Schengen, vous devez disposer d'une assurance voyage avec "
            "une couverture minimale de 30\u00a0000\u00a0EUR. De nombreux autres pays l'exigent "
            "\u00e9galement ou la recommandent fortement. Consultez notre "
            "<a href=\"/fr/travel-insurance-for-visa-applications.html\">guide de l'assurance "
            "voyage</a>."
        ),
    },
    {
        "q_en": "How long must my passport be valid for travel?",
        "q_fr": "Quelle doit \u00eatre la dur\u00e9e de validit\u00e9 de mon passeport pour voyager ?",
        "a_fr": (
            "La plupart des pays exigent que votre passeport soit valide au moins 6\u00a0mois "
            "apr\u00e8s votre s\u00e9jour pr\u00e9vu. Les pays Schengen exigent 3\u00a0mois "
            "apr\u00e8s votre date de d\u00e9part, plus deux pages vierges. V\u00e9rifiez "
            "toujours les exigences sp\u00e9cifiques du pays."
        ),
    },
    {
        "q_en": "Can I apply for a visa if my passport expires soon?",
        "q_fr": "Puis-je demander un visa si mon passeport expire bient\u00f4t ?",
        "a_fr": (
            "En g\u00e9n\u00e9ral, non. La plupart des pays exigent une validit\u00e9 du "
            "passeport d'au moins 6\u00a0mois. Si votre passeport expire dans moins de "
            "6\u00a0mois, renouvelez-le avant de d\u00e9poser votre demande de visa. "
            "Certains pays exigent \u00e9galement des pages vierges pour la vignette "
            "visa (g\u00e9n\u00e9ralement 2\u00a0pages vierges)."
        ),
    },
    {
        "q_en": "What bank statement amount do I need for a visa?",
        "q_fr": "Quel montant de relev\u00e9 bancaire faut-il pour un visa ?",
        "a_fr": (
            "Pour les visas Schengen, pr\u00e9voyez 50 \u00e0 100\u00a0EUR par jour de "
            "s\u00e9jour. Pour le visa B1/B2 am\u00e9ricain, il faut d\u00e9montrer des "
            "fonds suffisants (pas de montant fixe). Pour le Royaume-Uni, pr\u00e9sentez "
            "3 \u00e0 6\u00a0mois de revenus r\u00e9guliers. En r\u00e8gle g\u00e9n\u00e9rale, "
            "montrez un solde couvrant les frais de voyage plus 30 \u00e0 50\u00a0% de marge."
        ),
    },
    {
        "q_en": "Is a hotel booking required for a visa application?",
        "q_fr": "Une r\u00e9servation d'h\u00f4tel est-elle obligatoire pour une demande de visa ?",
        "a_fr": (
            "La plupart des demandes de visa exigent une preuve d'h\u00e9bergement pour "
            "toute la dur\u00e9e du s\u00e9jour. Il peut s'agir d'une r\u00e9servation "
            "d'h\u00f4tel (pas forc\u00e9ment pr\u00e9pay\u00e9e), d'une r\u00e9servation "
            "Airbnb ou d'une lettre de votre h\u00f4te. Pour les visas Schengen, toutes "
            "les nuit\u00e9es doivent \u00eatre couvertes."
        ),
    },
    {
        "q_en": "Do I need a return ticket to get a visa?",
        "q_fr": "Ai-je besoin d'un billet retour pour obtenir un visa ?",
        "a_fr": (
            "La plupart des pays exigent une preuve de voyage de retour ou de continuation "
            "pour les demandes de visa et \u00e0 l'immigration. Il peut s'agir d'une "
            "r\u00e9servation de vol confirm\u00e9e, d'un billet de bus ou de ferry "
            "montrant que vous pr\u00e9voyez de quitter le pays avant l'expiration de "
            "votre visa."
        ),
    },
    {
        "q_en": "What is an invitation letter for a visa?",
        "q_fr": "Qu'est-ce qu'une lettre d'invitation pour un visa ?",
        "a_fr": (
            "Une lettre d'invitation est un document r\u00e9dig\u00e9 par une personne ou "
            "une organisation dans le pays de destination vous invitant \u00e0 venir. Elle "
            "contient les coordonn\u00e9es de l'h\u00f4te, votre lien, l'objet et les dates "
            "du s\u00e9jour, les modalit\u00e9s d'h\u00e9bergement et la prise en charge "
            "financi\u00e8re. Elle est requise pour de nombreuses demandes de visa Schengen "
            "et de visa d'affaires."
        ),
    },
    {
        "q_en": "What are biometrics for a visa?",
        "q_fr": "Qu'est-ce que la biom\u00e9trie pour un visa ?",
        "a_fr": (
            "La biom\u00e9trie comprend la prise d'empreintes digitales et une photo "
            "num\u00e9rique collect\u00e9es lors de votre demande de visa. Les pays "
            "Schengen, le Royaume-Uni, les \u00c9tats-Unis, le Canada et de nombreux "
            "autres pays l'exigent. Les donn\u00e9es sont conserv\u00e9es pour la "
            "v\u00e9rification d'identit\u00e9 et sont g\u00e9n\u00e9ralement valables "
            "5\u00a0ans."
        ),
    },
    # ── Category 4: Fees & Processing Times (6 questions) ──
    {
        "q_en": "How much does a visa cost?",
        "q_fr": "Combien co\u00fbte un visa ?",
        "a_fr": (
            "Les frais de visa varient consid\u00e9rablement. Exemples\u00a0: visa Schengen "
            "80\u00a0EUR, visa B1/B2 am\u00e9ricain 185\u00a0USD, eVisa Inde 25-80\u00a0USD, "
            "eVisa Turquie 50\u00a0USD, ETA Australie 20\u00a0AUD, eVisa Cambodge 36\u00a0USD. "
            "Les enfants et certaines nationalit\u00e9s peuvent b\u00e9n\u00e9ficier de "
            "tarifs r\u00e9duits. Voir notre page "
            "<a href=\"/fr/visa-processing-times.html\">d\u00e9lais de traitement</a>."
        ),
    },
    {
        "q_en": "How long does visa processing take?",
        "q_fr": "Combien de temps prend le traitement d'un visa ?",
        "a_fr": (
            "Les eVisas sont g\u00e9n\u00e9ralement trait\u00e9s en 24 \u00e0 72\u00a0heures. "
            "Les visas Schengen prennent 15 \u00e0 45\u00a0jours calendaires. Les visas "
            "B1/B2 am\u00e9ricains peuvent prendre des semaines \u00e0 des mois selon "
            "l'ambassade. D\u00e9posez toujours votre demande bien avant votre date de "
            "d\u00e9part."
        ),
    },
    {
        "q_en": "How far in advance should I apply for a visa?",
        "q_fr": "Combien de temps \u00e0 l'avance dois-je d\u00e9poser ma demande de visa ?",
        "a_fr": (
            "Pour les eVisas\u00a0: 1 \u00e0 2\u00a0semaines avant le voyage. Pour les visas "
            "Schengen\u00a0: 3 \u00e0 6\u00a0mois \u00e0 l'avance (au plus t\u00f4t 6\u00a0mois, "
            "au plus tard 15\u00a0jours avant le d\u00e9part). Pour les visas am\u00e9ricains\u00a0: "
            "3 \u00e0 6\u00a0mois ou plus en raison des d\u00e9lais d'attente. Les p\u00e9riodes "
            "de forte affluence touristique peuvent n\u00e9cessiter des demandes encore plus "
            "anticip\u00e9es."
        ),
    },
    {
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_fr": "Puis-je \u00eatre rembours\u00e9 si ma demande de visa est refus\u00e9e ?",
        "a_fr": (
            "Dans la plupart des cas, les frais de visa ne sont pas remboursables, quel "
            "que soit le r\u00e9sultat. Les frais couvrent le co\u00fbt du traitement de "
            "votre demande et ne garantissent pas l'obtention du visa."
        ),
    },
    {
        "q_en": "How do I track my visa application status?",
        "q_fr": "Comment suivre l'\u00e9tat de ma demande de visa ?",
        "a_fr": (
            "La plupart des ambassades et des centres VFS Global proposent un suivi en "
            "ligne. Vous recevez un num\u00e9ro de r\u00e9f\u00e9rence lors du d\u00e9p\u00f4t "
            "de votre dossier. Saisissez ce num\u00e9ro sur le site de l'ambassade ou de VFS "
            "pour v\u00e9rifier l'\u00e9tat d'avancement. Certains pays envoient \u00e9galement "
            "des notifications par e-mail ou SMS \u00e0 chaque \u00e9tape."
        ),
    },
    {
        "q_en": "What is VFS Global?",
        "q_fr": "Qu'est-ce que VFS Global ?",
        "a_fr": (
            "VFS Global est une entreprise priv\u00e9e qui traite les demandes de visa "
            "pour le compte de gouvernements. Elle g\u00e8re des centres de demande de "
            "visa (VAC) dans le monde entier. Vous d\u00e9posez vos documents dans un "
            "centre VFS au lieu de vous rendre directement \u00e0 l'ambassade. VFS "
            "facture des frais de service en plus des frais de visa."
        ),
    },
    # ── Category 5: Extensions, Overstay & Refusal (4 questions) ──
    {
        "q_en": "Can I extend my visa?",
        "q_fr": "Puis-je prolonger mon visa ?",
        "a_fr": (
            "Cela d\u00e9pend du pays et du type de visa. Certains pays autorisent les "
            "prolongations (par exemple, le VOA indon\u00e9sien peut \u00eatre prolong\u00e9 "
            "de 30\u00a0jours, le visa touristique tha\u00eflandais de 30\u00a0jours). Les "
            "visas Schengen ne peuvent \u00eatre prolong\u00e9s que dans des circonstances "
            "exceptionnelles. Consultez notre page "
            "<a href=\"/fr/visa-rejection-reasons.html\">motifs de refus de visa</a> pour "
            "plus d'informations."
        ),
    },
    {
        "q_en": "What happens if my visa is refused?",
        "q_fr": "Que se passe-t-il si mon visa est refus\u00e9 ?",
        "a_fr": (
            "Vous recevrez une notification \u00e9crite indiquant le motif du refus. Les "
            "raisons courantes sont\u00a0: preuves financi\u00e8res insuffisantes, documents "
            "incomplets ou soup\u00e7on d'intention migratoire. Vous pouvez g\u00e9n\u00e9ralement "
            "faire appel dans un d\u00e9lai de 1 \u00e0 3\u00a0mois ou d\u00e9poser une "
            "nouvelle demande avec un dossier am\u00e9lior\u00e9."
        ),
    },
    {
        "q_en": "What is overstaying a visa?",
        "q_fr": "Qu'est-ce que le d\u00e9passement de la dur\u00e9e de s\u00e9jour d'un visa ?",
        "a_fr": (
            "Le d\u00e9passement de s\u00e9jour signifie rester dans un pays au-del\u00e0 "
            "de la dur\u00e9e autoris\u00e9e. Les cons\u00e9quences comprennent des amendes "
            "(par exemple, la Tha\u00eflande facture 500\u00a0THB/jour), l'expulsion, "
            "la d\u00e9tention, des interdictions d'entr\u00e9e (1 \u00e0 10\u00a0ans) et des "
            "difficult\u00e9s \u00e0 obtenir de futurs visas. Respectez toujours les dates "
            "de validit\u00e9 de votre visa."
        ),
    },
    {
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_fr": "Que faire si je perds mon passeport contenant un visa valide ?",
        "a_fr": (
            "Contactez imm\u00e9diatement l'ambassade de votre pays la plus proche pour "
            "obtenir un document de voyage d'urgence. Vous devrez demander un nouveau visa, "
            "car les visas contenus dans des passeports perdus sont consid\u00e9r\u00e9s "
            "comme nuls. D\u00e9posez un rapport de police et conservez-en une copie pour "
            "la nouvelle demande."
        ),
    },
    # ── Category 6: Special Visa Types (10 questions) ──
    {
        "q_en": "What is a transit visa?",
        "q_fr": "Qu'est-ce qu'un visa de transit ?",
        "a_fr": (
            "Un visa de transit vous autorise \u00e0 traverser un pays pour rejoindre votre "
            "destination finale. Il est g\u00e9n\u00e9ralement valable 24 \u00e0 72\u00a0heures. "
            "Certains pays exigent un visa de transit m\u00eame si vous ne quittez pas "
            "l'a\u00e9roport."
        ),
    },
    {
        "q_en": "Can I work on a tourist visa?",
        "q_fr": "Puis-je travailler avec un visa touristique ?",
        "a_fr": (
            "Non. Les visas touristiques n'autorisent g\u00e9n\u00e9ralement pas l'emploi. "
            "Travailler avec un visa touristique est ill\u00e9gal dans la plupart des pays "
            "et peut entra\u00eener l'expulsion, des amendes et le refus de futurs visas. "
            "Vous avez besoin d'un visa de travail ou d'un permis de travail sp\u00e9cifique."
        ),
    },
    {
        "q_en": "What is a digital nomad visa?",
        "q_fr": "Qu'est-ce qu'un visa pour nomade num\u00e9rique ?",
        "a_fr": (
            "Un visa pour nomade num\u00e9rique permet aux travailleurs \u00e0 distance de "
            "vivre dans un pays tout en travaillant pour des employeurs ou des clients \u00e0 "
            "l'\u00e9tranger. Les pays populaires incluent le "
            "<a href=\"/fr/visa-portugal.html\">Portugal</a>, "
            "l'<a href=\"/fr/visa-spain.html\">Espagne</a>, la "
            "<a href=\"/fr/visa-thailand.html\">Tha\u00eflande</a>, la "
            "<a href=\"/fr/visa-colombia.html\">Colombie</a> et "
            "l'<a href=\"/fr/visa-indonesia.html\">Indon\u00e9sie</a>. Consultez notre "
            "<a href=\"/fr/digital-nomad-visas-guide.html\">guide des visas nomade "
            "num\u00e9rique</a>."
        ),
    },
    {
        "q_en": "What is a student visa?",
        "q_fr": "Qu'est-ce qu'un visa \u00e9tudiant ?",
        "a_fr": (
            "Un visa \u00e9tudiant vous permet d'\u00e9tudier dans un \u00e9tablissement "
            "d'enseignement \u00e0 l'\u00e9tranger. Les conditions comprennent une lettre "
            "d'acceptation, un justificatif de paiement des frais de scolarit\u00e9 ou une "
            "bourse, des moyens financiers pour les frais de s\u00e9jour, une assurance "
            "maladie et parfois des certificats de comp\u00e9tence linguistique."
        ),
    },
    {
        "q_en": "What is a Working Holiday Visa?",
        "q_fr": "Qu'est-ce qu'un visa vacances-travail (PVT) ?",
        "a_fr": (
            "Un visa vacances-travail (PVT) permet aux jeunes (g\u00e9n\u00e9ralement de "
            "18 \u00e0 30 ou 18 \u00e0 35\u00a0ans) de voyager et de travailler dans un "
            "autre pays pendant 1 \u00e0 2\u00a0ans. Les programmes les plus populaires "
            "concernent l'<a href=\"/fr/visa-australia.html\">Australie</a>, la "
            "<a href=\"/fr/visa-new-zealand.html\">Nouvelle-Z\u00e9lande</a>, le "
            "<a href=\"/fr/visa-canada.html\">Canada</a> et le "
            "<a href=\"/fr/visa-japan.html\">Japon</a>."
        ),
    },
    {
        "q_en": "What is a Golden Visa?",
        "q_fr": "Qu'est-ce qu'un Golden Visa ?",
        "a_fr": (
            "Un Golden Visa est un permis de s\u00e9jour accord\u00e9 aux investisseurs "
            "r\u00e9alisant un investissement financier important (g\u00e9n\u00e9ralement "
            "immobilier ou commercial). Des programmes populaires existent au "
            "<a href=\"/fr/visa-portugal.html\">Portugal</a>, en "
            "<a href=\"/fr/visa-spain.html\">Espagne</a>, en "
            "<a href=\"/fr/visa-greece.html\">Gr\u00e8ce</a> et aux "
            "<a href=\"/fr/visa-uae.html\">\u00c9mirats arabes unis</a>. Les investissements "
            "vont de 250\u00a0000 \u00e0 plus de 500\u00a0000\u00a0EUR."
        ),
    },
    {
        "q_en": "What is a long-stay visa (Type D)?",
        "q_fr": "Qu'est-ce qu'un visa de long s\u00e9jour (type D) ?",
        "a_fr": (
            "Un visa de type D (visa national) autorise des s\u00e9jours de plus de "
            "90\u00a0jours dans un pays donn\u00e9. Contrairement au visa Schengen de "
            "court s\u00e9jour (type C), le visa de type D est d\u00e9livr\u00e9 par "
            "chaque pays pour des motifs tels que les \u00e9tudes, le travail, le "
            "regroupement familial ou la retraite."
        ),
    },
    {
        "q_en": "What is a multiple-entry visa?",
        "q_fr": "Qu'est-ce qu'un visa \u00e0 entr\u00e9es multiples ?",
        "a_fr": (
            "Un visa \u00e0 entr\u00e9es multiples vous permet d'entrer et de sortir d'un "
            "pays plusieurs fois pendant la p\u00e9riode de validit\u00e9 du visa. C'est "
            "particuli\u00e8rement utile pour les voyageurs d'affaires ou les personnes "
            "visitant les pays voisins. Les visas \u00e0 entr\u00e9e unique deviennent "
            "invalides d\u00e8s que vous quittez le pays."
        ),
    },
    {
        "q_en": "Do children need their own visa?",
        "q_fr": "Les enfants ont-ils besoin de leur propre visa ?",
        "a_fr": (
            "Oui, les enfants ont besoin de leur propre visa dans la plupart des cas, "
            "y compris les nourrissons. Certains pays offrent des tarifs r\u00e9duits pour "
            "les enfants de moins de 6 ou 12\u00a0ans. Les enfants doivent avoir leur propre "
            "passeport pour la plupart des voyages internationaux."
        ),
    },
    {
        "q_en": "Can dual citizens use either passport for visas?",
        "q_fr": "Les binationaux peuvent-ils utiliser l'un ou l'autre de leurs passeports ?",
        "a_fr": (
            "Oui, les binationaux peuvent choisir le passeport \u00e0 utiliser. Utilisez "
            "celui qui offre les meilleures conditions de visa. Entrez et sortez toujours "
            "d'un pays avec le m\u00eame passeport. Certains pays ne reconnaissent pas la "
            "double nationalit\u00e9 \u2014 v\u00e9rifiez la l\u00e9gislation de vos deux pays."
        ),
    },
    # ── Category 7: Embassy & Application Process (5 questions) ──
    {
        "q_en": "How do I apply for a visa at an embassy?",
        "q_fr": "Comment faire une demande de visa aupr\u00e8s d'une ambassade ?",
        "a_fr": (
            "\u00c9tapes\u00a0: 1) V\u00e9rifiez les conditions sur le site de l'ambassade. "
            "2) Rassemblez les documents. 3) Prenez rendez-vous. 4) Pr\u00e9sentez-vous et "
            "d\u00e9posez les documents. 5) Payez les frais. 6) Attendez le traitement. "
            "7) R\u00e9cup\u00e9rez votre passeport avec le visa. Consultez notre "
            "<a href=\"/fr/how-to-apply-evisa.html\">guide de demande</a>."
        ),
    },
    {
        "q_en": "What is a visa interview?",
        "q_fr": "Qu'est-ce qu'un entretien de visa ?",
        "a_fr": (
            "Certains pays (notamment les \u00c9tats-Unis, le Royaume-Uni et le Canada) "
            "exigent un entretien en personne \u00e0 l'ambassade. L'agent consulaire vous "
            "posera des questions sur vos projets de voyage, vos attaches dans votre pays "
            "d'origine, votre situation financi\u00e8re et le but de votre visite. Soyez "
            "honn\u00eate et apportez les documents justificatifs."
        ),
    },
    {
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_fr": "Puis-je demander un visa depuis un pays dont je ne suis pas citoyen ?",
        "a_fr": (
            "Oui, dans de nombreux cas, vous pouvez d\u00e9poser votre demande aupr\u00e8s "
            "de l'ambassade d'un pays o\u00f9 vous avez la r\u00e9sidence l\u00e9gale. Vous "
            "devrez fournir une preuve de r\u00e9sidence l\u00e9gale (titre de s\u00e9jour, "
            "visa de long s\u00e9jour). Certains pays n'acceptent les demandes que de la "
            "part des citoyens ou r\u00e9sidents permanents du pays h\u00f4te."
        ),
    },
    {
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_fr": "Quelle diff\u00e9rence entre vignette visa, tampon et e-visa ?",
        "a_fr": (
            "Une vignette visa est une \u00e9tiquette physique coll\u00e9e sur une page du "
            "passeport (Schengen, \u00c9tats-Unis, Royaume-Uni). Un tampon est une marque "
            "d'entr\u00e9e/sortie appos\u00e9e par l'immigration. Un e-visa est une "
            "autorisation num\u00e9rique li\u00e9e \u00e0 votre num\u00e9ro de passeport "
            "\u2014 aucune vignette physique n'est n\u00e9cessaire."
        ),
    },
    {
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_fr": "Puis-je voyager avec un visa dans un passeport annul\u00e9 ?",
        "a_fr": (
            "Dans certains cas, oui, si le visa est toujours valide. Des pays comme les "
            "\u00c9tats-Unis et le Royaume-Uni vous autorisent \u00e0 voyager avec un visa "
            "valide dans un ancien passeport accompagn\u00e9 de votre nouveau passeport. "
            "V\u00e9rifiez les r\u00e8gles sp\u00e9cifiques de chaque pays, car certains "
            "exigent le transfert du visa sur le nouveau passeport."
        ),
    },
]
