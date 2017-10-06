import requests
import props as P

class Requester:
    
    def __init__(self,URL=None):
        self.URL=URL
        
    def getHtml(self):        
        r = requests.get(self.URL)
        return r.text
