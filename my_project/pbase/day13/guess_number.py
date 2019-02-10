import random as R

count = 0
x = R.randint(0,100)
while True: 
    
    y = int(input("请输入一个整数:"))
    count += 1
    if y == x:
        print("恭喜您猜对了!!!")
        break
    elif y < x:
        print("您输入的数字太小,再接再厉~")
    elif y > x:
        print("您输入的数字太大,再接再历~")

print("您猜了", count, '次数字')


