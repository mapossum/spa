import arcpy
arcpy.env.overwriteOutput = True

out_path = r"C:\temp\M7"
out_name = "Lines.shp"
fc = r"{}/{}".format(out_path,out_name)
spatial_reference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(out_path, out_name, "Polyline", "", "", "", spatial_reference)

cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array([arcpy.Point(-77.4349451, 37.5408265),
                     arcpy.Point(-78.6384349, 35.7780943)])
polyline = arcpy.Polyline(array, spatial_reference)

cursor.insertRow([polyline])

del cursor
