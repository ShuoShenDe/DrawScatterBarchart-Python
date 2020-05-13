# library &amp; dataset

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
from intoMongo import connectDB

def pricearea():
    # 连接数据库
    data = connectDB()

    def areachange(x):
        area=re.findall(r"\d+\.?\d*",str(x))
        return int(area[0])
    data['area'] = data['area'].apply(areachange)
    data['price'] = data['price'].astype(int)
    return data


def Scatter(data):
    sns.set(font='SimHei')  # 解决Seaborn中文显示问题
    # Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
    # s = sns.jointplot(x=data["area"], y=data["price"], kind='scatter')

    # Custom the color
    sns.set(style="white", color_codes=True)
    plt.show()


# create data

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
df =pricearea()
# Plot with palette
s = sns.lmplot(x='price', y='area', data=df, fit_reg=False, hue='price', legend=False, palette="Blues")
s.set_axis_labels('平均价格', '面积')

plt.show()
