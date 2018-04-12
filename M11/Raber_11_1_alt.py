from arcpy.sa import *
from arcpy import env
import arcpy
import numpy as np
env.overwriteOutput = True

env.workspace = r"C:\temp\spaLab\week10\climatedata.gdb"

rasters = arcpy.ListRasters("temp*")

firsttime = True
listofArrays = []
for raster in rasters:
    print raster
    #convert raster into numpy array
    arr = arcpy.RasterToNumPyArray(raster,nodata_to_value=0)

    if firsttime:
        totarr = arr
    else:
        totarr = totarr + arr
    firsttime = False

print totarr

#divide totarr by 12 to get new anwser array
