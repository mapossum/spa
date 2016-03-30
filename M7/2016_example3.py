import arcpy

fc = r"C:\temp\m7\Cityi10copy.shp"
fields = ["SHAPE@", "NAME10", 'ALAND10']


cursor = arcpy.da.UpdateCursor(fc, fields)

for row in cursor:
    row[2] = len(row[1])
    cursor.updateRow(row)

del cursor, row
