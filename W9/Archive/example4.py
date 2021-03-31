import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\Parks.shp", ["Name", "SHAPE@JSON"])

for row in rows:
    print row[1]

