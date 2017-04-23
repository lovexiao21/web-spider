#!/usr/bin/python
# encoding: utf-8

output = 'D:/PycharmProjects/amazon_web_spiders/'+u'小家电_个护电器.txt'
f = file(output,'a')

for i in range(1,73):
     x = 'https://www.amazon.cn/s/ref=sr_pg_'+str(i)+\
         '?fst=as%3Aoff&rh=n%3A1841388071%2Cn%3A2016126051%2Cn%3A%212016127051%2Cn%3A814224051%2Cn%3A814228051&page='\
        +str(i)+'&bbn=1841388071&ie=UTF8&qid=1492968717'
     f.write(x)
     f.write('\n')

f.close()

