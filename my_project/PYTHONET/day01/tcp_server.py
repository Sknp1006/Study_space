import socket

#创建TCP套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0', 10000))

#设置监听
sockfd.listen(5)

#等待处理客户端连接
print("Waitting for connect...")
connfd,addr = sockfd.accept()
print("Connect from", addr)  #打印客户端地址

    #消息收发
while True:
    data = connfd.recv(1024)
    if not data:
        break
    print("Receive Msg:", data)
    n = connfd.send(b'I see')
    print("Send %d bytes"%n)

#关闭套接字
sockfd.close()
connfd.close()