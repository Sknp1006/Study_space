from flask import Flask, render_template, request

app = Flask(__name__, template_folder='muban')


@app.route('/01-parent')
def parent_views():
    uname = '漩涡鸣人'
    return render_template('01-parent.html', uname=uname)


@app.route('/02-child')
def child_views():
    uname = "宇智波佐助"
    return render_template('02-child.html', uname=uname)


@app.route('/03-request')
def request_views():
    # print(request)
    # 查看request中所有的成员
    # print(dir(request))

    print("scheme:", request.scheme)
    print("method:", request.method)
    print("args:", request.args)
    print("form:", request.form)
    print("cookies:", request.cookies)
    print("files:", request.files)
    print("path:", request.path)
    print("full_path:", request.full_path)
    print("url:", request.url)
    print("headers:", request.headers)
    # 从request.headers取出Referer消息头
    ref = "没有请求源地址"
    if 'Referer' in request.headers:
        ref = request.headers['Referer']
    print("请求源地址为:" + ref)

    ref = request.headers.get('Referer', '/')
    print("ref的值为:" + ref)

    return "成功查看request对象"


@app.route('/04-form')
def form_views():
    return render_template("04-form.html")


@app.route('/05-get')
def get_views():
    # 获取请求提交的数据
    uname = request.args['uname']
    uage = request.args.get('uage')
    return "姓名:%s,年龄:%s" % (uname, uage)


@app.route('/06-post',methods=['POST','GET'])
def post_views():
    uname = request.form.get('uname')
    uage = request.form['uage']

    return "POST请求的数据为,uname:%s,uage:%s" % (uname,uage)


@app.route('/07-form',methods=['POST','GET'])
def form07_views():
    # 判断请求方式是GET还是POST
    # 如果是GET请求的话,则可以渲染07-form.html 模板
    # 如果是POST请求的话,则可以接收07-form.html提交过来的数据
    if request.method == 'GET':
        return render_template('07-form.html')
    else:
        #接收提交过来的account参数值
        account = request.form.get('account')
        #接收提交过来的hobby参数值(可能是多个)
        hobby = request.form.getlist('hobby')
        print("account:"+account)
        print("hobby:",hobby)
        return "接收数据成功!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
