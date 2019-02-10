def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in myinteger(10):
    print(x)

print("------")
it = iter(myinteger(20))
print(next(it))
print(next(it))
print(next(it))