import arcpy

arcpy.env.overwriteOutput = True

out_path = r'c:\temp\spaLab\\'
out_name = "rects.shp"
geometry_type = "POLYGON"

prjlocation = out_path + "Cityi10.prj"

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, "", "", "", prjlocation)

fc = out_path + out_name
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@", "Id"])


for i in range(100,500,10):
    for j in range(0,100,5):
        print i,j
        #xy = (i,j)
        array = arcpy.Array([arcpy.Point(i, j), arcpy.Point(i + 10, j), arcpy.Point(i + 10, j + 5), arcpy.Point(i, j + 5)])
        newpolygon = arcpy.Polygon(array)
        cursor.insertRow([newpolygon, i * j])

del cursor
                   
