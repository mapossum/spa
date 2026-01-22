import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"

tempRaster = arcpy.Raster("averge_summer_temperature")
elevRaster = arcpy.Raster("Elv_0")

env.extent = tempRaster
cellSize = tempRaster

outConTemp = Con(tempRaster, 1, 0, "VALUE > 260")
outConelev = Con(elevRaster, 10, 0, "VALUE > 530")

Climate = eval("outConTemp + outConelev")

Climate.save("temp_elev_3")

print("All Done")


#cellSize = 
#env.overwriteOutput = True




