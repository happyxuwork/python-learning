# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# arr = pd.Series([2,-10,62,56],index=['a','b','c','d'])
# arr.name = 'values'
# arr.index.name = 'index'
# arr.sort()
# print(arr)
# #print(arr[arr >20])

dataFrame = DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],
          columns=['one','two','three','four'])
# col = ['he','yy','cc']
# print(dataFrame)
#
# dataCIndex = dataFrame.reindex(['a','b','c','d'],method='ffill')
# dataCCol = dataFrame.reindex(columns=col)
# print(dataCIndex)
# print(dataCCol)
#print(dataFrame)
# print(dataFrame[0:2]) #get the 0 1 row
# print(dataFrame.iat[0,0])#get the (0,0) position value
# print(dataFrame[['one','two']])#get the one two col values
# print(dataFrame.ix[0:2,[0,1,2]]) #get the ...

# f = lambda x : x.max() - x.min()
# print(dataFrame.apply(f,axis=0)) #apply the function f to the all col of dataFrame
# print(dataFrame.apply(f,axis=1)) #apply the function f to the all row of dataFrame


# def f(x):
#     return Series([x.min(),x.max()],index=['min','max'])
# print(dataFrame.apply(f))
# dataFrame.apply(f).to_csv('E:/file/python/data/a.csv',encoding='UTF-8')



# import sqlalchemy
# mysql_cn= sqlalchemy.connect(host='localhost', port=3306,user='myusername', passwd='mypassword', db='mydb')
# df = pd.read_sql('select * from test;', con=mysql_cn)
# mysql_cn.close()
# dataFrameother = DataFrame(np.arange(15).reshape(5,3))
#
# from sqlalchemy import create_engine
# yconnect = create_engine('mysql+mysqldb://root:root@localhost:3306/test?charset=utf8')
# pd.io.sql.to_sql(dataFrameother,'customer', yconnect, schema='test', if_exists='append')

'''
排序
'''
# frame = DataFrame(np.arange(8).reshape(2,4),index=['one','three'],
#                   columns=['d','a','b','c'])
# print(frame)
# print(frame.sort_index(axis=1,ascending=False))
# print(frame.sort_values(by=['a']))

# obj = Series(['b','g','f','a','d','b','c','d','c','a'])
# print(obj.unique())
# #print(obj.value_counts().sort_values(ascending=False))
# objother = obj.value_counts()
#
# print(type(objother))
# print(objother)



df = pd.read_excel('E:/file/python/data/d1.xlsx')
print(df)

df1 = pd.read_excel('E:/file/python/data/d1.xlsx',na_values=['56'])
print(df1)











