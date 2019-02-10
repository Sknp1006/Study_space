import torch as t
from torch import nn

embedding = t.nn.Embedding(10, 2)  #十个词，每个词用二维词向量表示
input = t.arange(0, 6).view(3, 2).long()  #三个句子，每句有两个词
input = t.autograd.Variable(input)
output = embedding(input)
print(output.size())
print(embedding.weight.size())
