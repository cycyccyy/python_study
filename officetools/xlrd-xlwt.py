# -*- coding = utf-8 -*-
# @Time : 2020/12/10-20:07
# @Author: chenying
# @File : xlrd-xlwt.py
# @Software: PyCharm

import xlrd
import xlwt

# 读取excel表格具体单元格的值
# 1、打开一个表格文件
# 2、获取sheet 通过索引或者sheetname读取
# 3、读取单元格的值   多种方式读取指定的单元格值
xlxs = xlrd.open_workbook("xlrd-test.xlsx")
# table = xlxs.sheet_by_index(0)
table = xlxs.sheet_by_name('学生信息表')
print(table.cell_value(0, 0))
print(table.cell(0, 0).value)
print(table.row(0)[0].value)

# 向工作簿中写入数据
# 1、新建一个工作簿
# 2、向工作簿中新建一个sheet
# 3、向表格中指定单元格加入数据
# 4、保存工作簿到指定路径

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test写入')
worksheet.write(0, 0, 'test')
workbook.save('test写入.xlsx')
