# -*- coding = utf-8 -*-
# @Time : 2020/11/26 上午11:56
# @Author: chenying
# @File: fundCompany.py
# @Software:PyCharm
# @Description: 爬取天天基金网站各个基金公司基金的信息


from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt


def main():
    # 1、获取网页
    baseurl = " http://fund.eastmoney.com/company/default.html"
    # 2、解析网页内容获取基金公司链接id
    dataList = getCompanyLink(baseurl)
    # 3、循环爬取基金公司的基金信息
    companyurl = "http://fund.eastmoney.com/Company/home/KFSFundRank?gsid="
    resultList = getFundInfo(companyurl, dataList)
    # # 保存数据
    savepath = "基金公司代码.xls"
    saveData(resultList, savepath)


findLink = re.compile(r'<a class="ttjj-link" href="(.*?)">详情</a>')
findFundName = re.compile(r'<a class="name" .*?>(.*?)</a>')
findFundLink = re.compile(r'<a class="name" href="(.*?)" .*?>.*?</a>')
findFundCode = re.compile(r'<a class="code" .*?>(\d*)</a>')
findFundType = re.compile(r'<td>([\u4e00-\u9fa5]*)</td>')


def getCompanyLink(url):
    dataList = []
    html = parseUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('div', id="companyTable"):
        item = str(item)
        companyLink = re.findall(findLink, item)
    for c in companyLink:
        dataList.append(re.findall(r"\d+?\d*", c))
    return dataList


def parseFundInfo(url, id):
    dataList = []
    html = parseUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('table', class_="ttjj-table"):
        item = str(item)
        fundName = re.findall(findFundName, item)
        fundCode = re.findall(findFundCode, item)
        fundLink = re.findall(findFundLink, item)
        fundType = re.findall(findFundType, item)
        for (name, code, t, l) in zip(fundName, fundCode, fundType, fundLink):
            data = []
            data.append(name)
            data.append(code)
            data.append(t)
            data.append(l)
            data.append(id)
            dataList.append(data)
        print('list', dataList)
        return dataList


def getFundInfo(companyurl, dataList):
    # resultList = []
    savepath = "基金公司代码.xls"
    list = parseFundInfo('http://fund.eastmoney.com/Company/home/KFSFundRank?gsid=80041198', 80041198)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('基金公司代码信息', cell_overwrite_ok=True)
    col = ('基金名称', '基金代码', '基金类型', '基金详情', '所属基金公司')
    for i in range(0, 5):
        sheet.write(0, i, col[i])
    print('list',type())
    # for m in range(0, len(list)):
    #     print('m',m)
    #     # for k in range(0, len(m)):
    #     #     sheet.write(m + 1, k, m[k])

    book.save(savepath)
        # for j in range(0, 5):
        #     sheet.write(m + 1, j, list[])

    # for data in dataList:
    #     resultList.append(data[0])
    # for data in resultList:
    #     url = companyurl + data
    #     list = parseFundInfo(url, data)
    #     resultList.append(list)
    # return resultList


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
    return html


def saveData(dataList, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('基金公司代码信息', cell_overwrite_ok=True)
    col = ('基金名称', '基金代码', '基金类型', '基金详情', '所属基金公司')
    for i in range(0, 5):
        sheet.write(0, i, col[i])
    for i in range(0, len(dataList)):
        data = dataList[i]
        print('data', data)
        for m in range(0, len(data)):
            print('数据', data[m])
            for j in range(0, 5):
                sheet.write(m + 1, j, data[m][j])
    book.save(savepath)


if __name__ == '__main__':
    main()
