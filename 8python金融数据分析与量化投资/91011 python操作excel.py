#coding:utf8

#python的作用  1 处理工具 操控excel实现exel功能
#2 数据处理 数据交换
#3 分析引擎 替代 vba

import xlrd,xlwt
import pandas as pd
import numpy as np
import xlsxwriter
#
path='./data/'
#
# wb=xlwt.Workbook()
#
# wb.add_sheet('first_sheet',cell_overwrite_ok=True)
#
# ws_1=wb.get_sheet(0)
#
# ws_2=wb.add_sheet('second_sheet')
#
# data=np.arange(1,65).reshape(8,8)
#
#
#
# values=np.random.standard_normal(15).cumsum()
# ws_1.write(0,0,100)

# wb.save(path+'workbook2.xls')

#2---------------------------
# import xlrd,xlwt
# import pandas as pd
# import numpy as np
# import xlsxwriter
#
# path='./data/'
#
# wb=xlsxwriter.Workbook()
#
# wb.add_worksheet('first_sheet',cell_overwrite_ok=True)
#
# ws_1=wb.get_sheet(0)
#
#
#
# data=np.arange(1,65).reshape(8,8)
#
#
#
# values=np.random.standard_normal(15).cumsum()
# ws_1.write(0,0,100)
# ws_1.write_colum('a1',values)
# wb.save(path+'workbook2.xls')

#pandas 交互
data=np.random.standard_normal((8,8)).round(5)
df_1=pd.read_excel(path+'workbook2.xls','first_sheet',header=None)

df_2=pd.read_excel(path+'workbook2.xls','second_sheet',header=None)

import string

columns= []

for c in range(8):
    columns.append(string.uppercase[c])


print df_1
df_1.columns=columns
print df_1

df_1.to_excel(path+'newbookwork.xlsx','mysheet')

#xlrd读 dataframe 对象

wbn=xlrd.open_workbook(path+'newbookwork.xlsx')

print wbn.sheet_names()

#python 编写excel脚本：用datanitro 代替vba
