# file_read_binary_mode.py

# 此示例示意用二进制方式读取一个内部存有文字信息的文件内容

try:
    fr = open('myfile.txt', 'rb')
    b = fr.read()  # 全部读出
    print(b)
    print("字节串的长度是:", len(b))  # 18
    s = b.decode() # 把字节串解码成为字符串
    print(s)

    fr.close()  # 关闭文件
except OSError:
    print("文件打开失败")

    