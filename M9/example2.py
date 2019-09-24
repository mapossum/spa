from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
slopeWSB = Slope(wsbDEM)

total = slopeWSB + wsbDEM

total.save(r"C:\temp\spaLab\week10\wsb_dsm_total.tif")
