import requests
#保持对话
#新建一个session对话
sess= requests.session()
#先完成登录
data={'user':'abc','password':123}

headers={'User-Agent':'Mozilla/5.0 (L'
         'inux; Android 6.0; Nexus 5 Build/MRA58N)' 
         'AppleWebKit/537.36 (KHTML, like Gecko) Chro'
         'me/118.0.0.0 Mobile Safari/537.36 Edg/118.0.2088.76'}

sess.post('https://www.baidu.com',data=data,headers=headers)
#在这个会话下去访问其他的网址
b=sess.get('https://www.weibo.com')