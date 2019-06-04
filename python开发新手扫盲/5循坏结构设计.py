# -*- coding:utf8 -*-
#--------------------------总结
# by william xia, supported by 北风万视频
#第5章熟悉了 for while
# break continue 高性能循环
#------------------------------

#1。
cont='yes'
sum=0
count=0



while cont == 'yes':
    score = input('输入分数')
    count = count + 1
    sum = sum + score
    avg = (sum) / count
    print avg
    cont = input('继续吗？')