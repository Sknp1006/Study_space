from flask import Flask, request, session, render_template, make_response
#name=admin  passsword=admin
app=Flask(__name__)
app.config['SECRET_KEY']='gongli1314520'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        if 'uname' in session and 'upwd' in session:
            uname=session['uname']
            return '欢迎:'+uname
        else:
            if 'uname' in request.form and 'upwd' in request.form:
                uname=request.cookies['uname']
                upwd=request.cookies['upwd']
                if uname=='admin' and upwd=='admin':
                    return '您已经登录过'
                else:
                    return render_template('login.html')
            else:
                return render_template('login.html')
    else:
        uname=request.form['uname']
        upwd=request.form['upwd']
        if uname=='admin' and upwd=='admin':
            session['uname']=uname
            session['upwd']=upwd
            resp=make_response('登陆成功,回到首页')
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname,60*60*24)
                resp.set_cookie('upwd',upwd,60*60*24)
            return resp
        else:
            return render_template('login.html',errMsg='您的用户或者密码错误')

if __name__ == '__main__':
    app.run()