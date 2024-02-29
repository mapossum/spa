import arcpy

rows = arcpy.da.SearchCursor(r"C:\courses\spa\W7\animaldata\data\GPS_points.shp", ["SHAPE@JSON", "Animal", "Time"])

total = 0
count = 0
for row in rows:
    print(row[0])
    print(type(row[0]))
    a = eval(row[0])
    print(type(a))
    print (a["x"], a["y"])
    

