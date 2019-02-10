from threading import Event

#创建事件对象
e = Event()

e.set()
e.clear()

print(e.is_set())

e.wait(2)

print("**********************************************")