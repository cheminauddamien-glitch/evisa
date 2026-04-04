#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create proper home pages for all 9 language directories,
mirroring www/index.html (the EN home) with language-specific content.
"""

import re, os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www"
ROOT_INDEX = os.path.join(BASE, "index.html")

with open(ROOT_INDEX, encoding="utf-8") as f:
    EN_HTML = f.read()

# Per-language configuration
LANGS = {
    "fr": {
        "html_lang": "fr",
        "lang_label": '<span class="fi fi-fr"></span> Francais',
        "title": "eVisa-Card.com — Informations eVisa mondiales - Guide de voyage",
        "meta_desc": "eVisa-Card.com fournit des informations officielles sur les eVisa pour les voyageurs du monde entier. Decouvrez les types de visa, les demandes en ligne, les conditions, les frais et les delais de traitement par pays.",
        "canonical": "https://www.evisa-card.com/fr/",
        "og_title": "eVisa-Card.com — Informations eVisa mondiales - Guide de voyage",
        "og_desc": "Guide officiel des eVisa et autorisations de voyage pour les principales destinations touristiques.",
        "nav_home": "Accueil",
        "nav_dest": "Destinations",
        "nav_about": "A propos",
        "nav_guides": "Guides",
        "hero_h1": "eVisa-Card.com — Votre guide mondial d'eVisa &amp; d'autorisation de voyage",
        "hero_p": "Trouvez les informations officielles sur les eVisa pour chaque pays. Decouvrez les types de visa, les conditions, les demarches en ligne, les frais et les delais de traitement pour le tourisme et les affaires.",
        "btn_asia": "Explorer l'Asie",
        "btn_europe": "Explorer l'Europe",
        "btn_americas": "Explorer les Ameriques",
        "btn_oceania": "Explorer l'Oceanie",
        "section_asia": "Asie",
        "desc_asia": "Trouvez les types d'eVisa, durees, frais, liens officiels et conseils pour les principales destinations touristiques asiatiques. Chaque page pays contient les conditions, frais, liens et etapes pour postuler en ligne.",
        "section_europe": "Europe",
        "desc_europe": "Informations sur les visas Schengen, eVisa et autorisation de voyage pour l'Europe. Consultez les conditions, delais de traitement et guichets officiels pour les voyageurs hors UE.",
        "section_americas": "Amerique du Nord et du Sud",
        "desc_americas": "Decouvrez les options de visa et eVisa pour les principaux pays d'Amerique du Nord et du Sud. Consultez les conditions, portails officiels, durees de sejour et programmes comme eTA et ESTA.",
        "section_oceania": "Oceanie",
        "desc_oceania": "Informations sur les visas et eVisitor pour l'Oceanie. Consultez les conditions eVisitor, eTA ou visa pour l'Australie et la Nouvelle-Zelande.",
        "faq_title": "Questions frequentes — eVisa &amp; Autorisations de voyage",
        "faq_q1": "Ai-je besoin d'un eVisa pour voyager ?",
        "faq_a1": "Les regles de visa dependent de votre nationalite et de votre destination. De nombreux pays autorisent l'entree sans visa, d'autres exigent une autorisation en ligne ou un visa ambassade.",
        "faq_q2": "Combien de temps prend l'approbation d'un eVisa ?",
        "faq_a2": "Le delai d'approbation varie generalement de quelques heures a plusieurs jours selon la destination et le volume de demandes.",
        "faq_q3": "Quels documents sont necessaires pour un visa en ligne ?",
        "faq_a3": "En general : passeport valide, photo recente, details du voyage et moyen de paiement pour les frais de visa.",
        "footer_copy": "© 2026 eVisa-Card.com — Plateforme mondiale d'information sur les eVisa &amp; voyages",
        "legal": "Mentions legales",
        "disclaimer": "Avertissement",
    },
    "es": {
        "html_lang": "es",
        "lang_label": '<span class="fi fi-es"></span> Espanol',
        "title": "eVisa-Card.com — Informacion global sobre eVisa - Guia de viaje",
        "meta_desc": "eVisa-Card.com ofrece informacion oficial sobre eVisa para viajeros de todo el mundo. Descubra tipos de visa, solicitudes en linea, requisitos, tarifas y tiempos de tramitacion por pais.",
        "canonical": "https://www.evisa-card.com/es/",
        "og_title": "eVisa-Card.com — Informacion global sobre eVisa - Guia de viaje",
        "og_desc": "Guia oficial de eVisa y autorizaciones de viaje para los principales destinos turisticos.",
        "nav_home": "Inicio",
        "nav_dest": "Destinos",
        "nav_about": "Acerca de",
        "nav_guides": "Guias",
        "hero_h1": "eVisa-Card.com — Su guia global de eVisa &amp; autorizacion de viaje",
        "hero_p": "Encuentre informacion oficial sobre eVisa para todos los paises. Conozca los tipos de visa, requisitos, pasos de solicitud en linea, tarifas y tiempos de tramitacion para turismo y negocios.",
        "btn_asia": "Explorar Asia",
        "btn_europe": "Explorar Europa",
        "btn_americas": "Explorar America",
        "btn_oceania": "Explorar Oceania",
        "section_asia": "Asia",
        "desc_asia": "Encuentre tipos de eVisa, duraciones, tarifas, enlaces oficiales y orientacion para solicitar en linea en los principales destinos turisticos asiaticos.",
        "section_europe": "Europa",
        "desc_europe": "Informacion sobre visas Schengen, eVisa y autorizaciones de viaje para Europa. Consulte los requisitos, tiempos de tramitacion y portales oficiales.",
        "section_americas": "America del Norte y del Sur",
        "desc_americas": "Explore las opciones de visa y eVisa para los principales paises de America. Encuentre requisitos, portales oficiales, duraciones de estancia y programas como eTA y ESTA.",
        "section_oceania": "Oceania",
        "desc_oceania": "Informacion de visa y eVisitor para Oceania. Consulte los requisitos de eVisitor, eTA o visa para Australia y Nueva Zelanda.",
        "faq_title": "Preguntas frecuentes — eVisa &amp; Autorizaciones de viaje",
        "faq_q1": "Necesito un eVisa para viajar?",
        "faq_a1": "Las reglas de visa dependen de su nacionalidad y destino. Muchos paises permiten la entrada sin visa, mientras que otros exigen una autorizacion en linea o visa de embajada.",
        "faq_q2": "Cuanto tarda la aprobacion de un eVisa?",
        "faq_a2": "El tiempo de aprobacion generalmente oscila entre unas pocas horas y varios dias segun el destino y el volumen de solicitudes.",
        "faq_q3": "Que documentos se necesitan para un visa en linea?",
        "faq_a3": "Normalmente: pasaporte valido, foto reciente, detalles del viaje y un metodo de pago para las tarifas de visa.",
        "footer_copy": "© 2026 eVisa-Card.com — Plataforma mundial de informacion sobre eVisa &amp; viajes",
        "legal": "Aviso legal",
        "disclaimer": "Descargo de responsabilidad",
    },
    "pt": {
        "html_lang": "pt",
        "lang_label": '<span class="fi fi-br"></span> Portugues',
        "title": "eVisa-Card.com — Informacoes globais sobre eVisa - Guia de viagem",
        "meta_desc": "eVisa-Card.com fornece informacoes oficiais sobre eVisa para viajantes do mundo inteiro. Descubra tipos de visto, solicitacoes online, requisitos, taxas e prazos de processamento por pais.",
        "canonical": "https://www.evisa-card.com/pt/",
        "og_title": "eVisa-Card.com — Informacoes globais sobre eVisa - Guia de viagem",
        "og_desc": "Guia oficial de eVisa e autorizacoes de viagem para os principais destinos turisticos.",
        "nav_home": "Inicio",
        "nav_dest": "Destinos",
        "nav_about": "Sobre",
        "nav_guides": "Guias",
        "hero_h1": "eVisa-Card.com — Seu guia global de eVisa &amp; autorizacao de viagem",
        "hero_p": "Encontre informacoes oficiais sobre eVisa para todos os paises. Saiba sobre tipos de visto, requisitos, etapas de solicitacao online, taxas e prazos de processamento para turismo e negocios.",
        "btn_asia": "Explorar Asia",
        "btn_europe": "Explorar Europa",
        "btn_americas": "Explorar America",
        "btn_oceania": "Explorar Oceania",
        "section_asia": "Asia",
        "desc_asia": "Encontre tipos de eVisa, duracoes, taxas, links oficiais e orientacao para solicitar online nos principais destinos turisticos asiaticos.",
        "section_europe": "Europa",
        "desc_europe": "Informacoes sobre vistos Schengen, eVisa e autorizacoes de viagem para a Europa. Consulte os requisitos, prazos de processamento e portais oficiais.",
        "section_americas": "America do Norte e do Sul",
        "desc_americas": "Explore as opcoes de visto e eVisa para os principais paises das Americas. Encontre requisitos, portais oficiais, duracoes de estadia e programas como eTA e ESTA.",
        "section_oceania": "Oceania",
        "desc_oceania": "Informacoes de visto e eVisitor para a Oceania. Verifique os requisitos de eVisitor, eTA ou visto para Australia e Nova Zelandia.",
        "faq_title": "Perguntas frequentes — eVisa &amp; Autorizacoes de viagem",
        "faq_q1": "Preciso de um eVisa para viajar?",
        "faq_a1": "As regras de visto dependem da sua nacionalidade e destino. Muitos paises permitem a entrada sem visto, enquanto outros exigem uma autorizacao online ou visto de embaixada.",
        "faq_q2": "Quanto tempo leva a aprovacao de um eVisa?",
        "faq_a2": "O prazo de aprovacao geralmente varia de algumas horas a varios dias, dependendo do destino e do volume de solicitacoes.",
        "faq_q3": "Quais documentos sao necessarios para um visto online?",
        "faq_a3": "Normalmente: passaporte valido, foto recente, detalhes da viagem e um metodo de pagamento para as taxas de visto.",
        "footer_copy": "© 2026 eVisa-Card.com — Plataforma mundial de informacoes sobre eVisa &amp; viagens",
        "legal": "Aviso legal",
        "disclaimer": "Isencao de responsabilidade",
    },
    "zh": {
        "html_lang": "zh",
        "lang_label": '<span class="fi fi-cn"></span> zhongwen',
        "title": "eVisa-Card.com — quanqiu dianzi qianzheng xinxi - lvxing shouquan zhinan",
        "meta_desc": "eVisa-Card.com wei quanqiu lvxingzhe tigong guanfang dianzi qianzheng xinxi. An guojia chazhao qianzheng leixing, zaixian shenqing, yaoqiu, feiyong he chuli shijian.",
        "canonical": "https://www.evisa-card.com/zh/",
        "og_title": "eVisa-Card.com — quanqiu dianzi qianzheng xinxi",
        "og_desc": "Zhuyo lvyou mudi de guanfang dianzi qianzheng he lvxing shouquan zhinan.",
        "nav_home": "shouye",
        "nav_dest": "mudi",
        "nav_about": "guanyu",
        "nav_guides": "zhinan",
        "hero_h1": "eVisa-Card.com — nin de quanqiu dianzi qianzheng &amp; lvxing shouquan zhinan",
        "hero_p": "Chazhao mei ge guojia de guanfang dianzi qianzheng xinxi. Liaojie lvyou he shangwu qianzheng leixing, yaoqiu, zaixian shenqing bu zhou, feiyong he chuli shijian.",
        "btn_asia": "tansuo yazhou",
        "btn_europe": "tansuo ouzhou",
        "btn_americas": "tansuo meizhou",
        "btn_oceania": "tansuo dayanzhou",
        "section_asia": "yazhou",
        "desc_asia": "Chazhao zhuyao yazhou lvyou mudi de dianzi qianzheng leixing, tingliu shichang, feiyong, guanfang lianjie ji zaixian shenqing zhidao.",
        "section_europe": "ouzhou",
        "desc_europe": "Ouzhou shengen qianzheng, dianzi qianzheng he lvxing shouquan xinxi. Chazhao fei-EU lvxingzhe de yaoqiu, chuli shijian he guanfang mendian.",
        "section_americas": "nan-bei meizhou",
        "desc_americas": "Tansuo nan-bei meizhou zhuyao guojia de qianzheng he dianzi qianzheng xuanze. Chazhao yaoqiu, guanfang shenqing mendian, tingliu shichang ji eTA, ESTA deng xiangmu.",
        "section_oceania": "dayanzhou",
        "desc_oceania": "Dayanzhou qianzheng he dianzi fangke xinxi. Chazhao aodaliya he xinxilan de eVisitor, eTA huo qianzheng yaoqiu.",
        "faq_title": "changjian wenti — dianzi qianzheng &amp; lvxing shouquan",
        "faq_q1": "Lvxing shifou xuyao dianzi qianzheng?",
        "faq_a1": "Qianzheng guize qu jue yu nin de guoji he mudi. Xuduo guojia yunxu mianqian ruzheng, qita guojia ze xu zaixian lvxing shouquan huo dashiguan qianzheng.",
        "faq_q2": "Dianzi qianzheng shenpi xuyao duochang shijian?",
        "faq_a2": "Shenpi shijian tongchang cong ji xiaoshi dao shu tian bu deng, juti qu jue yu mudi he shenqing liang.",
        "faq_q3": "Zaixian qianzheng xuyao na xie wenjian?",
        "faq_a3": "Tongchang xuyao: youxiao huzhao, jin qi zhaopian, lvxing xiangqing he qianzheng feiyong de youxiao zhifu fangshi.",
        "footer_copy": "© 2026 eVisa-Card.com — quanqiu dianzi qianzheng &amp; lvxing xinxi pingtai",
        "legal": "falv shengming",
        "disclaimer": "mianze shengming",
    },
    "ja": {
        "html_lang": "ja",
        "lang_label": '<span class="fi fi-jp"></span> nihongo',
        "title": "eVisa-Card.com — gurobaru eVisa joho - ryoko kyoka gaido",
        "meta_desc": "eVisa-Card.com wa sekaijuu no ryokoshatachi ni koushiki eVisa joho wo teikyoshimasu. Kuni goto ni biza no shurui, onlain shinsei, youken, tesuuryou, shori jikan wo kakuninshite kudasai.",
        "canonical": "https://www.evisa-card.com/ja/",
        "og_title": "eVisa-Card.com — gurobaru eVisa joho - ryoko kyoka gaido",
        "og_desc": "Shuyou kanko chi no koushiki eVisa oyobi ryoko kyoka gaido.",
        "nav_home": "hoomu",
        "nav_dest": "mokuteki chi",
        "nav_about": "gaiyou",
        "nav_guides": "gaido",
        "hero_h1": "eVisa-Card.com — gurobaru eVisa &amp; ryoko kyoka gaido",
        "hero_p": "Subete no kuni no koushiki eVisa joho wo kakuninshite kudasai. Kanko oyobi bijinesu ryoko no biza no shurui, youken, onlain shinsei tetsuzuki, tesuuryou, shori jikan wo gorannita dakemasu.",
        "btn_asia": "ajia wo sagasu",
        "btn_europe": "yooroppa wo sagasu",
        "btn_americas": "america wo sagasu",
        "btn_oceania": "ooshanea wo sagasu",
        "section_asia": "ajia",
        "desc_asia": "Shuyou na ajia kanko chi no eVisa no shurui, taizai kikan, tesuuryou, koushiki rinku, onlain shinsei shidou wo kakuninshite kudasai.",
        "section_europe": "yooroppa",
        "desc_europe": "Yooroppa no shenggen biza, eVisa, ryoko kyoka ni kansuru joho. EU-gai no ryokoshatachi no youken, shori jikan, koushiki pootaru wo kakuninshite kudasai.",
        "section_americas": "hokubei - nanbei",
        "desc_americas": "Hokubei - nanbei no shuyou koku no biza to eVisa no sentaku shi wo gorannita dakemasu. Youken, koushiki shinsei pootaru, taizai kikan, eTA, ESTA nado no puroguramu wo kakuninshite kudasai.",
        "section_oceania": "ooshanea",
        "desc_oceania": "Ooshanea no biza to eVisitor joho. Oosutoraria to Nyuujiirando no eVisitor, eTA, biza no youken wo kakuninshi, koushiki imin saito kara shinsei shite kudasai.",
        "faq_title": "yoku aru shitsumon — eVisa &amp; ryoko kyoka",
        "faq_q1": "ryoko ni eVisa wa hitsuyou desu ka?",
        "faq_a1": "Biza no kisoku wa kokuseki to mokuteki chi ni yotte kotonari masu. Ooku no kuni wa biza nashi de nyukoku dekimasu ga, onlain ryoko kyoka ya taishi kan biza ga hitsuyou na kuni mo arimasu.",
        "faq_q2": "eVisa no shounin ni wa dono kurai jikan ga kakari masu ka?",
        "faq_a2": "Shounin jikan wa, mokuteki chi ya shinsei ryo ni yotte suujikan kara suu-nichi kakaru baai ga arimasu.",
        "faq_q3": "onlain biza ni hitsuyou na shorui wa nani desu ka?",
        "faq_a3": "Tsuujou, yuukou na pasupooto, saikin no shashin, ryoko no shousai, biza tesuuryou no shiharai houhou ga hitsuyou desu.",
        "footer_copy": "© 2026 eVisa-Card.com — gurobaru eVisa &amp; ryoko joho purattofoomu",
        "legal": "housou tsuchi",
        "disclaimer": "menseki jikou",
    },
    "ko": {
        "html_lang": "ko",
        "lang_label": '<span class="fi fi-kr"></span> hangugeo',
        "title": "eVisa-Card.com — geullobeol jeonja bija jeongbo - yeohaeng heoga annae",
        "meta_desc": "eVisa-Card.com eun jeon segye yeohaengja ege gongshik jeonja bija jeongboreul jegonghabnida. Gukgabyeol bija yuheong, onlain sincheong, yogeon, susuryo mit cheori gigan eul hwaginhasaeyo.",
        "canonical": "https://www.evisa-card.com/ko/",
        "og_title": "eVisa-Card.com — geullobeol jeonja bija jeongbo",
        "og_desc": "Juyyo gwangwang mudi reul wihan gongshik jeonja bija mit yeohaeng heoga annae.",
        "nav_home": "hom",
        "nav_dest": "mokjeokji",
        "nav_about": "sogae",
        "nav_guides": "gaideu",
        "hero_h1": "eVisa-Card.com — geullobeol jeonja bija &amp; yeohaeng heoga annae",
        "hero_p": "Modeun gukga eui gongshik jeonja bija jeongboreul hwaginhasaeyo. Gwangwang mit bizeuniseu yeohaeng eul wihan bija yuheong, yogeon, onlain sincheong jeolcha, susuryo mit cheori gigan eul alaborasaeyo.",
        "btn_asia": "asia tamsaek",
        "btn_europe": "yureop tamsaek",
        "btn_americas": "ameraika tamsaek",
        "btn_oceania": "oseania tamsaek",
        "section_asia": "asia",
        "desc_asia": "Juyyo asia gwangwang mudi eui jeonja bija yuheong, cheryugi gan, susuryo, gongshik lingkeu mit onlain sincheong annae reul hwaginhasaeyo.",
        "section_europe": "yureop",
        "desc_europe": "Yureop eui sengen bija, jeonja bija mit yeohaeng heoga jeongbo. EU-oe yeohaengja reul wihan yogeon, cheori sigan mit gongshik poteol eul hwaginhasaeyo.",
        "section_americas": "bukmi mit nammi",
        "desc_americas": "Bukmi nammi juyyo gukga eui bija mit jeonja bija opseyon eul alaborasaeyo. Yogeon, gongshik sincheong poteol, cheryugi gan mit eTA, ESTA gateun peulogeulaem eul hwaginhasaeyo.",
        "section_oceania": "oseania",
        "desc_oceania": "Oseania eui bija mit jeonja bangmun jeongbo. Hoju wa nyujillaendeu eui eVisitor, eTA doneun bija yogeon eul hwaginhasaeyo.",
        "faq_title": "jaju mutneun jilmun — jeonja bija &amp; yeohaeng heoga",
        "faq_q1": "yeohaeng e jeonja bija ga pilyohan gayo?",
        "faq_a1": "Bija gyuchig eun gukjeok gwa mokjeokji e ttara dareumnida. Manheun gukga ga mubija ibgug eul heoyonghajiman, onlain yeohaeng heoga na daesagwan bija ga pilyohan gukga do itseumnida.",
        "faq_q2": "jeonja bija seungyin e eolmana geollinayo?",
        "faq_a2": "Seungyin sigan eun mokjeokji wa sincheong ryang e ttara myeot sigan eseo myeot il kkaji soyo doel su itseumnida.",
        "faq_q3": "onlain bija e pilyohan seoryu neun mueosinnayo?",
        "faq_a3": "Ilbanjeok euro yuehyo han yeogwon, choegeun sajin, yeohaeng sebo jeongbo, bija susuryo gyeolche sudo ga pilyohabnida.",
        "footer_copy": "© 2026 eVisa-Card.com — geullobeol jeonja bija &amp; yeohaeng jeongbo peullaetpom",
        "legal": "beomnyul goji",
        "disclaimer": "myeonjek johang",
    },
    "ru": {
        "html_lang": "ru",
        "lang_label": '<span class="fi fi-ru"></span> Russkiy',
        "title": "eVisa-Card.com — Globalnaya informatsiya ob elektronnykh vizakh - Rukovodstvo po puteshestviyam",
        "meta_desc": "eVisa-Card.com predostavlyaet ofitsialnuyu informatsiyu ob elektronnykh vizakh dlya puteshestvennikov so vsego mira. Uznayte o tipakh viz, onlayn-zayavkakh, trebovaniyakh, sborakh i srokakh obrabotki po stranam.",
        "canonical": "https://www.evisa-card.com/ru/",
        "og_title": "eVisa-Card.com — Globalnaya informatsiya ob elektronnykh vizakh",
        "og_desc": "Ofitsialnoye rukovodstvo po elektronnym vizam i razresheniyam na vezd dlya osnovnykh turisticheskikh napravleniy.",
        "nav_home": "Glavnaya",
        "nav_dest": "Napravleniya",
        "nav_about": "O nas",
        "nav_guides": "Rukovodstva",
        "hero_h1": "eVisa-Card.com — Vash globalnyy putevoditel po elektronnym vizam &amp; razresheniyam na vezd",
        "hero_p": "Naydite ofitsialnuyu informatsiyu ob elektronnykh vizakh dlya kazhdoy strany. Uznayte o tipakh viz, trebovaniyakh, shagakh onlayn-podachi zayavki, sborakh i srokakh obrabotki dlya turizma i biznesa.",
        "btn_asia": "Issledovat Aziyu",
        "btn_europe": "Issledovat Yevropu",
        "btn_americas": "Issledovat Ameriku",
        "btn_oceania": "Issledovat Okeaniya",
        "section_asia": "Aziya",
        "desc_asia": "Naydite tipy elektronnykh viz, sroki prebyvaniya, sbory, ofitsialnyye ssylki i rukovodstvo po onlayn-podache zayavok dlya osnovnykh aziatskikh turisticheskikh napravleniy.",
        "section_europe": "Yevropа",
        "desc_europe": "Informatsiya o shengenskikh vizakh, elektronnykh vizakh i razresheniyakh na vezd v Yevropu. Uznayte o trebovaniyakh, srokakh obrabotki i ofitsialnykh portalakh dlya puteshestvennikov iz-za predelov YES.",
        "section_americas": "Severnaya i Yuzhnaya Amerika",
        "desc_americas": "Izuchite varianty viz i elektronnykh viz dlya osnovnykh stran Severnoy i Yuzhnoy Ameriki. Naydite trebovaniya, ofitsialnyye portaly podachi zayavok, sroki prebyvaniya i programmy, takiye kak eTA i ESTA.",
        "section_oceania": "Okeaniya",
        "desc_oceania": "Informatsiya o vizakh i elektronnom poseshchenii Okeanii. Proverite trebovaniya eVisitor, eTA ili vizy dlya Avstralii i Novoy Zelandii.",
        "faq_title": "Chasto zadavayemyye voprosy — elektronnyye vizy &amp; razresheniya na vezd",
        "faq_q1": "Nuzhna li mne elektronnaya viza dlya puteshestviya?",
        "faq_a1": "Pravila vizovogo rezhima zavisyat ot grazhdanstva i punkta naznacheniya. Mnogie strany razreshayut vezd bez vizy, drugiye trebuyut onlayn-razresheniye ili posolskuyu vizu.",
        "faq_q2": "Skolko vremeni zanimayet odobreniye elektronnoy vizy?",
        "faq_a2": "Vremya odobreniya obychno sostavlyayet ot neskolkikh chasov do neskolkikh dney v zavisimosti ot napravleniya i obyema zayavok.",
        "faq_q3": "Kakiye dokumenty nuzhny dlya onlayn-vizy?",
        "faq_a3": "Kak pravilo: deystvuyushchiy pasport, nedavnyaya fotografiya, dannyye o poyezdke i deystvuyushchiy sposob oplaty dlya vizovykh sborov.",
        "footer_copy": "© 2026 eVisa-Card.com — Globalnaya platforma informatsii ob elektronnykh vizakh &amp; puteshestviyakh",
        "legal": "Pravovyye uvedomleniya",
        "disclaimer": "Otkaz ot otvetstvennosti",
    },
    "ar": {
        "html_lang": "ar",
        "lang_label": '<span class="fi fi-sa"></span> alarabiyya',
        "title": "eVisa-Card.com — maelumat altaasheera aliliktruniyya alealamiyya - daleel alsafar",
        "meta_desc": "yuwafir mawqi eVisa-Card.com maelumat rasmiyya ean altaasheera aliliktruniyya lilmusafirin hawla alealami. aktashif anwae altaasheera wal-tatbiqat eabr alinternet wal-mutatalabat wal-rusum wamuddat almuealjat lkull dawla.",
        "canonical": "https://www.evisa-card.com/ar/",
        "og_title": "eVisa-Card.com — maelumat altaasheera aliliktruniyya alealamiyya",
        "og_desc": "daleel rasmiy liltaasheera aliliktruniyya wa-tasareeh alsafar lil-wajhat alsiyahiyya alrayeesiyya.",
        "nav_home": "alrayeesiyya",
        "nav_dest": "alwajhat",
        "nav_about": "hawl",
        "nav_guides": "al-adilla",
        "hero_h1": "eVisa-Card.com — daleelak aleaalami liltaashiraat aliliktruniyya &amp; tasareeh alsafar",
        "hero_p": "ibhath ean maelumat rasmiyya ean altaasheera aliliktruniyya likull dawla. taearraf ealaa anwae altaasheera wal-mutatalabat wakhutuat altaqadim eabr alinternet wal-rusum wawqt almuealjat lissiyaha walaaemal.",
        "btn_asia": "istikshaf asya",
        "btn_europe": "istikshaf urubba",
        "btn_americas": "istikshaf alamrikatayn",
        "btn_oceania": "istikshaf awqiyanus",
        "section_asia": "asya",
        "desc_asia": "ibhath ean anwae altaashiraat aliliktruniyya wamudad aliqama wal-rusum wal-rawabat alrasmiyya wairshadat altaqadim eabr alinternet lil-wajhat alsiyahiyya alrayeesiyya fi asya.",
        "section_europe": "urubba",
        "desc_europe": "maelumat ean tashayraat shenghan wal-taashiraat aliliktruniyya wa-tasareeh alsafar 'iilaa 'uruppa. tahaqqaq min almutatalabat wawqat almuealjat wal-bawwabat alrasmiyya lilmusafirin min khaarij alitihaad al-'urubbi.",
        "section_americas": "amrika alshamaaliyya waljanuubiyya",
        "desc_americas": "istikshaf khiyarat altaasheera waltaasheera aliliktruniyya lidduwwal alrayeesiyya fi amrika. ibhath ean almutatalabat wal-bawwabat alrasmiyya wamudad aliqama wa-baramij mithil eTA wa ESTA.",
        "section_oceania": "awqiyanuusiya",
        "desc_oceania": "maelumat altaasheera walzaayir aliliktruuniy li'awqiyaanusiya. tahaqqaq min mutatalabat eVisitor 'aw eTA 'aw altaasheera li'ustraaliya wa-nyuuzylndah.",
        "faq_title": "al-as'ila alshayieat — altashiraat aliliktruniyya &amp; tasareeh alsafar",
        "faq_q1": "hal 'ahtaj 'iilaa taasheera 'iiliktruniyya lissafar?",
        "faq_a1": "taetamid qawaid altaasheera ealaa jinsiyatik wawajhatik. tashmah kathir min alduwwal bialdukhul bidun taasheera, baynama tatatalab duwal 'ukhraa tasrihan 'iiliktrunian 'aw taasheerat sifara.",
        "faq_q2": "kam yastatghriqu alhasul ealaa muwafaqat altaasheera aliliktruniyya?",
        "faq_a2": "yataraawah waqt almuwafaqat eadatan min saeat qaliila 'iilaa eiddat 'ayaam hasab alwajha wahjm altalbiyat.",
        "faq_q3": "maa alwathaayiq almatluba liltaasheera aliliktruniyya?",
        "faq_a3": "eadatan: jawaz safar saarin, sura hadithat, tafasil alsafar, wawasilat dafe sariyat lirisum altaasheera.",
        "footer_copy": "© 2026 eVisa-Card.com — mansat maelumat altaasheera aliliktruniyya &amp; alsafar alealamiyya",
        "legal": "ishear qanuuni",
        "disclaimer": "ikhlaa almasuwliyya",
    },
    "th": {
        "html_lang": "th",
        "lang_label": '<span class="fi fi-th"></span> thai',
        "title": "eVisa-Card.com — khomun eVisa thuakhong - khumu kandern thang",
        "meta_desc": "eVisa-Card.com hai khomun eVisa yang pen thangkan samrap nak dern thang thuakhong. khon ha praphet wisa, kan samat ok lain, kho kam nod, kha thamniarm, lae rawaya wela dam nen ngan tam prathet.",
        "canonical": "https://www.evisa-card.com/th/",
        "og_title": "eVisa-Card.com — khomun eVisa thuakhong",
        "og_desc": "khumu eVisa yang pen thangkan lae kan arnu yat kan dern thang samrap jut mai plai thang thong thiao lak.",
        "nav_home": "na raek",
        "nav_dest": "jut mai plai thang",
        "nav_about": "kiao kap",
        "nav_guides": "khumu",
        "hero_h1": "eVisa-Card.com — khumu eVisa &amp; kan arnu yat kan dern thang thuakhong khong khun",
        "hero_p": "khon ha khomun eVisa yang pen thangkan samrap thuk prathet. rean ru kiao kap praphet wisa, kho kam nod, khan ton kan samat ok lain, kha thamniarm, lae rawaya wela dam nen ngan samrap kan thong thiao lae thurakij.",
        "btn_asia": "samruad asia",
        "btn_europe": "samruad yurob",
        "btn_americas": "samruad america",
        "btn_oceania": "samruad o-shia-nia",
        "section_asia": "asia",
        "desc_asia": "khon ha praphet eVisa, rawaya yu, kha thamniarm, link yang pen thangkan, lae kham nan na kan samat ok lain samrap jut mai plai thang thong thiao lak nai asia.",
        "section_europe": "yurob",
        "desc_europe": "khomun wisa Schengen, eVisa, lae kan arnu yat kan dern thang pai yang yurob. truat sob kho kam nod, rawaya wela dam nen ngan, lae pho-tal yang pen thangkan samrap nak dern thang thi mai chai EU.",
        "section_americas": "america nua lae tai",
        "desc_americas": "samruad tang leuk khong wisa lae eVisa samrap prathet lak nai america nua lae tai. khon ha kho kam nod, pho-tal samat yang pen thangkan, rawaya yu, lae khrongkan thao eTA lae ESTA.",
        "section_oceania": "o-shia-nia",
        "desc_oceania": "khomun wisa lae eVisitor samrap o-shia-nia. truat sob kho kam nod eVisitor, eTA, rue wisa samrap australia lae nyu si-lan.",
        "faq_title": "kham tham thi phob ban krong — eVisa &amp; kan arnu yat kan dern thang",
        "faq_q1": "chan tong mi eVisa phue dern thang rue plao?",
        "faq_a1": "kotchamniarm wisa khun yu kap san chat lae jut mai plai thang khong khun. lai prathet arnu yat hai khao prathet doi mai tong mi wisa, nai kha thi bang prathet tong kan arnu yat ok lain rue wisa sa than thut.",
        "faq_q2": "kan anu mat eVisa chai wela nan thao rai?",
        "faq_a2": "wela anu mat chai wela ton pra man cak mai khi chua mong thung lai wan khun yu kap jut mai plai thang lae pa ri man kan samat.",
        "faq_q3": "tong chai ekkasan arai bang samrap wisa ok lain?",
        "faq_a3": "doi thuai pai: nang su dern thang thi yang mai mot ayu, rup thai lao sun, rai la iad kan dern thang, lae wit hi cham ra ka tham niarm wisa thi chai dai.",
        "footer_copy": "© 2026 eVisa-Card.com — phaen thi khomun eVisa &amp; kan dern thang thuakhong",
        "legal": "prakad thang kotmai",
        "disclaimer": "kho cam kad khwam rap phit chob",
    },
}

LANG_DROPDOWN_TEMPLATE = """                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item{act_en}" href="/"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item{act_fr}" href="/fr/"><span class="fi fi-fr"></span> Fran&#231;ais</a>
                        <a class="dropdown-item{act_es}" href="/es/"><span class="fi fi-es"></span> Espa&#241;ol</a>
                        <a class="dropdown-item{act_pt}" href="/pt/"><span class="fi fi-br"></span> Portugu&#234;s</a>
                        <a class="dropdown-item{act_zh}" href="/zh/"><span class="fi fi-cn"></span> &#20013;&#25991;</a>
                        <a class="dropdown-item{act_th}" href="/th/"><span class="fi fi-th"></span> &#3652;&#3607;&#3618;</a>
                        <a class="dropdown-item{act_ru}" href="/ru/"><span class="fi fi-ru"></span> &#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;</a>
                        <a class="dropdown-item{act_ar}" href="/ar/"><span class="fi fi-sa"></span> &#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;</a>
                        <a class="dropdown-item{act_ja}" href="/ja/"><span class="fi fi-jp"></span> &#26085;&#26412;&#35486;</a>
                        <a class="dropdown-item{act_ko}" href="/ko/"><span class="fi fi-kr"></span> &#54620;&#44397;&#50612;</a>
                    </div>"""


def make_page(lang, cfg):
    html = EN_HTML

    # 1. html lang attribute
    html = html.replace('<html lang="en">', f'<html lang="{cfg["html_lang"]}">', 1)

    # 2. Canonical
    html = re.sub(r'<link href="https://www\.evisa-card\.com/" rel="canonical" />',
                  f'<link rel="canonical" href="{cfg["canonical"]}"/>', html)

    # 3. Title
    html = re.sub(r'<title>[^<]*</title>',
                  f'<title>{cfg["title"]}</title>', html)

    # 4. Meta description
    html = re.sub(r'(<meta content=")[^"]*(" name="description" />)',
                  lambda m: m.group(1) + cfg["meta_desc"] + m.group(2), html)

    # 5. OG tags
    html = re.sub(r'(<meta content=")[^"]*(" property="og:title" />)',
                  lambda m: m.group(1) + cfg["og_title"] + m.group(2), html)
    html = re.sub(r'(<meta content=")[^"]*(" property="og:description" />)',
                  lambda m: m.group(1) + cfg["og_desc"] + m.group(2), html)
    html = re.sub(r'(<meta content=")[^"]*(" property="og:url" />)',
                  lambda m: m.group(1) + cfg["canonical"] + m.group(2), html)

    # 6. CSS paths: relative → ../css/
    html = html.replace('href="css/', 'href="../css/')
    html = html.replace("href='css/", "href='../css/")

    # 7. JS paths: relative → ../js/
    html = html.replace('src="js/', 'src="../js/')
    html = html.replace("src='js/", "src='../js/")

    # 8. Image paths in style attributes
    html = html.replace("url('images/", "url('../images/")
    html = html.replace('url("images/', 'url("../images/')
    html = html.replace("url(images/", "url(../images/")

    # 9. Brand logo and img src paths
    html = html.replace('src="images/', 'src="../images/')
    html = html.replace("src='images/", "src='../images/")

    # 10. All /en/ links → /lang/
    html = html.replace('href="/en/', f'href="/{lang}/')

    # 11. Navbar brand
    html = html.replace('href="/index.html"', f'href="/{lang}/"', 1)

    # 12. Nav links (Home, Destinations, About, Guides)
    html = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="[^"]*">Home</a></li>',
        f'<li class="nav-item"><a class="nav-link" href="/{lang}/">{cfg["nav_home"]}</a></li>',
        html
    )
    html = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="/destination\.html">Destinations</a></li>',
        f'<li class="nav-item"><a class="nav-link" href="/{lang}/destination.html">{cfg["nav_dest"]}</a></li>',
        html
    )
    html = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="/about\.html">About</a></li>',
        f'<li class="nav-item"><a class="nav-link" href="/{lang}/about.html">{cfg["nav_about"]}</a></li>',
        html
    )
    html = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="[^"]*expat-guides\.html">Guides</a></li>',
        f'<li class="nav-item"><a class="nav-link" href="/{lang}/expat-guides.html">{cfg["nav_guides"]}</a></li>',
        html
    )

    # 13. Language dropdown
    acts = {l: '' for l in ['en', 'fr', 'es', 'pt', 'zh', 'th', 'ru', 'ar', 'ja', 'ko']}
    acts[lang] = ' active'
    new_dropdown = LANG_DROPDOWN_TEMPLATE.format(**{f'act_{l}': acts[l] for l in acts})
    html = re.sub(
        r'<div class="dropdown-menu dropdown-menu-right"[^>]*>.*?</div>',
        new_dropdown,
        html,
        flags=re.DOTALL,
        count=1
    )

    # 14. Active lang button label (the toggle button text)
    html = re.sub(
        r'(<a class="nav-link dropdown-toggle"[^>]*>)[^<]*(<span class="fi fi-[a-z]+">[^<]*</span>[^<]*)(</a>)',
        lambda m: m.group(1) + cfg['lang_label'] + m.group(3),
        html
    )

    # 15. Hero texts
    html = re.sub(
        r'<h1 class="mb-3 bread"[^>]*>[^<]*</h1>',
        f'<h1 class="mb-3 bread" style="font-size:1.5rem;">{cfg["hero_h1"]}</h1>',
        html
    )
    html = re.sub(
        r'<p class="lead mb-3"[^>]*>[^<]*</p>',
        f'<p class="lead mb-3" style="font-size:1rem;max-width:700px;margin:0 auto;">{cfg["hero_p"]}</p>',
        html
    )

    # 16. Explore buttons
    html = html.replace('>Explore Asia<', f'>{cfg["btn_asia"]}<')
    html = html.replace('>Explore Europe<', f'>{cfg["btn_europe"]}<')
    html = html.replace('>Explore America<', f'>{cfg["btn_americas"]}<')
    html = html.replace('>Explore Oceania<', f'>{cfg["btn_oceania"]}<')

    # 17. Section headings + descriptions
    html = re.sub(
        r'(<h2 class="mb-3">)Asia(</h2>)',
        r'\g<1>' + cfg["section_asia"] + r'\g<2>',
        html, count=1
    )
    html = re.sub(
        r'(<h2 class="mb-3">)Europe(</h2>)',
        r'\g<1>' + cfg["section_europe"] + r'\g<2>',
        html, count=1
    )
    html = re.sub(
        r'(<h2 class="mb-3">)North and South America(</h2>)',
        r'\g<1>' + cfg["section_americas"] + r'\g<2>',
        html, count=1
    )
    html = re.sub(
        r'(<h2 class="mb-3">)Oc[eé]anie?(</h2>)',
        r'\g<1>' + cfg["section_oceania"] + r'\g<2>',
        html, count=1
    )

    # 18. Section lead descriptions
    html = re.sub(
        r'<p class="lead">Find eVisa types[^<]*</p>',
        f'<p class="lead">{cfg["desc_asia"]}</p>',
        html, count=1
    )
    html = re.sub(
        r'<p class="lead">Overview of Schengen visas[^<]*</p>',
        f'<p class="lead">{cfg["desc_europe"]}</p>',
        html, count=1
    )
    html = re.sub(
        r'<p class="lead">Explore visa and eVisa options for major countries across[^<]*</p>',
        f'<p class="lead">{cfg["desc_americas"]}</p>',
        html, count=1
    )
    html = re.sub(
        r'<p class="lead">Visa and eVisitor information for Oceania[^<]*</p>',
        f'<p class="lead">{cfg["desc_oceania"]}</p>',
        html, count=1
    )

    # 19. FAQ section
    html = re.sub(
        r'<h2 class="text-center mb-4">Frequently Asked Questions[^<]*</h2>',
        f'<h2 class="text-center mb-4">{cfg["faq_title"]}</h2>',
        html
    )
    html = html.replace(
        '<h3>Do I need an eVisa to travel?</h3>',
        f'<h3>{cfg["faq_q1"]}</h3>'
    )
    html = re.sub(
        r'<p>Visa rules depend on nationality[^<]*</p>',
        f'<p>{cfg["faq_a1"]}</p>',
        html, count=1
    )
    html = html.replace(
        '<h3>How long does an eVisa take to be approved?</h3>',
        f'<h3>{cfg["faq_q2"]}</h3>'
    )
    html = re.sub(
        r'<p>Approval time usually ranges[^<]*</p>',
        f'<p>{cfg["faq_a2"]}</p>',
        html, count=1
    )
    html = html.replace(
        '<h3>What documents are needed for an online visa?</h3>',
        f'<h3>{cfg["faq_q3"]}</h3>'
    )
    html = re.sub(
        r'<p>Typically: passport validity[^<]*</p>',
        f'<p>{cfg["faq_a3"]}</p>',
        html, count=1
    )

    # 20. Footer
    html = html.replace(
        '© 2026 eVisa-Card.com — Global eVisa &amp; Travel Information Platform',
        cfg['footer_copy']
    )
    html = re.sub(
        r'<a href="[^"]*legal-notice\.html"[^>]*>Legal Notice</a>',
        f'<a href="/{lang}/legal-notice.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">{cfg["legal"]}</a>',
        html
    )
    html = re.sub(
        r'<a href="[^"]*disclaimer\.html"[^>]*>Disclaimer</a>',
        f'<a href="/{lang}/disclaimer.html" style="color:#ffffff;text-decoration:underline;font-weight:500;">{cfg["disclaimer"]}</a>',
        html
    )

    return html


count = 0
for lang, cfg in LANGS.items():
    out_path = os.path.join(BASE, lang, "index.html")
    html = make_page(lang, cfg)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print(f"[OK] {out_path}")

print(f"\nDone: {count} language home pages created.")
