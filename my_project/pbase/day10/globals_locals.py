a = 1
b = 2
c = 3

def fn(c, d):
    #global c
    e = 300
    print(locals())
    #print(globals())
    print(globals()['c'])
    #print(c)
    #等同于
    ddd = globals()
    print(ddd['c']))
    
fn(100, 200)
