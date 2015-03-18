import arcpy

arcpy.env.overwriteOutput = True

fc = r"C:\temp\week8\Cityi10.shp"
fc2 = r"C:\temp\week8\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

fields = ["Name10", "SHAPE@"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        print row[0], (row[1].length / row[1].area) * 1000

del cursor, row
