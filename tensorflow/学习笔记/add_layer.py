import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#添加层
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#定义隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

#定义输出层
predition = add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition),reduction_indices=[1]))

#用优化器以0.1的学习效率优化误差
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

# with tf.Session() as sess:
for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i % 50:
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        # print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
        predition_value = sess.run(predition, feed_dict={xs:x_data})
        lines = ax.plot(x_data, predition_value, 'r-', lw=5)
        plt.pause(0.1)
