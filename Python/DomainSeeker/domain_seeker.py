#!/usr/bin/env python
# encoding:utf-8
# author: Anka9080
# email: funsociety.bat@gmail.com

import re
import sys
import Queue
import logging
import threading
import requests
import argparse


import dns.resolver
import dns.rdatatype


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logging.getLogger("requests").setLevel(logging.WARN)

# 域名服务器
NAMESERVERS = [
    '114.114.114.114',
    '119.29.29.29',
    '223.5.5.5',
    '8.8.8.8',
    '182.254.116.116',
    '223.6.6.6',
    '8.8.4.4',
    '180.76.76.76',
    '216.146.35.35',
    '123.125.81.6',
    '218.30.118.6',
]

class FileUtils(object):
    @staticmethod
    def getLines(filename):
        with open(filename) as fn:
            for line in fn.readlines():
                yield line.strip()

# 域名基类(提供解析相关的功能函数)
class Domain(object):

    def __init__(self,nameservers=[],timeout=''):
        self.resolver = dns.resolver.Resolver()
        if nameservers: self.resolver.nameservers = nameservers
        if timeout: self.resolver.timeout = timeout
        

    # 获取泛解析的IP列表
    def extensive(self,target):
        test_domains = ['Anka9080_{0}.{1}'.format(i,target) for i in range(3)]
        # print '-- test_domains:',test_domains
        e_ips = []
        for domain in test_domains:
            record = self.query(domain,'A')
            if record is not None:
                e_ips.extend(record['A'])
        return e_ips

    # 解析域名
    def query(self,target,rdtype):
        try:
            answer = self.resolver.query(target, rdtype)
            return self.parser(answer)
        except dns.resolver.NoAnswer:
            return None # catch the except, nothing to do
        except dns.resolver.NXDOMAIN:
            return None # catch the except, nothing to do
        except dns.resolver.Timeout:
            # timeout retry
            print(target, rdtype, '<timeout>')
        except Exception, e:
            raise e
            logging.info(str(e))
            
            
    def parser(self, answer):
        """result relationship only two format 
        @domain     domain name
        @address    ip address
        """
        result = {}
        for rrsets in answer.response.answer:
            for item in rrsets.items:
                rdtype = self.get_type_name(item.rdtype)

                if item.rdtype == self.get_type_id('A'):
                    if result.has_key(rdtype):
                        result[rdtype].append(item.address)
                    else:
                        result[rdtype] = [item.address]
        return result

    def is_domain(self, domain):
        domain_regex = re.compile(
            r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', 
            re.IGNORECASE)
        return True if domain_regex.match(domain) else False

    def get_type_name(self, typeid):
        return dns.rdatatype.to_text(typeid)

    def get_type_id(self, name):
        return dns.rdatatype.from_text(name)

# 域名枚举类(域名解析的入口)
class DomainFuzzer(object):

    def __init__(self,target,dict_file='top200_domain.txt'):
        self.target = target
        self.dict = list(set(FileUtils.getLines(dict_file)))
        self.resolver = Domain(NAMESERVERS,timeout=5)

    # 多线程枚举 入口
    def run(self,thread_cnt=16):
        # 所有子域名队列,check后存在的域名和IP字典
        all_queue,ok_queue = Queue.Queue(),Queue.Queue()
        for line in self.dict:
            all_queue.put('.'.join([str(line),str(self.target)]))
        
        e_ips,threads = self.resolver.extensive(self.target),[]
        # print '-- extensive',e_ips

        for i in xrange(thread_cnt):
            threads.append(self.bruteWorker(self.resolver,all_queue,ok_queue,e_ips))
        
        for t in threads: t.start()
        for t in threads: t.join()

        while not ok_queue.empty():
            yield ok_queue.get()

    # 单线程枚举入口
    class bruteWorker(threading.Thread):

        def __init__(self,resolver,all_queue,ok_queue,extensive=[]):
            threading.Thread.__init__(self)
            self.all_queue = all_queue
            self.resolver = resolver
            self.ok_queue = ok_queue
            self.extensive = extensive

        def run(self):
            try:
                while not self.all_queue.empty():
                    sub = self.all_queue.get_nowait()
                    # print '-- sub: ',sub

                    record = self.resolver.query(sub,'A')
                    if record:
                        ips = record['A']
                        for ip in ips:
                            if ip not in self.extensive:
                                self.ok_queue.put(sub)
                                break
                return self.ok_queue
            except Exception,e:
                pass

# 好搜搜索引擎接口
class HaosouAPI(object):

    api = 'http://www.haosou.com/s?src=360sou_newhome&q=site:'
    # 好搜搜索引擎的入口
    def __init__(self,target):
        self.target = target
        self.ptn = self.get_ptn()


    def get_ptn(self):
        tmp = self.target.replace('.','\.')
        return re.compile('linkinfo\"\>\<cite\>(.+?\.'+tmp+')')

    def run(self,page_cnt=50):
        subs = []
        for x in xrange(1,page_cnt):
            url = self.api+self.target+'&pn='+str(x)
            try:
                rsp = requests.get(url)
            except Exception,e:
                logging.info(str(e))
                continue
            html = rsp.text
            items = re.findall(self.ptn,html)
            for i in items:
                subs.append(i)
        return set(subs)

# i.links.cn 子域名查询接口
class ILinksAPI(object):

    api = 'http://i.links.cn/subdomain/'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded", 
        "Referer": "http://i.links.cn/subdomain/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
    }

    def __init__(self,target):
        self.target = target
        self.ptn = self.get_ptn()

    def get_ptn(self):
        tmp = self.target.replace('.','\.')
        return re.compile('https?://([\w\-\.]*?'+tmp+')')

    def run(self):
        subs = set()
        data = {
            'domain':self.target,
            'b2':1,
            "b3":1,
            "b4":1
        }
        try:
            rsp = requests.post(self.api,headers=self.headers,data=data)
        except Exception,e:
            logging.info(str(e))
            return subs
        html = rsp.text
        items = re.findall(self.ptn,html)
        for i in items:
            subs.add(i)
        return subs
            

def run(args):
    domain = args.domain
    thread_cnt = int(args.thread)
    if not domain:
        print('usage: domain_seeker.py -d aliyun.com -a')
        sys.exit(1)

    res_subs = set()

    # 使用 API
    if args.api:
        iapi = ILinksAPI(domain)
        subs = iapi.run()
        logging.info('API Module success with '+str(len(subs)))
        res_subs = res_subs.union(subs)  

    # 使用搜索引擎
    if args.search:
        ha = HaosouAPI(domain)
        subs = ha.run()
        logging.info('Search Engine Module success with '+str(len(subs)))
        res_subs = res_subs.union(subs)

    # 使用 dns 枚举
    if args.bruteforce:
        # logging.info("Fuck")
        df = DomainFuzzer(domain)
        # 爆破得到的域名列表
        subs = set()
        for sub in df.run(thread_cnt):
            subs.add(sub)
        logging.info('Bruteforce Module success with '+str(len(subs)))
        res_subs = res_subs.union(subs)

    logging.info('End success with '+str(len(res_subs)))
    for x in res_subs:
        print x
    return res_subs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Multi-method SubDomain Seeker")
    parser.add_argument("-t","--thread",metavar='NUM',default=100,help="thread count")
    parser.add_argument("-d","--domain",metavar='DOMAIN',help="target doamin")
    parser.add_argument("-b","--bruteforce",help="dns bruteforce",action='store_true')
    parser.add_argument("-s","--search",help="search engine",action='store_true')
    parser.add_argument("-a","--api",help="domain finder api",action='store_true')    
    args = parser.parse_args()

    try:
        run(args)
    except KeyboardInterrupt:
        logging.info("Ctrl C - Human Stop")
        sys.exit(1)