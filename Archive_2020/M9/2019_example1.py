import arcpy
import numpy

arcpy.env.overwriteOutput = True
# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,100) #numpy.ones(25) * 5 #
myArray.shape = (5,5,4)
print(myArray)

## Convert array to a geodatabase raster
point = arcpy.Point(493907, 195476)
myRaster = arcpy.NumPyArrayToRaster(myArray,point,100)
myRaster.save(r"C:\temp\spaLab\week9\MyRandomRaster_Coords3.tif")

#dsc = arcpy.Describe(r"C:\temp\spaLab\week9\climatedata.gdb\usa_states")
#coord_sys = dsc.spatialReference

coord_sys = arcpy.SpatialReference(32145)

arcpy.DefineProjection_management(r"C:\temp\spaLab\week9\MyRandomRaster_Coords3.tif", coord_sys)
