import os
import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

#占位，便于后面加数据
x = tf.placeholder("float", [None, 784])  #行不定，784列
#定义变量(返回值：<tf.Variable 'Variable:0' shape=(784, 10) dtype=float32_ref>)
#定义一个784行，10列的矩阵(784个特征和10个输出值)
W = tf.Variable(tf.zeros([784,10]))
#定义一个10列的矩阵
b = tf.Variable(tf.zeros([10]))
#定义softmax函数(映射为0-1之间的实数)
y = tf.nn.softmax(tf.matmul(x,W) + b)  #矩阵相乘

y_ = tf.placeholder("float", [None,10])  #行不定，10列
#交叉熵, y为实际输出，y_为期望输出(一种损失函数)
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#设置优化器(tensorflow有大量的优化算法)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#变量初始化
init = tf.global_variables_initializer()
#创建会话
sess = tf.Session()
#sess.run(执行的操作，参数)
sess.run(init)

#设置训练次数
for i in range(1000):
    #next_batch的参数是训练数据的数量
    batch_xs, batch_ys = mnist.train.next_batch(100)
    #用batch_xs,batch_ys代替占位符，通过优化器训练
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

#tf.equal 来检测我们的预测是否真实标签匹配(索引位置一样表示匹配)
#这里返回一个布尔数组。为了计算我们分类的准确率，我们将布尔值转换为浮点数来代表对、错，然后取平均值
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#计算准确率
#cast(原格式， 目标格式)
#reduce_mean根据维度取平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# eval() 其实就是tf.Tensor的Session.run() 的另外一种写法
# print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

