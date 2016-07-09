# coding: utf-8
# anka9080
# BaiduSpider v0.1

"""
    提供关键词（Dork） 和 需要爬行的页数
    输入搜索结果中的 URL到文件中
"""

import requests
import re
import time
from multiprocessing.dummy import Pool as ThreadPool

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept':'*/*'
}
class BaiduSpider():
    """
        get urls from baidu
    """
    def __init__(self,dork,num):
        self.urls = []
        self.num = num
        self.base_url = 'https://www.baidu.com/s?rsv_srlang=en&wd='
        self.url = self.base_url + dork

        self.spider()
        # self.get_true_url()
        # pass

    def get_page(self):
        html = requests.get(self.url,headers = HEADERS).text
        num_str = re.search(ur'找到相关结果约(.*?)个',html)
        tmp = num_str.group(1)
        num = int(tmp.replace(',',''))
        return num

    def spider(self):
        real_num = self.get_page()
        if self.num * 10 > real_num:
            self.num = real_num
        for x in xrange(0,self.num * 10,10):
            # time.sleep(2)
            url = self.url + '&pn=' + str(x)
            print '> URL: ',url
            html = requests.get(url,headers = HEADERS,timeout = 2).text
            pattern = re.compile(r'class="c-showurl".*?url":"(http://www.baidu.com/link\?url=[\w-]*)"')
            res = re.findall(pattern,html)
            if res:
                print res
                self.urls.extend(res)
            # print len(self.urls)

def get_real_url(old_url):
    try:
        r = requests.get(old_url,headers = HEADERS,timeout = 3)
    except Exception,e:
        return ''
    else:
        # print old_url,' vs  ',r.url
        return r.url

def list2file(list,fn):
    with open(fn,'w') as output:
        for line in list:
            output.write(line + '\n')

    print '[*] all urls saved to file!'

if __name__ == '__main__':

    bs = BaiduSpider('inurl:? inurl:.sg',100)
    tp = ThreadPool(10)
    real_urls = tp.map(get_real_url,bs.urls)
    real_urls = list(set(real_urls))
    list2file(real_urls,'res_sg_100.txt')