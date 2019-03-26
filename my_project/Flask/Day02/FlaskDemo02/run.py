from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-temp')
def temp():
    """
    演示模板的渲染和响应
    :return: 响应内容
    """
    # 声明变量传递到01-temp.html中进行显示
    name = '小泽maria'
    age = 30
    gender = '男'
    return render_template('01-temp.html', name=name, age=age, gender=gender)


@app.route('/02-var')
def var():
    title = '钢铁是咋练成的'
    author = '奥斯特洛夫斯基'
    publisher = '北京大学出版社'
    pub_date = '1965-10-12'
    # 渲染模板
    return render_template('02-var.html', title=title, author=author, publisher=publisher, pub_date=pub_date)


@app.route('/03-var')
def var03():
    """
    演示允许传递到模板中做变量的数据类型
    :return:响应内容
    """

    uname = '旋涡鸣人'
    uage = 16
    salary = 350.52
    list = ["漩涡鸣人", "佐助", "小樱", "卡卡西"]
    tup = ("大蛇丸", "奈良鹿丸", "樱桃小丸子")
    dic = {
        "WMZ": '魏老板',
        "MARIA": '吕泽',
        "MM": '蒙蒙'
    }
    person = Person()
    person.name = '狮王.金毛'

    print(locals())

    return render_template('03-var.html', params=locals())


@app.route('/04-filter')
def filter_views():
    salary = -785
    name = "uzumaki naruto"
    msg = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque cupiditate dignissimos dolores eos libero pariatur soluta. Distinctio, eum iusto numquam sapiente temporibus vero. Aspernatur cum, dolorum et illo laborum nesciunt!"
    return render_template('04-filter.html', salary=salary, name=name, msg=msg)


@app.route('/05-for')
def for_views():
    list = ["宋江", "潘金莲", "李师师", "陈圆圆"]
    return render_template('05-for.html', list=list)


@app.route('/06-macro')
def macro_views():
    list = ["魏老师", "吕老师", "王老师", "蒙蒙"]
    return render_template('06-macro.html', list=list)


@app.route('/07-static')
def static_views():
    return render_template('07-static.html')

class Person(object):
    name = None

    def show(self):
        return "my name is " + self.name


if __name__ == "__main__":
    app.run(debug=True)
