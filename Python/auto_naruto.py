# coding: utf-8

'''
title: 火影忍者online 自动刷FB + 生存试练1-9关 脚本
description: 
		1. 操作系统要求 windows ，浏览器要求 Chrome45，电脑分辨率 1366*768
		2. 调用 pymouse库 完成自动点击，拖拉鼠标的操作，即运行脚本后鼠标会自动点击
		3. 自带一键AI的回合制游戏就是脚本的屠宰场呀  每天手动扫荡什么的实在无聊到爆
		4. 在这里默认设定刷的是君麻吕和凯碎片的FB，需要扫荡生存试练1-9关的把 live_training() 前面的注释清掉
author: EvilCLAY
time: 2015.11.20
how to use: 
		python auto_naruto.py
'''

from pymouse import PyMouse
from time import sleep

def auto_fb():
	global count,m
	
	# 副本按钮
	sleep(0.5)
	m.click(1316,676)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	# 剧情副本按钮
	sleep(2)
	m.click(600,120)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	## 副本列数：2  木叶保卫战
	sleep(0.5)
	m.click(300,210)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	slide_to_bottom()

	# 副本ID：10  飞段与角都
	sleep(2)
	m.click(580,320)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	# 精英副本按钮
	sleep(2)
	m.click(760,120)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())


	## 副本列数：1  70级
	sleep(0.5)
	m.click(250,160)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	slide_to_top()

	# 副本ID：6  凯
	sleep(2)
	m.click(1060,470)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	slide_to_bottom()

	# 副本ID：12  君麻吕
	sleep(2)
	m.click(1070,470)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	# 副本ID：13  阿飞
	sleep(2)
	m.click(580,620)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	## 副本列数 3 50级
	sleep(2)
	m.click(260,260)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	slide_to_top()

	# 副本ID：5  君麻吕
	sleep(2)
	m.click(830,470)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	slide_to_bottom()

	# 副本ID：13  凯
	sleep(2)
	m.click(580,320)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	## 副本列数：5  30级
	sleep(0.5)
	m.click(300,360)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	slide_to_bottom()

	# 副本ID：19  凯
	sleep(2)
	m.click(580,620)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	fight_this_fb()

	# 关闭副本面板
	sleep(2)
	m.click(1160,130)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

def fight_this_fb():
	global count,m

	print '[+] Click Number '+ str(count) +'  ' + str(m.position())
	# 进行3次副本扫荡
	sleep(2)
	m.click(780,610)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	# 取消重置副本（防止重复扫荡）
	sleep(0.5)
	m.click(760,430)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

	# 关闭扫荡面板
	sleep(2)
	m.click(950,150)
	count += 1
	print '[+] Click Number '+ str(count) +'  ' + str(m.position())

def slide_to_top():
	# 拖动副本滑动栏到顶部
	global m
	sleep(2)
	m.press(1130,500)
	sleep(1)
	m.move(1130,270)
	sleep(1)
	m.release(1130,270)

def slide_to_bottom():
	# 拖动副本滑动栏到底部
	global m
	m.press(1130,270)
	sleep(1)
	m.move(1130,370)
	sleep(1)
	m.release(1130,370)


def live_training():
	# 进入生存试炼
	sleep(1)
	m.click(740,90)
	# 重置
	sleep(1)
	m.click(740,670)
	# # 第 1 - 6 层
	sleep(1)
	m.click(380,240)
	sleep(1)
	m.click(480,240)
	comform_prize()
	m.click(550,370)
	sleep(1)
	m.click(410,360)
	comform_prize()
	m.click(430,560)
	sleep(1)
	m.click(540,530)
	comform_prize()
	m.click(690,560)
	sleep(1)
	m.click(740,410)
	comform_prize()
	m.click(880,390)
	sleep(1)
	m.click(950,200)
	comform_prize()
	m.click(1100,240)
	sleep(1)
	m.click(1240,150)
	comform_prize()
	sleep(1)
	m.click(1330,360)
	# # 第 7 - 9 层
	m.click(110,270)
	sleep(1)
	m.click(120,360)
	comform_prize()
	m.click(140,570)
	sleep(1)
	m.click(270,470)
	comform_prize()
	m.click(420,510)
	sleep(1)
	m.click(530,370)
	comform_prize()
	# #  第 10 - 12 层
	m.click(570,220)
	# 水主
	sleep(1)
	m.press(370,100)
	sleep(1)
	m.move(320,440)
	sleep(1)
	m.release(320,440)
	# 佐助
	sleep(1)
	m.press(730,100)
	sleep(1)
	m.move(420,440)
	sleep(1)
	m.release(420,440)
	# 畜生道
	sleep(1)
	m.press(880,100)
	sleep(1)
	m.move(310,470)
	sleep(1)
	m.release(310,470)
	# 南
	sleep(1)
	m.press(850,100)
	sleep(1)
	m.move(410,470)
	sleep(1)
	m.release(410,470)
	# 确定布局
	sleep(1)
	m.click(680,170)



def comform_prize():
	sleep(1)
	m.click(680,450)
	sleep(1)

if __name__ == '__main__':
	# 焦点回到游戏
	count = 0 
	m = PyMouse()
	sleep(1)
	m.click(50,110)

	# 自动刷 FB
	auto_fb()

	# 生存试炼
	# live_training()


