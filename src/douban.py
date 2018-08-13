# coding: utf-8
import urllib.request
import urllib.error
import urllib.parse
import ssl
import socket
from bs4 import BeautifulSoup
from tools.get_data_from_html import get_img_src_from_html

ssl._create_default_https_context = ssl._create_unverified_context
timeout = 2



# headers信息fannyco
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
       }
# POST请求的信息，填写你的用户名和密码
value = {'source': 'index_nav','form_password': 'test','form_email': 'fannyco@163.com'}

#测试是否需要验证码

data = urllib.parse.urlencode(value).encode('utf8')
request = urllib.request.Request('http://www.douban.com', data=data, headers=headers)
response = urllib.request.urlopen(request)
result = response.read().decode('utf8')
src = get_img_src_from_html(result) #如果有验证码，下载图片并识别
if(src.replace(' ','')!=''):
    urllib.urlretrive(src, )


# 登录操作
try:
    socket.setdefaulttimeout(timeout)
    data = urllib.parse.urlencode(value).encode('utf8')
    request = urllib.request.Request('http://www.douban.com/login', data=data, headers=headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf8')
    print(result)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('error reason:' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('error_code:' + str(e.code))
except socket.timeout:
    print('socket timeout')
else:
    print('request success!')
