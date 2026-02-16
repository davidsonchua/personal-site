# Davidson Chua - Personal Website

SEO-optimized personal website with Google Knowledge Panel support.

## 📁 File Structure

```
davidsonchua.cc/
├── index.html          # Homepage (portfolio view)
├── about.html          # About page (full story)
├── sitemap.xml         # Search engine sitemap
├── robots.txt          # Search engine instructions
└── assets/
    ├── profile.jpeg    # Your profile photo
    └── media/
        ├── straits-times-feature.jpg
        ├── podcast-tech-city.jpg
        ├── podcast-tech-jobs.jpg
        └── podcast-gen-ai.jpg
```

## 🚀 Quick Deploy to GitHub Pages

### Option 1: Using GitHub Web Interface

1. Go to your GitHub repository
2. Click "Add file" → "Upload files"
3. Drag and drop:
   - `index.html`
   - `about.html`
   - `sitemap.xml`
   - `robots.txt`
4. Make sure your `assets/` folder structure is preserved
5. Commit the changes
6. Enable GitHub Pages in Settings → Pages → Source: main branch

### Option 2: Using Git Command Line

```bash
# Clone your repo (or navigate to it)
git clone https://github.com/yourusername/davidsonchua.cc.git
cd davidsonchua.cc

# Copy the files to your repo directory
# (Place index.html, about.html, sitemap.xml, robots.txt in root)

# Add, commit, and push
git add .
git commit -m "Add SEO-optimized website with About page"
git push origin main
```

## ✅ Post-Deployment Checklist

### 1. Verify Files Load
- [ ] Visit https://davidsonchua.cc and verify homepage loads
- [ ] Visit https://davidsonchua.cc/about and verify about page loads
- [ ] Visit https://davidsonchua.cc/sitemap.xml and verify sitemap displays
- [ ] Visit https://davidsonchua.cc/robots.txt and verify robots.txt displays

### 2. Test Navigation
- [ ] Click "About" link in homepage nav
- [ ] Click "Back to home" in about page
- [ ] Click "View my work" button in about page
- [ ] All social/contact links work

### 3. Google Search Console Setup (CRITICAL for Knowledge Panel)

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add Property" → Enter `davidsonchua.cc`
3. Verify ownership (HTML tag method recommended)
4. Once verified:
   - Submit sitemap: `https://davidsonchua.cc/sitemap.xml`
   - Request indexing for homepage
   - Request indexing for about page

### 4. Validate Structured Data

1. Go to [Google Rich Results Test](https://search.google.com/test/rich-results)
2. Enter `https://davidsonchua.cc`
3. Verify Person schema is detected correctly
4. Repeat for `https://davidsonchua.cc/about`

### 5. Create Wikidata Entry (Important for Knowledge Panel)

1. Go to [Wikidata.org](https://www.wikidata.org)
2. Create an account
3. Click "Create new item"
4. Add:
   - Name: Davidson Chua
   - Occupation: Founder, Builder
   - Education: NUS (Business Analytics), Singapore Polytechnic (Marine Engineering)
   - Employer: Autosave
   - Website: https://davidsonchua.cc
   - Social profiles: LinkedIn, Telegram
   - Notable work: Featured in The Straits Times
5. Save and publish

### 6. Build Authority Backlinks

Within 1-2 weeks, get links from:
- [ ] Update LinkedIn profile → Add website to "Contact Info"
- [ ] Get listed on Autosave.club team/about page
- [ ] Get listed on ROADS.sg contributor page
- [ ] Create Crunchbase profile with website link
- [ ] Create AngelList profile with website link

## 🎯 SEO Features Included

### ✅ Technical SEO
- JSON-LD structured data (Person schema)
- Open Graph meta tags
- Twitter Card meta tags
- Semantic HTML5 elements
- Proper heading hierarchy
- Image optimization with alt text
- Mobile responsive
- Fast loading (minimal CSS, no external dependencies)

### ✅ On-Page SEO
- Keyword-optimized title tags
- Meta descriptions
- Canonical URLs
- Internal linking
- Breadcrumb schema (about page)
- Article/PodcastEpisode schema for media mentions

### ✅ Content SEO
- 1,200+ words on About page
- Natural keyword usage
- Clear content structure
- Compelling storytelling

## 📊 Tracking & Monitoring

### Google Search Console Metrics to Watch
- Impressions for "Davidson Chua"
- Knowledge Panel appearance
- Click-through rate (CTR)
- Average position for target keywords

### Target Keywords
**Primary:**
- Davidson Chua
- Davidson Chua Singapore
- Davidson Chua NUS
- Davidson Chua Autosave

**Secondary:**
- Singapore automotive community
- Mobility trends Singapore
- Community-led branding
- Road safety Singapore

## ⏱️ Expected Timeline

- **Week 1-2:** Google indexes pages, structured data processed
- **Week 2-4:** Knowledge Panel may start appearing (if Wikidata entry created)
- **Month 2-3:** Full SEO effects visible, improved rankings

## 🔧 Customization Notes

### Updating Content
- **Homepage:** Edit `index.html` sections
- **About page:** Edit `about.html` content
- **New pages:** Add to sitemap.xml with appropriate priority

### Adding More Pages
If you add `/projects` or `/blog` later:

1. Create the HTML file
2. Add to sitemap.xml:
```xml
<url>
  <loc>https://davidsonchua.cc/projects</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```
3. Add navigation links in index.html and about.html

## 🐛 Troubleshooting

**About page shows 404:**
- Verify `about.html` is in root directory (not in a subfolder)
- Check filename is exactly `about.html` (lowercase)
- Clear browser cache and try again

**Structured data not showing in Google:**
- Wait 1-2 weeks for Google to crawl
- Verify in Rich Results Test
- Check Search Console for errors

**Knowledge Panel not appearing:**
- Create Wikidata entry (most important!)
- Build authority backlinks
- Wait 2-4 weeks after deployment
- Request Knowledge Panel in Search Console

## 📞 Support

For questions about implementation:
- Open an issue in this repo
- Email: davidsonchua@outlook.com

## 📝 License

© 2026 Davidson Chua. All rights reserved.

---

**Last Updated:** February 16, 2026
**Version:** 1.0.0
