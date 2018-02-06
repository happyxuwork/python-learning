# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import tensorflow as tf
import tensorflow.contrib.layers as layers


def leaky_rectify(x, leakiness=0.01):
    assert leakiness <= 1
    ret = tf.maximum(x, leakiness * x)
    return ret

NONLINEARITY_NAME_TO_F = {
    'lrelu': leaky_rectify,
    'relu': tf.nn.relu,
    'sigmoid': tf.nn.sigmoid,
    'tanh': tf.nn.tanh,
    'identity': tf.identity,
}

OPS =  [
   ('+', lambda a, b: a+b),
   ('-', lambda a, b: a-b),
   ('*', lambda a, b: a*b),
   ('x', lambda a, b: a*b),
   ('/', lambda a, b: a//b),
]


def parse_math(s):
   for operator, f in OPS:
       try:
           idx = s.index(operator)
           return f(parse_math(s[:idx]), parse_math(s[idx+1:]))
       except ValueError:
           pass
   return int(s)

# string = "fc:1024,fc:7x7x128,reshape:7:7:128,deconv:4:2:64,deconv:4:2:1:sigmoid"
# string = "conv:4:2:64:lrelu,conv:4:2:128:lrelu,fc:1024:lrelu"
string = "fc:1024"
layer_strs = string.split(",")

out = tf.Variable(tf.random_normal([64, 62]))
for i, layer in enumerate(layer_strs):
    print(str(i)+"======"+layer)

    if layer.startswith("fc"):
        maybe_fc_batch_norm = layers.batch_norm
        is_training = True
        layer_idx = 0
        params = layer[len("fc:"):].split(":")
        nonlinearity_str = 'relu'
        if len(params) == 2:
            params, nonlinearity_str = params[:-1], params[-1]
        num_outputs = parse_math(params[0])
        nonlinearity = NONLINEARITY_NAME_TO_F[nonlinearity_str]

        out = layers.fully_connected(
            out,
            num_outputs=num_outputs,
            activation_fn=nonlinearity,
            normalizer_fn=maybe_fc_batch_norm,
            normalizer_params={"is_training": is_training, "updates_collections": None},
            # scope='layer_%d' % (layer_idx,)
        )
        print(out)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(out))