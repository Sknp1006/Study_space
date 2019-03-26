from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    # return "<a href='/login'>登录</a>"

    # 通过　login 生成对应的访问地址 - 反向解析
    # url_login = url_for('login')
    # print("地址为:"+url_login)
    # return "<a href='%s'>登录</a>" % url_login

    # 通过　show 生成对应的访问地址　- 带参反向解析
    url_show=url_for('show',name='小泽Maria')
    return "<a href='%s'>显示</a>" % url_show;
    pass

@app.route('/manager/user/admin/auth/member/login')
def login():
    return "欢迎来到登录页面"

@app.route('/show/<name>')
def show(name):
    return "姓名为:"+name

if __name__ == "__main__":
    app.run(debug=True)