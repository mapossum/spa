import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")


outCon = Con(Raster(r"D:\temp\M9\wsb_dsm.tif") > 46, 1, 0)

outCon.save(r"D:\temp\M9\wsb_dsm_con.tif")

print "done!"

