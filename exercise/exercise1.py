#获取17173新游频道下游戏名

import requests
from bs4 import BeautifulSoup

# 页面url地址
url = 'http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-1-2.html'

r=requests.get(url)

soup=BeautifulSoup(r.text,'lxml')

info_list=soup.find_all(attrs={'class':'ptlist ptlist-pc'})

tit_list=info_list[0].find_all(attrs={'class':'tit'})
for title in tit_list:
    # print(title.text.replace('\n',' '))
    a_tag=title.find('a')
    if a_tag:
        print(a_tag.text.replace('\n',' '))
