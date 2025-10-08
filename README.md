# Yupeng Xie's Academic Homepage

This is the personal academic homepage of Yupeng Xie, built with [Jekyll](https://jekyllrb.com/) and based on the [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) template.

## 🚀 Quick Start

### Local Development

1. Install Ruby and Jekyll following the [Jekyll installation guide](https://jekyllrb.com/docs/installation/)

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Run the local server:
   ```bash
   ./run_server.sh
   ```
   or
   ```bash
   bundle exec jekyll serve --livereload
   ```

4. Open http://127.0.0.1:4000 in your browser

### GitHub Actions Setup

To enable automatic Google Scholar citation updates:

1. Go to your repository **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Add a secret with:
   - Name: `GOOGLE_SCHOLAR_ID`
   - Value: `Xt8HBrIAAAAJ` (your Google Scholar ID)

The GitHub Action will automatically:
- Run daily at 8:00 UTC
- Update citation statistics
- Store results in the `google-scholar-stats` branch

## 📝 Customization

### Update Personal Information

Edit `_config.yml` to update:
- Name, bio, location
- Email, social media links
- Google Scholar, GitHub, etc.

### Update Homepage Content

Edit `_pages/about.md` to modify:
- Introduction
- Publications
- News
- Research interests
- Awards and honors

### Add Photos

Place your images in the `images/` folder:
- `profile.png` - Your profile photo (recommended: 400x400px)
- `haichart.png` - Paper preview images

### Styling

Customize styles in `assets/css/main.css`

## 📂 Project Structure

```
.
├── _config.yml           # Site configuration
├── _pages/               # Page content
│   └── about.md         # Homepage content
├── _layouts/            # Page templates
│   └── default.html     # Default layout
├── _includes/           # Reusable components
│   ├── sidebar.html     # Sidebar with profile
│   └── footer.html      # Footer
├── assets/
│   ├── css/main.css     # Styles
│   └── js/main.js       # JavaScript
├── images/              # Images and photos
├── google_scholar_crawler/  # Citation crawler
└── .github/workflows/   # GitHub Actions
```

## 🎓 About

**Yupeng Xie**  
PhD Student  
Hong Kong University of Science and Technology (Guangzhou)  
Research: Intelligent Data Visualization

## 📄 License

This project is based on [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io), which is distributed under the MIT License.

## 🙏 Acknowledgments

- [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) template by RayeRen
- [Jekyll](https://jekyllrb.com/) static site generator
- [Font Awesome](https://fontawesome.com/) icons
- [Academicons](https://jpswalsh.github.io/academicons/) academic icons
