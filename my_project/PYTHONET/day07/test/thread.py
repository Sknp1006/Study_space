from test import *
import threading
import time


def IO():
    write()
    read()

    
jobs = []
t = time.time()
for i in range(10):
    # th = threading.Thread(target=count, args=(1, 1))
    th = threading.Thread(target=IO)
    jobs.append(th)
    th.start()
for i in jobs:
    i.join()
print("Thread cpu:", time.time() - t)