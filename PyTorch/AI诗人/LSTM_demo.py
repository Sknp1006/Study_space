import torch as t
from torch import nn
from torch.autograd import Variable

# 输入词用10维词向量表示
# 隐藏元用20维向量表示
# 两层的lstm
rnn = nn.LSTM(10, 20, 2)

# 输入每句话有5个词
# 每个词由10维的词向量表示
# 总共三句话
input = Variable(t.randn(5, 3, 10))

# 隐藏元（hidden state和cell state）的初始值
# 形状（num_layers, batch size, hidden_size）
h0 = Variable(t.zeros(2, 3, 20))
c0 = Variable(t.zeros(2, 3, 20))

#output是最后一层所有隐藏元的值
#hn和cn是所有层（这里有两层）的最后一个隐藏元的值
output, (hn, cn) = rnn(input, (h0, c0))

print(output.size())
print(hn.size())
print(cn.size())