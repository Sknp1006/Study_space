def myfun1(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

L = [1, 2, 3]
T = (100, 200, 300)
s = "ABC"

myfun1(c=3, b=2, a=1) #关键字传参
myfun1(a=1, 2, c=5)   #位置传参要在关键字传参之前

