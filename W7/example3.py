import arcpy

arcpy.env.overwriteOutput = True

folder = r"C:\temp\data"
file = "GPS_points_buffered.shp"

arcpy.CreateFeatureclass_management(folder, file, "POLYGON", 
                                    r"C:\temp\data\GPS_points.shp", "DISABLED", "DISABLED", 
                                    r"C:\temp\data\GPS_points.shp")

fc = folder + "//" + file

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "Animal", "Time"])

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["SHAPE@", "Animal", "Time"])

for row in rows:
    pointbuf = row[0].buffer(10)
    pointbuf2 = row[0].buffer(20)
    outgeom = pointbuf2.symmetricDifference(pointbuf)
    cursor.insertRow([outgeom, row[1], row[2]])
    print(pointbuf.area)

del cursor



