# coding : utf-8
# author : EvilCLAY
# date   : 20160402
# version: 1.0

import socket
from socket import gethostbyname

def domain2ip():
	"""
		批量把域名转换成 IP 
		input : domain.txt
		output: domain_ip.txt
	"""
	ip_list = []
	with open('domain.txt') as input:
		with open('domain_ip.txt','w') as output:
			for line in input.readlines():
				domain = line.strip('\n')
				try:
					ip = gethostbyname(domain)  # 探测主机是否存活
				except Exception,e:
					ip = 'noip'
				if ip is not 'noip' :
					ip_list.append(ip)
				info =  domain + '__' + ip 
				print info
				output.write( info + '\n')

	ip_list = list(set(ip_list))
	with open('ip.txt','w') as output:
		output.write("\n".join(ip_list))

if __name__ == '__main__':
	socket.setdefaulttimeout(3)
	domain2ip()
