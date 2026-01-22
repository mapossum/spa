import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Animal"])

total = 0
count = 0
for row in rows:
    total += row[0]
    count += 1

print total, count, total / count
