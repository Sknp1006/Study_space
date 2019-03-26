from flask import Flask,render_template

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')


# http://127.0.0.1:5000/login
@app.route('/login')
def login():
    return render_template('login.html')


# http://127.0.0.1:5000/list
@app.route('/list')
def list_views():
    return render_template('list.html')


# http://127.0.0.1:5000/register
@app.route('/register')
def register():
    return render_template('register.html')


# http://127.0.0.1:5000/info
@app.route('/info')
def info_views():
    return render_template('info.html')


if __name__ == "__main__":
    app.run(debug=True)
