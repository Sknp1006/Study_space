#命名关键字形参的定义方法和调用传参
def fun1(a, b, *args, c, d):
    print(a, b, args, c, d)

#fun1(1, 2, 3, 4)   <--此处出错
fun1(11, 22, d=44, c=33)
fun1(1, 2, 3, 4, c=300, d=400)

def print(*args, sep=' ', end='\n',flush=False)
