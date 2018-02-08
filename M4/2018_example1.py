myDictionary = {}
Dict2 = dict()

myDict = {"quiero": "I want", "hola": "hello", "cinco": "five", "cervezas": "beers"}


def translateSpEn(sent):

    outList = []
    words = sent.split(" ")
    for word in words:
        outList.append(myDict[word])
    
    return " ".join(outList)


sentance = "quiero cinco cervezas"

outsentance = translateSpEn(sentance)

print outsentance

#print myDict["cinco"]
