#coding:utf8

#python的作用  1 处理工具 操控excel实现exel功能
#2 数据处理 数据交换
#3 分析引擎 替代 vba

import xlrd,xlwt
import pandas as pd
import numpy as np
import xlsxwriter

path='./data/'

wb=xlwt.Workbook()