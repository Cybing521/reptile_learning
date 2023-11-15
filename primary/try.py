import requests

headers={'User-Agent':'Mozilla/5.0 (L'
         'inux; Android 6.0; Nexus 5 Build/MRA58N)' 
         'AppleWebKit/537.36 (KHTML, like Gecko) Chro'
         'me/118.0.0.0 Mobile Safari/537.36 Edg/118.0.2088.76'}

# r=requests.get('https://www.baidu.com/',headers=headers)
# print(r.status_code)
# print(r.text) #显示源码

data={'user':'abc','password':'123'}
r=requests.post('https://www.weibo.com',data=data,headers=headers)
