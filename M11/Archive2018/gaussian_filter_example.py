import arcpy
import numpy
from scipy.ndimage import gaussian_filter

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

outarr = gaussian_filter(arr, sigma=1)

myRaster = arcpy.NumPyArrayToRaster(outarr,lowerLeft,cellSize,value_to_nodata=0)
myRaster.save(r"C:\temp\climatedata.gdb\ft_temp_3_gaussian")

print outarr
