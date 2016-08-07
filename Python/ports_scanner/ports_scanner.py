# coding:utf-8
# author: Anka9080
# time:20160804
# 多线程端口扫描器 v 1.0
# 直接python ports_scanner.py 运行脚本：
# 默认从ip.txt中读取ip，输出rex.txt，扫描线程20。
# 扫描端口：21,22,23,25,53,80,88,110,443,1080,1433,3124,
#           3128,3306,3389,5900,8000,8080,9100,9200,27017

import os
import re
import socket
import threading
import Queue

from subprocess import Popen, PIPE
from datetime import datetime
from optparse import OptionParser
socket.setdefaulttimeout(1)

def init_ip(ip_file):
    ips = []
    ip_reg = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\..*')
    if re.match(ip_reg,ip_file):
        if ',' in ip_file:  # multi-ip
            ips = ip_file.split(',')
        elif '*' in ip_file:  # ip C segment
            mark = ip_file.find('*')
            ip_pre = ip_file[:mark]
            for x in range(1,255):
                ip = ip_pre + str(x)
                ips.append(ip)
        else: # one ip
            ips.append(ip_file)
    else: # use ip file as input
        with open(ip_file,'r') as input:
            for row in input.readlines():
                ip = socket.gethostbyname(row.strip())
                ips.append(ip)
    return ips

def check_online(ips):
    # new_ips = []
    # for ip in ips:
    #     p = Popen("ping -n 1 " + ip,stdout=PIPE)
    #     print p.stdout.read()
    #     res =  re.search(' = (.*)ms',p.stdout.read())
    #     if res: #  shows online
    #         print '[+] {} is alive.'.format(ip)
    #         new_ips.append(ip)
    return ips

def init_queue(ips,ports):
    queue = Queue.Queue()
    for ip in ips:
        for port in ports:
            queue.put((ip,port))
    # print '--',queue.qsize()
    return queue

# thread run the function
def run(queue,save_file):
    # queue = args()
    while not queue.empty():
        ip,port = queue.get()
        # print ip,port
        try:
            s = socket.socket(2,1)
            res = s.connect_ex((ip,port))
            # print res
            if res == 0: # 如果端口开启 发送 hello 获取banner
                print '[+] {} {}: OPEN'.format(ip,port)
                save_file.write('{}:{}\n'.format(ip,port))
                save_file.flush()
            else:
                print '[-] {} {}: CLOSE'.format(ip,port)
            s.close()
        except Exception,e:
            print str(e.message)

def usage():
    parser = OptionParser()
    parser.add_option('-i',"--ip",dest = 'ip_file',default ='ip.txt',help = 'set the ip file,default ./ip.txt') # 设置IP读取的文件
    parser.add_option('-s',"--save",dest = 'save_file', default = 'res.txt',help = 'set results file,default ./res.txt') # 设置结果输出文件
    parser.add_option('-p',dest = 'port',default = '',help = 'set port,if more than one,use "," split them') # 自定义扫描的端口
    parser.add_option('-t',"--threads",dest = 'thread_num',default = '20',help = 'set scan threads num,default 20') # 设置扫描的线程数
    global options
    (options, args) = parser.parse_args()
    return parser

def main():
    parser = usage()

    global options
    # set ips
    ip_file = options.ip_file
    try:
        ips = init_ip(ip_file)
    except Exception,e:
        print '[-]',str(e),'\n'
        print parser.print_help()
        return -1
    # get alive ips
    ips = check_online(ips)
    # set ports
    ports = [21,22,23,25,53,80,88,110,443,1080,1433,3124,3128,3306,3389,5900,8000,8080,9100,9200,27017]
    if options.port:
        ports = []
        ports_str = options.port.split(',')
        for x in ports_str:
            ports.append(int(x))
    # set work queue
    queue = init_queue(ips,ports)
    # set save_file
    save_file = open(options.save_file,'w')

    # print queue.qsize()

    # set threads
    threads = []
    thread_num = 1000   # default set threads to 100
    if options.thread_num:
        thread_num = int(options.thread_num)
    # run threads
    for x in range(thread_num):
        t = threading.Thread(target=run,args=(queue,save_file))
        t.start()
        threads.append(t)
        print t.getName(),'started !'

    for t in threads:
        t.join()  # avoid main thread quit early

if __name__ == '__main__':
    main()
