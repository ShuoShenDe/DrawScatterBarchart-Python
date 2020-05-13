# library &amp; dataset
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(15, 10))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
area = ["12m","14m","18m","20m","22m"]
price = [110,120,130,140,150]

plt.bar(area, price, color=(0.2, 0.4, 0.6, 0.6))
# Custom Axis title
plt.xlabel('title of the xlabel', fontweight='bold', color='orange', fontsize='17', horizontalalignment='center')
plt.show()