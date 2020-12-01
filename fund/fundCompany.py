# -*- coding = utf-8 -*-
# @Time : 2020/11/26 上午11:56
# @Author: chenying
# @File: fundCompany.py
# @Software:PyCharm
# @Desciption: 爬取天天基金网站基金公司相关数据


from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import xlwt


def main():
    # 1、获取网页
    baseurl = " http://fund.eastmoney.com/company/default.html"
    # 2、解析网页内容
    dataList = getData(baseurl)
    # 保存数据
    savepath = "fund/基金公司.xls"
    saveData(dataList, savepath)


findTbody = re.compile(r'<tr>(.*)</tr>')
findNum = re.compile(r'<td class="sno width50">(.*?)</td>')
findCompany = re.compile(r'<td class="td-align-left" .*">(.*?)</a></td>')
findCompanyDate = re.compile(r'<td>(\d{4}-\d{1,2}-\d{1,2})</td>')
findScale = re.compile(r'<td class="scale number" data-sortvalue="(.*?)">')
findLink = re.compile(r'<a class="ttjj-link" href="(.*?)">详情</a>')


def getData(url):
    dataList = []
    companyCode = []
    html = parseUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('div', id="companyTable"):
        item = str(item)
        company = re.findall(findCompany, item)

        companyDate = re.findall(findCompanyDate, item)
        companyScale = re.findall(findScale, item)
        companyLink = re.findall(findLink, item)
    for link in companyLink:
        code = re.findall("\d+", link)
        companyCode.append(code)

    for (c, e, d, s, l) in zip(company, companyCode, companyDate, companyScale, companyLink):
        data = []
        data.append(c)
        data.append(e[0])
        data.append(d)
        data.append(s)
        data.append(l)
        dataList.append(data)
    return dataList


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
    sheet = book.add_sheet('基金公司相关信息', cell_overwrite_ok=True)
    col = ('基金公司', '基金公司代码', '成立日期', '基金规模', '详情')
    for i in range(0, 5):
        sheet.write(0, i, col[i])
    for i in range(0, len(dataList)):
        data = dataList[i]
        for j in range(0, 5):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


if __name__ == '__main__':
    main()
