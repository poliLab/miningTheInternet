# otras librerias: lxml, html.parser, urllib.request, urllib.parse
import sys
import requests
from bs4 import BeautifulSoup
from enum import Enum

class SEEDT(Enum):
    URL = 1
    FILE = 2
    FOLDER = 3
    HTML = 4
    
class ACTIONS(Enum):
    TAGS = 1
    TAG = 2
    
opts={SEEDT.URL : '-u', SEEDT.FILE: '-f', ACTIONS.TAGS: '-ts', ACTIONS.TAG: '-t' }

class Crawly:
    def __init__(self,seed=None,seedType=None):
        self.seed = seed or []
        self.seedType = seedType or SEEDT.URL
        
        
    def parseSeeds(self):
        if(self.seedType == SEEDT.FILE):
            seedsFile = open(self.seed,encoding = 'utf-8',mode = 'r')
            seeds = seedsFile.read().splitlines()
            seedsFile.close()
            return seeds            
    
    def getHtml(self):
        if(self.seedType == SEEDT.URL):
            r = requests.get(self.seed)
            print(r.url)
            return r.text
    
    def getTags(self,doc):
        soup = BeautifulSoup(markup=doc,features='html.parser')
        tags = soup.find_all()
        return tags
    
    def getTag(self,tag,doc):
        soup = BeautifulSoup(markup=doc,features='html.parser')
        return soup.find_all(tag)    
        


def main(argv):    
    crawler = Crawly()   
    if argv[1] == opts[SEEDT.FILE] and len(argv) == 3 :
        crawler.seed = argv[2]
        crawler.seedType = SEEDT.FILE
        seeds = crawler.parseSeeds();
        crawler.seedType = SEEDT.URL
        for seed in seeds:
            crawler.seed = seed
            print(crawler.getHtml())
    elif argv[1] == opts[SEEDT.URL] and len(argv) == 3 :
        crawler.seed = argv[2]
        crawler.seedType = SEEDT.URL
        print(crawler.getHtml())    
    elif len(argv) == 2 and argv[1] not in opts.values():
        crawler.seed = argv[1]
        crawler.seedType = SEEDT.URL
        html = crawler.getHtml()
        tags = crawler.getTag('a',html)
        for tag in tags: print(tag.name+":"+str(tag.attrs))
    else:
        print("error")
        

if __name__ == "__main__":
    if(len(sys.argv)>1):
        main(sys.argv[0:])
    else: 
        print("Need an argument")

