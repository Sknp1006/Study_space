#   写程序将这些数据读取出来,并以如下格式打印在屏幕终端上
#     小张 今年 20 岁,成绩是: 100
#     小李 今年 18 岁,成绩是: 98
#     小赵 今年 19 岁,成绩是: 80
    
# def read_info_from_file():
#     '''此函数将从文件中读取信息
#     形成字典的列表'''
#     L = []
#     try:
#         fr = open('info.txt', 'rt')
#         # 读取数据放在列表L中
#         for line in fr:  # line = '小张 20 100\n'
#             line = line.strip()  # line = '小张 20 100'
#             lst = line.split()  # lst=['小张', '20', '100']
#             n, a, s = lst # 序列赋值 a='20' s='100'
#             a = int(a)
#             s = int(s)  # 转为整数
#             d = dict(name=n, age=a, score=s)
#             L.append(d)  # 放入列表

#         fr.close()
#     except OSError:
#         print("读取文件失败!")

#     return L

# def print_info(L):
#     for d in L:
#         print(d['name'], '今年', d['age'],
#               '岁, 成绩是:', d['score'])

# infos = read_info_from_file()
# print_info(infos)


try:
    info = open('/home/tarena/my_project/day16/info.txt')
    f = info.readlines()
    for i in range(len(f)):
        l = f[i].split(' ')
        print(l[0], "今年", l[1], "岁","成绩是:" ,l[2], end='')
    # for line in info:
    #     print(line[6])

except OSError:
    print("文件打开失败")

finally:
    info.close()