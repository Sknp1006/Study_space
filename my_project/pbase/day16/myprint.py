import sys
# 方法1
def myprint(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    flag = False #代表是否打印分隔符
    for obj in args:
        s = str(obj) #转为字符串
        if flag:
            file.write(sep)
        flag = True
        file.write(s)
    file.write(end) #输出末尾字符
myprint(1,2,3,4)
myprint(1,4,5,6,7,7, sep='#', end='\n***\n')

# 方法2
def myprint(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    L = [str(obj) for obj in args]
    file.write(sep.join(L))
    file.write(end)

myprint(1,2,3,4,55,6, sep='@')
