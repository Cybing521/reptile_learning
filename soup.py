import requests
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
# 选用lxml解析器来解析
soup = BeautifulSoup(html, 'lxml')

#获取标题
print(soup.title)

#获取标题文本
print(soup.title.text)

#通过标签定位
print(soup.find_all('a'))

#通过属性定位
print(soup.find_all(attrs={'id':'link2'}))

#标签加属性定位

print(soup.find_all('a',id='link1'))

print("--------")
print(soup.find_all(attrs={'class':"sister",'id':'link2'}))
