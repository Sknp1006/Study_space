import os, sys

filename = './day06笔记'

#获取文件大小
size = os.path.getsize(filename)

#父子进程共用一个文件对象偏移量会相互影
# f = open(filename, 'rb')
pid = os.fork()
if pid < 0:
     print("REEOR")
elif pid == 0:
    #复制上半部分
    f = open(filename, 'rb')
    fw = open('1', 'wb')
    n = size//2
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
            # sys.exit(0)
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()
else:
    #复制下半部分
    # pid, status = os.wait()
    f = open(filename, 'rb')
    fw = open("2", 'wb')
    f.seek(size//2, 0)
    while True:
        data = f.read(1024)
        if not data:
            break
            # sys.exit(0)
        fw.write(data)
    f.close()
    fw.close()

