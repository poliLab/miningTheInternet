import validators

bannedIN = ['#']
bannedEQ = ['/', '#']

def urlValid(URL):
    return True if validators.url(URL) else False
    
def urlFix(URL, LINK):
    nURL = URL+LINK
    return LINK if (any(ban in LINK for ban in bannedIN) or any(ban==LINK for ban in bannedEQ)) else nURL
