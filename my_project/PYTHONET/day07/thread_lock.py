from threading import Thread, Lock

a = b = 0
l = Lock()

def value():
    while True:
        l.acquire()
        if a != b:
            print("a = %d, b = %d"%(a, b))
        l.release()

t = Thread(target=value)
t.start()
while True:
    with l:
        a += 1
        b += 1 

t.join()