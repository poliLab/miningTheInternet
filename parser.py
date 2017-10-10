from bs4 import BeautifulSoup

class Parser:
    def __init__(self,HTML):
        self.HTML= HTML        
     
    def getTags(self,doc):
        soup = BeautifulSoup(markup=doc,features='html.parser')
        tags = soup.find_all()
        return tags
    
    def getTag(self,tag):
        soup = BeautifulSoup(markup=self.HTML,features='html.parser') 
        return soup.find_all(tag)

class Tag:
    def __init__(self, tag):
        self.tag=tag;
    def hasKey(self, key):
        return True if self.tag.get(key, None) is not None else False
    def hasValue(self, value):
        return True
    def getV(self, key):
        return self.tag.get(key, None)
        
        
        
