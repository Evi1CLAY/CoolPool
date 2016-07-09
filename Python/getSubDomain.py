# coding=utf-8
# author:Anka9080
# getSubDomain v0.1
# 根据搜索引擎获得指定网站的二级域名
# 并输出对应的IP + 地理位置

import urllib
import urllib2
import cookielib
import re

#site = 'baidu.com'
print 'Please input the root site like "baidu.com":'
site = raw_input()
siteFormat1 = site
siteFormat1 = siteFormat1.replace('.', '\.')
#print siteFormat1

urlPage = 'http://www.haosou.com/s?src=360sou_newhome&q=site:'+site
req = urllib2.Request(urlPage)
res = urllib2.urlopen(req)
html = res.read().decode('utf-8')
# 获得搜索结果的页面数
pageStr = re.search(ur'找到相关结果约(.*?)个',html)
page = pageStr.group(1)
formatNum = '0123456789'
for c in page:
    if not c in formatNum:
        page = page.replace(c,'')
page = int(page) / 10
print 'Total Page: ' + str(page)

if page > 50:
    page = 50
newItems = []
for p in range(1, page):
    urlDomain = 'http://www.haosou.com/s?src=360sou_newhome&q=site:'+site+'&pn='+str(p)
    req = urllib2.Request(urlDomain)
    res = urllib2.urlopen(req)
    html = res.read().decode('utf-8')
    tmp = 'linkinfo\"\>\<cite\>(.+?\.'+siteFormat1+')';
    pattern = re.compile(tmp)        
    items = re.findall(pattern, html)
    
    
    # 去重操作
    for item in items:
        if item not in newItems:  
            newItems.append(item)

print 'SubDomain Count: '+ str(len(newItems))

for item in newItems: 
   
    # 获得对应 IP 信息
    pattern = re.compile(ur'\>\>\ (.*?)\<\/font[\s|\S]*?本站主数据：(.*?)\<\/li\>')
    urlIP = 'http://www.ip138.com/ips138.asp?ip='+item
    req = urllib2.Request(urlIP)
    res = urllib2.urlopen(req)
    html = res.read().decode('gb2312')    
    result = re.search(pattern,html)
    print item + '    ' + result.group(1) + '    ' + result.group(2)