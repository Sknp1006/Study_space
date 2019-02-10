'''
本教程演示Tensor对象的加法
'''

from __future__ import print_function
import torch as t

#只分配空间，不进行初始化
# x = t.Tensor(5, 3)
# print(x)

#随机生成[0, 1]均匀分布矩阵
x = t.rand(5, 3)
# print(x)
y = t.rand(5, 3)
# print(y)

# print(t.add(x,y))   #第二种加法
#
# result = t.Tensor(5, 3)  #预先分配空间
# t.add(x, y, out=result)  #分配到result中
# print(result)

print(y.add(x))    #普通加法，不改变y的值，会返回一个新的Tensor
print(y)
print(y.add_(x))   #inplace加法，y变了
print(y)


#以下示例利用GPU加速计算（需要大量的计算才有效果）
x = t.Tensor(5, 3)
y = t.Tensor(5, 3)

if t.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x + y)

