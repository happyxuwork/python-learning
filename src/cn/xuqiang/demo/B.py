# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

from A import (
    methodA,
    methodA1,
    methodA2,
)
def methodB():
    methodA()
    methodA1()
    methodA2()
    print("i am the method B")



if __name__ == "__main__":
    methodB()