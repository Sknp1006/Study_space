L = []
while True:
    num = int(input("输入正整数:"))
    if num < 0:
        if len(L) > 2:
            break
        else:
            print("您输入的数字太少,请继续输入.")
            continue
    # if num not in L:
    #     L.append(num)
    # else:
    #     print("已经输入过这个数了"))
    if L.count(num) != 0:
        print("已经输入过这个数了")
    else:
        L.append(num)
print(L)
print("这些数的和:", sum(L))

L1 = sorted(L.copy())
print(L1)
print("最大的数:", L1[-1])
print("第二大的数:", L1[-2])

# del L1[0]
# print(L1)
zuixiao = L1[0]
L.remove(zuixiao)
print(L)

