#此示例示意模块的隐藏属性

#隐藏属性不会被 from ... import *导入

def f():
    pass

def _f():
    pass

def __f():
    pass

name1 = 'aaa'
_name = 'bbb'

# ['__builtins__', '__doc__', 
# '__loader__', '__name__', '
# __package__', '__spec__', 'f', 'name1']