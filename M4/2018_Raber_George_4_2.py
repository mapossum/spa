import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address, 'key': 'AIzaSyAIkAkn6l3NkAqQ1xXmIniNnGvL24_N1Lc'})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

#Get a list of Cities to test with

def findCityLocations(Cities):
    citiesDict = {}

    for city in Cities:
        x, y = getaddresslocation(city)
        citiesDict[city] = {"x": x, "y": y}

    return citiesDict

#Test the function by calling it and print the return value
