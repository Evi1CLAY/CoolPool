#coding:utf-8
# 列车号信息抓取脚本
# author: Anka9080
# time  : 2016/12/25
# referer: www.huoche.net
# Merry Christmas~



import re
import time
from requests import get
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from config import TYPE_MAP,HEADERS
from model import MySQLHandler



class Train(object):

    def __init__(self):
        self.index = 'http://www.huoche.net/lieche/'
        self.detail = 'http://www.huoche.net/checi/'
        self.train_no_ptn = re.compile(ur'<li><a href="http://www.huoche.net/checi/(\w{1,6})/" title="\w{1,6}车次时刻表" target="_blank">\w{1,6}</a> </li>')
        self.station_ptn = re.compile(ur'title="([\u4e00-\u9fa5]{1,10})火车站时刻表"  target="_blank">[\u4e00-\u9fa5]{1,10}</a></td>')
        print TYPE_MAP
    
    def init_train_no(self):
        for no,train_type in TYPE_MAP.items():
            url = self.index +'checi' + no
            rsp = get(url,HEADERS)
            # print rsp.text
            mysql = MySQLHandler()
            res = re.findall(self.train_no_ptn,rsp.text)
            for train_no in res:
                sql = "insert into train(train_no,train_type) values('{}','{}')".format(train_no,train_type)
                mysql.insert(sql)

                print train_no
            mysql.close()
            time.sleep(2)

    def get_train_no(self):
        mysql = MySQLHandler()
        sql = "select train_no from train where stations = ''"
        mysql.query(sql)
        res =  mysql.fetch_all()
        self.train_nos = []
        for (train_no,) in res:
            self.train_nos.append(train_no)
        mysql.close()
        print 'ALL Train Count',len(self.train_nos)
        return self.train_nos

    def init_detail(self):
        for train_no in self.train_nos:
            url = self.detail + train_no + '/'
            rsp = get(url,HEADERS)
            # print rsp.text
            res = re.findall(self.station_ptn,rsp.text)
            station_list = []

            for station in res:
                station_list.append(station)
            station_str = ','.join(station_list)

            mysql = MySQLHandler()
            sql = "update train set stations = '{}' where train_no = '{}'".format(station_str,train_no)
            # print sql
            mysql.update(sql)
            mysql.close()
            
            # time.sleep(1)
            # break

    def unavailable_check(self):
        for train_no in self.train_nos:
            url = self.detail + train_no + '/'
            rsp = get(url,HEADERS)
            # print rsp.text
            if '没有你要查找的车次,或该车' in rsp.text:
                mysql = MySQLHandler()
                sql = "update train set stations = '{}' where train_no = '{}'".format('暂时停用',train_no)
                # print sql
                mysql.update(sql)
                mysql.close()

if __name__ == '__main__':
    t = Train()
    # t.init_train_no()
    t.get_train_no()
    # t.init_detail()
    t.unavailable_check()