import validators
import nltk.data
from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
 
bannedIN = ['#']
bannedEQ = ['/', '#']


stop_words = set(stopwords.words("spanish"))
tagger = nltk.data.load("taggers/cess_esp_aubt.pickle")


def urlValid(URL):
    return True if validators.url(URL) else False


def urlFix(URL, LINK):
    nURL = parentUrl(URL)+LINK
    #print("fixed URL>> ", nURL)
    return LINK if (any(ban in LINK for ban in bannedIN) or any(ban == LINK for ban in bannedEQ)) else nURL


def parentUrl(URL):
    return URL.rsplit('/', URL.count('/')-2)[0]


def filterWords(words, filters):
    tagged_words = tagger.tag(words)
    filtered_words = [w1 for w1, w2 in tagged_words if w2.startswith(tuple(filters))]
    return filtered_words


def extractWords(tags, types):
    words = []
    for tag in tags:
        tokens = [w for w in word_tokenize(tag.text) if w not in stop_words]
        words.extend(filterWords(tokens, types))
    return words



#example = "correr, corría. El estaba comiendo comida. El sol está muy caliente. La canción que Daniel cantó fue excelente"
##print(sent_tokenize(example))
##print(word_tokenize(example))

#stop_words = set(stopwords.words("spanish"))
##print(stop_words)

#filtered_setence = [w for w in word_tokenize(example) if w not in stop_words]

##print(filtered_setence)

#ps = SnowballStemmer("spanish")

##for w in word_tokenize(example):
    ##print(ps.stem(w))
    
#tokens = word_tokenize(example)

#tagger = nltk.data.load("taggers/cess_esp_aubt.pickle")
#print(tagger.tag(tokens))
