# coding=utf-8

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were

<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
# soup = BeautifulSoup(open('index.html'))
#print soup.prettify() # format print
print soup.title
print soup.head
print soup.title.string
print soup.title.parent.name
print soup.a # return first matched string
print soup.p
print type(soup.a) # 2 Attr： name attrs
print soup.a.name   # 获得标签名
print soup.a.attrs # 返回的是一个字典

print soup.p['class'] # 单独获得某一个属性
soup.p['class'] = "newClass" # 修改属性
print soup.p['class'] 

print soup.p.string     #获得标签的内容  类型NavigableString可遍历的字符串
print type(soup.p.string)

print soup.a.string #获得标签的内容  在这是的类型是Comment 注释
print type(soup.a.string) 
# if type(soup.a.string)== bs4.element.Comment:
#     print u'a标签的内容是注释'

# 子节点 .children .contents
# tag 的 .contents 属性可以将tag的子节点以列表的方式输出
print soup.head.contents
print soup.body.contents[1] # 获得第一个子节点
# .children它返回的不是一个 list，不过我们可以通过遍历获取所有子节点
print soup.head.children
for child in soup.head.children:
    print child
