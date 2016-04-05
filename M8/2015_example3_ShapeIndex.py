import arcpy, math, SEC


def findSQ(area):
    x = math.sqrt(area)
    perm = x * 4
    return perm

arcpy.env.overwriteOutput = True

fc = r"C:\temp\week8\Cityi10.shp"
fc2 = r"C:\temp\week8\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

fields = ["Name10", "SHAPE@"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:

        pa = row[1].length / row[1].area
        pa2 = findSQ(row[1].area) / row[1].area
        SHAPEINDEX = pa / pa2
        print row[0], SHAPEINDEX
        

del cursor, row
