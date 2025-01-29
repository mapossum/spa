import arcpy

infc = r"C:\courses\spa\W7\Cityi10\Cityi10.shp"
infcMBG = r"C:\courses\spa\W7\Cityi10\Cityi10_MBC.shp"
arcpy.env.overwriteOutput = True
arcpy.CreateFeatureclass_management(r"C:\courses\spa\W7\Cityi10", "citiesShape.shp", "POLYGON", infc, "#", "#", infc)
arcpy.AddField_management(r"C:\courses\spa\W7\Cityi10\citiesShape.shp", "ShapeInd", "Double")

MBGSC = arcpy.da.SearchCursor(infcMBG, ["SHAPE@", "NAME10"])
cursor = arcpy.da.InsertCursor(r"C:\courses\spa\W7\Cityi10\citiesShape.shp", ['SHAPE@', "NAME10", "ShapeInd"])


# Enter for loop for each feature
for row in arcpy.da.SearchCursor(infc, ["SHAPE@", "NAME10"]):
    MBGrow = next(MBGSC)
    geom = row[0]
    geom2 = MBGrow[0]
    shpInd = (geom.area / geom2.area) * 100
    print(geom.partCount, row[1], MBGSC[1], shpInd)
    newshape = geom2.difference(geom)
    cursor.insertRow([newshape, row[1], shpInd])
    
del cursor
