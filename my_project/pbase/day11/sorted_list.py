# 1.将列表内的五个元组按第二个数据的从小到大的顺序进行排序
#     (4,1) (5,3) (1,5) (3,6) (3,9)
# 2.将列表内的五个元组按第二个数的从大到小顺序进行排序,打印排序后的结果
# 3.假设元组中的数据是数学直角坐标系的坐标,则按他们距离原点的距离进行排序

import math
L = [(1,5),(3,9),(4,1),(3,6),(5,3)]

def fk(s):
    return s[::-1]

print(sorted(L, key=fk))
print(sorted(L, key=fk, reverse=True))

def dis(s):
    return math.sqrt(s[0]**2+s[1]**2)

print(sorted(L, key=dis))

L4 = sorted(L, key=lambda x, y: (x**2+y**2)**0.5)
print(L4)