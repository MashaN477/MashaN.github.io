# Quick Reference Guide: Common Website Updates

This guide shows you how to do common tasks on your website. **No coding experience needed!**

---

## 📝 How to Write a New Blog Post

### Method 1: Copy an Existing Post (Easiest!)

1. Go to your repository on GitHub
2. Click on `post1.html`
3. Click the **Copy raw file** button (or click "Raw" and copy all the text)
4. Go back to your main repository page
5. Click **Add file** → **Create new file**
6. Name it something like `my-new-post.html`
7. Paste the copied code
8. Edit these parts:
   - `<title>` tag: Change the page title
   - `<h1>` tag: Change the main heading
   - `<p class="post-meta">`: Change the date
   - Replace all the content with your own story
9. Click **Commit changes**
10. Now add a link to it in `blog.html` (see next section)

### Method 2: From Scratch Template

Create a new file named `your-post-title.html` and use this template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Post Title - My Life Blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <div class="nav-container">
                <h1 class="logo">My Journey</h1>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <main>
        <article class="post-content">
            <h1>Your Post Title Here</h1>
            <p class="post-meta">Published on [Date]</p>
            
            <p>Your first paragraph goes here...</p>
            
            <h2>Section Heading</h2>
            
            <p>More content here...</p>
            
            <p><a href="blog.html" class="read-more">← Back to All Posts</a></p>
        </article>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>
```

---

## 🔗 How to Add Your New Post to the Blog List

After creating a new post, you need to add it to `blog.html`:

1. Open `blog.html` in GitHub
2. Click the pencil icon to edit
3. Find the section that looks like this:
```html
<article class="post-card">
    <h3>Lessons I've Learned</h3>
    <p class="post-date">November 10, 2025</p>
    <p>Looking back on the past few months...</p>
    <a href="post3.html" class="read-more">Read More →</a>
</article>
```

4. Copy this entire `<article>` section
5. Paste it right after (to add your post to the top)
6. Edit the copied section:
   - Change the `<h3>` to your post title
   - Change the date
   - Change the preview text
   - Change `href="post3.html"` to your new file name
7. Click **Commit changes**

**Example of what to add:**
```html
<article class="post-card">
    <h3>My Amazing Summer Trip</h3>
    <p class="post-date">November 18, 2025</p>
    <p>This summer I went on an incredible journey that changed my perspective on travel and adventure...</p>
    <a href="my-summer-trip.html" class="read-more">Read More →</a>
</article>
```

---

## 🎨 How to Change Website Colors

1. Open `style.css` in your GitHub repository
2. Click the pencil icon to edit
3. Look for lines with color codes like `#667eea` or `#764ba2`

### Main Colors to Change:

**Navigation Bar & Hero Section** (around line 15):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

**Links and Accent Colors** (around line 103):
```css
color: #667eea;
```

**Buttons** (around line 80):
```css
color: #667eea;
```

### Color Ideas:

Copy and paste these to replace the gradient line:

- **Ocean Blue**: `background: linear-gradient(135deg, #2E3192 0%, #1BFFFF 100%);`
- **Sunset Orange**: `background: linear-gradient(135deg, #FF512F 0%, #F09819 100%);`
- **Forest Green**: `background: linear-gradient(135deg, #134E5E 0%, #71B280 100%);`
- **Rose Pink**: `background: linear-gradient(135deg, #F857A6 0%, #FF5858 100%);`
- **Teal**: `background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);`

---

## 📸 How to Add Images

### Step 1: Upload Your Image

1. Go to your GitHub repository
2. Click **Add file** → **Upload files**
3. Drag your image file (must be .jpg, .png, or .gif)
4. Name it something simple: `photo1.jpg`, `vacation.png`, etc.
5. Click **Commit changes**

### Step 2: Add Image to a Blog Post

1. Open the blog post HTML file
2. Click the pencil icon to edit
3. Where you want the image, add this code:

```html
<img src="photo1.jpg" alt="Description of the photo" style="max-width: 100%; border-radius: 10px; margin: 2rem 0;">
```

**Replace:**
- `photo1.jpg` with your image filename
- `Description of the photo` with what the image shows

### Image Styling Options:

**Full width with rounded corners:**
```html
<img src="your-image.jpg" alt="Description" style="max-width: 100%; border-radius: 10px;">
```

**Centered with shadow:**
```html
<img src="your-image.jpg" alt="Description" style="max-width: 100%; border-radius: 10px; display: block; margin: 2rem auto; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
```

**Smaller image (50% width):**
```html
<img src="your-image.jpg" alt="Description" style="max-width: 50%; border-radius: 10px; display: block; margin: 1rem auto;">
```

---

## ✏️ How to Update the About Page

1. Open `about.html` in your repository
2. Click the pencil icon
3. Find the parts in `<p>` tags (paragraph tags)
4. Replace the placeholder text:
   - `[Your Name]` → Your actual name
   - `[add your hobbies/interests here]` → Your hobbies
   - The entire paragraphs → Your own story
5. Click **Commit changes**

---

## 🏠 How to Update the Homepage

1. Open `index.html`
2. Click the pencil icon
3. Look for the hero section (around line 20):

```html
<h2>Welcome to My Life Story</h2>
<p>A collection of my experiences, adventures, and lessons learned along the way</p>
```

4. Change the text to whatever you want
5. To update the featured posts preview, scroll down and edit the post cards

---

## 🎯 How to Change the Site Logo/Title

The site title appears in the top-left of every page.

1. Open any HTML file (like `index.html`)
2. Click the pencil icon
3. Find this line:
```html
<h1 class="logo">My Journey</h1>
```
4. Change "My Journey" to your preferred title
5. Click **Commit changes**
6. **Important**: You need to change this in ALL HTML files for consistency

**Pro Tip**: Use GitHub's search feature to find and replace "My Journey" in all files at once!

---

## 📧 How to Set Up the Contact Form

The contact form needs a service to actually send you emails.

1. **Sign up for Formspree**:
   - Go to https://formspree.io
   - Create a free account
   - Create a new form
   - Copy your form ID (looks like: `mxxxxxxx`)

2. **Update your website**:
   - Open `contact.html`
   - Click the pencil icon
   - Find this line:
   ```html
   <form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   - Replace `YOUR_FORM_ID` with your actual form ID
   - Click **Commit changes**

3. **Test it**:
   - Visit your contact page
   - Send yourself a test message
   - Check your email!

---

## 🔍 How to Make Your Site Show Up in Google

### 1. Add Meta Descriptions

In each HTML file, add this in the `<head>` section (right after the `<title>` tag):

```html
<meta name="description" content="A brief description of your website or this specific page">
```

### 2. Create a Sitemap

Create a new file called `sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourusername.github.io/</loc>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>https://yourusername.github.io/about.html</loc>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>https://yourusername.github.io/blog.html</loc>
    <changefreq>weekly</changefreq>
  </url>
</urlset>
```

Replace `yourusername` with your actual GitHub username.

### 3. Submit to Google

- Go to https://search.google.com/search-console
- Add your website
- Submit your sitemap

---

## 🚨 Common Problems & Solutions

### Problem: Website not showing up
**Solution**: 
- Wait 10-15 minutes after uploading files
- Check your repository name: must be `yourusername.github.io`
- Go to Settings → Pages and verify GitHub Pages is enabled

### Problem: Changes not appearing
**Solution**:
- Wait 1-2 minutes for GitHub to rebuild
- Clear your browser cache: Press Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
- Check that you clicked "Commit changes"

### Problem: Images not showing
**Solution**:
- Make sure the image filename in your HTML matches exactly (case-sensitive!)
- Verify the image was uploaded to the main folder (not a subfolder)
- Check the file extension is correct (.jpg, .png, etc.)

### Problem: Page looks broken
**Solution**:
- Check that `style.css` is in the same folder as your HTML files
- Verify all HTML files have this line in the `<head>` section:
  ```html
  <link rel="stylesheet" href="style.css">
  ```

### Problem: Links not working
**Solution**:
- Check spelling of filenames (case-sensitive!)
- Verify the linked file exists in your repository
- Make sure you're using the correct file extension (.html)

---

## 💡 Pro Tips

1. **Write regularly**: Update your blog at least once a month to keep it fresh
2. **Use descriptive titles**: Make it clear what each post is about
3. **Add images**: Posts with images are more engaging
4. **Keep it personal**: Share YOUR unique experiences and insights
5. **Proofread**: Check for typos before publishing
6. **Share it**: Add your website link to your resume, LinkedIn, and email signature

---

## 📱 Testing Your Website

Always check your website on different devices:
- Desktop computer
- Tablet
- Mobile phone

The website is designed to look good on all screen sizes!

---

## ⏰ Maintenance Checklist

**Weekly**:
- Write or draft a new blog post
- Check for broken links

**Monthly**:
- Review and update your About page
- Update your latest projects/achievements
- Check website loads correctly

**Quarterly**:
- Review old posts and update if needed
- Consider redesigning or refreshing the look

---

**Remember**: You don't need to be a coding expert to maintain this website. Most updates are just changing text! If you get stuck, refer back to this guide or the setup-guide.md file.

Happy blogging! 🎉
