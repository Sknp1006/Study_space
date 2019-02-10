from test import *
# import threading
import multiprocessing as mp
import time


def IO():
    write()
    read()

    
jobs = []
t = time.time()
for i in range(10):
    # p = mp.Process(target=count, args=(1, 1))
    p = mp.Process(target=IO)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("Thread cpu:", time.time() - t)

