
# coding:utf-8

'''
title: 爬取指定网站单页的 HTML 静态文件  v 1.0
description: 1. 抓取网站单页引入的本地 JS ， CSS ， 图片(jpg,png) 文件
			 2. 抓取网站单页引入的 CSS 文件里引入的 图片文件(一些背景图)
			 3. 抓取网站单页引入的 CSS 文件里引入的 其他 CSS 文件
author: EvilCLAY
time: 2015.10.10
'''
import urllib 
import urllib2
import re
import os 
import time
import socket

class HTMLCPer():
	
	# 构造函数
	def __init__(self,index):
		# 首页url地址
		self.index = index
		self.indexHTML = ''
		self.ResourcesList = []
		self.ImageList = []
		self.downloadIndex()
		self.getResourcesList()
		self.downloadResourcesFile()
	
	# 下载首页 HTML 文档
	def downloadIndex(self):
		req = urllib2.Request(self.index)
		# 获得 html 文档 并编码成 gbk 在 Windows CMD 打开才不会乱码
		content = urllib2.urlopen(req).read()
		self.indexHTML = content
		with open('index.html','w') as w:
			w.write(content)
		#print content
	'''
		默认资源文件包括：
		1、 css文件
		2、 js文件
		3、 png/jpg 类型图片文件
	'''
	# 获得 首页引入的 资源 文件列表
	def getResourcesList(self):

		pattern1 = re.compile(r'href[=" ]{2,5}(.*?\.css)')
		res = pattern1.findall(self.indexHTML)
		for i in res:
			self.ResourcesList.append(i)

		pattern2 = re.compile(r'script .*?src[=" ]{2,5}(.*?\.js)')
		res = pattern2.findall(self.indexHTML)
		for i in res:
			self.ResourcesList.append(i)

		pattern3 = re.compile(r'img .*?src[=" ]{2,5}(.*?\.jpg|.*?\.png)')
		res = pattern3.findall(self.indexHTML)
		for i in res:
			if i not in self.ResourcesList:
				self.ResourcesList.append(i)

		print len(self.ResourcesList)

	# 下载 资源 文件
	def downloadResourcesFile(self):
		
		# 本地新建  资源 文件
		for i in self.ResourcesList:
			print i
			
			# 如果 css js 是外部网站的资源 则跳过
			if 'http://' in i or 'https://' in i:
				continue
			else:
				newDir = ''
				
				# 从 资源 的文件名里面解析出文件名，文件夹名，用于之后在本地当前目录创建对应文件，文件夹
				dirList = i.split('/')
				for d in dirList[:-1]:
					# split 出来的会有空文件名
					if d != '':

						newDir = newDir + d + '\\'
				
				newDir = os.getcwd() + '\\' + newDir
				# print newDir
				# 批量创建文件夹、子文件夹
				if not os.path.isdir(newDir):
					print '[+] file not exists. creating...'
					os.makedirs(newDir)
				else:

					print '[-] file alreadly exists'

				newFile = newDir + dirList[-1]
				print newFile
				if not os.path.isfile(newFile):
					print '\n[+] download ' + newFile + '...'
					with open(newFile,'wb') as w:
						try:
							time.sleep(2)
							req = urllib2.Request(self.index + i)
							content = urllib2.urlopen(req).read()
							w.write(content)
							if 'css' in i:
								#print '===========  find a css file!'
								self.downLoadCSSImage(content)
								self.downLoadImportCSS(content,i)
								#print content
						except Exception,e:
							print e
					# try:
					# 	urllib.urlretrieve(self.index + i,newFile)
					# except Exception,e:
					# 	print e
					# 	continue

					# print 'ok!'
				print '================================================================='
		for x in self.ResourcesList:
			print x
		print 'Downloaded all:' + str(len(self.ResourcesList))

	# 解析 CSS 文件中的 图片文件，放到资源列表
	def downLoadCSSImage(self,cssText):
		
		pattern4 = re.compile(r'url\(([\/\w.]*\.jpg|[\/\w.]*\.png)')
		res = pattern4.findall(cssText)
		for j in res:
			if j not in self.ResourcesList:
				self.ResourcesList.append(j)
		
	# 解析 CSS 文件中的 引入的 CSS 文件，放到资源列表
	def downLoadImportCSS(self,cssText,cssName):
		# print '============================ test have import ?'
		pattern5 = re.compile(r'import "([\/\w.]*\.css)"')
		res = pattern5.findall(cssText)
		for j in res:
			# print '====================== find  a import css'
			mark = cssName.rfind('/')
			j = cssName[:mark + 1] + j
			if j not in self.ResourcesList:
				self.ResourcesList.append(j)

if __name__ == "__main__":

	HTMLCPer('http://www.evilclay.com/')
	socket.setdefaulttimeout(5)