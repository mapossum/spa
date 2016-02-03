import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

cities = ["Hattiesburg, MS", "New York, NY", "Chicago, IL", "New Orleans, LA"]

for city in cities:
    latlon = getaddresslocation(city)
    #run function from last week 
