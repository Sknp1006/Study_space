def myfun1(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

L = [1, 2, 3]
T = (100, 200, 300)
s = "ABC"

d = {'a':11, 'b':22, 'c':33}
myfun1(**d)

#错误示例:
d2 = {'c':33, 'b':22, 'd':11}
d3 = {'c':33, 'b':22, 'd':11, 'a':11} #多了不行,d不存在

