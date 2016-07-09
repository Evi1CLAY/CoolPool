# coding=utf-8
# anka9080
# 使用cookielib 库 登录天津科技大学，并查看相关信息

import urllib
import urllib2
import cookielib

# get blank cookie
cookieUrl = 'http://pic.tust.edu.cn/pic/login.do'
cj = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(handler)
resp = opener.open(cookieUrl)

print "第一次响应：",len(resp.read()) 

id = 1211****
pwd = ******

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
values = {'Login.Token1':id,'Login.Token2':pwd}
data = urllib.urlencode(values)

url1 = 'http://pic.tust.edu.cn/pic/login.do'
request = urllib2.Request(url1,data)
response = opener.open(request)
html = response.read()

print "第二次响应：",len(html) 

url2 = 'http://pic.tust.edu.cn/pic/infoSetDataDetailQuery.do?infoSetId=519f93c8-8be4-4097-8344-edb6345a5c36'
#headers = {}
#headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
#headers['Referer'] = 'http://pic.tust.edu.cn/pic/main.do'
request = urllib2.Request(url1,data)
response = opener.open(request)
html = response.read()

print "第三次响应：",len(html) 
print '---------------------------------------------------------'
print html
