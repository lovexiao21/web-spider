#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
from time import ctime,sleep
from http_proxy import  *



class thread:

    def __init__(self,ip_list,url_list):
        self.ip_list = ip_list
        self.url_list = url_list

    def one_thread(self,a,b,catalog_name):
        number_of_ip = len(self.ip_list)
        number_of_url = len(self.url_list)
        c = int(number_of_ip*a/b)
        d = int(number_of_ip*(a+1)/b)
        e = int(number_of_url*a/b)
        f = int(number_of_url*(a+1)/b)
        #print type(c)
        path_name = catalog_name+str(a)
        get = http_pxoxy(self.ip_list[c:d], self.url_list[e:f],path_name)
        get.using_proxy_ip()
        #print c,d,e,f,'\n'
        sleep(1)

    def one_thread_using_Dynamic_IP(self,a,b,catalog_name):  #a为线程序号，b为线程数
        number_of_url = len(self.url_list)
        e = int(number_of_url * a / b)
        f = int(number_of_url * (a + 1) / b)
        # print type(c)
        path_name = catalog_name + str(a+1)
        get = http_pxoxy(self, url_pool=self.url_list[e:f], catalog_name=path_name)
        get.using_proxy_ip_using_Dynamic_IP()
        # print c,d,e,f,'\n'
        sleep(1)

    def threads_management_using_Dynamic_IP(self,b,catalog):
        threads = []
        for i in range(b):
            sleep(1)
            t1 = threading.Thread(target=self.one_thread_using_Dynamic_IP, args=(i, b, catalog))
            threads.append(t1)
        return threads

    def threads_management(self, b, catalog):
        threads = []
        for i in range(b):
            t1 = threading.Thread(target=self.one_thread, args=(i, b, catalog))
            threads.append(t1)
        return threads


'''if __name__ == '__main__':
    threads = thread(ip_list,url_list)
    all_threads = threads.threads_management(2)
    for t in all_threads:
        t.setDaemon(True)
        t.start()

    for t in all_threads:
        t.join()

    print "all over %s" %ctime()'''