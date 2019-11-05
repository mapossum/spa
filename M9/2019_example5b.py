import arcpy
import numpy

arcpy.env.overwriteOutput = True

for x in range(1,12):
    inRas = arcpy.Raster(r"C:\temp\spaLab\week9\climatedata.gdb\temp_" + str(x))
    inRas2 = arcpy.Raster(r"C:\temp\spaLab\week9\climatedata.gdb\precip_" + str(x))
    lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
    cellSize = inRas.meanCellWidth

    arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-1000)

    arr2 = (arr/100.0)*(9.0/5.0) + 32

    outarr = numpy.where(arr2 > 75, 1, 0)

    parr = arcpy.RasterToNumPyArray(inRas2,nodata_to_value=-1000)
    outarr2 = numpy.where(parr > 10000, 10, 0)

    finalarr = outarr + outarr2

    finalarr = numpy.where(arr == -1000, -1000, finalarr)

    myRaster = arcpy.NumPyArrayToRaster(finalarr,lowerLeft,cellSize,value_to_nodata=-1000)
    myRaster.save(r"C:\temp\spaLab\week9\climatedata.gdb\ft_threshold2_temp_precip_" + str(x))
    print("done with: " + str(x))

print("done")

