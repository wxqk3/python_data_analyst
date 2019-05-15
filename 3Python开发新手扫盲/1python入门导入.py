# -*- coding:utf8 -*-
# list 类型
a = [10,10,20,30,40]

a.append(50)
a.append(50)
a.extend(a)
index=a.index(30)
print(index)


#元组 （与列表相似，但元素不可变）

b=(1,2,3)

#字典

c={'databse':'blog'}
c.get('databse')

g,k = input('输入两个数，都好，求和')

print(g+k)

#对象的删除
dele=[1,2,3]

del dele[0]

print(dele)