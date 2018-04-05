from arcpy.sa import *
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
myextent = wsbDEM.extent
env.extent = myextent
env.cellSize = r"C:\temp\spaLab\week10\wsb_dsm.tif"

wsbCon = Con(wsbDEM > 40, 1,0)

wsbCon.save(r"C:\temp\spaLab\week10\wsb_dsm_con.img")
