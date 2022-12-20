# -*- coding = utf-8 -*-
# @Time  :2022/11/20 19:28
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :writeMemberPage.py
# @Software: PyCharm

# 写入文件
def writePage(filename, html):
    with open('./page/'+filename, 'w', encoding='utf-8') as f:
        f.write(html)
        print('写入成功')
