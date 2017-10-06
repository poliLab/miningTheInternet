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
        
        
