import math, urllib
import urllib.parse
import urllib.request

def getaddresslocation(address, outSR=4326):
    params = urllib.parse.urlencode({'SingleLine': address, 'f': 'json', 'outSR': outSR})
    f = urllib.request.urlopen("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?%s" % params)
    loc = eval(f.read())
    outdic = loc['candidates'][0]['location']
    outdic['location'] = address
    return (loc['candidates'][0]['location'])

print(getaddresslocation("Hattiesburg, MS", 102100))
print(getaddresslocation("Jackson, MS"))
print(getaddresslocation("Los Angeles, CA"))
