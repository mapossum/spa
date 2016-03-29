import arcpy

#search each GPS Point and get points, Place into Dictionary

def findCenter(animal):
    for pt in animal:
        print pt

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Shape@XY", "Animal", "Time"])


totalx = 0
totaly = 0
count = 0

animals = {}
for row in rows:
    #print "Animal:" + str(row[1])
    if not animals.has_key(row[1]):
        animals[row[1]] = []
    animals[row[1]].append(arcpy.Point(*row[0]))
    totalx += row[0][0]
    totaly += row[0][1]
    count += 1
    
#print animals
    
centroid = totalx / count, totaly / count
print centroid

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
    
    polyline = arcpy.Polyline(array)

    #write out data

    lines.insertRow([polyline, 0 , animal])

    #this will fail until we calculate stdev
    
    #homeRange = polyline.buffer(stdev)

    #Also we need a shapefile to save this homeRange in
    
    

del lines
