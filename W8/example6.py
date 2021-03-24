import arcpy

rows = arcpy.da.SearchCursor(r"C:\temp\data\Parks.shp", ["Name", "SHAPE@"])

rownumber = 0
for row in rows:
    for partnumber in range(0,row[1].partCount):
        print "Row: " + str(rownumber)
        print "Part: " + str(partnumber)
        part = row[1].getPart(partnumber)
        for pt in part:
            print pt

    rownumber += 1
    

