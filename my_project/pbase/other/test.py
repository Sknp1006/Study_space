# import random as R
# #0-9
# #a-z
# #A-Z
# string = [chr(x) for x in range(ord('A'), ord('Z')+1)] + \
#          [chr(x) for x in range(ord('a'), ord('z')+1)] + \
#          [x for x in range(ord('1'), ord('9')+1)]
# code = R.sample(string, 6)
# print(code)
# print(' '.join(code))

# s = {"唐僧", '悟空', '八戒', '沙僧'}
# it = iter(s)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


# print(100/2/2/2/2/2/2/2/2/2/2)



# L = [100]
# def qiu(n):
#     s = 100
#     for i in range(n):
#         s /= 2
#         L.append(s)

# qiu(10)
# print(s)
# print(sum(L))

# def fun(x):
#     for i in range(x):
#         yield i

# x = iter(fun(10))
# for i in range(10):
#     print(next(x))


# L = list(zip("ABCD", range(10.20)))
# for x in zip("ABC", "123"):
#     print(x)

# def even(start, stop):
#     while start < stop:
#         yield start 
#         start += 1
# for x in even(1, 10):
#     print(x)  # [2, 4, 6, 8]
# L = [x for x in even(10, 20) if x % 2 ==0]
# print(L)  

# it = iter(even(3, 10))
# print(next(it))  # 4
# print(next(it))  # 6
# print(next(it))  # 8
# print(next(it))  # StopIteration

# 1. 已知有列表:
# L = [2, 3, 5, 7]
    # 1) 写一个生成器函数,让此函数能够动态提供数据, 提供的数据
    #   为原列表的数字的平方+1
# def yie():
#     for i in L:
#         yield i**2 + 1
#     # 2) 写一个生成器表达式,让此表达式能够动态提供数据,提供的数
#     #   据依旧为原列表的数字的平方+1
# it = iter(x**2+1 for x in L)
#     # 3) 写一个列表,此列表内的数据为原列表的数字的平方+1

# print(next(iter(yie()))
# print(next(it))

# L2 = [x**2+1 for x in L]
# print(L2)

# def myfilter(fn, iterable):
#     L = []
#     for i in iterable:
#         if fn(i):
#             L.append(i)
#     return L

# for x in myfilter(lambda y:y%2==1, range(10)):
#     print(x)  # 1 3 5 7


# def myzip(iter1, iter2):
#     #.... # 此处自己实现
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         try:
#             x1 = next(it1)
#             x2 = next(it2)
#             yield(x1, x2)
#         except StopIteration:
#             return

# d = dict(myzip("ABC", "123"))
# print(d)  # {'A': '1', 'B': '2', 'C': 3}

# def myenumerate(iterable, start=0):
#     it = zip(iterable, range(start, start + len(iterable)))
#     return it

# def myenumerate(iterable, start=0):
#     it = iter(iterable)
#     while True:
#         try:
#             x = next(it)
#             yield (start, x)
#             start += 1
#         except StopIteration:
#             return

# d = dict(myenumerate("ABCDE", 1))
# print(d) 


# # it = dict(zip("ABCD", range(1,6)))
# # print(it)

print