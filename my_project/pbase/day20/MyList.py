class MyList:
    def __init__(self, iterable=()):
        '''此处用给定的可迭代对象iterable创建一个新列表,
        绑定此对象的data实例变量中'''
        self.data = [x for x in iterable]
        
    def __repr__(self):
        return 'MyList(%r)' %self.data

    def __add__(self, rhs):
        s = self.data + rhs.data
        return MyList(s)   #创建一个新的对象并返回
    
    def __rmul__(self, lhs):
        s = self.data * lhs
        return MyList(s)

    # def __sub__(self, rhs):
    #     s = self.data - rhs.data
    #     return MyList(s)
    #列表没有减操作
    

    def __mul__(self, rhs):
        s = self.data * rhs
        return MyList(s)
L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2
print(L3)       #MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)       #MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 2
print(L5)       #MyList([1, 2, 3, 1, 2, 3])

L6 = 2 * L1 
print(L6)



