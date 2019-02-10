from socket import *
import os, sys

#客户端处理函数
def client_hander(c):
    print("客户端:", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank you')
    c.close()

#创建套接字
HOST = '0.0.0.0'
POST = 8888
ADDR = (HOST, POST)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

#循环等待接收客户端连接请求
print("Listen to the port 8888...")
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print("Error:", e)
        continue


    #创建新的进程处理客户端请求
    pid = os.fork()

    if pid < 0:
        pass
    if pid == 0:
        p = os.fork()
        if p == 0:  #二级子进程
            s.close()
            client_hander(c)  #处理具体请求
            sys.exit(0)  #子进程处理完即退出
        else:
            os._exit(0)  #退出一级子进程
    #父进程或者创建进程失败都等待下一个客户端连接
    else:
        c.close()
        os.wait()

