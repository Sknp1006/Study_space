# 1.写一个程序,让用户输入很多个正整数,最后将这些整数存于文件 mynumber.txt中
try:
    fw = open("mynumbers.txt", 'w')
    try:
        while True:
            n = int(input("请输入:"))
            if n < 0:
                break
            fw.write(str(n))
            fw.write('\n')
    finally:
        fw.close()
except OSError:
    print("打开失败!")

