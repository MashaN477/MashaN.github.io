
# Create sample blog post pages
post1_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Blog Post - My Life Blog</title>
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
            <h1>My First Blog Post</h1>
            <p class="post-meta">Published on November 17, 2025</p>
            
            <p>Welcome to my very first blog post! I'm excited to finally launch this website where I can share my experiences, thoughts, and the journey of my life.</p>
            
            <p>Starting a blog has been something I've wanted to do for a long time. I believe that documenting our experiences not only helps us reflect on our own growth but can also inspire and connect with others who might be going through similar situations.</p>
            
            <h2>Why I Started This Blog</h2>
            
            <p>There are several reasons why I decided to create this space:</p>
            
            <ul>
                <li><strong>Personal Growth:</strong> Writing helps me process my experiences and learn from them.</li>
                <li><strong>Sharing Knowledge:</strong> I want to share what I've learned with others who might find it helpful.</li>
                <li><strong>Building Connections:</strong> I hope to connect with people who have similar interests and experiences.</li>
                <li><strong>Career Development:</strong> A personal website showcases my writing skills and demonstrates initiative to potential employers.</li>
            </ul>
            
            <h2>What to Expect</h2>
            
            <p>In future posts, I'll be sharing stories about my adventures, career experiences, lessons learned, and reflections on life. Some posts will be deeply personal, while others might be more practical and informative.</p>
            
            <p>Thank you for being here at the beginning of this journey. I'm looking forward to sharing more with you!</p>
            
            <p><a href="blog.html" class="read-more">← Back to All Posts</a></p>
        </article>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

post2_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>An Adventure to Remember - My Life Blog</title>
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
            <h1>An Adventure to Remember</h1>
            <p class="post-meta">Published on November 15, 2025</p>
            
            <p>This is a template for your second blog post. Replace this content with your own story about an adventure or experience that was meaningful to you.</p>
            
            <h2>The Beginning</h2>
            
            <p>Start by setting the scene. Where were you? What led to this experience? What were you feeling at the time?</p>
            
            <h2>The Experience</h2>
            
            <p>Describe what happened. Use vivid details to bring your reader into the moment with you. What did you see, hear, feel?</p>
            
            <h2>What I Learned</h2>
            
            <p>Reflect on what this experience taught you. How did it change your perspective? What would you do differently next time?</p>
            
            <p><a href="blog.html" class="read-more">← Back to All Posts</a></p>
        </article>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

post3_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lessons I've Learned - My Life Blog</title>
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
            <h1>Lessons I've Learned</h1>
            <p class="post-meta">Published on November 10, 2025</p>
            
            <p>This is a template for your third blog post. Use this to share important lessons or insights from your experiences.</p>
            
            <h2>Lesson 1: [Your First Lesson]</h2>
            
            <p>Describe what you learned and how you came to understand this lesson. Share a specific example or story that illustrates this point.</p>
            
            <h2>Lesson 2: [Your Second Lesson]</h2>
            
            <p>Share another insight you've gained from your experiences. Explain why this lesson is important and how it has impacted your life.</p>
            
            <h2>Lesson 3: [Your Third Lesson]</h2>
            
            <p>Continue sharing your wisdom and reflections. Remember, your unique perspective is valuable!</p>
            
            <h2>Moving Forward</h2>
            
            <p>Conclude by discussing how these lessons will guide you in the future and what advice you'd give to others.</p>
            
            <p><a href="blog.html" class="read-more">← Back to All Posts</a></p>
        </article>
    </main>

    <footer>
        <p>&copy; 2025 My Life Blog. All rights reserved.</p>
    </footer>
</body>
</html>"""

with open('post1.html', 'w') as f:
    f.write(post1_html)
    
with open('post2.html', 'w') as f:
    f.write(post2_html)
    
with open('post3.html', 'w') as f:
    f.write(post3_html)

print("✓ Created post1.html")
print("✓ Created post2.html")
print("✓ Created post3.html")
