from socket import *
from time import sleep

sockfd = socket()
sockfd.connect(('127.0.0.1', 8888))

filename = input("请输入要发送的文件:")
f = open(filename, 'rb')
sockfd.send(filename.encode())
sleep(1)
while True:
    data = f.read(1024)
    if not data:
        break
    sockfd.send(data)

f.close()
sockfd.close()