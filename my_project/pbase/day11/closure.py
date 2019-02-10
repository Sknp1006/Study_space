# #1,全局变量money不安全
# money = 1000 #父母给的压岁钱

# def child_buy(obj, m):
#     global money
#     if money > m:
#         print('买', obj, "花了", m,"元","剩余",money)
#         money -= m
#     else:
#         print("买", obj,"失败")



# #2,局部money不符合逻辑
# def child_buy(obj, m):
#     money = 1000 #父母给的压岁钱
#     if money > m:
#         print('买', obj, "花了", m,"元","剩余",money)
#         money -= m
#     else:
#         print("买", obj,"失败")

# #3,把money变量放在外部嵌套作用域内
# def give_yasui_money(m):
#     money = m #创建外部嵌套函数变量
#     def child_buy(obj, m):
#         nonlocal money
#         if money > m:
#             print('买', obj, "花了", m,"元","剩余",money)
#             money -= m
#         else:
#             print("买", obj,"失败")
#     return child_buy

# cb = give_yasui_money(1000)   #cb绑定child_buy
# cb('变形金刚', 200)
# #money = 0 #钱没了
# cb('漫画三国', 100)
# cb('手机', 1300)

#closure2.py
#创建一系列函数:
# def pow2(x):
#     return x**2
# def pow100(x):
#     return x**100

def make_power(y):
    def fn(x):
        return x**y
    return fn

pow2 = make_power(2)
print(pow2(3))
print(pow2(4))

pow5 = make_power(5)
print(pow5(2))
print(pow5(4))