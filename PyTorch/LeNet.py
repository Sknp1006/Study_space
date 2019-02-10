'''
LeNet5是最早的卷积神经网络
卷积神经网络（Convolutional Neural Networks, CNN）
是一类包含卷积计算且具有深度结构的前馈神经网络（Feedforward Neural Networks），
是深度学习（deep learning）的代表算法之一[1][2]。
由于卷积神经网络能够进行平移不变分类（shift-invariant classification），
因此也被称为“平移不变人工神经网络（Shift-Invariant Artificial Neural Networks, SIANN）”
'''

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch as t

class Net(nn.Module):
    def __init__(self):
        #nn.Module子类的函数必须在构建函数中执行父类的构造函数
        #下列等价于nn.Module.__init__(self)
        super(Net, self).__init__()
        #卷积层'1'表示输入图片为单通道,'6'表示输出通道数
        #'5'表示卷积核为5*5
        self.conv1 = nn.Conv2d(1, 6, 5)
        #卷积层
        self.conv2 = nn.Conv2d(6, 16, 5)
        #仿射层/全连接层, y = Wx + b
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        #卷积-->激活-->池化
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        #reshape, '-1'表示自适应
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
# print(net)
params = list(net.parameters())
# print(params)
# print(net.parameters())
for name, parameters in net.named_parameters():
    print(name, ':', parameters.size())

input = Variable(t.randn(1, 1, 32, 32))
out = net(input)
print(out.size())

net.zero_grad()  #所有参数的梯度清零
out.backward(Variable(t.ones(1, 10)))  #反向传播

output = net(input)
target = Variable(t.arange(0., 10.))
criterion = nn.MSELoss()
loss = criterion(output, target)
print(loss)
# loss.grad_fn
loss.backward()
print(loss.grad_fn)