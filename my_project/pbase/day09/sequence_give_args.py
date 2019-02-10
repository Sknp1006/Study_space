def myfun1(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

L = [1, 2, 3]
T = (100, 200, 300)
s = "ABC"

myfun1(*L)
myfun1(*T)
myfun1(*s)
