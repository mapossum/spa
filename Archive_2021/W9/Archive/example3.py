import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\Parks.shp", ["Animal", "SHAPE@WKT"])

total = 0
count = 0
for row in rows:
    print row[1]
    total += row[0]
    count += 1

print total, count, total / count
