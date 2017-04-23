#!/usr/bin/python
# encoding: utf-8

import urllib2

apiUrl = 'http://api.ip.data5u.com/dynamic/get.html?order=31a3587d5e8fae7e11d991751fdefe55'
try:
    # 获取IP列表
    res = urllib2.urlopen(apiUrl).read().strip("\n");
    # 按照\n分割获取到的IP
    ips = res.split("\n");
    print(ips)
except Exception, e:
    print(e)