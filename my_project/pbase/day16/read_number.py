#   2.写一个程序,将上一个程序输入的内容从mynumber文件中读取出来,打印和

try:
    fr = open("mynumbers.txt", 'r')
    L = []
    while True:
        s = fr.readline()
        if not s:
            break
        L.append(int(s.rstrip()))
    fr.close()
except OSError:
    print("打开失败")

print("和是:", sum(L))