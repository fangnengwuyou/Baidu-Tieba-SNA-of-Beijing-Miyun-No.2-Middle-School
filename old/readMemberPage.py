# -*- coding = utf-8 -*-
# @Time  :2022/11/20 19:26
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :readMemberPage.py
# @Software: PyCharm
import urllib.request


def readPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    # 发起请求
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('gbk')
    return html
