# -*- coding = utf-8 -*-
# @Time  :2022/11/20 19:29
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :crawlMemberPage.py
# @Software: PyCharm
from readMemberPage import readPage
from writeMemberPage import writePage


def crawlPage(baseurl, begin, end):
    for pn in range(begin, end + 1):
        url = baseurl + '&pn=' + str(pn)

        # 调用函数
        html = readPage(url)
        filename = '第' + str(pn) + '页.html'
        writePage(filename, html)


