#encoding = UTF-8
'''
@author: xuqiang
'''
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [i+2 for i in a]
# # for i in a:
# #     b.append(i+2)
# print(b)

# b = dict.fromkeys(['xu','qiang'],20)
# print(b)
'''
the use of set
'''
# a = {1,2,3,4,5}
# b = {1,2,3,6,7,8}
# print(a | b)
# print(a & b)
# print(a - b)

'''
use map
'''
# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# if len(a)==len(b):
#     print(list(map(lambda x, y: x * y, a, b)))
# else:
#     print('sorray')

'''
use reduce to get the result of iterator
'''
# print(reduce(lambda x,y:x*y,range(1,10)))
# #be equal to the fellow
# s = 1
# for i in range(1,10):
#     s = s * i
# print(s)

'''
use filter to get what you want
'''
print(filter(lambda x:x>5 and x<10,range(1,10)))








