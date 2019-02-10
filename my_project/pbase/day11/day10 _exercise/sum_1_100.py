def mysum(n):
    if n == 1:
        return 1
    return n+mysum(n-1)

print(mysum(100))


#方法1:
def mysum(x):
    s = 0
    for i in range(1,x+1):
        s += i
    return s


#方法2:
    print(sum(range(1,101)) #函数式编程


