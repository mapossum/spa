import arcpy
import numpy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:/temp/myRandomRaster4.tif")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth


arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

arr[3,1] = 0

print arr

myRaster = arcpy.NumPyArrayToRaster(arr,lowerLeft,cellSize,value_to_nodata=0)
myRaster.save("C:/temp/myRandomRaster5.tif")
