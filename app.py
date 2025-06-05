from dotenv import load_dotenv
load_dotenv()
from flask import request, Flask, render_template, jsonify
from markupsafe import Markup
from ai_generator.generator import generate_blog_post
import markdown2
import scheduler
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate')
def generate_blog_post_route():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return 'Please provide a keyword using the ?keyword= parameter.', 400
    markdown_content = generate_blog_post(keyword)
    # Remove leading code block markers if present
    if markdown_content.strip().startswith('```markdown'):
        markdown_content = markdown_content.strip()[len('```markdown'):].lstrip('\n')
    if markdown_content.strip().endswith('```'):
        markdown_content = markdown_content.strip()[:-3].rstrip()
    # Save markdown to generated_posts folder
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    safe_keyword = keyword.replace(' ', '_')
    os.makedirs('generated_posts', exist_ok=True)
    filename = f"generated_posts/blog_{safe_keyword}_{today}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    html_content = Markup(markdown2.markdown(markdown_content))
    # Check for JSON request
    if request.args.get('format') == 'json' or request.headers.get('Accept') == 'application/json':
        return jsonify({
            'keyword': keyword,
            'markdown': markdown_content,
            'html': str(html_content)
        })
    return render_template('blog.html', keyword=keyword, html_content=html_content)

if __name__ == '__main__':
    scheduler.generate_and_save_daily_post()
    app.run(debug=True) 