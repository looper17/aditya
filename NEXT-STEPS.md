# Next Steps to Launch Your Portfolio

Your portfolio website is built! Here's what to do next:

## ✅ What's Done

- ✅ Hugo site with Apple-inspired design
- ✅ Dark/light mode toggle with localStorage
- ✅ Responsive mobile design
- ✅ CSS-only animations
- ✅ Work samples, writing, resume, and contact sections
- ✅ Footer navigation with smooth scrolling
- ✅ GitHub Actions for automatic deployment
- ✅ Google Analytics integration (ready to enable)
- ✅ Complete documentation

## 📋 What You Need to Do

### 1. Create GitHub Repository

```bash
# Make sure you're in the project directory
cd /Users/adityanarvekar/CC\ Work/adityanarvekar.com

# Create a new repository on GitHub.com first, then:
git remote add origin https://github.com/YOUR-USERNAME/adityanarvekar.com.git
git branch -M main
git push -u origin main
```

**Steps on GitHub.com:**
1. Go to https://github.com/new
2. Name: `adityanarvekar.com`
3. Make it **Public** (required for free GitHub Pages)
4. **DON'T** initialize with README (we already have one)
5. Click "Create repository"
6. Run the commands above

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Build and deployment":
   - Source: **GitHub Actions**
4. Save

The first deployment will start automatically when you push to GitHub.

### 3. Replace Placeholder Content

**Your information to add:**

1. **Home Page** (`content/_index.md`):
   - Replace professional title
   - Update bio text
   - Add real contact links (email, LinkedIn, GitHub, Twitter)
   - Update resume content

2. **Work Samples** (`content/work/`):
   - Delete placeholder projects
   - Add your real projects (see LEARN.md)
   - Upload preview images to `static/images/`
   - Upload PDF files to `static/work/` (create this folder)

3. **Writing** (`content/writing/`):
   - Delete placeholder articles
   - Add your real articles with links

4. **Resume PDF**:
   - Upload your resume as `static/resume.pdf`

### 4. Optional: Set Up Google Analytics

If you want visitor tracking:

1. Create account at https://analytics.google.com
2. Get your Measurement ID (G-XXXXXXXXXX)
3. Edit `hugo.toml`:
   ```toml
   google_analytics_id = 'G-YOUR-ACTUAL-ID'
   ```
4. Commit and push

### 5. Buy and Connect Your Domain

**Buy domain:**
- Go to https://namecheap.com
- Search for "adityanarvekar.com"
- Purchase (~$12/year)

**Connect domain:**
- Follow detailed instructions in LEARN.md under "Connecting Your Domain"
- DNS propagation takes 24-48 hours

## 🚀 Quick Commands Reference

```bash
# Preview site locally
hugo server

# View at: http://localhost:1313

# Deploy to GitHub (after setting up remote)
git add -A
git commit -m "Update content"
git push
```

## 📚 Documentation

- **README.md** - Quick start guide
- **LEARN.md** - Complete detailed guide for everything
- Both files are in the repository root

## ✨ Features You Have

1. **Automatic deployment** - Push to GitHub, site updates in ~1 minute
2. **Dark/light mode** - Toggle in top-right, preference saved
3. **Mobile responsive** - Looks great on all devices
4. **Fast loading** - Optimized CSS, minimal JavaScript
5. **PDF work samples** - Opens in new tab on desktop, download on mobile
6. **Footer navigation** - Quick links to all sections
7. **SEO ready** - Meta tags, semantic HTML

## 🎯 Test Checklist

After deploying, verify:

- [ ] Site loads at your-username.github.io/adityanarvekar.com
- [ ] Dark/light mode toggle works
- [ ] Refresh keeps dark mode preference
- [ ] All sections visible (Hero, About, Work, Writing, Resume, Contact)
- [ ] Footer links scroll smoothly
- [ ] Work samples open PDFs in new tab
- [ ] External links open in new tab
- [ ] Mobile layout looks good (use browser dev tools)
- [ ] Resume PDF downloads

## ❓ Need Help?

- Check LEARN.md for detailed instructions
- Review README.md for quick reference
- GitHub Actions tab shows deployment status and errors
- All content editable directly on GitHub.com

---

Your portfolio is ready to launch! 🎉

Start by creating the GitHub repository and enabling Pages, then gradually replace the placeholder content with your real information.
