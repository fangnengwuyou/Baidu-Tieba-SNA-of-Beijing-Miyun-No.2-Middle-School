# -*- coding = utf-8 -*-
# @Time  :2022/11/20 22:29
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :readPersonPage.py
# @Software: PyCharm
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import math


tieba_name = '密云二中'
username_tuple_list = eval(open('./username/密云二中吧会员.txt', 'r', encoding='UTF-8').read())
# 初始自动登录chrome模拟器
cookies = eval(open('cookies.txt', 'r', encoding='UTF-8').read())
driver = webdriver.Chrome()
driver.get('https://tieba.baidu.com/')
driver.delete_all_cookies()
for cookie in cookies:
    cookie_dict = {
        'domain': '.baidu.com',
        'name': cookie.get('name'),
        'value': cookie.get('value'),
        "expires": cookie.get('value'),
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
    driver.add_cookie(cookie_dict)
driver.refresh()


# 密云二中吧循环4486人集合
for k in range(0, len(username_tuple_list)):
    username_tuple = username_tuple_list[k]
    username = username_tuple[1]
    homepage = username_tuple[2]
    url = "https://tieba.baidu.com" + homepage
    driver.get(url)
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    concern = soup.find_all("span", class_="concern_num")
    concernNet = []
    # 如果收集到了链接
    if concern:
        # 查看每一条收集到的链接是不是关注链接
        for user in concern:
            content = user.find('a')['href']
            if re.match("/home/concern", content):
                # 如果匹配到了就是关注(常规流程)
                # 关注链接
                concernLink = content[16: -8]
                # 爬取关注页链接 关注人数 关注页数
                concernNum = user.find('a').text
                page = math.ceil(eval(concernNum) / 20)
                # 爬取他/她关注的人的数据 (将来会有关注他的人)
                concernNet = []
                # 他本人放在第一个 之后是他关注的人
                for pn in range(1, page + 1):
                    url = "https://tieba.baidu.com/i/i/concern?u" + concernLink + '&pn=' + str(pn)
                    driver.get(url)
                    data = driver.page_source
                    soup = BeautifulSoup(data, 'html.parser')
                    concern = soup.find_all('span', class_='name')
                    for i in range(0, len(concern)):
                        concernUser = concern[i].text
                        concernNet.append(concernUser)
                # 匹配到一个就break，不尽兴第二次匹配
                break
    # 建立用户网络列表
    userNet = [username, concernNet]
    print(k)
    print(userNet)
    with open('./username/' + tieba_name + '吧会员关注情况.txt', 'a', encoding='utf-8') as f:
        f.write(str(userNet) + ',')
        print('写入成功')
driver.close()
