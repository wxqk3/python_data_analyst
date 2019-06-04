# -*- coding:utf8 -*-
from lxml import etree
import requests


url = "https://www.appannie.com/apps/ios/app/idle-heroes/reviews/?order_by=date&order_type=desc&date=2019-04-29~2019-05-29&translate_selected=false&granularity=weekly&stack&percent=false&series=rating_star_1,rating_star_2,rating_star_3,rating_star_4,rating_star_5"


with open('htm0.txt', 'r') as myfile:
  html = myfile.read()

#结论1 503not avaliable,反爬虫第一道墙，设置header模拟真机访问
header ={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
response = requests.get(url,headers = header)
htm0 = response.content

# text_file = open("htm0.txt", "w")
#
# text_file.write(htm0)
#
# text_file.close()

#结论 2-------用request爬虫 会被反爬虫 得不到重要数据,需对表格接口单独request才行，或者手动用元素半自动爬虫

# re=response.content
#
#
#
# selector2=etree.HTML(re)
selector=etree.HTML(html)

#contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')

# simple1=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/span[1]/a')
# print simple1
# print simple1

simple2=selector.xpath('//*[@id="4229616386"]/div/div[2]/text()')
print simple2
print simple2

# //*[@id="4229616386"]/div/div[2]/text()
# //*[@id="4230292243"]/div/div[2]
# //*[@id="4230292243"]/div
# //*[@id="4237381132"]/div

# 结论 3--------反爬虫做得太好了，id也是随机数, 自己研究规律，手动解码，找到id即可按顺序爬取所有数据,遍历倒数tr即可

simple3=selector.xpath('//*[@id="sub-container"]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]')

#此处已经找到id,为etree对象，打印出来很像字典，便试试强制转换
print dict(simple3[0].attrib)['id']

#已找到id,完成半自动爬虫

#打印出评价
pingjia_path='//*[@id="'+dict(simple3[0].attrib)['id']+'"]/div/div[2]/text()'
pingjia=selector.xpath(pingjia_path)
print pingjia





#-----------一次爬取多个数据
results=[]
for i in range(1,101):
    id_path='//*[@id="sub-container"]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/table/tbody/tr['+str(i)+']/td[2]'
    id_selector=selector.xpath(id_path)
    pingjia_path = '//*[@id="' + dict(id_selector[0].attrib)['id'] + '"]/div/div[2]/text()'
    pingjia = selector.xpath(pingjia_path)
    results.append(pingjia)

#print results

#----- 处理编码问题
results_utf8=[]
for strr in results:
    #print str(strr)
    results_utf8.append(str(strr).decode('unicode-escape').encode('utf-8'))
    str_utf8= str(strr).decode('unicode-escape').encode('utf-8')
    print str_utf8
#print(results_utf8)

ustring = unicode(str(results[9]), "utf-8")
#print ustring.decode('unicode-escape').encode('utf-8')
import numpy as np
np.savetxt("评价（解码）.text", results, delimiter=",", fmt='%s')
np.savetxt("评价(未解码).csv", results, delimiter=",", fmt='%s')


#注：html文件 可由利用selenium+phantomjs，模拟游览器的方式得到，此文没有应用上，手动复制的网页元素文件