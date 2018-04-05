from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")

wsbInt = Int(wsbDEM)

wsbInt.save(r"C:\temp\spaLab\week10\wsb_dsm_int.img")
