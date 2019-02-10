# 一、定义列表:list1 = ['life','is','short'],

#            list2 = ['you','need','python']

#    完成以下几个要求：
#     1）输出python及其下标
#     2）将 'python' 改为 'python3'
#     3) 将list1和list2合并构造集合 list_set2

# list1 = ['life','is','short']
# list2 = ['you','need','python']
# print(list2[2], list2.index('python'))
# list2[2] = 'python3'
# print(list2)
# list1.extend(list2)
# list_set2 = set(list1)
# print(list_set2)

# 二、通讯录管理
# =======通讯录管理系统=======
# 1.增加姓名和手机号
# 2.删除姓名
# 3.修改手机号
# 4.查询所有用户 #输出为一个表格
# 5.根据姓名查找手机号
# 6.退出
# ============================ 

# import time
# def menu():
#     print("+----------------------+")
#     print("| 1.增加姓名和手机号   |")
#     print("| 2.删除姓名           |")
#     print("| 3.修改手机号         |")
#     print("| 4.查询所有用户       |")
#     print("| 5.根据姓名查找手机号 |")
#     print("| 6.退出               |")
#     print("+----------------------+")

# def main():
#     menu()
#     tip = input("输入序号:")
#     if tip == '1':
#         add_infos()
#         time.sleep(1)
#         return main()
#     elif tip == '2':
#         del_name()
#         time.sleep(3)
#         return main()
#     elif tip == '3':
#         mod_num()
#         time.sleep(3)
#         return main()
#     elif tip == '4':
#         show_infos()
#         time.sleep(3)
#         return main()
#     elif tip == '5':
#         search_num()
#         time.sleep(3)
#         return main()
#     elif tip == '6':
#         return print('退出')

# def input_name():
#     try:
#         name = input("输入姓名:")
#     except:
#         print("---名字不合法---")
#         return input_name
#     else:
#         if name:
#             return name
#         else:
#             print("---默认名字为None---")

# def add_infos():
#     name = input_name()
#     try:
#         ph_num = int(input("输入电话号码:"))
#     except ValueError:
#         print("---号码不合法,保存失败---")
#         return add_infos
#     else:
#         info = {'name': name, 'ph_num':ph_num}
#         LIST.append(info)
#     return

# def del_name():
#     name = input_name()
#     for key in LIST:
#         if key['name'] == name:
#             del LIST[LIST.index(key)]
#             print("---删除成功---")
#             return
#     print("---删除失败---")

# def mod_num():
#     name = input_name()
#     for key in LIST:
#         if key['name'] == name:
#             try:
#                 ph_mun = int(input("输入新的号码:"))
#             except ValueError:
#                 print("---输入的号码不合法---")
#                 return mod_num()
#             else:
#                 key['ph_num'] = ph_mun
#                 print("---修改成功---")
#                 return
#     print("---修改失败---")            

# def show_infos(name=None):
#     print("+---------+----------------+")
#     print("|  name   |     ph_mun     |")
#     print("+---------+----------------+")
#     if name:
#         for key in LIST:
#             if key['name'] == name:
#                 ph_num = str(key['ph_num'])
#                 print("|%s|%s|" %(name.center(9),
#                                 ph_num.center(16)))
#     else:
#         for key in LIST:
#             name = key['name']
#             ph_num = str(key['ph_num'])
#             print("|%s|%s|" %(name.center(9),
#                             ph_num.center(16)))
#     print("+---------+----------------+")

# def search_num():
#     name = input_name()
#     for key in LIST:
#         if key['name'] == name:
#             show_infos(name)
#             return
#     print("---查无此人---")

# if __name__ == '__main__':
#     LIST = [{'name': 'tarena', 'ph_num': 123456789}, {'name': 'mike', 'ph_num': 987654321}]
#     main()
    # print(LIST)

# 三、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
d = {}
string = input("请输入一段字符串:")
def count(string, n=0):
    for i in string:
        if ord(i) == 32:
            num += 1
            d["空格"] = num
        elif 65 <= ord(i) <= 122:
            num += 1
            d['字母'] = num
        else:
            num += 1
            d['其他'] = num
    print(d)

count(string)

            
    

# 四、给定排序数组和目标值，如果找到目标，则返回索引。如果没有，请返回索引按顺序插入的索引。

#     您可以假设数组中没有重复项。
# 输入： [1,3,5,6]，5 输出： 2
# 输入： [1,3,5,6]，2 输出： 1
# 输入： [1,3,5,6]，7 输出： 4
# 输入： [1,3,5,6]，0 输出： 0

# 五、罗马数字是由七个不同的符号来表示  I，V，X，L，C，D和M。

# 符号       值
# 我1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
# 例如，两个用II 罗马数字写成，只有两个加在一起。十二写为，XII简称X+ II。数字二十七写为XXVII，XX+ V+ II。
# 罗马数字通常从左到右从最大到最小。但是，四个数字不是IIII。相反，第四个被写为IV。因为一个在五个之前，我们减去四个。同样的原则适用于编号为9的数字IX。有六个使用减法的实例：
# I可以在V（5）和X（10）之前放置4和9。 
# X可以在L（50）和C（100）之前放置40和90。 
# C可以在D（500）和M（1000）之前放置以产生400和900。
# 给定罗马数字，将其转换为整数。输入保证在1到3999的范围内。

