# -*- coding = utf-8 -*-
# @Time  :2022/11/20 19:18
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :main.py
# @Software: PyCharm
from old.usernameDig import crawlMemberPage

if __name__ == "__main__":
    name = "密云二中"
    MemberUrl = "https://tieba.baidu.com/bawu2/platform/listMemberInfo?word=%E5%AF%86%E4%BA%91%E4%BA%8C%E4%B8%AD&ie=utf-8"
    begin = 1
    end = 187
    # crawlPage(MemberUrl, begin, end)
    username_list = crawlMemberPage(begin, end)
    for username in username_list:
        username[0]

    # writeUsername(name, str(username_list))
    username_list



    # print(username_list)
    # userNumber=len(username_list)
    # print(userNumber)
    # for i in range(0, userNumber):
    #     if username_list[i]=='方能无忧':
    #         print(i/24)


