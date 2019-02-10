def f1():
    print("f1函数被调用")

def f2():
    print("f2函数被调用")

def fx(fn):
    print(fn)
    fn()

fx(f1)      #<function f1 at 0x7f03e1b80f28>
fx(f2)      #<function f2 at 0x7f03e0402730>
fx(print)   #<built-in function print>
#fx(max)     #出错,max函数不能无参调用
print("程序结束")
