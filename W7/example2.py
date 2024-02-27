import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\GPS_points.shp", ["SHAPE@JSON", "Animal", "Time"])

total = 0
count = 0
for row in rows:
    a = eval(row[0])
    print(type(a))
    
    #print(row[0])
    #total = row[0][0] + total
    #count = count + 1
    
#print(total / count)
