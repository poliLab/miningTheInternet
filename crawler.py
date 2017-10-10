
# otras librerias: lxml, html.parser, urllib.request, urllib.parse
import props as P
from requester import Requester
from parser import Parser,  Tag
from saver import Saver
import filter as F
class Crawly:
    def __init__(self,seed=None,seedType=None):
        self.seed = [seed] or []
        self.seedType = seedType or P.SEEDT.URL  
        self.saver = Saver
        
    def parseSeeds(self):
        if(self.seedType == P.SEEDT.FILE):
            seedsFile = open(self.seed,encoding = 'utf-8',mode = 'r')
            seeds = seedsFile.read().splitlines()
            seedsFile.close()
            self.seed=seeds;
            self.seedType = P.SEEDT.URLS            
    
    def crawl(self,URL,depth=0, cont=0):
        if depth<P.crawlerProp.depth: 
            print("DEPTH >> ", depth)
            print("VISITING URL >> ",  URL)
            requester = Requester(URL)
            HTML= requester.getHtml()            
            parser = Parser(HTML)
            links= parser.getTag('a')
            for link in links[:P.crawlerProp.range]:   
                depth+=1
                if Tag(link).hasKey('href'):
                    nURL = link['href'] if F.urlValid(link['href']) else (F.urlFix(URL, link['href']) if  F.urlValid(F.urlFix(URL, link['href'])) else None)
                    #print(nURL)
                    self.crawl( nURL, depth,  cont+1) if  nURL is not None else print("SKIPPING URL NOT VALID >> ",  nURL) 
        else:
            print("REACHED DEPTH LIMIT FOR >> ", URL)
        
        return cont,  depth
                    
    
    def start(self):        
        for s in self.seed: 
            requester = Requester(s)
            HTML= requester.getHtml()            
            parser = Parser(HTML)
            tags= parser.getTag('a')
            
            for tag in tags:
                if Tag(tag).hasKey('href'):
                    print(self.crawl(tag['href']) if F.urlValid(tag['href']) else print("SKIPPING URL NOT VALID", tag['href']))

