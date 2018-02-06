# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
img = tf.Variable(tf.random_normal([128, 32, 32, 64]))
# print(img)
axis = list(range(len(img.get_shape()) - 1))
mean, variance = tf.nn.moments(img, axis)
# print("=====================")
# print(mean)
# print("=====================")
# print(variance)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(img))
    print(sess.run(mean))
    print(sess.run(variance))
