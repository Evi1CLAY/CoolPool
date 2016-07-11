# coding:utf-8
# anka9080
# SSHLogAnalyser v0.2

"""
	v0.1
	分析 Ubuntu日志文件auth.log，
	获得有哪些IP尝试访问主机，并记录最后一次访问时间
	v0.2 更新：
	增加了 显示 IP 对应的地理位置功能
	v0.3 更新：
	fix multiprocessing IP_TIME_LOCATION empty BUG
"""

import sys
import re
import time
from requests import get
from multiprocessing.dummy import Pool as ThreadPool

IP_TIME = []
IP_TIME_LOCATION = []
pattern = re.compile(ur'所在地理位置：\<code\>(.*?)\<\/code\>')
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept':'*/*'
}

class SSHLogAnalyser(object):
	"""docstring for SSHLogAnalyser"""
	def __init__(self, ssh_file):
		self.ip_time={}
		self.p_ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		self.p_time = re.compile(r'^\w{3,12}  \d{1,2} [\d\:]{8}')
		self.read_and_analyse(ssh_file)
		# self.save(save_file)
		self.expert_out()

	def read_and_analyse(self,ssh_file):
		with open(ssh_file) as input:
			for x in input.readlines():
				ip = re.search(self.p_ip,x)
				if ip:
					ip = ip.group()
					t = re.search(self.p_time,x).group()
					self.ip_time[ip] = t
					# print ip

	# def save(self,save_file):
	# 	# print len(self.ip_time)
	# 	with open(save_file,'w') as output:
	# 		for k,v in self.ip_time.items():
	# 			output.write(k +' ---> ' + v + '\n')

	def expert_out(self):
		for k,v in self.ip_time.items():
			IP_TIME.append((k,v))

def ip2location(ip_time):
	time.sleep(1)
	ip = ip_time[0]
	t = ip_time[1]
	url = 'http://ip.cn/index.php?ip=' + ip
	try:
		r = get(url,headers = HEADERS,timeout = 3)
		html = r.text
		res = re.search(pattern,html)
		location = res.group(1)
		# print type(location)
		print '[*]',ip,location
	except Exception,e:
		print '[*]',str(e)
		location = 'UNKNOW IP'
	IP_TIME_LOCATION.append((ip,t,location))
	# return (ip,t,location)

def save(save_file):

	IP_TIME_LOCATION
	# for x,y,z in IP_TIME_LOCATION:
	# 	print x,y,z
	with open(save_file,'w') as output:
		for x,y,z in IP_TIME_LOCATION:
			# print x+'----' + y + '----' + z
			output.write(x+'----' + y + '----' + z +'\n')

def test():
	# url = 'http://ip.cn/index.php?ip=mysweet.gift'
	# r = get(url)
	# html = r.text
	# res = re.search(pattern,html)
	# print res.group(1)
	ip2location(('124.83.54.249', 'Jul  5 04:30:19'))

def main():
	start = time.time()
	reload(sys)
	sys.setdefaultencoding("utf-8")
	ssh_file = 'auth.log'
	save_file = 'ip_time.txt'
	SSHLogAnalyser(ssh_file)
	end = time.time()
	print '[*] Analyse to get ip [ {} ] over , cost: {:.2f} s'.format(ssh_file,end-start)

	tp = ThreadPool(4) # fuzz result get thread 4 is just fine!
	IP_TIME_LOCATION = tp.map(ip2location,IP_TIME)
	tp.close()
	tp.join()
	# for x,y,z in IP_TIME_LOCATION:
	# 	print x,y,z

	save(save_file)
	eend = time.time()
	print '[*] request to get location [ {} ] over , cost: {:.2f} s'.format(ssh_file,eend-end)

if __name__ == '__main__':
	main()
	# test()