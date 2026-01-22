import arcpy
from arcpy.sa import *
from arcpy import env

env.workspace = r"C:\courses\spa\W8\Raster_Python\USA_Data.gdb"

highslopes = Con(Slope("elevation"),1,0, "Value > 20")

highslopes.save(r"highslopes")






