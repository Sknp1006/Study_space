# fr = open("test.txt", 'r')
# for line in fr:
#     print(line)
# fr.close()

#以下示例示意用with语句改写with.py中try-finally的用法
# try:
#     with open("test.txt", 'r') as fr:
#         for line in fr:
#             print(line)
#             3 / 0
#     fr.read()  #出错,fr已经被with语句自动关闭
# except OSError:
#     print('文件打开失败!!')

#此示例示意自定义一个环境管理器,让其用于with语句管理

class A:
    def __enter__(self):
        print("A.__enter__方法被调用")
        self.file = open('test.txt')
        return self  #return返回的对象会被as变量所绑定
    def __exit__(self, e_type, e_value, e_cb):
        self.file.close()
        if e_type is None:
            print("ok")
        else:
            print("Error")
            print("e_type=", e_type)
            print("e_value=", e_value)
            print("e_cb=", e_cb)
            print("A.__exit__方法被调用")
with A() as a:
    print(a.file.readline())
    3 / 0 #
    print("这是with语句内部的语句")
print("程序正常退出!")