# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf

'''
下面的例子不行啊
def method1():
    return "method1"

def method2():
    return "method2"


flag = tf.placeholder(tf.bool,[])
flag = True


normalized_x = tf.cond(
        1>2,
        method1,
        method2,
        )

print(normalized_x)

#
# import tensorflow as tf
# a=tf.constant(2)
# b=tf.constant(3)
# x=tf.constant(4)
# y=tf.constant(5)
# z = tf.multiply(a, b)
# result = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
with tf.Session() as session:
    # print(result.eval())
    print(normalized_x)
'''
a=tf.constant(2)
b=tf.constant(3)
x=tf.constant(4)
y=tf.constant(5)

tf.equal(1, 1)
z = tf.multiply(a, b)

is_training = tf.placeholder(
        tf.bool,
        [],
        name="is_training_generator"
    )
result = tf.cond(tf.equal(1, 1), lambda: tf.add(x, y), lambda: tf.square(y))
with tf.Session() as session:
    print(result.eval())