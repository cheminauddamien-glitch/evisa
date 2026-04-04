#!/usr/bin/env python3
"""
Fix all remaining issues:
1. Remove grey veil (ftco-loader hidden immediately + remove scrollax grey)
2. Add logo image to navbar (all pages, all langs)
3. Remove line-clamp CSS (card descriptions no longer truncated)
4. Fix footer link color (white → readable dark)
5. Create FR/ES/PT legal pages (fix 404)
"""
import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

WWW = "C:/Users/chemi/Documents/evisa/pacific-main/www"

# ── 1. Fix CSS: remove line-clamp + fix ftco-loader grey ─────────────────────
css_path = os.path.join(WWW, "css", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove line-clamp on project-wrap p
css = css.replace(
    """.col-md-3 .project-wrap p {
  font-size: 12px !important;
  line-height: 1.4 !important;
  margin-bottom: 4px !important;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}""",
    """.col-md-3 .project-wrap p {
  font-size: 12px !important;
  line-height: 1.4 !important;
  margin-bottom: 4px !important;
}"""
)

# Hide ftco-loader immediately (no transition delay)
css = css.replace(
    "#ftco-loader {\n  position: fixed;",
    "#ftco-loader {\n  display: none !important;\n  position: fixed;"
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("CSS fixed: line-clamp removed, ftco-loader hidden")


# ── 2. Fix all HTML pages ─────────────────────────────────────────────────────
all_html = (
    glob.glob(os.path.join(WWW, "*.html")) +
    glob.glob(os.path.join(WWW, "en", "*.html")) +
    glob.glob(os.path.join(WWW, "fr", "*.html")) +
    glob.glob(os.path.join(WWW, "es", "*.html")) +
    glob.glob(os.path.join(WWW, "pt", "*.html"))
)

fixed = errors = 0

for fpath in all_html:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        orig = html

        # Determine prefix (root or subdir)
        rel = os.path.relpath(fpath, WWW).replace("\\", "/")
        is_root = "/" not in rel
        img_prefix = "images/" if is_root else "../images/"

        # ── A. Replace text-only brand with logo image ──────────────────────
        # Root pages: href="index.html" or href="/index.html"
        # Lang subpages: href="../index.html"
        html = re.sub(
            r'<a class="navbar-brand"([^>]*)>eVisa-Card<span>\.com</span></a>',
            lambda m: f'<a class="navbar-brand"{m.group(1)} style="padding:4px 0;"><img src="{img_prefix}logo.png" alt="eVisa-Card.com" style="height:44px;width:auto;vertical-align:middle;"></a>',
            html
        )

        # ── B. Fix footer link color (white → near-white stays visible on dark bg) ──
        # Change to white text with better contrast
        html = html.replace(
            'style="color:rgba(255,255,255,0.7);text-decoration:none;"',
            'style="color:#ffffff;text-decoration:underline;font-weight:500;"'
        )

        # ── C. Fix legal page links for FR/ES/PT (point to EN if lang pages don't exist) ──
        # Will be fixed properly after creating the pages — skip for now

        if html != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            fixed += 1
    except Exception as e:
        print(f"ERR {fpath}: {e}")
        errors += 1

print(f"HTML fixed: {fixed} pages | Errors: {errors}")


# ── 3. Create FR/ES/PT legal pages ───────────────────────────────────────────

def legal_page(lang, page_type):
    """Generate a legal/disclaimer page in the given language."""
    configs = {
        "fr": {
            "legal": {
                "slug": "mentions-legales",
                "title": "Mentions Légales | eVisa-Card.com",
                "h1": "Mentions Légales",
                "content": """
    <h2>Éditeur du site</h2>
    <p>eVisa-Card.com est un site d'information indépendant dédié aux informations sur les visas de voyage pour les voyageurs internationaux.</p>
    <ul>
        <li><strong>Site web :</strong> https://www.evisa-card.com</li>
        <li><strong>Contact :</strong> <a href="mailto:contact@evisa-card.com">contact@evisa-card.com</a></li>
    </ul>
    <h2>Hébergement</h2>
    <p>Ce site est hébergé par un prestataire d'hébergement tiers. Pour plus d'informations, contactez-nous à l'adresse e-mail ci-dessus.</p>
    <h2>Propriété intellectuelle</h2>
    <p>Tout le contenu publié sur eVisa-Card.com — textes, graphiques, logos et données — est la propriété exclusive d'eVisa-Card.com ou de ses partenaires de contenu, et est protégé par les lois sur la propriété intellectuelle applicables.</p>
    <p>La reproduction, la distribution ou l'utilisation de tout contenu sans autorisation écrite préalable est strictement interdite.</p>
    <h2>Données et confidentialité</h2>
    <p>eVisa-Card.com utilise Google Analytics (GA4) pour collecter des statistiques de trafic anonymes. Aucune donnée personnelle n'est vendue ou partagée à des tiers à des fins marketing. Ce site utilise Google AdSense pour afficher des publicités.</p>
    <h2>Liens externes</h2>
    <p>eVisa-Card.com peut contenir des liens vers des sites externes. Nous ne sommes pas responsables du contenu ou des pratiques de confidentialité de ces sites.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Dernière mise à jour : mars 2026</p>"""
            },
            "disclaimer": {
                "slug": "disclaimer",
                "title": "Avertissement | eVisa-Card.com",
                "h1": "Avertissement (Disclaimer)",
                "content": """
    <h2>À titre informatif uniquement</h2>
    <p>Les informations fournies sur eVisa-Card.com sont à des fins d'information générale uniquement. Elles ne constituent pas un conseil juridique, un conseil en immigration ou tout autre conseil professionnel.</p>
    <h2>Exactitude des informations</h2>
    <p>Bien que nous nous efforcions de maintenir toutes les informations sur les visas exactes et à jour, <strong>les réglementations, frais et conditions d'entrée changent fréquemment</strong>. eVisa-Card.com ne peut garantir l'exhaustivité, l'exactitude ou l'actualité des informations fournies.</p>
    <p>Vérifiez toujours les dernières exigences auprès de l'ambassade ou du consulat officiel de votre pays de destination.</p>
    <h2>Absence de responsabilité</h2>
    <p>eVisa-Card.com ne peut être tenu responsable de toute perte, dommage ou inconvénient découlant de la confiance accordée aux informations publiées sur ce site. L'utilisation de ce site est entièrement à vos propres risques.</p>
    <h2>Publicité et affiliation</h2>
    <p>Ce site affiche des publicités via Google AdSense. Certains liens peuvent être des liens d'affiliation. Cela n'influence pas notre contenu éditorial.</p>
    <h2>Pas de service de demande de visa</h2>
    <p>eVisa-Card.com <strong>ne traite pas</strong> les demandes de visa, ne délivre pas de visas et n'agit pas en tant qu'agence de voyage.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Dernière mise à jour : mars 2026</p>"""
            }
        },
        "es": {
            "legal": {
                "slug": "aviso-legal",
                "title": "Aviso Legal | eVisa-Card.com",
                "h1": "Aviso Legal",
                "content": """
    <h2>Editor del sitio</h2>
    <p>eVisa-Card.com es un sitio web de información independiente dedicado a proporcionar orientación sobre visas de viaje para viajeros internacionales.</p>
    <ul>
        <li><strong>Sitio web:</strong> https://www.evisa-card.com</li>
        <li><strong>Contacto:</strong> <a href="mailto:contact@evisa-card.com">contact@evisa-card.com</a></li>
    </ul>
    <h2>Alojamiento</h2>
    <p>Este sitio web está alojado por un proveedor de alojamiento externo. Para más detalles, contáctenos en el correo electrónico indicado.</p>
    <h2>Propiedad intelectual</h2>
    <p>Todo el contenido publicado en eVisa-Card.com — incluyendo textos, gráficos, logotipos y datos — es propiedad exclusiva de eVisa-Card.com o sus socios de contenido, y está protegido por las leyes de propiedad intelectual aplicables.</p>
    <p>La reproducción, distribución o uso de cualquier contenido sin permiso previo por escrito está estrictamente prohibida.</p>
    <h2>Datos y privacidad</h2>
    <p>eVisa-Card.com utiliza Google Analytics (GA4) para recopilar estadísticas de tráfico anónimas. Ningún dato personal se vende ni comparte con terceros con fines de marketing. Este sitio utiliza Google AdSense para mostrar anuncios.</p>
    <h2>Enlace a sitios externos</h2>
    <p>eVisa-Card.com puede contener enlaces a sitios externos. No somos responsables del contenido o las prácticas de privacidad de dichos sitios.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Última actualización: marzo 2026</p>"""
            },
            "disclaimer": {
                "slug": "disclaimer",
                "title": "Aviso Legal (Disclaimer) | eVisa-Card.com",
                "h1": "Aviso de Exención de Responsabilidad",
                "content": """
    <h2>Solo con fines informativos</h2>
    <p>La información proporcionada en eVisa-Card.com es <strong>solo para fines informativos generales</strong>. No constituye asesoramiento legal, asesoramiento en inmigración ni ningún otro asesoramiento profesional.</p>
    <h2>Precisión de la información</h2>
    <p>Aunque nos esforzamos por mantener toda la información sobre visas precisa y actualizada, <strong>las regulaciones, tarifas y requisitos de entrada cambian con frecuencia</strong>. eVisa-Card.com no puede garantizar la integridad, precisión o actualidad de la información proporcionada.</p>
    <p>Siempre verifique los últimos requisitos con la embajada o consulado oficial de su país de destino.</p>
    <h2>Sin responsabilidad</h2>
    <p>eVisa-Card.com no será responsable de ninguna pérdida, daño o inconveniente derivado de la confianza depositada en la información publicada en este sitio web. El uso de este sitio es enteramente bajo su propio riesgo.</p>
    <h2>Publicidad y afiliación</h2>
    <p>Este sitio web muestra anuncios a través de Google AdSense. Algunos enlaces pueden ser enlaces de afiliados. Esto no influye en nuestro contenido editorial.</p>
    <h2>Sin servicio de solicitud de visa</h2>
    <p>eVisa-Card.com <strong>no</strong> procesa solicitudes de visa, emite visas ni actúa como agencia de viajes.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Última actualización: marzo 2026</p>"""
            }
        },
        "pt": {
            "legal": {
                "slug": "aviso-legal",
                "title": "Aviso Legal | eVisa-Card.com",
                "h1": "Aviso Legal",
                "content": """
    <h2>Editor do site</h2>
    <p>eVisa-Card.com é um site de informações independente dedicado a fornecer orientação sobre vistos de viagem para viajantes internacionais.</p>
    <ul>
        <li><strong>Site:</strong> https://www.evisa-card.com</li>
        <li><strong>Contato:</strong> <a href="mailto:contact@evisa-card.com">contact@evisa-card.com</a></li>
    </ul>
    <h2>Hospedagem</h2>
    <p>Este site é hospedado por um provedor de hospedagem terceirizado. Para mais detalhes, entre em contato pelo e-mail acima.</p>
    <h2>Propriedade intelectual</h2>
    <p>Todo o conteúdo publicado na eVisa-Card.com — incluindo textos, gráficos, logotipos e dados — é propriedade exclusiva da eVisa-Card.com ou de seus parceiros de conteúdo, e é protegido pelas leis de propriedade intelectual aplicáveis.</p>
    <p>A reprodução, distribuição ou uso de qualquer conteúdo sem permissão prévia por escrito é estritamente proibida.</p>
    <h2>Dados e privacidade</h2>
    <p>eVisa-Card.com usa o Google Analytics (GA4) para coletar estatísticas de tráfego anônimas. Nenhum dado pessoal é vendido ou compartilhado com terceiros para fins de marketing. Este site usa o Google AdSense para exibir anúncios.</p>
    <h2>Links externos</h2>
    <p>eVisa-Card.com pode conter links para sites externos. Não somos responsáveis pelo conteúdo ou práticas de privacidade desses sites.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Última atualização: março de 2026</p>"""
            },
            "disclaimer": {
                "slug": "disclaimer",
                "title": "Isenção de Responsabilidade | eVisa-Card.com",
                "h1": "Isenção de Responsabilidade",
                "content": """
    <h2>Apenas para fins informativos</h2>
    <p>As informações fornecidas na eVisa-Card.com são para <strong>fins informativos gerais apenas</strong>. Não constituem aconselhamento jurídico, aconselhamento em imigração ou qualquer outro aconselhamento profissional.</p>
    <h2>Precisão das informações</h2>
    <p>Embora nos esforcemos para manter todas as informações sobre vistos precisas e atualizadas, <strong>regulamentos, taxas e requisitos de entrada mudam frequentemente</strong>. A eVisa-Card.com não pode garantir a integridade, precisão ou atualidade das informações fornecidas.</p>
    <p>Sempre verifique os requisitos mais recentes com a embaixada ou consulado oficial do seu país de destino.</p>
    <h2>Sem responsabilidade</h2>
    <p>eVisa-Card.com não será responsável por qualquer perda, dano ou inconveniente decorrente da confiança nas informações publicadas neste site. O uso deste site é inteiramente por sua conta e risco.</p>
    <h2>Publicidade e afiliação</h2>
    <p>Este site exibe anúncios via Google AdSense. Alguns links podem ser links de afiliados. Isso não influencia nosso conteúdo editorial.</p>
    <h2>Sem serviço de solicitação de visto</h2>
    <p>eVisa-Card.com <strong>não</strong> processa solicitações de visto, emite vistos nem atua como agência de viagens.</p>
    <p style="color:#999;font-size:13px;margin-top:40px;">Última atualização: março de 2026</p>"""
            }
        }
    }

    cfg = configs[lang][page_type]
    flag = {"fr":"fi-fr","es":"fi-es","pt":"fi-br"}[lang]
    label = {"fr":"Français","es":"Español","pt":"Português"}[lang]
    home = {"fr":"Accueil","es":"Inicio","pt":"Início"}[lang]
    dest = {"fr":"Destinations","es":"Destinos","pt":"Destinos"}[lang]
    about = {"fr":"À propos","es":"Sobre Nosotros","pt":"Sobre Nós"}[lang]
    guides = {"fr":"Guides","es":"Guías","pt":"Guias"}[lang]
    legal_url = {"fr":"/fr/mentions-legales.html","es":"/es/aviso-legal.html","pt":"/pt/aviso-legal.html"}[lang]
    legal_label = {"fr":"Mentions légales","es":"Aviso Legal","pt":"Aviso Legal"}[lang]
    disc_url = f"/{lang}/disclaimer.html"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XC1GYM27WC"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XC1GYM27WC');</script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9298895030863686" crossorigin="anonymous"></script>
    <title>{cfg['title']}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <meta name="robots" content="noindex, follow"/>
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700" rel="stylesheet"/>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css" rel="stylesheet"/>
    <link href="../css/animate.css" rel="stylesheet"/>
    <link href="../css/style.css" rel="stylesheet"/>
    <link rel="canonical" href="https://www.evisa-card.com/{lang}/{cfg['slug']}.html"/>
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
                <li class="nav-item"><a class="nav-link" href="../index.html">{home}</a></li>
                <li class="nav-item"><a class="nav-link" href="../destination.html">{dest}</a></li>
                <li class="nav-item"><a class="nav-link" href="../about.html">{about}</a></li>
                <li class="nav-item"><a class="nav-link" href="../blog.html">Blog</a></li>
                <li class="nav-item"><a class="nav-link" href="/{lang}/expat-guides.html">{guides}</a></li>
                <li class="nav-item dropdown ml-3">
                    <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.3);border-radius:4px;">
                        <span class="fi {flag}"></span> {label}</a>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="langDropdown">
                        <a class="dropdown-item" href="/en/{cfg['slug'] if cfg['slug']!='mentions-legales' else 'legal-notice'}.html"><span class="fi fi-gb"></span> English</a>
                        <a class="dropdown-item" href="/fr/{'mentions-legales' if page_type=='legal' else 'disclaimer'}.html"><span class="fi fi-fr"></span> Français</a>
                        <a class="dropdown-item" href="/es/{'aviso-legal' if page_type=='legal' else 'disclaimer'}.html"><span class="fi fi-es"></span> Español</a>
                        <a class="dropdown-item" href="/pt/{'aviso-legal' if page_type=='legal' else 'disclaimer'}.html"><span class="fi fi-br"></span> Português</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>

<section class="ftco-section">
<div class="container" style="max-width:860px;margin:60px auto;padding:0 20px;">
    <h1 style="margin-bottom:30px;">{cfg['h1']}</h1>
    {cfg['content']}
</div>
</section>

<footer class="ftco-footer bg-bottom ftco-no-pt" style="background-image: url(../images/bg_3.jpg);">
    <div class="container">
        <div class="row mb-5 justify-content-center">
            <div class="col-md-6 text-center">
                <p class="mt-4">© 2026 eVisa-Card.com</p>
                <p class="mt-2" style="font-size:13px;">
                    <a href="{legal_url}" style="color:#ffffff;text-decoration:underline;font-weight:500;">{legal_label}</a>
                    &nbsp;|&nbsp;
                    <a href="{disc_url}" style="color:#ffffff;text-decoration:underline;font-weight:500;">Disclaimer</a>
                </p>
            </div>
        </div>
    </div>
</footer>
<script src="../js/jquery.min.js"></script>
<script src="../js/popper.min.js"></script>
<script src="../js/bootstrap.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>"""

pages_created = 0
for lang in ["fr", "es", "pt"]:
    for ptype in ["legal", "disclaimer"]:
        cfg = {
            "fr": {"legal": "mentions-legales", "disclaimer": "disclaimer"},
            "es": {"legal": "aviso-legal", "disclaimer": "disclaimer"},
            "pt": {"legal": "aviso-legal", "disclaimer": "disclaimer"},
        }
        slug = cfg[lang][ptype]
        out = os.path.join(WWW, lang, f"{slug}.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(legal_page(lang, ptype))
        print(f"Created: {lang}/{slug}.html")
        pages_created += 1

print(f"\nLegal pages created: {pages_created}")
print("DONE")
