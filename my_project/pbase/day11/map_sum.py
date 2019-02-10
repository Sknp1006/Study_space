# 求 1**2 + 2**2 + 3**2 + ... + ... + 9**2 的和
# 求 1**3 + 2**3 + 3**3 + ... + ... + 9**3 的和
# 求 1**9 + 2**8 + 3**7 + ... + ... + 9**1 的和

# print(sum(map(pow, range(1,10),9*(2,))))   #元组可以乘
# print(sum(map(pow, range(1,10),9*[3])))  #列表可以乘
# print(sum(map(pow, range(1,10),range(1,10)[::-1])))

# #字符串也可以乘,但是转换太麻烦

# print(sum(map(lambda x: x**2, range(1,10))))





def tran(x):
    r = [i for i in x]
    return r
        
print(sum(map(pow, range(1,10), map(tran, 9*'2'))))