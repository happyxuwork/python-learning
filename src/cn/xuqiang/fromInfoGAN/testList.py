# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import numpy as np
import tensorflow as tf

kk = tf.random_normal(shape=(64,10))
num_categorical = sum([true_categorical.get_shape()[1].value for true_categorical in kk])
# for k in kk:
#     print(k)




