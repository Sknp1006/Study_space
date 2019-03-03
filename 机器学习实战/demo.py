# from numpy import *
# import numpy as np
# group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
# t = tile([0,0], (4,1)) - group
# print(group.shape[0])
# print(t**2)

# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# c=np.array([[1,2,3],[4,5,6]])
#
# print(c.dot(a))
#
# zero = zeros((1, 5))
# print(zero)

# import operator
# demo = {'动作片': 2, "爱情片": 1}
# sorted1 = sorted(demo.items(), key=operator.itemgetter(1), reverse=True)
# # print(sorted1[0][0])
# print(demo.items())
# import numpy
# for i in range(10):
#     b = numpy.log(i*0.1)
#     print(b)

import re
import jieba
#
# def jiebaCut(text):
#     r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
#     text = text.strip()
#     text = re.sub(r, '', text)
#     print(text)
#     # 添加停用词
#     stopwords = [word.split('\n')[0] for word in open(r'C:\Users\74001\Documents\GitHub\Study_space\机器学习实战\朴素贝叶斯\stopwords_cn.txt', 'r', encoding='utf8').readlines()]
#     print(stopwords)
#     # if '很' in stopwords:
#     #     print('hen')
#     # 分词
#     cutText = list(jieba.cut(text, cut_all=False))
#     print(cutText)
#     final = []
#     for seg in cutText:
#         # print(seg)
#         if seg not in stopwords:
#             final.append(seg)
#     print(final)
#     # 去除标点
#     return final
# r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
# text = '其他词都出现1次，那么为什么接下来输出的是“著名景点”、“太和殿”和“向阳”呢？这是因为，在词频一样的前题下，根据TF/IDF的顺序来输出，因为其他词的TF一样（都是1），所以IDF小的会先输出来。不知道结巴分词是根据什么来判断IDF的，假如是根据dict.txt中的第二列词频来判断'
# text = re.sub(r, '', text)
# print(text)
# jiebaCut(text)
# '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
from numpy import *

def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

dataMatIn, classLabels = loadDataSet(r'C:\Users\74001\Documents\GitHub\Study_space\机器学习实战\支持向量机\testSet.txt')

dataMatrix = mat(dataMatIn)
labelMat = mat(classLabels).transpose()
b = 0
m, n = shape(dataMatrix)
alphas = mat(zeros((100, 1)))
fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[1, :].T))
# print(dataMatrix)
# print(dataMatrix * dataMatrix[1, :].T)

print((multiply(alphas, labelMat).T).shape)
print(dataMatrix * dataMatrix[1, :].T)
print(fXi)