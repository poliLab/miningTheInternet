import sys
import props as P
from crawler import Crawly
opts={P.SEEDT.URL: '-u', P.ACTIONS.TAGS: '-ts', P.ACTIONS.TAG: '-t'}

def main(argv):    
    crawler = Crawly()   
    if argv[1] == opts[P.SEEDT.URL] and len(argv) == 3:
        crawler.seed = [argv[2]]
        crawler.seedType = P.SEEDT.URL
    elif len(argv) == 2 and argv[1] not in opts.values():
        crawler.seed = [argv[1]]
        crawler.seedType = P.SEEDT.URL    
    crawler.start()        

if __name__ == "__main__":
    if(len(sys.argv)>1):
        main(sys.argv[0:])
    else: 
        print("Need an argument")

