from enum import Enum, unique

@unique
class SEEDT(Enum):
    URL = 1
    URLS = 2
    FILE = 3
    FOLDER = 4
    
@unique    
class ACTIONS(Enum):
    TAGS = 1
    TAG = 2

class dictProp:  
    init = ["noticia","información","colombia","nacional","clima","medio ambiente","ecologia","reporte","periodista","bogota","medellin","economia"]
    ban = ["facebook","fb","twitter","instagram",".pdf",".doc",".docx",".jpg",".png","advertise","ads","mozilla","w3e"]
    
class crawlerProp:
    depth=3
    range=3
    freq=500  #ms
    atlas = { "h1":10, "a":10, "h2":8, "h3":8, "h4":8, "p":9, "span":9, "label":7, "li":10, "b":10 ,"meta":10 }

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
    REC = "rec"
    
@unique    
class CONTENTS(Enum):
    HEADLINES = "headlines" # props like h1 h2 h3... label span
    BODY = "body" # props like p div
    IMG = "img" # [{}] array of images links
    
class schemas(): 
    def __init__(self):
        
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
            MAIN.CONT.value:"",
            MAIN.REC.value:""
            }
        
        self.contentsDict = {
            CONTENTS.HEADLINES.value:"",
            CONTENTS.BODY.value:"",
            CONTENTS.IMG.value:""
            }
