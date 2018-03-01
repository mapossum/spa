import arcpy

arcpy.env.overwriteOutput = True

fc = r"C:\temp\Cityi10.shp"
fc2 = r"C:\temp\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

fields = ["Name10", "SHAPE@"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        print row[0]
        polygonbuf = row[1].buffer(100)
        row[1] = polygonbuf.difference(row[1])
        cursor.updateRow(row) 
