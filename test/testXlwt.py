# -*- coding = utf-8 -*-
# @Time : 2020/11/26 上午11:36
# @Author: chenying
# @File: testXlwt.py
# @Software:PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')
workbook.save('hello.xls')