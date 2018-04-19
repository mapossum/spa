import arcpy
import numpy as np
from scipy.ndimage import gaussian_filter
import scipy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-9999)

arr2 = np.where(arr > -9999, 1,0)

arr3 = np.where(scipy.ndimage.morphology.binary_dilation(arr2) == False, 0 ,1)

arr4 = np.where(arr3 != arr2, scipy.ndimage.filters.maximum_filter(arr, size=(3,3)), arr)


kernelew = np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
kernelns = np.array([[1.,2.,1.],[0.,0.,0.],[-1.,-2.,-1.]])

outarrew = scipy.ndimage.filters.convolve(arr4,kernelew) / (8.0 * 5000.0)
outarrns = scipy.ndimage.filters.convolve(arr4,kernelns) / (8.0 * 5000.0)

fout = np.arctan(np.sqrt((outarrew * outarrew) + (outarrns * outarrns))) * 57.2958

founter = np.where(arr2 == 1, fout,-9999)

myRaster = arcpy.NumPyArrayToRaster(founter,lowerLeft,cellSize) #,value_to_nodata=0)
myRaster.save(r"C:\temp\climatedata.gdb\ft_temp_3_convolve_slope")

print fout

del myRaster
