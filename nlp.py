from glob import glob
from codecs import open, BOM_UTF8 
from collections import defaultdict
from nltk.corpus import cess_esp


# "el" => {"DA": 3741, "NP": 243, "CS": 13, "RG": 7}) 
lexicon = defaultdict(lambda: defaultdict(int))

for tag in cess_esp.tagged_words()[:100]:
    lexicon[tag[0]][tag[1]] += 1


top = [] 
for w, tags in lexicon.items():    
    freq = sum(tags.values())      # 3741 + 243 + ...
    tag  = max(tags, key=tags.get) # DA
    top.append((freq, w, tag))


top = sorted(top, reverse=True)[:100] # top 100,000
top = ["%s %s" % (w, tag) for freq, w, tag in top if w]

open("es-lexicon.txt", "w").write("\n".join(top))

ANONYMOUS = "anonymous"
for s in cess_esp.tagged_words()[:100]:
    for i, (w, tag) in enumerate(s):
        if tag.startswith("NP"): # NP = proper noun in Parole tagset.
            s[i] = (ANONYMOUS, "NP")
