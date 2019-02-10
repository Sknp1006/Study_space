def prime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

#用构造函数    
L = list(filter(prime, range(100)))
print(L)

#用推导式

