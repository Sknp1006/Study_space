from socket import *

#创建套接字
sockfd = socket()

#发起连接请求
server_addr = (('127.0.0.1', 8000))
sockfd.connect(server_addr)

#消息收发
while True:
    data_s = input(">>")
    if not data_s:
        break
    sockfd.send(data_s.encode())
    data_r = sockfd.recv(1024)
    print("From Server:", data_r)

sockfd.close()
