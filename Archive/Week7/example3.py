import arcpy

arcpy.env.overwriteOutput = True

folder = r"C:\courses\spa\Week7\animaldata\data"
file = "GPS_points_buffered.shp"

arcpy.CreateFeatureclass_management(folder, file, "POLYGON", 
                                    r"{}\GPS_points.shp".format(folder), "DISABLED", "DISABLED", 
                                    r"{}\GPS_points.shp".format(folder))

fc = folder + r"/" + file

arcpy.management.AddField(fc, "Area", "DOUBLE")

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "Animal", "Time", "Area"])

rows = arcpy.da.SearchCursor(r"{}\GPS_points.shp".format(folder), ["SHAPE@", "Animal", "Time"])

for row in rows:
    pointbuf = row[0].buffer(row[1])
    pointbuf2 = row[0].buffer(20)
    outgeom = pointbuf2.symmetricDifference(pointbuf)
    cursor.insertRow([outgeom, row[1], row[2], pointbuf.area])
    print(pointbuf.area)

del cursor



