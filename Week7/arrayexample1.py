import arcpy
fc = r"C:\courses\spa\Week7\animaldata\data\GPS_points.shp"
gpsdata = arcpy.da.FeatureClassToNumPyArray(fc,["SHAPE@XY", "Animal", "Time"])

print(gpsdata)
print(type(gpsdata))
