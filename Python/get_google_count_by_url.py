# coding:utf-8
__author__ = 'Administrator'
import urllib2,urllib
import simplejson
import socket
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re

# 功能：给定关键词，输出这个关键词在google搜索的搜索条目
class GoogleResult():
    product_cnvd = []
    product_cnvd_google = []
    product_cnvd_google4 = []

    # 从文件夹中读入需要搜索的关键词
    def __init__(self):
        with open('22.txt') as pct:
            for line in pct:
                # 以防读入空行
                if line.strip() != '':
                    self.product_cnvd.append(line.strip())
        pct.close()

    def google_test(self):

        pcgt = open('22_ok_test.txt','w')
        print '[+ info ] start ....'
        for pc in self.product_cnvd:
            p = pc.split(',')[0]

            try:
                browser = webdriver.Firefox() # Get local session of firefox
                browser.get("https://www.google.co.jp/?gfe_rd=cr&ei=gdjQVc2CM8_98wfTsazAAQ#q=%s" %p)
                time.sleep(6) # Let the page load
                element = browser.find_element_by_xpath("//div[contains(@id,'resultStats')]") # get element on page
                result = element.text
                count = re.compile('[\d\,]{1,20}').search(result).group().replace(',','')

            except:
                count = 'Null'
                #assert 0, "can't find resultStats"  #  assert  什么鬼  报错直接GG?
            finally:
                all = pc  + str(count)
                self.product_cnvd_google.append(all)
                pcgt.write(all + '\n')
                print all
                browser.quit()


        pcgt.close()

    # 把product_cnvd_google写入文件
    def save_file(self):
        with open('22_ok.txt','w') as pcgt:
            for line in self.product_cnvd_google:
                #print line
                pcgt.write(line + '\n')
        pcgt.close()

        # with open('x.txt','w') as x:
        #     x.write(json)
    def google_test_2(self):

        pcgt = open('last_product_cnvd_zoomeye_google3.txt','w+')
        print '[+ info ] start ....'
        for pc in self.product_cnvd_google:
            p = pc.split(',')[0]
            mark = pc.split(',')[3]
            if mark != 'Null':
                self.product_cnvd_google4.append(pc)
            else:
                try:
                    browser = webdriver.Firefox() # Get local session of firefox
                    browser.get("https://www.google.co.jp/?gfe_rd=cr&ei=gdjQVc2CM8_98wfTsazAAQ#q=%s" %p)
                    time.sleep(10) # Let the page load
                    element = browser.find_element_by_xpath("//div[contains(@id,'resultStats')]") # get element on page
                    result = element.text
                    count = re.compile('[\d\,]{1,20}').search(result).group().replace(',','')

                except:
                    count = 'Null'
                    #assert 0, "can't find resultStats"  #  assert  什么鬼  报错直接GG?
                finally:
                    all = pc.strip('Null')  + str(count)
                    self.product_cnvd_google4.append(all)
                    pcgt.write(all + '\n')
                    print all
                    browser.quit()
        pcgt.close()

    def save_file2(self):
        with open('last_product_cnvd_google4.txt','w+') as pcgt:
            for line in self.product_cnvd_google4:
                #print line
                pcgt.write(line + '\n')
        pcgt.close()

        # with open('x.txt','w') as x:
        #     x.write(json)

if __name__ == '__main__':
    socket.setdefaulttimeout(15)
    gr = GoogleResult()
    print '11' * 10
    gr.google_test()
    print '22' * 10
    gr.save_file()
    print '33' * 10
    # gr.google_test_2()
    # print '44' * 10
    # gr.save_file2()