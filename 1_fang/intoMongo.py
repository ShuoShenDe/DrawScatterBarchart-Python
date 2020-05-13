import pymongo
import pandas as pd

class Fangtianxia(object):
    def __init__(self):
        host = "127.0.0.1"
        port = 27017
        dbname = "fangtianxia"
        sheetname = "fang"
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item):
        try:
            data = dict(item)
            self.post.insert(data)
            return item
        except:
            print('插入失败')
        
def connectDB():
    client = pymongo.MongoClient('localhost', 27017)
    fangtianxia = client['fangtianxia']
    info = fangtianxia['fang']
    # 加载数据
    data = pd.DataFrame(list(info.find()))
    return data