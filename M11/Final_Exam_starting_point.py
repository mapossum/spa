
import numpy as np
import matplotlib.pyplot as plt
import arcpy
from arcpy.sa import *

#This is optional but will earn you more points
#def regress(inputfc, outputraster):
  #Build Function here:

    
# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


inMaskData = r"C:\temp\spaLab\elevClim.gdb\sample1"

#Get X data and create and array of the elevation values
elevpath = r"C:\temp\spaLab\elevClim.gdb\USA_elevation_meters"
outExtractByMask = ExtractByMask(elevpath, inMaskData)
xarr = arcpy.RasterToNumPyArray(outExtractByMask,nodata_to_value=-9999)
# get the extent and cell size like you did in lab 11 of outExtractByMask

x = xarr[np.where(xarr != -9999)]


#Get Y data and create and array of the temp values

#find the slope and the intercept

#find correlation coefficent

#create an array to save back out using formula on next line
#modeled temperature outputraster = slope(m)*xarr + intercept(b)

#use NumpyArraytoRaster to create a raster and use the extent and cell size of outExtractByMask
#save that raster out to file specified by the user.




