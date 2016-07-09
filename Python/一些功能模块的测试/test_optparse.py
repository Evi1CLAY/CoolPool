#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option('-d',dest = 'directory',help = 'Directory name')
parser.add_option('-f',dest = 'ffff',help = '')
(options,args) = parser.parse_args()

print sys.argv[1]
print options.directory
if not options.ffff:
    print 'ffff is not set!'
    parser.print_help()

print 'Over'
