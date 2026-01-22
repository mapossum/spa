import arcpy
import numpy as np
from scipy.ndimage import gaussian_filter
import scipy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-99999)

arr2 = np.where(arr > -9999, 1,0)

arr3 = np.where(scipy.ndimage.morphology.binary_dilation(arr2) == False, 0 ,1)

arr4 = np.where(arr3 != arr2, scipy.ndimage.filters.maximum_filter(arr, size=(3,3)), arr)

myRaster = arcpy.NumPyArrayToRaster(arr4,lowerLeft,cellSize ,value_to_nodata=-99999)
myRaster.save(r"C:\temp\climatedata.gdb\ft_temp_3_mask")

print arr4

del myRaster
