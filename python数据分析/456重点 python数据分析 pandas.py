#coding:utf8
#1 pandas : series一维数组

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



series=pd.Series([1,2,3],index=['will','lucy','xia'])


#考点1 缺失值检测，替换 https://blog.csdn.net/sinat_29957455/article/details/79017363

series.isnull()



#2  http://python.jobbole.com/84416/

#cratea a new obj  with numpy--------

s=pd.Series([1,3,5,np.nan,6,8])

dates=pd.date_range('20130101',periods=6)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

# print df

#cratea a new obj  with dict------

df2=pd.DataFrame({
    'A':1,
    'B':pd.Series(1,index=list(range(4))),
    'C':pd.Timestamp('20100101'),
    'D':np.array([3]*4)
})

# print df2


#数据透视表
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})

pd.pivot_table(df, values='D', index=['A','B'],columns=['C'])


ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
ts = ts.cumsum()
ts.plot()

plt.show()