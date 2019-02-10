#写一个xrange生成器函数，此函数按range规则生成一系列整数
def myxrange(start, stop=None, step=1):
    def process():
        nonlocal start, stop, step
        if stop:
            while start < stop:
                yield start
                start += step
        else:
            stop = start
            start = 0
            while start < stop:
                yield start
                start += step
    return iter(process())

for i in myxrange(10,20,2):
    print(i)

print(sum(map(lambda x: x**2, myxrange(1,10,2))))