# Complete Guide to Your Portfolio Website

This guide explains everything about your portfolio website and how to update it.

## Table of Contents

1. [How Your Website Works](#how-your-website-works)
2. [Updating Content on GitHub.com](#updating-content-on-githubcom)
3. [Adding New Work Samples](#adding-new-work-samples)
4. [Adding New Articles](#adding-new-articles)
5. [Updating Your Resume](#updating-your-resume)
6. [Changing Site Settings](#changing-site-settings)
7. [Setting Up Google Analytics](#setting-up-google-analytics)
8. [Connecting Your Domain](#connecting-your-domain)
9. [Troubleshooting](#troubleshooting)

---

## How Your Website Works

### The Big Picture

Your website is built using three main technologies:

1. **Hugo** - Transforms your content (written in simple text files) into a beautiful website
2. **GitHub** - Stores all your files and hosts the website for free
3. **GitHub Actions** - Automatically rebuilds your site whenever you make changes

### What Happens When You Edit a File

```
You edit a file on GitHub.com
        ↓
GitHub saves your changes
        ↓
GitHub Actions automatically runs Hugo
        ↓
Hugo builds your website
        ↓
New website goes live (~1 minute)
```

**You never need to "build" or "deploy" manually** - it happens automatically!

---

## Updating Content on GitHub.com

This is the easiest way to update your portfolio. No coding knowledge required!

### Step-by-Step Instructions

1. **Go to your repository**
   - Visit: `https://github.com/YOUR-USERNAME/adityanarvekar.com`

2. **Navigate to the file you want to edit**
   - Click on the `content/` folder
   - Choose the file (e.g., `_index.md` for home page)

3. **Click the pencil icon** (Edit this file)

4. **Make your changes**
   - Edit the text using simple Markdown formatting

5. **Preview your changes** (optional)
   - Click the "Preview" tab to see how it will look

6. **Commit your changes**
   - Scroll to bottom
   - Add a brief description (e.g., "Updated bio")
   - Click "Commit changes"

7. **Wait for deployment**
   - Go to the "Actions" tab in your repository
   - Watch the deployment progress (takes ~1 minute)
   - Your site will update automatically!

### Understanding Markdown

Markdown is a simple way to format text. Here are the basics:

```markdown
# Large Heading
## Medium Heading
### Small Heading

**Bold text**
*Italic text*

- Bullet point 1
- Bullet point 2

[Link text](https://example.com)
```

---

## Adding New Work Samples

Work samples are stored in the `content/work/` folder. Each project is a separate file.

### Step 1: Prepare Your Materials

You'll need:
- **Preview image** - A screenshot or image representing the project (800x600px recommended)
- **PDF file** - Your project case study or presentation
- **Project details** - Title, company, one-sentence description

### Step 2: Upload Your Files

1. **Upload the preview image**
   - Go to `static/images/` in your repository
   - Click "Add file" → "Upload files"
   - Upload your image (e.g., `my-project.jpg`)
   - Click "Commit changes"

2. **Upload the PDF**
   - Create a `work` folder inside `static/` (if it doesn't exist)
   - Upload your PDF file (e.g., `my-project.pdf`)

### Step 3: Create the Work Sample File

1. **Navigate to** `content/work/`
2. **Click** "Add file" → "Create new file"
3. **Name your file:** `my-project.md` (use lowercase, hyphens instead of spaces)
4. **Paste this template:**

```markdown
---
title: "Your Project Title"
company: "Company Name"
description: "One sentence describing what you did and the impact."
image: "/images/my-project.jpg"
pdf: "/work/my-project.pdf"
date: 2024-01-15
---
```

5. **Replace the placeholder text** with your actual project details
6. **Click** "Commit changes"

**That's it!** Your new work sample will appear on the site in ~1 minute.

### Example

```markdown
---
title: "Mobile Banking App Redesign"
company: "FinTech Corp"
description: "Led UX redesign that increased user engagement by 45% and reduced support tickets by 30%."
image: "/images/banking-app.jpg"
pdf: "/work/banking-app-case-study.pdf"
date: 2023-11-20
---
```

---

## Adding New Articles

Articles you've written elsewhere are displayed in the Writing section.

### Step-by-Step

1. **Navigate to** `content/writing/`
2. **Click** "Add file" → "Create new file"
3. **Name your file:** `article-name.md`
4. **Paste this template:**

```markdown
---
title: "Your Article Title"
publication: "Where It Was Published"
external_url: "https://medium.com/@you/your-article"
date: 2024-01-15
---
```

5. **Fill in your details**
6. **Click** "Commit changes"

### Example

```markdown
---
title: "How We Scaled to 1 Million Users"
publication: "TechCrunch"
external_url: "https://techcrunch.com/2024/01/how-we-scaled"
date: 2024-01-10
---
```

---

## Updating Your Resume

Your resume appears in two forms:
1. **Displayed on the page** - Formatted nicely within the site
2. **Downloadable PDF** - Visitors can download the full version

### Updating the On-Page Resume

1. **Edit** `content/_index.md`
2. **Find the section** that starts with `resume_content: |`
3. **Update the text** using Markdown formatting
4. **Commit changes**

Example format:

```markdown
resume_content: |
  ### Experience

  #### Senior Product Manager | Tech Company
  *2020 - Present*

  - Achievement one
  - Achievement two
  - Achievement three

  #### Product Manager | Startup Inc
  *2018 - 2020*

  - Achievement one
  - Achievement two

  ### Education

  #### MBA | Business School
  *2018*

  ### Skills

  - Skill category one
  - Skill category two
```

### Updating the Downloadable PDF

1. **Navigate to** `static/` folder
2. **Upload your new** `resume.pdf` (it will replace the old one)
3. **Commit changes**

---

## Changing Site Settings

Site-wide settings are in `hugo.toml` at the root of your repository.

### Common Settings to Change

```toml
baseURL = 'https://www.adityanarvekar.com/'  # Your domain
title = 'Aditya Narvekar'                     # Your name
theme = 'apple-minimal'                        # Theme name (don't change)

[params]
  description = 'Professional Portfolio'       # Site description for SEO
  author = 'Aditya Narvekar'                   # Your name
  # google_analytics_id = 'G-XXXXXXXXXX'       # Uncomment to enable analytics
```

### Updating Contact Information

1. **Edit** `content/_index.md`
2. **Find the front matter** (section between `---`)
3. **Update these fields:**

```markdown
---
email: "your.email@example.com"
linkedin: "https://linkedin.com/in/yourprofile"
github: "https://github.com/yourusername"
twitter: "https://twitter.com/yourhandle"
---
```

4. **Remove any you don't want** to display
5. **Commit changes**

---

## Setting Up Google Analytics

Want to track how many people visit your site?

### Step 1: Get Your Google Analytics ID

1. **Go to** [analytics.google.com](https://analytics.google.com)
2. **Create an account** (if you don't have one)
3. **Create a property** for your website
4. **Choose** "Web" platform
5. **Copy your Measurement ID** (looks like `G-XXXXXXXXXX`)

### Step 2: Add It to Your Site

1. **Edit** `hugo.toml`
2. **Find this line:**
   ```toml
   # google_analytics_id = 'G-XXXXXXXXXX'
   ```
3. **Remove the `#` and replace the X's** with your actual ID:
   ```toml
   google_analytics_id = 'G-1234567890'
   ```
4. **Commit changes**

**Done!** Analytics will start tracking visitors within 24-48 hours.

---

## Connecting Your Domain

Right now your site is at `your-username.github.io`. Let's connect www.adityanarvekar.com!

### Step 1: Buy Your Domain

1. **Go to** [namecheap.com](https://namecheap.com)
2. **Search for** "adityanarvekar.com"
3. **Purchase the domain** (~$12/year)

### Step 2: Configure DNS Settings

1. **Log into Namecheap**
2. **Go to** Domain List → Manage
3. **Click** Advanced DNS
4. **Delete all existing records**
5. **Add these records:**

| Type  | Host | Value                  | TTL       |
|-------|------|------------------------|-----------|
| A     | @    | 185.199.108.153        | Automatic |
| A     | @    | 185.199.109.153        | Automatic |
| A     | @    | 185.199.110.153        | Automatic |
| A     | @    | 185.199.111.153        | Automatic |
| CNAME | www  | YOUR-USERNAME.github.io | Automatic |

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3: Configure GitHub Pages

1. **Go to your repository** on GitHub
2. **Click** Settings → Pages
3. **Under "Custom domain"**, enter: `www.adityanarvekar.com`
4. **Click** Save
5. **Wait 24-48 hours** for DNS to propagate

### Step 4: Enable HTTPS

1. **After DNS propagates**, return to Settings → Pages
2. **Check** "Enforce HTTPS"
3. **Your site is now live** at https://www.adityanarvekar.com! 🎉

---

## Troubleshooting

### My changes aren't showing up

**Check deployment status:**
1. Go to the "Actions" tab in your repository
2. Look for the latest workflow run
3. If it's red (failed), click on it to see the error
4. Most common issue: typo in YAML front matter (the section between `---`)

**Wait a moment:**
- Changes typically take 1-2 minutes to appear
- Try hard-refreshing your browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)

### My site shows a 404 error

- Check that GitHub Pages is enabled (Settings → Pages)
- Verify your repository is public
- Make sure the deployment workflow completed successfully

### Images aren't showing

- Check the image path starts with `/` (e.g., `/images/photo.jpg`)
- Verify the image was uploaded to the correct folder (`static/images/`)
- Image filenames are case-sensitive - match them exactly

### The dark mode toggle isn't working

- Hard refresh your browser to clear cached JavaScript
- Check browser console for errors (F12 → Console tab)

### I accidentally broke something

Don't panic! GitHub keeps a history of all changes.

1. **Go to the file** you edited
2. **Click** "History" button
3. **Find the last working version**
4. **Copy the content**
5. **Edit the current file** and paste the old content back
6. **Commit** to restore

---

## Getting Help

### Resources

- **Hugo Documentation:** [gohugo.io/documentation](https://gohugo.io/documentation/)
- **Markdown Guide:** [markdownguide.org](https://www.markdownguide.org/)
- **GitHub Pages Guide:** [pages.github.com](https://pages.github.com/)

### Need More Help?

If you're stuck:
1. Check if there's an error in the Actions tab
2. Review this guide for the specific task you're trying to do
3. Google the error message (usually very helpful!)
4. Ask ChatGPT or Claude to help troubleshoot

---

## Tips for Keeping Your Portfolio Updated

**Set a reminder:**
- Update quarterly with new projects and articles
- Keep your resume current

**Be consistent:**
- Use similar image dimensions for all work samples
- Keep descriptions roughly the same length
- Date format: YYYY-MM-DD

**Test before big updates:**
- If making major changes, test them locally first with `hugo server`
- Make one change at a time so you know what worked or broke

**Backup important PDFs:**
- Keep local copies of all your work PDFs
- GitHub stores everything, but local backups are good practice

---

You now have everything you need to maintain and update your portfolio website. Remember: the site rebuilds automatically whenever you commit changes to GitHub. Keep it updated, and it will serve you well in your career!
