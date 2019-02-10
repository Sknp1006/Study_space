# users = ['libai', 'lula']
# pwds = [123, 456]
# name = input("请输入用户名:") or "admin"
# pwd = int(input("请输入密码:"))
# #方法1
# i = 0
# while i < len(users):
#     if name == users[i]:
#         break
#     i += 1 
# else:
#     print('没有此用户!')
#     exit()
# if pwd == pwds[i]:
#     print("登录成功")
# else:
#     print('登录失败')

# 方法2
# if name in users:
#     pwd = int(input("请输入密码:"))
#     if pwd == pwds[users.index(name)]:
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print("没有此用户")
#     exit()

# 方法3
# if users.count(name) == 1:
#     i = users.index(name)
# else:
#     print("没有此用户")
#     exit()
# if pwd == pwds[i]:
#     print('登录成功')
# else:
#     print('密码有误')


# 实现注册功能(注册成功打印出所有的用户名)
# a)用户名验证功能(只能有数字,英文字母组成,长度>4)
# b)密码验证(长度8以上,不能全是数字)
# c)密码二次输入验证
# d)用户名添加到users中, 密码添加到pwds中
users = []
pwd = []
def login():
    name = input("请输入用户名:")
    for i in name:
        while len(i) > 4 and ord('0') <= ord(i) <= ord('9') and ord('a') <= ord(i) <= ord('z'):
            print("用户名合法")
            users.append(name)
            break
            print('请重新输入用户名:')

    pwd_1 = input("请输入密码:")
    try:
        int[pwd_1]
    except ValueError:
        pwd_2 = input("请再次确认密码:")
        if pwd_2 == pwd_1:
            pwd.append(pwd_1)
        else:
            print("与之前的密码不符")
    else:
        print("密码不能全为数字")

login()
    


# 扩展题:
#   机选双色球,
#   红球:01,02,~,33  ---->红球选6个
#   篮球:01,02,~,16  ---->篮球选1个
# 机选双色球程序

# import random as R

# red = [x for x in range(1, 34)]
# blue = [x for x in range(1, 17)]

# l = R.sample(red, 6)
# r = R.sample(blue, 1)
# double_balls = list(l + r)
# # double_balls.extend(l)
# # double_balls.extend(r)
# print(double_balls)

