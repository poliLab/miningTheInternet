from pymongo import MongoClient

class DB():
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.CrawlerIndex
        
    def connect(self):
        return self.db;

