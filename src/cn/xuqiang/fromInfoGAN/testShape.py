# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
import numpy as np

x=tf.constant([[1,2,3],[4,5,6]])
y=[[1,2,3],[4,5,6]]
z=np.arange(24).reshape([2,3,4])
# 返回的是个元组
print(x.get_shape()[-1])

# 返回的是个Tensor
print(tf.shape(y))
print(tf.shape(z))