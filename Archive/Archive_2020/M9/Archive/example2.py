import arcpy
from arcpy.sa import *
import numpy


arcpy.CheckOutExtension("Spatial")

arr1 = arcpy.RasterToNumPyArray(Raster(r"C:\temp\week10data\data\worldwidedata.gdb\prec_1"),nodata_to_value=0)
arr2 = arcpy.RasterToNumPyArray(Raster(r"C:\temp\week10data\data\worldwidedata.gdb\prec_7"),nodata_to_value=0)

outarr = numpy.maximum(arr1, arr2)

myRaster = arcpy.NumPyArrayToRaster(outarr)

myRaster.save(r"C:\temp\week10data\data\worldwidedata.gdb\prec_max")

#outras.save(r"C:\temp\week10data\data\worldwidedata.gdb\prec_add")
