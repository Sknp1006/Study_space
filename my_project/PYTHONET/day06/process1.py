import multiprocessing as mp
from time import sleep

a = 1
#编写进程函数
def fun():
    sleep(3)
    global a
    print("a=", a)
    a = 10000
    print("子进程事件")

#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()

sleep(4)
print("父进程")
#回收进程,阻塞函数,超时不回收,会变成僵尸
p.join()

print('Parent a:', a)

# a= 1
# 子进程事件
# 父进程
# Parent a: 1