# AI-Powered Blog Post Generator with Daily Automation

![3def63d8-9cb3-4a2d-98a1-0620dd354fd8](https://github.com/user-attachments/assets/d1f640bd-5dec-426b-9bf9-a8319d106968)

## Overview

This project is a modern, modular Flask application that uses OpenAI's GPT models to generate high-quality, SEO-optimized blog posts from a single keyword. It features:

- A beautiful, responsive web UI for on-demand blog generation.
- Automated daily blog post creation using a large set of trending keywords.
- SEO research (randomized for demo) and affiliate link support.
- Clean, production-ready code structure.

---

## Features

- **AI-Powered Blog Generation:** Enter any keyword and instantly get a full, well-structured blog post written by AI.
- **SEO Integration:** Each post is tailored with SEO metrics (randomized for demo) to simulate real-world research.
- **Modern UI:** Clean, responsive design for both desktop and mobile.
- **Markdown to HTML:** Blog posts are generated in Markdown and rendered as styled HTML.
- **Affiliate Link Placeholders:** Posts include affiliate link prompts, replaced with dummy URLs for easy monetization.
- **No Coding Required:** Simple web interface—just enter a keyword and click a button.
- **Daily Automation:** A scheduler automatically generates a new blog post every day using a random trending keyword, saving it to the `generated_posts/` directory.
- **Environment Variable Support:** Securely loads your OpenAI API key from a `.env` file.

---

## How It Works

1. **User Input:** On the home page, enter a keyword (e.g., "technology").
2. **AI & SEO:** The app fetches random SEO metrics and sends a detailed prompt to OpenAI's GPT model.
3. **Blog Generation:** The AI returns a markdown-formatted, SEO-optimized blog post.
4. **Display:** The post is converted to HTML and shown in a beautiful, readable format.
5. **Daily Automation:** Each day, the app picks a trending keyword and generates a new blog post automatically.
6. **Repeat:** Generate as many posts as you like, for any keyword!

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-blog-generator-interview-TushinKulshreshtha
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key

- Get your API key from [OpenAI](https://platform.openai.com/account/api-keys)
- Create a `.env` file in the project root:
  ```env
  OPENAI_API_KEY=your_openai_api_key_here
  ```

### 5. Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Project Structure

```
.
├── app.py
├── scheduler.py
├── ai_generator/
│   ├── __init__.py
│   ├── generator.py
│   └── seo_fetcher.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── blog.css
└── templates/
    ├── home.html
    └── blog.html
└── generated_posts/
    └── (auto-generated daily blog posts)
```

---

## How This App Helps You Write Blogs

- **Saves Time:** Instantly generates long-form, structured blog posts—no more writer's block.
- **SEO-Optimized:** Posts are tailored with SEO best practices and simulated SEO metrics.
- **Monetization Ready:** Includes affiliate link placeholders, replaced with dummy URLs for easy integration.
- **Professional Quality:** Uses OpenAI's advanced language models for natural, engaging, and informative content.
- **Easy to Use:** Just enter a keyword and get a ready-to-publish blog post.
- **Automated Content:** Never miss a day—fresh content is generated automatically every day.

---

## Customization & Extensibility

- Swap out the SEO metrics fetcher for real data sources if desired.
- Adjust the AI prompt in `ai_generator/generator.py` for different writing styles or requirements.
- Add user authentication, post saving, or export features as needed.
- Serve or display the auto-generated posts from the web interface.

---

## License

MIT License
