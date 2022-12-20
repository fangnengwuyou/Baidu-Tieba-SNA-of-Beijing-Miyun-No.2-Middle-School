# -*- coding = utf-8 -*-
# @Time  :2022/11/26 18:17
# @Author:FangNengWuYou
# @Site  :BUPT
# @File  :matrixBuilder.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import openpyxl


# 建立矩阵(二维列表)
user_concernNet = eval(open('./username/密云二中吧会员精简关注情况.txt', 'r', encoding='UTF-8').read())
# 顶点集
node = []
for i in range(0, len(user_concernNet)):
    node.append(user_concernNet[i][0])
print(node)
# 邻接矩阵
matrix = np.zeros((len(user_concernNet), len(user_concernNet)), dtype='int8')

print(matrix[0][0])
for i in range(0, len(user_concernNet)):
    for j in range(0, len(user_concernNet)):
        if user_concernNet[i][0] in user_concernNet[j][1]:
            matrix[i][j] = 1
print(matrix)

np.savetxt("./username/密云二中吧会员精简关注情况邻接矩阵.txt", matrix)

data_df = pd.DataFrame(matrix)
data_df.columns = node
data_df.index = node
writer = pd.ExcelWriter('./username/密云二中吧会员精简关注情况邻接矩阵.xlsx')  # 创建名称为test的excel表格
data_df.to_excel(writer, 'page_1',
                 float_format='%d')  # float_format 精度，将data_df写到test表格的第一页中。若多个文件，可以在page_2中写入
writer.save()  # 保存
