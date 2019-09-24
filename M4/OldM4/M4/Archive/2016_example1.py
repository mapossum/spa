import math, urllib
def getaddresslocation(address):
    params = urllib.urlencode({'address': address})
    f = urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?%s" % params)
    loc = eval(f.read())
    return (loc["results"][0]["geometry"]["location"]['lng'],  loc["results"][0]["geometry"]["location"]['lat'])


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)
    def translate(self, xshift = 0, yshift = 0):
        self.x = self.x + xshift
        self.y = self.y + yshift

#Reads a text file - input (path), output list of each line in file

def cities(path, header = True):
    f = open(path, 'r')

    listofCities = []
    for l in f:
        listofCities.append(l.strip())

    if header:  
        return listofCities[1:]
    else:
        return listofCities

#take a list of cities and return dictionary with keys city names
# values are a point object

def returnCities(listofCities):
    dictofCities = {}

    for city in listofCities:
        location = getaddresslocation(city)
        dictofCities[city] = Point(location[0],location[1]) 
    
    return dictofCities

#write a report of that info (dictionary) to a file.

def locationReport(ourCitiesDict):

    #loop through each key in the dictionary
    #write to file name of city, Lat, Lon

ourCities = cities(r"C:\courses\spa\week4\citiesSmall.txt")
ourCitiesDict = returnCities(ourCities)
print ourCitiesDict
