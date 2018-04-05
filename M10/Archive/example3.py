import arcpy
from arcpy.sa import *
import numpy


arcpy.CheckOutExtension("Spatial")

a = SetNull(r"C:\temp\week10data\data\worldwidedata.gdb\prec_max", r"C:\temp\week10data\data\worldwidedata.gdb\prec_max", "Value < 0.00001")

a.save(r"C:\temp\week10data\data\worldwidedata.gdb\prec_max_nodata2")
