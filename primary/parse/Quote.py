from urllib.parse import quote,unquote
keyword='傻逼'
url='https://www.baidu.com/s?wd='+quote(keyword)
print(url)

url='https://www.baidu.com/s?wd=%E5%82%BB%E9%80%BC'
print(unquote(url))