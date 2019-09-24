import math, urllib
import urllib.parse
import urllib.request

def getaddresslocation(address):
    params = urllib.parse.urlencode({'SingleLine': address, 'f': 'json'})
    f = urllib.request.urlopen("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?%s" % params)
    loc = eval(f.read())
    return (loc['candidates'][0]['location']['x'], loc['candidates'][0]['location']['y'])

print(getaddresslocation("Hattiesburg, MS"))



