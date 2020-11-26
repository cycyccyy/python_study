# -*- coding = utf-8 -*-
# @Time : 2020/10/27 上午11:01
# @Author: chenying
# @File: testBs4.py
# @Software:PyCharm

'''
BeautifulSoup4将复杂的html文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：

- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup

file = open("./baidu.html")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# print(type(bs.title))
# # 1. Tag 标签及其内容：拿到它所找到的第一个内容
# print((bs.title.string))
# print(type(bs.title.string))
# # 2. NavigableString 标签里面的内容
# print(bs.a.attrs)
# print(type(bs))
# # 3.BeautifulSoup 整个文档
# print(bs.a.string)
# print(type(bs.a.string))
# 4.Comment 这是一个特殊的NavigableString，输出的内容不包含注释符号

# 文档的搜索
'''
#1、find_all()
# t_list=bs.find_all("a")
# print(t_list)
'''

'''
#2、正则表达式搜索
import re
t_list=bs.find_all(re.compile("a"))
print(t_list)
'''

'''
#3、传入函数或方法，根据函数的要求搜索
def name_is_exists(tag):
    return tag.has_attr("name")

t_title=bs.find_all(name_is_exists)
print(t_title)
'''

'''
#4、kwargs 参数
# t_title=bs.find_all(id="head")
t_title=bs.find_all(class_=True)
for item in t_title:
    print(item)
'''

'''
#5、text参数
import re
# t_title=bs.find_all(text="hao123")
# t_title=bs.find_all(text=["hao123","地图","贴吧"])

t_title=bs.find_all(text=re.compile("\d"))    # 运用正则表达式找包含特殊文本的内容（标签里面的数字)
for item in t_title:
    print(item)
'''

'''
#6、limit参数
t_title=bs.find_all("a",limit=2)
print(t_title)
'''

'''
# 7、css选择器
 t_title=bs.select('title')    #通过标签来查找
 t_title=bs.select(".mnav")    #通过类名来查找
 t_title=bs.select("#u1")      #通过id来查找
 t_title = bs.select("a[class='toindex']")    #通过属性来查找
 t_title = bs.select("head > meta")  # 查找标签里面的标签
 for item in t_title:
     print(item)
t_title=bs.select(".s-top-nav ~ .s-center-box")   #通过兄弟节点查找文本
print(t_title[0].get_text())
'''

