import arcpy
from arcpy.sa import *
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
for dataset in datasets:
    #print dataset, dataset.replace(".shp", "_distance.img")
    outEucDistance = EucDistance(dataset, 1000)
    #Change everything from here down to numpy and then change result back to Raster
    RiskDataset = 1000 - outEucDistance
    FRiskDataset = Con(IsNull(RiskDataset), 0, RiskDataset)
    FRiskDataset.save(dataset.replace(".shp", "_risk.img"))
    
    riskRasters.append(dataset.replace(".shp", "_risk.img"))

statement = "Raster('" + ("') + Raster('").join(riskRasters) + "')"

arcpy.AddMessage( statement)
#set this equal to some variable
TotalRisk = eval(statement)

finish = datetime.datetime.now()
print finish - start

#save it to some location.
TotalRisk.save(outputloc)
