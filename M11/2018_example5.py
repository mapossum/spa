import arcpy
import numpy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\spaLab\week10\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-1000)

arr2 = (arr/100.0)*(9.0/5.0) + 32

outarr = numpy.where(arr2 > 75, 1, 0)

myRaster = arcpy.NumPyArrayToRaster(outarr,lowerLeft,cellSize,value_to_nodata=14.0)
myRaster.save(r"C:\temp\spaLab\week10\climatedata.gdb\ft_threshold_temp_3")

print "done"

