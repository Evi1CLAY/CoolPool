# coding:utf-8
# Project :Python 的线程池实现
# Author: Anka9080

import Queue
import threading
import sys
import time
import urllib

class MyThread(threading.Thread):
	def __init__(self,workQueue,resultQueue,timeout = 30, **kwargs):
		threading.Thread.__init__(self,kwargs = kwargs)

		self.timeout = timeout
		self.setDaemon(True) # 将线程声明为守护线程，如果不声明会被无线挂起
		################?
		self.workQueue = workQueue
		self.resultQueue = resultQueue
		self.start() # 线程开始工作

	def run(self):
		while True:
			try:
				# 从工作队列获取一个任务
				callable, args,kwargs = self.workQueue.get(timeout = self.timeout)
				# 执行任务
				res = callable(args,kwargs)
				# 将执行结果返回到结果队列中
				self.resultQueue.put(res + "| 线程名：" + self.getName())
			################？
			except Queue.Empty: # 任务对列为空结束此线程
				break
			except :
				print sys.exc_info() # 打印异常消息
				raise	# 抛出异常
class ThreadPool:
	def __init__(self,num_of_threads = 10):
		self.workQueue = Queue.Queue()	# 初始化任务队列为空
		self.resultQueue = Queue.Queue() # 初始化结果队列为空
		self.threads = []	# 设置线程池的线程列表，初始化为空
		self.__createThreadPool(num_of_threads) # 创建num_of_threads个线程，并添加到self.threads列表中

	# 创建线程池
	def __createThreadPool(self,num_of_threads):
		for i in range(num_of_threads):
			################# 为什么要传入workQueue...绑定？
			thread =  MyThread(self.workQueue,self.resultQueue) 
			self.threads.append(thread)	# 把线程实体添加到线程尺中

	# 向工作队列添加任务
	def add_job(self,callable, *args, **kwargs):
		self.workQueue.put( (callable,args,kwargs)) # 向工作序列添加任务

	# 分配线程调用run函数处理工作队列的任务，处理完成后将结果返回到结果队列resultQueue
	def wait_for_complete(self):  
		while len(self.threads):
			thread = self.threads.pop() # 从线程池取出这个线程
			if thread.isAlive():
				thread.join()	# 若线程存活，则调用join处理工作队列



def test_job(id,sleep  = 1):
	html = ""
	try:
		#time.sleep(0)
		conn = urllib.urlopen('http://www.baidu.com') 
		html = conn.read(20) # 读取前20个字节
	except:
		print sys.exc_info()
	return html

def main():
	start =  time.time()
	print 'start testing'
	# 创造线程池对象，设定10个线程
	tp = ThreadPool(10)
	# 利用循环，产生50个任务并添加到工作序列workQueue
	for i in range(50):
		#time.sleep(0.2)
		tp.add_job(test_job,i, i * 0.001)

	print  'wait for complete...'

	tp.wait_for_complete()

	print 'result Queue\'s length == %d' % tp.resultQueue.qsize()

	while tp.resultQueue.qsize():
	# 从结果队列拿出任务完成的结果
		print tp.resultQueue.get()
		
	print 'end testing'
	end = time.time()
	cost = end - start
	print cost

if __name__ == '__main__':
	main()
