import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"

tempRaster = arcpy.Raster("averge_summer_temperature")
precipRaster = arcpy.Raster("average_summer_precip")

outConTemp = Con(tempRaster, 1, 0, "VALUE > 260")
outConPrecip = Con(precipRaster, 10, 0, "VALUE > 125")

Climate = outConTemp + outConPrecip

Climate.save("climate")

print("All Done")

#env.extent = ""
#cellSize = 
#env.overwriteOutput = True




