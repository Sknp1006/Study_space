'''
ftp 文件服务器程序
fork server迅雷
'''
from socket import *
import os, sys
import time

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FILES = '/home/tarena/my_project/'

#将文件处理功能封装
class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd
    
    def do_list(self):
        print("执行List")
        #获取文件列表
        file_list = os.listdir(FILES)
        #文件库为空则不许获取
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILES + file):
                files = files + file + '#'
        #将拼接好的字符串发送
        self.connfd.send(files.encode())
        return
    
    def do_get(self, filename):
        try:
            fd = open(FILES+filename, 'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        #循环发送文件内容
        while True:
            data = fd.read(1024)
            #到文件尾
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
    
    def do_put(self, filename):
        if os.path.exists(FILES + filename):
            self.connfd.send('文件存在'.encode())
            return
        try:
            fd = open(FILES+filename, 'wb')
        except:
            self.connfd.send('上传失败'.encode())
            return
        self.connfd.send(b'OK')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        time.sleep(0.1)
        return

#封装并发网络模型
def main():
    #创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("listen to the port 8888...")

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务端异常:", e)
            continue
        print('客户端:', addr,'已连接')
        #创建子进程
        pid = os.fork()
        if pid == 0:
            p = os.fork()
            if p == 0:
                sockfd.close()
                ftp = FtpServer(connfd)  #创建对象
                #根据客户端的请求执行操作
                while True:
                    #接收请求
                    data = connfd.recv(1024).decode()
                    if not data or data[0] == 'Q':
                        connfd.close()
                        sys.exit("客户端退出")
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(' ')[-1]
                        ftp.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split(' ')[-1]
                        ftp.do_put(filename)
                    # print(data)
            else :
                os._exit(0)
        else:
            connfd.close()
            os.wait()

main()