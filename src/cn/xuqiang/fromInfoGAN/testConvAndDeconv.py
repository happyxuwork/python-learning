# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow.contrib.layers as layers
import tensorflow as tf
# tf.set_random_seed(1)
# x = tf.random_normal(shape = [1,3,3,1])
# y = layers.convolution2d_transpose(x,1,3)
# sess = tf.Session()
# tf.global_variables_initializer().run(session = sess)
# print(y.eval(session=sess))

def conv_batch_norm(inputs,
                    name="batch_norm",
                    is_training=True,
                    trainable=True,
                    epsilon=1e-5):
    # 使用的是==滑动平均的方法更新参数
    ema = tf.train.ExponentialMovingAverage(decay=0.9)
    # get_shape() of the last dimension
    shp = inputs.get_shape()[-1].value
    print("this is a debug information==输入中的get_shape()[-1]的值为: "+str(shp))
    with tf.variable_scope(name) as scope:
        # 函数原型：tf.random_normal_initializer(mean=0.0, stddev=1.0, seed=None, dtype=tf.float32)
        # 返回一个生成具有正态分布的张量的初始化器。
        gamma = tf.get_variable("gamma", [shp], initializer=tf.random_normal_initializer(1., 0.02), trainable=trainable)
        beta = tf.get_variable("beta", [shp], initializer=tf.constant_initializer(0.), trainable=trainable)

       #  tf.nn.moments(inputs, [0, 1, 2])==对四维向量进行均值和方差的计算，其中返回depth维度的tensor
       # * for so-called "global normalization", used with convolutional filters with
       #   shape `[batch, height, width, depth]`, pass `axes=[0, 1, 2]`.
       # * for simple batch normalization pass `axes=[0]` (batch only).
        mean, variance = tf.nn.moments(inputs, [0, 1, 2])
        # tensor.set_shape()重新设置tensor的形状
        mean.set_shape((shp,))
        variance.set_shape((shp,))
        ema_apply_op = ema.apply([mean, variance])

        def update():
            with tf.control_dependencies([ema_apply_op]):
                # tf.nn.batch_norm_with_global_normalization===提供了进行批量归一化的操作。
                print("this is a debug information==进行update操作--mean和variance的值为: "+str(mean)+",,"+str(variance))
                return tf.nn.batch_norm_with_global_normalization(
                    inputs, mean, variance, beta, gamma, epsilon,
                    scale_after_normalization=True
                )
        def do_not_update():
            return tf.nn.batch_norm_with_global_normalization(
                inputs, ema.average(mean), ema.average(variance), beta,
                gamma, epsilon,
                scale_after_normalization=True
            )
        # 相当于c语言中的if...else...
        normalized_x = tf.cond(
            is_training,
            update,
            do_not_update
        )
        return normalized_x
'''
测试反卷积的输出
out1 = tf.random_normal(shape=[1024,7,7,128])
nkernels = 4
num_outputs = 64
stride = 2
nonlinearity = tf.nn.relu
is_training = tf.equal(1,1)
maybe_conv_batch_norm = conv_batch_norm
out = layers.convolution2d_transpose(
                out1,
                num_outputs=num_outputs,
                kernel_size=nkernels,
                stride=stride,
                activation_fn=nonlinearity,
                normalizer_fn=maybe_conv_batch_norm,
                normalizer_params={"is_training": is_training},
                scope='layer_%d' % (1,)
            )
print(out)

'''

# 测试卷积的输出
out1 = tf.random_normal(shape=[64, 28, 28, 1])
nkernels = 4
num_outputs = 64
stride = 2
nonlinearity = tf.nn.relu
is_training = tf.equal(1, 1)
maybe_conv_batch_norm = conv_batch_norm
out = layers.convolution2d(
    out1,
    num_outputs=num_outputs,
    kernel_size=nkernels,
    stride=stride,
    normalizer_params={"is_training": is_training},
    normalizer_fn=maybe_conv_batch_norm,
    activation_fn=nonlinearity,
    scope='layer_%d' % (1,)
)
print(out)