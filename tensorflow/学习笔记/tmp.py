import os
import tensorflow as tf

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

A = tf.Variable(tf.constant(0.0), dtype=tf.float32)
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(sess.run(A))
	sess.run(tf.assign(A, 10))
	print(sess.run(A))

#请使用tf.global_variables_initializer初始化变量