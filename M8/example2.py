import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Animal", "SHAPE@JSON"])

total = 0
count = 0
for row in rows:
    rowGeom = eval(row[1])
    print rowGeom["x"], rowGeom["y"]
    total += row[0]
    count += 1

print total, count, total / count
