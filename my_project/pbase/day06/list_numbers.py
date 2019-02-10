
L = []
while True:
    num = int(input("请输入一个正整数:"))
    if num < 0:
        break
    L += [num]
for x in L:
    print(x)
print(max(L))
print(sum(L)/len(L))
