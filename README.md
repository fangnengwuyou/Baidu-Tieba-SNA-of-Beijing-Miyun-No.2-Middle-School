# Baidu-Tieba-SNA-of-Beijing-Miyun-No.2-Middle-School
本项目针对百度贴吧中密云二中吧用户关注网络的社会网络分析
## 简介

## 模型
节点：会员\
边缘：单向关注\
有向图\
无权图

## 环境
python3.8

## 软件
PyCharm 2022.2.4\
Gephi

## 架构
cookies.txt：个人百度贴吧cookie\
dataRemaker.py matrixBuilder.py readNumberPage.py readPersonPage.py：百度贴吧关注数据爬取代码\
main.py：主函数，但不使用

## 输出
密云二中吧会员关注图.gephi：Gephi社会网络项目文件\
密云二中吧会员关注图输出.png：4096×4096像素图输出\
密云二中吧会员精简关注情况邻接矩阵.xlsx：数据邻接矩阵\
作者本人所在集群.png：作者本人(方能无忧)所处狭小关系网络\
贴吧关注网络分析-齐勇-2019210637.pptx: 汇报幻灯片

## 分析
节点个数:713\
边缘条数:1505\
平均度：2.111\
平均路径长度：5.309\
网络直径:14\
图密度:0.003\
连通分量：71个弱连通分量，404个强连通分量,最大连通分量尺寸超过500\
平均聚类系数：0.076\





