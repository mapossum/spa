import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address, 'key': 'AIzaSyAIkAkn6l3NkAqQ1xXmIniNnGvL24_N1Lc'})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

#Get a list of Cities from a file.

def readFileToList(path, hasHeader=True):
    f = open(path, "r")

    fileLines = []

    for line in f.readlines():
        fileLines.append(line.strip())

    f.close()

    if hasHeader:
        fileLines = fileLines[1:]

    return fileLines


def findCityLocations(Cities):
    citiesDict = {}

    for city in Cities:
        x, y = getaddresslocation(city)
        citiesDict[city] = {"x": x, "y": y}

    return citiesDict

fileData = readFileToList(r"citiesSmall.txt")

print findCityLocations(fileData)

#Loop through each key in output Dictionary
  k, mydict[k]["x"], mydict[k]["y"]

#write the dictionary out to a file by looping through all the keys

#Final output should be a file with lines that look like this:

#city,Lat(y),Lon(x)
