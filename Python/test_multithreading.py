# coding: utf-8
# author: EvilCLAY
# date  : 20160404

import time
import threading

class Worker(threading.Thread):
	def __init__(self,num): 
		threading.Thread.__init__(self) # 父类初始化
		self._run_num = num
		
	"""
		run 函数里写每一个线程运行的实例
		需要共享的全局变量 要加上 global 声明
		需要对变量的值进行修改 要加上互斥锁 
	"""
	def run(self):  # 
		global count,mutex
		thread_name = threading.currentThread().getName()

		for x in xrange(0,int(self._run_num)):
			mutex.acquire()
			count += 1
			mutex.release()
			print '[-] thread_name :',thread_name , '循环次数:',x , '计数器:',count
			time.sleep(1)

if __name__ == '__main__':
	global count,mutex
	threads = []  # 多线程列表
	num = 5
	count = 0

	# 创建锁
	mutex = threading.Lock()
	# 创建线程对象
	for x in xrange(0,num):
		threads.append(Worker(10))
	# 启动线程
	for t in threads:
		t.start()

	# 等待子线程结束
	for t in threads:
		t.join()