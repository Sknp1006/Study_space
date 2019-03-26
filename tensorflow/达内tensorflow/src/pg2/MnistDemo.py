import numpy as np
import tensorflow as tf
from DataUtil import *
import os
import time
from datetime import timedelta


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

# 卷积层1,32个结果,28*28
con1 = tf.layers.conv2d(inputs=x_img,  # inputs: 卷积的对象
                        filters=32,  # filters: 卷积核数量 16或32
                        kernel_size=[5, 5],  # kernel_size: 卷积核大小（一般为奇数，有中心能对齐）
                        padding='same',  # padding: 填充，same产生的大小与原图相同
                        activation=tf.nn.relu)  # activation: 激活函数

# 池化层1,32个结果,14*14
pool1 = tf.layers.max_pooling2d(inputs=con1, pool_size=[2, 2], strides=2)

# 卷积层2，64个14*14结果
con2 = tf.layers.conv2d(inputs=pool1,
                        filters=64,
                        kernel_size=[5, 5],
                        padding='same',
                        activation=tf.nn.relu)

# 池化层，64个7*7结果
pool2 = tf.layers.max_pooling2d(inputs=con2, pool_size=[2, 2], strides=2)

# 对池化结果进行扁平化操作
flat = tf.reshape(pool2, shape=[-1, 7 * 7 * 64])

# 全连接层1
full1 = tf.layers.dense(inputs=flat, units=1024, activation=tf.nn.relu)

# 防止过拟合
# rate 降采样,照顾大多数情况，不理睬个别数据
dp = tf.layers.dropout(inputs=full1, rate=0.4)

# 全连接层2
'''
  最后一层输出0~9这10个数字的概率值
  不再使用relu激活函数
  对于二分类使用sigmoid函数
'''
full2 = tf.layers.dense(inputs=dp, units=10)
logit = tf.nn.softmax(full2)  # 归一化
pred = tf.argmax(logit, dimension=1)  # 预测类别

# 利用交叉熵定义损失函数
cross = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logit)
cost = tf.reduce_mean(cross)  # 损失均值

# 优化,随机梯度下降
train = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

# 性能评估
corr_pred = tf.equal(y_true, pred)
acc = tf.reduce_mean(tf.cast(corr_pred, tf.float32))

# 保存训练模型
# 创建保存路径
save_dir = 'checkpoint/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
save_path = os.path.join(save_dir, 'bestmodel')
# 模型保存
saver = tf.train.Saver()

# 分批处理样本的数量
batch_size = 64


def opt(num_iter):
    '''
    :param num_iter: 更新迭代的次数
    :return: 无
    '''
    session = tf.Session()  # 创建会话
    session.run(tf.global_variables_initializer())  # 初始化全局变量

    # 最优准确率
    best_acc = 0
    for i in range(num_iter):
        # 不断产生参与训练的样本
        x_batch, y_batch = mnist.train.next_batch(batch_size)
        # 执行优化与性能评估
        _, ac = session.run([train, acc], feed_dict={x: x_batch, y: y_batch})

        if i % 100 == 0:
            print('迭代次数：{0}， 准确率：{1}'.format((i + 1), ac))

        # 保存最优准确率对应的模型
        if ac > best_acc:
            best_acc = ac
            saver.save(sess=session, save_path=save_path)

    # 使用训练后的权重参数，输出测试集第一个样本的标签
    pred_test = session.run(pred, feed_dict={x: mnist.test.images[:1]})
    print(pred_test)
    print('正确标签：{0}'.format(mnist.test.cls[:1]))


opt(1000)
