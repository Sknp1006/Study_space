from socket import *
from time import sleep

#创建套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
sockfd.setblocking(False)

#发起连接请求
server_addr = (('127.0.0.1', 8888))
print(server_addr)
sockfd.connect(server_addr)
# except timeout:
#     print("等不起啊...")
sockfd.send('sknp'.encode())
# data_r = sockfd.recv(1024)
# print("From Server:", data_r)

sockfd.close()
