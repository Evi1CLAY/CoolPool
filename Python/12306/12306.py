# coding:utf-8
# 刷票助手 v0.1

import ssl,urllib2
import json
import smtplib
import time
import datetime
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header

from config import *

# trains = ['G345','G1905']

seat_dict = {
    '二等座':'ze_num',
    '硬卧':'yw_num',
    '硬座':'yz_num'
}
seat_name = ''

# 根据输入判断选择的座位类型
def select_seat():
    global seat_name
    if seat_type in seat_dict.keys():
        seat_name = seat_dict[seat_type]


"""
    请求页面判断指定的车次是否有指定座位
"""
def refresh():
    global seat_name
    # url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-10-06&from_station=OXH&to_station=HFH'
    # r = requests.get(url)
    req = urllib2.Request(url)
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    html = urllib2.urlopen(req, context=gcontext).read()
    # print html
    print '> {} refrash ...'.format(datetime.datetime.now())
    html_dict = json.loads(html)
    # print html_dict
    datas = html_dict['data']['datas']
    for data in datas:
        if data['station_train_code'] in trains:
        # if data['station_train_code']:
            # ze_num 表示二等座
            if data[seat_name] != u'无' and data[seat_name] != u'--':
                print  data
                print '[+] Congratulations!'
                msg = 'Great Shoot, 火车:{} 去登录官网瞅瞅吧!'.format(data['station_train_code'])
                send_email(msg,email)
                return 1
    return 0

"""
	使用 smtp.qq.com 服务器 来发送邮件
"""
def send_email(info,to_addr):
    msg = MIMEText(info, 'html', 'utf-8')

    #输入Email地址和口令 需要自己配置
    from_addr = 'xxxxxx@foxmail.com'  # Email账号
    password = 'xxxxxxx' # POP3 授权码

    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'
    # 输入收件人地址:
    to_addr = to_addr
    msg['From'] = _format_addr(u'抢火车票 小助手 <%s>' % from_addr)
    msg['To'] = _format_addr(u'你好 <%s>' % to_addr)
    msg['Subject'] = Header(u'Hello, 已经成功捕获一只小白兔 ~', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)  # 连接 SMTP服务器 端口
    server.starttls() # 使用SSL加密方式传输数据
    server.set_debuglevel(0)  # 打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password) # 认证  这里的 password 不是QQ邮箱密码开启SMTP服务器后生成的授权码
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

"""
    格式化邮件正文信息
"""
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))
"""
    程序循环入口
"""
def main():
    # 选择座位类型
    select_seat()

    success = False
    # 每个10秒钟发送一个请求查询票源情况
    while not success:
        success = refresh()
        time.sleep(10)

if __name__ == '__main__':
    main()