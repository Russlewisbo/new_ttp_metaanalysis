# GitHub Pages Deployment Checklist ✅

Quick reference for deploying your TTP meta-analysis reports.

## Pre-Flight Check

- [x] Reports generated and saved as HTML
- [x] Landing page (index.html) created
- [x] All files in project root directory
- [x] Git repository initialized and connected to GitHub
- [ ] Ready to deploy!

## Deployment Commands

Copy and paste these into Terminal:

```bash
cd /Users/russelllewis/new_ttp_metaanalysis

git add index.html TTP_MetaAnalysis_Report.html Clinical_Failure_Report.html

git commit -m "Add GitHub Pages site for TTP meta-analysis"

git push origin main
```

## GitHub Settings (Do on Website)

1. ⬜ Go to `https://github.com/YOUR_USERNAME/new_ttp_metaanalysis`
2. ⬜ Click **Settings** (top tab)
3. ⬜ Click **Pages** (left sidebar)
4. ⬜ Set Source: **Deploy from a branch**
5. ⬜ Set Branch: **main** and **/ (root)**
6. ⬜ Click **Save**
7. ⬜ Wait 1-2 minutes
8. ⬜ Visit: `https://YOUR_USERNAME.github.io/new_ttp_metaanalysis/`

## Post-Deployment

- [ ] Landing page loads correctly
- [ ] Main report link works
- [ ] Clinical failure report link works
- [ ] All images and tables display
- [ ] Mobile view looks good
- [ ] Share URL with colleagues

## Your URLs

Replace `YOUR_USERNAME` with your GitHub username:

**Landing Page:**
```
https://YOUR_USERNAME.github.io/new_ttp_metaanalysis/
```

**Main Report:**
```
https://YOUR_USERNAME.github.io/new_ttp_metaanalysis/TTP_MetaAnalysis_Report.html
```

**Clinical Failure:**
```
https://YOUR_USERNAME.github.io/new_ttp_metaanalysis/Clinical_Failure_Report.html
```

## Troubleshooting

**404 Error?**
- Wait a few more minutes (first build takes up to 10 min)
- Check Settings → Pages shows green success message
- Verify branch is `main` and folder is `/ (root)`

**Reports Not Loading?**
- Check file names match exactly (case-sensitive)
- Clear browser cache or try incognito mode
- Verify files were pushed: Check repository on GitHub

**Need to Update?**
1. Regenerate reports in R
2. `git add *.html`
3. `git commit -m "Update reports"`
4. `git push origin main`
5. Wait 1-2 minutes for auto-update

## Files Deployed

- ✅ `index.html` (14 KB) - Landing page
- ✅ `TTP_MetaAnalysis_Report.html` (2.9 MB) - Main analysis
- ✅ `Clinical_Failure_Report.html` (1.9 MB) - Supplement

Total: ~4.8 MB of professional meta-analysis content!

---

**Status: Ready to Deploy! 🚀**

Run the commands above and you'll be live in 2 minutes!
