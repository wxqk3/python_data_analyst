import requests
from lxml import etree

url = "https://www.appannie.com/apps/ios/app/idle-heroes/reviews/?order_by=date&order_type=desc&date=2019-04-29~2019-05-29&translate_selected=false&granularity=weekly&stack&percent=false&series=rating_star_1,rating_star_2,rating_star_3,rating_star_4,rating_star_5"

header ={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}


response = requests.get(url,headers = header)
#print response.text
html=response.content

print html

selector=etree.HTML(html)

#contents=selector.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[5]/div/div[2]/div[2]')

simple1=selector.xpath('//*[@id="4229616386"]/div/div[2]/text()')
print simple1