# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
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


string = "fc:1024,fc:7x7x128,reshape:7:7:128,deconv:4:2:64,deconv:4:2:1:sigmoid"
layer_strs = string.split(",")
for i, layer in enumerate(layer_strs):
    print(str(i)+"======"+layer)
    if layer.startswith("fc"):
        params = layer[len("fc:"):].split(":")
        nonlinearity_str = 'relu'
        if len(params) == 2:
            params, nonlinearity_str = params[:-1], params[-1]
            print("yes")
        num_outputs = parse_math(params[0])
        print(num_outputs)