# -*- coding = utf-8 -*-
# @Time  :2022/11/20 21:42
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :writeUsername.py
# @Software: PyCharm
def writeUsername(name, username):
    with open('./username/'+name+'吧成员昵称.txt', 'w', encoding='utf-8') as f:
        f.write(username)
        print('写入成功')
