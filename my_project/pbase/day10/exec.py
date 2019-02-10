#exec.py

s = '''
v = 100
def f1():
    v = 200
    print("函数开始时: f1.v", v)
    def f2():
        nonlocal v
        v = 300
        print("函数结束时: f2.v", v)
    f2()
    print("函数结束时: f1.v", v)
f1()
print("全局的v=", v)  '''
exec(s)