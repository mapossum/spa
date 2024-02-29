import arcpy
fc = r"C:\courses\spa\W7\animaldata\data\GPS_points.shp"
gpsdata = arcpy.da.FeatureClassToNumPyArray(fc,["SHAPE@XY", "Animal", "Time"])

print(gpsdata)
print(type(gpsdata))
