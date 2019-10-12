from pattern.en import conjugate
def getBase(englishEntry):
    if englishEntry[0:4] == "s/he":
        return englishEntry[5:]
    else:
        return englishEntry

def getVerbAndSuffix(englishBase):
    words = englishBase.split(" ")
    return (words[0], words[1:])

def fullConjugate(englishEntry, conjugationString):
    base = getBase(englishEntry)
    words = getVerbAndSuffix(base)
    return conjugate(words[0], conjugationString)+" " + ' '.join(words[1])
