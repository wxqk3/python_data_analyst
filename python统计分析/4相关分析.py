#coding:utf8
import pandas as pd
df=pd.read_excel("./corrDataSet.xlsx")
print df.corr()

