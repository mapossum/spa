import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"

myRaster = arcpy.Raster("averge_summer_temperature")

outCon = Con(myRaster, 1, 0, "VALUE > 260")

outCon.save("warm_places")

print("All Done")

#env.extent = ""
#cellSize = 
#env.overwriteOutput = True




