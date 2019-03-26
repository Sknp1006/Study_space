import numpy as np
import tensorflow as tf
from DataUtil import *

def fun1():
    # 定义常量
    t1 = tf.constant([[1, 2], [3, 4]])
    t = t1 * 2
    # 定义变量
    t2 = tf.Variable(tf.random.normal(shape=[2, 1]))
    print(t)
    print(t1)
    # 定义占位符
    t1 = tf.placeholder(tf.float32)
    t2 = tf.placeholder(tf.float32)
    t3 = t1 + t2

    sess = tf.Session()
    ts = sess.run(t3, feed_dict={t1: 3.0, t2: 4.0})
    print(ts)
    sess.close()

x = tf.placeholder(tf.float32, shape=[None, 784])  # 表示不关心有多少样本,784个特征
y = tf.placeholder(tf.float32, shape=[None, 10])  # 表示有10个分类
# 将输入数据修改为矩阵
# shape: [样本数量，行，列，颜色通道]
x_img = tf.reshape(x, shape=[-1, 28, 28, 1])
# 样本真实标签
y_true = tf.argmax(y, dimension=1)
