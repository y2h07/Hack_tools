# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:58:35 2019

@author: lcy
"""

import requests
import time
from bs4 import BeautifulSoup

start = time.time()

def cx(url,csite,head):
    curl = url.format(csite)
    rb = requests.get(curl,head)
    gf = BeautifulSoup(rb.content,'html.parser') #获取内容并以html方式返回
    for x in gf.find_all('p'):
        res = x.get_text()
        print(res)

#设置浏览器头
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
#输入查询域名
csite = input("输入要查询的域名: ")
#查询ip解析记录
print("[+]IP解析记录：")
url = "https://site.ip138.com/{}/"
cx(url,csite,head)
#查询子域名
print("[+]子域名：")
url = "https://site.ip138.com/{}/domain.htm"
cx(url,csite,head)
#查询备案信息
print("[+]备案信息：")
url = "https://site.ip138.com/{}/beian.htm"
cx(url,csite,head)
#查询whois
print("[+]whois：")
url = "https://site.ip138.com/{}/whois.htm"
cx(url,csite,head)
#输出查询时长
end = time.time()
print("查询时间：" , end-start)