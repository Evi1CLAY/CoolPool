# coding: utf-8
# anka9080
# 测试使用socks5 访问网站

__author__ = 'Anka9080'

import socket
import requests
import socks

# HTTP Headers
HEADERS = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Cache-Control':'max-age=0',
	'Connection':'Connection',
}

# Google 搜索
class Google():

	def __init__(self):
		# 使用 google.co.jp 谷歌日本的搜索引擎
		self.url = 'https://www.google.co.jp/#q='
		self.url0 = 'http://ip.cn'
		self.keyword  = 'Anka9080'
		self.spider()
		# 设置 sock5 代理
		socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",1080)
		socket.socket = socks.socksocket
		print(requests.get(url = self.url0, headers = HEADERS).text)

	# 爬行页面抓取 urls
	def spider(self):
		pass

if __name__ == '__main__':
	Google()
