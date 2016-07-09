

__author__ = 'anka9080'

from termcolor import colored

print colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print colored('Hello, World!', 'green', 'on_red')

red_on_cyan = lambda x: colored(x, 'red', 'on_cyan')
print red_on_cyan('Hello, World!')
print red_on_cyan('Hello, Universe!')