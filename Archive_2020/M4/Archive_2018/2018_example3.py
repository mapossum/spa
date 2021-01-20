import arcpy

arcpy.env.workspace = r"C:\temp\tydix"
arcpy.env.overwriteOutput = True

roads = r"risk_roads.shp"
roadsBuffer = r"risk_roads_buff_"
distanceField = "TERR_DISTA"

for bufdistance in range(100,1000,100):
    arcpy.Buffer_analysis(roads, roadsBuffer + str(bufdistance), bufdistance, "" , "", "ALL")





