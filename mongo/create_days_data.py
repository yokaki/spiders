import datetime
from pymongo import MongoClient

num = 1
now = datetime.datetime.now()
client = MongoClient()
db = client.day_list
collection = db.days


def get_day(number):
    new_date = now + datetime.timedelta(days=number)
    new_date = str(new_date)[:10].replace('-', '')
    collection.insert({'day': new_date})


while True:
    get_day(num)
    num -= 1
    if num == -600:
        break
