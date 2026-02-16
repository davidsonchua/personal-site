# 🚀 Deployment Guide - Step by Step

## What You Have

You now have a complete, SEO-optimized personal website with:
- Homepage (index.html)
- About page (about.html)
- Sitemap (sitemap.xml)
- Robots.txt (robots.txt)
- README documentation
- .gitignore file

## 📦 Files to Upload to GitHub

```
Your Repository Root/
├── index.html          ← Homepage
├── about.html          ← About page
├── sitemap.xml         ← For search engines
├── robots.txt          ← For search engines
├── README.md           ← Documentation
├── .gitignore          ← Git ignore file
└── assets/             ← Keep your existing assets folder
    ├── profile.jpeg
    └── media/
        ├── straits-times-feature.jpg
        ├── podcast-tech-city.jpg
        ├── podcast-tech-jobs.jpg
        └── podcast-gen-ai.jpg
```

## 🎯 Method 1: GitHub Web Interface (Easiest)

### Step 1: Go to Your Repository
1. Open your browser
2. Go to `github.com/yourusername/yourrepo`
3. Make sure you're on the `main` branch

### Step 2: Upload Files
1. Click the **"Add file"** button (top right)
2. Click **"Upload files"**
3. Drag and drop these files:
   - `index.html`
   - `about.html`
   - `sitemap.xml`
   - `robots.txt`
   - `README.md`
   - `.gitignore`
4. Scroll down and click **"Commit changes"**

### Step 3: Verify Assets Folder
1. Make sure your `assets/` folder exists with:
   - `profile.jpeg`
   - `media/` subfolder with all 4 images
2. If missing, upload them the same way

### Step 4: Enable GitHub Pages
1. Go to your repository **Settings**
2. Click **"Pages"** in the left sidebar
3. Under "Source", select **"main"** branch
4. Click **"Save"**
5. Wait 1-2 minutes
6. Your site will be live at `https://yourusername.github.io/yourrepo/`

### Step 5: Test Your Site
1. Visit `https://yourusername.github.io/yourrepo/`
2. Click around, test all links
3. Visit the `/about` page
4. Verify all images load

---

## 💻 Method 2: Using Git (Command Line)

### Prerequisites
- Git installed on your computer
- GitHub account connected

### Step 1: Clone or Navigate to Your Repo
```bash
# If you don't have the repo locally:
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# If you already have it:
cd path/to/yourrepo
```

### Step 2: Copy All Files
Copy these files to your repository root:
- index.html
- about.html
- sitemap.xml
- robots.txt
- README.md
- .gitignore

### Step 3: Commit and Push
```bash
# Add all files
git add .

# Commit with message
git commit -m "Add SEO-optimized website with About page"

# Push to GitHub
git push origin main
```

### Step 4: Enable GitHub Pages
Follow the same steps as Method 1, Step 4

---

## ⚡ Method 3: Using GitHub Desktop (GUI)

### Step 1: Open GitHub Desktop
1. Open GitHub Desktop app
2. Add your repository (if not already added)

### Step 2: Copy Files
1. Copy all files to your local repository folder
2. GitHub Desktop will automatically detect changes

### Step 3: Commit and Push
1. Review changes in GitHub Desktop
2. Add commit message: "Add SEO-optimized website with About page"
3. Click **"Commit to main"**
4. Click **"Push origin"**

### Step 4: Enable GitHub Pages
Follow the same steps as Method 1, Step 4

---

## 🔧 Using Custom Domain (davidsonchua.cc)

If you want to use your custom domain instead of GitHub Pages URL:

### Step 1: Configure GitHub Pages for Custom Domain
1. Go to repository **Settings** → **Pages**
2. Under "Custom domain", enter: `davidsonchua.cc`
3. Click **"Save"**
4. Check **"Enforce HTTPS"** (after DNS propagates)

### Step 2: Configure DNS Settings
Go to your domain registrar (where you bought davidsonchua.cc) and add:

**For apex domain (davidsonchua.cc):**
```
Type: A
Name: @
Value: 185.199.108.153
TTL: 3600

Type: A
Name: @
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @
Value: 185.199.111.153
TTL: 3600
```

**For www subdomain (optional):**
```
Type: CNAME
Name: www
Value: yourusername.github.io
TTL: 3600
```

### Step 3: Create CNAME File
1. In your repository root, create a file named `CNAME` (no extension)
2. Add one line: `davidsonchua.cc`
3. Commit and push

### Step 4: Wait for DNS Propagation
- Usually takes 1-24 hours
- Check status at https://www.whatsmydns.net/

---

## ✅ Post-Deployment Checklist

### Immediate Testing (Do Right After Upload)
- [ ] Homepage loads at your URL
- [ ] About page loads at your URL/about
- [ ] All navigation links work
- [ ] All social media links work
- [ ] All images display correctly
- [ ] Mobile responsive (test on phone)

### Within 24 Hours
- [ ] Submit sitemap to Google Search Console
- [ ] Request indexing for homepage
- [ ] Request indexing for about page
- [ ] Validate structured data with Rich Results Test

### Within 1 Week
- [ ] Create Wikidata entry
- [ ] Update LinkedIn with website link
- [ ] Get listed on Autosave team page
- [ ] Get listed on ROADS.sg
- [ ] Create Crunchbase profile

### Within 2-4 Weeks
- [ ] Monitor Google Search Console impressions
- [ ] Check if Knowledge Panel appears (search "Davidson Chua" in incognito)
- [ ] Monitor page rankings
- [ ] Check backlink profile

---

## 🆘 Common Issues & Solutions

### Issue: About page shows 404
**Solution:**
- Verify `about.html` is in root directory (same level as index.html)
- Check filename is exactly `about.html` (lowercase, no spaces)
- Clear browser cache (Cmd+Shift+R or Ctrl+Shift+R)
- Wait 2-3 minutes after pushing for GitHub to rebuild

### Issue: Images not loading
**Solution:**
- Verify `assets/` folder structure matches exactly
- Check image filenames match (case-sensitive)
- Verify images are in repository
- Check browser console for 404 errors

### Issue: Links don't work on custom domain
**Solution:**
- Remove leading slashes from links if using subdirectory
- If using custom domain, update paths in HTML if needed
- GitHub Pages serves from root, so `/about` should work

### Issue: GitHub Pages not enabled
**Solution:**
- Go to Settings → Pages
- Make sure "Source" is set to "main" branch
- Click "Save" again
- Wait 1-2 minutes and refresh

---

## 📞 Need Help?

If you run into issues:
1. Check the error message carefully
2. Search the issue on Google/Stack Overflow
3. Check GitHub Pages status: https://www.githubstatus.com/
4. Open an issue in your repository
5. Email: davidsonchua@outlook.com

---

## 🎉 Success Indicators

You'll know it's working when:
✅ Both pages load without errors
✅ All links are clickable
✅ Images display
✅ Rich Results Test shows valid Person schema
✅ Google Search Console shows pages indexed
✅ After 2-4 weeks: Knowledge Panel starts appearing

---

**Good luck with your deployment! 🚀**
