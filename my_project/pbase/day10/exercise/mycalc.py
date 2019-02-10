def myadd(x, y):
    return x + y
def mysub(x, y):
    return x - y
def mymul(x, y):
    return x * y
# ...
# 另有一个函数get_func,有一个参数op 代表用给定的字符串
def get_func(op):
    if op == '加' or op == '+':
        # myadd(a, b)
        return myadd
    elif op == '减' or op == '-':
        return mysub
    elif op == '乘' or op == '*':
        return mymul
    #     ...
    # 此函数在传入字符串"加",或 '+'时,返回myadd函数
    # 此函数在传入字符串"减",或 '-'时,返回mysub函数
    #     ...
# 在主函数中:
def main():
    while True:
        s = input("请输入计算公式:")  #10加20
        L = s.split(' ')
        #print(L)
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))
main()