import arcpy

arcpy.env.overwriteOutput = True

out_path = r'c:\temp\spaLab\\'
out_name = "points2.shp"
geometry_type = "POINT"

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type)

fc = out_path + out_name
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY"])


for i in range(100,500,10):
    for j in range(0,100,5):
        print i,j
        xy = (i,j)
        cursor.insertRow([xy])

del cursor
                   
