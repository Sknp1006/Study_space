L = [3,5]
print(id(L))
L[0:0] = [1,2]
print(id(L))
L[3:3] = [4]
print(id(L))
L[5:5] = [6]

print(L)
print(id(L))

L[:] = L[::-1]
# L.reverse()
print(L)
print(id(L))

print(L[0:5])
print(id(L))