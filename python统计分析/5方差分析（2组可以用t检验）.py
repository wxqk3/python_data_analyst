#coding:utf8
#https://jingyan.baidu.com/article/cdddd41c6a2f2553cb00e13b.html
#http://blog.sciencenet.cn/blog-2577109-1143281.html
#数据描述
#
# 有A,B, C,D,E五个品种，共有4个重复的产量数据。
#
# Variety 品种
#
# rep 重复（此处没用上）
#
# y 产量
import pandas as pd
from scipy.stats import f_oneway
df=pd.read_csv("./f_data.csv")
d1=df[df['Variety']=='A']['y']
d2=df[df['Variety']=='B']['y']
args=[d1,d2]
print f_oneway(*args)

#p<0.05 拒绝