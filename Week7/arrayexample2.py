import arcpy
fc = r"C:\courses\spa\Week7\animaldata\data\GPS_points.shp"
fc2 = r"C:\courses\spa\Week7\animaldata\data\GPS_points_mod.shp"
spatial_ref = arcpy.Describe(fc).spatialReference
gpsdata = arcpy.da.FeatureClassToNumPyArray(fc,["SHAPE@XY", "Animal", "Time"])

print(gpsdata)
print(type(gpsdata))

gpsdata["Time"] = gpsdata["Time"] * 3.4

#arcpy.da.NumPyArrayToFeatureClass(gpsdata, fc2, ["SHAPE@XY", "Animal", "Time"], spatial_ref)

#arcpy.da.ExtendTable("c:/data/base.gdb/current_table", "tableid", array, "idfield")


