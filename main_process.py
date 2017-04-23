#!/usr/bin/python
# -*- coding: utf-8 -*-

from multi_threads import *

f = file(u'D:/PycharmProjects/amazon_web_spiders/小家电_个护电器.txt','r')
ip_list = []

try:
    all_the_text = f.read()
    x = all_the_text.split('\n')
    url_list = []
    for each_url in x:
        url_list.append(each_url)
    print url_list

    threads = thread(ip_list, url_list)
    all_threads = threads.threads_management_using_Dynamic_IP(1,u'小家电_个护电器items')
    for t in all_threads:
        t.setDaemon(True)
        t.start()

    for t in all_threads:
        t.join()

    print "all over %s" % ctime()


finally:
    f.close()