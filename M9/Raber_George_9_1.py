import arcpy
import numpy

arcpy.env.overwriteOutput = True

for x in range(1,12):
    inRas = arcpy.Raster(r"C:\temp\spaLab\week9\climatedata.gdb\temp_" + str(x))
    lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
    cellSize = inRas.meanCellWidth

    arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=-1000)

    if (x == 1):
        total = arr * 1
    else:
        ### Calculate total each time through the loop
        total = ????????

    print("done with: " + str(x))

#### Reassign no data into the appropriate areas
    
#### Convert total back into a raster with the same dimentions

print("done")

