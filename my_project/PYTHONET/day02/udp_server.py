from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(('0.0.0.0', 8888))

while True:
    data, addr = sockfd.recvfrom(1024)  #此处阻塞
    print("Receive from %s:%s"%(addr, data.decode()))
    data_s = input(">>").encode()
    sockfd.sendto(data_s, addr)

sockfd.close()
