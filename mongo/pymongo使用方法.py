from pymongo import MongoClient

Client = MongoClient()  # 链接mongodb

db = Client.test  # 链接数据库
collection = db.name_list  # 链接集合
collection.insert({"name": "mike", "active_time": "20130408"})  # 插入数据
for i in collection.find():  # 找到所有数据
    print(i)
