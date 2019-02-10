#----------------------------#                             
#                            #
#                            #
#本程序用来连接本教室打开服务的计算机
from socket import *
from time import sleep

#创建套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
sockfd.setblocking(False)

#发起连接请求
for x in range(32, 50):
    for y in range(8000, 20000):
        server_addr = (('176.136.4.' + str(x), y))
        try:
            print(server_addr)
            sockfd.connect(server_addr)
        # except timeout:
        #     print("等不起啊...")
        except:
            continue
        else:
            sockfd.send('sknp'.encode())
            # data_r = sockfd.recv(1024)
            # print("From Server:", data_r)

sockfd.close()