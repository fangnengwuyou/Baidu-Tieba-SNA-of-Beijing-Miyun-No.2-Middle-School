# -*- coding = utf-8 -*-
# @Time  :2022/11/22 21:39
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :dataRemaker.py
# @Software: PyCharm
import re

def clean(desstr, restr=''):
    # ่ฟๆปค่กจๆ
    co = re.compile(u'[๐พ ๐ฆ ๐ ๐ ๐ ๐ก ๐ ๐งถ ๐ ๐ ๐ ๐ฅถ ๐ โ ๐ด ๐ค ๐ ๐พ ๐ฒ ๐ ๐ป ๐ ๐ฅฐ โ  ๐ โ ๐ ๐  ๐ ๐ฑ ๐ ๐ ๐ ๐ ๐คถ๐ป ๐ โ ๐พ โค ๐ฝ ๐ง ๐ฅ ๐ฌ ๐ฅ ๐ ๐ฎ ๐ ๐ต ๐ช ๐ ๐ฐ ๐  โญ ๐ ๐ฟ ๐ฅต ๐๐ป โ ๐ ๐ ๐ฆ ๐ฅณ ๐ข ๐ ๐ โฐ ๐ ๐ โ ๐ณ ๐ ๐คณ ๐ ๐ ๐ฅ โ ๐ฆ ๐ง โ  ๐ ๐ ๐ ๐ผ โฅ ๐ ๐]+')

    return co.sub(restr, desstr)
# 1F900โ1F9FF

user_concernNet = eval('['+open('./username/ๅฏไบไบไธญๅงไผๅๅณๆณจๆๅต4486ไบบ.txt', 'r', encoding='UTF-8').read()+']')
# print(len(user_concernNet))

# ๅ ๆต็งฐ็่กจๆ
remake_concernNet = []
for i in range(0, len(user_concernNet)):
    user_concern = []
    for user in user_concernNet[i][1]:
        user_concern.append(clean(user))
    user_list = [user_concernNet[i][0], user_concern]
    remake_concernNet.append(user_list)
#print(remake_concernNet)

tieba_name = 'ๅฏไบไบไธญ'
with open('./username/' + tieba_name + 'ๅงไผๅๅณๆณจๆๅต็ฒ็ญ.txt', 'w', encoding='utf-8') as f:
    f.write(str(remake_concernNet))
    print('ๅๅฅๆๅ')

user_name = []
for i in range(0, len(remake_concernNet)):
    user_name.append(remake_concernNet[i][0])
# print(user_name)
# print(len(user_name))

# ่ฟๆปค้ๅงไผๅๅณๆณจ
inner_concernNet = []
for i in range(0, len(user_name)):
    concern = []
    for user in remake_concernNet[i][1]:
        if user in user_name:
            concern.append(user)
    inner_concern = [remake_concernNet[i][0], concern]
    inner_concernNet.append(inner_concern)

# print(inner_concernNet)
with open('./username/' + tieba_name + 'ๅงไผๅๅณๆณจๆๅต็ป็ญ.txt', 'w', encoding='utf-8') as f:
    f.write(str(inner_concernNet))
    print('ๅๅฅๆๅ')


# ๅๆฏ่ทฏ็บฟ้ๆฉ ๅฏไปฅๅ ้คไบไธๅณๆณจ็็จๆท ๅชไฟ็ๆๅณๆณจๅณ็ณป็่็นๅจๅถไธญ๏ผ็ฎๅๅพๅฝข
user_concernNet = eval(open('./username/ๅฏไบไบไธญๅงไผๅๅณๆณจๆๅต็ป็ญ.txt', 'r', encoding='UTF-8').read())
# print(len(user_concernNet))
new_concernNet = []
# ๅฏนไบ4486ไธชไผๅๆฏไธชไบบๅ ้คไธ่ฟ้่็น(ๅฐ้ๆ)
for i in range(0, len(user_concernNet)):
    # ๅฆๆไปๆฌ่บซๆๅณๆณจ็ไบบ๏ผๅฆๆๅชๆไธไธชๅนถไธไธๆฏไป่ชๅทฑๆฌ่บซ๏ผๅฐฑ่ทณ่ฟ
    if not user_concernNet[i][1]:
        # ็ๅถไปไบบๆๆฒกๆๅฏน่ชๅทฑ็ๅณๆณจ๏ผๅฆๆๆฒกๆๅฐฑๅ ้ค่ฟไธชไบบ
        for j in range(0, len(user_concernNet)):
            # ๆญคๆถๅฆๆๆๅซไบบๅฏน่ชๅทฑ็ๅณๆณจ๏ผๅฐฑไธๅ ้คไบ(ๅๆๅ ้ค๏ผ็ฉบ็ฝๆทปๅ )
            if user_concernNet[i][0] in user_concernNet[j][1]:
                # ๅ ๅฅๆฐ็ฝ็ป
                new_concernNet.append(user_concernNet[i])
                # ่ทณๅบๅฐๅพช็ฏ
                break
    else:
        new_concernNet.append(user_concernNet[i])
print(new_concernNet)
print(len(new_concernNet))
with open('./username/ๅฏไบไบไธญๅงไผๅ็ฒพ็ฎๅณๆณจๆๅต.txt', 'w', encoding='utf-8') as f:
    f.write(str(new_concernNet))
    print('ๅๅฅๆๅ')


