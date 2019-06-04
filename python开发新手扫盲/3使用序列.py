# -*- coding:utf8 -*-
#--------------------------总结
# by william xia, supported by 北风万视频
#第三章熟悉了 三个东西  ：序列 元祖 和 字典
#------------------------------
data=[]
for int in range(5):
    x=input("input")
    data=data+[x]

# 错误实例  sort没有返回值result=data.sort()
data.sort()
print (data)

#4序列，列表 list基础知识
data2=[1,2,3,43]
data3=data2[0:2] #切片用中括号，左边包含，右边不包含


#字典

a_dict={'a':45,'b':'will','c':66}

for key in a_dict.keys():
    print(a_dict[key])



