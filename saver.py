from pymongo import MongoClient
from props import dictProp

dictProp()

client = MongoClient('localhost', 27017)

db = client.CrawlerIndex

initialDic = {"initSeeds": dictProp.dictInit }


db.dic.insert_one(initialDic)



