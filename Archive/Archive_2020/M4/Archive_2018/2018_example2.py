import arcpy

arcpy.env.workspace = r"C:\temp\tydix"
arcpy.env.overwriteOutput = True

roads = r"risk_roads.shp"
roadsBuffer = r"risk_roads_buff.shp"
distanceField = "TERR_DISTA"
arcpy.Buffer_analysis(roads, roadsBuffer, distanceField, "" , "", "ALL")


import arcpy

# Create a Describe object
#
desc = arcpy.Describe("risk_roads_buff.shp")

print desc.dataType



