#阶乘公式(n!):
#    1     如果n == 0
#    n*(n-1)!   当n>0

def myfac(n):
    if n == 0:
        return 1
    s = n * myfac(n-1)
    return s  
print(myfac(5))
