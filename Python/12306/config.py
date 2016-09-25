# coding: utf-8

# 配置文件 ----------------------------------------------------------------

# 点击查询时按钮发送的请求 URL (浏览器 F12 查看 network 选项卡 能看到这个请求)
url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-10-06&from_station=OXH&to_station=HFH'

# 期望刷到的火车编号
trains = ['G3245','G105']

# 期望刷到的座位类型
# 从 ['二等座','硬卧','硬座'] 中选一个填写
seat_type = '二等座'

# 刷到火车票洪接收通知的邮件账户，成功后会向该账户发送一封提示邮件
email = 'anka9080@foxmail.com'

