#-coding:utf8-
#https://www.zhihu.com/question/25949022


# 检验正态分布等，ks h0 假设为正态分布
import numpy as np
from scipy.stats import kstest
x = np.linspace(-15, 15, 3)
print kstest(x, 'norm')

#最终返回的结果，第二个值 p-value=0.76584491300591395，比指定的显著水平（假设为5%）大，则我们不能拒绝假设：x服从正态分布。
#p<0.05 则可以拒绝

# 疑问？第一个d值怎么看，什么用


