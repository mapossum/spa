import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

def getlocationList(namedLocations):
    listofTupleLocation = []
    for city in cities:
        location = getaddresslocation(city)
        listofTupleLocation.append(location)
    return listofTupleLocation

cities = ["Hattiesburg, MS", "New York, NY", 'Seattle, WA', "Irvine, CA"]

LLlocations = getlocationList(cities)

for location in LLlocations:
    #do your code here (use stuff from last week)
    print location
