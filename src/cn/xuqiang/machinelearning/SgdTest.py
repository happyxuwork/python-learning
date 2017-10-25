#encoding = UTF-8
'''
@author: xuqiang
'''
import numpy as np
class Network(object):
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x)
                        for x,y in zip(sizes[:-1],sizes[1:])]

size = [2,3,1]
net = Network(size)
print(net.num_layers)
print(net.sizes)
print(net.biases)
print(net.weights)