#!/usr/bin/python
# encoding: UTF-8

import urllib2
from regular_exp import *

url = 'https://www.amazon.cn/%E5%8C%96%E5%A6%86/dp/B01859QHJU/ref=sr_1_4?s=amazon-global-store&ie=UTF8&qid=1492968966&sr=1-4'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
User_agent = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers=User_agent)
for i in range(1):

    #response = urllib2.urlopen(request,timeout=3)
    #page = response.read()

    #f = file('D:/PycharmProjects/amazon_web_spiders/test/test1', 'w')
    #f.write(page)

    f = file('D:/PycharmProjects/amazon_web_spiders/test/test1', 'r')
    page = f.read()
    f.close()

    get_items_details(page)
    break

