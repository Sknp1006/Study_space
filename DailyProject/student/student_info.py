def input_infos():
    while True:
        name = input("请输入名字:")
        if name == '':
            return None
        try:
        age = int(input("请输入年龄:"))
        score = int(input("请输入成绩:"))
        except ValueError:
            print("您输入的信息有误!!!")
            continue
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