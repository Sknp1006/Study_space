#file : mypack/office/__init__.py

#此列表限定用在from mypack.office import *
#语句导入时,会导入excel 和 word 模块
__all__ = ['excel', 'word']