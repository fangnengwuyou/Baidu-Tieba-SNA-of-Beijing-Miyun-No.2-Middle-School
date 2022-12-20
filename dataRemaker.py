# -*- coding = utf-8 -*-
# @Time  :2022/11/22 21:39
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :dataRemaker.py
# @Software: PyCharm
import re

def clean(desstr, restr=''):
    # 过滤表情
    co = re.compile(u'[🐾 🦅 👉 🔅 💐 🍡 💃 🧶 🍃 👑 🌕 🥶 👅 ✌ 👴 🤗 🍓 👾 🌲 👍 🏻 🐟 🥰 ⚠ 🎈 ✈ 🍎 🌠 😋 🐱 🍅 💜 🏀 🍋 🤶🏻 🍙 ✔ 🎾 ❤ 🐽 🍧 🍥 🍬 😥 🔒 🍮 😊 🏵 🌪 😀 🐰 🐠 ⭕ 🏙 👿 🥵 🙅🏻 ☀ 🙃 🍇 🦁 🥳 🐢 💈 🙄 ⛰ 🌏 🙂 ⛈ 🐳 🐉 🤳 🐔 📖 🥜 ☕ 🦋 🚧 ☠ 👊 😅 🍊 🏼 ♥ 😃 💗]+')

    return co.sub(restr, desstr)
# 1F900—1F9FF

user_concernNet = eval('['+open('./username/密云二中吧会员关注情况4486人.txt', 'r', encoding='UTF-8').read()+']')
# print(len(user_concernNet))

# 删昵称的表情
remake_concernNet = []
for i in range(0, len(user_concernNet)):
    user_concern = []
    for user in user_concernNet[i][1]:
        user_concern.append(clean(user))
    user_list = [user_concernNet[i][0], user_concern]
    remake_concernNet.append(user_list)
#print(remake_concernNet)

tieba_name = '密云二中'
with open('./username/' + tieba_name + '吧会员关注情况粗筛.txt', 'w', encoding='utf-8') as f:
    f.write(str(remake_concernNet))
    print('写入成功')

user_name = []
for i in range(0, len(remake_concernNet)):
    user_name.append(remake_concernNet[i][0])
# print(user_name)
# print(len(user_name))

# 过滤非吧会员关注
inner_concernNet = []
for i in range(0, len(user_name)):
    concern = []
    for user in remake_concernNet[i][1]:
        if user in user_name:
            concern.append(user)
    inner_concern = [remake_concernNet[i][0], concern]
    inner_concernNet.append(inner_concern)

# print(inner_concernNet)
with open('./username/' + tieba_name + '吧会员关注情况细筛.txt', 'w', encoding='utf-8') as f:
    f.write(str(inner_concernNet))
    print('写入成功')


# 分支路线选择 可以删除互不关注的用户 只保留有关注关系的节点在其中，简化图形
user_concernNet = eval(open('./username/密云二中吧会员关注情况细筛.txt', 'r', encoding='UTF-8').read())
# print(len(user_concernNet))
new_concernNet = []
# 对于4486个会员每个人删除不连通节点(小透明)
for i in range(0, len(user_concernNet)):
    # 如果他本身有关注的人，如果只有一个并且不是他自己本身，就跳过
    if not user_concernNet[i][1]:
        # 看其他人有没有对自己的关注，如果没有就删除这个人
        for j in range(0, len(user_concernNet)):
            # 此时如果有别人对自己的关注，就不删除了(原有删除＝空白添加)
            if user_concernNet[i][0] in user_concernNet[j][1]:
                # 加入新网络
                new_concernNet.append(user_concernNet[i])
                # 跳出小循环
                break
    else:
        new_concernNet.append(user_concernNet[i])
print(new_concernNet)
print(len(new_concernNet))
with open('./username/密云二中吧会员精简关注情况.txt', 'w', encoding='utf-8') as f:
    f.write(str(new_concernNet))
    print('写入成功')


