from socket import *

s = socket(AF_INET, SOCK_STREAM)
#设置端口立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET, SO_REUSEADDR))


s.bind(('127.0.0.1', 8888))
print(s.type)   
print(s.family)

print(s.getsockname())
print(s.fileno())


s.listen(3)
c, addr = s.accept()
print("Client address:", c.getpeername())

data = c.recv(1024)

c.close()
s.close()