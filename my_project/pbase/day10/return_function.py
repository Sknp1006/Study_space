#此示例示意函数可以返回另一个函数的引用关系

def get_function():
    s = input("请输入你要做的操作")
    if s == "求最大":
        return max
    elif s == "求最大":
        return min
    elif s == "求最大":
        return max
    else:
        return print

L = [2, 4, 6, 8, 10]
f = get_function()  #相当于f绑定 max(),min(),max()
print(f(L))
