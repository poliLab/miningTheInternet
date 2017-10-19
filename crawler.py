
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
    
    def crawl(self, URL, depth=0):
        
        if depth < P.crawlerProp.depth and URL not in self.visited:
            print("DEPTH >> ", depth)
            print("VISITING URL >> ",  URL)
            
            try:
                requester = Requester(URL)
                HTML = requester.getHtml()            
                parser = Parser(HTML)
                links = parser.getTag('a')
                depth += 1
                
                for link in links[:P.crawlerProp.range]:
                    if link is not None:
                        if Tag(link).hasKey('href'):
                            nURL = link['href'] if F.urlValid(link['href']) else (F.urlFix(URL, link['href']) if F.urlValid(F.urlFix(URL, link['href'])) else None)
                            self.visited.append(nURL)
                            self.crawl(nURL, depth) if nURL is not None else print("SKIPPING URL NOT VALID >> ",  nURL)
            except:
                print(Exception())
        else:
            print("REACHED DEPTH LIMIT FOR >> ", URL)
        
        print(self.visited)
            
    def start(self):      
        self.crawl(self.seed)

