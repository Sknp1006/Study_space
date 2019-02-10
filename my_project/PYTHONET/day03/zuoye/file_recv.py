from socket import *
from time import sleep

sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))

sockfd.listen(5)

conn, addr = sockfd.accept()
print('Connect from:', addr)
filename = conn.recv(1024)
sleep(1)
f = open(filename, 'wb')
while True:
    data = conn.recv(1024)
    if not data:
        break
    f.write(data)

conn.send('OK'.encode())

f.close()
conn.close()
sockfd.close()
