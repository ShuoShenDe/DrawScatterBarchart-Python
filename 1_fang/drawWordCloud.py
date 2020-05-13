# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
import pymongo

def readmongodb():
    # 处理中文问题
    # plt.rcParams['font.family'] = ['Arial Unicode MS']
    plt.figure(figsize=(15, 10))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 连接数据库
    client = pymongo.MongoClient('localhost', 27017)
    fangtianxia = client['fangtianxia']
    info = fangtianxia['fang']
    # 加载数据
    data = pd.DataFrame(list(info.find()))
    title = data['title']
    return title

# trnasform image format
def transform_format(val):

    if all(val)== True:
        return 255
    else:
        return 0

def wordcloud(text):

    wine_mask = np.array(Image.open("house.png"))
    # Transform your mask into a new one that will work with the function:
    transformed_wine_mask = np.ndarray((wine_mask.shape[0], wine_mask.shape[1]), np.int32)
    for i in range(len(wine_mask)):
        transformed_wine_mask[i] = list(map(transform_format, wine_mask[i]))

    mytext = " ".join(jieba.cut(text))
    wordcloud = WordCloud(font_path="simsun.ttf", max_words=1000,mask=transformed_wine_mask, background_color="white")
    wordcloud.generate(mytext)
    # store to file
    wordcloud.to_file("wordcloud.png")
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    text=readmongodb()
    wordcloud(text.to_string(   ))