#coding:utf8

#数据工具1------------------------------基本画图
import numpy as np

import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)+0.5*x

x=np.linspace(-2*np.pi,2*np.pi,50)

# plt.plot(x,f(x),'b')
# plt.grid(True)

#---------线性回归
reg=np.polyfit(x,f(x),deg=5)
ry=np.polyval(reg,x)

plt.plot(x,ry,'b',label='reg')
plt.plot(x,f(x),'r.',label='fx')
plt.grid(True)
plt.show()



