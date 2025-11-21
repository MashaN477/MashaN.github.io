
# Create About page
about_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me - My Life Blog</title>
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
        <section class="about-section">
            <h2>About Me</h2>
            <p>Welcome to my personal corner of the internet! My name is [Your Name], and this is where I share my life experiences, adventures, and the lessons I've learned along the way.</p>
            
            <p>I created this blog to document my journey and connect with others who might find inspiration or insight from my stories. Whether it's travel, personal growth, career experiences, or everyday observations, I believe that sharing our experiences helps us grow and learn from one another.</p>
            
            <p>When I'm not writing, you can find me [add your hobbies/interests here - e.g., exploring new hiking trails, reading books, trying new recipes, etc.].</p>
            
            <p>Thank you for stopping by, and I hope you enjoy reading my stories as much as I enjoy writing them!</p>
            
            <h3>Why I Started This Blog</h3>
            <p>In our fast-paced world, it's easy to forget the moments that shape us. This blog serves as both a personal archive and a way to share meaningful experiences with others. I believe everyone has a story worth telling, and this is mine.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

# Create Blog listing page
blog_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts - My Life Blog</title>
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
        <section class="featured-posts">
            <h2>All Blog Posts</h2>
            <div class="posts-grid">
                <article class="post-card">
                    <h3>My First Blog Post</h3>
                    <p class="post-date">November 17, 2025</p>
                    <p>This is my very first blog post! I'm excited to start sharing my experiences and stories with the world. In this post, I'll talk about why I decided to start this blog and what you can expect in future posts...</p>
                    <a href="post1.html" class="read-more">Read More →</a>
                </article>
                
                <article class="post-card">
                    <h3>An Adventure to Remember</h3>
                    <p class="post-date">November 15, 2025</p>
                    <p>Last weekend's adventure taught me so much about stepping outside my comfort zone. Here's what happened and what I learned from the experience...</p>
                    <a href="post2.html" class="read-more">Read More →</a>
                </article>
                
                <article class="post-card">
                    <h3>Lessons I've Learned</h3>
                    <p class="post-date">November 10, 2025</p>
                    <p>Looking back on the past few months, I've gathered some important insights that have changed my perspective on life, work, and relationships...</p>
                    <a href="post3.html" class="read-more">Read More →</a>
                </article>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

# Create Contact page
contact_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - My Life Blog</title>
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
        <section class="contact-section">
            <h2>Get in Touch</h2>
            <p>I'd love to hear from you! Whether you have questions, comments, or just want to connect, feel free to reach out.</p>
            
            <form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                
                <button type="submit" class="submit-button">Send Message</button>
            </form>
            
            <p style="margin-top: 2rem;">Note: To make this contact form work, sign up for a free account at <a href="https://formspree.io" target="_blank">Formspree.io</a> and replace YOUR_FORM_ID in the form action with your actual form ID.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

with open('about.html', 'w') as f:
    f.write(about_html)
    
with open('blog.html', 'w') as f:
    f.write(blog_html)
    
with open('contact.html', 'w') as f:
    f.write(contact_html)

print("✓ Created about.html")
print("✓ Created blog.html")
print("✓ Created contact.html")
