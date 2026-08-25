#!/usr/bin/env python3
"""
Static site generator for davidsonchua.cc

Single source of truth for the schema.org entity graph, nav, and page shells.
Run:  python3 _tools/build.py
Output: ./site/
"""
import json, os, shutil, datetime, html, re

BASE = "https://davidsonchua.cc"
OUT = "site"
TODAY = "2026-08-25"

# ---------------------------------------------------------------------------
# ENTITY GRAPH  — the single most important block on the site.
# Every page emits this identical graph. Consistency across pages and across
# off-site profiles is what lets Google resolve "Davidson Chua" to one entity.
# ---------------------------------------------------------------------------

PERSON_ID = f"{BASE}/#davidsonchua"
SITE_ID = f"{BASE}/#website"
INFLUENCEES_ID = "https://www.influencees.com/#organization"
AUTOSAVE_ID = "https://www.autosave.club/#organization"

SAME_AS = [
    "https://www.wikidata.org/wiki/Q141103594",
    "https://www.linkedin.com/in/davidsonchua/",
    "https://www.crunchbase.com/person/davidson-chua-cc",
    "https://davidsonchua.medium.com/",
    "https://x.com/davidsonchua",
    "https://www.helpareporter.com/journalist/davidsonchua",
    "https://t.me/davidsonchua",
    "https://baycityculture.com/",
]

PERSON = {
    "@type": "Person",
    "@id": PERSON_ID,
    "name": "Davidson Chua",
    "alternateName": ["Davidson Chua Chee Chuan", "Dav Chua"],
    "givenName": "Davidson",
    "familyName": "Chua",
    "url": f"{BASE}/",
    "mainEntityOfPage": {"@id": f"{BASE}/about#profilepage"},
    "image": {
        "@type": "ImageObject",
        "@id": f"{BASE}/#primaryimage",
        "url": f"{BASE}/assets/profile-800.webp",
        "width": 800,
        "height": 800,
        "caption": "Davidson Chua, founder of Influencees and Autosave, Singapore",
    },
    "jobTitle": ["Co-founder & CEO, Influencees", "Founder, Autosave"],
    "description": (
        "Davidson Chua is a Singapore-based founder and community builder. He is the "
        "co-founder and CEO of Influencees, an AI-powered creator credibility and discovery "
        "platform for Southeast Asia, and the founder of Autosave, Singapore's most active "
        "automotive community."
    ),
    "disambiguatingDescription": (
        "Singaporean technology founder (Influencees, Autosave); not to be confused with "
        "other individuals named Davidson Chua."
    ),
    "nationality": {"@type": "Country", "name": "Singapore"},
    "homeLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressCountry": "SG", "addressLocality": "Singapore"}},
    "worksFor": {"@id": INFLUENCEES_ID},
    "founder": [{"@id": INFLUENCEES_ID}, {"@id": AUTOSAVE_ID}],
    "alumniOf": [
        {
            "@type": "CollegeOrUniversity",
            "name": "National University of Singapore",
            "sameAs": "https://www.nus.edu.sg/",
        },
        {
            "@type": "CollegeOrUniversity",
            "name": "Singapore Polytechnic",
            "sameAs": "https://www.sp.edu.sg/",
        },
    ],
    "hasCredential": [
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "Bachelor's Degree",
            "name": "Bachelor of Science (Honours), Business Analytics",
            "recognizedBy": {"@type": "CollegeOrUniversity", "name": "National University of Singapore"},
        },
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "Diploma",
            "name": "Diploma with Merit, Marine Engineering",
            "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Singapore Polytechnic"},
        },
    ],
    "knowsAbout": [
        "Creator economy",
        "Influencer marketing",
        "Creator credibility and verification",
        "Community building",
        "Singapore automotive industry",
        "Electric vehicles in Singapore",
        "Business analytics",
        "Startup founding and growth",
        "Brand partnerships",
    ],
    "knowsLanguage": [{"@type": "Language", "name": "English"}],
    "subjectOf": [
        {
            "@type": "NewsArticle",
            "@id": "https://technode.global/2026/08/24/influencees-davidson-chua-on-measuring-creator-influence-beyond-follower-count-qa/#article",
            "headline": "Influencees' Davidson Chua on measuring creator influence beyond follower count [Q&A]",
            "url": "https://technode.global/2026/08/24/influencees-davidson-chua-on-measuring-creator-influence-beyond-follower-count-qa/",
            "datePublished": "2026-08-24",
            "author": {"@type": "Person", "name": "J. Angelo Racoma"},
            "publisher": {"@type": "Organization", "name": "TNGlobal", "url": "https://technode.global/"},
            "about": {"@id": PERSON_ID},
        },
        {
            "@type": "Article",
            "@id": "https://www.comp.nus.edu.sg/news/how-influencees-is-building-the-ai-layer-for-the-creator-economy/#article",
            "headline": "An NUS Computing Alumnus Developing an AI Tool That's Rethinking How Brands Find Creators",
            "url": "https://www.comp.nus.edu.sg/news/how-influencees-is-building-the-ai-layer-for-the-creator-economy/",
            "publisher": {"@type": "Organization", "name": "NUS School of Computing", "url": "https://www.comp.nus.edu.sg/"},
            "about": {"@id": PERSON_ID},
        },
    ],
    "email": "mailto:davidsonchua@outlook.com",
    "identifier": [
        {"@type": "PropertyValue", "propertyID": "Wikidata", "value": "Q141103594",
         "url": "https://www.wikidata.org/wiki/Q141103594"},
        {"@type": "PropertyValue", "propertyID": "Crunchbase", "value": "davidson-chua-cc",
         "url": "https://www.crunchbase.com/person/davidson-chua-cc"},
    ],
    "sameAs": SAME_AS,
}

INFLUENCEES = {
    "@type": "Organization",
    "@id": INFLUENCEES_ID,
    "name": "Influencees",
    "url": "https://www.influencees.com/",
    "description": (
        "AI-powered creator credibility and discovery platform for Southeast Asia. "
        "Influencees syncs data directly from Instagram and TikTok so brands can evaluate "
        "creators on verified engagement rather than self-reported follower counts."
    ),
    "foundingDate": "2026",
    "foundingLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressCountry": "SG"}},
    "founder": [
        {"@id": PERSON_ID},
        {"@type": "Person", "name": "Edwin Koh"},
    ],
    "sameAs": [
        "https://www.linkedin.com/company/influencees/",
        "https://www.instagram.com/influenceeshq",
        "https://x.com/influenceesHQ",
    ],
}

AUTOSAVE = {
    "@type": "Organization",
    "@id": AUTOSAVE_ID,
    "name": "Autosave",
    "legalName": "Autosave Pte. Ltd.",
    "url": "https://www.autosave.club/",
    "description": (
        "Singapore's most active automotive community, with 20,000+ members across Telegram "
        "and social channels, plus motoring media and owner meets."
    ),
    "foundingDate": "2022",
    "founder": {"@id": PERSON_ID},
    "identifier": {
        "@type": "PropertyValue",
        "propertyID": "UEN",
        "value": "202431449C",
    },
    "address": {"@type": "PostalAddress", "addressCountry": "SG", "addressLocality": "Singapore"},
    "award": "Best Automotive Community & Media Platform 2025 - Singapore (Corporate Vision Automotive Awards)",
    "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "Award",
        "name": "Best Automotive Community & Media Platform 2025 - Singapore",
        "recognizedBy": {"@type": "Organization", "name": "Corporate Vision — Automotive Awards"},
        "url": "https://www.corporatevision-news.com/winners/sg-cars/",
    },
    "sameAs": [
        "https://www.instagram.com/baycityculture",
        "https://www.corporatevision-news.com/winners/sg-cars/",
    ],
}

WEBSITE = {
    "@type": "WebSite",
    "@id": SITE_ID,
    "url": f"{BASE}/",
    "name": "Davidson Chua",
    "alternateName": "davidsonchua.cc",
    "description": "The official website of Davidson Chua, Singapore-based founder of Influencees and Autosave.",
    "inLanguage": "en-SG",
    "publisher": {"@id": PERSON_ID},
    "copyrightHolder": {"@id": PERSON_ID},
    "about": {"@id": PERSON_ID},
}

CORE_GRAPH = [PERSON, INFLUENCEES, AUTOSAVE, WEBSITE]


def breadcrumb(trail):
    """trail = [(name, path), ...]  path '' for home"""
    return {
        "@type": "BreadcrumbList",
        "@id": f"{BASE}/#breadcrumb",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": f"{BASE}{path}",
            }
            for i, (name, path) in enumerate(trail)
        ],
    }


# ---------------------------------------------------------------------------
# SHELL
# ---------------------------------------------------------------------------

NAV = [
    ("About", "/about"),
    ("Ventures", "/ventures"),
    ("Writing", "/writing"),
    ("Media", "/media"),
    ("Contact", "/contact"),
]


def nav_html(current):
    items = []
    for label, path in NAV:
        cur = ' aria-current="page"' if path == current else ""
        items.append(f'<a href="{path}"{cur}>{label}</a>')
    return "\n        ".join(items)


def head(*, title, desc, path, og_type="website", og_image=None, extra_head=""):
    canonical = f"{BASE}{path}"
    img = og_image or f"{BASE}/assets/og-image.png"
    return f"""<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="author" content="Davidson Chua">

  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Davidson Chua">
  <meta property="og:locale" content="en_SG">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Davidson Chua — Co-founder and CEO of Influencees, Founder of Autosave">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(desc)}">
  <meta name="twitter:image" content="{img}">
  <meta name="twitter:creator" content="@davidsonchua">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/assets/icon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#ffffff">

  <link rel="preload" as="image" href="/assets/profile-400.webp" fetchpriority="high">
  <link rel="stylesheet" href="/assets/site.css">
  <link rel="me" href="https://www.linkedin.com/in/davidsonchua/">
  <link rel="alternate" type="application/rss+xml" title="Davidson Chua — Writing" href="/writing/feed.xml">
{extra_head}"""


def page(*, path, title, desc, body, graph_extra=None, og_type="website",
         og_image=None, current=None, extra_head=""):
    graph = list(CORE_GRAPH) + (graph_extra or [])
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                        indent=2, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="en-SG">
<head>
  {head(title=title, desc=desc, path=path, og_type=og_type, og_image=og_image, extra_head=extra_head)}

  <script type="application/ld+json">
{jsonld}
  </script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="siteHeader">
    <div class="shell headerInner">
      <a class="brand" href="/">Davidson&nbsp;Chua</a>
      <nav class="nav" aria-label="Primary">
        {nav_html(current)}
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="siteFooter">
    <div class="shell">
      <div class="footGrid">
        <div>
          <div class="footName">Davidson Chua</div>
          <p class="footBio">Singapore-based founder and community builder. Co-founder &amp; CEO of
            <a href="https://www.influencees.com" rel="noopener">Influencees</a>; founder of
            <a href="https://www.autosave.club" rel="noopener">Autosave</a>.</p>
        </div>
        <nav class="footNav" aria-label="Footer">
          <a href="/about">About</a>
          <a href="/ventures">Ventures</a>
          <a href="/writing">Writing</a>
          <a href="/media">Media</a>
          <a href="/contact">Contact</a>
        </nav>
        <nav class="footNav" aria-label="Elsewhere">
          <a href="https://www.linkedin.com/in/davidsonchua/" rel="me noopener">LinkedIn</a>
          <a href="https://www.crunchbase.com/person/davidson-chua-cc" rel="me noopener">Crunchbase</a>
          <a href="https://davidsonchua.medium.com/" rel="me noopener">Medium</a>
          <a href="https://t.me/davidsonchua" rel="me noopener">Telegram</a>
        </nav>
      </div>
      <div class="footBase">
        <span>&copy; 2026 Davidson Chua</span>
        <span>Singapore</span>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def write(path, content):
    """path like '/about/' -> site/about/index.html"""
    rel = path.strip("/")
    d = os.path.join(OUT, rel) if rel else OUT
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", os.path.join(d, "index.html"))
