class MyNumber:
    def __init__(self, value):
        self.data = value
    
    def __repr__(self):
        return 'MyNumber(%d)' %self.data
    
    def __add__(self, other):
        s = self.data + other.data
        return MyNumber(s)   #创建一个新的对象并返回
    
    def __sub__(self, other):
        s = self.data - other.data
        return MyNumber(s)

n1 = MyNumber(100)
n2 = MyNumber(200)
# print(n1)

# n3 = n1.__add__(n2)  
# n3 = n1 + n2  #等同于n3 = n1.__add__(n2)
# print(n1, '+', n2, '=', n3)

print(n2 - n1)
