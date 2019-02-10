#global.py

v = 100
def f1():
    global v
    v = 200

f1()
print("v=", v)

