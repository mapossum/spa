import arcpy
from arcpy.sa import *
from arcpy import env

env.workspace = r"C:\courses\spa\W8\Raster_Python\USA_Data.gdb"
env.cellSize = "elevation"

outRaster = Con(IsNull("elevation"),0,"elevation")

outRaster.save("elevation_Water0")





