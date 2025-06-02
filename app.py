from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate')
def generate_blog_post():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return 'Please provide a keyword using the ?keyword= parameter.', 400
    return f"<h2>Blog Post for: {keyword}</h2><p>This is a generated blog post about <b>{keyword}</b>.</p>", 200

if __name__ == '__main__':
    app.run(debug=True) 