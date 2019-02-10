#global.py

v = 100
def f1():
    v = 200
    global v  #此处会报警告
    print(v)
    

f1()
print("v=", v)

