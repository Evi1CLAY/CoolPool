# coding: utf-8
# author:   anka9080
# datetime: 20160410

asciis = ['97','98','99']
words = []

""" 读入文本文件中的 ascii 码，然后格式化输出解码后的文本 """
def ascii2word(filename):
	# a_int = ord('a')
	# a_chr = chr(97)
	words = ''
	with open(filename) as input:
		asciis_str = input.read()
	input.close()
	# print asciis_str
	# 102 111 114 40 32 100 97 121 32 61 32 116 104 101 32 100 97 121 32 119 
	# 101 32 119 101 114 101 32 116 111 103 101 116 104 101 114 59 32 100 97 
	# 121 32 60 61 32 102 111 114 101 118 101 114 59 32 100 97 121 32 43 43 41
	# 10 123 10 9 79 117 114 32 76 111 118 101 32 43 43 59 10 125
	asciis_list = asciis_str.split(' ')
	print len(asciis_list)
	for x in asciis_list:
		words += chr(int(x))
		# print chr(int(x)),
	print words

def test():
	words = ''
	list = [110,98,100]
	for x in list:
		words = words +  chr(x)

	print words
def word2ascii(filename):
	with open(filename) as input:
		words = input.readlines()
	input.close()
	# print words   
	# 输出结果是字符列表
	# ['for( day = the day we were together; day <= forever; day ++)\n', '{\n', '\tOur Love ++;\n', '}']
	count = 0
	for line in words:
		for letter in line:
			print ord(letter),
			count += 1
	print '\ncount: ',count



if __name__ == '__main__':
	# ascii2word(asciis)
	word2ascii('raw.txt')
	# ascii2word('secret.txt')
	# test()




