# seek.py


# 此示例示意用F.seek方法来修改文件的读写指针的位置 

try:
    f = open("my20bytes.txt", 'rb')

    b1 = f.read(3)
    print("读完三个字节后的文件读写指针的位置是:", f.tell())
    # f.seek(5, 0)   # 1. 相对文件头偏移
    # f.seek(2, 1)  # 2.相对于当前位置向后移2个字节
    f.seek(-15, 2) # 3. 相对于文件尾向前移动15个字节
    print("文件读写指针的位置是:", f.tell())
    b2 = f.read(5)  # 要读取从第5~9字节, b2=b'abcde'
    print('b2=', b2)  # b'abcde'
    f.close()
except OSError:
    print("打开读文件失败!")


