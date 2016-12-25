# coding:utf-8

# MySQL 处理器

import time
import MySQLdb

from config import *

class MySQLHandler():
	def __init__(self):
		try:
			self._conn = MySQLdb.connect(host=MYSQL_HOST,
										port = MYSQL_PORT,
										user = MYSQL_USER,
										passwd = MYSQL_PASS,
										db = MYSQL_DBS,
										charset = MYSQL_CHARSET)
		except MySQLdb.Error,e:
			err_msg = '[-] MySQL err ',e.args[0],e.args[1]
			print err_msg
			# 失败重新连接
			if self._timecount < self._TIMEOUT:
				interval = 5
				time.sleep(interval)
				self._timecount += interval
				return self.__init__()
			else:
				raise Exception(err_msg)
		# 链接成功，初始化游标
		self._cur = self._conn.cursor() 

	def query(self,sql,verbose=True):
		if verbose:
			print '----\nquery sql:',sql
		try:
			self._cur.execute("SET NAMES utf8")
			res = self._cur.execute(sql)
		except Exception,e:
			err_msg = '[-] Query err: ',e.args[0],e.args[1]
			res = False
		return res

	def update(self,sql,verbose=True):
		if verbose:
			print '----\nupdate sql:',sql
		try:
			self._cur.execute("SET NAMES utf8")
			res = self._cur.execute(sql)
			self._conn.commit()
		except Exception,e:
			err_msg = '[-] Update err: ',e.args[0]
			print err_msg
			res = False
		return res

	def insert(self,sql,verbose=True):
		if verbose:
			print '----\ninsert sql:',sql
		try:
			self._cur.execute("SET NAMES utf8")
			res = self._cur.execute(sql)
			self._conn.commit()
		except Exception,e:
			err_msg = '[-] Insert err: ',e.args[0],e.args[1]
			res = False
			print err_msg
		# res = self._conn.insert_id()
		res = self._cur.lastrowid
		# print res
		return res

	def fetch_one(self):
		return self._cur.fetchone()

	def fetch_all(self):
		return self._cur.fetchall()

	def get_record_count(self):
		return self._cur.rowcount

	def close(self):
		try:
			self._cur.close()
			self._conn.close()
		except:
			pass

if __name__ == '__main__':
	mysql = MySQLHandler()
	sql = "select * from task where taskid = 2200"
	mysql.query(sql)
	count = mysql.get_record_count()
	print count
	mysql.close()