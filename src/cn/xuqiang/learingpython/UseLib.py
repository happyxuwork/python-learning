# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import numpy as np
import matplotlib.pyplot as plt
'''
drawing the picture you want
'''
# x= np.linspace(0,10,100)
# y = np.sin(x)+1
# z= np.cos(x**2)+1
#
# plt.figure(figsize=(8,4))
# plt.plot(x,y,label='$\sin x+1$',color='red',linewidth = 2)
#
# plt.plot(x,z,'b--',label = '$\cos x^2+1$')
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('a simple example')
# plt.ylim(0,2,2)
# plt.legend()
# plt.show()

'''
use pandas
'''
import pandas as pd
# s = pd.Series([1,2,3],index= ['a','b','c'])
# d = pd.DataFrame([[1,2,3],[4,5,6]])
# d2 = pd.DataFrame(s)
#1-布尔索引
# print(d.head())
# print(d.describe())
#
data = pd.read_excel("E:\\file\\1.xls", index_col="ID")
# print(data)
#
# print(data.loc[(data["CUSTOMER"]==5) & (data["TIME"]==4),
# ["CUSTOMER","TIME"]])

#Create a new function:
# def num_missing(x):
#   return sum(x.isnull())
# #Applying per column:
# print "Missing values per column:"
# print data.apply(num_missing, axis=0) #axis=0 defines that function is to be applied on each column
# #Applying per row:
# print "nMissing values per row:"
# print data.apply(num_missing, axis=1).head() #axis=1 defines that function is to be applied on each row


from sklearn.linear_model import LinearRegression

from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
print(iris.data.shape)
clf = svm.LinearSVC()
clf.fit(iris.data,iris.target)
print(clf.predict([[5.0,3.6,1.3,0.25]]))
print(clf.coef_)

