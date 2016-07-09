# coding:utf-8
# DomainSeeker v0.1
# anka9080
# 20160709
# 需要注意token的值
# 程序运行期间访问checkapi.aliyun.com可能会被ban IP

import time
import json
from requests import get

class DomainSeeker(object):
	"""docstring for DomainSeeker"""
	def __init__(self,keywords,suffix,save_file):
		super(DomainSeeker, self).__init__()
		self.aval_domains = []
		self.LOG_FILE = open('log.txt','w')
		self.spider(keywords,suffix)
		self.save(save_file)
		self.LOG_FILE.close()

	# https://checkapi.aliyun.com/check/checkdomain?domain=aaa.store&token=check-web-hichina-com%3Axjqeea1rgettssvasmsc0c8cf3igdp6x
	def spider(self,keywords,suffix):
		all = len(keywords)
		i = 0
		ok = 0
		for k in keywords:
			print '[*]',i,' of ',all,,'avail :',ok
			i += 1
			try:
				r = get('https://checkapi.aliyun.com/check/checkdomain?'\
					'domain={}.{}&token=check-web-hichina-com%3Aamdg6mi'\
					'3q7pdkt4octyjam3vyjh9hth9'.format(k,suffix))
				html = r.text
				res = html[1:-2]
				data = json.loads(res)
				module = data['module']
				print module
				self.log_str(str(module) + ' >  ' + str(i) + ' of ' + str(all))
				if module[0]['avail']:
					ok += 1
					print '[*] find a avaliable domain ---> {}'.format(module[0]['name'])
					self.aval_domains.append(module[0]['name'])
				time.sleep(1)
			except Exception,e:
				print '[*] ',str(e)
				continue

	def log_str(self,str):
		self.LOG_FILE.write(str + '\n')

	def save(self,save_file):
		with open(save_file,'w') as output:
			for ad in self.aval_domains:
				print ad
				output.write(ad + '\n')

def create_keywords():
	chars = 'zyxwvutsrqponmlkjihgfedcba9876543210-'
	# keywords = ['asda12dw','qwes2i2']
	keywords = [x+y+z for x in chars for y in chars for z in chars]
	return keywords

def main():
	keywords = create_keywords()
	suffix = 'win'
	save_file = 'win.txt'
	DomainSeeker(keywords,suffix,save_file)
	# DomainSeeker(keywords,suffix,save_file)


def test():
	a = 'abcdefghijklmnopqrstuvwxyz'
	res =''
	for i in range(1,27):
		res += a[-i]
	print res

if __name__ == '__main__':
	main()
	# test()
		