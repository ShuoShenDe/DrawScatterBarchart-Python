import pymongo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager
import matplotlib as mpl
import matplotlib.pyplot as plt


# 处理中文问题
#plt.rcParams['font.family'] = ['Arial Unicode MS']
plt.figure(figsize=(15, 10))
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#连接数据库
client = pymongo.MongoClient('localhost',27017)
fangtianxia = client['fangtianxia']
info = fangtianxia['fang']
#加载数据
data = pd.DataFrame(list(info.find()))
d = data['_id'].groupby(by=data['address']).count()
# 设置风格，seaborn有5种基本风格，context表示环境
sns.set(style="white", context="notebook")
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']})
x = d.index
print(x)
y = d.values
g = sns.barplot(x, y)
plt.xlabel('地区')
plt.ylabel('数量')
plt.title("成都各区房源统计")
#在柱状图的上面显示各个类别的数量
plt.savefig('./a.png')
plt.show()
