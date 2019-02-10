def make_except():
    print("开始...")
    # raise ValueError  #触发一个错误  raise被调用,下面的代码不执行
    #创建一个错误类型用error来绑定
    error = ValueError("XXX大街YYY号着火了")   #异常对象
    raise error   #触发ValueError类型错误对象
    print("结束...")

try:
    make_except()
    print("make_except调用完成")
except ValueError as err:    #类型 as 对象  err绑定raise发出的错误信号
    print("收到ValueError错误类型的通知", err)
print("程序正常结束")


#此示例用raise语句传递错误信息
# def f1():
#     n = int(input("请输入整数:")) #此处可能触发ValueError错误

# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内出错")
#         print("f2里的err=", err)
#         # raise err
#         raise
    
# try:
#     f2()
# except ValueError as err:
#     print("f2内发生了ValueError类型错误")

