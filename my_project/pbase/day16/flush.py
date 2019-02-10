# 此示例示意缓冲区的作用及清除方法

# 此处省略try语句

fw = open("myflush.txt", "w")

fw.write("这是一行文字!")
fw.flush()  # 强制清空缓冲区!
input("请输入回车键继续: ")

fw.close()
print("程序退出")

