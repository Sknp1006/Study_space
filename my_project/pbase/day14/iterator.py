#此示例示意用迭代器遍历一个列表: 
L = [2, 3, 5, 7]
it = iter(L)  # it 绑定的是L提供的迭代器
while True:
    try:
        print(next(it))
    except StopIteration:
        break
        
#---以上多条语句,可以用如下的for循环来实现----
for x in L:
    print(x)
# #用迭代器访问range(1, 10, 3)
# myit = iter(range(1, 10, 3))  # 1, 4, 7
# print(next(myit))  # 1
# print(next(myit))  # 4
# print(next(myit))  # 7
# # print(next(myit))  # StopIteration异常

