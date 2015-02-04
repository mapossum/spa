import location

def getFileList(path):
    f = open(path, "r")

    f.readline()
    fileList = []
    for line in f:
        fileList.append(line.strip())

    f.close()

    return fileList


class Point:

    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)


def makeCitiesDict(citiesList):

    CitiesDict = dict()

    for city in citiesList:
        latlog = location.getaddresslocation(city)
        x = latlog[0]
        y = latlog[1]
        CitiesDict[city] = Point(x, y)

    return CitiesDict

def writeDictFile(aDict, filename):

    #put code to go through Dict Here and write file


myCities = getFileList(r"C:\courses\spa\week4\citiesSmall.txt")

myCitiesDict = makeCitiesDict(myCities)

print myCitiesDict


