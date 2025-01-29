import arcpy

infc = r"C:\courses\spa\W7\Cityi10\cd.shp"
infcMBG = r"C:\courses\spa\W7\Cityi10\cd_MBC.shp"
arcpy.env.overwriteOutput = True
arcpy.CreateFeatureclass_management(r"C:\courses\spa\W7\Cityi10", "cdShape.shp", "POLYGON", infc, "#", "#", infc)
arcpy.AddField_management(r"C:\courses\spa\W7\Cityi10\cdShape.shp", "ShapeInd", "Double")

MBGSC = arcpy.da.SearchCursor(infcMBG, ["SHAPE@", "NAME"])
cursor = arcpy.da.InsertCursor(r"C:\courses\spa\W7\Cityi10\cdShape.shp", ['SHAPE@', "NAME", "ShapeInd"])


# Enter for loop for each feature
for row in arcpy.da.SearchCursor(infc, ["SHAPE@", "NAME"]):
    MBGrow = next(MBGSC)
    geom = row[0]
    geom2 = MBGrow[0]
    shpInd = (geom.area / geom2.area) * 100
    print(geom.partCount, row[1], MBGSC[1], shpInd)
    newshape = geom2.difference(geom)
    cursor.insertRow([newshape, row[1], shpInd])
    
del cursor
