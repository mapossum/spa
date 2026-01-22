from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")
wsbDEM = Raster(r"C:\temp\spaLab\week10\wsb_dsm.tif")

neighborhood = NbrRectangle(10, 10, "CELL")
outFocalStatistics = FocalStatistics(wsbDEM, neighborhood, "MEAN")

total = outFocalStatistics - wsbDEM 

total.save(r"C:\temp\spaLab\week10\wsb_dsm_edge_10.tif")
