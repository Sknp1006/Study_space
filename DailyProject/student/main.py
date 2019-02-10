from student_info import *
from menu import menu

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

if __name__ == '__main__':
    student_dict = {}
    infos = [{'score': '90', 'name': 'tarena', 'age': '15'}, {'score': '94', 'name': 'qwe', 'age': '14'}, {'score': '91', 'name': 'hong', 'age': '15'}, {'score': '100', 'name': 'casio', 'age': '18'}, {'score': '100', 'name': 'nice', 'age': '11'}, {'score': '60', 'name': 'hello', 'age': '20'}]
    while True:
        menu()
        tip = input("请输入操作:")
        if tip != 'q':
        main(tip)
        else:
            break
    # print(infos)