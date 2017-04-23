#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from urllib2 import *
from time import ctime,sleep
from regular_exp import *
'''proxies = { "http": "113.121.185.32:20057", "https": "60.17.232.195:35452")
r = requests.get("http://www.amazon.cn", proxies=proxies)
print r.text'''

import urllib2
from random import choice


class http_pxoxy:
    def __init__(self,ip_pool,url_pool,catalog_name):
        self.ip_pool = ip_pool
        self.url_pool = url_pool
        self.catalog_name = catalog_name
        self.ip_counter = 0

    def  using_proxy_ip(self):
        for url in self.url_pool:
            flag = 0
            while(1):
                if (flag == 1):
                    break
                if self.ip_counter == len(self.ip_pool):
                    print 'all proxy ip are failed.'
                    print 'Ended at',url
                    break
                print url
                enable_proxy = True
                proxy_ip = self.ip_pool[self.ip_counter]
                #proxy_ip = choice(self.ip_pool)
                print proxy_ip
                proxy_handler = urllib2.ProxyHandler({"https": proxy_ip})
                null_proxy_handler = urllib2.ProxyHandler({})

                if enable_proxy:
                    opener = urllib2.build_opener(proxy_handler)
                else:
                    opener = urllib2.build_opener(null_proxy_handler)

                urllib2.install_opener(opener)

                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                User_agent = { 'User-Agent' : user_agent }
                req = urllib2.Request(url, None, headers=User_agent)
                Max_Num=6
                for i in range(Max_Num):
                    sleep(0.3)
                    try:
                        r = urllib2.urlopen(req,timeout=3).read() #读入url的页面源代码
                        #print(r)
                        output_filepath = 'D:/PycharmProjects/amazon_web_spiders/items_url/'+self.catalog_name+'.txt'
                        '''f = file(output_filepath,'w')
                        f.write(r)
                        f.close()'''
                        get_items_url(r,output_filepath)
                        flag = 1
                        break
                    except urllib2.HTTPError,e:
                        if i < Max_Num - 1:
                            continue
                        else:
                            print 'The server couldn\'t fulfill the request.'
                            print 'Error code:',e.code
                            self.ip_counter+=1
                    except urllib2.URLError,e:
                        if i < Max_Num - 1:
                            continue
                        else:
                            print 'We failed to open the URL:%s' %(url)
                            print 'Reason:',e.reason
                            self.ip_counter += 1

    def using_proxy_ip_using_Dynamic_IP(self):
        count = 0
        apiUrl = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy?count=1&spiderId=bba1cb6c44b142cb9aa8fde3bb317079&returnType=1'
        for i in range(4):
            try:
                self.ip_counter = 0
                # 获取IP列表
                res = urllib2.urlopen(apiUrl).read().strip("\n");
                # 按照\n分割获取到的IP
                ips = res.split("\n");
                flag = 0
                sleep(10)
                print 'getting ip', count, '\n'
                count += 1
                break

            except Exception, e:
                print u'代理ip不好用了'
                print(e)
        for url in self.url_pool:
            flag = 0
            while (1):
                if (flag == 1):
                    break
                if (self.ip_counter == 5):
                    print 'all proxy ip are failed.'
                    print 'Ended at', url

                    for i in range(4):
                        try:
                            # 获取IP列表
                            self.ip_counter = 0
                            res = urllib2.urlopen(apiUrl).read().strip("\n");
                            # 按照\n分割获取到的IP
                            ips = res.split("\n");
                            flag = 0
                            sleep(10)
                            print 'getting ip', count, '\n'
                            count += 1
                            break;

                        except Exception, e:
                            print u'代理ip不好用了_2'
                            print(e)
                # print url

                enable_proxy = True
                proxy_ip = ips[self.ip_counter]
                # proxy_ip = choice(self.ip_pool)
                # print proxy_ip
                proxy_handler = urllib2.ProxyHandler({"https": proxy_ip})
                null_proxy_handler = urllib2.ProxyHandler({})

                if enable_proxy:
                    opener = urllib2.build_opener(proxy_handler)
                else:
                    opener = urllib2.build_opener(null_proxy_handler)

                urllib2.install_opener(opener)

                user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                User_agent = {'User-Agent': user_agent}
                req = urllib2.Request(url, None, headers=User_agent)
                Max_Num = 6
                for i in range(Max_Num):
                    sleep(0.2)
                    try:
                        r = urllib2.urlopen(req, timeout=3).read()  # 读入url的页面源代码
                        # print(r)
                        output_filepath = 'D:/PycharmProjects/amazon_web_spiders/items_url/' + self.catalog_name + '.txt'
                        '''f = file(output_filepath,'w')
                        f.write(r)
                        f.close()'''
                        get_items_url(r, output_filepath)
                        flag = 1
                        break
                    except urllib2.HTTPError, e:
                        if i < Max_Num - 1:
                            continue
                        else:
                            print 'The server couldn\'t fulfill the request.'
                            print 'Error code:', e.code
                            self.ip_counter += 1
                            #flag = 2
                            break
                    except urllib2.URLError, e:
                        if i < Max_Num - 1:
                            continue
                        else:
                            print 'We failed to open the URL:%s' % (url)
                            print 'Reason:', e.reason
                            self.ip_counter += 1
                            #flag = 2
                            break
                    except Exception, e:
                        if i < Max_Num - 1:
                            continue
                        else:
                            print 'Some Unknown error'
                            print 'Reason:', e
                            self.ip_counter += 1
                            # flag = 2
                            break



if __name__ =='__main__':
    get = http_pxoxy(ip_list,url_list)
    get.using_proxy_ip()

