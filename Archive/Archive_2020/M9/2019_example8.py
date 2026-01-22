import arcpy
import numpy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\spaLab\week9\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=1000000)

arr2 = (arr/100.0)*(9.0/5.0) + 32

outarr = numpy.where(arr2 > 75, arr2, 0).astype(int)

myRaster = arcpy.NumPyArrayToRaster(outarr,lowerLeft,cellSize,value_to_nodata=18032)
myRaster.save(r"C:\temp\spaLab\week9\climatedata.gdb\ft_stop_temp_6")

print(outarr)



