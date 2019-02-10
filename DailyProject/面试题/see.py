def out():
    return [lambda x,i=i :i*x for i in range(14)]

print([m(4) for m in out()])
