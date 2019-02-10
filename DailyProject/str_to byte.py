#写一个程序，从键盘输入一段字符串，用变量s绑定
#1.将此字符串转为字节串用变量b绑定，并打印出来
#2.打印字符串s的长度和字节串的长度
#3.将字节串再次转换为字符串变量s2绑定，判断s2与s是否相同
# 再将上述字节串改为字节数组完成练习

#字符串转字节串
s = input("输入一段字符串：")
b = bytes(s, encoding='utf-8')
print("字节串b是:", b)
print("字符串的长度：", len(s))
print("字节串的长度：", len(b))
s2 = b.decode('utf-8')
print(s2 == s)

#字符串转字节数组
s = input("输入一段字符串：")
b = bytearray(s, encoding='utf-8')
print("字节串b是:", b)
print("字符串的长度：", len(s))
print("字节串的长度：", len(b))
s2 = b.decode('utf-8')
print(s2 == s)