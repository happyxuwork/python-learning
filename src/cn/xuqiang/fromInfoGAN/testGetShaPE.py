# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
import numpy as np
# true_categoricals = tf.random_normal((64,10))
# true_continuous = tf.random_normal((64,2))
# print(true_categoricals)
# true_categoricals = np.arange(640).reshape(64,10)
# true_continuous = np.arange(128).reshape(64,2)

true_categoricals = [[1 for col in range(10)] for row in range(64)]
true_categoricals = np.array(true_categoricals)
true_categoricals = tf.convert_to_tensor(true_categoricals)

true_continuous = [[1 for col in range(2)] for row in range(64)]
true_continuous = np.array(true_continuous)
true_continuous = tf.convert_to_tensor(true_continuous)

num_categorical = sum([true_categorical.get_shape()[1].value for true_categorical in true_categoricals])
num_continuous = true_continuous.get_shape()[1].value

print(num_categorical)
print(num_continuous)