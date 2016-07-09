# coding:utf-8
# anka9080
# SSHLogAnalyser v0.1

"""
	分析 Ubuntu日志文件auth.log，
	获得有哪些IP尝试访问主机，并记录最后一次访问时间
"""

import re
import time

class SSHLogAnalyser(object):
	"""docstring for SSHLogAnalyser"""
	def __init__(self, ssh_file,save_file):
		self.ip_time={}
		self.p_ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		self.p_time = re.compile(r'^\w{3,12}  \d{1,2} [\d\:]{8}')
		self.read_and_analyse(ssh_file)
		self.save(save_file)

	def read_and_analyse(self,ssh_file):
		with open(ssh_file) as input:
			for x in input.readlines():
				ip = re.search(self.p_ip,x)
				if ip:
					ip = ip.group()
					t = re.search(self.p_time,x).group()
					self.ip_time[ip] = t
					# print ip

	def save(self,save_file):
		# print len(self.ip_time)
		with open(save_file,'w') as output:
			for k,v in self.ip_time.items():
				output.write(k +' ---> ' + v + '\n')

def main():
	start = time.time()
	ssh_file = 'auth.log'
	save_file = 'ip_time.txt'
	SSHLogAnalyser(ssh_file,save_file)
	end = time.time()
	print '[*] Analyse [ {} ] over , cost: {:.2f} s'.format(ssh_file,end-start)

if __name__ == '__main__':
	main()
