import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)  #matmul

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[7.], input2:[2.]}))



# multiply与matmul的区别
# a
# [[1, 2, 3],
#  [4, 5, 6]] a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# b1
# [[ 7,  8],
#  [ 9, 10],
#  [11, 12]] b1 = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])

#b2
#[[ 7  8  9]
# [10 11 12]] b2 = tf.constant([7, 8, 9, 10, 11, 12], shape=[2, 3])


# c矩阵相乘 第一个矩阵的列数（column）等于第二个矩阵的行数（row）
# [[ 58,  64],
#  [139, 154]] c = tf.matmul(a, b1)

# d`数元素各自相乘
#[[ 7 16 27]
# [40 55 72]] d = tf.multiply(a, b2) #维度必须相等 with tf.Session()
