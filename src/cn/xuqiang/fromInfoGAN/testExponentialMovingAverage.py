# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
# shadow_variable = decay * shadow_variable + (1-decay) * variable
# tf.train.ExponentialMovingAverage这个函数还提供了自己动更新decay的计算方式：
# decay= min（decay，（1+steps）/（10+steps））
# steps是迭代的次数，可以自己设定。
import tensorflow as tf
w = tf.Variable(1.0)
ema = tf.train.ExponentialMovingAverage(0.9)
update = tf.assign_add(w,1.0)
# ema_op = ema.apply([w])
with tf.control_dependencies([update]):  #这句话放在这里和上面是不一样的，放在上面的话，输出全为1
    print("yes")

ema_op = ema.apply([w])
ema_val = ema.average(w)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(3):
        sess.run(ema_op)
        print(sess.run(ema_val))
        # 输出：
        # 1.1      =0.9*1 + 0.1*2
        # 1.29     =0.9*1.1+0.1*3
        # 1.561    =0.9*1.29+0.1*4