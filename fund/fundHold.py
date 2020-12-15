# -*- coding = utf-8 -*-
# @Time : 2020/12/12-9:57
# @Author: chenying
# @File : fundHold.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt


def main():
    # 1、获取网页
    baseurl = "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code=001938&topline=10&year=&month=&rt=0.7946864204714235"
    # http: // fundf10.eastmoney.com / FundArchivesDatas.aspx?type = jjcc & code = 001
    # 938 & topline = 10 & year = 2019 & month = & rt = 0.021929859675946295
    # 2、解析网页内容
    dataList = getData(baseurl)
    # 保存数据
    savepath = "fund/基金公司.xls"
    # saveData(dataList, savepath)


def getData(url):
    html = parseUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('div', id="cctable"):
        print(item)
        item = str(item)


def parseUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError  as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    print(html)
    return html


if __name__ == '__main__':
    main()
