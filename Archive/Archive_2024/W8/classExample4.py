import arcpy
from arcpy.sa import *
from arcpy import env

env.workspace = r"C:\courses\spa\W8\Raster_Python\USA_Data.gdb"

#out_raster = RasterCalculator('"averge_summer_temperature" + "averge_winter_temperature"')
out_raster = Raster("averge_summer_temperature") + Raster("averge_winter_temperature") / 2

out_raster.save(r"averageTemp")






