import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

state = tf.Variable(0, name='counter')
#print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()  #important

with tf.Session() as sess:
    sess.run(init)      #初始化init绑定的Variable
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))


#请使用tf.global_variables_initializer初始化变量