import arcpy

arcpy.env.overwriteOutput = True

folder = r"C:\courses\spa\W7\animaldata\data"
file = "GPS_points_connected.shp"

#Connect all dots from the the same animal in time order

def writenew(polylineList, cursor):
        print(polylineList)
        #This only happens when we finish the animal
        array = arcpy.Array(polylineList)
        polyline = arcpy.Polyline(array)
        cursor.insertRow([polyline, row[1]])
        

arcpy.CreateFeatureclass_management(folder, file, "POLYLINE", 
                                    r"{}\GPS_points.shp".format(folder), "DISABLED", "DISABLED", 
                                    r"{}\GPS_points.shp".format(folder))

fc = folder + "//" + file

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "Animal"])

rows = arcpy.da.SearchCursor(r"{}\GPS_points.shp".format(folder), ["SHAPE@XY", "Animal", "Time"], sql_clause=(None, "ORDER BY Animal, Time"))

polylineList = []

previousAnimal = 1

for row in rows:
    print(row[0], row[1], row[2])

    currentAnimal = row[1]
    
    if currentAnimal != previousAnimal:
        #Write out to output file the path
     
        writenew(polylineList, cursor)
        polylineList = []
    
    pt = arcpy.Point(row[0][0], row[0][1])
    polylineList.append(pt)

    previousAnimal = currentAnimal

#Write out to output file the path
writenew(polylineList, cursor)    


del cursor



