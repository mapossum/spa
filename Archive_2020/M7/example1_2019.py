import arcpy

fc = r"C:\temp\M7\Cityi10.shp"
fields = ['SHAPE@', 'NAME10']
cursor1 = arcpy.da.SearchCursor(fc, fields, "NAME10 LIKE 'La%'")

for row in cursor1:
    shape = row[0]
    print(row[1])
    for part in shape:
        for ring in part:
            print(ring)
