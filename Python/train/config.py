#coding:utf-8

TYPE_MAP = {
	'1':'普快',
	'2':'空调普慢',
	'3':'普慢',
	'4':'直达特快',
	'5':'空调普快',
	'6':'空调快速',
	'7':'特快',
	'8':'空调特快',
	'9':'快速',
	'10':'动车组',
	'11':'城际高速',
	'12':'高速动车'
}

HEADERS = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
}

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_DBS = 'train_db' 
MYSQL_USER = 'thisisuaer'
MYSQL_PASS = 'thisispass'
MYSQL_CHARSET = 'utf8'