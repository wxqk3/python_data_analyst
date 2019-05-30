
# -*- coding:utf8 -*-
#1 request 的使用
#
# import requests
#
# response = requests.get('https://www.appannie.com/apps/ios/app/idle-heroes/reviews/?order_by=date&order_type=desc&date=2019-04-29~2019-05-29&translate_selected=false&granularity=weekly&stack&percent=false&series=rating_star_1,rating_star_2,rating_star_3,rating_star_4,rating_star_5&country=CN')
# print response.text


# import requests
# header ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}
# response = requests.get('https://www.appannie.com/apps/ios/app/idle-heroes/reviews/?order_by=date&order_type=desc&date=2019-04-29~2019-05-29&translate_selected=false&granularity=weekly&stack&percent=false&series=rating_star_1,rating_star_2,rating_star_3,rating_star_4,rating_star_5&country=CN')
# #print response.text
#
# print response.content.decode('gbk')



#  自己写的简单爬虫

#
# import requests
# from lxml import etree
#
# url = "https://www.douban.com"
#
# header ={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
#
#
# response = requests.get(url,headers = header)
# #print response.text
# html=response.content
# selector=etree.HTML(html)
#
# #contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')
#
# simple=selector.xpath('//*[@id="anony-time"]/div/div[3]/ul/li[1]/a[2]')
# print simple[0].text



# 此爬虫用于google play，被反爬虫了，手动爬虫

import requests
from lxml import etree

url = "https://play.google.com/store/apps/details?id=com.droidhang.ad"

header ={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}


response = requests.get(url,headers = header)
#print response.text
html=response.content
selector=etree.HTML(html)

#contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')

simple1=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/span[1]/a')
print simple1
print simple1[0].attrib

# simple2=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[3]/div/div[1]/meta')
# print simple2
# print simple2