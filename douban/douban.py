# -*- coding = utf-8 -*-
# @Time : 2020/10/26 下午4:19
# @Author: chenying
# @File: douban.py
# @Software:PyCharm


from bs4 import BeautifulSoup  # 网页解析,获取数据
import re  # 正则表达式,进行文字匹配
import urllib.request, urllib.error, urllib.parse  # 指定URL,获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite3数据库操作


# 爬取豆瓣top250电影并处理
def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    dataList = getData(baseurl)
    savepath = "douban/豆瓣电影Top250.xls"
    saveData(dataList, savepath)


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，匹配电影链接
findImage = re.compile(r'<img.*src="(.*?)"', re.S)  # 匹配图片地址  re.S忽略换行符
findName = re.compile(r'<span class="title">(.*)</span>')  # 匹配电影名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findRatingNUm = re.compile(r'<span>(\d*)人评价</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
        # 2、逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            image = re.findall(findImage, item)[0]
            data.append(image)
            name = re.findall(findName, item)
            if (len(name) == 2):
                cname = name[0]
                data.append(cname)
                oname = name[1].replace('/', "")
                oname = oname.replace('\xa0', "")
                data.append(oname)
            else:
                cname = re.findall(findName, item)[0]
                data.append(cname)
                oname = ''
                data.append(oname)
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', '')
                data.append(inq)
            else:
                data.append(" ")
            ratingNum = re.findall(findRatingNUm, item)[0]
            data.append(ratingNum)
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br>
            bd = re.sub('/', " ", bd)  # 去掉/
            bd = re.sub('\xa0', " ", bd)
            data.append(bd.strip())
            dataList.append(data)
    return dataList


# 得到指定的一个url网页内容
def askUrl(url):
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


# 保存数据
def saveData(dataList, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ('电影链接', '电影图片', '影片中文名', '影片外文名', '评分', '评价数', '概述', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


if __name__ == "__main__":
    main()
