from enum import Enum


def dictProp():    
    dictProp.dictInit=["noticia","información","colombia","nacional","clima","reporte","periodista","bogota","medellin","economia"]
    

def deepProp():
    dictProp.deep=10;
    
    
def schemas():
    
    class HISTORY(Enum):
        URL = "url"
        TITLE = "title"
        METAS = "metas"
        REC = "rec" #[0:10] if the page shouldn't be visted : 0 or most likely be visited again >6
        COUNTER = "counter" #how many times the url has been visited
        
    class DICT(Enum):
        INIT = "init" #initial dictionary
        GEN = "gen" #[{}{}{}] array of generations of generated dictionary mutations
        EXPAND = "expand" #how much can the dictionary can be expanded
        COUNTER = "counter" # how many
    
    class MAIN(Enum):
        URL = "url"
        PARENT = "parent" # ref Main _id
        TITLE = "title"
        METAS = "metas"
        LINKS = "links"
        TAGS = "tags" # [{}] array of tags, keywords
        DATE = "date"
        CONT = "content" # ref a CONTENTS _id
        
    
    class CONTENTS(Enum):
        HEADLINES = "headlines" # props like h1 h2 h3... label span
        BODY = "body" # props like p div
        IMG = "img" # [{}] array of images links
        
        
    
        
        
