import validators
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
 
bannedIN = ['#']
bannedEQ = ['/', '#']

def urlValid(URL):
    return True if validators.url(URL) else False

def urlFix(URL, LINK):
    nURL = URL+LINK
    print("fixed URL>> ", nURL)
    return LINK if (any(ban in LINK for ban in bannedIN) or any(ban == LINK for ban in bannedEQ)) else nURL


example = "correr, corría. El estaba comiendo comida. El sol está muy caliente. La canción que Daniel cantó fue excelente"
#print(sent_tokenize(example))
#print(word_tokenize(example))

stop_words = set(stopwords.words("spanish"))
#print(stop_words)

filtered_setence = [w for w in word_tokenize(example) if w not in stop_words]

#print(filtered_setence)

ps = SnowballStemmer("spanish")

#for w in word_tokenize(example):
    #print(ps.stem(w))
    
tokens = word_tokenize(example)

tagger = nltk.data.load("taggers/cess_esp_aubt.pickle")
print(tagger.tag(tokens))
