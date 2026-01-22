import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"C:\temp\M8\Tydixton_Park_Data"
env.extent = "tydixton_watershed.shp"
env.overwriteOutput = True
env.cellSize = 50

datalist = arcpy.ListFeatureClasses("risk*")

outputList = []
for layer in datalist:

    outlayer = layer.replace(".shp", ".tif")

    outEucDistance = EucDistance(layer)
    diff = 1000 - outEucDistance
    outCon = Con(diff > 0, diff, 0)

    outCon.save(outlayer)
    #Build a list of each raster dataset to build the final command to run in EVAL
    outputList.append("Raster('" + outlayer + "')")
    print(layer, outlayer)


print(" ")
print(outputList)
print(" ")
print(" + ".join(outputList))
#Join them and eval to get final answer
finalRaster = eval(" + ".join(outputList))
finalRaster.save("final2.tif")

