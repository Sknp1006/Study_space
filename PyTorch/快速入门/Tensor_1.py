'''
本教程演示Tensor对象的加法
'''

from __future__ import print_function
import torch as t

#只分配空间，不进行初始化
# x = t.Tensor(5, 3)
# print(x)
# tensor([[0.0000e+00, 0.0000e+00, 0.0000e+00],
#         [0.0000e+00, 0.0000e+00, 0.0000e+00],
#         [0.0000e+00, 0.0000e+00, 0.0000e+00],
#         [0.0000e+00, 1.6087e-42, 0.0000e+00],
#         [0.0000e+00, 1.3458e-14, 0.0000e+00]])


#随机生成[0, 1]均匀分布矩阵(值为[0,1]之间的数)
x = t.rand(5, 3)
# print(x)
# tensor([[0.2435, 0.0794, 0.2762],
#         [0.4804, 0.6992, 0.9625],
#         [0.5286, 0.7764, 0.6942],
#         [0.5800, 0.1747, 0.3133],
#         [0.0971, 0.6841, 0.9279]])
y = t.rand(5, 3)
# print(y)
# tensor([[0.5502, 0.6765, 0.5273],
#         [0.2294, 0.2711, 0.2882],
#         [0.7849, 0.6645, 0.1038],
#         [0.0286, 0.2010, 0.3498],
#         [0.6699, 0.0356, 0.9613]])



# print(t.add(x, y))   #第二种加法，不改变x的值

# result = t.Tensor(5, 3)  #预先分配空间
# t.add(x, y, out=result)  #分配到result中
# print(result)

# print(y.add(x))    #普通加法，不改变y的值，会返回一个新的Tensor
# print(y)
# print(y.add_(x))   #inplace加法，y变了
# print(y)


#以下示例利用GPU加速计算（需要大量的计算才有效果）
# x = t.Tensor(5, 3)
# y = t.Tensor(5, 3)
#
# if t.cuda.is_available():
#     x = x.cuda()
#     y = y.cuda()
#     print(x + y)

