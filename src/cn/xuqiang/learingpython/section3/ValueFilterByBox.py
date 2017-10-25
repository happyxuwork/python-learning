# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import pandas as pd
category = '..\..\data\section3\catering_sale.xls'
data = pd.read_excel(category,index_col=u'日期')
# #DataFrame类型有describe函数
# print data.describe()#可以查看数据的基本情况，要加个print，不然不显示，因为数据有空值，所以结果会出现NAN
# print len(data)#行数
# print data.isnull()#看到空值，是空值的就标出true
# dd=data.dropna()#去掉空值的行，原来的data不变
# print dd.describe()#发现去掉空行后，原始文件并没有变化
#
#
#
# import matplotlib.pyplot as plt #导入图像库
# plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#
# plt.figure(figsize=(5,5)) #建立图像
# p = data.boxplot(return_type='dict')#画箱线图，直接使用DataFrame的方法
# x = p['fliers'][0].get_xdata() # 'flies'即为异常值的标签
# y = p['fliers'][0].get_ydata()
# y.sort() #从小到大排序，该方法直接改变原对象
#
# #用annotate添加注释
# #其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
# #以下参数都是经过调试的，需要具体问题具体调试。
# for i in range(len(x)):
#   if i>0:
#     plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
#   else:
#     plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))
#
# plt.show() #展示箱线图


data = data[(data[u'销量']>400) & (data[u'销量']<5000)]#过滤异常的数据
sta = data.describe()#保存基本的统计量

sta.loc['range'] = sta.loc['max'] - sta.loc['min']
sta.loc['var'] = sta.loc['std'] /sta.loc['mean']#变异系数
sta.loc['dis'] = sta.loc['75%'] - sta.loc['25%']

print(sta)

