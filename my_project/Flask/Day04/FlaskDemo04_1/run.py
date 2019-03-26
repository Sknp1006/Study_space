from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        # 1.从缓存区中获取名称为picture的文件
        if 'picture' in request.files:
            f = request.files['picture']
            # 2.将获取的文件使用其原始名称保存至static目录中
            # 2.1 获取文件名
            fname = f.filename
            print("上传的文件名为:" + fname)
            # 2.2 将文件保存至static目录中
            f.save('static/'+fname)
        uname=request.form['uname']
        print('用户名称:' + uname)
        return "文件上传成功"


if __name__ == '__main__':
    app.run(debug=True)
