#!/usr/bin/python
# encoding: utf-8

import re
number_of_items = 24

def jugg_chinese(text):
    chinese = re.compile(ur'[ \u4e00-\u9fa5]+')
    if re.search(chinese, text.decode('utf-8')) != None:
        return text
    else:
        return ""

def get_items_url(all_the_text,save_file_path):
    pattern1 = re.compile(r'(?<=li id="result).+?(?=</li>)', re.M | re.I | re.S)
    result = re.findall(pattern1, all_the_text)
    #print(len(result))
    # print(result[0])

    pattern2 = re.compile(r'(?<=<a class="a-link-normal a-text-normal" target="_blank" href=")[^"]+(?=")', re.M | re.I)
    f = file(save_file_path, 'a')

    for i in range(0, number_of_items):
        link1 = re.findall(pattern2, result[i])
        #print(i, len(link1), link1)
        f.write(result[i][0:5])
        f.write('  :')
        f.write(link1[0])
        f.write('\n')

    f.close()

def catalog_page_url(all_the_text,save_file_path):
    pattern4 = re.compile(r'(?<=<li>).+?(?=</li>)', re.M | re.I | re.S)
    link4 = re.findall(pattern4, all_the_text)
    print('link4:', len(link4))

    pattern3 = re.compile(r'(?<=href=")[^"]+?">.+?<span class="boldRefinementLink">.*?(?=</span><span)',
                          re.M | re.I | re.S)
    f_w = file(save_file_path,'a')
    for j in range(0, len(link4)):
        link2 = re.findall(pattern3, link4[j])
        print('link2:', len(link2))
        # --------------------------------------------------------------------------------------------------------------

        # ----------------------------针对列表页面，获取下一页URL---------------------------------------------------------
        # patter4 = re.compile()
        # --------------------------------------------------------------------------------------------------------------

        link2 = ['https://www.amazon.cn' + line.replace('&amp;', '&') + '\n' for line in link2]
        f_w.writelines(link2)
    f_w.close()

def next_page_url(all_the_text,save_file_path):
    pattern5 = re.compile(r'(?<=id="pagnNextLink").*?">.*?(?=pagnNextString)', re.M | re.I|re.S)
    pattern6 = re.compile(r'(?<=href=")[^"]*(?=">)')
    f = file(save_file_path, 'a')

    link_next_page_big_range = re.findall(pattern5, all_the_text)
    #print len(link_next_page_big_range)
    if not link_next_page_big_range:
        return 0
    link_next_page = re.findall(pattern6,link_next_page_big_range[0])
    link_next_page = ['https://www.amazon.cn' + line.replace('&amp;', '&') + '\n' for line in link_next_page]
    f.writelines(link_next_page)
    f.write('\n')

    f.close()

    if not link_next_page:
        return  0

    return link_next_page[0]

def get_items_details(page):
    #----------------商品描述-------------------------------------
    patters_productDescription = re.compile(r'(?<=<div id="productDescription").*?(?=</div>)', re.M | re.I | re.S)
    result = re.findall(patters_productDescription, page)  # list
    # print result
    patters_find_p = re.compile(r'(?<=<p>).*?(?=</p>)', re.M | re.I | re.S)
    result_productDescription = re.findall(patters_find_p, result[0])
    productDescription = result_productDescription[0].replace('\n', '').replace('\t', '')  # string
    '''test2 = '我是utf8编码'
    fortest = u'我是一个学生。'''
    '''print fortest
    print test2
    print test2.decode('utf-8')
    print productDescription.decode('utf-8')'''
    productDescription = jugg_chinese(productDescription) #判断 商品描述是否为中文
    # -------------------基本信息-----------------------------------------------------------------------------
    patters_basicInformation = re.compile(r'(?<=基本信息).*?(?=用户评分)', re.M | re.I | re.S)
    result2 = re.findall(patters_basicInformation, page)  # list
    # print result2
    patters_find_li = re.compile(r'(?<=<li>).*?(?=</li>)', re.M | re.I | re.S)
    list_basicInfomation = re.findall(patters_find_li, result2[0])  # list
    patters_find_asin = re.compile(r'(?<=ASIN).+',re.M | re.I)
    for i in range(len(list_basicInfomation)):
        list_basicInfomation[i]=list_basicInfomation[i].replace('<b>', '').replace('</b>', '').replace('\n', ' ')
        a = re.search(patters_find_asin, list_basicInfomation[i])
        if a:
            patters_find_asin_2 = re.compile(r'[a-zA-Z0-9]+')
            asin = re.findall(patters_find_asin_2,a.group(0))[0]
            print 'asin:',asin


    # --------------------------生产商提供信息-----------------------------------------------------------------------
    patters_producer_provide_1 = re.compile(r'(?<=生产商提供信息).*?(?=商品描述)', re.M | re.I | re.S)
    patters_producer_provide_2 = re.compile(r'(?<=生产商提供信息).*?(?=基本信息)', re.M | re.I | re.S)
    result3 = re.findall(patters_producer_provide_1, page)
    result4 = re.findall(patters_producer_provide_2, page)
    if (len(result3) == 0 and len(result4) == 0):
        print 'no producer_provided information'
    elif (len(result3) == 0 and len(result4) != 0):
        print '2'
        result_producer_provide = result4[0]
    elif (len(result4) == 0 and len(result3) != 0):
        print '3'
        result_producer_provide = result3[0]
    else:
        if (len(result3) > len(result4)):
            print '4'
            result_producer_provide = result4[0]
        else:
            print '5'
            result_producer_provide = result3[0]  # string
    patters_find_h = re.compile(r'(?<=<h).*?(?=</h)', re.M | re.I | re.S)
    list_producer_provide_h = re.findall(patters_find_h, result_producer_provide)
    list_producer_provide_p = re.findall(patters_find_p, result_producer_provide)
    list_producer_provide_li = re.findall(patters_find_li, result_producer_provide)
    for i in range(len(list_producer_provide_h)):
        list_producer_provide_h[i] = jugg_chinese(list_producer_provide_h[i])
    for i in range(len(list_producer_provide_p)):
        list_producer_provide_p[i] = jugg_chinese(list_producer_provide_p[i])
    for i in range(len(list_producer_provide_li)):
        list_producer_provide_li[i] = jugg_chinese(list_producer_provide_li[i])

    #-----------------------------------特征信息-----------------------------------------------------
    patters_feature_bullets = re.compile(r'(?<=<div id="feature-bullets").*?(?=</div>)', re.M | re.I | re.S)
    result_feature_bullets = re.findall(patters_feature_bullets, page)
    # print result_feature_bullets
    patters_for_feature_bulletes = re.compile(r'(?<=<span class="a-list-item">).*?(?=</span>)',re.M | re.I | re.S)
    list_feature_bullets = re.findall(patters_for_feature_bulletes, result_feature_bullets[0])
    for i in range(len(list_feature_bullets)):
        list_feature_bullets[i] = jugg_chinese(list_feature_bullets[i])
    save_file_path = 'D:/PycharmProjects/amazon_web_spiders/item_details/'+asin+'_c.txt'
    f = file(save_file_path, 'w')
    f.write("基本信息：")
    f.write('\n')
    for i in range(len(list_basicInfomation)):
        f.writelines(list_basicInfomation[i])
        f.write('\n')

    f.write('\n\n')

    f.write("商品描述：")
    f.write('\n')
    f.write(productDescription)
    f.write('\n\n')

    f.write("特征信息：")
    f.write('\n')
    for i in range(len(list_feature_bullets)):
        f.writelines(list_feature_bullets[i])
    f.write('\n\n')

    f.write("生产商提供信息：")
    f.write('\n')
    f.write('内容h\n')
    for i in range(len(list_producer_provide_h)):
        f.writelines(list_producer_provide_h[i])
    f.write('内容p\n')
    for i in range(len(list_producer_provide_p)):
        f.writelines(str(i))
        f.writelines(list_producer_provide_p[i])
    f.write('内容li\n')
    for i in range(len(list_producer_provide_li)):
        f.writelines(list_producer_provide_li[i])
    f.write('\n\n')

    f.close()
