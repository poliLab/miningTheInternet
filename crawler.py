
# otras librerias: lxml, html.parser, urllib.request, urllib.parse
import props as P
from requester import Requester
from parser import Parser
from enum import Enum

    

class Crawly:
    def __init__(self,seed=None,seedType=None):
        self.seed = [seed] or []
        self.seedType = seedType or P.SEEDT.URL        
        
    def parseSeeds(self):
        if(self.seedType == P.SEEDT.FILE):
            seedsFile = open(self.seed,encoding = 'utf-8',mode = 'r')
            seeds = seedsFile.read().splitlines()
            seedsFile.close()
            
            self.seed=seeds;
            self.seedType = P.SEEDT.URLS            
        
    def start(self):        
        for s in self.seed: 
            requester = Requester(s)
            html= requester.getHtml()
            parser = Parser(html)
            tags= parser.getTag('a')
            for tag in tags: print(tag['href'])

