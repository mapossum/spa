import arcpy

arcpy.env.overwriteOutput = True

folder = r"C:\temp\data"
file = "GPS_points_connected.shp"

#Connect all dots from the the same animal in time order

arcpy.CreateFeatureclass_management(folder, file, "POLYLINE", 
                                    r"C:\temp\data\GPS_points.shp", "DISABLED", "DISABLED", 
                                    r"C:\temp\data\GPS_points.shp")

fc = folder + "//" + file

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "Animal"])

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["SHAPE@XY", "Animal", "Time"], sql_clause=(None, "ORDER BY Animal, Time"))

polylineList = []

previousAnimal = 1

for row in rows:
    print(row[0], row[1], row[2])

    currentAnimal = row[1]
    
    if currentAnimal != previousAnimal:
        #Write out to output file the path
     
        print(polylineList)
        #This only happens when we finish the animal
        array = arcpy.Array(polylineList)
        polyline = arcpy.Polyline(array)
        cursor.insertRow([polyline, row[1]])
        polylineList = []

    
    pt = arcpy.Point(row[0][0], row[0][1])
    polylineList.append(pt)

    previousAnimal = currentAnimal

#Write out to output file the path
print(polylineList)
#This only happens when we finish the animal
array = arcpy.Array(polylineList)
polyline = arcpy.Polyline(array)
cursor.insertRow([polyline, row[1]])
polylineList = []       


del cursor



