# -*- coding:utf8 -*-
#--------------------------总结
# by william xia, supported by 北风万视频
#第4章熟悉了 选择结构
#------------------------------
x=2
if x >2:
    print("dayu 2")
else:
    print('budayu 2')


#实战

people=input('请输入人数\n')
zhan=input("请输入站数\n")

if (zhan >= 1 and zhan <=4):
    print 'price',people*3
elif people>=5 and people <=9:
    print 'price',people*4
else:
    print 'price',people*5
