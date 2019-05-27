#coding:utf8
#1 numpy使用

#1.1 新建

import numpy as np

arr=np.array([[1,2,3],[4,5,6]])


arr2=np.array([[1,2],[3,4],[5,6]])



arr.reshape(3,2)

#数组运算
arr +=2

arange=np.arange(3,7,2)

print arange



#矩阵积

arr3=arr.dot(arr2)


print np.shape(arr3),arr3.shape,'array的形状'




#------------------------------------索引

arr=np.arange(32).reshape(8,4)

arr[[0,3,5],[0,3,2]]



#------------------------------------转 置

arr.T
arr.transpose()

#------------------------------------通用函数

arr.max()
arr.min()
arr.std()
np.sqrt(arr)

#--------------------------------np.where 使用
#替换 缺失值为0

arr=(
    [
        [1,2,np.NAN,4],
        [3,4,5,np.NAN]
    ]
)

np.isnan(arr)

condition=np.isnan(arr)

result=np.where(condition,0,arr)


#-------------------------- np save and load

np.save('save1',result)

result2=np.load('save1.npy')

print result2

np.savetxt('save2.csv', result2,delimiter=',',fmt='%.1f')
#2pandas
#https://blog.csdn.net/zhuzuwei/article/details/80429209