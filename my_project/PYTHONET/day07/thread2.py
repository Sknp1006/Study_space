from threading import Thread
from time import sleep

#线程函数参数的传递
def fun(sec, name):
    print("线程函数传参")
    sleep(sec)
    print("%s线程执行完毕"%name)

#创建多个线程
thread = []
for i in range(3):
    t = Thread(target=fun, args=(2, ), kwargs={'name' : 't%d'}%i)
    thread.append(t)
    t.start()

for i in thread:
    i.join()
