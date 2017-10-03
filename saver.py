from db import DB
from props import dictProp
from props import schemas
import props

con = DB().connect()
dict = schemas()
dictProp()

dict.dictDict[props.DICT.INIT.value]=dictProp.init

#print(props.DICT.INIT.value, type(props.DICT.INIT.value))
#initialDic = {"initSeeds": dictProp.dictInit }

con.dic.insert_one(dict.dictDict)



