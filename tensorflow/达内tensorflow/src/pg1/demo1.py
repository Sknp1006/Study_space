'''
1/ 导入库
'''
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

'''
2/ 数据预处理： 加载数据  分割数据  数据可视化
'''
x = [[0, 0], [1, 0], [0, 1], [1, 1], [1, 1], [0, 0]]
y = [0, 1, 1, 1, 1, 0]

# for lbl, dt in zip(y, x):
#     plt.plot(dt[0], dt[1],
#              'o' if lbl else '^',  # 形状
#              mec='r' if lbl else 'g')  # 颜色
# 数据可视化，绘制样本散点图
# 将标签为0的显示为绿色
# 将标签为1的显示为红色
# plt.show()

'''
3/ 构建神经网络
'''
weights = np.random.normal(0, 0.001, size=[np.array(x).shape[1], 1])
print(list(zip(weights, [0,1])))
bias = np.random.normal(0, 0.001, size=1)

'''
4/ 训练模型
'''


# y = np.dot(x, weights) + bias

# 激活函数
def f(lin_r):
    return 1 if lin_r > 0 else 0


# 预测输出
def predict(vec, theta, b):
    '''
    :param vec: 输入的特征向量
    :param theta:  权重参数
    :param b:  阈值
    :return:  预测结果
    '''
    return f(np.dot(vec, theta) + b)


# 测试代码，输出训练集的预测结果
# for v in x:
#     pred = predict(v, weights, bias)
# print("测试输出", pred)

'''
5/ 优化
反向传播算法： 通过预测结果计算预测的误差，根据误差反向调整权重和阈值
'''


def updata_theta(pred, y_true, rate, vec):
    """
    :param pred: 预测结果
    :param y_true:  正确标签
    :param rate:  学习速率
    :param vec:  输入值
    :return:
    """
    # 误差函数
    loss = y_true - pred
    # 调整权重参数
    global weights
    weights = list(map(lambda x1: x1[0] + x1[1] * loss * rate, list(zip(weights, vec))))
    print('weights:', weights, list(zip(weights, vec)))
    global bias
    bias = bias + loss * rate


def one_iter():
    samples = zip(x, y)
    for v, lbl in samples:
        print('V:', v, 'lbl:', lbl)
        pred = predict(v, weights, bias)  # 预测结果
        updata_theta(pred, lbl, 0.1, v)  # 权重参数


# 测试代码
# for i in range(100):
#     one_iter()
    # print(weights, bias)
one_iter()
'''
6/ 性能评估
'''
x_text = [0, 0]
y_text = predict(x_text, weights, bias)
print(y_text)
