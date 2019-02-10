def main(tip):
    if tip == '1':
        input_infos()
    elif tip == '2':
        output_infos(infos)
    elif tip == '3':
        remove_infos()
    elif tip == '4':
        modify_infos()
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
    print("+--------------------------------+")
    print("| 1)  添加学生信息                |")
    print("| 2)  显示学生信息                |")
    print("| 3)  删除学生信息                |")
    print("| 4)  修改学生信息                |")
    print("| 5)  按学生成绩高~低显示学生信息  |")
    print("| 6)  按学生成绩低~高显示学生信息  |")
    print("| 7)  按学生年龄高~低显示学生信息  |")
    print("| 8)  按学生年龄低~高显示学生信息  |")
    print("| q   退出                       |")
    print("+--------------------------------+")

def input_infos():
    while True:
        name = input("输入姓名：")
        if len(name) == 0:
            break
        age = input("输入年龄:")
        score = input("输入成绩：")
        student = {'name': name, 'age': age, 'score': score}
        infos.append(student)

def output_infos(list):
    print("+----------+----------+----------+")
    print("|   name   |    age   |   score  |")
    print("+----------+----------+----------+")
    for i in list:
        n = i['name']
        a = i['age']
        s = i['score']
        print("|%s|%s|%s|" %(n.center(10), a.center(10), s.center(10)))
    print("+----------+----------+----------+")

def remove_infos():
    name = input("输入姓名：")
    for i in infos:
        if i['name'] == name:
            del infos[infos.index(i)]
            print("删除成功")
            return
    print("删除失败")

def modify_infos():
    name = input("输入姓名：")
    for i in infos:
        if i['name'] == name:
            score = input("输入新成绩：")
            i['score'] = score
            print("修改完成！")
            return
    print("修改失败！")

def sort_age(i):
    return int(i['age'])

def sort_score(i):
    return int(i['score'])

if __name__ == '__main__':
    student = {}
    infos = [{'name': 'tarena', 'age': '15', 'score': '99'}, {'name': 'cat', 'age': '13', 'score': '60'}, {'name': 'dog', 'age': '6', 'score': '90'}, {'name': 'monkey', 'age': '19', 'score': '70'}, {'name': 'party', 'age': '11', 'score': '66'}, {'name': 'soon', 'age': '13', 'score': '89'}]
    while True:
        menu()
        tip = input("输入序号：")
        if tip != 'q':
            main(tip)
        else:
            break
    print(infos)

