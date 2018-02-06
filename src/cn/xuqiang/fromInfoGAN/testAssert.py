# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

# 在开发一个程序时候，与其让它运行时崩溃，不如在它出现错误条件时就崩溃（返回错误）。这时候断言assert 就显得非常有用。
#
# assert的语法格式：
#
# assert expression
# 它的等价语句为：
#
# if not expression:
#     raise AssertionError

str_a ="xuqiang"
assert type(str_a) == int