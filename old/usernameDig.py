# -*- coding = utf-8 -*-
# @Time  :2022/11/20 20:03
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :usernameDig.py
# @Software: PyCharm
from bs4 import BeautifulSoup


def crawlMemberPage(begin, end):
    username_list = []
    begin = 1
    end = 187
    for i in range(begin, end+1):
        html = open('./page/第'+str(i)+'页.html', 'r', encoding='UTF-8')
        soup = BeautifulSoup(html, 'html.parser')
        # 返回的username是个列表
        username = soup.find_all("a", class_="user_name")
        for user in username:
            # 三列数据 主页链接 用户名 昵称 主页链接 用元组表示
            username_tuple =(user['title'], user.text, user['href'])
            username_list.append(username_tuple)
    return username_list

