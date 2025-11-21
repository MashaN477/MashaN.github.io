
# Create a README file that explains the project
readme_content = """# My Personal Blog Website 🌟

A beautiful, modern personal blog to share your life experiences and stories!

## 📁 Project Structure

```
your-website/
├── index.html       # Homepage (landing page)
├── about.html       # About you page
├── blog.html        # Blog listing page
├── contact.html     # Contact form page
├── post1.html       # First blog post
├── post2.html       # Second blog post
├── post3.html       # Third blog post
├── style.css        # All the styling/design
└── README.md        # This file
```

## ✨ Features

- **Responsive Design**: Works perfectly on phones, tablets, and computers
- **Modern Look**: Professional gradient design with smooth animations
- **Easy to Edit**: No coding experience needed to update content
- **Fast Loading**: Lightweight and optimized
- **SEO Friendly**: Good for search engines
- **Free Hosting**: Hosted on GitHub Pages at no cost

## 🚀 Quick Start

1. Create a GitHub account at https://github.com
2. Create a new repository named `yourusername.github.io`
3. Upload all these files to your repository
4. Enable GitHub Pages in Settings → Pages
5. Visit `https://yourusername.github.io` after 5-10 minutes

**For detailed instructions, see the `setup-guide.md` file!**

## ✏️ How to Edit Content

### Update Your About Page
1. Click `about.html` on GitHub
2. Click the pencil icon (✏️) to edit
3. Replace the placeholder text with your information
4. Click "Commit changes"

### Write a New Blog Post
1. Copy an existing post file (e.g., `post3.html`)
2. Rename it (e.g., `post4.html`)
3. Edit the content
4. Add a link to it in `blog.html`
5. Commit your changes

### Change Colors
1. Open `style.css`
2. Find the gradient color codes (e.g., `#667eea`)
3. Replace with your preferred colors
4. Commit changes

## 🎨 Color Schemes

Try these color combinations in `style.css`:

- **Ocean Blue**: `#2E3192` and `#1BFFFF`
- **Sunset**: `#FF512F` and `#F09819`
- **Forest**: `#134E5E` and `#71B280`
- **Rose**: `#F857A6` and `#FF5858`
- **Purple** (current): `#667eea` and `#764ba2`

## 📸 Adding Images

1. Upload your image to GitHub (e.g., `photo.jpg`)
2. In any HTML file, add:
```html
<img src="photo.jpg" alt="Description" style="max-width: 100%; border-radius: 10px;">
```

## 🔧 Contact Form Setup

The contact form uses Formspree (free):

1. Sign up at https://formspree.io
2. Create a new form
3. Copy your form ID
4. In `contact.html`, replace `YOUR_FORM_ID` with your actual ID

## 💡 Tips

- Update your blog regularly (at least once a month)
- Keep posts between 300-800 words
- Use clear, descriptive titles
- Add relevant images to make posts more engaging
- Share your website link on your resume and LinkedIn

## 🐛 Troubleshooting

**Website not showing?**
- Wait 10 minutes after uploading
- Check repository name is correct: `yourusername.github.io`
- Verify GitHub Pages is enabled in Settings

**Changes not appearing?**
- Wait 1-2 minutes for GitHub to rebuild your site
- Clear your browser cache (Ctrl+F5 or Cmd+Shift+R)

## 📚 Resources

- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [HTML Tutorial](https://www.w3schools.com/html/)
- [CSS Tutorial](https://www.w3schools.com/css/)

## 🎯 Next Steps

1. Customize the About page with your story
2. Write your first real blog post
3. Share your website URL with friends and on social media
4. Add more pages (Portfolio, Resume, etc.)
5. Consider getting a custom domain (optional, costs ~$10/year)

## 📄 License

Feel free to use this template for your own personal website!

---

**Happy blogging!** 🎉

Made with ❤️ for aspiring bloggers and job seekers
"""

with open('README.md', 'w') as f:
    f.write(readme_content)

print("✓ Created README.md")
print("\n" + "="*60)
print("All files created successfully! 🎉")
print("="*60)
print("\nYou now have these files:")
print("  1. index.html (homepage)")
print("  2. about.html (about page)")
print("  3. blog.html (blog listing)")
print("  4. contact.html (contact form)")
print("  5. post1.html (blog post 1)")
print("  6. post2.html (blog post 2)")
print("  7. post3.html (blog post 3)")
print("  8. style.css (all styling)")
print("  9. README.md (project info)")
print(" 10. setup-guide.md (detailed setup instructions)")
print("\nNext step: Follow the setup-guide.md to get your website online!")
