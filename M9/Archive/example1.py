import arcpy
from arcpy.sa import *
import numpy


arcpy.CheckOutExtension("Spatial")

outras = Plus(r"C:\temp\week10data\data\worldwidedata.gdb\prec_1",r"C:\temp\week10data\data\worldwidedata.gdb\prec_2")

arr = arcpy.RasterToNumPyArray(outras,nodata_to_value=0)
print arr.shape

#outras.save(r"C:\temp\week10data\data\worldwidedata.gdb\prec_add")
