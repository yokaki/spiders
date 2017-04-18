from pymongo import MongoClient


class UrlManager(object):
    def __init__(self):
        self.url_list = []

    def get_new_url(self):
        return self.url_list.pop()

    def has_url(self):
        return len(self.url_list) != 0

    def get_url_list(self):
        base_url = 'http://news.at.zhihu.com/api/4/news/before/'
        client = MongoClient()
        db = client.day_list
        collection = db.days
        for i in collection.find():
            self.url_list.append(base_url + i['day'])
