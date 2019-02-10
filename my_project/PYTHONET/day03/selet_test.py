from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0', 8888))
s,listen(3)

print("监控IO")
rs, ws, xs = select([s],[],[], 3)  #3s之后没有就绪的,继续往下运行

print("就绪IO:", rs)
print("就绪IO:", ws)
print("就绪IO:", xs)