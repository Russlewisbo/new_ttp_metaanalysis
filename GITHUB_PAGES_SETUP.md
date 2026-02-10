# Setting Up GitHub Pages for TTP Meta-Analysis Reports

This guide will help you publish your meta-analysis reports on GitHub Pages so they're accessible via a public URL.

## 📋 Quick Setup (5 Minutes)

### Step 1: Prepare Your Files

You already have these files ready:
- ✅ `index.html` - Landing page (just created)
- ✅ `TTP_MetaAnalysis_Report.html` - Main report
- ✅ `Clinical_Failure_Report.html` - Supplement

### Step 2: Commit and Push Files

Run these commands in Terminal (in your project directory):

```bash
# Make sure you're in the right directory
cd /Users/russelllewis/new_ttp_metaanalysis

# Add the new index page
git add index.html

# Add the reports if not already committed
git add TTP_MetaAnalysis_Report.html Clinical_Failure_Report.html

# Commit the changes
git commit -m "Add GitHub Pages website with meta-analysis reports"

# Push to GitHub
git push origin main
```

### Step 3: Enable GitHub Pages

1. Go to your GitHub repository: `https://github.com/yourusername/new_ttp_metaanalysis`
2. Click **Settings** (top right)
3. Scroll down to **Pages** in the left sidebar
4. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `main` and `/ (root)`
   - Click **Save**

### Step 4: Wait and Access

- GitHub Pages will build your site (takes 1-2 minutes)
- Your site will be available at: `https://yourusername.github.io/new_ttp_metaanalysis/`
- You'll see a message at the top with the URL once it's ready

---

## 🎨 What You'll Get

### Landing Page (index.html)
- Professional overview of the project
- Key findings summary
- Links to both reports
- Statistics cards
- Clinical implications
- Responsive design

### Individual Reports
- `https://yourusername.github.io/new_ttp_metaanalysis/TTP_MetaAnalysis_Report.html`
- `https://yourusername.github.io/new_ttp_metaanalysis/Clinical_Failure_Report.html`

---

## 📱 Features of Your Website

✅ **Professional Design**
- Modern, gradient background
- Responsive layout (mobile-friendly)
- Card-based design
- Easy navigation

✅ **Clear Information Hierarchy**
- Key findings highlighted
- Statistics displayed prominently
- Primary vs secondary reports clearly marked
- Clinical implications section

✅ **User-Friendly**
- Direct links to reports
- Quick overview without opening reports
- Helpful descriptions
- Clear call-to-action buttons

---

## 🔧 Troubleshooting

### Problem: 404 Error

**Solution 1:** Make sure files are in the root directory
```bash
ls -la | grep html
# Should see: index.html, TTP_MetaAnalysis_Report.html, Clinical_Failure_Report.html
```

**Solution 2:** Check GitHub Pages settings
- Go to Settings → Pages
- Verify branch is `main` and folder is `/ (root)`

**Solution 3:** Wait a bit longer
- First deployment can take up to 10 minutes
- Subsequent updates are faster (1-2 minutes)

### Problem: Reports Not Loading

**Check file names are exact:**
```bash
# Should match exactly (case-sensitive)
TTP_MetaAnalysis_Report.html
Clinical_Failure_Report.html
```

### Problem: Site Not Updating

**Force refresh:**
1. Clear browser cache
2. Try incognito/private window
3. Or add `?v=2` to URL: `yoursite.html?v=2`

---

## 🎯 Advanced: Custom Domain (Optional)

If you have a custom domain:

1. Create a file named `CNAME` in your repository
2. Add your domain name (e.g., `ttp-meta-analysis.yourdomain.com`)
3. Configure DNS settings with your domain provider
4. Add a CNAME record pointing to `yourusername.github.io`

---

## 📊 Updating Reports

When you regenerate reports:

```bash
# Regenerate reports in R
quarto::quarto_render("TTP_MetaAnalysis_Report.qmd")
quarto::quarto_render("Clinical_Failure_Report.qmd")

# Commit and push updates
git add TTP_MetaAnalysis_Report.html Clinical_Failure_Report.html
git commit -m "Update meta-analysis reports"
git push origin main

# GitHub Pages will auto-update in 1-2 minutes
```

---

## 🔒 Privacy Considerations

### Current Setup: Public
- Anyone with the URL can view your reports
- Reports are indexed by search engines
- Good for: Publications, presentations, sharing with colleagues

### To Make Private:

**Option 1: Private Repository (Requires GitHub Pro)**
- Change repository to private in Settings
- GitHub Pages still works but only accessible to collaborators

**Option 2: Password Protection**
- Not natively supported by GitHub Pages
- Would require external service or moving to Netlify/Vercel

**Option 3: Remove After Review**
- Publish temporarily
- Disable GitHub Pages when done
- Re-enable when needed

---

## 📝 Customization Tips

### Update the Landing Page

Edit `index.html` to:
- Change colors (edit CSS variables at top)
- Update your GitHub username in footer
- Add more details
- Change text/descriptions

### Add More Content

Create additional pages:
```html
<!-- Link from index.html -->
<a href="methods.html">Detailed Methods</a>
```

### Add Google Analytics (Optional)

Add before `</head>` in index.html:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR_GA_ID');
</script>
```

---

## ✅ Pre-Launch Checklist

Before you push to GitHub, verify:

- [ ] All HTML files are in root directory
- [ ] File names match exactly (case-sensitive)
- [ ] Reports open correctly in browser locally
- [ ] Links in index.html point to correct files
- [ ] Repository is public (unless you have GitHub Pro)
- [ ] Git repository is connected to GitHub remote

---

## 🚀 Launch Command Sequence

Copy and paste these commands:

```bash
cd /Users/russelllewis/new_ttp_metaanalysis

# Check status
git status

# Add all HTML files
git add index.html TTP_MetaAnalysis_Report.html Clinical_Failure_Report.html

# Commit
git commit -m "Add GitHub Pages site for TTP meta-analysis"

# Push
git push origin main

# Output will show: 
# To github.com:yourusername/new_ttp_metaanalysis.git
```

Then:
1. Go to GitHub.com → Your Repository
2. Settings → Pages
3. Select main branch, / (root)
4. Save
5. Wait 2 minutes
6. Visit: `https://yourusername.github.io/new_ttp_metaanalysis/`

---

## 📧 Sharing Your Reports

Once live, you can share:

**Main Site:**
```
https://yourusername.github.io/new_ttp_metaanalysis/
```

**Direct to Mortality Report:**
```
https://yourusername.github.io/new_ttp_metaanalysis/TTP_MetaAnalysis_Report.html
```

**Direct to Clinical Failure:**
```
https://yourusername.github.io/new_ttp_metaanalysis/Clinical_Failure_Report.html
```

---

## 🎓 Example Uses

### For Publication Submission
- Include URL in cover letter
- Reviewers can access full reports online
- Interactive exploration of results

### For Presentations
- QR code linking to reports
- Share URL in slides
- Audience can review later

### For Grant Applications
- Demonstrate completed work
- Easy access for reviewers
- Professional presentation

---

## 🛠️ Alternative: Netlify (If GitHub Pages Doesn't Work)

Netlify offers similar hosting with more features:

1. Go to [netlify.com](https://netlify.com)
2. Sign up (free)
3. Drag and drop your folder
4. Get instant URL
5. No Git required (but supported)

---

## ❓ Need Help?

Common resources:
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Pages Quick Start](https://pages.github.com/)
- [Troubleshooting Guide](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)

---

**Ready to launch?** Run the commands in Step 2 above! 🚀
