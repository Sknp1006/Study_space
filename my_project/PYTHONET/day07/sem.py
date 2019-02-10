from multiprocessing import Process, Semaphore
from time import sleep
import os

sem = Semaphore(3)

def fun():
    print("%d 想执行的事件"%os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("%d 执行事件..."%os.getpid())
    sleep(3)
    print("%d 执行完毕"%os.getpid())
    sem.release() #执行完成后添加一个信号量

jobs = []
for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print("sem:", sem.get_value())