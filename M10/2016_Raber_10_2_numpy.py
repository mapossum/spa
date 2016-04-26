import arcpy
from arcpy.sa import *
import numpy
import datetime
start = datetime.datetime.now()

arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"C:\temp\Tydixton_Park_Data"
arcpy.env.extent = r"C:\temp\Tydixton_Park_Data\tydixton_watershed.shp"
arcpy.env.cellsize = "50"
filefilter = "risk" + "*"
outputloc = "Testy.img"
arcpy.env.overwriteOutput = True

datasets = arcpy.ListFeatureClasses(filefilter)

firsttime = True
for dataset in datasets:
    outEucDistance = EucDistance(dataset, 1000)
    ed = arcpy.RasterToNumPyArray(outEucDistance, nodata_to_value = 1000)
    RiskDataset = 1000 - ed 
    if firsttime:
        totRas = RiskDataset
        firsttime = False
    else:
        totRas = totRas + RiskDataset

print "done"

finish = datetime.datetime.now()

print finish - start


