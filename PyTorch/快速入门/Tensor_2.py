'''
Autograd: 自动微分
'''

import torch as t
from torch.autograd import Variable

# x = Variable(t.ones(2, 2), requires_grad = True)
# print(x)
#
# y = x.sum()    #y = x.sum() = (x[0][0] + x[0][1] + x[1][0] + x[1][1])
# print(y)
# print(y.grad_fn)
# # <SumBackward0 object at 0x000002414710C8D0>
#
# y.backward()  #反向传播,计算梯度,第一次
# print(x.grad)
#
# y.backward()  #反向传播,计算梯度,第二次
# print(x.grad)
#
# y.backward()  #反向传播,计算梯度,第三次
# print(x.grad)
#
# print(x.grad.data.zero_())  #梯度清零,这里使用inplace操作



x = Variable(t.ones(4, 5))
t.cos_(x)  #inplace操作
y = t.cos(x)
x_tensor_cos = t.cos(x.data)
print(y)
print(x_tensor_cos)
