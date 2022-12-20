# -*- coding = utf-8 -*-
# @Time  :2022/11/21 22:54
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :readNumberPage.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from selenium import webdriver

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

user_list = []
tieba_name = '密云二中'
tieba_home_url = 'https://tieba.baidu.com/f?kw=' + tieba_name

begin = 1
end = 187
for pn in range(begin, end + 1):
    tieba_Num_url = 'https://tieba.baidu.com/bawu2/platform/listMemberInfo?word=' + tieba_name + '&ie=utf-8&pn=' + str(pn)
    driver.get(tieba_Num_url)
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')

    # 返回的username是个列表
    user = soup.find_all('a', class_="user_name")
    for i in range(0, len(user)):
        # 三列数据 主页链接 用户名 昵称 主页链接 用元组表示
        user_tuple = (user[i]['title'], user[i].text, user[i]['href'])
        user_list.append(user_tuple)

with open('./username/' + tieba_name + '吧会员.txt', 'w', encoding='utf-8') as f:
    f.write(str(user_list))
    print('写入成功')
print(user_list)
