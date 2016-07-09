# coding:utf-8
# author: anka9080
# date: 20160429
# 测试使用 Ghost 解析网页内容

from ghost import Ghost
ghost = Ghost()

with ghost.start() as session:
    try:
    	page, extra_resources = session.open("http://mysweet.gift")
    	print page.http_status
    	print page.content
    except Exception,e:
    	print e