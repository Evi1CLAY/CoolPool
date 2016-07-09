# coding:utf-8
# anka9080
# SinaSpider v0.1
# 爬行www.sina.com.cn的网站收集其域名下的 URL
# 爬行深度 2
# 可以指定收集URL的文件类型

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

FILTER_TYPE = ['.svg','.jpg','.css','.js']

class Site():
    def __init__(self,domain):
        self.urls = []
        self.pattern = re.compile(r'href="(http://www.sina.com.cn.*?)"')
        self.domain = domain
        self.spider(self.domain,0)
        self.spider_urls(1)

    def spider(self,url,deep):
        r = requests.get(url,headers = HEADERS,timeout = 3)
        html = r.text
        # print html
        res = re.findall(self.pattern,html)
        for u in res:
            u_type = self.get_type(u)
            if u_type:
                if u_type not in FILTER_TYPE:
                    self.urls.append((u,deep + 1))
                    print u
            else:
                # add directly
                self.urls.append((u,deep + 1))

    def get_type(self,url):
        if '.' in url:
            mark = url.rfind('.')
            return url[mark:]
        else:
            return None

    def spider_urls(self,deep):
        count = 1
        for (u,d) in self.urls:
            if d == deep:
                time.sleep(1)
                print '[*] count: ', count
                count += 1
                self.spider(u,deep)


if __name__ == '__main__':
    s = Site('http://www.sina.com.cn')