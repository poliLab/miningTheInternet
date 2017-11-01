import requests
import props as P

class Requester:
    
    def __init__(self, URL=None):
        self.URL = URL
        
    def getHtml(self):    
        try:
            print("trying to request url {}".format(self.URL))
            r = requests.get(self.URL)
            
            return r.text
        except Exception:
            print(Exception())
            
       
