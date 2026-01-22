import arcpy
from arcpy import env
from arcpy.sa import *
import numpy as np

arcpy.env.overwriteOutput = True

env.workspace = r"G:\courses\spa\W9\Raster_Python\USA_Data.gdb"

tempRaster = arcpy.Raster("averge_summer_temperature")

lowerLeft = arcpy.Point(tempRaster.extent.XMin-10000, tempRaster.extent.YMin-1000)
cs = tempRaster.meanCellWidth

arr = arcpy.RasterToNumPyArray(tempRaster, nodata_to_value=-1000)

arr2 = ((arr / 10.0) * (9.0/5.0) + 32.0).astype(int)

Temp_F = arcpy.NumPyArrayToRaster(arr2, lower_left_corner=lowerLeft, x_cell_size=cs-100, y_cell_size=cs-100, value_to_nodata=-148)

Temp_F.save("averge_summer_temperature_f_wrong")

print(arr2)





