#eval.py

s1 = "1+2*3"
s2 = 'x+y'

v = eval(s1)
print(v)

v2 = eval(s2, {'x':10, 'y':20})
print(v2)   #20

v2 = eval(s2, {'x':10, 'y':20}, {'y': 2})
print(v2)   #12
