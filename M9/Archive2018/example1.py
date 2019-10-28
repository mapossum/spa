from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
slopeWSB = Slope(wsbDEM)

slopeWSB.save(r"C:\temp\spaLab\week10\wsb_dsm_slope.tif")
