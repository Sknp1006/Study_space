#写一个lambda 表达式来创建函数,此函数返回两个参数的最大值
        def mymax(x, y):
           ...

#mymax = lambda :...           
mymax = lambda *args: max(args)
mymax = lambda x,y:x if x > y else y
print(mymax(100, 200))
print(mymax('ABC', "123"))
