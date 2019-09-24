from arcpy.sa import *
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

env.workspace = r"C:\temp\spaLab\week10\Tydixton_Park_Data"

env.extent = r"C:\temp\spaLab\week10\Tydixton_Park_Data\tydixton_watershed.shp"
env.cellSize = "100"

featureclasses = arcpy.ListFeatureClasses("risk*")

firstTime = True
# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    print fc
    outEucDistance = EucDistance(fc)
    if (firstTime == False):
        outDistTot = outEucDistpre + outEucDistance
    else:
        outDistTot = outEucDistance
        firstTime = False
    outEucDistpre = outDistTot

outDistTot.save("total_test.tif")


    



    

