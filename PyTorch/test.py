from torch.autograd import Variable
import torch as t

u = Variable(t.Tensor(range(0, 10)))
print(u)
s = Variable(t.arange(0., 10.))
print(s.type())