def get_score():
    s = input("请输入成绩(0~100):")
    sc = int(s)
    if 0 <= sc <= 100:
        return sc
    return 0

try:
    score = get_score()
except ValueError:
    print("你输入的成绩不合法")
else:    
    print("学生成绩是:", score)



# def get_score():
#     print('这是开始')
#     s = input("请输入成绩(0~100):")
#     try:
#         sc = int(s)
#     except ValueError:
#         print("你输入的成绩不合法")
#         return 0

#     else:
#         if 0 <= sc <= 100:
#             return sc
    
# score = get_score()
# print("学生成绩是:", score)