import math
from flask import Flask, request, render_template,redirect
# 导入SQLAlchemy用于创建数据库的实例
from flask_sqlalchemy import SQLAlchemy
# 从flask_script包中导入Manager类,用于管理项目
from flask_script import Manager
# 从flask_migrate包中导入Migrate,MigrateCommand,用于做数据库的迁移
from flask_migrate import Migrate, MigrateCommand
# 从sqlalchemy 包中导入or_
from sqlalchemy import or_
# 从sqlalchemy 中导入func以便使用聚合函数
from sqlalchemy import func

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

# 声明一个全局变量,用于接收修改之前的请求源地址
url_referer = None

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
    # 做与Wife类之间的一对一的关联属性和反向引用关系属性
    wife = db.relationship("Wife",backref="user",uselist=False)

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
    # 增加一个列,引用自Course类(表)的主键(id)
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id'),
        nullable=True
    )


# 实体类-Course(id,cname)
class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    #增加关联属性和反向引用关系属性
    #关联属性:在Course的对象中要通过哪个属性引用对应的所有的Teacher对象
    #反向引用关系属性:在Teacher的对象中要通过哪个属性引用对应的Course对象
    teachers = db.relationship('Teacher',backref='course',lazy='dynamic')
    #增加对Student类的多对多操作(关联属性和反向引用关系属性)
    students = db.relationship(
        "Student",
        secondary = 'student_course',
        lazy = 'dynamic',
        backref = db.backref(
            "courses",
            lazy = "dynamic"
        )
    )



# 增加一个实体类-Wife,要与Users实体类做一对一的关联映射
class Wife(db.Model):
    __tablename__ = "wife"
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(20))
    wage = db.Column(db.Integer)
    #增加外键,表示与Users表的一对一关系
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)

# 实体类- StudentCourse,表示Student和Course之间的第三张关联表
class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    id = db.Column(db.Integer,primary_key=True)
    #外键:引用自student表的主键
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id")
    )
    #外键:引用自course表的主键
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )

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
    users = db.session.query(Users).filter(Users.age > 30).all()
    for user in users:
        print("姓名:%s,年龄:%d" % (user.username, user.age))

    return "Query Success!!!"


@app.route('/04-queryall')
def queryall_views():
    # 查询Users中的所有的数据
    users = db.session.query(Users).all()
    # 将数据发送到04-queryall.html中显示
    return render_template('04-queryall.html', users=users)


@app.route('/05-query_or')
def query_or():
    # 查询年龄大于40或id大于1的人的信息
    users = db.session.query(Users).filter(
        or_(Users.age > 40, Users.id > 1)
    ).all()

    for u in users:
        print("ID:%d,姓名:%s,年龄:%d" % (u.id, u.username, u.age))

    return "Query Success!"


@app.route('/06-query_like')
def query_like():
    # 查询email中包含maria的用户的信息
    users = db.session.query(Users).filter(
        Users.email.like('%maria%')
    ).all()
    for u in users:
        print("姓名:%s,邮箱:%s" % (u.username, u.email))

    return "Query Success"


@app.route('/07-query_like_exer')
def query_like_exer():
    uname = request.args.get('uname', '')
    # 如果uname不为空的话，则按照条件筛选
    if uname:
        # users = db.session.query(Users).filter(Users.username.like('%' + uname + '%')).all()

        # 在username和email中搜索关键字满足的数据
        users = db.session.query(Users).filter(
            or_(
                Users.username.like('%' + uname + '%'),
                Users.email.like('%' + uname + '%')
            )
        )
    else:
        # 否则查询所有数据
        users = db.session.query(Users).all()

    return render_template('07-like.html', users=users, uname=uname)


@app.route('/08-limit')
def limit_views():
    # 取users表中前2条数据
    users = db.session.query(Users).limit(2).all()
    for u in users:
        print("姓名:%s,邮箱:%s" % (u.username, u.email))

    return "Query Success"


@app.route('/09-offset')
def offset_views():
    users = db.session.query(Users).offset(3).limit(5).all()
    for u in users:
        print("姓名:%s,邮箱:%s" % (u.username, u.email))
    return "Query Success"


@app.route('/10-page')
def page_views():
    # 变量-pageSize,表示每页所显示的记录数量
    pageSize = 2
    # 接收前端传递过来的参数-page,如果没有传递进来,则默认为1,并保存在page变量中
    page = int(request.args.get('page', 1))
    # 查询第page页的数据
    # 跳过(page-1)*pageSize条数据后再取前pageSize条数据
    # ost表示的要跳过的记录数
    ost = (page - 1) * pageSize
    users = db.session.query(Users).offset(ost).limit(pageSize).all()
    # 计算尾页
    # 根据pageSize和总记录数计算尾页页码
    totalCount = db.session.query(Users).count()
    # 计算尾页并保存在lastPage变量中
    lastPage = math.ceil(totalCount / pageSize)
    # 计算上一页
    # 通过page计算上一页,并保存在变量prePage中
    prePage = 1  # 设置上一页默认为1
    # 如果page大于1的话,上一页则为page-1
    if page > 1:
        prePage = page - 1
    # 计算下一页
    # 通过page计算下一页,并保存在变量nextPage中
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1
    return render_template("10-page.html", users=users, lastPage=lastPage, prePage=prePage, nextPage=nextPage)


@app.route('/11-aggregate')
def aggregate_views():
    # 1.查询users表中所有人的平均年龄
    # result = db.session.query(func.avg(Users.age)).all()
    # print("result:",result)
    # print("平均年龄为:%.2f" % result[0][0])

    # 2.查询users表中所有人的平均年龄,总年龄,最大年龄,最小年龄分别是多少
    # result = db.session.query(
    #     func.avg(Users.age),
    #     func.sum(Users.age),
    #     func.max(Users.age),
    #     func.min(Users.age)
    # ).all()
    # print("result:",result)
    # print("平均年龄:%.2f,总年龄:%.2f,最大年龄:%d,最小年龄:%d" % (result[0][0],result[0][1],result[0][2],result[0][3]))

    # 3.分组聚合-按isActive分组求每组的人数
    # sql:select isActive,count(*) from users group by isActive
    users = db.session.query(
        Users.isActive,
        func.count('*')
    ).group_by('isActive').all()
    print(users)
    for r in users:
        print(r[0], ":", r[1])
    return "Aggregate query success"


@app.route('/12-update')
def update_views():
    # 1.查询出id为4的用户的信息
    user = Users.query.filter_by(id=4).first()
    # 2.将其isActive修改为True
    user.isActive = True
    # 3.将其保存回数据库
    db.session.add(user)

    return "修改成功"


@app.route('/13-delete')
def delete_views():
    # 查询id为4的用户的信息
    user = Users.query.filter_by(id=4).first()
    # 删除该信息
    db.session.delete(user)
    return "删除成功"

@app.route('/14-delete')
def deleteuser_views():
    # 1.接收前端传递过来的参数id
    id = request.args.get('id')
    # 2.删除指定id对应的元素
    u = Users.query.filter_by(id=id).first()
    db.session.delete(u)
    return redirect('/10-page')

@app.route('/15-update',methods=['GET','POST'])
def update15_views():
    if request.method == 'GET':

        # 记录请求源地址,并保存给url_referer全局变量
        global url_referer
        url_referer = request.headers.get('Referer')

        #1.接收id并查询相关数据
        id = request.args.get('id')
        user = Users.query.filter_by(id=id).first()
        #2.响应给模板
        return render_template("15-update.html",user=user)
    else:
        print("请求源地址:"+url_referer)
        # 1.接收前端传递过来的数值
        id = request.form['id']
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        isActive = False
        if 'isActive' in request.form:
            isActive = True
        # 2.根据id查询对应的user对象
        user = Users.query.filter_by(id=id).first()
        # 3.为user对象重新赋值
        user.username = username
        user.age = age
        user.email = email
        user.isActive = isActive
        # 4.重新保存对象
        db.session.add(user)

        return redirect(url_referer)


@app.route('/16-regteacher')
def regteacher():
    #方案1:通过外键列设定关联数据
    # teacher = Teacher()
    # teacher.tname = '魏老师'
    # teacher.tage = 47
    # teacher.isActive = True
    # teacher.course_id = 1
    # db.session.add(teacher)

    # 方案2:通过反向引用关系属性
    # 1.获取id为2的课程对象
    course=Course.query.filter_by(id=2).first()
    # 2.声明一个Teacher对象,并将course赋值给Teacher对象的course属性
    teacher = Teacher()
    teacher.tname = '王丹波'
    teacher.tage = 36
    teacher.isActive = True
    teacher.course = course
    db.session.add(teacher)
    return "增加老师成功!"


@app.route('/17-query')
def query17_views():
    #1.通过teacher对象查询对应的course信息
    # teacher=Teacher.query.filter_by(tname='魏老师').first()
    # 通过teacher.course属性获取对应的course
    # print("老师:"+teacher.tname)
    # print("所教课程:"+teacher.course.cname)

    # 2.通过course查询对应的老师们
    course=Course.query.filter_by(id=2).first()
    # print(course.teachers)
    # print(type(course.teachers))
    teachers=course.teachers.all()
    for tea in teachers:
        print("姓名:%s,课程:%s" % (tea.tname,tea.course.cname))

    return "Query OK"


@app.route('/18-query')
def query18_views():
    #获取所有的课程
    courses = Course.query.all()
    #接收前端传递过来的id值
    #有id的话则查询对应的课程的老师
    #没有id的话则查询所有的老师
    if 'id' in request.args:
        #查询对应课程的老师
        id = request.args.get('id')
        teachers = Teacher.query.filter_by(course_id=id).all()
    else:
        id = 0
        #查询所有老师
        teachers = Teacher.query.all()
    return render_template(
        '18-query.html',
        courses = courses,
        teachers=teachers,
        id=int(id))

@app.route('/19-addwife')
def addwife_views():
    #方式1:通过外键列增加关联数据
    # wife = Wife()
    # wife.wname = "Maria夫人1"
    # wife.wage = 30
    # wife.users_id = 3
    # db.session.add(wife)

    #方式2:通过反向引用关系属性增加关联数据
    user = Users.query.filter_by(id=5).first()
    wife = Wife()
    wife.wname = "JL"
    wife.wage = 30
    wife.user = user
    db.session.add(wife)

    return "增加wife成功"


@app.route('/20-oto',methods=['GET','POST'])
def oto_views():
    if request.method == 'GET':
        #查询Users中的所有数据
        users = Users.query.all()
        return render_template("20-oto.html",users=users)
    else:
        #接收前端数据
        wname=request.form['wname']
        wage=request.form['wage']
        user_id = request.form['user']
        #判断user_id在Wife表中是否存在　
        user = Wife.query.filter_by(users_id = user_id).first()
        if user:
            # user_id已经存在
            return "user已经存在!!!"
        else:
            # user_id不存在可以做插入
            wife = Wife()
            wife.wname = wname
            wife.wage = wage
            wife.users_id = user_id
            db.session.add(wife)
            return "注册Wife成功"

@app.route('/21-oto')
def oto21_views():
    wifes = Wife.query.all()
    return render_template('21-oto.html',wifes=wifes)


@app.route('/22-mtm')
def mtm_views():
    #创建Student的对象,并保存进数据库
    stu = Student()
    stu.sname = '漩涡鸣人'
    stu.sage = 16
    stu.isActive = True
    db.session.add(stu)
    db.session.commit()
    #查询出id为1的course信息,并插入到第三张关联表中
    course = Course.query.filter_by(id=1).first()
    course.students.append(stu)
    return "插入关联数据成功"

@app.route('/23-mtm',methods=['GET','POST'])


@app.route('/24-mtm-query')
def mtm_query():
    # 1.通过course 查询 students
    course = Course.query.filter_by(id=1).first()
    students = course.students.all()
    print("课程名称:"+course.cname)
    print("学员信息:")
    for s in students:
        print("姓名:%s,年龄:%d" % (s.sname,s.sage))
    #2.查询id为2的学员所选择的课程

    return "Query OK"
def mtm23_views():
    if request.method == 'GET':
        courses = Course.query.all()
        return render_template('23-mtm.html',courses=courses)
    else:
        sname = request.form['sname']
        sage = request.form['sage']
        stu = Student()
        stu.sname = sname
        stu.sage = sage
        db.session.add(stu)
        db.session.commit()
        #获取所有的course值
        courses_id = request.form.getlist('courses')
        #获取到相关的courses的对象
        list = Course.query.filter(Course.id.in_(courses_id)).all()
        #循环遍历list得到每个course并append到stu中
        for c in list:
            stu.courses.append(c)
        return "注册成功"
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







