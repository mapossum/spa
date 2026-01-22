from arcpy.sa import *
from arcpy import env
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
myextent = wsbDEM.extent
env.extent = myextent
env.cellSize = r"C:\temp\spaLab\week10\wsb_dsm.tif"


wsbMeters = wsbDEM * 0.3048

wsbMeters.save(r"C:\temp\spaLab\week10\wsb_dsm_meters.img")
