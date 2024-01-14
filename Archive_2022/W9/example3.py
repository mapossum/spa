import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"

tempRaster = arcpy.Raster("averge_summer_temperature")
elevRaster = arcpy.Raster("elevation")

env.extent = tempRaster
cellSize = tempRaster

outConTemp = Con(tempRaster, 1, 0, "VALUE > 260")
outConelev = Con(elevRaster, 10, 0, "VALUE > 530")

Climate = outConTemp + outConelev

Climate.save("temp_elev_2")

print("All Done")


#cellSize = 
#env.overwriteOutput = True




