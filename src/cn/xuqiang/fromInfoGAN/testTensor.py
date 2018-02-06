# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
arrays = tf.random_normal((10,4))
for i in arrays:
    print("============")
    print(i)
    print("============")