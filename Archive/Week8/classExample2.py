import arcpy
from arcpy.sa import *
from arcpy import env

env.workspace = r"C:\courses\spa\W8\Raster_Python\USA_Data.gdb"

hiprecip = Con("average_summer_precip",1,0,"Value > 140")
hitemp = Con("averge_summer_temperature",1,0,"Value > 265")

hotpwet = hiprecip + hitemp 

out_raster = Con(hotpwet,1,0,"Value = 2")

out_raster.save(r"hotandhumid")


