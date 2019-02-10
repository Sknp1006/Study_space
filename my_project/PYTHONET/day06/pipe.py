from multiprocessing import process, Pipe
import os, time

#创建管道对象
#如果是单向管道,fd1-->只读,fd2-->只写
fd1, fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send(name)

jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd2.recv()
    print(data)

for i in jobs:
    i.join()
