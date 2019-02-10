import os

pid = os.fork()


if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child Process")
    print("Child pid:", os.getpid())
    print("Get Parent PID:", os.getppid())
else:
    print("Parent Process")
    print("Parent pid:", os.getpid())
    print("Get Child PID:", pid)