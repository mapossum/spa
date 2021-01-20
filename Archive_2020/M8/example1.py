import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"C:\temp\M8\Tydixton_Park_Data"
env.extent = "tydixton_watershed.shp"
env.overwriteOutput = True

outEucDistance = EucDistance("risk_urban_areas.shp", "", 50)
diff = 1000 - outEucDistance
outCon = Con(diff > 0, diff, 0)

outCon.save("conditional.tif")
