from flask import request, Flask, render_template
from markupsafe import Markup
from ai_generator.generator import generate_blog_post
import markdown2

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
    html_content = Markup(markdown2.markdown(markdown_content))
    return render_template('blog.html', keyword=keyword, html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True) 