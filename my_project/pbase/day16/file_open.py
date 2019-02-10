# file_open.py

# 此示例示意读取当前文件夹下myfile.txt这个记录文字信息的
# 文件

# 1.打开文件
try:
    myfile = open('myfile.txt')  # 成功打开文件
    # myfile = open('我不存在.txt')  # 失败
    print("文件打开成功")
    # 2. 读/写文件

    # 3. 关闭文件
    myfile.close()
    print("文件关闭成功")
except OSError as O:  # OSError表示无法进行输入输出
    print('文件打开失败!', O)
