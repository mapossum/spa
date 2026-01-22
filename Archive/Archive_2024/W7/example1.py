import arcpy
from statistics import mean 

rows = arcpy.da.SearchCursor(r"C:\courses\spa\W7\animaldata\data\GPS_points.shp", ["SHAPE@XY", "Animal", "Time"])

xcoords = []
ycoords = []
for row in rows:
    point = row[0]
    print(row[0], row[1], row[2])
    xcoord, ycoord = point[0], point[1]
    xcoords.append(xcoord)
    ycoords.append(ycoord)


print("The Centroid of all the animal data is: {} , {}".format(mean(xcoords), mean(ycoords)))
    
    
    

