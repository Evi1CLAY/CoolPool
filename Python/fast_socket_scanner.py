# coding: utf-8
# fast_socket_scanner v0.1
# anka9080
# 多线程端口扫描器

import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

remote_server = raw_input("Enter a remote host to scan:")
remote_server_ip = socket.gethostbyname(remote_server)
ports = []

print '-' * 60
print 'Please wait, scanning remote host ', remote_server_ip
print '-' * 60


socket.setdefaulttimeout(2)

def scan_port(port):
    try:
        s = socket.socket(2,1)
        res = s.connect_ex((remote_server_ip,port))
        if res == 0: # 如果端口开启 发送 hello 获取banner
            try:
                s.send('hello')
                banner = s.recv(1024)

            except Exception,e:
                print 'Port {}: OPEN'.format(port)
                print str(e.message)
            else:
                print 'Port {}: OPEN'.format(port)
                print 'Banner {}'.format(banner)

        s.close()
    except Exception,e:
        print str(e.message)



for i in range(1,1025):
    ports.append(i)

# Check what time the scan started
t1 = datetime.now()


pool = ThreadPool(processes = 1024)
results = pool.map(scan_port,ports)
pool.close()
pool.join()

print 'Multiprocess Scanning Completed in  ', datetime.now() - t1




