# coding: utf-8
# author: anka9080
# date  : 20160408
# 去重小脚本
def deduplication():
	list1 = []  #  总文件列表
	list2 = []  #  去重参数列表
	list3 = []  #  去重后的文件列表
	with open('1.txt') as f1:
		for i in f1.readlines():
			list1.append(i.rstrip())

	with open('2.txt') as f2:
		for i in f2.readlines():
			list2.append(i.rstrip())

	for i in list1:
		if i not in list2:
			list3.append(i)

	with open('3.txt','w') as f3:
		for i in list3:
			f3.write(i + '\n')

if __name__ == '__main__':
	deduplication()
