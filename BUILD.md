# davidsonchua.cc — how this site is built

Every page shares one identical schema.org entity graph. That consistency is the whole
point, so **don't hand-edit the generated HTML** — edit the source and re-run the build.

## Files

- `_tools/build.py` — the entity graph (Person / Organization / WebSite), the page shell,
  `<head>` tags, nav and footer. Change facts about you here.
- `_tools/pages.py` — the content of each page, the blog posts, sitemap/robots/RSS/vercel.json.

## Build

```bash
PYTHONPATH=_tools python3 _tools/pages.py
```

Writes into `site/`. Requires Python 3 only — no dependencies.

## Adding a blog post

Add a dict to `POSTS` in `_tools/pages.py` (slug, title, desc, date, readable_date, body)
and re-run. Sitemap, RSS, the writing index and `BlogPosting` schema all update themselves.

## Deployment

Vercel, `cleanUrls: true`, `trailingSlash: false` — so `about/index.html` is served at
`/about`. Canonical host is the apex `davidsonchua.cc`; set www to redirect in Vercel →
Settings → Domains. To switch to www instead, change `BASE` in `_tools/build.py` and rebuild.
