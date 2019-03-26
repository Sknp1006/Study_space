# 从flask包中导入Flask类
from flask import Flask

#将当前运行的主程序构建成Flask的应用
#以便接受用户的请求(request)并给出响应(response)
app = Flask(__name__)

#@app.route()是Flask中的路由定义,主要定义用户的访问路径
#'/'表示的是整个网站的根路径
# def index(),表示的是匹配到　@app.route() 后的访问路径之后的处理程序－－视图函数．所有的视图函数中必须要有一个return,return的后面可以是一个字符串或响应对象,表示的是要响应给客户端浏览器的内容是什么
@app.route('/')
def index():
    # return "<h1 style='color:red;'>这是我的第一个Flask Demo</h1>"
    return "<script>alert('这是我的第一个Flask Demo');</script>"


@app.route('/show')
def show():
    return "这是我的show访问路径"

# 带参数的路由
@app.route('/news/<year>')
def news(year):
    return "<h1>想看的年份为:"+year+"</h1>"

@app.route('/news/<year>/<month>')
def news1(year,month):
    return "年份:"+year+",月份:"+month

@app.route('/info/<name>/<int:age>')
def info(name,age):
    return "姓名：%s,年龄:%d" % (name, age)

# 127.0.0.1:5000/category
# 127.0.0.1:5000/cate
@app.route('/category')
@app.route('/cate')
def cate_views():
    return "这是category/cate对应的视图"

# 运行Flask的应用(启动Flask的服务),默认在本机开启的端口是5000
#debug=True:将以调试模式的方式启动服务(开发环境使用True,生产环境重病使用False)
if __name__ == "__main__":
    app.run(debug=True)















