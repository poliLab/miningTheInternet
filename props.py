from enum import Enum, unique


def dictProp():    
    dictProp.init=["noticia","información","colombia","nacional","clima","medio ambiente","ecologia","reporte","periodista","bogota","medellin","economia"]
    dictProp.initSize=len(dictProp.init)
       
    
def crawlerProp():
    crawlerProp.deep=10;

@unique
class HISTORY(Enum):
    URL = "url"
    TITLE = "title"
    METAS = "metas"
    REC = "rec" #[0:10] if the page shouldn't be visted : 0 or most likely be visited again >6
    COUNTER = "counter" #how many times the url has been visited
    
@unique   
class DICT(Enum):
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)
    INIT = "init" #initial dictionary
    GEN = "gen" #[{}{}{}] array of generations of generated dictionary mutations
    EXPAND = "expand" #how much can the dictionary can be expanded
    
@unique
class MAIN(Enum):
    URL = "url"
    PARENT = "parent" # ref Main _id
    TITLE = "title"
    METAS = "metas"
    LINKS = "links"
    TAGS = "tags" # [{}] array of tags, keywords
    DATE = "date"
    CONT = "content" # ref a CONTENTS _id
    
@unique    
class CONTENTS(Enum):
    HEADLINES = "headlines" # props like h1 h2 h3... label span
    BODY = "body" # props like p div
    IMG = "img" # [{}] array of images links
    
class schemas(): 
    def __init__(self):
        self.historyDict = {
            HISTORY.URL.value:"",
            HISTORY.TITLE.value:"",
            HISTORY.METAS.value:"",
            HISTORY.REC.value:"",
            HISTORY.COUNTER.value:""
            }
        
        self.dictDict = {
            DICT.INIT.value:[],
            DICT.GEN.value:[],
            DICT.EXPAND.value:""
            }
        
        self.mainDict = {
            MAIN.URL.value:"",
            MAIN.PARENT.value:"",
            MAIN.TITLE.value:"",
            MAIN.METAS.value:"",
            MAIN.LINKS.value:"",
            MAIN.TAGS.value:"",
            MAIN.DATE.value:"",
            MAIN.CONT.value:""
            }
        
        self.contentsDict = {
            CONTENTS.HEADLINES.value:"",
            CONTENTS.BODY.value:"",
            CONTENTS.IMG.value:""
            }
