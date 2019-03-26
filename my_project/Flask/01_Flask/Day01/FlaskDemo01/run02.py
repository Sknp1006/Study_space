from flask import Flask

app = Flask(__name__)

# 127.0.0.1/login
@app.route('/login')
def login():
    return "欢迎来到登录页面"

# 127.0.0.1/register
@app.route('/register')
def register():
    return "欢迎来到注册页面"

# 127.0.0.1:5000/
# 127.0.0.1:5000/index
# 127.0.0.1:5000/<page>
# 127.0.0.1:5000/index/<page>
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
@app.route('/index/<int:page>')
def index(page=1):
    return "<h1>您当前想看的页数为:%d</h1>" % page



if __name__ == "__main__":
    app.run(debug=True)