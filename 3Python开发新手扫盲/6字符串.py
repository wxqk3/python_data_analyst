# -*- coding:utf8 -*-
#--------------------------总结
# by william xia, supported by 北风万视频
#第6章熟悉了
# break continue 高性能循环
#------------------------------

#1。
import string

a=3.667
'%7.3f'%a

#2.字符串截取和切片
#split join等


#映射表 和 使用映射
table=string.maketrans('abc','rst')

s='python===abc'

s2=s.translate(table,'=')

print 'success'+s2

#
#----------------------
s=raw_input('输入字符串')
li=s.split(',')

sum=0
for num in li:
    sum=sum+float(num)
print sum