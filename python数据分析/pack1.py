#coding:utf8

#第一章 1-4----------------
#1 多行注释用三引号

#2 区分大小写

a=u'{0}年{1}月{2}日'.format('2017',3,24)

print a

b=format(1000000,'e')
'''科学计数法'''

'''格式化输出'''
print('%s %s' % ('hello world','hello'))



#第一章 5-8---------------- list,tuple,dict,序列及分片，set  https://blog.csdn.net/business122/article/details/7541486

dict={1:1,2:2}
dict2={'1':1,2:2}
#潜复制 不影响值
#dict3=dict 则指向同一对象

def fun_a(x,y):
    return x+y