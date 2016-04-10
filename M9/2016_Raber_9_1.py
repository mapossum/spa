import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")


arcpy.env.workspace = r"D:\temp\M9"
arcpy.env.extent = r"D:\temp\M9\tydixton_watershed.shp"
arcpy.env.cellsize = "50"
arcpy.env.overwriteOutput = True


datasets = arcpy.ListFeatureClasses("risk*")

riskRasters = []
for dataset in datasets:
    print dataset, dataset.replace(".shp", "_distance.img")
    outEucDistance = EucDistance(dataset, 1000)
    #outEucDistance.save(dataset.replace(".shp", "_distance.img"))
    RiskDataset = 1000 - outEucDistance
    FRiskDataset = Con(IsNull(RiskDataset), 0, RiskDataset)
    FRiskDataset.save(dataset.replace(".shp", "_risk.img"))
    riskRasters.append(dataset.replace(".shp", "_risk.img"))

statement = "Raster('" + ("') + Raster('").join(riskRasters) + "')"

#set this equal to some variable
eval(statement)

#save it to some location.
