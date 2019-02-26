'''
numpy 与 Tensor 可以互转
二者共享内存
转换时基本不消耗资源
'''
import torch as t
import numpy

# a = t.ones(5)
# print(a)
#
# b = a.numpy()
# print(b)

import numpy as np

a = np.ones(5)
print(a)
b = t.from_numpy(a)
print(b)

b.add_(1)
print(b)
print(a)
# tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
# [2. 2. 2. 2. 2.]


#z 转为GPU的Tensor
# if t.cuda.is_available():
#     x = x.cuda()
#     y = y.cuda()
#     x + y