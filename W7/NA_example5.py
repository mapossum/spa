import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Animal", "SHAPE@"], '"Animal" = 3')


for row in rows:
    print row[1]
    

