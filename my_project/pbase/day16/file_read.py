# file_read.py


# 此示例示意用文件流对象的读方法来获取myfile.txt内的
# 字符数据
try:
    fr = open("/home/tarena/my_project/day16/myfile.txt")
    print("文件打开成功")
    # 2. 读取文件内容
    s = fr.readline()  # 读取全部文件内容
    print("读到%d个字符" %len(s), "\n", s)
    print("len(s)=", len(s))

    fr.close()
except OSError:
    print("文件打开失败")