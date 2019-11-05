import arcpy
import numpy

arcpy.env.overwriteOutput = True

inputDataset = r"C:\temp\spaLab\week9\climatedata.gdb\temp_3"
outputDataset = r"C:\temp\spaLab\week9\climatedata.gdb\ft_temp_3"

inRas = arcpy.Raster(inputDataset)
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-10000)

arr2 = (arr/100.0)*(9.0/5.0) + 32

print(arr2)

myRaster = arcpy.NumPyArrayToRaster(arr2,lowerLeft,cellSize,value_to_nodata=-148.0)
myRaster.save(outputDataset)

dsc = arcpy.Describe(inputDataset)
coord_sys = dsc.spatialReference

arcpy.DefineProjection_management(outputDataset, coord_sys)

##print("done")
