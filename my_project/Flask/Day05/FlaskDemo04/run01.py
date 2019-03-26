from flask import Flask, request, render_template
# 导入SQLAlchemy用于创建数据库的实例
from flask_sqlalchemy import SQLAlchemy
# 从flask_script包中导入Manager类,用于管理项目
from flask_script import Manager
# 从flask_migrate包中导入Migrate,MigrateCommand,用于做数据库的迁移
from flask_migrate import Migrate, MigrateCommand

# 导入pymysql 并将其视为 mysqldb
# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 通过app指定连接数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
# 取消SQLAlchemy的信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 设置自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 为app指定启动模式
app.config['DEBUG'] = True
# 创建数据库应用实例 - db
db = SQLAlchemy(app)

# 创建Manager对象并指定要管理的应用(app)
manager = Manager(app)
# 创建Migrate对象,并指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加子命令,允许做数据库迁移的子命令
# 为manager增加一个叫 db 的子命令,该子命令的具体操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


# 创建实体类-Users,映射到数据库中表名叫users表
# 创建字段-id,主键,自增
# 创建字段-username,长度为80的字符串,不允许为空,值唯一,增加索引
# 创建字段-age,整数,允许为空
# 创建字段-email,长度为120的字符串,值唯一,不允许为空
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(80),
        nullable=False, unique=True, index=True
    )
    age = db.Column(
        db.Integer, nullable=True
    )
    email = db.Column(
        db.String(120),
        unique=True, nullable=False
    )
    # 增加一个列:isActive(Boolean,默认为True)
    isActive = db.Column(db.Boolean, default=True)

    # 重写__repr__方法去定义其展现形式
    def __repr__(self):
        return "<Users:%r>" % self.username


# 实体类-Student(id,sname,sage,isActive)
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


# 实体类-Teacher(id,tname,tage)
class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个属性-isActive,默认值为True
    isActive = db.Column(db.Boolean, default=True)


# 实体类-Course(id,cname)
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)


@app.route('/')
def index():
    return "这是我的Flask应用"


@app.route('/01-add')
def add_views():
    # 通过Users实体类,向users表中增加一条数据
    users = Users()
    users.username = "王丹波"
    users.age = 35
    users.email = 'bobo@163.com'

    db.session.add(users)
    # db.session.commit()

    return "Register Users Success!"


@app.route('/02-register', methods=['GET', 'POST'])
def register_views():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']

        # isActive = False
        # if 'isActive' in request.form:
        #     isActive = True

        isActive = 'isActive' in request.form

        users = Users()
        users.username = username
        users.age = age
        users.email = email
        users.isActive = isActive

        db.session.add(users)
        return "注册成功"


@app.route('/03-query')
def query_views():
    # 1. 通过db.session.query 构建查询对象
    # query = db.session.query(Users)
    # print('query:',query)
    # print(' type:',type(query))

    # 2. 查询执行函数

    # users = db.session.query(Users).all()
    # for u in users:
    #     print("姓名:%s,年龄:%d,邮箱:%s" % (u.username, u.age, u.email))

    # user = db.session.query(Users).first()
    # print(user)

    # count = db.session.query(Users).count()
    # print("Users表中共有%d条数据" % count)

    # 3.查询过滤器函数-filter()
    # 3.1 查询Users实体中,年龄大于30岁的人的信息
    users=db.session.query(Users).filter(Users.age>30).all()
    for user in users:
        print("姓名:%s,年龄:%d" % (user.username,user.age))

    return "Query Success!!!"


@app.route('/04-queryall')
def queryall_views():
    # 查询Users中的所有的数据
    users = db.session.query(Users).all()
    # 将数据发送到04-queryall.html中显示
    return render_template('04-queryall.html',users=users)

if __name__ == "__main__":
    # app.run(debug=True)

    # 　通过manager启动服务
    manager.run()
    # 通过　manager 启动服务
    # python3 run01.py runserver
    # 问题1:无法指定调试模式(debug=True)
    # 解决方案: app.config['DEBUG']=True
    # 问题2:无法指定启动主机地址(host=0.0.0.0)
    # 解决方案: python3 run01.py runserver --host 0.0.0.0
    # 问题3:无法指定启动端口(port=5555)
    # 解决方案: python3 run01.py runserver --port 5555
    # 问题2和问题3整体解决方案:
    # python3 run01.py runserver --host 0.0.0.0 --port 5555









