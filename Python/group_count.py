# coding: utf-8
# author: anka9080
# date  : 20160408
# 合并计数小脚本
# 输入
# abc
# aaa
# abc
# 输出
# abc 2
# aaa 1

def group_count():
	title_count_list = []
	title_list = []
	count_list =  []
	dict = {}
	with open('0418.txt') as input:
		for x in input.readlines():
			list = x.rstrip().split('&&')
			if list[0] not in dict:
				print list[1]
				dict[list[0]] = int(list[1])
			else:
				print list[1]
				dict[list[0]] += int(list[1])
			# print list
	with open('0418_res.txt','w') as output:
	# print len(dict)
		for x in dict:
			output.write(x + '&&' + str(dict[x]) + '\n')
if __name__ == '__main__':
	group_count()