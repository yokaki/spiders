from pymongo import MongoClient

client = MongoClient()
db = client.day_list
collection = db.days
day_list = []
for i in collection.find():
    print(i['day'])
