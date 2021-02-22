import math, urllib
import urllib.parse
import urllib.request
import numpy as np

def getaddresslocation(address, outSR=4326):
    params = urllib.parse.urlencode({'SingleLine': address, 'f': 'json', 'outSR': outSR})
    f = urllib.request.urlopen("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?%s" % params)
    loc = eval(f.read())
    outdic = loc['candidates'][0]['location']
    outdic['location'] = address
    return (loc['candidates'][0]['location'])

#print(getaddresslocation("Hattiesburg, MS", 102100))
#print(getaddresslocation("Jackson, MS"))
#print(getaddresslocation("Los Angeles, CA"))


#clist = ["Hattiesburg, MS", "Jackson, MS", "Los Angeles, CA"]

#result = map(getaddresslocation,clist,[102100] * 3)
#print(list(result))

datadef = [('Name', "S32"),('City', 'S32'),('State', 'S32'), ('X', 'f8'), ('Y', 'f8')]

outputlist = []
#open a file
f = open(r"G:\courses\spa\W4\Presidents.csv", "r")

for line in f:
    ls = line.split(",")
    result = (getaddresslocation(ls[1].strip() + "," + ls[2].strip()))
    outputlist.append((ls[0], ls[1].strip(), ls[2].strip(), result["x"], result["y"]))

f.close()

del outputlist[0]
print(outputlist)

presidentArray = np.zeros((len(outputlist)), dtype=datadef)
presidentArray[:] = outputlist[:]
print(presidentArray)


