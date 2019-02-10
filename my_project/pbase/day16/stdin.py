# stdin.py

# 此示例示意标准输入文件的用法
import sys

# s = input("请输入:")  #input函数内部调用sys.stdin.read()
# s = sys.stdin.readline()

# print(s)
# print("len(s)=", len(s))

# sys.stdin.close()  # 一旦关闭,input函数将不再可用

# s2 = input("请输入文字: ")  # 内部会间接调用sys.stdin.readline
# print("s2=", s2)


s = sys.stdin.read()  #输入ctrl+D输入文件结束符
print("s=", s)
print("程序正常结束!!")
