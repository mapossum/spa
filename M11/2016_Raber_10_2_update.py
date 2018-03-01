import arcpy
from arcpy.sa import *
import datetime
start = datetime.datetime.now()

arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"C:\temp\Tydixton_Park_Data"
arcpy.env.extent = r"C:\temp\Tydixton_Park_Data\tydixton_watershed.shp"
arcpy.env.cellsize = "50"
filefilter = "risk" + "*"
outputloc = "Total.img"
arcpy.env.overwriteOutput = True

datasets = arcpy.ListFeatureClasses(filefilter)

riskRasters = []

totalRisk = 0
for dataset in datasets:
    #print dataset, dataset.replace(".shp", "_distance.img")
    outEucDistance = EucDistance(dataset, 1000)
    lowerLeft = arcpy.Point(outEucDistance.extent.XMin,outEucDistance.extent.YMin)
    #Change everything from here down to numpy and then change result back to Raster
    edarray = arcpy.RasterToNumPyArray(outEucDistance, nodata_to_value = 1000)
    RiskDataset = 1000 - edarray
    totalRisk = totalRisk + RiskDataset

finish = datetime.datetime.now()
print finish - start

myRaster = arcpy.NumPyArrayToRaster(totalRisk,lowerLeft,50,value_to_nodata=0)
myRaster.save("C:/temp/myRandomRaster6.tif")


