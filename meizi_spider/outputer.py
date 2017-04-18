import json
from pymongo import MongoClient


class HtmlOutputer(object):
    def __init__(self):
        self.test = []

    def collect_data(self, data):
        if data is None:
            self.test.append(1)
            return
        client = MongoClient()
        db = client.meizi
        collection = db.url_list
        for i in data:
            collection.insert(i)

    def output_html(self):
        print('down')
