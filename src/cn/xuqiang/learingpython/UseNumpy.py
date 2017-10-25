# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import numpy as np
import pandas as pd
# a = np.array([[1,2,3],[4,5,6]])
# #a = a[:3]
# print(a)
# print(a*a)
# print(np.shape(a))
# print(np.size(a))
# a = np.zeros(10)
# b = np.empty(10)
# c = np.ones_like(a)
# print(a)
# print(b)
# print(c)
# print('==================')
# d = np.eye(5,5)
# print(d)
# print('==================')
#
# e = np.identity(5,dtype=np.float64)
# print(e)



# __author__ = "xdg"
#
# import csv
# import numpy as np
# import os
# import pandas as pd
# from random import shuffle
import time
#
#读取csv文件，得到矩阵
start = time.time()
df=pd.read_excel("E:/file/304/data/simple.xlsx",encoding='UTF-8')
# category = str(df[0:1])
# category = category.decode('unicode-escape')
# users = df['custid']
# userIdentify = users.unique()
# yes = len(userIdentify)
# type = type(userIdentify)
# for i in users:
#     print(i)
data_matrix1=df.as_matrix()
data_matrix=np.array(data_matrix1)
# category = str(data_matrix1[0])
# print  category.decode('unicode-escape')
#print(df)
#获取矩阵第一列（用户名列表）
userlist=data_matrix[:,1]
#获取用户名集合（无重复）
userset=list(set(userlist))
#
print ("用户：")
print (userset)
#分离出每个用户数据，单独存储
print ("开始处理...")
# # #方法1
# # count=1
# # # for row in data_matrix:
# # #     print ("处理第%d行"% count)
# # #     for user in userset:
# # #         if str(row[1])== str(user):
# # #             with open("G:/Git/304first/data/users/"+str(user)+".csv","a") as f:
# # #                 csvwriter=csv.writer(f)
# # #                 csvwriter.writerow(row)
# # #     count+=1
# #方法2
col=['id','custid','大类编码','大类名称','中类编码','中类名称','小类编码','小类名称','销售日期','销售月份','商品编码','规格型号','商品类型','单位','销售数量'	,'销售金额'	,'商品单价','是否促销']
userNum=1  #用户个数
total_dataNum=0 #所有记录数
for user in userset:
    print ("第%d个用户"%userNum)
    user_mat=[]
    # user_mat.append(category)
    data_count=0#每个用户消费记录条数
    for row in data_matrix:
        if str(row[1])== str(user):
            user_mat.append(row)
            data_count+=1
    toDf = (pd.DataFrame(user_mat,columns=col))
    toDf.to_csv("E:/file/304/data/user/"+str(user)+".csv",encoding="UTF-8")
    print ("此用户有%d条消费记录"%data_count)
    total_dataNum+=data_count
    userNum+=1

print ("\n表中共有%d条数据"%total_dataNum)
print ("共有%d个用户"%len(userset))
print ("处理完毕！")
end = time.time()
print(end-start)

# print(data)
# print('=====================')
#
# data1 = np.random.rand(7,4)
# print(data1)

# data = np.random.randn(7)
# otherdata = np.random.randn(7)
# names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
# othernames = np.array(['Apple','Goe','Will','Bob','Will','Joe','Joe'])
# # print(data[names == 'Bob'])
# # print(data[names == 'Bob',2:])
# print(np.maximum(data,otherdata))

'''

'''
# arr = np.random.randn(5,4)
# sizex = arr.shape[0]
# sizey = arr.shape[1]
# for i in range(sizey):
#     sum = 0;
#     mean = 0;
#     for j in range(sizex):
#         sum += arr[j,i]
#     mean = sum / (sizey)
#     print('第%d列的均值为%.5f，总和为%.5f'%(i,mean,sum))
#
# arrmean = arr.mean(axis=0)
# arrmean1 = arr.mean(axis=1)
# arrsum = arr.sum(axis=0)
# arrsum1 = arr.sum(axis=1)
# print(arrmean)
# print(arrmean1)
# print(arrsum)
# print(arrsum1)


'''
数组A中是否包含数组B中的元素
如果包含，输出A中对应位置数组
如果不包含，输出空
'''
# A = np.array([6,8,5,3,1,4,2,3,0,2,5,6])
# B = np.array([1])
# contain = np.in1d(A,B)
# index = []
# for i in range(len(contain)):
#     if contain[i] == True:
#         index.append(i)
#         ++i
#     else:
#         ++i
# if(len(index) == 0):
#     print('A do not have B element')
# else:
#   print(index)

'''
使用np.save()和np.load()进行数据的存储和读取
'''
# import os
# arrA = np.random.randn(5,4)
# arrB = np.random.randn(6,6)
# path = 'E:/file/python/data/'
# pathexit = os.path.exists(path)
# if pathexit:
#     np.savez(path+'arrAB', a=arrA,b=arrB)
# else:
#      os.mkdir(path)
#      np.save(pathexit, arrA)
#
# loadAB = np.load(path+'arrAB.npz')
# print(loadAB['a'])

'''
文本的存取操作
np.loadtxt() np.genfromtxt()
np.savetxt() 
'''
# path = 'E:/file/python/data/'
# arr = np.loadtxt(path+'arr1.txt',delimiter=',')
# print(arr)
#
# arr2 = np.random.rand(5,4)
# np.savetxt(path+'arr2.txt',arr2,delimiter=' ')



















