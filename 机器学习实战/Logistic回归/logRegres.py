from math import exp
from numpy import *


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    # 将列表转成矩阵
    dataMatrix = mat(dataMatIn)
    # 将lableMat转成矩阵后进行转置
    labelMat = mat(classLabels).transpose()
    m, n = shape(dataMatrix)
    alpha = 0.002  # 移动步长，学习速率，控制更新幅度
    maxCycles = 500
    weights = ones((n, 1))
    for k in range(maxCycles):
        # 梯度上升矢量化数据
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


if __name__ == '__main__':
    dataArr, labelMat = loadDataSet()
    print(dataArr)  # 二维数组
    print(labelMat)
    print(gradAscent(dataArr, labelMat))