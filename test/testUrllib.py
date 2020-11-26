# -*- coding = utf-8 -*-
# @Time : 2020/10/26 下午4:56
# @Author: chenying
# @File: testUrllib.py
# @Software:PyCharm

# 补充urllib知识
'''
import urllib.request

# 获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")
f = open('baidu.html', 'w')
f.write(response.read().decode('utf-8'))
f.close
'''

'''
# 获取一个post请求
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
'''

'''
import urllib.request

try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out")
'''

'''
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
print(response.getheaders())
'''

'''
import urllib.request
import urllib.parse

url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
request = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response =urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
'''

import urllib.request
import urllib.parse

url = "http://www.douban.com"
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
request = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response =urllib.request.urlopen(request)
f=open("douban.html","w")
f.write(response.read().decode('utf-8'))
f.close()


