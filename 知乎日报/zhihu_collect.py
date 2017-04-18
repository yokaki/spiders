from pymongo import MongoClient


class Collect(object):
    def collect(self, new_data):
        client = MongoClient()
        db = client.zhrb
        collection = db.data_by_day
        collection.insert(new_data)
