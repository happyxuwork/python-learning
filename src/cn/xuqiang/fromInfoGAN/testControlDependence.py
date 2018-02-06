# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
'''
tf.control_depencies结合tf.identity使用的情况
其中tf.control_dependencies()设计是用来控制计算流图的，给图中的某些计算指定顺序。
比如：我们想要获取参数更新后的值，那么我们可以这么组织我们的代码。
w = tf.Variable(1.0)
ema = tf.train.ExponentialMovingAverage(0.9)
update = tf.assign_add(w, 1.0)

ema_op = ema.apply([update])
with tf.control_dependencies([ema_op]):
    ema_val = tf.identity(ema.average(update)) #一个identity搞定

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(3):
        print(sess.run([ema_val]))

'''
x = tf.Variable(0.0)
#返回一个op，表示给变量x加1的操作
x_plus_1 = tf.assign_add(x, 1)

#control_dependencies的意义是，在执行with包含的内容（在这里就是 y = x）前
#先执行control_dependencies中的内容（在这里就是 x_plus_1）
with tf.control_dependencies([x_plus_1]):
    y = tf.identity(x)
init = tf.initialize_all_variables()

with tf.Session() as session:
    init.run()
    for i in range(5):
        print(y.eval())#相当于sess.run(y)，由于control_dependencies的所以执行print前都会先执行x_plus_1
