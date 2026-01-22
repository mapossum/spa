import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"C:\temp\M8\Tydixton_Park_Data"
env.extent = "tydixton_watershed.shp"
env.overwriteOutput = True
env.cellSize = 50

datalist = arcpy.ListFeatureClasses("risk*")

for layer in datalist:
    outlayer = layer.replace(".shp", ".tif")

    #find the distance from the features in
    #layer for the watershed using Euc Dist tool

    #Run difference from 1000

    #Run outcon to set all negative values to 0

    #Finally save the output outlayer
    
    print(layer, outlayer)
