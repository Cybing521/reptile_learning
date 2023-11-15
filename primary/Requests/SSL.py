import requests
from requests.packages import urllib3
import logging

# response = requests.get('https://ssr2.scrape.center/')
# print(response.status_code)


#忽略证书，直接进行
response = requests.get('https://ssr2.scrape.center/',verify=False)
print(response.status_code)

#设置忽略方式1 
urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)

#设置忽略方式2

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/', verify=False)
print(response.status_code)