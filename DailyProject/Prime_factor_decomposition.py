num = int(input("输入一个整数:"))

#高级
a = []
x = 2

while x <= num:
    if num % x == 0:
        a.append(x)
        num /= x
        continue
    x += 1

print(a)

#普遍
# def is_prime():
#     pass

# range(2, num)