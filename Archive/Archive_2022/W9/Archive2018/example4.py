import arcpy

arcpy.env.overwriteOutput = True

out_path = r'c:\temp\spaLab\\'
out_name = "points2.shp"
geometry_type = "POINT"

prjlocation = out_path + "Cityi10.prj"

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, "", "", "", prjlocation)

fc = out_path + out_name
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@XY", "Id"])


for i in range(100,500,10):
    for j in range(0,100,5):
        print i,j
        xy = (i,j)
        cursor.insertRow([xy, i * j])

del cursor
                   
