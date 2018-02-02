import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address, 'key': 'AIzaSyAIkAkn6l3NkAqQ1xXmIniNnGvL24_N1Lc'})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])

print getaddresslocation("Hattiesburg, MS")
