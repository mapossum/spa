import arcpy
from arcpy import env
from arcpy.sa import *
import numpy as np

arcpy.env.overwriteOutput = True

env.workspace = r"C:\courses\spa\W8\Raster_Python\USA_Data.gdb"

tempRaster = Raster("averge_summer_temperature")

lowerLeft = arcpy.Point(tempRaster.extent.XMin, tempRaster.extent.YMin)
cs = tempRaster.meanCellWidth

arr = arcpy.RasterToNumPyArray(tempRaster, nodata_to_value=-1000)

arr[0,0] = 40
ch = arcpy.NumPyArrayToRaster(arr, lower_left_corner=lowerLeft, x_cell_size=cs, y_cell_size=cs, value_to_nodata=-1000)
ch.save("change2")

##arr2 = ((arr / 10.0) * (9.0/5.0) + 32.0).astype(int)
##
##Temp_F = arcpy.NumPyArrayToRaster(arr2, lower_left_corner=lowerLeft, x_cell_size=cs-100, y_cell_size=cs-100, value_to_nodata=-148)
##
##Temp_F.save("averge_summer_temperature_f")
##
##print(arr2)
