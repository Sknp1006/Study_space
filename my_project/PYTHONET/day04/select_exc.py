from select import select
from socket import *
import sys
from time import ctime

#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))

s.listen(3)

f = open('mylog', 'a')  #日志文件

#添加关注列表
rlist = [s, sys.stdin]
wlist = []
xlist = [s]

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            print("s准备就绪")
            c, addr = r.accept()
            print("Connect from:", addr)
            rlist.append(c)
        elif r is sys.stdin:
            data = sys.stdin.readline()
            data = ctime() + ' ' + data + '\n'
            f.write(data)
            f.flush()   #清理写缓存
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            data = ctime() + ' ' + data + '\n'
            f.write(data)
            f.flush()
            r.send(b'ADD logging')
    for w in ws:
        pass

    for x in xs:
        x.close()