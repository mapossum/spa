import arcpy

infc = r"C:\courses\spa\Week7\Cityi10\Cityi10.shp"

# Enter for loop for each feature
for row in arcpy.da.SearchCursor(infc, ["SHAPE@", "NAME10"]):
    geom = row[0]
    if geom.partCount > 1:
        print(geom.partCount, row[1])
        
        for prt in geom:
            
            newPL = arcpy.Polyline(prt, geom.spatialReference)
            print(newPL.getLength())
            #for pnt in prt:
                #print(pnt)
