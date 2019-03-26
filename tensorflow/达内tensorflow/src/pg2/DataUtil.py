import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data


def loadData(filename):
    '''

    :param filename: 文件路径
    :return: mnist数据集
    mnist.train: 55000
        images: 以二进制形式存储文件，28x28像素共784个
        labels: 图片对应的标签，默认以十进制存储0~9
    mnist.validation: 5000
        images: 以二进制形式存储文件，28x28像素共784个
        labels: 图片对应的标签，默认以十进制存储0~9
    mnist.test: 10000
        images: 以二进制形式存储文件，28x28像素共784个
        labels: 图片对应的标签，默认以十进制存储0~9

    '''
    mnist = input_data.read_data_sets(filename, one_hot=True)
    mnist.train.cls = np.argmax(mnist.train.labels, axis=1)
    mnist.test.cls = np.argmax(mnist.test.labels, axis=1)
    mnist.validation.cls = np.argmax(mnist.validation.labels, axis=1)
    return mnist


def plotData(imgs, cls, pred=None):
    '''

    :param imgs: 可视化图片
    :param cls: 图片标签
    :param pred: 图片预测结果，默认None
    :return: 无
    '''
    assert len(imgs) == len(cls) == 9
    fix, axis = plt.subplots(3, 3)
    for i, axi in enumerate(axis.flat):
        axi.imshow(imgs[i].reshape((28, 28)), cmap='binary')
    plt.show()


mnist = loadData('../../dataset')
plotData(mnist.train.images[:9], mnist.train.cls[:9])
# print(mnist)
