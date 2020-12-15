# -*- coding = utf-8 -*-
# @Time : 2020/12/15-19:54
# @Author: chenying
# @File : shahaiTop50.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt

findStock = re.compile(r'<td>(.*?)</td>')
def main():
    # 1、解析网页内容
    dataList = getData()
    # 保存数据
    savepath = "上证50成分公司信息.xls"
    saveData(dataList, savepath)

def getData():
    dataList = []
    f = open("shahaiTop50.html", "r", encoding='utf-8')
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('table', class_="table search_cfList searchCC"):
        item = str(item)
        stock = re.findall(findStock, item)
        dataList.extend(stock)
    return dataList

def saveData(dataList,savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('上证50Top50公司', cell_overwrite_ok=True)
    for i in range(0, 1):
        sheet.write(0, 0, '上市公司名称')
    for i in range(0, len(dataList)):
        data = dataList[i]
        for j in range(0, 1):
            sheet.write(i + 1, j, data)
    book.save(savepath)

if __name__ == '__main__':
    main()