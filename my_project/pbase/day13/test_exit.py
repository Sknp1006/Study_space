import sys

#此示例用sys.exit函数直接退出当前函数

def myfun():
    print("函数开始")
    sys.exit()
    print("函数结束")

myfun()
print("程序结束")