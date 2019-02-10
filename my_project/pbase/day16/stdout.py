# stdout.py

# 此示例示意标准输出和标准错误输出的用法

import sys

# sys.stdout.write("你好!\n")
# sys.stdout.write("ABC")
# sys.stdout.writelines(['abc', '123'])

# sys.stdout.close() # 关闭这个文件!关掉之后不能使用print()
# # sys.stdout.write("AAAAAAA")  # 出错
# # print("hello world!")

# sys.stderr.write("我的出现是个错误!\n")

# print("我是print打印的输出")



f = open("myprint.txt", 'w')
print(1, 2, 3, 4, file=f)
f.close()
print('正常退出')