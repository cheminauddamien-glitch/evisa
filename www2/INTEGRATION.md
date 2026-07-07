# Guide d'intégration — evisa-card.com v2026

> Comment générer les 13 000 pages statiques à partir du design system.

---

## 1. Structure des fichiers

```
/
├── assets/
│   └── css/
│       └── site.css          ← CSS global (seul fichier requis)
├── assets/
│   └── flags/                ← Drapeaux hébergés en local (prod)
│       ├── th.png, fr.png … (flagcdn.com/w40/{cc}.png)
│       └── th@2x.png …      (flagcdn.com/w80/{cc}.png)
└── [pages HTML générées par script]
```

---

## 2. Squelette `<head>` minimal (toutes pages)

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><!-- TITRE DYNAMIQUE --></title>
  <meta name="description" content="<!-- META DESCRIPTION -->">

  <!-- Canonical + hreflang (obligatoires) -->
  <link rel="canonical" href="https://evisa-card.com/<!-- CHEMIN PROPRE SANS .html -->">
  <link rel="alternate" hreflang="en"       href="https://evisa-card.com/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="fr"       href="https://evisa-card.com/fr/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="es"       href="https://evisa-card.com/es/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="de"       href="https://evisa-card.com/de/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="pt"       href="https://evisa-card.com/pt/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="ru"       href="https://evisa-card.com/ru/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="ar"       href="https://evisa-card.com/ar/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="zh"       href="https://evisa-card.com/zh/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="ja"       href="https://evisa-card.com/ja/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="ko"       href="https://evisa-card.com/ko/<!-- CHEMIN -->">
  <link rel="alternate" hreflang="x-default" href="https://evisa-card.com/<!-- CHEMIN -->">

  <!-- Robots (pages indexables) -->
  <meta name="robots" content="index, follow">
  <!-- Pour les pages légales/contact/404 : content="noindex, follow" -->

  <!-- Polices — Latin/Cyrillique uniquement (par défaut) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap">

  <!-- CSS global — seul fichier requis -->
  <link rel="stylesheet" href="/assets/css/site.css">

  <!-- JSON-LD (voir section 5) -->
  <script type="application/ld+json"><!-- JSON-LD selon template --></script>
</head>
```

### Polices additionnelles par langue

Injecter le `<link>` correspondant uniquement sur les pages de la langue concernée :

| Langue | `<link>` Google Fonts |
|---|---|
| `lang="ar"` | `family=IBM+Plex+Sans+Arabic:wght@400;500;600;700` |
| `lang="zh"` | `family=Noto+Sans+SC:wght@400;500;700` |
| `lang="ja"` | `family=Noto+Sans+JP:wght@400;500;700` |
| `lang="ko"` | `family=Noto+Sans+KR:wght@400;500;700` |
| `lang="th"` | `family=Noto+Sans+Thai:wght@400;500;700` |

### RTL (arabe)

Sur les pages arabes, ajouter `dir="rtl"` sur `<html>` :
```html
<html lang="ar" dir="rtl">
```
Aucune feuille CSS supplémentaire n'est nécessaire — le RTL est géré par les propriétés CSS logiques.

---

## 3. Templates HTML par type de page

### T1 — Hub pays (`/visa-{pays}`)

Classe sur `<body>` : `page-country-hub`

Structure obligatoire :
```
<header class="site-header"> (composant fixe)
<div class="section--breadcrumb"> + <nav aria-label="Breadcrumb"> + <ol class="breadcrumb">
<section class="hero-country">  ← flag + h1 + subtitle
<main id="main-content">
  <div class="container">
    <div class="page-layout">
      <div class="page-layout__main">
        <div class="visa-snapshot">         ← KPI card
        <nav class="toc">                   ← Table of contents
        <article class="article-body">      ← Contenu sectionné
          <section id="...">               ← h2 ancré pour le TOC
          <div class="table-wrap">          ← Tableaux responsive
          <ol class="steps">               ← Comment postuler
          <ul class="faq-list">            ← FAQ accordion
        </article>
        <div class="cta-banner">            ← Bannière CTA
        <div class="related-links">         ← Liens associés
      </div>
      <aside class="page-layout__aside">   ← Sidebar
        <div class="sidebar-card">
    </div>
  </div>
</main>
<footer class="site-footer">
```

### T2 — Page combinatoire (`/{dest}-visa-for-{nat}-citizens`)

Identique à T1 mais :
- Hero : `.hero-article` (plus compact) avec drapeaux des 2 pays
- Pas de sidebar sur mobile
- Snapshot card adaptée à l'éligibilité de la nationalité

### T3 — Pages info (`/{dest}-visa-requirements`, `-fees`, `-processing-time`, etc.)

```
hero-article + article-body + table-wrap (si applicable) + related-links
```
Pas de sidebar, article centré avec `container--article` (max 740 px).

### T4 — Listicle / Blog (`/blog/...`)

```
hero-article (avec date + reading time) + toc + article-body (sections h2/h3)
+ related-links en bas
```

### T5 — Répertoire (`/destination`)

```
hero-article + search-bar + filter tabs + dir-grid (groupes par continent)
```

### T6 — Institutionnel (`/about`, `/contact`, `/about-our-experts`)

```
hero-article + article-body (container--article, prose longue)
```

### T7 — Légal (`/disclaimer`, `/privacy`, `/legal-notice`, `/aviso-legal`)

Identique T6. Ajouter `<meta name="robots" content="noindex, follow">`.

### T8 — 404

```
<main> centré, pas de hero class, 404 + search + popular destinations
```

---

## 4. Composants — guide de classes

### Header
```html
<header class="site-header" role="banner">
  <div class="container">
    <div class="site-header__inner">
      <!-- Logo, nav-toggle, site-nav, lang-selector -->
    </div>
  </div>
</header>
```

**Active nav link :** ajouter `site-nav__link--active` sur le lien de la section courante.

### Breadcrumb
```html
<ol class="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
  <li class="breadcrumb__item" itemprop="itemListElement" ...>
    <a href="/" class="breadcrumb__link" itemprop="item"><span itemprop="name">Home</span></a>
    <meta itemprop="position" content="1">
  </li>
  <li class="breadcrumb__item">
    <span class="breadcrumb__current">Page actuelle</span>
  </li>
</ol>
```

### Visa Snapshot Card (4 KPIs)
```html
<div class="visa-snapshot">
  <div class="visa-snapshot__header"><!-- titre + date --></div>
  <div class="visa-snapshot__grid">
    <div class="visa-snapshot__kpi">
      <span class="visa-snapshot__kpi-label">Visa Type</span>
      <span class="visa-snapshot__kpi-value">eVisa</span>
      <span class="visa-snapshot__kpi-sub">Online application</span>
    </div>
    <!-- × 4, ajouter visa-snapshot__kpi--highlight sur le prix -->
  </div>
  <div class="visa-snapshot__footer"><!-- éligibilité + CTA --></div>
</div>
```

### Country Card
```html
<a href="/visa-{pays}" class="country-card">
  <span class="country-card__flag">
    <img src="/assets/flags/{cc}.png" alt="" loading="lazy" width="40" height="30">
  </span>
  <span class="country-card__info">
    <span class="country-card__name">Thailand</span>
    <span class="country-card__meta">eVisa · USD 35</span>
  </span>
  <svg class="country-card__arrow" ...><!-- chevron SVG --></svg>
</a>
```

### Tableau responsive
```html
<div class="table-wrap">
  <table class="data-table">
    <thead><tr><th scope="col">...</th></tr></thead>
    <tbody>
      <tr class="row--highlight"><!-- ligne mise en avant -->
        <td><strong>eVisa Tourist</strong></td>
        <td class="td--number">USD 35</td>
        <td class="td--free">Free</td>
      </tr>
    </tbody>
    <caption>Source et date</caption>
  </table>
</div>
```

Modificateurs de cellule : `.td--number` (valeurs numériques), `.td--free` (vert "gratuit"), `.row--highlight` (ligne vedette).

### Steps timeline
```html
<ol class="steps">
  <li class="step">
    <span class="step__number" aria-hidden="true">1</span>
    <div class="step__content">
      <h3 class="step__title">Titre de l'étape</h3>
      <div class="step__body"><p>Description...</p></div>
    </div>
  </li>
</ol>
```

### FAQ accordion (natif `<details>`)
```html
<ul class="faq-list" itemscope itemtype="https://schema.org/FAQPage">
  <li class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
    <details>
      <summary>
        <span itemprop="name">Question ?</span>
        <svg class="faq-icon" ...><!-- chevron --></svg>
      </summary>
      <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <div itemprop="text"><p>Réponse...</p></div>
      </div>
    </details>
  </li>
</ul>
```

### Alert box
```html
<!-- Variantes : alert--info | alert--warning | alert--official | alert--danger | alert--success -->
<div class="alert alert--info" role="note">
  <svg class="alert__icon" ...><!-- icône --></svg>
  <div class="alert__content">
    <p class="alert__title">Titre</p>
    <p class="alert__body">Corps de l'alerte.</p>
  </div>
</div>
```

### Badges
```html
<!-- Variantes : badge--brand | badge--success | badge--warning | badge--danger | badge--official | badge--neutral -->
<span class="badge badge--success">Updated 2026</span>
```

### Buttons
```html
<!-- Variantes : btn--primary (vert) | btn--secondary (contour bleu) | btn--ghost (blanc sur fond sombre) -->
<!-- Tailles : btn--sm | btn--lg (défaut = base) -->
<a href="..." class="btn btn--primary">Apply Now</a>
<a href="..." class="btn btn--secondary btn--sm">Learn more</a>
```

### Flag chip
```html
<span class="flag-chip">
  <img class="flag-chip__img" src="/assets/flags/{cc}.png" alt="" loading="lazy" width="20" height="15">
  Country Name
</span>
<!-- Cliquable : remplacer <span> par <a href="..."> -->
```

### CTA Banner
```html
<div class="cta-banner">
  <div class="cta-banner__content">
    <p class="cta-banner__title">Titre accrocheur</p>
    <p class="cta-banner__body">Description courte.</p>
  </div>
  <div class="cta-banner__actions">
    <a href="..." class="btn btn--primary">CTA primaire</a>
    <a href="..." class="btn btn--ghost">CTA secondaire</a>
  </div>
</div>
```

---

## 5. JSON-LD par template

### Hub pays — HowTo + FAQPage + BreadcrumbList
```json
[
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "item": { "@id": "https://evisa-card.com", "name": "Home" } },
      { "@type": "ListItem", "position": 2, "item": { "@id": "https://evisa-card.com/{continent}", "name": "{Continent}" } },
      { "@type": "ListItem", "position": 3, "item": { "@id": "https://evisa-card.com/visa-{pays}", "name": "{Pays} Visa" } }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Do I need a visa for {pays}?",
        "acceptedAnswer": { "@type": "Answer", "text": "..." }
      }
    ]
  }
]
```

### Listicle / Blog — Article
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "datePublished": "2026-01-01",
  "dateModified": "2026-06-01",
  "author": { "@type": "Organization", "name": "eVisaCard" }
}
```

### Homepage — WebSite + SearchAction
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "eVisaCard",
  "url": "https://evisa-card.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": { "@type": "EntryPoint", "urlTemplate": "https://evisa-card.com/destination?q={q}" },
    "query-input": "required name=q"
  }
}
```

---

## 6. JS minimal requis (inline dans chaque page)

```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Nav toggle (mobile)
  var toggle = document.querySelector('.nav-toggle');
  var nav    = document.querySelector('#main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open');
    });
  }
  // Language selector dropdown
  var langSel = document.querySelector('.lang-selector');
  if (langSel) {
    langSel.querySelector('.lang-selector__btn').addEventListener('click', function(e) {
      e.stopPropagation();
      langSel.classList.toggle('is-open');
    });
    document.addEventListener('click', function() { langSel.classList.remove('is-open'); });
  }
  // Back to top
  var btt = document.querySelector('.back-to-top');
  if (btt) {
    window.addEventListener('scroll', function() {
      btt.classList.toggle('is-visible', window.scrollY > 500);
    }, { passive: true });
    btt.addEventListener('click', function() { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }
});
</script>
```

---

## 7. Drapeaux — recommandations production

En dev : `https://flagcdn.com/w40/{cc}.png` (CDN externe).

**En production :** héberger localement dans `/assets/flags/` pour :
- Indépendance réseau
- Meilleure performance (serveur même domaine)
- Contrôle du cache

Script de téléchargement (bash) :
```bash
#!/bin/bash
CODES=(th vn jp in id my kh lk ae sa jo ke eg us gb fr de es pt au ca br mx tr ru cn ko ar)
for cc in "${CODES[@]}"; do
  curl -o "assets/flags/${cc}.png"   "https://flagcdn.com/w40/${cc}.png"
  curl -o "assets/flags/${cc}@2x.png" "https://flagcdn.com/w80/${cc}.png"
done
```

Puis remplacer `https://flagcdn.com/w40/{cc}.png` → `/assets/flags/{cc}.png` dans les templates.

---

## 8. Checklist de validation avant déploiement

### HTML
- [ ] Un seul `<h1>` par page
- [ ] Hiérarchie Hn correcte (h1 → h2 → h3)
- [ ] `alt=""` sur tous les drapeaux (décoratifs)
- [ ] `width` + `height` sur toutes les images (prévient le CLS)
- [ ] `loading="lazy"` sauf images above-the-fold

### SEO
- [ ] `<link rel="canonical">` (URL sans `.html`)
- [ ] Tous les hreflang × 10 + x-default
- [ ] `<meta name="description">` unique par page (150–160 chars)
- [ ] JSON-LD présent et valide (Rich Results Test)
- [ ] Fil d'Ariane visible et en microdata

### Accessibilité
- [ ] Skip link `.skip-link` en 1er enfant du body
- [ ] `<header role="banner">`, `<main>`, `<footer role="contentinfo">`, `<nav aria-label="...">`, `<aside>`
- [ ] Focus visible (ne pas `outline: none` sans alternative)
- [ ] Contrastes AA : texte normal ≥ 4,5:1, grand texte ≥ 3:1

### Performance
- [ ] `site.css` servi gzip + cache long terme (`?v=YYYYMMDD`)
- [ ] Polices Google : `display=swap` + `preconnect`
- [ ] Pas de JS bloquant dans `<head>` (tout en fin de body ou `DOMContentLoaded`)

---

## 9. URL pattern — règles de génération

| Type | Pattern | Exemple |
|---|---|---|
| Hub pays | `/visa-{country-slug}` | `/visa-thailand` |
| Combinatoire | `/{country-slug}-visa-for-{nationality-slug}-citizens` | `/thailand-visa-for-french-citizens` |
| Requirements | `/{country-slug}-visa-requirements` | `/thailand-visa-requirements` |
| Fees | `/{country-slug}-visa-fees` | `/thailand-visa-fees` |
| Processing | `/{country-slug}-visa-processing-time` | `/thailand-visa-processing-time` |
| Extension | `/{country-slug}-visa-extension` | `/thailand-visa-extension` |
| eVisa info | `/{country-slug}-evisa` | `/thailand-evisa` |
| ETA info | `/{country-slug}-eta` | `/australia-eta` |
| Listicle | `/{slug}` | `/best-countries-digital-nomads-2026` |
| Répertoire | `/destination` | `/destination` |
| Langue EN | `` (racine) | `/visa-thailand` |
| Autre langue | `/{lang}/{slug}` | `/fr/visa-thailand` |

**Règle absolue :** aucune extension `.html` dans les URL canoniques.
