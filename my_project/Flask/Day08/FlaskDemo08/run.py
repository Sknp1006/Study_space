from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/00-test')
def test_views():
    return "这是测试的地址"

@app.route('/01-setcookie')
def setcookie():
    # 通过make_response构建响应对象
    resp = make_response('保存cookies成功')
    #1.保存名称为uname值为Maria的cookie,存期为1年
    resp.set_cookie('uname','Maria',60*60*24*365)
    #2.保存名称为upwd值为123456的cookie,不指定时长
    resp.set_cookie('upwd','123456')
    # 响应: 保存cookies成功
    return resp

@app.route('/02-login',methods=['GET','POST'])
def login_views():
    if request.method == 'GET':
        #判断uname和upwd是否保存在cookies中
        if 'uname' in request.cookies and 'upwd' in request.cookies:
            #1.获取uname和upwd的值
            uname = request.cookies['uname']
            upwd = request.cookies['upwd']
            #2.判断值是否为admin
            if uname=='admin' and upwd=='admin':
                return "欢迎:"+uname
            return render_template('02-login.html')
        else:
            return render_template('02-login.html')
    else:
        #1.接收用户名和密码
        uname = request.form['uname']
        upwd = request.form['upwd']
        #2.判断用户名和密码的正确性
        if uname=='admin' and upwd == 'admin':
            #3.如果都为admin,判断是否要记住密码
            # 3.1如果记住密码则讲用户名和密码保存进cookies
            resp = make_response('登录成功')
            if 'isSaved' in request.form:
                max_age = 60*60*24*365
                resp.set_cookie('uname',uname,max_age)
                resp.set_cookie('upwd',upwd,max_age)
            return resp
        else:
            #4.如果不是admin,则给出错误提示
            return "用户名或密码错误<a href='/02-login'>登录</a>"

@app.route('/03-getcookie')
def getcookie_views():
    # print(request.cookies)
    if 'uname' in request.cookies:
        print("用户名:"+request.cookies['uname'])
    if 'upwd' in request.cookies:
        print("密码:"+request.cookies['upwd'])
    return "获取cookies成功"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')









