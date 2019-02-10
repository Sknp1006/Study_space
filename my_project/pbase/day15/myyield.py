#myyield

#此示例示意生成器函数的创建和调用

def myyield():
    print("即将生成2")
    yield 2
    print("生产器函数结束")


gen = myyield()
print(gen)

it = iter(gen)
print(next(it))
print(next(it))
