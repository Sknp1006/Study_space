#1
def input_number():
    l = []
    while True:
        n = int(input("输入int number:"))
        if n < 0:
            return l
        l.append(n)

#2


L = input_number()
print("用户输入的最大值是:", max(L))
print("用户输入的最小值是:", min(L))
print("用户输入的全部数的和是:", sum(L))