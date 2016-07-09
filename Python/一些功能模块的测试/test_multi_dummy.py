# coding: utf-8
# from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time
import urllib2

urls = [
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/',
    'http://mysweet.gift/'
]

start = time.time()
results = map(urllib2.urlopen, urls)
print 'Normal:', time.time() - start

start2 = time.time()
# 开8个 worker，没有参数时默认是 cpu 的核心数
pool = ThreadPool(processes=8)
# 在线程中执行 urllib2.urlopen(url) 并返回执行结果
results2 = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start2