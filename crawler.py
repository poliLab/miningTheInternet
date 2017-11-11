
# otras librerias: lxml, html.parser, urllib.request, urllib.parse
import props as P
from requester import Requester
from parser import Parser,  Tag
from saver import Saver
import filter as F

cont = 0

class Crawly:   
    
    visited = []
   
    def __init__(self, seed=None, seedType=None):
        self.seed = seed or None
        self.seedType = seedType or P.SEEDT.URL  
        self.saver = Saver
    
    def __pass(self, URL):
        if URL is not None and URL not in self.visited and not any(ban in URL for ban in P.dictProp.ban):
            return True
        else:
            return False
    
    def crawl(self, URL, depth=0):
        
        if depth <= P.crawlerProp.depth:
            print("DEPTH >> ", depth)
            print("VISITING URL >> ",  URL)
            
            try:
                requester = Requester(URL)
                HTML = requester.getHtml()          
                parser = Parser(HTML)
                links = parser.getTag('a')
                
                #print(HTML)
                words = F.extractWords(parser.getTags(list(P.crawlerProp.atlas.keys())), P.crawlerProp.pos_tag)
                
                print(words)
                
                depth += 1
                
                for link in links:
                    if link is not None:
                        if Tag(link).hasKey('href'):
                            nURL = link['href'] if F.urlValid(link['href']) else (F.urlFix(URL, link['href']) if F.urlValid(F.urlFix(URL, link['href'])) else None)
                            
                            if self.__pass(nURL):
                                self.visited.append(nURL)
                                #print(nURL)
                                self.crawl(nURL, depth)
                            #else:
                                #print("SKIPPING URL NOT VALID >> ",  nURL)                                
            except:
                print(Exception())
        else:
            print("REACHED DEPTH LIMIT FOR >> ", URL)
        
        #print(self.visited)
            
    def start(self):     
        self.crawl(self.seed.strip())

