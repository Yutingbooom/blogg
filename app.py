from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# 模擬部落格資料
posts = [
    {
        'id': 1,
        'title': 'Flask 入門教學',
        'author': '小明',
        'content': 'Flask 是一個輕量級的 Python Web 框架，非常適合入門。這篇文章會帶你了解 Flask 的基本用法。'
    },
    {
        'id': 2,
        'title': 'Python 變數與資料型別',
        'author': '小華',
        'content': 'Python 支援多種資料型別，包括整數、浮點數、字串、列表、字典等。這篇文章將介紹它們的使用方式。'
    },
    {
        'id': 3,
        'title': '如何使用 Jinja2 渲染模板',
        'author': '小李',
        'content': 'Jinja2 是 Flask 的模板引擎，讓你可以在 HTML 中使用 {{ 變數 }} 與 {% for %} 迴圈等語法。'
    }
]

@app.route('/')
def index():
    """首頁：顯示所有文章列表"""
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    """單篇文章頁面"""
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """新增文章頁面"""
    if request.method == 'POST':
        # 取得表單資料
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        
        # 產生新文章 ID（假設是數字，並且會自動遞增）
        new_id = max([post['id'] for post in posts]) + 1 if posts else 1
        
        # 新增文章到 posts 清單
        new_post = {
            'id': new_id,
            'title': title,
            'author': author,
            'content': content
        }
        posts.append(new_post)
        
        # 跳轉到新文章的詳細頁面
        return redirect(url_for('post_detail', post_id=new_id))
    
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)
