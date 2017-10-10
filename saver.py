from db import DB
from props import schemas
import props as P


class Saver:
    def __init__(self):        
        self.con = DB().connect()
        self.dict = schemas()
        #dict.dictDict[props.DICT.INIT.value]=dictProp['init']

        #print(props.DICT.INIT.value, type(props.DICT.INIT.value))
        #initialDic = {"initSeeds": dictProp.dictInit }
        
    def save(self,dict,collection):
        self.con.collection.insert_one(dict)
        #self.con[collection].insert_one(dict)

