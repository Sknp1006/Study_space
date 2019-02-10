#before
L = [1, 2, 3]
def f(n=0, lst=[]):
    lst.append(n)   #only '=','+','-','*','/' can change obj
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)    #lst was created when we created def 
f()
f(100, L)
f()

# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [100]
# [100, 200]
# [100, 200, 0]
# [1, 2, 3, 4, 5, 100]

#after
L = [1, 2, 3]
def f(n=0, lst=None):
    if lst is None:
        lst = []
    lst.append(n)
    print(lst)
f(4,L)
f(5,L)
f(100)
f(200)    #lst was created when we created def 
f()
f(100, L)

# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [100]
# [00]
# [0]
# [1, 2, 3, 4, 5, 100]
