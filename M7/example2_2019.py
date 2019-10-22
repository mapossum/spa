import arcpy

fc = r"C:\temp\M7\Cityi10_copy2.shp"
fields = ['SHAPE@', 'NAME10']
cursor1 = arcpy.da.UpdateCursor(fc, fields, "NAME10 LIKE 'La%'")

for row in cursor1:
    shape = row[0]
    newgeometry = shape.convexHull()
    row[0] = newgeometry.buffer(200).difference(shape)
    cursor1.updateRow(row) 
