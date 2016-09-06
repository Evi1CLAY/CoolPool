# coding:utf-8
# tasks.py

'''
需要安装的环境：
==== RabbitMQ 消息中间人
sudo apt-get install rabbitmq-server
==== Celery 协程
pip install celery
'''

from celery import Celery
import time

# Celery 实例, Worker 进程，可以作为守护进程执行

# tasks 当前模块的名称
# broker 指定消息中间人
# backend 指定后端数据库，用于追踪任务的状态
app = Celery('tasks',broker='amqp://localhost',backend='amqp')

# add 单一的任务aa
@app.task
def add(x,y):
	print '[*] Start task with x : {0} and y : {1}'.format(x,y)
	time.sleep(5)
	res = x+y
	print '[+] Add RES: {0}'.format(res)
	# Fucking Success! We can call other worker in the worker
	# print mult.delay(x,y)
	return res

# mult
@app.task
def mult(x,y):
	print '[*] Start task with x : {0} and y : {1}'.format(x,y)
	time.sleep(5)
	res = x*y
	print '[+] Mult RES: {0}'.format(res)
	return res

# 启动 Celery Woker 服务器
# tasks 指需要启动的Celery模块名称
# celery -A tasks worker --loglevel=info

'''
# 调用 worker 的代码
# 建议在 python 交互式shell执行 方便观察结果

from tasks import add,mult

# 使用异步的方式执行add任务，返回一个AsyncResult实例，可用于检查任务的状态
res = add.delay(2,2)
# 查看任务是否处理完成
res.ready()
# 等待任务处理完成并输出结果，会把异步调用变成阻塞调用，不常用
res.get(timeout=1)
# 使用阻塞调用方式执行 mult 任务不会调用 Celery的Worker，执行结束得到mult方法的返回值
res = mult(3,3)
'''





