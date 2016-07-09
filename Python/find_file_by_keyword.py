#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# anka9080
# 输入关键词 和 文件夹地址
# 程序遍历文件夹中的文件
# 输出包含关键词的所有文本文件名称
# 可以指定搜索的文件类型

import os,sys
from optparse import OptionParser

class GetFile(): #  遍历得到根文件夹所有文件和文件夹

    startDir = ''# 起始文件夹
    keyword = ''

    def __init__(self):
        global options
        self.startDir = options.directory
        self.keyword = options.keyword

    def iterateDir(self):

        # os.walk() 用于得到文件夹父目录，它所包含的所有文件夹，以及所包含的所有文件
        for parent,dirnames,filenames in os.walk(self.startDir):
            # for dirname in dirnames:
            #     print '[+] dirname :' + os.path.join(parent,dirname)
            # print '++++'
            for filename in filenames:
                if filename.endswith('.py') or filename.endswith('.py~'):
                    absName = os.path.join(parent,filename)
                    input = open(absName,'r').read() # 搜索该文本中有木有要找的关键字
                    global options
                    if options.keyword != '':  # 判断keyword是否为空
                        if options.ignore.upper() == 'TRUE' :
                            if self.keyword.upper() in input.upper():
                                print ' [-] filename :' + absName # 打印匹配的文件名
                        else:
                            if self.keyword in input :
                                print ' [-] filename :' + absName # 打印匹配的文件名
                    else:
                        print ' [-] filename :' + absName # 打印所有文件的名字

def usage():
    parser = OptionParser()
    parser.add_option('-d',dest = 'directory',default ='./',help = 'set the start directory,default ./') # 搜索的起始目录
    parser.add_option('-k',dest = 'keyword', default = '',help = 'the keyword you want to find') # 想要搜索的关键字
    parser.add_option('-i',dest = 'ignore',default = 'True',help = 'ignore case,default True') # 忽略大小写
    global options
    (options, args) = parser.parse_args()

if __name__ == '__main__':
    usage()

    gt = GetFile()
    gt.iterateDir()


