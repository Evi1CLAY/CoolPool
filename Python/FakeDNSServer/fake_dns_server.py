#!/usr/bin/env python
# coding: utf-8
# author: Anka9080
# mail: funsociety.bat@gmail.com

# 说明：
# 没有 DNSLog 功能强大，一个轻便型 伪DNS 服务器
# 可以配合 nslookup 命令 显示没有回显类漏洞的命令执行结果
# 不能实现真正的DNS解析，直接打印请求的IP，Port和需要解析的域名
# 说白了就是一个UDP的socket绑定在53端口循环接收DNS请求信息并格式化输出 xD

import sys
import socket
import thread

class DNSQuery(object):
    """
    DNS请求解析类
    from http://code.activestate.com/recipes/491264-mini-fake-dns-server/
    """
    def __init__(self, data):
        self.data = data
        self.domain = ''

        tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
        if tipo == 0:                     # Standard query
            ini = 12
            lon = ord(data[ini])
            while lon != 0:
                self.domain += data[ini+1:ini+lon+1]+'.'
                ini += lon+1
                lon = ord(data[ini])


def usage():
    print ""
    print "Usage:  python fake_dns_server.py"
    print ""
    print "并没有提供DNS解析功能，直接打印发起请求的IP，Port和需要解析的域名 :P"
    print ""
    sys.exit(1)

def print_dns_query(data, addr):
    p=DNSQuery(data)
    ip = addr[0]
    port = addr[1]
    print 'From {}:{} DNSQuery -> {}'.format(ip,port,p.domain)

if __name__ == '__main__':
    try:
        udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建一个UDP IPv4型 Socket
        udps.bind(('', 53))  # 绑定 53 端口
    except Exception, e:
        print "Failed to create socket on UDP port 53:", e
        sys.exit(1)

    print '\nFake DNS Server Started > ... \n'
    try:
        while 1:
            data, addr = udps.recvfrom(1024)
            thread.start_new_thread(print_dns_query, (data, addr))
    except KeyboardInterrupt:
        print '\n^C, Exit!'
    except Exception, e:
        print '\nError: %s' % e
    finally:
        udps.close()

