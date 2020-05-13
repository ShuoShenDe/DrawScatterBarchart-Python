# library &amp; dataset
import seaborn as sns
import matplotlib.pyplot as plt
import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from intoMongo import connectDB
import re

def pricearea():
    # 连接数据库
    data=connectDB()

    data['price'] = data['price'].astype(int)
    def areachange(x):
        area=re.findall("\d+",str(x))
        return int(area[0])   #
    data['area'] = data['area'].apply(areachange)
    price= data.groupby('area').mean()
    price.sort_values(by=['area'])
    return price

def pricetype():
    # 连接数据库
    data=connectDB()
    data.filter(like='合租')
    print(data)
    data['price'] = data['price'].astype(int)
    price= data.groupby(by=data['type']).mean()
    return price

def barchart(data,xlabel,ylabel):
    # 处理中文问题
    # plt.rcParams['font.family'] = ['Arial Unicode MS']
    plt.figure(figsize=(15, 10))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    print(data)
    area= data.index
    price = data['price']
    #y_pos = np.arange(len(area))
    plt.bar(area, price, color=(0.2, 0.4, 0.6, 0.6))
    # Custom Axis title
    plt.xlabel(xlabel, fontweight='bold', color='orange', fontsize='17', horizontalalignment='center')
    plt.ylabel(ylabel, fontweight='bold', color='orange', fontsize='17', horizontalalignment='center')
    plt.show()

if __name__ == "__main__":

    #价格和面积的柱状图
    data=pricearea()


    xlabel='面积'
    ylabel="平均价格"
    barchart(data,xlabel,ylabel)
    # 合租房源的人均价格柱状图
    # data2=pricetype()
    # xlabel = '合租类型'
    # ylabel = "人均价格"
    # barchart(data2,xlabel,ylabel)
