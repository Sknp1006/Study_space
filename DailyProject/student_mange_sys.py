def main(tip):
    if tip == '1':
        input_infos()
    elif tip == '2':
        output_infos(infos)
    elif tip == '3':
        del_infos()
    elif tip == '4':
        edit_infos()
    elif tip == '5':
        list_ = sorted(infos, key=sort_score, reverse=True)
        output_infos(list_)
    elif tip == '6':
        list_ = sorted(infos, key=sort_score)
        output_infos(list_)
    elif tip == '7':
        list_ = sorted(infos, key=sort_age, reverse=True)
        output_infos(list_)
    elif tip == '8':
        list_ = sorted(infos, key=sort_age)
        output_infos(list_)

def menu():
    print("+---------------------------------+")
    print("|  1)添加学生信息                 |")
    print("|  2)显示学生信息                 |")
    print("|  3)删除学生信息                 |")
    print("|  4)修改学生信息                 |")
    print("|  5)按学生成绩高~低显示学生信息  |")
    print("|  6)按学生成绩低~高显示学生信息  |")
    print("|  7)按学生年龄高~低显示学生信息  |")
    print("|  8)按学生年龄低~高显示学生信息  |")
    print("|  q)退出                         |")
    print("+---------------------------------+")

def input_infos():
    while True:
        name = input("请输入名字:")
        if name == '':
            return None
        age = input("请输入年龄:")
        score = input("请输入成绩:")
        student_dict = {'name': name,'age': age, 'score':score}
        infos.append(student_dict)

def output_infos(infos):
    print("+----------+----------+----------+")
    print("|   name   |    age   |   score  |")
    print("+----------+----------+----------+")
    for i in infos:
        n = i['name']
        a = i['age']
        s = i['score']
        print("|%s|%s|%s|" %(n.center(10),
                             a.center(10),
                             s.center(10)))
    print("+----------+----------+----------+")

def del_infos():
    for i in infos:
        if i['name'] == name:
            del infos[infos.index(i)]
            print("删除成功")
        return
    print('删除失败')

def edit_infos():
    name = input("请输入名字:")
    for i in infos:
        if i['name'] == name:
            age = input("请输入新年龄:")
            score = input("请输入新成绩:")
            i['age'] = age
            i['score'] = score
            print("修改成功")
            return
    print('修改失败')

def sort_age(s):
    return int(s['age'])

def sort_score(s):
    return int(s['score'])

    

student_dict = {}
infos = [{'score': '90', 'name': 'tarena', 'age': '15'}, {'score': '94', 'name': 'qwe', 'age': '14'}, {'score': '91', 'name': 'hong', 'age': '15'}, {'score': '100', 'name': 'casio', 'age': '18'}, {'score': '100', 'name': 'nice', 'age': '11'}, {'score': '60', 'name': 'hello', 'age': '20'}]
while True:
    menu()
    tip = input("请输入操作:")
    if tip != 'q':
        main(tip)
    else:
        break
print(infos)
