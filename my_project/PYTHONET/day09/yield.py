def fun():
    print("启动生成器")
    yield 1
    print("生成器完成")



print(next(fun()))