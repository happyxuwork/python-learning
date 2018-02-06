# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf


'''
W = tf.constant([[-2.,12.,6.],
                 [3.,2.,8.]], )
mean,var = tf.nn.moments(W, axes = [0])
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    resultMean = sess.run(mean)
    print(resultMean)
    resultVar = sess.run(var)
    print(resultVar)

    size = 3
    scale = tf.Variable(tf.ones([size]))
    shift = tf.Variable(tf.zeros([size]))
    epsilon = 0.001
    W = tf.nn.batch_normalization(W, mean, var, shift, scale, epsilon)
    # 必须要加这句不然执行多次sess会报错
    sess.run(tf.global_variables_initializer())
    resultW = sess.run(W)
    print(resultW)
    # 观察初始W第二列 12>2 返回BN的W值第二列第二行是负的，其余两列相反
    # 参考下图BN的公式，相当于进行如下计算
    # W = (W - mean) / tf.sqrt(var + 0.001)
    # W = W * scale + shift
'''



# tf.nn.moments()
# * for so-called "global normalization", used with convolutional filters with
#      shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
#    * for simple batch normalization pass `axes=[0]` (batch only).
shape = [128, 32, 32, 64]
a = tf.Variable(tf.random_normal(shape))        # a：activations
axis = list(range(len(shape)-1))                # len(x.get_shape())
a_mean, a_var = tf.nn.moments(a, axis)
# 这里我们仅给出 a_mean, a_var 的维度信息，
sess = tf.Session()
sess.run(tf.global_variables_initializer())
a = sess.run(a)
a_mean = sess.run(a_mean)
print(a_mean.shape)      # (64, )
a_var = sess.run(a_var)
print(a_var.shape)       # (64, )    ⇒ 也即是以 kernels 为单位，batch 中的全部样本的均值与方差