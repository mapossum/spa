from arcpy.sa import *
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

env.workspace = r"C:\temp\spaLab\week10\Tydixton_Park_Data"

env.extent = r"C:\temp\spaLab\week10\Tydixton_Park_Data\tydixton_watershed.shp"
env.cellSize = "100"

featureclasses = arcpy.ListFeatureClasses("risk*")

outputList = []
# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    print fc
    outEucDistance = EucDistance(fc)
    #outSub = type subtraction prob
    #outcon = type con statement
    
    outputname = fc.replace(".shp",".tif")
    outcon.save(outputname)
    outputList.append(outputname)

    #Raster(name1) + Raster(name2) + Raster(name3) ...

statement = "Raster('" + "') + Raster('".join(outputList) + "')"
outputRas = eval(statement)

outputRas.save("total.tif")



    



    

