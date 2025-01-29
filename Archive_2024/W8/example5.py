import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"


elevRaster = arcpy.Raster("elevation")

outNull = IsNull(elevRaster)
replacedNoData = Con(outNull, 0, elevRaster)


replacedNoData.save("Elv_0")

