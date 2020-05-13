import pymongo
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #指定默认字体  
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# 处理中文问题
#plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.figure(figsize=(15, 10))

#连接数据库
client = pymongo.MongoClient('localhost',27017)
fangtianxia = client['fangtianxia']
info = fangtianxia['fang']
#加载数据
data = pd.DataFrame(list(info.find()))
def processPrice(x):
    if 0< int(x) <2000:
        return "0-2k"
    elif int(x) < 4000:
        return "2-4k"
    elif int(x) < 6000:
        return "4-6k"
    elif int(x) > 6000:
        return "6k以上"
data['priceType'] = data['price'].apply(processPrice)
d = data['priceType'].groupby(by=data['priceType']).count()
labels = ['0-2k','2-4k','4-6k','6k以上']
sizes = [2,5,12,70]
explode = (0,0,0,0.1)
plt.pie(d.values,explode=explode,labels=d.index,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("全成都房租价格分布")
plt.savefig('b.png')
plt.show()
