import arcpy
import numpy as np
from scipy.ndimage import gaussian_filter
import scipy

arcpy.env.overwriteOutput = True

inRas = arcpy.Raster(r"C:\temp\climatedata.gdb\temp_3")
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

kernelew = np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
kernelns = np.array([[1.,2.,1.],[0.,0.,0.],[-1.,-2.,-1.]])

outarrew = scipy.ndimage.filters.convolve(arr,kernelew) / (8 * 5000)
outarrns = scipy.ndimage.filters.convolve(arr,kernelns) / (8 * 5000)

fout = np.arctan(np.sqrt((outarrew * outarrew) + (outarrns * outarrns)))

myRaster = arcpy.NumPyArrayToRaster(outarr,lowerLeft,cellSize,value_to_nodata=0)
myRaster.save(r"C:\temp\climatedata.gdb\ft_temp_3_convolve_4")

print outarr

del myRaster
