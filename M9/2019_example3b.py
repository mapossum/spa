import arcpy
import numpy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\spaLab\week9\MyRandomRaster_Coords_Copy.tif\Band_4")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

#Turn no Data into 0
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

#Get Default NoData Values
arr = arcpy.RasterToNumPyArray(inRas)

#Turn no Data into -1
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-1)

#Array in Centimeters and we need to change it to inches
inarr = arr * 0.393701  #some function of arr

inarr = numpy.where(inarr < 0, 0, inarr)

print(inarr)

myRaster = arcpy.NumPyArrayToRaster(inarr,lowerLeft,cellSize, value_to_nodata=0)
myRaster.save(r"C:\temp\spaLab\week9\MyRandomRaster_Coords_Precip_inches.tif")

