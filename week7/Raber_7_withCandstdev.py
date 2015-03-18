import arcpy, math

#search each GPS Point and get points, Place into Dictionary

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def stDev(animal, center):
    totdistance = 0
    count = -1
    for pt in animal:
        cdistance = distance(pt.X, pt.Y, center[0], center[1])
        totdistance += cdistance * cdistance
        count += 1
    return math.sqrt(totdistance / count)
        
def findCenter(animal):
    totalx = 0
    totaly = 0
    count = 0
    for pt in animal:
        totalx += pt.X
        totaly += pt.Y
        count += 1
        
    #print animals
        
    centroid = totalx / count, totaly / count
    return centroid

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Shape@XY", "Animal", "Time"])



animals = {}
for row in rows:
    if not animals.has_key(row[1]):
        animals[row[1]] = []
    animals[row[1]].append(arcpy.Point(*row[0]))

del rows


#Create Lines and insert into Insert Cursor
lines = arcpy.da.InsertCursor(r"C:\temp\data\tracks.shp", ["SHAPE@", "Time", "Animal"])

#do this after we calc stdev
#arcpy.CreateFeatureclass_management("C:/output")

for animal in animals:
    print animal#, animals[animal]
    array = arcpy.Array(animals[animal])
    #write find centroid function pass animal to it
    
    mycenter = findCenter(animals[animal])
    mystdev = stDev(animals[animal], mycenter)
    print mystdev
    
    polyline = arcpy.Polyline(array)

    #write out data

    lines.insertRow([polyline, 0 , animal])

    #this will fail until we calculate stdev
    
    homeRange = polyline.buffer(mystdev)

    #Also we need a shapefile to save this homeRange in
    
    

del lines
