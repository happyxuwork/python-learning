# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import pandas as pd
# # category = '..\..\data\section3\catering_dish_profit.xls'
# category = '..\..\data\section3\catering_sale_all.xls'
# data = pd.read_excel(category,index_col=u'日期')
# data.corr()#相关系数矩阵，给出了任意两款菜式之间的相关系数
# print(data.corr()[u'百合酱蒸凤爪'])#只显示百合酱蒸凤爪与其它菜系的相关系数
# print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))
# print(u'各列sum:')
# print(data.sum())
# print("=============")
#
# print(u'各列均值:')
# print(data.mean())
# print("=============")
#
# print(u'各列方差:')
# print(data.var())
# print("=============")
# data = data[u'盈利'].copy()
# data.sort(inplace = True)
# print(data)

# D = pd.DataFrame([range(8,30,2),range(2,9)])
# D.corr(method = 'pearson')
# S1 = D.loc[0]
# S2 = D.loc[1]
# print(S1.corr(S2,method='pearson'))


import numpy as np
D = pd.DataFrame(np.random.randn(6,5))#随机产生6*5的矩阵
print(D)
print(D.describe())

print(D.cov())
print(D[0].cov(D[1]))






