import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = arcpy.GetParameterAsText(0) #r"C:\temp\Tydixton_Park_Data"
arcpy.env.extent = arcpy.GetParameterAsText(1) #r"C:\temp\Tydixton_Park_Data\tydixton_watershed.shp"
arcpy.env.cellsize = arcpy.GetParameterAsText(2) #"50"
filefilter = arcpy.GetParameterAsText(3) + "*"
outputloc = arcpy.GetParameterAsText(4)
arcpy.env.overwriteOutput = True

datasets = arcpy.ListFeatureClasses(filefilter)

riskRasters = []
for dataset in datasets:
    #print dataset, dataset.replace(".shp", "_distance.img")
    outEucDistance = EucDistance(dataset, 1000)
    #outEucDistance.save(dataset.replace(".shp", "_distance.img"))
    RiskDataset = 1000 - outEucDistance
    FRiskDataset = Con(IsNull(RiskDataset), 0, RiskDataset)
    FRiskDataset.save(dataset.replace(".shp", "_risk.img"))
    
    riskRasters.append(dataset.replace(".shp", "_risk.img"))

statement = "Raster('" + ("') + Raster('").join(riskRasters) + "')"

arcpy.AddMessage( statement)
#set this equal to some variable
TotalRisk = eval(statement)

#save it to some location.
TotalRisk.save(outputloc)
