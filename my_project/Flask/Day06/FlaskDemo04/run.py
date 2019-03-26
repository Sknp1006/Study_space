from flask import Flask, request, render_template
import os, datetime

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
            # fname = f.filename

            # 采　用年月日时分秒微秒.扩展名 为文件命名
            # 拼用年月日时分秒微秒
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # 获取文件的扩展名
            ext = f.filename.split('.')[-1]
            # 将时间.扩展名拼出来
            fname = ftime + '.' + ext

            print("上传的文件名为:" + fname)
            # 2.2 将文件保存至static目录中
            # f.save('static/'+fname)

            # 使用绝对路径保存文件至static目录中
            basedir = os.path.dirname(__file__)
            upload_path = os.path.join(basedir, 'static', fname)
            f.save(upload_path)

        uname = request.form['uname']
        print('用户名称:' + uname)
        return "文件上传成功"


@app.route('/02-blog', methods=['GET', 'POST'])
def blog_views():
    if request.method == 'GET':
        return render_template('02-blog.html')
    else:
        title = request.form['title']
        type = request.form['type']
        content = request.form['content']
        print("标题为:" + title)
        print("类型为:" + type)
        print("内容为:" + content)
        # 处理上传的文件
        if 'picture' in request.files:
            # 1.获取文件
            f = request.files['picture']
            # 2.根据文件名称构建保存路径
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[-1]
            filename = ftime + "." + ext

            basedir = os.path.dirname(__file__)
            upload_path = os.path.join(basedir, 'static/upload', filename)
            print("图片路径:",upload_path)
            # 3.将文件保存至对应的目录处
            f.save(upload_path)
        return "博客发表成功"

if __name__ == '__main__':
    app.run(debug=True)
