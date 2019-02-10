import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child %d process exit"%os.getpid())
    #2*256
    os._exit(2)
else:
    #阻塞等待处理子进程退出
    pid, status = os.wait()
    print("pid:", pid)  #退出的子进程pid
    print("status:", status)  #子进程退出状态
    print("status:", os.WEXITSTATUS(status))
    print("parent process...")
    while True:
        pass