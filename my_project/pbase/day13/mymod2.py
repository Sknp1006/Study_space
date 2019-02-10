#此__all__列表限制在from mymod2 import *时
#只导入f1 和 name1 
__all__ = ['f1', 'name1']


def f1():
    f2()
    f3()

def f2():
    pass

def f3():
    pass

name1 = 'aaa'
name2 = 'bbb'