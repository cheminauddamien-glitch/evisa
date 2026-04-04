# eVisa-Card.com — Site Management Guide

## Structure du projet

```
pacific-main/
├── www/                          # Contenu du site (A UPLOADER sur le serveur)
│   ├── index.html                # Page d'accueil EN
│   ├── sitemap.xml               # 13 085 URLs
│   ├── robots.txt
│   ├── css/                      # CSS (style.css inclut Bootstrap 4.5)
│   ├── js/                       # JS (jQuery, Bootstrap, plugins)
│   ├── images/                   # Images (logo, bg_1-5, destinations)
│   ├── fonts/                    # Polices
│   ├── en/                       # 1 309 pages anglais
│   ├── fr/                       # 1 311 pages français
│   ├── es/                       # 1 311 pages espagnol
│   ├── pt/                       # 1 311 pages portugais
│   ├── zh/                       # 1 310 pages chinois
│   ├── th/                       # 1 310 pages thaï
│   ├── ru/                       # 1 310 pages russe
│   ├── ar/                       # 1 310 pages arabe
│   ├── ja/                       # 1 310 pages japonais
│   └── ko/                       # 1 310 pages coréen
│
└── scripts/                      # Scripts Python de génération/maintenance
    ├── generators/               # 49 scripts de création de pages
    └── fixers/                   # 32 scripts de correction/optimisation
```

## Types de pages (par langue)

| Type | Pattern | Nombre | Exemple |
|------|---------|--------|---------|
| Visa pays | `visa-{pays}.html` | 48 | `visa-japan.html` |
| Visa par nationalité | `{pays}-visa-for-{nat}-citizens.html` | 960 | `japan-visa-for-canadian-citizens.html` |
| Extension visa | `{pays}-visa-extension.html` | 48 | `thailand-visa-extension.html` |
| Frais visa | `{pays}-visa-fees.html` | 48 | `australia-visa-fees.html` |
| Conditions visa | `{pays}-visa-requirements.html` | 48 | `japan-visa-requirements.html` |
| Délai traitement | `{pays}-visa-processing-time.html` | 49 | `france-visa-processing-time.html` |
| ETA/eVisa | `{pays}-eta.html` / `{pays}-evisa.html` | 14 | `australia-eta.html` |
| Schengen nationalité | `schengen-visa-for-{nat}-citizens.html` | 8 | `schengen-visa-for-indian-citizens.html` |
| Guides expatriation | `expat-guide-{pays}.html` | 16 | `expat-guide-thailand.html` |
| Index guides | `expat-guides.html` | 1 | `expat-guides.html` |
| Visa-free | `visa-free-countries-{nat}-passport.html` | 10 | `visa-free-countries-us-passport.html` |
| Guides thématiques | Divers | ~8 | `retirement-visa-guide.html` |
| FMM Mexique | `mexico-fmm-tourist-card.html` | 1 | |
| Hayya Qatar | `qatar-hayya-visa.html` | 1 | |

## Commandes utiles

### Régénérer le sitemap
```bash
cd scripts/fixers
python update_sitemap.py
```

### Propager les pages EN vers toutes les langues
```bash
cd scripts/generators
python gen_all_missing_langs.py
```

### Corriger les hreflang sur les guides
```bash
cd scripts/fixers
python fix_guide_hreflang.py
```

### Normaliser le CSS/JS sur toutes les pages
```bash
cd scripts/fixers
python normalize_assets.py
```

### Optimiser les meta/title SEO
```bash
cd scripts/fixers
python optimize_seo_meta.py
```

### Ajouter un nouveau pays guide expatriation
1. Ajouter les données dans `scripts/generators/gen_detailed_expat_guides.py`
2. Exécuter le script
3. Propager avec `gen_all_missing_langs.py`
4. Mettre à jour `expat-guides.html` (ajouter la carte pays)
5. Régénérer le sitemap

### Ajouter une nouvelle page visa
1. Créer la page dans `www/en/`
2. Propager : `python scripts/generators/gen_all_missing_langs.py`
3. Sitemap : `python scripts/fixers/update_sitemap.py`

## SEO

- **Sitemap** : `www/sitemap.xml` (13 085 URLs)
- **Schema JSON-LD** : FAQPage sur les pages nationalité, Article sur les guides
- **Hreflang** : 10 langues + x-default sur toutes les pages
- **Maillage interne** : bloc "Related Pages" en bas de chaque page visa

## Langues

| Code | Langue | Drapeau |
|------|--------|---------|
| en | English | fi-gb |
| fr | Français | fi-fr |
| es | Español | fi-es |
| pt | Português | fi-br |
| zh | 中文 | fi-cn |
| th | ไทย | fi-th |
| ru | Русский | fi-ru |
| ar | العربية | fi-sa |
| ja | 日本語 | fi-jp |
| ko | 한국어 | fi-kr |

## Upload sur le serveur

Uploader uniquement le dossier `www/` sur le serveur web. Les scripts dans `scripts/` sont des outils de maintenance locale.

```bash
# Exemple avec rsync
rsync -avz --delete www/ user@server:/var/www/evisa-card.com/
```
