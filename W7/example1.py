import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["Shape@XY", "Animal", "Time"])

total = 0
count = 0
for row in rows:
    print(row[0])
    total = row[0][0] + total
    count = count + 1
    
print(total / count)
