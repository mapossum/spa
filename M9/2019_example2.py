import arcpy
import numpy

arcpy.env.overwriteOutput = True
# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,25) #numpy.ones(25) * 5 #
myArray.shape = (5,5)

for row in range(0,5):
    for col in range(0,5):
        myArray[row,col] = row

print(myArray)

# Convert array to a geodatabase raster
point = arcpy.Point(50, 50)
myRaster = arcpy.NumPyArrayToRaster(myArray,lower_left_corner=point,x_cell_size=10)
myRaster.save(r"C:\temp\spaLab\week9\rowstrip.tif")

coord_sys = arcpy.SpatialReference(32145)

arcpy.DefineProjection_management(r"C:\temp\spaLab\week9\rowstrip.tif", coord_sys)
