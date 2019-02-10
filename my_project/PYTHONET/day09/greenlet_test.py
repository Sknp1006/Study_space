from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()  #执行协程函数test2
    print(34)
    print(43)

def test2():
    print(56)
    gr1.switch()  
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()  #执行协程函数test1