#!/usr/bin/python
# encoding: utf-8


"""
@author: 大圣
@contact: excelchart@sina.cn
@file: xpathdemo.py
@time: 2015/12/5 0005 下午 8:26
"""

import requests

from lxml import etree



doubanhtml='''
<douban>
<dl>
    <dt>
      <a href="http://book.douban.com/subject/6082808/?from=tag" target="_blank">
        <img src="http://img3.douban.com/lpic/s6384944.jpg" />
      </a>
    </dt>
    <dd>
      <a href="http://book.douban.com/subject/6082808/?from=tag" class="title" target="_blank">百年孤独</a>


      <div class="desc">
        [哥伦比亚] 加西亚·马尔克斯 / 范晔 / 南海出版公司 / 2011-6 / 39.50元
      </div>

        <div class="rating">
          <span class="allstar50"></span>
          <span class="rating_nums">9.2</span>
        </div>
    </dd>
  </dl>






  <dl>
    <dt>
      <a href="http://book.douban.com/subject/26414020/?from=tag" target="_blank">
        <img src="http://img3.douban.com/lpic/s28096601.jpg" />
      </a>
    </dt>
    <dd>
      <a href="http://book.douban.com/subject/26414020/?from=tag" class="title" target="_blank">我不喜欢这世界，我只喜欢你</a>

      <div class="desc">
        乔一 / 湖南少年儿童出版社 / 2015-5-1 / 29.80元
      </div>

        <div class="rating">
          <span class="allstar45"></span>
          <span class="rating_nums">8.4</span>
        </div>
    </dd>
  </dl>
</douban>

'''

doc = etree.fromstring(doubanhtml)
print 1
print 2

for eachbook in doc.xpath('//dl/dd'):
    bookname = eachbook.xpath('a/text()')[0]
    bookurl = eachbook.xpath('a/@href')[0]
    pub = eachbook.xpath('div[@class="desc"]/text()')[0]
    rate = eachbook.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()')[0]
    print bookname,bookurl,pub,rate
